from __future__ import annotations

import argparse
import asyncio
import logging
import os
import signal

from .access import AccessConfigWatcher
from .config import AccessConfig, ConfigError
from .runtime import RDRServer

__all__ = ["RDRServer"]

logger = logging.getLogger(__name__)


async def run_server(args: argparse.Namespace) -> None:
    watcher = AccessConfigWatcher(
        args.access_config,
        args.global_access_config,
        poll_seconds=args.access_poll_seconds,
    )
    try:
        policy = watcher.load_initial()
    except ConfigError as exc:
        raise SystemExit(str(exc)) from exc

    server = RDRServer(args.host, args.port, policy.tokens)
    stop_event = asyncio.Event()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, stop_event.set)
        except NotImplementedError:
            pass

    async def apply(next_policy: AccessConfig) -> None:
        await server.set_access(next_policy.enabled, next_policy.tokens)

    await apply(policy)
    access_task = asyncio.create_task(
        watcher.watch(apply, stop_event=stop_event),
        name="rdr-access-watcher",
    )
    stop_task = asyncio.create_task(stop_event.wait(), name="rdr-stop-waiter")

    try:
        done, _ = await asyncio.wait(
            {access_task, stop_task},
            return_when=asyncio.FIRST_COMPLETED,
        )
        if access_task in done and not stop_event.is_set():
            exception = access_task.exception()
            if exception is not None:
                raise RuntimeError("RDR access watcher stopped unexpectedly") from exception
            raise RuntimeError("RDR access watcher stopped unexpectedly")
    finally:
        stop_event.set()
        for task in (access_task, stop_task):
            if not task.done():
                task.cancel()
        await asyncio.gather(access_task, stop_task, return_exceptions=True)
        await server.close()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="RDR remote diagnostic runtime")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", type=int, default=19090)
    parser.add_argument(
        "--access-config",
        default=os.environ.get("RDR_ACCESS_CONFIG", "/etc/rdr/access.json"),
        help="host-local access config JSON",
    )
    parser.add_argument(
        "--global-access-config",
        default=os.environ.get(
            "RDR_GLOBAL_ACCESS_CONFIG", "/data/bucket/rdr/access.json"
        ),
        help="optional shared access config JSON on the mounted bucket",
    )
    parser.add_argument("--access-poll-seconds", type=float, default=30.0)
    parser.add_argument("-v", "--verbose", action="count", default=0)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    level = logging.WARNING
    if args.verbose == 1:
        level = logging.INFO
    elif args.verbose >= 2:
        level = logging.DEBUG
    logging.basicConfig(level=level)
    asyncio.run(run_server(args))


if __name__ == "__main__":
    main()
