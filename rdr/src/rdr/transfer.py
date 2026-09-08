from __future__ import annotations

import asyncio
import hashlib
import os
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .protocol import LockedFrameWriter

_CHUNK = 256 * 1024


@dataclass
class UploadHandle:
    request_id: str
    destination: Path
    temp_path: Path
    file_obj: Any
    bytes_written: int = 0
    md5: Any = field(default_factory=hashlib.md5)
    expected_size: int | None = None


async def send_file(
    sender: LockedFrameWriter,
    *,
    request_id: str,
    path: str,
    offset: int = 0,
) -> None:
    """Stream a file (or the tail starting at ``offset``) as framed chunks.

    The ``file.done`` checksum always covers the transferred range, so a
    resumed transfer verifies each shard independently while ``file.started``
    carries the full file size for end-to-end length checks.
    """
    try:
        size = os.path.getsize(path)
        start = min(max(offset, 0), size)
        digest = hashlib.md5()
        await sender.send(
            {
                "type": "file.started",
                "request_id": request_id,
                "size": size,
                "offset": start,
            }
        )
        with open(path, "rb") as f:
            if start:
                f.seek(start)
            while True:
                chunk = await asyncio.to_thread(f.read, _CHUNK)
                if not chunk:
                    break
                digest.update(chunk)
                await sender.send({"type": "file.data", "request_id": request_id}, chunk)
        await sender.send(
            {
                "type": "file.done",
                "request_id": request_id,
                "size": size - start,
                "file_size": size,
                "offset": start,
                "checksum": digest.hexdigest(),
            }
        )
    except Exception as exc:
        await sender.send({"type": "file.error", "request_id": request_id, "error": str(exc)})


async def start_upload(
    sender: LockedFrameWriter,
    *,
    request_id: str,
    path: str,
    expected_size: int | None = None,
) -> UploadHandle | None:
    destination = Path(path)
    try:
        tmp = tempfile.NamedTemporaryFile(
            mode="wb",
            prefix=".rdr-upload-",
            dir=str(destination.parent),
            delete=False,
        )
        handle = UploadHandle(
            request_id=request_id,
            destination=destination,
            temp_path=Path(tmp.name),
            file_obj=tmp,
            expected_size=expected_size if isinstance(expected_size, int) else None,
        )
        await sender.send({"type": "file.put.ready", "request_id": request_id})
        return handle
    except Exception as exc:
        await sender.send({"type": "file.error", "request_id": request_id, "error": str(exc)})
        return None


def write_upload(handle: UploadHandle, payload: bytes) -> None:
    handle.file_obj.write(payload)
    handle.md5.update(payload)
    handle.bytes_written += len(payload)


async def finish_upload(
    sender: LockedFrameWriter,
    handle: UploadHandle,
    expected_checksum: str | None = None,
) -> None:
    try:
        actual = handle.md5.hexdigest()
        if expected_checksum and actual != expected_checksum:
            raise ValueError(
                f"checksum mismatch: expected {expected_checksum}, got {actual}"
            )
        if (
            isinstance(handle.expected_size, int)
            and handle.bytes_written != handle.expected_size
        ):
            raise ValueError(
                f"size mismatch: expected {handle.expected_size} bytes, "
                f"got {handle.bytes_written}"
            )
        handle.file_obj.flush()
        os.fsync(handle.file_obj.fileno())
        handle.file_obj.close()
        os.replace(handle.temp_path, handle.destination)
        await sender.send(
            {
                "type": "file.put.done",
                "request_id": handle.request_id,
                "size": handle.bytes_written,
                "checksum": actual,
            }
        )
    except Exception as exc:
        cleanup_upload(handle)
        await sender.send(
            {"type": "file.error", "request_id": handle.request_id, "error": str(exc)}
        )


def cleanup_upload(handle: UploadHandle) -> None:
    try:
        handle.file_obj.close()
    except Exception:
        pass
    try:
        handle.temp_path.unlink(missing_ok=True)
    except Exception:
        pass
