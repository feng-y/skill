from __future__ import annotations

import asyncio
import os
import signal


async def terminate_process_group(
    pid: int,
    *,
    grace_seconds: float = 1.0,
) -> None:
    """Terminate a process group created with a fresh session.

    Missing processes are treated as already terminated.
    """
    try:
        os.killpg(pid, signal.SIGTERM)
    except ProcessLookupError:
        return

    deadline = asyncio.get_running_loop().time() + grace_seconds
    while asyncio.get_running_loop().time() < deadline:
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return
        await asyncio.sleep(0.05)

    try:
        os.killpg(pid, signal.SIGKILL)
    except ProcessLookupError:
        pass


def parse_signal(name_or_number: str | int) -> signal.Signals:
    if isinstance(name_or_number, int):
        return signal.Signals(name_or_number)

    value = name_or_number.strip().upper()
    if not value.startswith("SIG"):
        value = f"SIG{value}"
    try:
        return signal.Signals(getattr(signal, value))
    except (AttributeError, ValueError) as exc:
        raise ValueError(f"unsupported signal: {name_or_number}") from exc
