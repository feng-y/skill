#!/usr/bin/env python3
"""Exercise publication with a real local Git remote and anonymous HTTP server."""

from contextlib import redirect_stdout
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
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

import to_pages as pages
from navigation import prepare_html, render_homepage


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
                                         "cloudflare": {"base_url": "https://reports.example/collection", "output_dir": "public"}}))
        self.source = self.root / "report.html"
        self.source.write_text("<!doctype html><title>Version one</title>")
        self.stale_paths = set()
        self.requested_paths = []
        test = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                requested_path = unquote(urlsplit(self.path).path)
                test.requested_paths.append(requested_path)
                path = requested_path.removeprefix("/collection/")
                if not path or path.endswith("/"):
                    path += "index.html"
                result = subprocess.run(["git", "--git-dir", str(test.remote), "show", "main:public/" + path], capture_output=True)
                self.send_response(200 if result.returncode == 0 else 404)
                self.end_headers()
                self.wfile.write(b"stale" if requested_path in test.stale_paths else result.stdout)

            def log_message(self, *args):
                pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.server.server_close)
        self.addCleanup(self.server.shutdown)
        original_git = pages.git
        original_public_url = pages.public_url

        def local_git(config, directory, env, *args):
            if args[:3] == ("remote", "add", "origin"):
                args = (*args[:3], str(test.remote))
            return original_git(config, directory, env, *args)

        def local_url(config, path):
            url = original_public_url(config, path)
            return f"http://127.0.0.1:{test.server.server_port}" + urlsplit(url).path if url else None

        for context in (patch.object(pages, "git", local_git), patch.object(pages, "public_url", local_url),
                        patch.dict(os.environ, {"GITHUB_TOKEN": "unit-test-placeholder"})):
            context.start()
            self.addCleanup(context.stop)

    def command(self, name, *extra, source=None, destination="reports/example"):
        args = ["to_pages.py", "--config", str(self.config), name, str(source or self.source),
                "--path", destination, *extra]
        output = io.StringIO()
        with patch.object(sys, "argv", args), redirect_stdout(output):
            pages.main()
        return [json.loads(line) for line in output.getvalue().splitlines()]

    def published(self, path):
        return subprocess.run(["git", "--git-dir", str(self.remote), "show", f"main:{path}"],
                              check=True, capture_output=True).stdout

    def commit_checkout(self, checkout):
        run_git("-C", checkout, "add", ".")
        run_git("-C", checkout, "-c", "user.name=Test", "-c", "user.email=test@example.org",
                "commit", "-m", "Site update")
        run_git("-C", checkout, "push", "origin", "main")

    def test_plan_is_read_only_and_publish_verifies_prepared_files_and_homepage(self):
        static = self.root / "static"
        static.mkdir()
        html = b'<img src="image.png">'
        image = b"\x89PNG\x00\xff\x01"
        (static / "index.html").write_bytes(html)
        (static / "image.png").write_bytes(image)
        (static / "details.htm").write_bytes(b"<h1>Details</h1>")
        plan = self.command("plan", source=static)
        self.assertEqual(plan[0]["status"], "planned")
        self.assertCountEqual(plan[0]["changed_files"], [
            "public/index.html", "public/reports/example/index.html",
            "public/reports/example/details.htm", "public/reports/example/image.png",
        ])
        self.assertFalse((self.remote / "refs/heads/main").exists())
        result = self.command("publish", "--timeout", "3", source=static)
        self.assertEqual(result[-1]["status"], "verified")
        self.assertEqual(result[-1]["files_verified"], 4)
        self.assertIn("/collection/", self.requested_paths)
        report = self.published("public/reports/example/index.html")
        self.assertTrue(report.startswith(b'<meta charset="utf-8"><img src="image.png">'))
        self.assertIn(b'href="/collection/"', report)
        self.assertIn(b'href="/collection/"', self.published("public/reports/example/details.htm"))
        self.assertEqual(self.published("public/reports/example/image.png"), image)
        self.assertEqual((static / "index.html").read_bytes(), html)

    def test_replace_preserves_other_paths_and_identical_publish_has_no_commit(self):
        first = self.command("publish", "--timeout", "3")
        prepared_source = self.root / "prepared.html"
        prepared_source.write_bytes(self.published("public/reports/example/index.html"))
        unchanged = self.command("publish", "--timeout", "3", source=prepared_source)
        self.assertEqual(first[0]["commit"], unchanged[0]["commit"])
        self.assertEqual(unchanged[0]["status"], "unchanged")
        extra = self.root / "other"
        run_git("clone", "--branch", "main", self.remote, extra)
        (extra / "unrelated.txt").write_text("keep me")
        self.commit_checkout(extra)
        self.source.write_text("<title>Version two</title>")
        with self.assertRaisesRegex(pages.PagesError, "already exists"):
            self.command("publish", "--timeout", "3")
        self.command("publish", "--replace", "--timeout", "3")
        self.assertEqual(run_git("--git-dir", self.remote, "show", "main:unrelated.txt"), "keep me")

    def test_stale_homepage_fails_publish_but_verify_checks_the_selected_source(self):
        self.stale_paths.add("/collection/")
        with self.assertRaisesRegex(pages.PagesError, "index.html content differs"):
            self.command("publish", "--timeout", "1")
        home = self.published("public/index.html")
        self.assertIn(b'href="./reports/example/"', home)
        self.assertIn("/collection/reports/example/index.html", self.requested_paths)
        self.assertIn("/collection/", self.requested_paths)
        result = self.command("verify", "--timeout", "3")
        self.assertEqual(result[0]["status"], "verified")
        self.assertEqual(result[0]["files_verified"], 1)

    def test_stale_report_fails_publish(self):
        self.stale_paths.add("/collection/reports/example/index.html")
        with self.assertRaisesRegex(pages.PagesError, "reports/example/index.html content differs"):
            self.command("publish", "--timeout", "1")
        self.assertIn(b"<title>Version one</title>", self.published("public/reports/example/index.html"))

    def test_catalog_adds_versions_and_preserves_existing_report_bytes(self):
        self.source.write_text(
            '<title>Rook &lt;iframe&gt; &amp; 工作台</title><h1>适用 <em>版本一</em></h1><h1>多余正文标题</h1>',
            encoding="utf-8",
        )
        self.command("push", destination="reports/rook-v1")
        first_report = self.published("public/reports/rook-v1/index.html")
        self.source.write_text(
            '<title>Rook &lt;iframe&gt; &amp; 工作台</title>'
            '<meta name="description" content="说明 &lt;script&gt; &amp; &quot;版本二&quot;">',
            encoding="utf-8",
        )
        self.command("publish", "--timeout", "3", destination="reports/rook-v2 & notes")
        homepage = self.published("public/index.html").decode("utf-8")
        self.assertIn("2 份报告", homepage)
        self.assertEqual(homepage.count("<h2>Rook &lt;iframe&gt; &amp; 工作台</h2>"), 2)
        self.assertIn('href="./reports/rook-v1/"', homepage)
        self.assertIn('href="./reports/rook-v2%20%26%20notes/"', homepage)
        self.assertIn("reports/rook-v2 &amp; notes/", homepage)
        self.assertIn("适用 版本一", homepage)
        self.assertNotIn("多余正文标题", homepage)
        self.assertIn("说明 &lt;script&gt; &amp; &quot;版本二&quot;", homepage)
        self.assertEqual(first_report, self.published("public/reports/rook-v1/index.html"))

    def test_existing_custom_homepage_is_preserved_during_report_publish(self):
        checkout = self.root / "custom-site"
        run_git("clone", self.remote, checkout)
        run_git("-C", checkout, "checkout", "--orphan", "main")
        site = checkout / "public"
        site.mkdir()
        custom_home = b'<title>My custom homepage</title><!-- mentions to-pages:managed-index -->'
        (site / "index.html").write_bytes(custom_home)
        self.commit_checkout(checkout)
        result = self.command("publish", "--timeout", "3")
        self.assertEqual(result[-1]["files_verified"], 1)
        self.assertEqual(self.published("public/index.html"), custom_home)
        self.assertNotIn("/collection/", self.requested_paths)
        self.assertIn(b'href="/collection/"', self.published("public/reports/example/index.html"))

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
        result = self.command("push")
        self.assertEqual([item["status"] for item in result], ["pushed"])
        self.assertIn(b'href="/"', self.published("public/reports/example/index.html"))
        self.assertIn(b'href="./reports/example/"', self.published("public/index.html"))
        self.assertEqual(self.requested_paths, [])

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


