from __future__ import annotations

import asyncio
import os
import time
from dataclasses import dataclass

from .process import terminate_process_group
from .protocol import LockedFrameWriter

_CHUNK = 256 * 1024


@dataclass
class ExecHandle:
    request_id: str
    task: asyncio.Task[None]
    process: asyncio.subprocess.Process | None = None


async def run_exec(
    handle: ExecHandle,
    sender: LockedFrameWriter,
    *,
    command: str,
    cwd: str | None,
    env: dict[str, str] | None,
    timeout: float | None,
) -> None:
    child_env = os.environ.copy()
    if env:
        child_env.update({str(k): str(v) for k, v in env.items()})

    started = time.monotonic()
    timed_out = False
    process: asyncio.subprocess.Process | None = None
    try:
        process = await asyncio.create_subprocess_exec(
            "/bin/bash",
            "-lc",
            command,
            cwd=cwd,
            env=child_env,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            start_new_session=True,
        )
        handle.process = process
        await sender.send(
            {"type": "exec.started", "request_id": handle.request_id, "pid": process.pid}
        )

        async def pump(stream: asyncio.StreamReader | None, stream_type: str) -> None:
            if stream is None:
                return
            while True:
                data = await stream.read(_CHUNK)
                if not data:
                    return
                await sender.send(
                    {"type": stream_type, "request_id": handle.request_id},
                    data,
                )

        stdout_task = asyncio.create_task(pump(process.stdout, "exec.stdout"))
        stderr_task = asyncio.create_task(pump(process.stderr, "exec.stderr"))
        try:
            if timeout is None:
                await process.wait()
            else:
                try:
                    await asyncio.wait_for(process.wait(), timeout=timeout)
                except asyncio.TimeoutError:
                    timed_out = True
                    await terminate_process_group(process.pid)
                    await process.wait()
            await asyncio.gather(stdout_task, stderr_task)
        finally:
            for task in (stdout_task, stderr_task):
                if not task.done():
                    task.cancel()

        await sender.send(
            {
                "type": "exec.exit",
                "request_id": handle.request_id,
                "exit_code": process.returncode,
                "timed_out": timed_out,
                "duration_ms": int((time.monotonic() - started) * 1000),
            }
        )
    except asyncio.CancelledError:
        if process is not None and process.returncode is None:
            await terminate_process_group(process.pid)
            await process.wait()
        raise
    except Exception as exc:
        await sender.send(
            {"type": "exec.error", "request_id": handle.request_id, "error": str(exc)}
        )


async def cancel_exec(handle: ExecHandle) -> None:
    if handle.process is not None and handle.process.returncode is None:
        await terminate_process_group(handle.process.pid)
