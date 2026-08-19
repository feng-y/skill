from __future__ import annotations

import asyncio
import os
import tempfile
import unittest
from pathlib import Path

from rdr.client import RDRClient, RDRClientError
from rdr.server import RDRServer


class RuntimeTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.server = RDRServer("127.0.0.1", 0, ("secret", "rotated"))
        await self.server.set_enabled(True)
        sock = self.server.listener.sockets[0]
        self.port = sock.getsockname()[1]

    async def asyncTearDown(self) -> None:
        await self.server.close()

    async def connect(self, token: str = "secret") -> RDRClient:
        client = RDRClient("127.0.0.1", self.port, token)
        await client.connect()
        self.addAsyncCleanup(client.close)
        return client

    async def test_invalid_token_rejected(self) -> None:
        client = RDRClient("127.0.0.1", self.port, "wrong")
        with self.assertRaises(RDRClientError):
            await client.connect()

    async def test_any_configured_token_is_accepted(self) -> None:
        client = await self.connect("rotated")
        identity = await client.get_identity()
        self.assertIn("hostname", identity)

    async def test_removing_token_closes_active_sessions(self) -> None:
        await self.connect("secret")
        self.assertTrue(self.server.connections)
        await self.server.set_access(True, ("rotated",))
        self.assertFalse(self.server.connections)

    async def test_exec_streams_and_returns_exit(self) -> None:
        client = await self.connect()
        streamed = bytearray()
        result = await client.exec(
            "printf hello; printf error >&2; exit 7",
            on_stdout=streamed.extend,
        )
        self.assertEqual(result["exit_code"], 7)
        self.assertEqual(result["stdout"], b"hello")
        self.assertEqual(result["stderr"], b"error")
        self.assertEqual(streamed, b"hello")

    async def test_exec_timeout(self) -> None:
        client = await self.connect()
        result = await client.exec("sleep 5", timeout=0.1)
        self.assertTrue(result["timed_out"])
        self.assertNotEqual(result["exit_code"], 0)

    @unittest.skipUnless(os.name == "posix", "PTY requires POSIX")
    async def test_pty_is_interactive(self) -> None:
        client = await self.connect()
        terminal = await client.open_terminal(command="read x; printf 'got:%s\\n' \"$x\"")
        try:
            await terminal.write(b"hello\n")
            output = bytearray()
            while True:
                header, payload = await asyncio.wait_for(terminal.read(), timeout=3)
                if header.get("type") == "terminal.output":
                    output.extend(payload)
                elif header.get("type") == "terminal.exit":
                    break
            self.assertIn(b"got:hello", output)
        finally:
            await terminal.close()

    @unittest.skipUnless(os.name == "posix", "PTY requires POSIX")
    async def test_pty_has_controlling_terminal_and_keeps_tail_output(self) -> None:
        client = await self.connect()
        terminal = await client.open_terminal(
            command="tty; printf 'tail-marker\\n'"
        )
        output = bytearray()
        while True:
            header, payload = await asyncio.wait_for(terminal.read(), timeout=3)
            if header.get("type") == "terminal.output":
                output.extend(payload)
            elif header.get("type") == "terminal.exit":
                break

        self.assertIn(b"/dev/pts/", output)
        self.assertIn(b"tail-marker", output)

    async def test_client_cancellation_stops_remote_exec(self) -> None:
        client = await self.connect()
        task = asyncio.create_task(client.exec("sleep 30"))
        await asyncio.sleep(0.1)
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task

        for _ in range(40):
            connection = next(iter(self.server.connections))
            if not connection.execs:
                break
            await asyncio.sleep(0.05)
        self.assertFalse(connection.execs)

    async def test_file_upload_and_download(self) -> None:
        client = await self.connect()
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            local = root / "local.bin"
            remote = root / "remote.bin"
            copy = root / "copy.bin"
            payload = os.urandom(600_000)
            local.write_bytes(payload)

            uploaded = await client.upload(local, str(remote))
            self.assertEqual(uploaded, len(payload))
            self.assertEqual(remote.read_bytes(), payload)

            downloaded = await client.download(str(remote), copy)
            self.assertEqual(downloaded, len(payload))
            self.assertEqual(copy.read_bytes(), payload)

    async def test_disable_closes_listener(self) -> None:
        await self.server.set_enabled(False)
        with self.assertRaises(OSError):
            await asyncio.open_connection("127.0.0.1", self.port)


if __name__ == "__main__":
    unittest.main()
