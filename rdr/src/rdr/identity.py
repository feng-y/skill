from __future__ import annotations

import os
import platform
import socket
from typing import Any


def runtime_identity() -> dict[str, Any]:
    return {
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "uid": os.getuid() if hasattr(os, "getuid") else None,
        "gid": os.getgid() if hasattr(os, "getgid") else None,
        "cwd": os.getcwd(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "machine": platform.machine(),
        "kernel": platform.release(),
    }
