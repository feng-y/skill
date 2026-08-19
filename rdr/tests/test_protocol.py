from __future__ import annotations

import asyncio
import unittest

from rdr.protocol import read_frame, write_frame


class ProtocolTest(unittest.IsolatedAsyncioTestCase):
    async def test_round_trip_binary_payload(self) -> None:
        received = asyncio.Future()

        async def handler(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
            try:
                received.set_result(await read_frame(reader))
            finally:
                writer.close()
                await writer.wait_closed()

        server = await asyncio.start_server(handler, "127.0.0.1", 0)
        host, port = server.sockets[0].getsockname()[:2]
        reader, writer = await asyncio.open_connection(host, port)
        del reader
        try:
            await write_frame(writer, {"type": "x", "value": 7}, b"\x00abc\xff")
            header, payload = await asyncio.wait_for(received, timeout=2)
            self.assertEqual(header["type"], "x")
            self.assertEqual(header["value"], 7)
            self.assertEqual(payload, b"\x00abc\xff")
        finally:
            writer.close()
            await writer.wait_closed()
            server.close()
            await server.wait_closed()


if __name__ == "__main__":
    unittest.main()
