from __future__ import annotations

import asyncio
import logging
from pathlib import Path
from typing import Awaitable, Callable

from .config import AccessConfig, ConfigError, merge_access_configs

logger = logging.getLogger(__name__)


class AccessConfigWatcher:
    """Watches host-local and optional global access configuration files.

    The local file is required at startup. The global file is optional until it
    has been read successfully once. After that, a transient read or mount
    failure keeps the last-known global policy instead of silently reopening
    access.
    """

    def __init__(
        self,
        local_path: str | Path,
        global_path: str | Path | None = None,
        *,
        poll_seconds: float = 30.0,
    ) -> None:
        if poll_seconds <= 0:
            raise ValueError("access poll interval must be positive")
        self.local_path = Path(local_path)
        self.global_path = Path(global_path) if global_path else None
        self.poll_seconds = poll_seconds
        self._local: AccessConfig | None = None
        self._global: AccessConfig | None = None
        self._global_seen = False

    def load_initial(self) -> AccessConfig:
        self._local = AccessConfig.load(self.local_path)
        self._refresh_global(initial=True)
        return merge_access_configs(self._local, self._global)

    def _refresh_local(self) -> None:
        try:
            self._local = AccessConfig.load(self.local_path)
        except ConfigError:
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
        if self._local is None:
            raise RuntimeError("access config watcher has not been initialized")
        self._refresh_local()
        self._refresh_global()
        return merge_access_configs(self._local, self._global)

    async def watch(
        self,
        apply: Callable[[AccessConfig], Awaitable[None]],
        *,
        stop_event: asyncio.Event,
    ) -> None:
        current = merge_access_configs(self._local, self._global) if self._local else None
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
