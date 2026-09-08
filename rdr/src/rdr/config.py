from __future__ import annotations

import json
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
    enabled: bool
    tokens: tuple[str, ...]

    @classmethod
    def load(cls, path: str | Path) -> "AccessConfig":
        value = _load_object(path)
        enabled = value.get("enabled")
        if not isinstance(enabled, bool):
            raise ConfigError(f"config {path} requires boolean 'enabled'")
        return cls(enabled=enabled, tokens=_tokens(value, path=path))


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
    enabled = all(config.enabled for config in configs) if configs else True
    token_sources: list[Iterable[str]] = [
        config.tokens for config in configs
    ] + [extra_tokens]
    for tokens in token_sources:
        for token in tokens:
            if token not in seen:
                merged_tokens.append(token)
                seen.add(token)
    return AccessConfig(enabled=enabled, tokens=tuple(merged_tokens))
