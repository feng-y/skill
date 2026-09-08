from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from rdr.config import AccessConfig, ConfigError, merge_access_configs


class ConfigTest(unittest.TestCase):
    def _write(self, value: object) -> Path:
        root = tempfile.TemporaryDirectory()
        self.addCleanup(root.cleanup)
        path = Path(root.name) / "config.json"
        path.write_text(json.dumps(value), encoding="utf-8")
        return path

    def test_access_config(self) -> None:
        config = AccessConfig.load(
            self._write({"enabled": True, "tokens": ["a", "b", "a"]})
        )
        self.assertTrue(config.enabled)
        self.assertEqual(config.tokens, ("a", "b"))

    def test_merge_local_and_global(self) -> None:
        local = AccessConfig(enabled=True, tokens=("local", "shared"))
        global_config = AccessConfig(enabled=True, tokens=("global", "shared"))
        merged = merge_access_configs(local, global_config)
        self.assertTrue(merged.enabled)
        self.assertEqual(merged.tokens, ("local", "shared", "global"))

    def test_any_disabled_config_disables_runtime(self) -> None:
        local = AccessConfig(enabled=True, tokens=("local",))
        global_config = AccessConfig(enabled=False, tokens=())
        merged = merge_access_configs(local, global_config)
        self.assertFalse(merged.enabled)
        self.assertEqual(merged.tokens, ("local",))

    def test_extra_tokens_are_unioned_without_duplicates(self) -> None:
        local = AccessConfig(enabled=True, tokens=("local", "shared"))
        merged = merge_access_configs(
            local, extra_tokens=("env", "local")
        )
        self.assertTrue(merged.enabled)
        self.assertEqual(merged.tokens, ("local", "shared", "env"))

    def test_merge_without_file_configs_uses_extra_tokens_only(self) -> None:
        merged = merge_access_configs(None, extra_tokens=("env",))
        self.assertTrue(merged.enabled)
        self.assertEqual(merged.tokens, ("env",))

    def test_merge_without_any_token_source_is_empty(self) -> None:
        merged = merge_access_configs(None)
        self.assertTrue(merged.enabled)
        self.assertEqual(merged.tokens, ())

    def test_rejects_missing_required_values(self) -> None:
        with self.assertRaises(ConfigError):
            AccessConfig.load(self._write({"enabled": True}))
        with self.assertRaises(ConfigError):
            AccessConfig.load(self._write({"tokens": ["a"]}))

    def test_rejects_invalid_token(self) -> None:
        with self.assertRaises(ConfigError):
            AccessConfig.load(self._write({"enabled": True, "tokens": [""]}))


if __name__ == "__main__":
    unittest.main()
