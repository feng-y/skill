#!/usr/bin/env python3
"""Validate paired-EVA fixture generators, public commands, hashes, and cleanliness."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIXTURES = {
    "F1-false-green.md": {
        "returncodes": [0, 0, 0],
        "contains": {0: "all checks passed"},
    },
    "F2-parser-migration.md": {
        "returncodes": [0, 0, 0],
        "nonempty": {1},
    },
    "F3-branch-blocker.md": {
        "returncodes": [1, 1, 0],
        "contains": {0: "test_percentage"},
    },
    "F4-cross-context.md": {
        "returncodes": [0, 0, 0],
        "nonempty": {1},
    },
}


def fenced_after(text: str, heading: str, language: str) -> str:
    try:
        section = text[text.index(heading) + len(heading) :]
    except ValueError as exc:
        raise AssertionError(f"missing heading: {heading}") from exc
    match = re.search(rf"```{re.escape(language)}\n(.*?)```", section, re.S)
    if not match:
        raise AssertionError(f"missing {language} block after {heading}")
    return match.group(1)


def stated_manifest_sha(text: str) -> str:
    match = re.search(r"Manifest SHA-256: `([0-9a-f]{64})`", text)
    if not match:
        raise AssertionError("missing manifest SHA-256")
    return match.group(1)


def run_command(command: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.setdefault("PYTHONDONTWRITEBYTECODE", "1")
    return subprocess.run(
        ["bash", "-lc", command],
        cwd=cwd,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


def validate_fixture(filename: str, spec: dict[str, object], temp_root: Path) -> dict[str, object]:
    path = ROOT / "fixtures" / filename
    text = path.read_text(encoding="utf-8")

    manifest = fenced_after(text, "## Oracle manifest", "text")
    actual_manifest_sha = hashlib.sha256(manifest.encode("utf-8")).hexdigest()
    expected_manifest_sha = stated_manifest_sha(text)
    if actual_manifest_sha != expected_manifest_sha:
        raise AssertionError(
            f"{filename}: manifest hash mismatch: {actual_manifest_sha} != {expected_manifest_sha}"
        )

    repo = temp_root / filename.removesuffix(".md")
    generator = fenced_after(text, "## Repository generator", "bash")
    generated = subprocess.run(
        ["bash", "-c", generator, "fixture-generator", str(repo)],
        text=True,
        capture_output=True,
        check=False,
    )
    if generated.returncode != 0:
        raise AssertionError(
            f"{filename}: generator failed\nstdout:\n{generated.stdout}\nstderr:\n{generated.stderr}"
        )

    if not (repo / ".git").is_dir():
        raise AssertionError(f"{filename}: generator did not create a Git repository")

    commands = [
        line.strip()
        for line in fenced_after(text, "## Public commands", "bash").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    expected_returncodes = list(spec["returncodes"])
    if len(commands) != len(expected_returncodes):
        raise AssertionError(
            f"{filename}: expected {len(expected_returncodes)} public commands, found {len(commands)}"
        )

    command_results: list[dict[str, object]] = []
    for index, (command, expected_rc) in enumerate(zip(commands, expected_returncodes, strict=True)):
        result = run_command(command, repo)
        combined = result.stdout + result.stderr
        if result.returncode != expected_rc:
            raise AssertionError(
                f"{filename}: command {index + 1} returned {result.returncode}, expected {expected_rc}\n"
                f"command: {command}\nstdout:\n{result.stdout}\nstderr:\n{result.stderr}"
            )
        expected_text = dict(spec.get("contains", {})).get(index)
        if expected_text and expected_text not in combined:
            raise AssertionError(
                f"{filename}: command {index + 1} output missing {expected_text!r}"
            )
        if index in set(spec.get("nonempty", set())) and not combined.strip():
            raise AssertionError(f"{filename}: command {index + 1} unexpectedly produced no output")
        if command == "git status --short" and result.stdout.strip():
            raise AssertionError(
                f"{filename}: public checks left a dirty worktree:\n{result.stdout}"
            )
        command_results.append(
            {
                "command": command,
                "returncode": result.returncode,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
            }
        )

    head = run_command("git rev-parse HEAD", repo)
    if head.returncode != 0:
        raise AssertionError(f"{filename}: cannot resolve initial commit")

    return {
        "fixture": filename,
        "manifest_sha256": actual_manifest_sha,
        "generated_repo_head": head.stdout.strip(),
        "commands": command_results,
        "result": "PASS",
    }


def main() -> int:
    missing = [name for name in ("bash", "git", "python", "pytest", "rg") if shutil.which(name) is None]
    if missing:
        print(json.dumps({"result": "BLOCK", "missing_tools": missing}, indent=2))
        return 2

    with tempfile.TemporaryDirectory(prefix="prompt-atlas-paired-fixtures-") as temp_dir:
        temp_root = Path(temp_dir)
        results = [
            validate_fixture(filename, spec, temp_root)
            for filename, spec in FIXTURES.items()
        ]

    print(json.dumps({"result": "PASS", "fixtures": results}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
