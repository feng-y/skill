"""Managed server start/status/stop for hosts without a supervisor.

`rdr server start` launches `rdr-server` detached (own session, log file,
pid file) and confirms readiness by polling the listener. `rdr server
status` reports process, listener and auth state. `rdr server stop`
terminates gracefully. Production hosts with systemd/supervisor can ignore
this module and run `rdr-server` in the foreground.
"""

from __future__ import annotations

import asyncio
import json
import os
import signal
import socket
import subprocess
import sys
import time
from pathlib import Path

from .client import RDRClient, RDRClientError
from .config import AccessConfig, ConfigError

DEFAULT_ACCESS_CONFIG = "/etc/rdr/access.json"
DEFAULT_WAIT_SECONDS = 10.0
_STOP_TIMEOUT_SECONDS = 10.0


def default_state_dir() -> Path:
    for candidate in (Path("/run/rdr"), Path.home() / ".rdr"):
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            if os.access(candidate, os.W_OK):
                return candidate
        except OSError:
            continue
    raise SystemExit("rdr server: no writable state directory for pid file")


def default_log_file() -> Path:
    candidate = Path("/var/log/rdr")
    try:
        candidate.mkdir(parents=True, exist_ok=True)
        if os.access(candidate, os.W_OK):
            return candidate / "server.log"
    except OSError:
        pass
    return default_state_dir() / "server.log"


def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def _is_rdr_server(pid: int) -> bool:
    try:
        cmdline = Path(f"/proc/{pid}/cmdline").read_bytes().split(b"\0")
    except OSError:
        return False
    return any(b"rdr.server" in part or b"rdr-server" in part for part in cmdline)


def _read_pid_file(pid_file: Path) -> dict | None:
    try:
        value = json.loads(pid_file.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(value, dict) or not isinstance(value.get("pid"), int):
        return None
    return value


def _port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except OSError:
        return False


def _server_access_config_path(access_config: str | None) -> str:
    return (
        access_config
        or os.environ.get("RDR_ACCESS_CONFIG")
        or DEFAULT_ACCESS_CONFIG
    )


def _resolve_server_token(
    explicit_token: str | None, access_config: str | None
) -> tuple[str | None, str]:
    """Return (token_for_child_env, source description).

    Token configuration is optional at startup. An existing config file must
    still be valid; a missing file simply means the server starts with no
    configured token and will reject authentication until one is supplied.
    """
    if explicit_token:
        return explicit_token, "--token"
    env_token = os.environ.get("RDR_TOKEN", "").strip()
    if env_token:
        return env_token, "RDR_TOKEN env"
    path = Path(_server_access_config_path(access_config))
    if path.exists():
        try:
            AccessConfig.load(path)
        except ConfigError as exc:
            raise SystemExit(f"rdr server start: {exc}") from exc
        return None, f"config {path}"
    return None, "not configured"


def _spawn_server(args) -> int:
    token, source = _resolve_server_token(args.token, args.access_config)
    server_access_config = _server_access_config_path(args.access_config)

    pid_file = Path(args.pid_file)
    log_file = Path(args.log_file)
    if pid_file.exists():
        previous = _read_pid_file(pid_file)
        if previous and _pid_alive(previous["pid"]):
            print(
                f"rdr server: already running (pid {previous['pid']}); "
                f"try 'rdr server status'"
            )
            raise SystemExit(1)
        pid_file.unlink()

    child_env = dict(os.environ)
    if token is not None:
        child_env["RDR_TOKEN"] = token

    command = [
        sys.executable,
        "-m",
        "rdr.server",
        "--host",
        args.host,
        "--port",
        str(args.port),
    ]
    if args.access_config:
        command += ["--access-config", args.access_config]

    log_handle = log_file.open("ab")
    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=log_handle,
            stderr=subprocess.STDOUT,
            start_new_session=True,
            env=child_env,
            close_fds=True,
        )
    finally:
        log_handle.close()

    pid_file.parent.mkdir(parents=True, exist_ok=True)
    pid_file.write_text(
        json.dumps(
            {
                "pid": process.pid,
                "host": args.host,
                "port": args.port,
                "token_source": source,
                "access_config": server_access_config,
                "log": str(log_file),
            }
        ),
        encoding="utf-8",
    )

    deadline = time.monotonic() + args.wait_seconds
    while time.monotonic() < deadline:
        if not _pid_alive(process.pid):
            pid_file.unlink(missing_ok=True)
            print(
                f"rdr server: process {process.pid} exited during startup; "
                f"see {log_file}",
                file=sys.stderr,
            )
            raise SystemExit(1)
        if _port_open("127.0.0.1", args.port, timeout=0.5):
            print(
                f"rdr server ready: pid={process.pid} "
                f"listen={args.host}:{args.port} token-source={source} "
                f"log={log_file}"
            )
            return 0
        time.sleep(0.2)

    print(
        f"rdr server: listener {args.host}:{args.port} not ready within "
        f"{args.wait_seconds}s; see {log_file}",
        file=sys.stderr,
    )
    raise SystemExit(1)


