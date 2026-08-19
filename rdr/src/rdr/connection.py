from __future__ import annotations

import asyncio
import uuid
from typing import Any, TYPE_CHECKING

from .execution import ExecHandle, cancel_exec, run_exec
from .identity import runtime_identity
from .process import terminate_process_group
from .protocol import LockedFrameWriter, ProtocolError, read_frame
from .terminal import TerminalHandle
from .transfer import (
    UploadHandle,
    cleanup_upload,
    finish_upload,
    send_file,
    start_upload,
    write_upload,
)

if TYPE_CHECKING:
    from .runtime import RDRServer


class ClientConnection:
    def __init__(
        self,
        server: "RDRServer",
        reader: asyncio.StreamReader,
        writer: asyncio.StreamWriter,
    ) -> None:
        self.server = server
        self.reader = reader
        self.writer = writer
        self.sender = LockedFrameWriter(writer)
        self.execs: dict[str, ExecHandle] = {}
        self.terminals: dict[str, TerminalHandle] = {}
        self.uploads: dict[str, UploadHandle] = {}
        self.tasks: set[asyncio.Task[Any]] = set()
        self.closed = False

    async def run(self) -> None:
        try:
            header, _ = await asyncio.wait_for(read_frame(self.reader), timeout=10.0)
            if header.get("type") != "auth":
                await self.sender.send({"type": "auth.error", "error": "auth required"})
                return

            token = header.get("token")
            if not isinstance(token, str) or not self.server.authenticate(token):
                await self.sender.send({"type": "auth.error", "error": "invalid token"})
                return

            await self.sender.send(
                {"type": "ready", "protocol": 1, "identity": runtime_identity()}
            )
            while True:
                header, payload = await read_frame(self.reader)
                await self.dispatch(header, payload)
        except (asyncio.IncompleteReadError, ConnectionResetError, BrokenPipeError):
            pass
        except asyncio.CancelledError:
            raise
        except ProtocolError as exc:
            try:
                await self.sender.send({"type": "protocol.error", "error": str(exc)})
            except Exception:
                pass
        finally:
            await self.close()

    async def dispatch(self, header: dict[str, Any], payload: bytes) -> None:
        msg_type = header.get("type")
        request_id = str(header.get("request_id") or "")

        if msg_type == "identity":
            await self.sender.send(
                {
                    "type": "identity.result",
                    "request_id": request_id,
                    "identity": runtime_identity(),
                }
            )
            return

        if msg_type == "exec.start":
            await self._start_exec(header)
            return
        if msg_type == "exec.cancel":
            await self._cancel_exec(header)
            return

        if msg_type == "terminal.open":
            await self._open_terminal(header)
            return
        if msg_type == "terminal.write":
            await self._terminal_write(header, payload)
            return
        if msg_type == "terminal.resize":
            await self._terminal_resize(header)
            return
        if msg_type == "terminal.signal":
            await self._terminal_signal(header)
            return
        if msg_type == "terminal.close":
            await self._terminal_close(header)
            return

        if msg_type == "file.get":
            path = header.get("path")
            if not isinstance(path, str):
                await self.sender.send(
                    {"type": "file.error", "request_id": request_id, "error": "path required"}
                )
                return
            task = asyncio.create_task(
                send_file(self.sender, request_id=request_id or uuid.uuid4().hex, path=path)
            )
            self._track(task)
            return

        if msg_type == "file.put.start":
            await self._file_put_start(header)
            return
        if msg_type == "file.put.data":
            await self._file_put_data(header, payload)
            return
        if msg_type == "file.put.end":
            await self._file_put_end(header)
            return
        if msg_type == "file.put.cancel":
            self._file_put_cancel(header)
            return

        await self.sender.send(
            {"type": "error", "request_id": request_id, "error": f"unsupported message type: {msg_type}"}
        )

    def _track(self, task: asyncio.Task[Any]) -> None:
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)

    async def _start_exec(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or uuid.uuid4().hex)
        command = header.get("command")
        if not isinstance(command, str) or not command:
            await self.sender.send(
                {"type": "exec.error", "request_id": request_id, "error": "command required"}
            )
            return
        if request_id in self.execs:
            await self.sender.send(
                {"type": "exec.error", "request_id": request_id, "error": "duplicate request_id"}
            )
            return

        cwd = header.get("cwd") if isinstance(header.get("cwd"), str) else None
        env = header.get("env") if isinstance(header.get("env"), dict) else None
        timeout_value = header.get("timeout")
        timeout = (
            float(timeout_value)
            if isinstance(timeout_value, (int, float)) and timeout_value > 0
            else None
        )

        async def runner() -> None:
            try:
                await run_exec(
                    handle,
                    self.sender,
                    command=command,
                    cwd=cwd,
                    env=env,
                    timeout=timeout,
                )
            finally:
                self.execs.pop(request_id, None)

        task = asyncio.create_task(runner())
        handle = ExecHandle(request_id=request_id, task=task)
        self.execs[request_id] = handle
        self._track(task)

    async def _cancel_exec(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or "")
        target_id = str(header.get("target_request_id") or "")
        handle = self.execs.get(target_id)
        if handle is not None:
            await cancel_exec(handle)
        await self.sender.send(
            {
                "type": "exec.cancelled",
                "request_id": request_id,
                "target_request_id": target_id,
                "found": handle is not None,
            }
        )

    async def _open_terminal(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or "")
        terminal_id = str(header.get("terminal_id") or uuid.uuid4().hex)
        if terminal_id in self.terminals:
            await self.sender.send(
                {
                    "type": "terminal.error",
                    "request_id": request_id,
                    "terminal_id": terminal_id,
                    "error": "duplicate terminal_id",
                }
            )
            return

        try:
            handle = await TerminalHandle.open(
                terminal_id=terminal_id,
                sender=self.sender,
                command=header.get("command") if isinstance(header.get("command"), str) else None,
                cwd=header.get("cwd") if isinstance(header.get("cwd"), str) else None,
                env=header.get("env") if isinstance(header.get("env"), dict) else None,
                rows=max(1, int(header.get("rows") or 24)),
                cols=max(1, int(header.get("cols") or 80)),
            )
        except Exception as exc:
            await self.sender.send(
                {
                    "type": "terminal.error",
                    "request_id": request_id,
                    "terminal_id": terminal_id,
                    "error": str(exc),
                }
            )
            return

        self.terminals[terminal_id] = handle
        await self.sender.send(
            {
                "type": "terminal.ready",
                "request_id": request_id,
                "terminal_id": terminal_id,
                "pid": handle.pid,
            }
        )

        async def forget_when_done() -> None:
            if handle.wait_task is not None:
                await asyncio.gather(handle.wait_task, return_exceptions=True)
            if self.terminals.get(terminal_id) is handle:
                self.terminals.pop(terminal_id, None)

        watcher = asyncio.create_task(forget_when_done())
        self._track(watcher)

    def _terminal(self, terminal_id: str) -> TerminalHandle:
        try:
            return self.terminals[terminal_id]
        except KeyError as exc:
            raise RuntimeError(f"unknown terminal: {terminal_id}") from exc

    async def _terminal_write(self, header: dict[str, Any], payload: bytes) -> None:
        terminal_id = str(header.get("terminal_id") or "")
        try:
            await self._terminal(terminal_id).write(payload)
        except Exception as exc:
            await self.sender.send(
                {"type": "terminal.error", "terminal_id": terminal_id, "error": str(exc)}
            )

    async def _terminal_resize(self, header: dict[str, Any]) -> None:
        terminal_id = str(header.get("terminal_id") or "")
        try:
            self._terminal(terminal_id).resize(
                max(1, int(header.get("rows") or 24)),
                max(1, int(header.get("cols") or 80)),
            )
        except Exception as exc:
            await self.sender.send(
                {"type": "terminal.error", "terminal_id": terminal_id, "error": str(exc)}
            )

    async def _terminal_signal(self, header: dict[str, Any]) -> None:
        terminal_id = str(header.get("terminal_id") or "")
        try:
            self._terminal(terminal_id).send_signal(header.get("signal", "INT"))
        except Exception as exc:
            await self.sender.send(
                {"type": "terminal.error", "terminal_id": terminal_id, "error": str(exc)}
            )

    async def _terminal_close(self, header: dict[str, Any]) -> None:
        terminal_id = str(header.get("terminal_id") or "")
        handle = self.terminals.pop(terminal_id, None)
        if handle is not None:
            await handle.close()

    async def _file_put_start(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or uuid.uuid4().hex)
        path = header.get("path")
        if not isinstance(path, str):
            await self.sender.send(
                {"type": "file.error", "request_id": request_id, "error": "path required"}
            )
            return
        if request_id in self.uploads:
            await self.sender.send(
                {"type": "file.error", "request_id": request_id, "error": "duplicate upload"}
            )
            return
        handle = await start_upload(self.sender, request_id=request_id, path=path)
        if handle is not None:
            self.uploads[request_id] = handle

    async def _file_put_data(self, header: dict[str, Any], payload: bytes) -> None:
        request_id = str(header.get("request_id") or "")
        handle = self.uploads.get(request_id)
        if handle is None:
            await self.sender.send(
                {"type": "file.error", "request_id": request_id, "error": "unknown upload"}
            )
            return
        write_upload(handle, payload)

    async def _file_put_end(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or "")
        handle = self.uploads.pop(request_id, None)
        if handle is None:
            await self.sender.send(
                {"type": "file.error", "request_id": request_id, "error": "unknown upload"}
            )
            return
        await finish_upload(self.sender, handle)

    def _file_put_cancel(self, header: dict[str, Any]) -> None:
        request_id = str(header.get("request_id") or "")
        handle = self.uploads.pop(request_id, None)
        if handle is not None:
            cleanup_upload(handle)

    async def close(self) -> None:
        if self.closed:
            return
        self.closed = True

        for handle in list(self.execs.values()):
            if handle.process is not None and handle.process.returncode is None:
                await terminate_process_group(handle.process.pid)
            handle.task.cancel()
        self.execs.clear()

        for handle in list(self.terminals.values()):
            await handle.close()
        self.terminals.clear()

        for handle in list(self.uploads.values()):
            cleanup_upload(handle)
        self.uploads.clear()

        for task in list(self.tasks):
            if task is asyncio.current_task():
                continue
            if not task.done():
                task.cancel()
        if self.tasks:
            await asyncio.gather(*self.tasks, return_exceptions=True)

        self.writer.close()
        try:
            await self.writer.wait_closed()
        except Exception:
            pass
        self.server.connections.discard(self)
