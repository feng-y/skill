from __future__ import annotations

import asyncio
import hashlib
import tempfile
import unittest
from pathlib import Path

from rdr.transfer import (
    finish_upload,
    send_file,
    start_upload,
    write_upload,
)


class FakeSender:
    def __init__(self) -> None:
        self.frames: list[tuple[dict, bytes]] = []

    async def send(self, header: dict, payload: bytes = b"") -> None:
        self.frames.append((header, payload))

    def types(self) -> list[str]:
        return [header.get("type", "") for header, _ in self.frames]


def md5_of(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


class SendFileTest(unittest.IsolatedAsyncioTestCase):
    async def test_done_frame_carries_matching_checksum(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "f.bin"
            payload = b"hello rdr transfer" * 1000
            path.write_bytes(payload)

            sender = FakeSender()
            await send_file(sender, request_id="r1", path=str(path))

            self.assertEqual(
                sender.types(), ["file.started", "file.data", "file.done"]
            )
            started, data, done = sender.frames
            self.assertEqual(started[0]["size"], len(payload))
            self.assertEqual(data[1], payload)
            self.assertEqual(done[0]["checksum"], md5_of(payload))
            self.assertEqual(done[0]["size"], len(payload))

    async def test_missing_file_reports_error(self) -> None:
        sender = FakeSender()
        await send_file(sender, request_id="r1", path="/nonexistent/f.bin")
        self.assertEqual(sender.types(), ["file.error"])
        self.assertIn("error", sender.frames[0][0])


class UploadTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        self.dir = Path(self.root.name)

    async def _upload(
        self,
        destination: Path,
        payload: bytes,
        *,
        checksum: str | None = None,
        expected_size: int | None = None,
    ) -> FakeSender:
        sender = FakeSender()
        handle = await start_upload(
            sender, request_id="r1", path=str(destination), expected_size=expected_size
        )
        assert handle is not None
        write_upload(handle, payload)
        await finish_upload(sender, handle, expected_checksum=checksum)
        return sender

    async def test_success_commits_file_and_echoes_checksum(self) -> None:
        destination = self.dir / "dst.bin"
        payload = b"payload-123" * 500

        sender = await self._upload(
            destination, payload, checksum=md5_of(payload), expected_size=len(payload)
        )

        self.assertEqual(sender.types(), ["file.put.ready", "file.put.done"])
        done = sender.frames[1][0]
        self.assertEqual(done["checksum"], md5_of(payload))
        self.assertEqual(done["size"], len(payload))
        self.assertEqual(destination.read_bytes(), payload)
        self.assertEqual(list(self.dir.glob(".rdr-upload-*")), [])

    async def test_checksum_mismatch_rejects_commit(self) -> None:
        destination = self.dir / "dst.bin"
        payload = b"real-bytes" * 100

        sender = await self._upload(
            destination, payload, checksum="0" * 32, expected_size=len(payload)
        )

        self.assertEqual(sender.types(), ["file.put.ready", "file.error"])
        self.assertIn("checksum mismatch", sender.frames[1][0]["error"])
        self.assertFalse(destination.exists())
        self.assertEqual(list(self.dir.glob(".rdr-upload-*")), [])

    async def test_size_mismatch_rejects_commit(self) -> None:
        destination = self.dir / "dst.bin"
        payload = b"size-check"

        sender = await self._upload(
            destination, payload, checksum=md5_of(payload), expected_size=99999
        )

        self.assertEqual(sender.types(), ["file.put.ready", "file.error"])
        self.assertIn("size mismatch", sender.frames[1][0]["error"])
        self.assertFalse(destination.exists())
        self.assertEqual(list(self.dir.glob(".rdr-upload-*")), [])

    async def test_legacy_client_without_checksum_still_commits(self) -> None:
        destination = self.dir / "dst.bin"
        payload = b"legacy"

        sender = await self._upload(destination, payload)

        self.assertEqual(sender.types(), ["file.put.ready", "file.put.done"])
        self.assertEqual(destination.read_bytes(), payload)


if __name__ == "__main__":
    unittest.main()
