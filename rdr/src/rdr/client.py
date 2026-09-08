from __future__ import annotations

import asyncio
import hashlib
import inspect
import os
import uuid
from collections.abc import Awaitable, Callable
from pathlib import Path
from typing import Any

from .protocol import LockedFrameWriter, read_frame

_CHUNK = 256 * 1024
OutputCallback = Callable[[bytes], None | Awaitable[None]]


class RDRClientError(RuntimeError):
    pass


def _md5_prefix(path: Path, length: int) -> str:
    digest = hashlib.md5()
    remaining = length
    with open(path, "rb") as f:
        while remaining:
            chunk = f.read(min(_CHUNK, remaining))
            if not chunk:
                raise RDRClientError(
                    f"part file ended before expected resume offset {length}: {path}"
                )
            digest.update(chunk)
            remaining -= len(chunk)
    return digest.hexdigest()


class RemoteTerminal:
    def __init__(
        self,
        client: "RDRClient",
        terminal_id: str,
        queue: asyncio.Queue[tuple[dict[str, Any], bytes]],
        *,
        replayed_bytes: int = 0,
        replay_truncated: bool = False,
    ) -> None:
        self.client = client
        self.terminal_id = terminal_id
        self.queue = queue
        self.replayed_bytes = replayed_bytes
        self.replay_truncated = replay_truncated
        self.closed = False
        self.detached = False

    def _require_attached(self) -> None:
        if self.closed:
            raise RDRClientError("terminal is closed")
        if self.detached:
            raise RDRClientError("terminal is detached")

    async def write(self, data: bytes) -> None:
        self._require_attached()
        await self.client._send(
            {"type": "terminal.write", "terminal_id": self.terminal_id},
            data,
        )

    async def resize(self, rows: int, cols: int) -> None:
        self._require_attached()
        await self.client._send(
            {
                "type": "terminal.resize",
                "terminal_id": self.terminal_id,
                "rows": rows,
                "cols": cols,
            }
        )

    async def signal(self, value: str | int) -> None:
        self._require_attached()
        await self.client._send(
            {
                "type": "terminal.signal",
                "terminal_id": self.terminal_id,
                "signal": value,
            }
        )

    async def read(self) -> tuple[dict[str, Any], bytes]:
        header, payload = await self.queue.get()
        if header.get("type") == "terminal.exit":
            self.closed = True
            self.client._terminal_queues.pop(self.terminal_id, None)
        return header, payload

    async def detach(self) -> None:
        if self.closed or self.detached:
            return
        await self.client.detach_terminal(self.terminal_id)
        self.detached = True
        self.client._terminal_queues.pop(self.terminal_id, None)

    async def close(self) -> None:
        if self.closed:
            return
        self._require_attached()
        await self.client._send(
            {"type": "terminal.close", "terminal_id": self.terminal_id}
        )
        self.closed = True
        self.client._terminal_queues.pop(self.terminal_id, None)