def _target_port(args) -> tuple[int, str | None, str | None]:
    record = _read_pid_file(Path(args.pid_file))
    if record:
        return record["port"], record.get("token_source"), record.get("log")
    return args.port, None, None


async def _auth_check(port: int, access_config: str | None) -> str:
    from .cli import resolve_access_config_path
    from .config import resolve_access_token

    client_token_configured = True
    try:
        token = resolve_access_token(resolve_access_config_path(access_config))
    except (ConfigError, SystemExit):
        # An empty token cannot be configured, so it is safe as a probe. The
        # server can then distinguish "no server token" from "client has no
        # usable token for an otherwise configured server".
        token = ""
        client_token_configured = False

    client = RDRClient("127.0.0.1", port, token)
    try:
        await asyncio.wait_for(client.connect(), timeout=3.0)
        return "ok"
    except RDRClientError as exc:
        error = str(exc)
        if error == "server token not configured":
            return "server token not configured"
        if error == "invalid token":
            return "invalid token" if client_token_configured else "client token not configured"
        return "failed"
    except (asyncio.TimeoutError, OSError):
        return "failed"
    finally:
        try:
            await client.close()
        except Exception:
            pass


async def _server_status(args) -> int:
    pid_file = Path(args.pid_file)
    record = _read_pid_file(pid_file)
    port, token_source, log_path = _target_port(args)

    if record is None:
        print(f"rdr server: no pid file at {pid_file}")
        print(f"listener 127.0.0.1:{port}: {'open' if _port_open('127.0.0.1', port) else 'closed'}")
        return 1

    pid = record["pid"]
    alive = _pid_alive(pid)
    print(f"process: pid={pid} {'alive' if alive else 'dead'}")
    if not alive:
        print("rdr server: not running (stale pid file)")
        return 1

    listening = _port_open("127.0.0.1", port)
    print(f"listener 127.0.0.1:{port}: {'open' if listening else 'closed'}")
    print(f"token-source: {token_source or 'unknown'}")
    if log_path:
        print(f"log: {log_path}")

    if not listening:
        return 1

    status_access_config = args.access_config or record.get("access_config")
    auth = await _auth_check(port, status_access_config)
    print(f"auth: {auth}")
    return 0 if auth == "ok" else 1


def _server_stop(args) -> int:
    pid_file = Path(args.pid_file)
    record = _read_pid_file(pid_file)
    if record is None:
        print(f"rdr server: not running (no pid file at {pid_file})")
        return 1

    pid = record["pid"]
    if not _pid_alive(pid) or not _is_rdr_server(pid):
        pid_file.unlink(missing_ok=True)
        print(f"rdr server: not running (stale pid file for pid {pid})")
        return 1

    os.kill(pid, signal.SIGTERM)
    deadline = time.monotonic() + _STOP_TIMEOUT_SECONDS
    while _pid_alive(pid) and time.monotonic() < deadline:
        time.sleep(0.1)
    if _pid_alive(pid):
        os.kill(pid, signal.SIGKILL)
        print(f"rdr server: pid {pid} killed after SIGTERM timeout")
    else:
        print(f"rdr server: stopped (pid {pid})")
    pid_file.unlink(missing_ok=True)
    return 0


async def run_server_command(args) -> int:
    if args.server_command == "start":
        return _spawn_server(args)
    if args.server_command == "stop":
        return _server_stop(args)
    if args.server_command == "status":
        return await _server_status(args)
    raise AssertionError(args.server_command)
