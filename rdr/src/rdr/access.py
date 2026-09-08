from __future__ import annotations

import asyncio
import logging
from pathlib import Path
from typing import Awaitable, Callable

from .config import AccessConfig, ConfigError, merge_access_configs

logger = logging.getLogger(__name__)


class AccessConfigWatcher:
    """Watches host-local and optional global access configuration files.

    The local file is required at startup unless ``static_tokens`` is
    non-empty (tokens supplied out of band, e.g. from the environment), in
    which case a missing local file only means "no file policy yet". A local
    file that exists but is invalid is always a startup failure. The global
    file is optional until it has been read successfully once. After that, a
    transient read or mount failure keeps the last-known global policy
    instead of silently reopening access.
    """

    def __init__(
        self,
        local_path: str | Path,
        global_path: str | Path | None = None,
        *,
        poll_seconds: float = 30.0,
        static_tokens: tuple[str, ...] = (),
    ) -> None:
        if poll_seconds <= 0:
            raise ValueError("access poll interval must be positive")
        self.local_path = Path(local_path)
        self.global_path = Path(global_path) if global_path else None
        self.poll_seconds = poll_seconds
        self.static_tokens = tuple(static_tokens)
        self._local: AccessConfig | None = None
        self._global: AccessConfig | None = None
        self._global_seen = False

    def load_initial(self) -> AccessConfig:
        try:
            self._local = AccessConfig.load(self.local_path)
        except ConfigError:
            if not self.static_tokens or self.local_path.exists():
                raise
            logger.warning(
                "local RDR access config %s is missing; starting with "
                "static env tokens only",
                self.local_path,
            )
        self._refresh_global(initial=True)
        return self._merged()

    def _merged(self) -> AccessConfig:
        if self._local is None and not self.static_tokens:
            raise RuntimeError("access config watcher has not been initialized")
        return merge_access_configs(
            self._local,
            self._global,
            extra_tokens=self.static_tokens,
        )

    def _refresh_local(self) -> None:
        try:
            self._local = AccessConfig.load(self.local_path)
        except ConfigError:
            if not self.local_path.exists() and self.static_tokens:
                return
            logger.exception(
                "failed to reload local RDR access config; keeping last-known state"
            )

    def _refresh_global(self, *, initial: bool = False) -> None:
        if self.global_path is None:
            self._global = None
            return

        try:
            if not self.global_path.exists():
                if not self._global_seen:
                    self._global = None
                return
            self._global = AccessConfig.load(self.global_path)
            self._global_seen = True
        except ConfigError:
            if initial and not self._global_seen:
                raise
            logger.exception(
                "failed to reload global RDR access config; keeping last-known state"
            )

    def read_policy(self) -> AccessConfig:
        self._refresh_local()
        self._refresh_global()
        return self._merged()

    async def watch(
        self,
        apply: Callable[[AccessConfig], Awaitable[None]],
        *,
        stop_event: asyncio.Event,
    ) -> None:
        current = self._merged()
        while not stop_event.is_set():
            policy = await asyncio.to_thread(self.read_policy)
            if policy != current:
                try:
                    await apply(policy)
                except asyncio.CancelledError:
                    raise
                except Exception:
                    logger.exception(
                        "failed to apply RDR access policy; retrying on next poll"
                    )
                else:
                    current = policy

            try:
                await asyncio.wait_for(stop_event.wait(), timeout=self.poll_seconds)
            except asyncio.TimeoutError:
                pass