class RDRClient:
    def __init__(self, host: str, port: int, token: str) -> None:
        self.host = host
        self.port = port
        self.token = token
        self.reader: asyncio.StreamReader | None = None
        self.writer: asyncio.StreamWriter | None = None
        self.sender: LockedFrameWriter | None = None
        self.identity: dict[str, Any] | None = None
        self._reader_task: asyncio.Task[None] | None = None
        self._request_queues: dict[str, asyncio.Queue[tuple[dict[str, Any], bytes]]] = {}
        self._terminal_queues: dict[str, asyncio.Queue[tuple[dict[str, Any], bytes]]] = {}
        self._closed = False

    async def connect(self) -> dict[str, Any]:
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        self.sender = LockedFrameWriter(self.writer)
        await self.sender.send({"type": "auth", "token": self.token, "protocol": 1})
        header, _ = await read_frame(self.reader)
        if header.get("type") == "auth.error":
            await self.close()
            raise RDRClientError(header.get("error", "authentication failed"))
        if header.get("type") != "ready":
            await self.close()
            raise RDRClientError(f"unexpected handshake response: {header.get('type')}")
        self.identity = header.get("identity")
        self._reader_task = asyncio.create_task(self._reader_loop())
        return self.identity or {}

    async def _reader_loop(self) -> None:
        assert self.reader is not None
        try:
            while True:
                header, payload = await read_frame(self.reader)

                # Request-scoped terminal errors must reach open/attach/detach
                # callers instead of being swallowed by the terminal stream.
                request_id = header.get("request_id")
                if request_id is not None:
                    queue = self._request_queues.get(str(request_id))
                    if queue is not None:
                        await queue.put((header, payload))
                        continue

                terminal_id = header.get("terminal_id")
                if terminal_id and header.get("type") in {
                    "terminal.output",
                    "terminal.exit",
                    "terminal.error",
                }:
                    queue = self._terminal_queues.get(str(terminal_id))
                    if queue is not None:
                        await queue.put((header, payload))
                    continue
        except (asyncio.IncompleteReadError, ConnectionResetError, BrokenPipeError):
            pass
        finally:
            if not self._closed:
                error = (
                    {"type": "connection.closed", "error": "RDR connection closed"},
                    b"",
                )
                for queue in self._request_queues.values():
                    queue.put_nowait(error)
                for queue in self._terminal_queues.values():
                    queue.put_nowait(error)

    async def _send(self, header: dict[str, Any], payload: bytes = b"") -> None:
        if self.sender is None:
            raise RDRClientError("client is not connected")
        await self.sender.send(header, payload)

    def _request_queue(self, request_id: str) -> asyncio.Queue[tuple[dict[str, Any], bytes]]:
        queue: asyncio.Queue[tuple[dict[str, Any], bytes]] = asyncio.Queue()
        self._request_queues[request_id] = queue
        return queue

    async def get_identity(self) -> dict[str, Any]:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        try:
            await self._send({"type": "identity", "request_id": request_id})
            header, _ = await queue.get()
            if header.get("type") != "identity.result":
                raise RDRClientError(header.get("error", "identity request failed"))
            return header["identity"]
        finally:
            self._request_queues.pop(request_id, None)

    async def exec(
        self,
        command: str,
        *,
        cwd: str | None = None,
        env: dict[str, str] | None = None,
        timeout: float | None = None,
        on_stdout: OutputCallback | None = None,
        on_stderr: OutputCallback | None = None,
        capture_limit: int = 4 * 1024 * 1024,
    ) -> dict[str, Any]:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        stdout = bytearray()
        stderr = bytearray()
        stdout_truncated = False
        stderr_truncated = False

        async def deliver(callback: OutputCallback | None, data: bytes) -> None:
            if callback is None:
                return
            result = callback(data)
            if inspect.isawaitable(result):
                await result

        try:
            header: dict[str, Any] = {
                "type": "exec.start",
                "request_id": request_id,
                "command": command,
            }
            if cwd is not None:
                header["cwd"] = cwd
            if env:
                header["env"] = env
            if timeout is not None:
                header["timeout"] = timeout
            await self._send(header)

            while True:
                frame, payload = await queue.get()
                frame_type = frame.get("type")
                if frame_type == "connection.closed":
                    raise RDRClientError(frame.get("error", "connection closed"))
                if frame_type == "exec.stdout":
                    await deliver(on_stdout, payload)
                    remaining = max(0, capture_limit - len(stdout))
                    if remaining:
                        stdout.extend(payload[:remaining])
                    if len(payload) > remaining:
                        stdout_truncated = True
                elif frame_type == "exec.stderr":
                    await deliver(on_stderr, payload)
                    remaining = max(0, capture_limit - len(stderr))
                    if remaining:
                        stderr.extend(payload[:remaining])
                    if len(payload) > remaining:
                        stderr_truncated = True
                elif frame_type == "exec.error":
                    raise RDRClientError(frame.get("error", "remote exec failed"))
                elif frame_type == "exec.exit":
                    return {
                        "request_id": request_id,
                        "exit_code": frame.get("exit_code"),
                        "timed_out": frame.get("timed_out", False),
                        "duration_ms": frame.get("duration_ms"),
                        "stdout": bytes(stdout),
                        "stderr": bytes(stderr),
                        "stdout_truncated": stdout_truncated,
                        "stderr_truncated": stderr_truncated,
                    }
        except asyncio.CancelledError:
            # Best effort: local cancellation should not orphan the remote process.
            try:
                await self._send(
                    {
                        "type": "exec.cancel",
                        "request_id": uuid.uuid4().hex,
                        "target_request_id": request_id,
                    }
                )
            except Exception:
                pass
            raise
        finally:
            self._request_queues.pop(request_id, None)

    async def cancel_exec(self, target_request_id: str) -> bool:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        try:
            await self._send(
                {
                    "type": "exec.cancel",
                    "request_id": request_id,
                    "target_request_id": target_request_id,
                }
            )
            header, _ = await queue.get()
            return bool(header.get("found"))
        finally:
            self._request_queues.pop(request_id, None)

    async def open_terminal(
        self,
        *,
        command: str | None = None,
        cwd: str | None = None,
        env: dict[str, str] | None = None,
        rows: int = 24,
        cols: int = 80,
        terminal_id: str | None = None,
    ) -> RemoteTerminal:
        request_id = uuid.uuid4().hex
        terminal_id = terminal_id or uuid.uuid4().hex
        if terminal_id in self._terminal_queues:
            raise RDRClientError(f"terminal already attached locally: {terminal_id}")
        request_queue = self._request_queue(request_id)
        terminal_queue: asyncio.Queue[tuple[dict[str, Any], bytes]] = asyncio.Queue()
        self._terminal_queues[terminal_id] = terminal_queue
        try:
            header: dict[str, Any] = {
                "type": "terminal.open",
                "request_id": request_id,
                "terminal_id": terminal_id,
                "rows": rows,
                "cols": cols,
            }
            if command is not None:
                header["command"] = command
            if cwd is not None:
                header["cwd"] = cwd
            if env:
                header["env"] = env
            await self._send(header)
            frame, _ = await request_queue.get()
            if frame.get("type") != "terminal.ready":
                raise RDRClientError(frame.get("error", "failed to open terminal"))
            return RemoteTerminal(
                self,
                terminal_id,
                terminal_queue,
                replayed_bytes=int(frame.get("replayed_bytes") or 0),
                replay_truncated=bool(frame.get("replay_truncated", False)),
            )
        except Exception:
            self._terminal_queues.pop(terminal_id, None)
            raise
        finally:
            self._request_queues.pop(request_id, None)

    async def attach_terminal(self, terminal_id: str) -> RemoteTerminal:
        if not terminal_id:
            raise RDRClientError("terminal_id required")
        if terminal_id in self._terminal_queues:
            raise RDRClientError(f"terminal already attached locally: {terminal_id}")

        request_id = uuid.uuid4().hex
        request_queue = self._request_queue(request_id)
        terminal_queue: asyncio.Queue[tuple[dict[str, Any], bytes]] = asyncio.Queue()
        self._terminal_queues[terminal_id] = terminal_queue
        try:
            await self._send(
                {
                    "type": "terminal.attach",
                    "request_id": request_id,
                    "terminal_id": terminal_id,
                }
            )
            frame, _ = await request_queue.get()
            if frame.get("type") != "terminal.attached":
                raise RDRClientError(frame.get("error", "failed to attach terminal"))
            return RemoteTerminal(
                self,
                terminal_id,
                terminal_queue,
                replayed_bytes=int(frame.get("replayed_bytes") or 0),
                replay_truncated=bool(frame.get("replay_truncated", False)),
            )
        except Exception:
            self._terminal_queues.pop(terminal_id, None)
            raise
        finally:
            self._request_queues.pop(request_id, None)

    async def detach_terminal(self, terminal_id: str) -> None:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        try:
            await self._send(
                {
                    "type": "terminal.detach",
                    "request_id": request_id,
                    "terminal_id": terminal_id,
                }
            )
            frame, _ = await queue.get()
            if frame.get("type") != "terminal.detached":
                raise RDRClientError(frame.get("error", "failed to detach terminal"))
        finally:
            self._request_queues.pop(request_id, None)

    async def download(self, remote_path: str, local_path: str | os.PathLike[str]) -> int:
        """Download a remote file with integrity-safe automatic resume.

        Transfers land in a stable ``.<name>.rdr-part`` temp file. Before a
        non-zero offset is trusted, the server hashes the remote prefix and
        the client compares it with the local part. The newly transferred
        range has its own md5 and the final assembled length is checked before
        atomic rename. A legacy server without range metadata still works by
        restarting the transfer from offset zero.
        """
        local = Path(local_path)
        temp = local.with_name(f".{local.name}.rdr-part")
        total = 0
        for attempt in (0, 1):
            request_id = uuid.uuid4().hex
            queue = self._request_queue(request_id)
            offset = temp.stat().st_size if temp.exists() else 0
            part_checksum = (
                await asyncio.to_thread(_md5_prefix, temp, offset) if offset else None
            )
            digest = hashlib.md5()
            total = 0
            restart = False
            try:
                await self._send(
                    {
                        "type": "file.get",
                        "request_id": request_id,
                        "path": remote_path,
                        "offset": offset,
                    }
                )
                with open(temp, "ab") as f:
                    while True:
                        header, payload = await queue.get()
                        frame_type = header.get("type")
                        if frame_type == "file.started":
                            file_size = header.get("size")
                            server_offset = header.get("offset")

                            # Servers predating range support omit `offset`.
                            # A fresh transfer is compatible; an existing part
                            # must be discarded because the server cannot prove
                            # that it is the prefix of the current remote file.
                            if server_offset is None:
                                if offset:
                                    if attempt == 0:
                                        restart = True
                                        break
                                    raise RDRClientError(
                                        f"cannot resume {remote_path}: server "
                                        "does not support safe ranged download"
                                    )
                            elif server_offset != offset or (
                                isinstance(file_size, int) and offset > file_size
                            ):
                                if attempt == 0:
                                    restart = True
                                    break
                                raise RDRClientError(
                                    f"cannot resume {remote_path}: part file "
                                    f"does not match remote state"
                                )
                            elif offset:
                                prefix_checksum = header.get("prefix_checksum")
                                if (
                                    not isinstance(prefix_checksum, str)
                                    or prefix_checksum != part_checksum
                                ):
                                    if attempt == 0:
                                        restart = True
                                        break
                                    raise RDRClientError(
                                        f"cannot resume {remote_path}: local part "
                                        "does not match remote prefix"
                                    )
                        elif frame_type == "file.data":
                            f.write(payload)
                            digest.update(payload)
                            total += len(payload)
                        elif frame_type == "file.error":
                            raise RDRClientError(
                                header.get("error", "download failed")
                            )
                        elif frame_type == "connection.closed":
                            raise RDRClientError(
                                header.get("error", "connection closed")
                            )
                        elif frame_type == "file.done":
                            expected = header.get("checksum")
                            if expected and expected != digest.hexdigest():
                                raise RDRClientError(
                                    f"checksum mismatch: expected {expected}, "
                                    f"got {digest.hexdigest()}"
                                )
                            file_size = header.get("file_size")
                            if isinstance(file_size, int):
                                if offset + total != file_size:
                                    raise RDRClientError(
                                        f"size mismatch: expected {file_size} "
                                        f"bytes, got {offset + total}"
                                    )
                            else:
                                # Legacy server: a compatible fresh request
                                # covers the whole file and `size` is total.
                                done_size = header.get("size")
                                if (
                                    isinstance(done_size, int)
                                    and done_size != total
                                ):
                                    raise RDRClientError(
                                        f"size mismatch: expected {done_size} "
                                        f"bytes, got {total}"
                                    )
                            f.flush()
                            os.fsync(f.fileno())
                            break
                if restart:
                    temp.write_bytes(b"")
                    continue
                os.replace(temp, local)
                return total
            finally:
                self._request_queues.pop(request_id, None)
        raise RDRClientError(f"download failed after retry: {remote_path}")

    async def upload(self, local_path: str | os.PathLike[str], remote_path: str) -> int:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        total = 0
        digest = hashlib.md5()
        try:
            await self._send(
                {
                    "type": "file.put.start",
                    "request_id": request_id,
                    "path": remote_path,
                    "size": os.path.getsize(local_path),
                }
            )
            frame, _ = await queue.get()
            if frame.get("type") != "file.put.ready":
                raise RDRClientError(frame.get("error", "upload rejected"))

            with open(local_path, "rb") as f:
                while True:
                    chunk = f.read(_CHUNK)
                    if not chunk:
                        break
                    digest.update(chunk)
                    await self._send(
                        {"type": "file.put.data", "request_id": request_id},
                        chunk,
                    )
                    total += len(chunk)

            await self._send(
                {
                    "type": "file.put.end",
                    "request_id": request_id,
                    "checksum": digest.hexdigest(),
                }
            )
            frame, _ = await queue.get()
            if frame.get("type") != "file.put.done":
                raise RDRClientError(frame.get("error", "upload failed"))
            ack_checksum = frame.get("checksum")
            if ack_checksum and ack_checksum != digest.hexdigest():
                raise RDRClientError(
                    f"checksum mismatch: expected {digest.hexdigest()}, got {ack_checksum}"
                )
            ack_size = frame.get("size")
            if isinstance(ack_size, int) and ack_size != total:
                raise RDRClientError(f"size mismatch: expected {total} bytes, got {ack_size}")
            return total
        except Exception:
            try:
                await self._send({"type": "file.put.cancel", "request_id": request_id})
            except Exception:
                pass
            raise
        finally:
            self._request_queues.pop(request_id, None)

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        if self._reader_task is not None:
            self._reader_task.cancel()
            await asyncio.gather(self._reader_task, return_exceptions=True)
        if self.writer is not None:
            self.writer.close()
            try:
                await self.writer.wait_closed()
            except Exception:
                pass
