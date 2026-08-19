from __future__ import annotations

import asyncio
import os
import tempfile
from dataclasses import dataclass
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


async def send_file(
    sender: LockedFrameWriter,
    *,
    request_id: str,
    path: str,
) -> None:
    try:
        size = os.path.getsize(path)
        await sender.send({"type": "file.started", "request_id": request_id, "size": size})
        with open(path, "rb") as f:
            while True:
                chunk = await asyncio.to_thread(f.read, _CHUNK)
                if not chunk:
                    break
                await sender.send({"type": "file.data", "request_id": request_id}, chunk)
        await sender.send({"type": "file.done", "request_id": request_id, "size": size})
    except Exception as exc:
        await sender.send({"type": "file.error", "request_id": request_id, "error": str(exc)})


async def start_upload(
    sender: LockedFrameWriter,
    *,
    request_id: str,
    path: str,
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
        )
        await sender.send({"type": "file.put.ready", "request_id": request_id})
        return handle
    except Exception as exc:
        await sender.send({"type": "file.error", "request_id": request_id, "error": str(exc)})
        return None


def write_upload(handle: UploadHandle, payload: bytes) -> None:
    handle.file_obj.write(payload)
    handle.bytes_written += len(payload)


async def finish_upload(sender: LockedFrameWriter, handle: UploadHandle) -> None:
    try:
        handle.file_obj.flush()
        os.fsync(handle.file_obj.fileno())
        handle.file_obj.close()
        os.replace(handle.temp_path, handle.destination)
        await sender.send(
            {
                "type": "file.put.done",
                "request_id": handle.request_id,
                "size": handle.bytes_written,
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
