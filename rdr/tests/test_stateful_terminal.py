from __future__ import annotations

import asyncio
import os
import unittest

from rdr.client import RDRClient, RDRClientError, RemoteTerminal
from rdr.server import RDRServer


@unittest.skipUnless(os.name == "posix", "PTY requires POSIX")
class StatefulTerminalTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.server = RDRServer("127.0.0.1", 0, ("secret", "rotated"))
        await self.server.set_enabled(True)
        sock = self.server.listener.sockets[0]
        self.port = sock.getsockname()[1]
        self.clients: list[RDRClient] = []

    async def asyncTearDown(self) -> None:
        for client in self.clients:
            await client.close()
        await self.server.close()

    async def connect(self, token: str = "secret") -> RDRClient:
        client = RDRClient("127.0.0.1", self.port, token)
        await client.connect()
        self.clients.append(client)
        return client

    async def read_until(
        self,
        terminal: RemoteTerminal,
        marker: bytes,
        *,
        timeout: float = 3.0,
    ) -> bytes:
        output = bytearray()

        async def collect() -> bytes:
            while marker not in output:
                header, payload = await terminal.read()
                frame_type = header.get("type")
                if frame_type == "terminal.output":
                    output.extend(payload)
                    continue
                if frame_type == "terminal.exit":
                    self.fail(f"terminal exited before {marker!r}: {bytes(output)!r}")
                if frame_type in {"terminal.error", "connection.closed"}:
                    self.fail(header.get("error", "terminal failed"))
            return bytes(output)

        return await asyncio.wait_for(collect(), timeout=timeout)

    async def wait_detached(self, terminal_id: str) -> None:
        for _ in range(100):
            handle = self.server.get_terminal(terminal_id)
            if handle is not None and handle.sender is None:
                return
            await asyncio.sleep(0.01)
        self.fail(f"terminal did not detach: {terminal_id}")

    async def test_terminal_state_survives_transport_disconnect(self) -> None:
        client = await self.connect()
        terminal_id = "stateful-shell"
        command = (
            "value=initial; "
            "while IFS= read -r line; do "
            "if [ \"$line\" = get ]; then "
            "printf 'value:%s\\n' \"$value\"; "
            "else value=\"$line\"; printf 'set:%s\\n' \"$value\"; fi; "
            "done"
        )
        terminal = await client.open_terminal(
            command=command,
            terminal_id=terminal_id,
        )
        await terminal.write(b"hello\n")
        await self.read_until(terminal, b"set:hello")

        await client.close()
        await self.wait_detached(terminal_id)
        self.assertIn(terminal_id, self.server.terminals)

        reconnected = await self.connect()
        attached = await reconnected.attach_terminal(terminal_id)
        self.assertEqual(attached.terminal_id, terminal_id)
        await attached.write(b"get\n")
        output = await self.read_until(attached, b"value:hello")
        self.assertIn(b"value:hello", output)

        await attached.close()
        for _ in range(100):
            if terminal_id not in self.server.terminals:
                break
            await asyncio.sleep(0.01)
        self.assertNotIn(terminal_id, self.server.terminals)

    async def test_detached_output_is_replayed_on_attach(self) -> None:
        client = await self.connect()
        terminal_id = "buffered-shell"
        await client.open_terminal(
            command="sleep 0.2; printf 'buffered-marker\\n'; sleep 30",
            terminal_id=terminal_id,
        )
        await client.close()
        await self.wait_detached(terminal_id)
        await asyncio.sleep(0.35)

        reconnected = await self.connect()
        attached = await reconnected.attach_terminal(terminal_id)
        self.assertGreater(attached.replayed_bytes, 0)
        output = await self.read_until(attached, b"buffered-marker")
        self.assertIn(b"buffered-marker", output)
        await attached.close()

    async def test_explicit_detach_keeps_terminal_alive(self) -> None:
        client = await self.connect()
        terminal = await client.open_terminal(
            command="sleep 30",
            terminal_id="explicit-detach",
        )
        await terminal.detach()
        handle = self.server.get_terminal("explicit-detach")
        self.assertIsNotNone(handle)
        assert handle is not None
        self.assertIsNone(handle.sender)

        attached = await client.attach_terminal("explicit-detach")
        await attached.close()

    async def test_attached_terminal_rejects_second_connection(self) -> None:
        first = await self.connect()
        terminal = await first.open_terminal(
            command="sleep 30",
            terminal_id="single-owner",
        )
        second = await self.connect()
        with self.assertRaisesRegex(RDRClientError, "already attached"):
            await second.attach_terminal("single-owner")
        await terminal.close()

    async def test_token_revocation_terminates_detached_terminal(self) -> None:
        client = await self.connect("secret")
        terminal_id = "revoked-terminal"
        await client.open_terminal(command="sleep 30", terminal_id=terminal_id)
        await client.close()
        await self.wait_detached(terminal_id)

        await self.server.set_tokens(("rotated",))
        for _ in range(100):
            if terminal_id not in self.server.terminals:
                break
            await asyncio.sleep(0.01)
        self.assertNotIn(terminal_id, self.server.terminals)


if __name__ == "__main__":
    unittest.main()
