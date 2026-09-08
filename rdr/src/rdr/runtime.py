from __future__ import annotations

import asyncio
import hmac
import logging
from collections.abc import Iterable

from .connection import ClientConnection
from .terminal import TerminalHandle

logger = logging.getLogger(__name__)


class RDRServer:
    def __init__(self, host: str, port: int, tokens: Iterable[str]) -> None:
        self.host = host
        self.port = port
        self.tokens = tuple(tokens)
        self.listener: asyncio.AbstractServer | None = None
        self.connections: set[ClientConnection] = set()
        self.terminals: dict[str, TerminalHandle] = {}
        self._terminal_watchers: set[asyncio.Task[None]] = set()
        self.enabled = False
        self._state_lock = asyncio.Lock()

    def authenticate(self, token: str) -> bool:
        return any(hmac.compare_digest(token, candidate) for candidate in self.tokens)

    async def set_tokens(self, tokens: Iterable[str]) -> None:
        next_tokens = tuple(tokens)
        revoked = set(self.tokens) - set(next_tokens)
        self.tokens = next_tokens

        if revoked:
            # Preserve the previous security boundary: token revocation ends
            # work created under the old access state, including detached PTYs.
            if self.connections:
                await asyncio.gather(
                    *(connection.close() for connection in list(self.connections)),
                    return_exceptions=True,
                )
            await self.close_terminals()

    def register_terminal(self, handle: TerminalHandle) -> None:
        terminal_id = handle.terminal_id
        if terminal_id in self.terminals:
            raise RuntimeError(f"duplicate terminal_id: {terminal_id}")
        self.terminals[terminal_id] = handle

        async def forget_when_done() -> None:
            if handle.wait_task is not None:
                await asyncio.gather(handle.wait_task, return_exceptions=True)
            if self.terminals.get(terminal_id) is handle:
                self.terminals.pop(terminal_id, None)

        watcher = asyncio.create_task(
            forget_when_done(), name=f"rdr-terminal-{terminal_id}"
        )
        self._terminal_watchers.add(watcher)
        watcher.add_done_callback(self._terminal_watchers.discard)

    def get_terminal(self, terminal_id: str) -> TerminalHandle | None:
        return self.terminals.get(terminal_id)

    async def close_terminal(self, terminal_id: str) -> bool:
        handle = self.terminals.pop(terminal_id, None)
        if handle is None:
            return False
        await handle.close()
        return True

    async def close_terminals(self) -> None:
        handles = list(self.terminals.values())
        self.terminals.clear()
        if handles:
            await asyncio.gather(
                *(handle.close() for handle in handles),
                return_exceptions=True,
            )

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

            # Server shutdown is stronger than transport disconnect: all
            # runtime-owned stateful sessions are terminated.
            await asyncio.gather(
                *(connection.close() for connection in list(self.connections)),
                return_exceptions=True,
            )
            await self.close_terminals()
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
