#!/usr/bin/env python3
"""Exercise publication with a real local Git remote and anonymous HTTP server."""

from contextlib import redirect_stdout
from datetime import datetime, timezone
from html.parser import HTMLParser
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
from catalog import CATALOG_PATH, content_digest, load_catalog, parse_timestamp
from navigation import prepare_html, render_homepage


def run_git(*args):
    return subprocess.run(["git", *map(str, args)], check=True, capture_output=True, text=True).stdout.strip()


class HTMLTags(HTMLParser):
    def __init__(self, data):
        super().__init__()
        self.tags = []
        self.feed(data.decode("utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


def archive_data(homepage):
    start = b'<script id="archive-data" type="application/json">'
    return json.loads(homepage.split(start, 1)[1].split(b"</script>", 1)[0])


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
        args = ["to_pages.py", "--config", str(self.config), name]
        if name in ("plan", "push", "publish", "verify"):
            args.extend((str(source or self.source), "--path", destination))
        args.extend(extra)
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

    def require_case_insensitive_checkout(self):
        if not self.source.with_name(self.source.name.upper()).exists():
            self.skipTest("Temporary checkout filesystem is case-sensitive")

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
            "public/reports/example/details.htm", "public/reports/example/image.png", str(CATALOG_PATH),
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

    def test_equal_titles_and_version_suffixes_remain_separate_topics(self):
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
        self.assertIn("2 个主题", homepage)
        self.assertEqual(homepage.count("<h2>Rook &lt;iframe&gt; &amp; 工作台</h2>"), 2)
        self.assertIn('href="./reports/rook-v1/"', homepage)
        self.assertIn('href="./reports/rook-v2%20%26%20notes/"', homepage)
        self.assertIn("reports/rook-v2 &amp; notes/", homepage)
        self.assertIn("适用 版本一", homepage)
        self.assertNotIn("多余正文标题", homepage)
        self.assertIn("说明 &lt;script&gt; &amp; &quot;版本二&quot;", homepage)
        self.assertEqual(first_report, self.published("public/reports/rook-v1/index.html"))

    def test_explicit_topic_preserves_versions_and_replaces_only_the_selected_path(self):
        first_path = "reports/rook-v1"
        second_path = "reports/rook-v2"
        started = datetime.now(timezone.utc)
        self.command("push", "--topic", "rook", "--title", "Rook", "--category", "技术方案",
                     "--project", "发布", "--summary", "首版", destination=first_path)
        self.source.write_text("<title>Version two</title>")
        self.command("push", "--topic", "rook", "--summary", "新增搜索", destination=second_path)
        old_report = self.published(f"public/{second_path}/index.html")
        baseline = self.command("catalog")[0]
        first, second = baseline["topics"][0]["versions"]
        self.assertEqual(baseline["topics"][0]["id"], "rook")
        self.assertEqual(baseline["topics"][0]["category"], "技术方案")
        self.assertEqual(baseline["topics"][0]["project"], "发布")
        self.assertEqual([(v["label"], v["path"]) for v in (first, second)],
                         [("v1", first_path), ("v2", second_path)])
        self.assertEqual(first["summary"], "首版")
        self.assertEqual(second["summary"], "新增搜索")
        self.assertEqual(second["digest"], content_digest({"index.html": old_report}))
        published = parse_timestamp(first["published_at"])
        self.assertLessEqual(started, published)
        self.assertLessEqual(published, datetime.now(timezone.utc))
        self.assertEqual(first["published_at"], first["updated_at"])
        archive = archive_data(self.published("public/index.html"))
        self.assertEqual([v["label"] for v in archive[0]["versions"]], ["v2", "v1"])

        self.source.write_text("<title>Amended first version</title>")
        replaced = self.command("push", "--replace", "--summary", "修订首版", destination=first_path)[0]
        recorded = self.command("catalog")[0]
        edited, kept = recorded["topics"][0]["versions"]
        self.assertEqual(kept, second)
        self.assertEqual(edited["published_at"], first["published_at"])
        self.assertGreater(parse_timestamp(edited["updated_at"]), published)
        self.assertNotEqual(edited["digest"], first["digest"])
        self.assertEqual(edited["summary"], "修订首版")
        self.assertEqual(self.published(f"public/{second_path}/index.html"), old_report)

        repeated = self.command("push", destination=first_path)[0]
        self.assertEqual(repeated["status"], "unchanged")
        self.assertEqual(repeated["commit"], replaced["commit"])
        self.assertEqual(self.command("catalog")[0], recorded)
        archive = archive_data(self.published("public/index.html"))
        self.assertEqual([v["label"] for v in archive[0]["versions"]], ["v2", "v1"])
        self.assertEqual(archive[0]["updated"], edited["updated_at"])
        self.assertEqual([v["date"] for v in archive[0]["versions"]],
                         [second["published_at"], first["published_at"]])

    def test_metadata_only_edit_keeps_report_time_and_content_digest(self):
        self.command("push")
        original = self.command("catalog")[0]["topics"][0]["versions"][0]
        old_body = self.published("public/reports/example/index.html")
        self.command("push", "--title", "New title", "--category", "使用文档", "--summary", "New summary")
        topic = self.command("catalog")[0]["topics"][0]
        self.assertEqual(topic["title"], "New title")
        self.assertEqual(topic["category"], "使用文档")
        self.assertEqual(topic["versions"], [{**original, "summary": "New summary"}])
        self.assertEqual(self.published("public/reports/example/index.html"), old_body)

    def test_conflicting_topic_or_label_does_not_mutate_remote(self):
        initial = self.command("push", "--topic", "rook", "--version", "draft")[0]["commit"]
        for options, destination in (
            (("--topic", "other"), "reports/example"),
            (("--version", "stable"), "reports/example"),
            (("--topic", "rook", "--version", "draft"), "reports/other"),
        ):
            with self.subTest(options=options), self.assertRaisesRegex(pages.PagesError, "already belongs"):
                self.command("push", *options, destination=destination)
        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), initial)

    def test_report_path_alias_preserves_published_tree_and_catalog(self):
        self.require_case_insensitive_checkout()
        original_path = "reports/Case"
        result = self.command("publish", "--topic", "original", "--timeout", "3", destination=original_path)
        self.assertEqual(result[-1]["status"], "verified")
        tree = run_git("--git-dir", self.remote, "ls-tree", "-r", "main")
        catalog = self.published(CATALOG_PATH)
        report_path = f"public/{original_path}/index.html"
        report = self.published(report_path)
        edited = self.root / "edited.html"
        edited.write_text("<title>Edited report</title>")

        for destination, source, replace in (
            ("reports/case", self.source, False),
            ("reports/case", self.source, True),
            ("reports/case", edited, False),
            ("reports/case", edited, True),
            ("Reports/Case", edited, True),
        ):
            options = ("--replace",) if replace else ()
            with self.subTest(destination=destination, source=source.name, replace=replace):
                with self.assertRaisesRegex(pages.PagesError, "Path spelling conflicts"):
                    self.command("publish", "--topic", "other", "--timeout", "1", *options,
                                 destination=destination, source=source)

        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), result[0]["commit"])
        self.assertEqual(run_git("--git-dir", self.remote, "ls-tree", "-r", "main"), tree)
        self.assertEqual(self.published(CATALOG_PATH), catalog)
        self.assertEqual(self.published(report_path), report)

    def test_asset_filename_alias_does_not_replace_published_file(self):
        self.require_case_insensitive_checkout()
        static = self.root / "static"
        static.mkdir()
        (static / "index.html").write_bytes(self.source.read_bytes())
        asset = static / "Image.png"
        asset.write_bytes(b"original image")
        initial = self.command("push", source=static)[0]["commit"]
        asset.rename(static / "image.png").write_bytes(b"edited image")

        with self.assertRaisesRegex(pages.PagesError, "Path spelling conflicts"):
            self.command("push", "--replace", source=static)
        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), initial)
        self.assertEqual(self.published("public/reports/example/Image.png"), b"original image")

    def test_source_asset_aliases_are_rejected_before_git_staging(self):
        self.require_case_insensitive_checkout()
        config = pages.load_config(self.config)
        with pages.checkout(config) as (repo, env):
            files = {"index.html": b"report", "Asset.png": b"first", "asset.png": b"second"}
            with self.assertRaisesRegex(pages.PagesError, "Path spelling conflicts"):
                pages.stage(config, repo, env, "reports/example", files, False)
            self.assertEqual(run_git("-C", repo, "ls-files"), "")

    def test_catalog_and_homepage_reject_aliased_entry_names(self):
        self.require_case_insensitive_checkout()
        self.command("push")
        repo = self.root / "site"
        run_git("clone", "--branch", "main", self.remote, repo)
        site = repo / "public"

        for path in (CATALOG_PATH.parent, CATALOG_PATH, Path("public/reports/example/index.html"),
                     Path("public/index.html")):
            with self.subTest(path=path):
                entry = repo / path
                alias = entry.rename(entry.with_name(entry.name.upper()))
                try:
                    with self.assertRaisesRegex(pages.PagesError, "Path spelling conflicts"):
                        if path == Path("public/index.html"):
                            render_homepage(site)
                        else:
                            load_catalog(repo, "public")
                finally:
                    alias.rename(entry)

    def test_replace_cannot_write_another_version_inside_the_report_directory(self):
        self.command("push", "--topic", "rook", destination="reports/rook")
        second_path = "reports/rook/detail"
        second = self.command("push", "--topic", "rook", destination=second_path)[0]["commit"]
        static = self.root / "replacement"
        (static / "detail").mkdir(parents=True)
        (static / "index.html").write_text("<title>Edited first version</title>")
        (static / "detail" / "index.html").write_text("<title>Do not replace the second version</title>")
        with self.assertRaisesRegex(pages.PagesError, "overlap another catalog version"):
            self.command("push", "--replace", source=static, destination="reports/rook")
        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), second)

    def test_index_bootstrap_preserves_separate_legacy_reports_with_unknown_dates(self):
        checkout = self.root / "legacy-site"
        run_git("clone", self.remote, checkout)
        run_git("-C", checkout, "checkout", "--orphan", "main")
        legacy_body = b"<title>Same legacy title</title>"
        for path in ("reports/legacy", "reports/legacy-v2"):
            entry = checkout / "public" / path / "index.html"
            entry.parent.mkdir(parents=True)
            entry.write_bytes(legacy_body)
        self.commit_checkout(checkout)

        before = run_git("--git-dir", self.remote, "rev-parse", "main")
        self.assertEqual(self.command("catalog"), [{"schema": 1, "output_dir": "public", "topics": []}])
        plan = self.command("index", "plan")[0]
        self.assertCountEqual(plan["changed_files"], ["public/index.html", str(CATALOG_PATH)])
        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), before)
        result = self.command("index", "publish", "--timeout", "3")
        self.assertEqual(result[-1]["files_verified"], 1)
        self.assertEqual(self.requested_paths, ["/collection/"])
        self.assertEqual(self.published("public/reports/legacy/index.html"), legacy_body)
        self.assertEqual(json.loads(self.published(CATALOG_PATH))["topics"], [])
        legacy = archive_data(self.published("public/index.html"))
        self.assertEqual(len(legacy), 2)
        self.assertEqual({topic["category"] for topic in legacy}, {"未分类"})
        self.assertEqual({topic["updated"] for topic in legacy}, {None})
        self.assertEqual({topic["versions"][0]["href"] for topic in legacy},
                         {"./reports/legacy/", "./reports/legacy-v2/"})

        self.command("push", "--topic", "reports/legacy", destination="reports/new")
        archive = archive_data(self.published("public/index.html"))
        self.assertEqual(len({topic["id"] for topic in archive}), 3)
        self.assertEqual(self.published("public/reports/legacy-v2/index.html"), legacy_body)

    def test_root_output_directory_still_generates_homepage_and_catalog(self):
        config = json.loads(self.config.read_text())
        config["cloudflare"]["output_dir"] = "."
        self.config.write_text(json.dumps(config))
        self.command("push")
        record = self.command("catalog")[0]
        self.assertEqual(record["output_dir"], ".")
        self.assertEqual(json.loads(self.published(CATALOG_PATH)), record)
        self.assertIn(b'href="./reports/example/"', self.published("index.html"))
        self.assertIn(b"<title>Version one</title>", self.published("reports/example/index.html"))

    def test_catalog_corruption_stops_the_publish_before_remote_changes(self):
        self.command("push")
        checkout = self.root / "corrupt-catalog"
        run_git("clone", "--branch", "main", self.remote, checkout)
        catalog_file = checkout / CATALOG_PATH
        catalog = json.loads(catalog_file.read_bytes())
        catalog["topics"][0]["versions"][0]["updated_at"] = "2026-02-30T12:00:00Z"
        catalog_file.write_text(json.dumps(catalog))
        self.commit_checkout(checkout)

        before = run_git("--git-dir", self.remote, "rev-parse", "main")
        with self.assertRaisesRegex(pages.PagesError, "ISO UTC timestamps"):
            self.command("push", destination="reports/new")
        self.assertEqual(run_git("--git-dir", self.remote, "rev-parse", "main"), before)

    def test_generated_archive_escapes_metadata_and_encodes_relative_links(self):
        title = '</script><img src=x onerror="example()">'
        self.command("push", "--title", title, "--category", "<category>",
                     "--summary", title, destination="reports/javascript:report#notes?")
        homepage = self.published("public/index.html")
        self.assertNotIn(title.encode(), homepage)
        self.assertIn(b'&lt;/script&gt;&lt;img src=x onerror=&quot;example()&quot;&gt;', homepage)
        self.assertIn(b'href="./reports/javascript%3Areport%23notes%3F/"', homepage)
        self.assertFalse(any(tag == "img" for tag, attrs in HTMLTags(homepage).tags))
        data = archive_data(homepage)[0]
        self.assertEqual(data["title"], title)
        self.assertEqual(data["category"], "<category>")
        self.assertEqual(data["versions"][0]["summary"], title)

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

    def test_push_requires_a_site_url_when_the_report_has_a_base_href(self):
        config = json.loads(self.config.read_text())
        config["cloudflare"]["base_url"] = ""
        self.config.write_text(json.dumps(config))
        self.source.write_text('<base href="https://cdn.example/assets/">')

        with self.assertRaisesRegex(pages.PagesError, r"index\.html.*cloudflare\.base_url"):
            self.command("push")
        self.assertFalse((self.remote / "refs/heads/main").exists())

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
    def test_report_with_base_and_csp_has_an_absolute_static_fallback(self):
        source = (
            b'<!doctype html><head><meta http-equiv="Content-Security-Policy" content="script-src \'none\'">'
            b'<base href="https://cdn.example/assets/" target="_blank"></head>'
            b'<body><img src="report.png"></body>'
        )
        base_url = "https://reports.example/sub%20folder&copy;/"
        prepared = prepare_html(source, base_url)
        repeated = prepare_html(prepared, base_url)
        tags = HTMLTags(repeated).tags
        links = [attrs for tag, attrs in tags if tag == "a"]
        policies = [attrs.get("content") for tag, attrs in tags
                    if tag == "meta" and attrs.get("http-equiv") == "Content-Security-Policy"]

        self.assertEqual(repeated, prepared)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0]["href"], "https://reports.example/sub%20folder&copy;/")
        self.assertEqual(links[0]["data-site-path"], "/sub%20folder&copy;/")
        self.assertEqual(links[0]["target"], "_self")
        self.assertEqual([attrs for tag, attrs in tags if tag == "base"], [
            {"href": "https://cdn.example/assets/", "target": "_blank"},
        ])
        self.assertEqual(policies, ["script-src 'none'"])
        self.assertIn(("img", {"src": "report.png"}), tags)

    def test_site_path_preserves_reserved_url_characters(self):
        prepared = prepare_html(b"<title>Report</title>", "https://reports.example/collection;v1/a@b+c/")
        links = [attrs for tag, attrs in HTMLTags(prepared).tags if tag == "a"]
        self.assertEqual(links[0]["href"], "/collection;v1/a@b+c/")
        self.assertEqual(links[0]["data-site-path"], "/collection;v1/a@b+c/")

    def test_static_fallback_stays_on_the_preview_without_an_active_base_href(self):
        for source in (b"<title>Report</title>", b'<base target="_blank">',
                       b'<template><base href="https://cdn.example/assets/"></template>'):
            with self.subTest(source=source):
                prepared = prepare_html(source, "https://reports.example/collection")
                links = [attrs for tag, attrs in HTMLTags(prepared).tags if tag == "a"]
                self.assertEqual(len(links), 1)
                self.assertEqual(links[0]["href"], "/collection/")
                self.assertEqual(links[0]["data-site-path"], "/collection/")
                self.assertEqual(links[0]["target"], "_self")

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

    def test_catalog_rejects_symlink_to_metadata_file(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            file = root / CATALOG_PATH
            file.parent.mkdir()
            file.symlink_to(root / "external.json")
            with self.assertRaisesRegex(pages.PagesError, "without symlinks"):
                load_catalog(root, "public")

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
