from __future__ import annotations

import asyncio
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


class RemoteTerminal:
    def __init__(
        self,
        client: "RDRClient",
        terminal_id: str,
        queue: asyncio.Queue[tuple[dict[str, Any], bytes]],
    ) -> None:
        self.client = client
        self.terminal_id = terminal_id
        self.queue = queue
        self.closed = False

    async def write(self, data: bytes) -> None:
        await self.client._send(
            {"type": "terminal.write", "terminal_id": self.terminal_id},
            data,
        )

    async def resize(self, rows: int, cols: int) -> None:
        await self.client._send(
            {
                "type": "terminal.resize",
                "terminal_id": self.terminal_id,
                "rows": rows,
                "cols": cols,
            }
        )

    async def signal(self, value: str | int) -> None:
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
        return header, payload

    async def close(self) -> None:
        if self.closed:
            return
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

                request_id = header.get("request_id")
                if request_id is not None:
                    queue = self._request_queues.get(str(request_id))
                    if queue is not None:
                        await queue.put((header, payload))
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
    ) -> RemoteTerminal:
        request_id = uuid.uuid4().hex
        terminal_id = uuid.uuid4().hex
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
            return RemoteTerminal(self, terminal_id, terminal_queue)
        except Exception:
            self._terminal_queues.pop(terminal_id, None)
            raise
        finally:
            self._request_queues.pop(request_id, None)

    async def download(self, remote_path: str, local_path: str | os.PathLike[str]) -> int:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        local = Path(local_path)
        temp = local.with_name(f".{local.name}.rdr-part-{uuid.uuid4().hex}")
        total = 0
        try:
            await self._send(
                {"type": "file.get", "request_id": request_id, "path": remote_path}
            )
            with open(temp, "wb") as f:
                while True:
                    header, payload = await queue.get()
                    frame_type = header.get("type")
                    if frame_type == "file.data":
                        f.write(payload)
                        total += len(payload)
                    elif frame_type == "file.error":
                        raise RDRClientError(header.get("error", "download failed"))
                    elif frame_type == "connection.closed":
                        raise RDRClientError(header.get("error", "connection closed"))
                    elif frame_type == "file.done":
                        break
                f.flush()
                os.fsync(f.fileno())
            os.replace(temp, local)
            return total
        finally:
            self._request_queues.pop(request_id, None)
            if temp.exists():
                temp.unlink(missing_ok=True)

    async def upload(self, local_path: str | os.PathLike[str], remote_path: str) -> int:
        request_id = uuid.uuid4().hex
        queue = self._request_queue(request_id)
        total = 0
        try:
            await self._send(
                {
                    "type": "file.put.start",
                    "request_id": request_id,
                    "path": remote_path,
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
                    await self._send(
                        {"type": "file.put.data", "request_id": request_id},
                        chunk,
                    )
                    total += len(chunk)

            await self._send({"type": "file.put.end", "request_id": request_id})
            frame, _ = await queue.get()
            if frame.get("type") != "file.put.done":
                raise RDRClientError(frame.get("error", "upload failed"))
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
