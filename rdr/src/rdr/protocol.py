from __future__ import annotations

import asyncio
import json
import struct
from typing import Any

_HEADER_LEN = struct.Struct("!I")
MAX_HEADER_BYTES = 1 << 20
MAX_PAYLOAD_BYTES = 64 << 20


class ProtocolError(RuntimeError):
    pass


async def read_frame(reader: asyncio.StreamReader) -> tuple[dict[str, Any], bytes]:
    raw_len = await reader.readexactly(_HEADER_LEN.size)
    (header_len,) = _HEADER_LEN.unpack(raw_len)
    if header_len <= 0 or header_len > MAX_HEADER_BYTES:
        raise ProtocolError(f"invalid header length: {header_len}")

    raw_header = await reader.readexactly(header_len)
    try:
        header = json.loads(raw_header)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProtocolError("invalid JSON header") from exc

    if not isinstance(header, dict):
        raise ProtocolError("frame header must be a JSON object")

    payload_size = header.get("payload_size", 0)
    if not isinstance(payload_size, int) or payload_size < 0 or payload_size > MAX_PAYLOAD_BYTES:
        raise ProtocolError(f"invalid payload size: {payload_size!r}")

    payload = await reader.readexactly(payload_size) if payload_size else b""
    return header, payload


async def write_frame(
    writer: asyncio.StreamWriter,
    header: dict[str, Any],
    payload: bytes = b"",
) -> None:
    if len(payload) > MAX_PAYLOAD_BYTES:
        raise ProtocolError(f"payload exceeds {MAX_PAYLOAD_BYTES} bytes")

    wire_header = dict(header)
    wire_header["payload_size"] = len(payload)
    raw_header = json.dumps(
        wire_header,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    if len(raw_header) > MAX_HEADER_BYTES:
        raise ProtocolError(f"header exceeds {MAX_HEADER_BYTES} bytes")

    writer.write(_HEADER_LEN.pack(len(raw_header)))
    writer.write(raw_header)
    if payload:
        writer.write(payload)
    await writer.drain()


class LockedFrameWriter:
    """Serializes frame writes from concurrently running commands and terminals."""

    def __init__(self, writer: asyncio.StreamWriter) -> None:
        self._writer = writer
        self._lock = asyncio.Lock()

    async def send(self, header: dict[str, Any], payload: bytes = b"") -> None:
        async with self._lock:
            await write_frame(self._writer, header, payload)
