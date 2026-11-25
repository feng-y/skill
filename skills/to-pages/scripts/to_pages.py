#!/usr/bin/env python3
"""Publish static reports through GitHub to a Git-connected Cloudflare site."""

import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path, PurePosixPath
import re
import stat
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen


class PagesError(Exception):
    pass


def relative_path(value, allow_root=False):
    if not isinstance(value, str) or not value:
        raise PagesError("Expected a nonempty relative path")
    if value == "." and allow_root:
        return value
    parts = value.split("/")
    if any(not p or p.startswith(".") or p in ("node_modules", "__pycache__")
           or "\\" in p or any(ord(c) < 32 for c in p) for p in parts):
        raise PagesError("Paths must be relative, without hidden or parent components")
    return str(PurePosixPath(value))


def private_file(path):
    info = path.stat()
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or info.st_mode & 0o077:
        raise PagesError("Credential files must be owned by this user and chmod 600")


def load_config(path):
    try:
        config = json.loads(path.read_text())
        github = config["github"]
        cloudflare = config["cloudflare"]
        repo = github["repo"]
        if not re.fullmatch(r"[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", repo):
            raise PagesError("github.repo must be owner/name")
        branch = github.get("branch", "main")
        if not isinstance(branch, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._/-]*", branch):
            raise PagesError("Invalid github.branch")
        result = subprocess.run(["git", "check-ref-format", "--branch", branch], capture_output=True)
        if result.returncode:
            raise PagesError("Invalid github.branch")
        sources = [key for key in ("token", "token_file", "token_env") if key in github]
        if len(sources) > 1:
            raise PagesError("Choose one of github.token, token_file, or token_env")
        if "token" in github:
            private_file(path)
            token = github["token"]
        elif "token_file" in github:
            token_path = Path(github["token_file"]).expanduser()
            if not token_path.is_absolute():
                token_path = path.parent / token_path
            private_file(token_path)
            token = token_path.read_text().strip()
        else:
            env_name = github.get("token_env", "GITHUB_TOKEN")
            token = os.environ.get(env_name, "")
        if not isinstance(token, str) or not token.strip() or any(c.isspace() for c in token):
            raise PagesError("GitHub token missing or malformed; load its configured environment or file")
        base_url = cloudflare.get("base_url", "").rstrip("/")
        url = urlsplit(base_url)
        if base_url and (url.scheme != "https" or not url.hostname or url.username
                         or url.password or url.query or url.fragment or url.port not in (None, 443)):
            raise PagesError("cloudflare.base_url must be an HTTPS site URL without credentials or query")
        return {"repo": repo, "branch": branch, "token": token,
                "base_url": base_url,
                "output_dir": relative_path(cloudflare.get("output_dir", "public"), allow_root=True)}
    except (KeyError, TypeError, ValueError, AttributeError, OSError) as exc:
        raise PagesError("Cannot read configuration; check JSON fields and credential file access") from exc


def source_files(source):
    if source.is_symlink():
        raise PagesError("Source symlinks are not supported")
    if source.is_file():
        if source.suffix.lower() not in (".html", ".htm"):
            raise PagesError("Single-file source must be HTML")
        files = {"index.html": source.read_bytes()}
    elif source.is_dir():
        files = {}
        for item in sorted(source.rglob("*")):
            if item.is_symlink():
                raise PagesError("Source directory contains a symlink")
            if item.is_file():
                name = relative_path(item.relative_to(source).as_posix())
                if item.suffix.lower() in (".pem", ".key", ".p12", ".pfx"):
                    raise PagesError("Source directory contains a credential-like file")
                files[name] = item.read_bytes()
        if "index.html" not in files:
            raise PagesError("Static directory must contain index.html")
    else:
        raise PagesError("Source does not exist")
    if any(len(data) > 25 * 1024 * 1024 for data in files.values()):
        raise PagesError("Cloudflare Pages assets must not exceed 25 MiB per file")
    return files


