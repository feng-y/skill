#!/usr/bin/env python3
"""Exercise publication with a real local Git remote and anonymous HTTP server."""

from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

spec = importlib.util.spec_from_file_location("to_pages", Path(__file__).with_name("to_pages.py"))
pages = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pages)


def run_git(*args):
    return subprocess.run(["git", *map(str, args)], check=True, capture_output=True, text=True).stdout.strip()


class PublishTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.remote = self.root / "remote.git"
        run_git("init", "--bare", self.remote)
        self.config = self.root / "config.json"
        self.config.write_text(json.dumps({"github": {"repo": "test/reports", "branch": "main"},
                                         "cloudflare": {"base_url": "https://reports.example", "output_dir": "public"}}))
        self.source = self.root / "report.html"
        self.source.write_text("<!doctype html><title>Version one</title>")
        self.stale = False
        test = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                path = unquote(urlsplit(self.path).path).lstrip("/")
                if path.endswith("/"):
                    path += "index.html"
                result = subprocess.run(["git", "--git-dir", str(test.remote), "show", "main:public/" + path], capture_output=True)
                self.send_response(200 if result.returncode == 0 else 404)
                self.end_headers()
                self.wfile.write(b"stale" if test.stale else result.stdout)

            def log_message(self, *args):
                pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        original_git = pages.git

        def local_git(config, directory, env, *args):
            if args[:3] == ("remote", "add", "origin"):
                args = (*args[:3], str(test.remote))
            return original_git(config, directory, env, *args)

        def local_url(config, destination, name=""):
            return "http://127.0.0.1:%s/%s/%s" % (test.server.server_port, destination, name)

        for context in (patch.object(pages, "git", local_git), patch.object(pages, "public_url", local_url),
                        patch.dict(os.environ, {"GITHUB_TOKEN": "unit-test-placeholder"})):
            context.start()
            self.addCleanup(context.stop)

    def command(self, name, *extra, source=None):
        args = ["to_pages.py", "--config", str(self.config), name, str(source or self.source),
                "--path", "reports/example", *extra]
        output = io.StringIO()
        with patch.object(sys, "argv", args), redirect_stdout(output):
            pages.main()
        return [json.loads(line) for line in output.getvalue().splitlines()]

    def test_plan_is_read_only_and_publish_verifies_binary_assets(self):
        static = self.root / "static"
        static.mkdir()
        (static / "index.html").write_bytes(b'<img src="image.png">')
        (static / "image.png").write_bytes(b"\x89PNG\x00\xff\x01")
        plan = self.command("plan", source=static)
        self.assertEqual(plan[0]["status"], "planned")
        self.assertFalse((self.remote / "refs/heads/main").exists())
        result = self.command("publish", "--timeout", "3", source=static)
        self.assertEqual(result[-1]["status"], "verified")
        self.assertEqual(result[-1]["files_verified"], 2)

    def test_replace_preserves_other_paths_and_identical_publish_has_no_commit(self):
        first = self.command("publish", "--timeout", "3")
        unchanged = self.command("publish", "--timeout", "3")
        self.assertEqual(first[0]["commit"], unchanged[0]["commit"])
        self.assertEqual(unchanged[0]["status"], "unchanged")
        extra = self.root / "other"
        run_git("clone", "--branch", "main", self.remote, extra)
        (extra / "unrelated.txt").write_text("keep me")
        run_git("-C", extra, "add", ".")
        run_git("-C", extra, "-c", "user.name=Test", "-c", "user.email=test@example.org", "commit", "-m", "Other report")
        run_git("-C", extra, "push", "origin", "main")
        self.source.write_text("<title>Version two</title>")
        with self.assertRaisesRegex(pages.PagesError, "already exists"):
            self.command("publish", "--timeout", "3")
        self.command("publish", "--replace", "--timeout", "3")
        self.assertEqual(run_git("--git-dir", self.remote, "show", "main:unrelated.txt"), "keep me")

    def test_stale_public_content_is_failure_after_successful_push(self):
        self.stale = True
        with self.assertRaisesRegex(pages.PagesError, "not verified"):
            self.command("publish", "--timeout", "1")
        self.assertEqual(run_git("--git-dir", self.remote, "show", "main:public/reports/example/index.html"), self.source.read_text())

    def test_missing_url_refuses_before_push(self):
        config = json.loads(self.config.read_text())
        config["cloudflare"]["base_url"] = ""
        self.config.write_text(json.dumps(config))
        with self.assertRaisesRegex(pages.PagesError, "actual production URL"):
            self.command("publish")
        self.assertFalse((self.remote / "refs/heads/main").exists())

    def test_explicit_push_without_cloudflare_url_only_updates_git(self):
        config = json.loads(self.config.read_text())
        config["cloudflare"]["base_url"] = ""
        self.config.write_text(json.dumps(config))
        self.stale = True
        result = self.command("push")
        self.assertEqual([item["status"] for item in result], ["pushed"])
        self.assertEqual(run_git("--git-dir", self.remote, "show", "main:public/reports/example/index.html"), self.source.read_text())

    def test_path_traversal_hidden_files_and_symlinks_are_rejected(self):
        for path in ("../outside", "/absolute", "reports/../outside", ".git/hooks", "reports//topic"):
            with self.assertRaises(pages.PagesError):
                pages.relative_path(path)
        directory = self.root / "source"
        directory.mkdir()
        (directory / "index.html").write_text("hi")
        link = directory / "link"
        link.symlink_to(self.source)
        with self.assertRaisesRegex(pages.PagesError, "symlink"):
            pages.source_files(directory)
        link.unlink()
        (directory / ".env").write_text("secret")
        with self.assertRaisesRegex(pages.PagesError, "hidden"):
            pages.source_files(directory)

    def test_plaintext_token_requires_private_config(self):
        config = json.loads(self.config.read_text())
        config["github"]["token"] = "unit-test-inline"
        self.config.write_text(json.dumps(config))
        self.config.chmod(0o644)
        with self.assertRaisesRegex(pages.PagesError, "chmod 600"):
            pages.load_config(self.config)
        self.config.chmod(0o600)
        self.assertEqual(pages.load_config(self.config)["token"], "unit-test-inline")

    def test_concurrent_push_is_rejected_without_losing_other_commit(self):
        self.command("publish", "--timeout", "3")
        other = self.root / "concurrent"
        run_git("clone", "--branch", "main", self.remote, other)
        config = pages.load_config(self.config)
        with pages.checkout(config) as (repo, env):
            (other / "concurrent.txt").write_text("new remote content")
            run_git("-C", other, "add", ".")
            run_git("-C", other, "-c", "user.name=Test", "-c", "user.email=test@example.org", "commit", "-m", "Concurrent update")
            run_git("-C", other, "push", "origin", "main")
            pages.stage(config, repo, env, "reports/another", {"index.html": b"second report"}, False)
            pages.git(config, repo, env, "-c", "user.name=Test", "-c", "user.email=test@example.org", "commit", "-m", "Report")
            with self.assertRaisesRegex(pages.PagesError, "rejected"):
                pages.git(config, repo, env, "push", "origin", "HEAD:refs/heads/main")
        self.assertEqual(run_git("--git-dir", self.remote, "show", "main:concurrent.txt"), "new remote content")


if __name__ == "__main__":
    unittest.main()
