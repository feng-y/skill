from __future__ import annotations

import argparse
import asyncio
import os
import re
import shutil
import signal
import sys

from .client import RDRClient, RDRClientError
from .config import ConfigError, resolve_access_token
from .deploy import default_log_file, default_state_dir, run_server_command

DEFAULT_ACCESS_CONFIG = "~/.config/rdr/access.json"
_REMOTE_SPEC = re.compile(r"^(?P<host>\[[^\]]+\]|[^:]+):(?P<port>\d+):(?P<path>.+)$")


def parse_endpoint(value: str) -> tuple[str, int]:
    if ":" not in value:
        raise argparse.ArgumentTypeError("endpoint must be HOST:PORT")
    host, raw_port = value.rsplit(":", 1)
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]
    try:
        port = int(raw_port)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("endpoint port must be an integer") from exc
    if not host or port <= 0 or port > 65535:
        raise argparse.ArgumentTypeError("invalid endpoint")
    return host, port


def parse_remote_spec(value: str) -> tuple[tuple[str, int], str]:
    match = _REMOTE_SPEC.fullmatch(value)
    if match is None:
        raise argparse.ArgumentTypeError(
            "remote path must be HOST:PORT:PATH; bracket IPv6 hosts"
        )
    host = match.group("host")
    if host.startswith("[") and host.endswith("]"):
        host = host[1:-1]
    port = int(match.group("port"))
    path = match.group("path")
    if port <= 0 or port > 65535 or not path:
        raise argparse.ArgumentTypeError("invalid remote path")
    return (host, port), path


def resolve_access_config_path(value: str | None) -> str:
    configured = value or os.environ.get("RDR_ACCESS_CONFIG") or DEFAULT_ACCESS_CONFIG
    return os.path.expanduser(configured)


