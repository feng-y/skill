from __future__ import annotations

import asyncio
import io
import json
import os
import stat
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from rdr.cli import (
    _connect,
    build_parser,
    parse_endpoint,
    parse_remote_spec,
    resolve_access_config_path,
)
from rdr.server import env_access_tokens


class _StubClient:
    instances: list["_StubClient"] = []

    def __init__(self, host: str, port: int, token: str) -> None:
        self.host = host
        self.port = port
        self.token = token
        self.connected = False
        _StubClient.instances.append(self)

    async def connect(self) -> dict[str, object]:
        self.connected = True
        return {}


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

    def test_root_help_exposes_stateless_vs_stateful_choice(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                build_parser().parse_args(["--help"])
        self.assertEqual(raised.exception.code, 0)
        help_text = output.getvalue()
        self.assertIn("stateless one-shot remote work", help_text)
        self.assertIn("stateful remote terminal", help_text)
        self.assertIn("rdr connect --help", help_text)

    def test_connect_help_exposes_stateful_discovery(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                build_parser().parse_args(["connect", "--help"])
        self.assertEqual(raised.exception.code, 0)
        help_text = output.getvalue()
        self.assertIn("stateful remote terminal", help_text)
        self.assertIn("multiple interactions or transport reconnects", help_text)
        self.assertIn("--terminal-id", help_text)
        self.assertIn("--attach", help_text)
        self.assertIn("prefer `rdr exec`", help_text)

    def test_server_help_prefers_config_or_env_over_token_argument(self) -> None:
        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                build_parser().parse_args(["server", "--help"])
        self.assertEqual(raised.exception.code, 0)
        help_text = output.getvalue()
        self.assertIn("recommended token sources", help_text)
        self.assertIn("/etc/rdr/access.json", help_text)
        self.assertIn("shell history", help_text)
        self.assertNotIn("quick start: rdr server start --token", help_text)

        output = io.StringIO()
        with redirect_stdout(output):
            with self.assertRaises(SystemExit) as raised:
                build_parser().parse_args(["server", "start", "--help"])
        self.assertEqual(raised.exception.code, 0)
        start_help = output.getvalue()
        self.assertIn("compatibility option", start_help)
        self.assertIn("prefer RDR_TOKEN", " ".join(start_help.split()))


class EnvTokenTest(unittest.TestCase):
    def test_env_access_tokens_parses_rdr_token(self) -> None:
        with patch.dict(os.environ, {"RDR_TOKEN": "env-token"}, clear=False):
            self.assertEqual(env_access_tokens(), ("env-token",))
        with patch.dict(os.environ, {"RDR_TOKEN": "   "}, clear=False):
            self.assertEqual(env_access_tokens(), ())
        env = dict(os.environ)
        env.pop("RDR_TOKEN", None)
        with patch.dict(os.environ, env, clear=True):
            self.assertEqual(env_access_tokens(), ())


class ConnectTokenSourceTest(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        _StubClient.instances = []
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        self.access = Path(self.root.name) / "access.json"
        self.access.write_text(
            json.dumps({"enabled": True, "tokens": ["file-token", "second"]}),
            encoding="utf-8",
        )

    async def test_rdr_token_overrides_access_config(self) -> None:
        with patch.dict(
            os.environ,
            {"RDR_TOKEN": "env-token", "RDR_ACCESS_CONFIG": str(self.access)},
            clear=False,
        ), patch("rdr.cli.RDRClient", _StubClient):
            client = await _connect(("host.example", 19090), None)
        self.assertEqual(client.token, "env-token")
        self.assertTrue(client.connected)

    async def test_access_config_first_token_is_used_without_env(self) -> None:
        env = dict(os.environ)
        env.pop("RDR_TOKEN", None)
        env["RDR_ACCESS_CONFIG"] = str(self.access)
        with patch.dict(os.environ, env, clear=True), patch(
            "rdr.cli.RDRClient", _StubClient
        ):
            client = await _connect(("host.example", 19090), None)
        self.assertEqual(client.token, "file-token")

    async def test_explicit_access_config_selects_file_despite_inherited_token(self) -> None:
        with patch.dict(os.environ, {"RDR_TOKEN": "stale-token"}), patch(
            "rdr.cli.RDRClient", _StubClient
        ):
            client = await _connect(("host.example", 19090), str(self.access))
            self.assertEqual(client.token, "file-token")
            with self.assertRaisesRegex(SystemExit, "cannot read config"):
                await _connect(("host.example", 19090), str(self.access.with_suffix(".missing")))

    async def test_missing_config_and_no_env_token_fails(self) -> None:
        env = dict(os.environ)
        env.pop("RDR_TOKEN", None)
        env["RDR_ACCESS_CONFIG"] = str(self.access.with_suffix(".missing"))
        with patch.dict(os.environ, env, clear=True), patch(
            "rdr.cli.RDRClient", _StubClient
        ):
            with self.assertRaises(SystemExit):
                await _connect(("host.example", 19090), None)


class ImportTokenTest(unittest.TestCase):
    INSTALLER = """#!/bin/bash
exit 42
cat >"$config_tmp" <<'JSON'
{"tokens": ["installer-fixture"]}
JSON
"""

    def setUp(self) -> None:
        root = tempfile.TemporaryDirectory()
        self.addCleanup(root.cleanup)
        self.access = Path(root.name) / "access.json"

    def import_token(self, installer: str = INSTALLER) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, "-m", "rdr.cli", "config", "import-token", "--access-config", str(self.access)],
            input=installer, capture_output=True, text=True,
        )
        self.assertNotIn("installer-fixture", result.stdout + result.stderr)
        return result

    def test_import_repairs_missing_tokens_and_preserves_other_fields(self) -> None:
        self.access.write_text('{"enabled": true}')
        self.import_token().check_returncode()
        self.assertEqual(json.loads(self.access.read_text()), {"enabled": True, "tokens": ["installer-fixture"]})

        self.access.write_text('{"tokens": ["other", "installer-fixture"]}')
        for _ in range(2):
            self.import_token().check_returncode()
            self.assertEqual(json.loads(self.access.read_text()), {"tokens": ["installer-fixture", "other"]})
            self.assertEqual(stat.S_IMODE(self.access.stat().st_mode), 0o600)

    def test_import_refuses_invalid_config_or_ambiguous_installer(self) -> None:
        self.access.write_text('{"tokens": null}')
        self.assertIn("requires array 'tokens'", self.import_token().stderr)
        self.assertEqual(self.access.read_text(), '{"tokens": null}')
        self.assertIn("expected one", self.import_token(self.INSTALLER * 2).stderr)
        self.assertEqual(self.access.read_text(), '{"tokens": null}')

    @unittest.skipUnless(os.geteuid() == 0, "requires chown to another UID and GID")
    def test_import_preserves_existing_owner_and_group(self) -> None:
        self.access.write_text('{"tokens": []}')
        os.chown(self.access, 65534, 65534)
        self.import_token().check_returncode()
        metadata = self.access.stat()
        self.assertEqual((metadata.st_uid, metadata.st_gid), (65534, 65534))
        self.assertEqual(stat.S_IMODE(metadata.st_mode), 0o600)


if __name__ == "__main__":
    unittest.main()
