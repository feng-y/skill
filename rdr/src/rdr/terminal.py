from __future__ import annotations

import asyncio
import os
import signal
import struct
from collections import deque
from dataclasses import dataclass, field

from .process import parse_signal, terminate_process_group
from .protocol import LockedFrameWriter

_CHUNK = 256 * 1024
_REPLAY_LIMIT = 4 * 1024 * 1024
_CONNECTION_ERRORS = (
    BrokenPipeError,
    ConnectionResetError,
    ConnectionAbortedError,
    OSError,
    RuntimeError,
)


@dataclass
class TerminalHandle:
    terminal_id: str
    pid: int
    master_fd: int
    loop: asyncio.AbstractEventLoop
    queue: asyncio.Queue[bytes | None] = field(default_factory=asyncio.Queue)
    pump_task: asyncio.Task[None] | None = None
    wait_task: asyncio.Task[None] | None = None
    closed: bool = False
    sender: LockedFrameWriter | None = None
    output_buffer: deque[bytes] = field(default_factory=deque)
    buffered_bytes: int = 0
    buffer_truncated: bool = False
    attachment_lock: asyncio.Lock = field(default_factory=asyncio.Lock)

    @classmethod
    async def open(
        cls,
        *,
        terminal_id: str,
        command: str | None,
        cwd: str | None,
        env: dict[str, str] | None,
        rows: int,
        cols: int,
    ) -> "TerminalHandle":
        if os.name != "posix" or not hasattr(os, "posix_spawn"):
            raise RuntimeError("PTY terminals require POSIX posix_spawn support")

        import fcntl
        import termios

        master_fd, slave_fd = os.openpty()
        try:
            slave_name = os.ttyname(slave_fd)
        finally:
            os.close(slave_fd)

        child_env = os.environ.copy()
        if env:
            child_env.update({str(k): str(v) for k, v in env.items()})
        shell = child_env.get("SHELL", "/bin/bash")

        if cwd:
            child_env["RDR_CWD"] = cwd
            if command:
                child_env["RDR_COMMAND"] = command
                argv = [
                    shell,
                    "-lc",
                    'cd -- "$RDR_CWD" && exec "$SHELL" -lc "$RDR_COMMAND"',
                ]
            else:
                argv = [shell, "-lc", 'cd -- "$RDR_CWD" && exec "$SHELL" -l']
        elif command:
            argv = [shell, "-lc", command]
        else:
            argv = [shell, "-l"]

        # Open the slave inside the new session. This gives the child a real
        # controlling terminal without forkpty() in a potentially threaded process.
        file_actions = [
            (os.POSIX_SPAWN_OPEN, 0, slave_name, os.O_RDWR, 0),
            (os.POSIX_SPAWN_DUP2, 0, 1),
            (os.POSIX_SPAWN_DUP2, 0, 2),
        ]
        spawn = os.posix_spawn if os.path.isabs(shell) else os.posix_spawnp
        try:
            pid = spawn(
                shell,
                argv,
                child_env,
                file_actions=file_actions,
                setsid=True,
                setsigdef=(
                    signal.SIGINT,
                    signal.SIGQUIT,
                    signal.SIGTERM,
                    signal.SIGHUP,
                    signal.SIGPIPE,
                ),
            )
        except Exception:
            os.close(master_fd)
            raise

        os.set_blocking(master_fd, False)
        fcntl.ioctl(
            master_fd,
            termios.TIOCSWINSZ,
            struct.pack("HHHH", rows, cols, 0, 0),
        )

        handle = cls(
            terminal_id=terminal_id,
            pid=pid,
            master_fd=master_fd,
            loop=asyncio.get_running_loop(),
        )
        handle._start()
        return handle

    def _start(self) -> None:
        def readable() -> None:
            try:
                data = os.read(self.master_fd, _CHUNK)
            except BlockingIOError:
                return
            except OSError:
                self._stop_reader()
                self.queue.put_nowait(None)
                return
            if data:
                self.queue.put_nowait(data)
            else:
                self._stop_reader()
                self.queue.put_nowait(None)

        self.loop.add_reader(self.master_fd, readable)
        self.pump_task = asyncio.create_task(self._pump_output())
        self.wait_task = asyncio.create_task(self._wait_for_exit())

    def _stop_reader(self) -> None:
        try:
            self.loop.remove_reader(self.master_fd)
        except Exception:
            pass

    def _buffer_output(self, data: bytes) -> None:
        if not data:
            return
        self.output_buffer.append(data)
        self.buffered_bytes += len(data)
        while self.buffered_bytes > _REPLAY_LIMIT and self.output_buffer:
            dropped = self.output_buffer.popleft()
            self.buffered_bytes -= len(dropped)
            self.buffer_truncated = True

    async def _deliver_output(self, data: bytes) -> None:
        async with self.attachment_lock:
            sender = self.sender
            if sender is None:
                self._buffer_output(data)
                return
            try:
                await sender.send(
                    {"type": "terminal.output", "terminal_id": self.terminal_id},
                    data,
                )
            except _CONNECTION_ERRORS:
                if self.sender is sender:
                    self.sender = None
                self._buffer_output(data)

    async def _pump_output(self) -> None:
        while True:
            data = await self.queue.get()
            if data is None:
                return
            await self._deliver_output(data)

    async def _send_exit(self, *, exit_code: int | None, exit_signal: int | None) -> None:
        async with self.attachment_lock:
            sender = self.sender
            if sender is None:
                return
            try:
                await sender.send(
                    {
                        "type": "terminal.exit",
                        "terminal_id": self.terminal_id,
                        "exit_code": exit_code,
                        "signal": exit_signal,
                    }
                )
            except _CONNECTION_ERRORS:
                if self.sender is sender:
                    self.sender = None

    async def _wait_for_exit(self) -> None:
        _, status = await asyncio.to_thread(os.waitpid, self.pid, 0)
        self._stop_reader()

        # Drain bytes that reached the PTY before child exit but not yet the event loop.
        while True:
            try:
                data = os.read(self.master_fd, _CHUNK)
            except (BlockingIOError, OSError):
                break
            if not data:
                break
            self.queue.put_nowait(data)

        try:
            os.close(self.master_fd)
        except OSError:
            pass

        if self.pump_task is not None and not self.pump_task.done():
            self.queue.put_nowait(None)
            await self.pump_task

        if os.WIFEXITED(status):
            exit_code = os.WEXITSTATUS(status)
            exit_signal = None
        elif os.WIFSIGNALED(status):
            exit_code = None
            exit_signal = os.WTERMSIG(status)
        else:
            exit_code = None
            exit_signal = None

        self.closed = True
        await self._send_exit(exit_code=exit_code, exit_signal=exit_signal)

    async def attach(self, sender: LockedFrameWriter) -> tuple[int, bool]:
        """Attach a transport and replay output produced while detached."""
        async with self.attachment_lock:
            if self.closed:
                raise RuntimeError("terminal is closed")
            if self.sender is not None and self.sender is not sender:
                raise RuntimeError("terminal is already attached")
            if self.sender is sender:
                return 0, False

            replay = list(self.output_buffer)
            replayed_bytes = self.buffered_bytes
            replay_truncated = self.buffer_truncated
            self.output_buffer.clear()
            self.buffered_bytes = 0
            self.buffer_truncated = False
            self.sender = sender

            for index, data in enumerate(replay):
                try:
                    await sender.send(
                        {"type": "terminal.output", "terminal_id": self.terminal_id},
                        data,
                    )
                except _CONNECTION_ERRORS as exc:
                    if self.sender is sender:
                        self.sender = None
                    if replay_truncated:
                        self.buffer_truncated = True
                    for remaining in replay[index:]:
                        self._buffer_output(remaining)
                    raise RuntimeError("terminal attach connection closed") from exc

            return replayed_bytes, replay_truncated

    async def detach(self, sender: LockedFrameWriter) -> bool:
        async with self.attachment_lock:
            if self.sender is not sender:
                return False
            self.sender = None
            return True

    def is_attached_to(self, sender: LockedFrameWriter) -> bool:
        return self.sender is sender

    async def write(self, data: bytes) -> None:
        if self.closed:
            raise RuntimeError("terminal is closed")
        view = memoryview(data)
        while view:
            try:
                written = os.write(self.master_fd, view)
                view = view[written:]
            except BlockingIOError:
                await asyncio.sleep(0)

    def resize(self, rows: int, cols: int) -> None:
        import fcntl
        import termios

        fcntl.ioctl(
            self.master_fd,
            termios.TIOCSWINSZ,
            struct.pack("HHHH", rows, cols, 0, 0),
        )

    def send_signal(self, value: str | int) -> None:
        sig = parse_signal(value)
        try:
            os.killpg(self.pid, sig)
        except ProcessLookupError:
            pass

    async def close(self) -> None:
        if self.closed:
            return
        await terminate_process_group(self.pid)
        if self.wait_task is not None:
            try:
                await asyncio.wait_for(asyncio.shield(self.wait_task), timeout=2.0)
            except (asyncio.TimeoutError, BrokenPipeError, ConnectionResetError):
                pass