def github_read(config, endpoint):
    request = Request("https://api.github.com/" + endpoint, headers={
        "Authorization": "Bearer " + config["token"],
        "Accept": "application/vnd.github+json", "User-Agent": "to-pages"})
    try:
        with urlopen(request, timeout=30) as response:
            return json.load(response)
    except HTTPError as exc:
        raise PagesError("GitHub read returned HTTP %s; check target repository and token access" % exc.code) from exc
    except (URLError, TimeoutError) as exc:
        raise PagesError("GitHub read failed; check network connectivity") from exc


def git(config, directory, env, *args):
    result = subprocess.run(["git", "--literal-pathspecs", "-c", "http.version=HTTP/1.1",
                             "-c", "credential.helper=", "-c", "core.hooksPath=/dev/null",
                             "-C", str(directory), *args], env=env, capture_output=True, text=True)
    if result.returncode:
        detail = result.stderr.replace(config["token"], "[REDACTED]").strip()
        raise PagesError("git %s failed: %s" % (args[0], detail))
    return result.stdout.strip()


@contextmanager
def checkout(config):
    with tempfile.TemporaryDirectory(prefix="to-pages-") as temporary:
        root = Path(temporary)
        askpass = root / "askpass"
        askpass.write_text("#!/usr/bin/env python3\nimport os,sys\n"
                           "print('x-access-token' if 'username' in sys.argv[1].lower() "
                           "else os.environ['TO_PAGES_GIT_TOKEN'])\n")
        askpass.chmod(0o700)
        env = dict(os.environ, GIT_ASKPASS=str(askpass), GIT_TERMINAL_PROMPT="0",
                   TO_PAGES_GIT_TOKEN=config["token"])
        for key in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_CONFIG_COUNT",
                    "GIT_CONFIG_PARAMETERS", "GIT_TRACE", "GIT_TRACE_CURL", "GIT_CURL_VERBOSE"):
            env.pop(key, None)
        repo = root / "repo"
        repo.mkdir()
        git(config, repo, env, "init", "--quiet")
        git(config, repo, env, "remote", "add", "origin", "https://github.com/" + config["repo"] + ".git")
        refs = git(config, repo, env, "ls-remote", "origin")
        expected = "refs/heads/" + config["branch"]
        found = any(line.split("\t")[-1] == expected for line in refs.splitlines())
        if found:
            git(config, repo, env, "fetch", "--depth=1", "origin", expected)
            git(config, repo, env, "checkout", "-b", config["branch"], "FETCH_HEAD")
        elif refs:
            raise PagesError("Configured branch is absent in a nonempty repository; check github.branch")
        else:
            git(config, repo, env, "checkout", "--orphan", config["branch"])
        yield repo, env


def target_directory(repo, config, destination):
    target = repo / config["output_dir"] / destination
    current = repo
    for part in target.relative_to(repo).parts:
        current = current / part
        if current.is_symlink() or (current.exists() and not current.is_dir()):
            raise PagesError("Destination contains a symlink or a file where a directory is required")
    return target


def stage(config, repo, env, destination, files, replace):
    target = target_directory(repo, config, destination)
    conflicts = []
    changes = []
    for name, data in files.items():
        out = target / name
        current = out
        while current != repo:
            if current.is_symlink():
                raise PagesError("Destination contains a symlink")
            current = current.parent
        if out.exists():
            if not out.is_file():
                raise PagesError("Destination file collides with a directory")
            if out.read_bytes() == data:
                continue
            conflicts.append(name)
        changes.append(name)
    if changes and target.exists() and any(target.iterdir()) and not replace:
        raise PagesError("Report path already exists; choose another --path or authorize its update with --replace")
    if conflicts and not replace:
        raise PagesError("Refusing to overwrite existing files without --replace")
    for name in changes:
        out = target / name
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(files[name])
        git(config, repo, env, "add", "--", str(out.relative_to(repo)))
    return [str((target / name).relative_to(repo)) for name in changes]


