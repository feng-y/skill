from __future__ import annotations

import asyncio
import json
import tempfile
import unittest
from pathlib import Path

from rdr.access import AccessConfigWatcher
from rdr.config import ConfigError


class AccessWatcherTest(unittest.TestCase):
    def setUp(self) -> None:
        self.root = tempfile.TemporaryDirectory()
        self.addCleanup(self.root.cleanup)
        root = Path(self.root.name)
        self.local = root / "local.json"
        self.global_path = root / "global.json"
        self._write(self.local, enabled=True, tokens=["local"])

    @staticmethod
    def _write(path: Path, *, enabled: bool, tokens: list[str]) -> None:
        path.write_text(
            json.dumps({"enabled": enabled, "tokens": tokens}),
            encoding="utf-8",
        )

    def test_global_file_is_optional_until_first_seen(self) -> None:
        watcher = AccessConfigWatcher(self.local, self.global_path)
        policy = watcher.load_initial()
        self.assertTrue(policy.enabled)
        self.assertEqual(policy.tokens, ("local",))

        self._write(self.global_path, enabled=True, tokens=["global"])
        policy = watcher.read_policy()
        self.assertTrue(policy.enabled)
        self.assertEqual(policy.tokens, ("local", "global"))

    def test_invalid_existing_global_file_fails_startup(self) -> None:
        self.global_path.write_text("{}", encoding="utf-8")
        watcher = AccessConfigWatcher(self.local, self.global_path)
        with self.assertRaises(ConfigError):
            watcher.load_initial()

    def test_global_disable_overrides_local_enable(self) -> None:
        self._write(self.global_path, enabled=False, tokens=["global"])
        watcher = AccessConfigWatcher(self.local, self.global_path)
        policy = watcher.load_initial()
        self.assertFalse(policy.enabled)
        self.assertEqual(policy.tokens, ("local", "global"))

    def test_missing_global_after_success_keeps_last_known_state(self) -> None:
        self._write(self.global_path, enabled=False, tokens=["global"])
        watcher = AccessConfigWatcher(self.local, self.global_path)
        policy = watcher.load_initial()
        self.assertFalse(policy.enabled)

        self.global_path.unlink()
        policy = watcher.read_policy()
        self.assertFalse(policy.enabled)
        self.assertEqual(policy.tokens, ("local", "global"))

    def test_local_token_rotation_is_observed(self) -> None:
        watcher = AccessConfigWatcher(self.local, self.global_path)
        watcher.load_initial()
        self._write(self.local, enabled=True, tokens=["rotated"])
        policy = watcher.read_policy()
        self.assertEqual(policy.tokens, ("rotated",))


class AccessWatcherAsyncTest(unittest.IsolatedAsyncioTestCase):
    async def test_failed_policy_apply_is_retried(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            local = Path(td) / "local.json"
            local.write_text(
                json.dumps({"enabled": True, "tokens": ["initial"]}),
                encoding="utf-8",
            )
            watcher = AccessConfigWatcher(local, poll_seconds=0.01)
            watcher.load_initial()
            local.write_text(
                json.dumps({"enabled": True, "tokens": ["rotated"]}),
                encoding="utf-8",
            )

            stop_event = asyncio.Event()
            calls = 0

            async def apply(_policy) -> None:
                nonlocal calls
                calls += 1
                if calls == 1:
                    raise RuntimeError("transient apply failure")
                stop_event.set()

            await asyncio.wait_for(
                watcher.watch(apply, stop_event=stop_event),
                timeout=1.0,
            )
            self.assertGreaterEqual(calls, 2)


if __name__ == "__main__":
    unittest.main()
