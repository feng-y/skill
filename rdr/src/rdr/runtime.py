from __future__ import annotations

import asyncio
import hmac
import logging
from collections.abc import Iterable

from .connection import ClientConnection

logger = logging.getLogger(__name__)


class RDRServer:
    def __init__(self, host: str, port: int, tokens: Iterable[str]) -> None:
        self.host = host
        self.port = port
        self.tokens = tuple(tokens)
        self.listener: asyncio.AbstractServer | None = None
        self.connections: set[ClientConnection] = set()
        self.enabled = False
        self._state_lock = asyncio.Lock()

    def authenticate(self, token: str) -> bool:
        return any(hmac.compare_digest(token, candidate) for candidate in self.tokens)

    async def set_access(self, enabled: bool, tokens: Iterable[str]) -> None:
        next_tokens = tuple(tokens)
        revoked = set(self.tokens) - set(next_tokens)
        self.tokens = next_tokens

        if revoked and self.connections:
            await asyncio.gather(
                *(connection.close() for connection in list(self.connections)),
                return_exceptions=True,
            )
        await self.set_enabled(enabled)

    async def set_enabled(self, enabled: bool) -> None:
        async with self._state_lock:
            if enabled == self.enabled:
                return

            if enabled:
                self.listener = await asyncio.start_server(self._accept, self.host, self.port)
                self.enabled = True
                sockets = self.listener.sockets or []
                bound = ", ".join(str(sock.getsockname()) for sock in sockets)
                logger.info("RDR enabled on %s", bound)
                return

            self.enabled = False
            listener = self.listener
            self.listener = None
            if listener is not None:
                listener.close()

            # Server.wait_closed() can wait for active handlers. End diagnostic
            # sessions before waiting so an access switch cannot deadlock.
            await asyncio.gather(
                *(connection.close() for connection in list(self.connections)),
                return_exceptions=True,
            )
            if listener is not None:
                await listener.wait_closed()
            logger.info("RDR disabled")

    async def _accept(
        self,
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        if not self.enabled:
            writer.close()
            await writer.wait_closed()
            return
        connection = ClientConnection(self, reader, writer)
        self.connections.add(connection)
        await connection.run()

    async def close(self) -> None:
        await self.set_enabled(False)