def public_url(config, destination, name=""):
    if not config["base_url"]:
        return None
    path = destination + "/" + name
    return config["base_url"] + "/" + quote(path, safe="/")


def verify(config, destination, files, timeout):
    deadline = time.monotonic() + timeout
    failures = []
    while True:
        failures = []
        for name, data in files.items():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                failures.append("verification deadline reached")
                break
            url = public_url(config, destination, name)
            try:
                request = Request(url, headers={"Cache-Control": "no-cache", "User-Agent": "to-pages-verify"})
                with urlopen(request, timeout=min(20, remaining)) as response:
                    actual = response.read(len(data) + 1)
                if actual != data:
                    failures.append(name + " content differs")
            except (URLError, TimeoutError, OSError) as exc:
                failures.append(name + " unavailable" + (" HTTP " + str(exc.code) if isinstance(exc, HTTPError) else ""))
        if not failures:
            return {"status": "verified", "url": public_url(config, destination), "files_verified": len(files)}
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            raise PagesError("Public content not verified: " + "; ".join(failures[:5]))
        time.sleep(min(5, remaining))


def emit(value):
    print(json.dumps(value, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path(os.environ.get(
        "TO_PAGES_CONFIG", "~/.config/to-pages/config.json")).expanduser())
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("doctor", help="Read authentication and repository metadata without writing")
    for command in ("plan", "push", "publish", "verify"):
        sub = commands.add_parser(command)
        sub.add_argument("source", type=Path)
        sub.add_argument("--path", required=True, help="Report directory relative to the site root")
        if command in ("plan", "push", "publish"):
            sub.add_argument("--replace", action="store_true")
        if command in ("publish", "verify"):
            sub.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    config = load_config(args.config.expanduser())
    if args.command == "doctor":
        user = github_read(config, "user")
        repo = github_read(config, "repos/" + config["repo"])
        emit({"status": "repository_read_ok", "login": user["login"], "repo": repo["full_name"],
              "private": repo["private"], "repository_role_push": repo.get("permissions", {}).get("push"),
              "token_write_verified": False, "branch": config["branch"],
              "base_url": config["base_url"] or None, "output_dir": config["output_dir"]})
        return
    destination = relative_path(args.path)
    if args.command in ("publish", "verify"):
        if not config["base_url"]:
            raise PagesError("Set cloudflare.base_url to the actual production URL before publishing or verifying")
        if args.timeout < 1 or args.timeout > 3600:
            raise PagesError("--timeout must be between 1 and 3600 seconds")
    files = source_files(args.source.expanduser())
    if args.command == "verify":
        emit(verify(config, destination, files, args.timeout))
        return
    with checkout(config) as (repo, env):
        changes = stage(config, repo, env, destination, files, args.replace)
        if args.command == "plan":
            emit({"status": "planned", "repo": config["repo"], "branch": config["branch"],
                  "changed_files": changes, "url": public_url(config, destination)})
            return
        if changes:
            git(config, repo, env, "-c", "user.name=to-pages", "-c", "user.email=to-pages@users.noreply.github.com",
                "commit", "-m", "Publish " + destination)
            sha = git(config, repo, env, "rev-parse", "HEAD")
            git(config, repo, env, "push", "origin", "HEAD:refs/heads/" + config["branch"])
        else:
            sha = git(config, repo, env, "rev-parse", "HEAD")
        emit({"status": "pushed" if changes else "unchanged", "commit": sha,
              "commit_url": "https://github.com/" + config["repo"] + "/commit/" + sha,
              "url": public_url(config, destination)})
    if args.command == "publish":
        emit(verify(config, destination, files, args.timeout))


if __name__ == "__main__":
    try:
        main()
    except (PagesError, OSError) as exc:
        emit({"status": "error", "message": str(exc) if isinstance(exc, PagesError) else "Local file or process access failed"})
        sys.exit(1)