def _add_access_config(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--access-config",
        help=(
            "client access config JSON; defaults to RDR_ACCESS_CONFIG or "
            "~/.config/rdr/access.json. RDR_TOKEN overrides the file token"
        ),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="RDR remote runtime client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "execution shapes:\n"
            "  rdr exec ...      stateless one-shot remote work\n"
            "  rdr connect ...   stateful remote terminal for work whose process "
            "state must survive multiple interactions or transport reconnects\n\n"
            "Use `rdr connect --help` to discover stateful terminal controls."
        ),
    )
    sub = parser.add_subparsers(dest="command", required=True)

    connect_parser = sub.add_parser(
        "connect",
        help="open or attach a stateful remote terminal",
        description=(
            "Open or attach a stateful remote terminal.\n\n"
            "Use this when the remote process must keep state across multiple "
            "interactions or transport reconnects. For one-shot remote work, "
            "prefer `rdr exec`."
        ),
        epilog=(
            "examples:\n"
            "  rdr connect HOST:PORT --terminal-id debug\n"
            "  rdr connect HOST:PORT --attach debug\n\n"
            "A transport disconnect detaches only that client. The remote terminal "
            "continues until its process exits, it is explicitly closed, access is "
            "revoked, or the RDR server stops."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    connect_parser.add_argument("endpoint", type=parse_endpoint, metavar="HOST:PORT")
    connect_parser.add_argument("--cwd")
    terminal_group = connect_parser.add_mutually_exclusive_group()
    terminal_group.add_argument(
        "--terminal-id",
        help="stable id for a newly opened stateful terminal; generated when omitted",
    )
    terminal_group.add_argument(
        "--attach",
        metavar="TERMINAL_ID",
        help="attach to an existing stateful terminal owned by the remote runtime",
    )
    _add_access_config(connect_parser)

    exec_parser = sub.add_parser(
        "exec", help="run one stateless remote shell command"
    )
    exec_parser.add_argument("endpoint", type=parse_endpoint, metavar="HOST:PORT")
    exec_parser.add_argument("remote_command")
    exec_parser.add_argument("--cwd")
    exec_parser.add_argument("--timeout", type=float)
    _add_access_config(exec_parser)

    identity_parser = sub.add_parser("identity", help="show remote runtime identity")
    identity_parser.add_argument("endpoint", type=parse_endpoint, metavar="HOST:PORT")
    _add_access_config(identity_parser)

    get_parser = sub.add_parser("get", help="download a remote file")
    get_parser.add_argument(
        "remote", type=parse_remote_spec, metavar="HOST:PORT:REMOTE_PATH"
    )
    get_parser.add_argument("local_path")
    _add_access_config(get_parser)

    put_parser = sub.add_parser("put", help="upload a local file")
    put_parser.add_argument("local_path")
    put_parser.add_argument(
        "remote", type=parse_remote_spec, metavar="HOST:PORT:REMOTE_PATH"
    )
    _add_access_config(put_parser)

    server_parser = sub.add_parser(
        "server",
        help="manage the local rdr-server (start/status/stop)",
        description=(
            "Install and startup are separate: the package is installed with "
            "pip once, then started/stopped with these commands.\n\n"
            "token sources, in priority order: --token > RDR_TOKEN env > "
            "server access config file (/etc/rdr/access.json by default).\n"
            "A server without any token still starts and listens, but rejects "
            "auth with 'server token not configured' until one is configured.\n\n"
            "quick start: rdr server start --token <token> ; rdr server status\n"
            "full flow: rdr/GUIDE.md"
        ),
    )
    server_parser.formatter_class = argparse.RawDescriptionHelpFormatter
    server_sub = server_parser.add_subparsers(dest="server_command", required=True)

    start_parser = server_sub.add_parser(
        "start", help="start rdr-server in the background and wait until ready"
    )
    start_parser.add_argument("--host", default="0.0.0.0")
    start_parser.add_argument("--port", type=int, default=19090)
    start_parser.add_argument(
        "--token",
        help=(
            "server access token; defaults to RDR_TOKEN env, then the server "
            "access config file. Passed to the child via environment"
        ),
    )
    start_parser.add_argument(
        "--access-config",
        help="server access config JSON; defaults to RDR_ACCESS_CONFIG or /etc/rdr/access.json",
    )
    start_parser.add_argument("--pid-file", default=str(default_state_dir() / "server.pid"))
    start_parser.add_argument("--log-file", default=str(default_log_file()))
    start_parser.add_argument("--wait-seconds", type=float, default=10.0)

    status_parser = server_sub.add_parser(
        "status", help="report local rdr-server process, listener and auth state"
    )
    status_parser.add_argument("--port", type=int, default=19090)
    status_parser.add_argument("--pid-file", default=str(default_state_dir() / "server.pid"))
    _add_access_config(status_parser)

    stop_parser = server_sub.add_parser("stop", help="stop the managed rdr-server")
    stop_parser.add_argument("--pid-file", default=str(default_state_dir() / "server.pid"))
    return parser


async def _connect(
    endpoint: tuple[str, int],
    access_config: str | None,
) -> RDRClient:
    host, port = endpoint
    access_path = resolve_access_config_path(access_config)
    try:
        token = resolve_access_token(access_path)
    except ConfigError as exc:
        raise SystemExit(str(exc)) from exc

    client = RDRClient(host, port, token)
    await client.connect()
    return client


async def _run_exec(client: RDRClient, args: argparse.Namespace) -> int:
    def stdout(data: bytes) -> None:
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush()

    def stderr(data: bytes) -> None:
        sys.stderr.buffer.write(data)
        sys.stderr.buffer.flush()

    result = await client.exec(
        args.remote_command,
        cwd=args.cwd,
        timeout=args.timeout,
        on_stdout=stdout,
        on_stderr=stderr,
        capture_limit=0,
    )
    return int(result["exit_code"] or 0)


async def _run_connect(client: RDRClient, args: argparse.Namespace) -> int:
    if os.name != "posix" or not sys.stdin.isatty() or not sys.stdout.isatty():
        raise RDRClientError("interactive connect requires a POSIX TTY")

    import termios
    import tty

    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    size = shutil.get_terminal_size((80, 24))
    if args.attach:
        terminal = await client.attach_terminal(args.attach)
        await terminal.resize(size.lines, size.columns)
    else:
        terminal = await client.open_terminal(
            cwd=args.cwd,
            rows=size.lines,
            cols=size.columns,
            terminal_id=args.terminal_id,
        )

    print(f"rdr terminal id: {terminal.terminal_id}", file=sys.stderr, flush=True)
    if terminal.replay_truncated:
        print(
            "rdr: detached terminal output exceeded replay buffer; oldest output was dropped",
            file=sys.stderr,
            flush=True,
        )

    loop = asyncio.get_running_loop()
    input_queue: asyncio.Queue[bytes | None] = asyncio.Queue()

    def readable() -> None:
        try:
            data = os.read(fd, 65536)
        except OSError:
            data = b""
        input_queue.put_nowait(data or None)

    def resized() -> None:
        current = shutil.get_terminal_size((80, 24))
        asyncio.create_task(terminal.resize(current.lines, current.columns))

    async def input_loop() -> None:
        while True:
            data = await input_queue.get()
            if data is None:
                return
            await terminal.write(data)

    async def output_loop() -> int:
        while True:
            header, payload = await terminal.read()
            frame_type = header.get("type")
            if frame_type == "terminal.output":
                os.write(sys.stdout.fileno(), payload)
            elif frame_type == "terminal.exit":
                code = header.get("exit_code")
                return int(code) if isinstance(code, int) else 1
            elif frame_type in {"terminal.error", "connection.closed"}:
                raise RDRClientError(header.get("error", "terminal failed"))

    try:
        tty.setraw(fd)
        loop.add_reader(fd, readable)
        if hasattr(signal, "SIGWINCH"):
            loop.add_signal_handler(signal.SIGWINCH, resized)

        input_task = asyncio.create_task(input_loop())
        output_task = asyncio.create_task(output_loop())
        done, pending = await asyncio.wait(
            {input_task, output_task},
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
        await asyncio.gather(*pending, return_exceptions=True)
        if output_task in done:
            return output_task.result()
        # Local TTY disappeared while the remote process is still alive.
        # Preserve the stateful session instead of terminating it.
        await terminal.detach()
        return 0
    finally:
        loop.remove_reader(fd)
        if hasattr(signal, "SIGWINCH"):
            try:
                loop.remove_signal_handler(signal.SIGWINCH)
            except Exception:
                pass
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)


async def run(args: argparse.Namespace) -> int:
    if args.command == "server":
        return await run_server_command(args)

    if args.command == "get":
        endpoint, remote_path = args.remote
    elif args.command == "put":
        endpoint, remote_path = args.remote
    else:
        endpoint = args.endpoint
        remote_path = None

    client = await _connect(endpoint, args.access_config)
    try:
        if args.command == "connect":
            return await _run_connect(client, args)
        if args.command == "exec":
            return await _run_exec(client, args)
        if args.command == "get":
            assert remote_path is not None
            size = await client.download(remote_path, args.local_path)
            print(f"{size} bytes downloaded", file=sys.stderr)
            return 0
        if args.command == "put":
            assert remote_path is not None
            size = await client.upload(args.local_path, remote_path)
            print(f"{size} bytes uploaded", file=sys.stderr)
            return 0
        if args.command == "identity":
            identity = await client.get_identity()
            for key, value in identity.items():
                print(f"{key}: {value}")
            return 0
        raise AssertionError(args.command)
    finally:
        await client.close()


def main() -> None:
    args = build_parser().parse_args()
    try:
        raise SystemExit(asyncio.run(run(args)))
    except KeyboardInterrupt:
        raise SystemExit(130)
    except RDRClientError as exc:
        print(f"rdr: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
