from __future__ import annotations

import hashlib
import tempfile
import unittest
from pathlib import Path

from rdr.client import RDRClient
from rdr.transfer import send_file


def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


class FakeSender:
    def __init__(self) -> None:
        self.frames: list[tuple[dict, bytes]] = []

    async def send(self, header: dict, payload: bytes = b"") -> None:
        self.frames.append((header, payload))


class ScriptedDownloadClient(RDRClient):
    """Exercise download state transitions without a real TCP connection."""

    def __init__(self, payload: bytes, *, legacy: bool = False) -> None:
        super().__init__("unused", 0, "unused")
        self.payload = payload
        self.legacy = legacy
        self.offsets: list[int] = []

    async def _send(self, header: dict, payload: bytes = b"") -> None:
        if header.get("type") != "file.get":
            raise AssertionError(header)
        request_id = str(header["request_id"])
        queue = self._request_queues[request_id]
        requested = int(header.get("offset") or 0)
        self.offsets.append(requested)

        if self.legacy:
            await queue.put(
                ({"type": "file.started", "request_id": request_id, "size": len(self.payload)}, b"")
            )
            await queue.put(
                ({"type": "file.data", "request_id": request_id}, self.payload)
            )
            await queue.put(
                ({"type": "file.done", "request_id": request_id, "size": len(self.payload)}, b"")
            )
            return

        start = min(max(requested, 0), len(self.payload))
        started = {
            "type": "file.started",
            "request_id": request_id,
            "size": len(self.payload),
            "offset": start,
        }
        if start:
            started["prefix_checksum"] = _md5(self.payload[:start])
        tail = self.payload[start:]
        await queue.put((started, b""))
        if tail:
            await queue.put(({"type": "file.data", "request_id": request_id}, tail))
        await queue.put(
            (
                {
                    "type": "file.done",
                    "request_id": request_id,
                    "size": len(tail),
                    "file_size": len(self.payload),
                    "offset": start,
                    "checksum": _md5(tail),
                },
                b"",
            )
        )


class ResumeIntegrityTest(unittest.IsolatedAsyncioTestCase):
    async def test_server_reports_checksum_for_existing_prefix(self) -> None:
        payload = b"abcdefghij" * 1000
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "remote.bin"
            path.write_bytes(payload)
            sender = FakeSender()
            await send_file(sender, request_id="r1", path=str(path), offset=1234)

        started = sender.frames[0][0]
        done = sender.frames[-1][0]
        self.assertEqual(started["offset"], 1234)
        self.assertEqual(started["prefix_checksum"], _md5(payload[:1234]))
        self.assertEqual(done["checksum"], _md5(payload[1234:]))

    async def test_valid_part_resumes_from_verified_prefix(self) -> None:
        payload = b"0123456789" * 1000
        client = ScriptedDownloadClient(payload)
        with tempfile.TemporaryDirectory() as td:
            local = Path(td) / "copy.bin"
            part = local.with_name(f".{local.name}.rdr-part")
            part.write_bytes(payload[:2345])

            transferred = await client.download("/remote.bin", local)

            self.assertEqual(client.offsets, [2345])
            self.assertEqual(transferred, len(payload) - 2345)
            self.assertEqual(local.read_bytes(), payload)

    async def test_corrupt_part_is_rejected_and_restarted(self) -> None:
        payload = b"abcdefghij" * 1000
        client = ScriptedDownloadClient(payload)
        with tempfile.TemporaryDirectory() as td:
            local = Path(td) / "copy.bin"
            part = local.with_name(f".{local.name}.rdr-part")
            part.write_bytes(b"x" * 2345)

            transferred = await client.download("/remote.bin", local)

            self.assertEqual(client.offsets, [2345, 0])
            self.assertEqual(transferred, len(payload))
            self.assertEqual(local.read_bytes(), payload)

    async def test_legacy_server_falls_back_to_full_download(self) -> None:
        payload = b"legacy-data" * 1000
        client = ScriptedDownloadClient(payload, legacy=True)
        with tempfile.TemporaryDirectory() as td:
            local = Path(td) / "copy.bin"
            part = local.with_name(f".{local.name}.rdr-part")
            part.write_bytes(payload[:1111])

            transferred = await client.download("/remote.bin", local)

            self.assertEqual(client.offsets, [1111, 0])
            self.assertEqual(transferred, len(payload))
            self.assertEqual(local.read_bytes(), payload)


if __name__ == "__main__":
    unittest.main()
