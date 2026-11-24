from __future__ import annotations

import fcntl
import json
import os
import re
import stat
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


class ConfigError(RuntimeError):
    pass


_INSTALLER_CONFIG = re.compile(
    r'''^[ \t]*cat >"\$config_tmp" <<'JSON'\r?\n(.*?)^JSON[ \t]*\r?$''',
    re.MULTILINE | re.DOTALL,
)


def _load_object(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    try:
        raw = config_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(f"cannot read config {config_path}: {exc}") from exc
    except UnicodeError as exc:
        raise ConfigError(f"config {config_path} is not UTF-8 text") from exc
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ConfigError(f"config {config_path} is not valid JSON") from exc
    if not isinstance(value, dict):
        raise ConfigError(f"config {config_path} must contain a JSON object")
    return value


def _tokens(value: dict[str, Any], *, path: str | Path) -> tuple[str, ...]:
    raw = value.get("tokens")
    if not isinstance(raw, list):
        raise ConfigError(f"config {path} requires array 'tokens'")

    tokens: list[str] = []
    seen: set[str] = set()
    for index, token in enumerate(raw):
        if not isinstance(token, str) or not token.strip():
            raise ConfigError(
                f"config {path} requires non-empty string tokens[{index}]"
            )
        if token not in seen:
            tokens.append(token)
            seen.add(token)
    return tuple(tokens)


@dataclass(frozen=True)
class AccessConfig:
    """Token list from an access config file.

    The schema is tokens-only. Historical files may still contain an
    ``enabled`` key, but it has no runtime meaning and is ignored regardless
    of value. Use ``tokens: []`` for an empty credential set and
    ``rdr server stop`` to stop the runtime process.
    """

    tokens: tuple[str, ...]

    @classmethod
    def load(cls, path: str | Path) -> "AccessConfig":
        value = _load_object(path)
        return cls(tokens=_tokens(value, path=path))


def import_installer_token(script: str, path: Path) -> None:
    blocks = _INSTALLER_CONFIG.findall(script)
    if len(blocks) != 1:
        raise ConfigError("expected one access config block in the RDR installer")
    try:
        source = json.loads(blocks[0])
    except json.JSONDecodeError as exc:
        raise ConfigError("RDR installer access config is not valid JSON") from exc
    if not isinstance(source, dict):
        raise ConfigError("RDR installer access config must contain a JSON object")
    values = source.get("tokens")
    if not isinstance(values, list) or len(values) != 1:
        raise ConfigError("expected one token in the RDR installer")
    (token,) = _tokens(source, path="in RDR installer")

    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
    try:
        fcntl.flock(directory, fcntl.LOCK_EX)
        try:
            existing = path.lstat()
        except FileNotFoundError:
            existing = None
        if existing is not None and not stat.S_ISREG(existing.st_mode):
            raise ConfigError(f"config {path} must be a regular file")
        config = _load_object(path) if existing is not None else {}
        previous = _tokens(config, path=path) if "tokens" in config else ()
        config["tokens"] = [token, *(value for value in previous if value != token)]
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as output:
            temporary = Path(output.name)
            try:
                os.fchmod(output.fileno(), 0o600)
                json.dump(config, output, indent=2)
                output.write("\n")
                output.flush()
                if existing is not None:
                    current = os.fstat(output.fileno())
                    if (current.st_uid, current.st_gid) != (existing.st_uid, existing.st_gid):
                        os.fchown(output.fileno(), existing.st_uid, existing.st_gid)
                os.fsync(output.fileno())
                os.replace(temporary, path)
            finally:
                temporary.unlink(missing_ok=True)
    finally:
        os.close(directory)


def merge_access_configs(
    local: AccessConfig | None,
    global_config: AccessConfig | None = None,
    *,
    extra_tokens: Iterable[str] = (),
) -> AccessConfig:
    configs = [
        config for config in (local, global_config) if config is not None
    ]
    merged_tokens: list[str] = []
    seen: set[str] = set()
    token_sources: list[Iterable[str]] = [
        config.tokens for config in configs
    ] + [extra_tokens]
    for tokens in token_sources:
        for token in tokens:
            if token not in seen:
                merged_tokens.append(token)
                seen.add(token)
    return AccessConfig(tokens=tuple(merged_tokens))


def resolve_access_token(access_config_path: str | Path, *, config_only: bool = False) -> str:
    if not config_only:
        env_token = os.environ.get("RDR_TOKEN", "").strip()
        if env_token:
            return env_token
    path = Path(access_config_path)
    config = AccessConfig.load(path)
    if not config.tokens:
        raise ConfigError(f"access config {path} contains no token")
    return config.tokens[0]
