#!/usr/bin/env python3
"""List the Human turns of a session transcript, with what the agent did between them.

Reads Claude Code or Codex JSONL transcripts. For each Human turn it prints the
transcript line, the Human text, the tail of the assistant text that preceded it,
and the agent work that followed until the next Human turn: tool calls, failed
tool calls, interrupts and the line span. Long spans, many failures and
interrupts mark struggles that no Human corrected. The default output is one
compact line per turn with a coverage header; --json gives full rows.

It does not classify or judge. Pass only transcripts of the work under review,
or --current for the newest transcript of this working directory. Output can
contain private context; keep it local.
"""

import argparse
import json
import os
import sys
from collections import Counter
from pathlib import Path

SKIP_PREFIXES = ("<local-command", "<command-", "<system-reminder", "<task-notification", "<agent-message",
                 "Another Claude session sent a message", "<environment_context", "<user_instructions",
                 "<permissions", "<recommended_plugins", "<turn_aborted", "<codex_internal_context",
                 "<skills_instructions", "<multi_agent_mode", "# AGENTS.md", "Caveat:",
                 "This session is being continued")
INTERRUPT_MARKERS = ("[Request interrupted by user", "<turn_aborted")


def text_of(content):
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return " ".join(c.get("text", "") for c in content
                    if isinstance(c, dict) and c.get("type") in ("text", "input_text", "output_text"))


def events(path):
    """Yield (line, kind, value) for main-thread events in either format.

    kind is 'human', 'assistant', 'tool' (value: name), 'tool_error' or 'interrupt'.
    """
    for idx, raw in enumerate(open(path, errors="ignore"), 1):
        try:
            ev = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if ev.get("type") in ("user", "assistant") and not ev.get("isSidechain"):
            content = (ev.get("message") or {}).get("content")
            if isinstance(content, list):
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    if c.get("type") == "tool_use":
                        yield idx, "tool", c.get("name", "?")
                    elif c.get("type") == "tool_result" and c.get("is_error"):
                        yield idx, "tool_error", None
                if any(isinstance(c, dict) and c.get("type") == "tool_result" for c in content):
                    continue
            text = text_of(content).strip()
            if text.startswith(INTERRUPT_MARKERS):
                yield idx, "interrupt", None
            elif text:
                yield idx, "human" if ev["type"] == "user" else "assistant", text
        payload = ev.get("payload") or {}
        kind = payload.get("type")
        if ev.get("type") == "response_item" and kind == "message":
            text = text_of(payload.get("content")).strip()
            if text and payload.get("role") in ("user", "assistant"):
                yield idx, "human" if payload["role"] == "user" else "assistant", text
        elif ev.get("type") == "response_item" and kind in ("function_call", "custom_tool_call", "web_search_call"):
            yield idx, "tool", payload.get("name", kind)
        elif ev.get("type") == "response_item" and kind in ("function_call_output", "custom_tool_call_output"):
            out = payload.get("output")
            out = out if isinstance(out, str) else json.dumps(out)
            if "Process exited with code " in out and "Process exited with code 0" not in out:
                yield idx, "tool_error", None
        elif ev.get("type") == "event_msg" and kind == "turn_aborted":
            yield idx, "interrupt", None


def turns(path, tail):
    rows, row, last = [], None, ""

    def close(end):
        if row is not None:
            row["work"]["until_line"] = end
            row["work"]["top_tools"] = dict(row["work"].pop("_tools").most_common(5))
            rows.append(row)

    end = 0
    for idx, kind, value in events(path):
        end = idx
        if kind == "assistant":
            last = value
        elif kind == "human" and not value.startswith(SKIP_PREFIXES):
            close(idx - 1)
            row = {"source": str(path), "line": idx, "human": value[:2000], "preceding_assistant": last[-tail:],
                   "work": {"tool_calls": 0, "tool_errors": 0, "interrupts": 0, "_tools": Counter()}}
        elif row is not None and kind == "tool":
            row["work"]["tool_calls"] += 1
            row["work"]["_tools"][value] += 1
        elif row is not None and kind == "tool_error":
            row["work"]["tool_errors"] += 1
        elif row is not None and kind == "interrupt":
            row["work"]["interrupts"] += 1
    close(end)
    return rows


def current_transcript(cwd):
    """Newest transcript whose session ran in cwd; never reads other projects' content."""
    found = []
    claude_dir = Path.home() / ".claude" / "projects" / "".join(c if c.isalnum() else "-" for c in str(cwd))
    found += list(claude_dir.glob("*.jsonl"))
    codex = sorted((Path.home() / ".codex" / "sessions").glob("*/*/*/rollout-*.jsonl"), key=os.path.getmtime)[-50:]
    for f in codex:
        try:
            first = json.loads(open(f).readline())
        except (json.JSONDecodeError, OSError):
            continue
        if (first.get("payload") or {}).get("cwd") == str(cwd):
            found.append(f)
    if not found:
        sys.exit(f"no Claude Code or Codex transcript found for {cwd}; name one explicitly")
    return max(found, key=os.path.getmtime)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcripts", nargs="*", help="explicit transcript paths of the work under review")
    ap.add_argument("--current", action="store_true", help="use the newest transcript of the current directory")
    ap.add_argument("--json", action="store_true", help="full JSON rows instead of the compact listing")
    ap.add_argument("--width", type=int, default=200, help="chars of Human text per turn in the compact listing")
    ap.add_argument("--tail", type=int, default=160, help="chars of preceding assistant text to keep")
    args = ap.parse_args()
    paths = [Path(t) for t in args.transcripts]
    if args.current:
        paths.append(current_transcript(Path.cwd().resolve()))
    if not paths:
        ap.error("name a transcript or pass --current")
    for t in paths:
        rows = turns(t, args.tail)
        if args.json:
            for row in rows:
                sys.stdout.write(json.dumps(row, ensure_ascii=False) + "\n")
            continue
        # Compact by default: a long session must fit in one read, or the
        # review silently covers only its first part.
        span = f"lines {rows[0]['line']}-{rows[-1]['work']['until_line']}" if rows else "no Human turns"
        print(f"# {t}: {len(rows)} Human turns, {span}")
        for r in rows:
            w = r["work"]
            flat = lambda s, n: " ".join(s.split())[:n]
            human = " ".join(r["human"].split())
            # Pasted reviews and logs put their findings after the opening
            # verdict, so flag cut turns for a full read.
            cut = f" [+{len(human) - args.width} chars, read in full]" if len(human) > args.width else ""
            print(f"L{r['line']}-{w['until_line']} tools={w['tool_calls']} err={w['tool_errors']} int={w['interrupts']} "
                  f"| H: {human[:args.width]}{cut} | before: {flat(r['preceding_assistant'], args.tail)}")


if __name__ == "__main__":
    main()
