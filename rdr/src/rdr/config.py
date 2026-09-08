from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


class ConfigError(RuntimeError):
    pass


def _load_object(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    try:
        raw = config_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ConfigError(f"cannot read config {config_path}: {exc}") from exc
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

    The current schema is tokens-only. Legacy files may still carry an
    ``enabled`` key. ``enabled: true`` is ignored, while ``enabled: false``
    is conservatively treated as an empty token set so upgrading cannot turn
    an explicitly disabled host into an authenticated one. New configuration
    must use ``tokens: []`` for the deny-all state and ``rdr server stop`` to
    stop the runtime process.
    """

    tokens: tuple[str, ...]

    @classmethod
    def load(cls, path: str | Path) -> "AccessConfig":
        value = _load_object(path)
        tokens = _tokens(value, path=path)
        legacy_enabled = value.get("enabled")
        if legacy_enabled is False:
            return cls(tokens=())
        return cls(tokens=tokens)


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


def resolve_access_token(access_config_path: str | Path) -> str:
    """Token used by client-side connections: RDR_TOKEN env wins, then the
    first token of the access config file."""
    env_token = os.environ.get("RDR_TOKEN", "").strip()
    if env_token:
        return env_token
    path = Path(access_config_path)
    config = AccessConfig.load(path)
    if not config.tokens:
        raise ConfigError(f"access config {path} contains no token")
    return config.tokens[0]
