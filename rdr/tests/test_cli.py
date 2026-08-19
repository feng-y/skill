from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from rdr.cli import (
    build_parser,
    parse_endpoint,
    parse_remote_spec,
    resolve_access_config_path,
)


class CLITest(unittest.TestCase):
    def test_connect_uses_positional_endpoint(self) -> None:
        args = build_parser().parse_args(["connect", "host.example:19090"])
        self.assertEqual(args.command, "connect")
        self.assertEqual(args.endpoint, ("host.example", 19090))

    def test_exec_uses_positional_endpoint_and_command(self) -> None:
        args = build_parser().parse_args(
            ["exec", "host.example:19090", "ps -ef", "--timeout", "5"]
        )
        self.assertEqual(args.endpoint, ("host.example", 19090))
        self.assertEqual(args.remote_command, "ps -ef")
        self.assertEqual(args.timeout, 5.0)

    def test_get_and_put_use_remote_spec(self) -> None:
        get_args = build_parser().parse_args(
            ["get", "host.example:19090:/tmp/perf.data", "./perf.data"]
        )
        self.assertEqual(
            get_args.remote,
            (("host.example", 19090), "/tmp/perf.data"),
        )
        self.assertEqual(get_args.local_path, "./perf.data")

        put_args = build_parser().parse_args(
            ["put", "./inspect.py", "host.example:19090:/tmp/inspect.py"]
        )
        self.assertEqual(
            put_args.remote,
            (("host.example", 19090), "/tmp/inspect.py"),
        )
        self.assertEqual(put_args.local_path, "./inspect.py")

    def test_bracketed_ipv6_is_supported(self) -> None:
        self.assertEqual(parse_endpoint("[::1]:19090"), ("::1", 19090))
        self.assertEqual(
            parse_remote_spec("[::1]:19090:/tmp/x"),
            (("::1", 19090), "/tmp/x"),
        )

    def test_access_config_defaults_to_user_config(self) -> None:
        env = dict(os.environ)
        env.pop("RDR_ACCESS_CONFIG", None)
        env["HOME"] = "/tmp/rdr-home"
        with patch.dict(os.environ, env, clear=True):
            self.assertEqual(
                resolve_access_config_path(None),
                "/tmp/rdr-home/.config/rdr/access.json",
            )

    def test_access_config_env_and_cli_override(self) -> None:
        with patch.dict(
            os.environ,
            {"RDR_ACCESS_CONFIG": "/env/access.json"},
            clear=False,
        ):
            self.assertEqual(resolve_access_config_path(None), "/env/access.json")
            self.assertEqual(
                resolve_access_config_path("/cli/access.json"),
                "/cli/access.json",
            )


if __name__ == "__main__":
    unittest.main()
