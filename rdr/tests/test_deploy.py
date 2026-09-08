from __future__ import annotations

import json
import os
import socket
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from rdr.deploy import (
    _auth_check,
    _is_rdr_server,
    _pid_alive,
    _port_open,
    _read_pid_file,
    _resolve_server_token,
)
from rdr.runtime import RDRServer


class ServerTokenTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        self.config = Path(self.root.name) / "access.json"
        self.config.write_text(
            json.dumps({"enabled": True, "tokens": ["file-token"]}),
            encoding="utf-8",
        )

    @staticmethod
    def _env(token: str | None) -> dict[str, str]:
        env = dict(os.environ)
        env.pop("RDR_TOKEN", None)
        if token is not None:
            env["RDR_TOKEN"] = token
        return env

    def test_explicit_token_wins(self) -> None:
        with patch.dict(os.environ, self._env("env-token"), clear=True):
            token, source = _resolve_server_token("flag-token", str(self.config))
        self.assertEqual((token, source), ("flag-token", "--token"))

    def test_env_token_next(self) -> None:
        with patch.dict(os.environ, self._env("env-token"), clear=True):
            token, source = _resolve_server_token(None, str(self.config))
        self.assertEqual((token, source), ("env-token", "RDR_TOKEN env"))

    def test_config_file_fallback_defers_to_child(self) -> None:
        with patch.dict(os.environ, self._env(None), clear=True):
            token, source = _resolve_server_token(None, str(self.config))
        self.assertIsNone(token)
        self.assertIn("config", source)

    def test_missing_everything_starts_without_token(self) -> None:
        with patch.dict(os.environ, self._env(None), clear=True):
            token, source = _resolve_server_token(
                None, str(self.config.with_suffix(".missing"))
            )
        self.assertIsNone(token)
        self.assertEqual(source, "not configured")

    def test_invalid_config_file_fails(self) -> None:
        self.config.write_text("{}", encoding="utf-8")
        with patch.dict(os.environ, self._env(None), clear=True):
            with self.assertRaises(SystemExit):
                _resolve_server_token(None, str(self.config))


class AuthCheckTest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self) -> None:
        self.server = RDRServer("127.0.0.1", 0, ("secret",))
        await self.server.set_enabled(True)
        self.port = self.server.listener.sockets[0].getsockname()[1]
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        self.missing_config = str(Path(self.root.name) / "missing.json")

    async def asyncTearDown(self) -> None:
        await self.server.close()

    @staticmethod
    def _without_token() -> dict[str, str]:
        env = dict(os.environ)
        env.pop("RDR_TOKEN", None)
        return env

    async def test_auth_states_are_distinct(self) -> None:
        with patch.dict(os.environ, self._without_token(), clear=True):
            self.assertEqual(
                await _auth_check(self.port, self.missing_config),
                "client token not configured",
            )

        with patch.dict(os.environ, {"RDR_TOKEN": "wrong"}, clear=False):
            self.assertEqual(
                await _auth_check(self.port, self.missing_config),
                "invalid token",
            )

        with patch.dict(os.environ, {"RDR_TOKEN": "secret"}, clear=False):
            self.assertEqual(await _auth_check(self.port, self.missing_config), "ok")

        await self.server.set_tokens(())
        with patch.dict(os.environ, self._without_token(), clear=True):
            self.assertEqual(
                await _auth_check(self.port, self.missing_config),
                "server token not configured",
            )


class PidFileTest(unittest.TestCase):
    def test_read_valid_and_invalid(self) -> None:
        root = tempfile.TemporaryDirectory()
        self.addCleanup(root.cleanup)
        path = Path(root.name) / "server.pid"

        self.assertIsNone(_read_pid_file(path))

        path.write_text(json.dumps({"pid": 1234, "port": 19090}), encoding="utf-8")
        record = _read_pid_file(path)
        self.assertEqual(record["pid"], 1234)
        self.assertEqual(record["port"], 19090)

        path.write_text("not json", encoding="utf-8")
        self.assertIsNone(_read_pid_file(path))

    def test_pid_alive_and_process_guard(self) -> None:
        self.assertTrue(_pid_alive(os.getpid()))
        self.assertFalse(_pid_alive(2**24))
        # the test runner command line is not rdr-server
        self.assertFalse(_is_rdr_server(os.getpid()))


class PortTest(unittest.TestCase):
    def test_port_open_reflects_listener(self) -> None:
        sock = socket.socket()
        self.addCleanup(sock.close)
        sock.bind(("127.0.0.1", 0))
        sock.listen(1)
        port = sock.getsockname()[1]

        self.assertTrue(_port_open("127.0.0.1", port))

        sock.close()
        self.assertFalse(_port_open("127.0.0.1", port))


if __name__ == "__main__":
    unittest.main()