class NavigationTests(unittest.TestCase):
    def test_preparation_preserves_markup_and_ignores_fake_tags_inside_raw_text(self):
        first = b'<!DOCTYPE html>\r\n<html lang="zh"><head>'
        body = (
            b'<title>A title &amp; text</title>'
            b'<script>const tag = "</body><head><meta charset=ascii>";'
            b'const marker = "<!-- to-pages:back-link:start -->fake<!-- to-pages:back-link:end -->";</script>'
            b'</head><body><textarea><head><meta charset=ascii></textarea>'
            b'<img src="images/as-is.svg"><script src="./scripts/report.js"></script>\r\n'
        )
        end = b"</body></html>\r\n"
        source = first + body + end
        prepared = prepare_html(source, "https://reports.example/sub%20folder")
        before, marker, rest = prepared.rpartition(b"<!-- to-pages:back-link:start -->")
        self.assertEqual(before, first + b'<meta charset="utf-8">' + body)
        self.assertTrue(marker)
        self.assertTrue(rest.endswith(b"<!-- to-pages:back-link:end -->" + end))
        self.assertIn(b'href="/sub%20folder/"', rest)
        self.assertNotIn(b"reports.example", rest)
        self.assertEqual(prepare_html(prepared, "https://preview.example/sub%20folder/"), prepared)
        moved = prepare_html(prepared, "https://preview.example/new-root")
        self.assertIn(b'href="/new-root/"', moved)
        self.assertNotIn(b'href="/sub%20folder/"', moved)
        self.assertEqual(moved.count("返回导航".encode("utf-8")), 1)

    def test_utf8_declaration_precedes_report_content_and_can_retain_existing_meta(self):
        fragment = '<title>你好</title><p>验证</p>'.encode("utf-8")
        prepared = prepare_html(fragment, "")
        self.assertTrue(prepared.startswith(b'<meta charset="utf-8">' + fragment))
        correct = b'<!doctype html><head><meta CHARSET="UTF-8"><title>test</title></head>'
        self.assertTrue(prepare_html(correct, "").startswith(correct))
        legacy = b'<!doctype html><head><meta http-equiv="Content-Type" content="text/html; charset=latin1"></head>'
        updated = prepare_html(legacy, "")
        self.assertTrue(updated.startswith(b'<!doctype html><head><meta charset="utf-8"></head>'))
        self.assertNotIn(b"latin1", updated)
        self.assertEqual(prepare_html(updated, ""), updated)

    def test_back_link_precedes_unclosed_comment_or_template(self):
        doctype = b"<!doctype html>"
        body = b"<title>Report</title><h1>Visible</h1>"
        for extra, tail in (
            (b"", b"<!-- build metadata"),
            (b"", b"<template><div>Saved content"),
            (b'<script>const metadata = "<!--";</script>', b"<!-- build metadata </body>"),
        ):
            with self.subTest(tail=tail):
                prepared = prepare_html(doctype + body + extra + tail, "")
                before, _, after = prepared.partition(b"<!-- to-pages:back-link:start -->")
                self.assertEqual(before, doctype + b'<meta charset="utf-8">' + body + extra)
                self.assertTrue(after.endswith(b"<!-- to-pages:back-link:end -->" + tail))
                self.assertEqual(prepare_html(prepared, ""), prepared)

    def test_replacing_a_back_link_also_replaces_encoding_metadata_inside_it(self):
        prefix = b"<!doctype html><head>"
        suffix = b"</head><body><h1>Report</h1></body>"
        start = b"<!-- to-pages:back-link:start -->"
        end = b"<!-- to-pages:back-link:end -->"
        for encoding in (b"latin1", b"utf-8"):
            with self.subTest(encoding=encoding):
                source = prefix + start + b'<meta charset="' + encoding + b'">Stale link' + end + suffix
                prepared = prepare_html(source, "")
                self.assertTrue(prepared.startswith(prefix + b'<meta charset="utf-8">' + start))
                self.assertTrue(prepared.endswith(end + suffix))
                self.assertEqual(prepared.count(end), 1)
                self.assertNotIn(b"Stale link", prepared)
                self.assertEqual(prepare_html(prepared, ""), prepared)

    def test_catalog_refreshes_a_homepage_with_crlf_ownership_marker(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "index.html").write_bytes(
                b"<!doctype html>\r\n<!-- to-pages:managed-index -->\r\n<title>Old catalog</title>"
            )
            report = root / "new-report"
            report.mkdir()
            (report / "index.html").write_bytes(b"<title>New report</title>")

            homepage = render_homepage(root)

            self.assertIsNotNone(homepage)
            self.assertIn(b'<a href="./new-report/"><h2>New report</h2>', homepage)
            self.assertNotIn(b"Old catalog", homepage)

    def test_catalog_ignores_hidden_and_linked_entries_and_can_adopt_a_custom_home(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "public"
            hidden = root / ".hidden"
            visible = root / "visible"
            linked_index = root / "linked-index"
            outside = Path(temporary) / "outside"
            for directory in (hidden, visible, linked_index, outside):
                directory.mkdir(parents=True, exist_ok=True)
            (hidden / "index.html").write_text("<title>Hidden</title>")
            (visible / "index.html").write_text("<h1>Visible</h1>")
            (outside / "index.html").write_text("<title>Outside</title>")
            (linked_index / "index.html").symlink_to(outside / "index.html")
            (root / "linked-dir").symlink_to(outside, target_is_directory=True)
            index = root / "index.html"
            index.write_bytes(b"<!doctype html><title>Custom home</title>")

            self.assertIsNone(render_homepage(root))
            adopted = render_homepage(root, adopt=True)
            self.assertIn(b'href="./visible/"', adopted)
            self.assertIn(b"<h2>Visible</h2>", adopted)
            self.assertNotIn(b"Hidden", adopted)
            self.assertNotIn(b"Outside", adopted)
            self.assertNotIn(b"Custom home", adopted)
            self.assertEqual(adopted.count(b"<h2>"), 1)
            self.assertEqual(index.read_bytes(), b"<!doctype html><title>Custom home</title>")
            index.write_bytes(adopted)
            self.assertEqual(render_homepage(root), adopted)


if __name__ == "__main__":
    unittest.main()
