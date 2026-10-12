#!/usr/bin/env python3
"""List Human turns from explicit session transcripts for feedback triage.

Eval-only backend. It reads Claude Code or Codex JSONL transcripts that the
caller names, and prints each Human turn with the tail of the assistant text
that preceded it, so a reviewer can trace a correction to a specific moment.
It does not classify, judge or write the ledger. Pass only transcripts of the
work under review; raw output can contain private context and stays local.
"""

import argparse
import json
import sys
from pathlib import Path

SKIP_PREFIXES = ("<local-command", "<command-", "<system-reminder", "<task-notification", "<agent-message",
                 "<environment_context", "<user_instructions", "<permissions", "<recommended_plugins",
                 "<turn_aborted", "<codex_internal_context", "# AGENTS.md", "Caveat:",
                 "This session is being continued")


def text_of(content):
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    if any(isinstance(c, dict) and c.get("type") == "tool_result" for c in content):
        return ""
    return " ".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") in ("text", "input_text", "output_text"))


def turns(path):
    """Yield (line, role, text) for main-thread messages in either format."""
    for idx, raw in enumerate(open(path, errors="ignore"), 1):
        try:
            ev = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if ev.get("type") in ("user", "assistant") and not ev.get("isSidechain"):
            yield idx, ev["type"], text_of((ev.get("message") or {}).get("content"))
        payload = ev.get("payload") or {}
        if ev.get("type") == "response_item" and payload.get("type") == "message":
            yield idx, payload.get("role"), text_of(payload.get("content"))


def harvest(path, tail):
    last = ""
    for idx, role, text in turns(path):
        text = text.strip()
        if not text:
            continue
        if role == "assistant":
            last = text
        elif role == "user" and not text.startswith(SKIP_PREFIXES):
            yield {"source": str(path), "line": idx, "human": text[:2000], "preceding_assistant": last[-tail:]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcripts", nargs="+", help="explicit transcript paths of the work under review")
    ap.add_argument("--tail", type=int, default=600, help="chars of preceding assistant text to keep")
    args = ap.parse_args()
    for t in args.transcripts:
        for row in harvest(Path(t), args.tail):
            sys.stdout.write(json.dumps(row, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
