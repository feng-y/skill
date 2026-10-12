#!/usr/bin/env python3
"""Run paired behavioral smoke cells with headless Claude Code CLI actors.

Eval-only backend. It prepares sanitized workspaces, installs each arm's Skill
sources, locks the rubric before launch, runs fresh actors in parallel, keeps
full stream-json transcripts, and records integrity / tool-call facts. Semantic
judging stays outside this script.
"""

import argparse
import concurrent.futures
import hashlib
import json
import os
import random
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
WORDS = (
    "alder aspen birch cedar elm fern gale hazel iris juno kale lark maple "
    "nori oak opal pecan quill reed sage teak umber vale wren yarrow zinnia "
    "acorn brook clove dune ember flint grove heath inlet jasper knoll loam "
    "moss nettle ochre pine quartz rowan sorrel thyme ulex vetch willow"
).split()
DEFAULT_TOOLS = "Bash Read Write Edit Glob Grep Agent"


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree_digest(root):
    out = {}
    for p in sorted(Path(root).rglob("*")):
        rel = p.relative_to(root).as_posix()
        if p.is_file() and not rel.startswith((".git/", ".agents/", ".claude/")):
            out[rel] = sha256_file(p)
    return out


def git(*args, cwd=REPO):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def install_arm(dest, ref, skills):
    """Copy Skill sources for one arm. ref='WORKTREE' uses the working tree;
    ref='NONE' installs nothing (a no-Skill control arm)."""
    blobs = {}
    if ref == "NONE":
        return blobs
    for skill in skills:
        target = dest / skill
        target.mkdir(parents=True, exist_ok=True)
        if ref == "WORKTREE":
            shutil.copytree(REPO / "skills" / skill, target, dirs_exist_ok=True)
        else:
            tar = subprocess.run(["git", "archive", ref, f"skills/{skill}"], cwd=REPO, check=True, capture_output=True).stdout
            subprocess.run(["tar", "-x", "-C", str(target), "--strip-components=2"], input=tar, check=True)
        blobs[skill] = sha256_file(target / "SKILL.md")
    return blobs


def prepare(spec, out):
    rubric = Path(spec["rubric"]).resolve()
    if not rubric.is_file():
        sys.exit("rubric must exist before launch")
    names = random.Random(spec.get("seed", 0)).sample(WORDS, k=sum(sum(c["arms"].values()) for c in spec["cells"]))
    actors = []
    for cell in spec["cells"]:
        fixture = Path(cell["fixture"]).resolve()
        for arm, count in cell["arms"].items():
            # A cell may give each arm its own prompt or Skill list, e.g. a slash
            # command in one arm and a plain request in the control.
            prompt_file = cell.get("prompt_files", {}).get(arm, cell.get("prompt_file"))
            prompt = Path(prompt_file).read_text()
            skills = cell.get("skills", spec["skills"])
            skills = skills[arm] if isinstance(skills, dict) else skills
            for _ in range(count):
                name = names.pop()
                ws = out / "ws" / name
                shutil.copytree(fixture, ws, ignore=shutil.ignore_patterns(".git"))
                subprocess.run(["git", "init", "-q"], cwd=ws, check=True)
                subprocess.run(["git", "add", "-A"], cwd=ws, check=True)
                subprocess.run(["git", "-c", "user.email=dev@example.com", "-c", "user.name=dev", "commit", "-qm", "init"], cwd=ws, check=True)
                skills_dir = cell.get("skills_dir", spec.get("skills_dir", ".agents/skills"))
                (ws / ".git" / "info" / "exclude").write_text(skills_dir.split("/")[0] + "/\n")
                blobs = install_arm(ws / skills_dir, spec["arms"][arm], skills)
                actors.append({
                    "name": name, "cell": cell["id"], "arm": arm, "ws": str(ws),
                    "prompt": prompt.replace("{ws}", str(ws)),
                    "disallowed_tools": cell.get("disallowed_tools", []),
                    "env": cell.get("env", {}),
                    "followups": [Path(f).read_text().replace("{ws}", str(ws)) for f in cell.get("followup_files", [])],
                    "skill_sha256": blobs, "pre": tree_digest(ws),
                })
    lock = {"rubric": str(rubric), "rubric_sha256": sha256_file(rubric), "locked_at": datetime.now(timezone.utc).isoformat()}
    return actors, lock


def session_id(transcript):
    sid = None
    for line in open(transcript):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "result" and ev.get("session_id"):
            sid = ev["session_id"]
    return sid


def run_actor(actor, spec, out):
    tmp = out / "tmp" / actor["name"]
    tmp.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, **actor.get("env", {}), "TMPDIR": str(tmp)}
    allowed = [t for t in spec.get("allowed_tools", DEFAULT_TOOLS).split() if t not in actor["disallowed_tools"]]
    cmd = [sys.executable, spec.get("claude", "/root/.claude/launch-direct.py"), "-p", actor["prompt"],
           "--model", spec["model"], "--output-format", "stream-json", "--verbose",
           "--allowedTools", " ".join(allowed),
           "--max-budget-usd", str(spec.get("max_budget_usd", 3))]
    if actor["disallowed_tools"]:
        cmd += ["--disallowedTools", " ".join(actor["disallowed_tools"])]
    transcript = out / "transcripts" / f"{actor['name']}.jsonl"
    start = time.time()
    # Follow-up turns resume the same session, so a Human correction lands in
    # the same agent context; all turns append to one transcript.
    with open(transcript, "w") as fh:
        proc = subprocess.run(cmd, cwd=actor["ws"], env=env, stdout=fh, stderr=subprocess.PIPE, text=True, timeout=spec.get("timeout_s", 1200))
    for followup in actor.get("followups", []):
        sid = session_id(transcript)
        if proc.returncode != 0 or not sid:
            break
        turn = cmd[:]
        turn[turn.index("-p") + 1] = followup
        turn += ["--resume", sid]
        with open(transcript, "a") as fh:
            proc = subprocess.run(turn, cwd=actor["ws"], env=env, stdout=fh, stderr=subprocess.PIPE, text=True, timeout=spec.get("timeout_s", 1200))
    actor["exit_code"] = proc.returncode
    actor["wall_s"] = round(time.time() - start, 1)
    actor["stderr_tail"] = proc.stderr[-2000:]
    actor["transcript"] = str(transcript)
    return actor


def analyze(actor):
    """Extract main-actor facts. Nested subagent events carry parent_tool_use_id
    and are kept out of the actor's own calls and texts; their completions and
    hand-back reports are read from task_notification events."""
    calls, acks, texts, completions, handbacks, final = [], {}, [], {}, {}, {}
    turns = []  # (line, origin sender task id, result text) for each turn-ending result event
    for idx, line in enumerate(open(actor["transcript"]), 1):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = ev.get("type")
        if kind == "result" and (ev.get("result") or "").strip():
            final = {k: ev.get(k) for k in ("result", "total_cost_usd", "num_turns", "is_error", "session_id")}
        elif kind == "result" and not final:
            final = {k: ev.get(k) for k in ("total_cost_usd", "num_turns", "is_error", "session_id")}
        if kind == "result":
            turns.append((idx, (ev.get("origin") or {}).get("senderTaskId"), ev.get("result") or ""))
        if kind == "system" and ev.get("subtype") == "task_notification":
            completions[ev.get("tool_use_id")] = {"line": idx, "status": ev.get("status"), "task_id": ev.get("task_id")}
        parent = ev.get("parent_tool_use_id")
        if parent is not None:
            for item in ((ev.get("message") or {}).get("content") or []):
                if isinstance(item, dict) and item.get("type") == "tool_use" and item.get("name") == "SubagentHandback":
                    handbacks[parent] = (item.get("input") or {}).get("message")
            continue
        content = (ev.get("message") or {}).get("content") or []
        for item in content if isinstance(content, list) else []:
            if not isinstance(item, dict):
                continue
            if kind == "assistant" and item.get("type") == "text":
                texts.append((idx, item.get("text") or ""))
            elif item.get("type") == "tool_use":
                inp = item.get("input") or {}
                entry = {"line": idx, "id": item["id"], "name": item["name"]}
                if item["name"] in ("Agent", "Task"):
                    entry["description"] = inp.get("description")
                    entry["prompt"] = inp.get("prompt")
                elif item["name"] == "Bash":
                    entry["command"] = (inp.get("command") or "")[:400]
                elif item["name"] in ("Read", "Skill"):
                    entry["target"] = inp.get("file_path") or inp.get("skill") or inp.get("name")
                calls.append(entry)
            elif item.get("type") == "tool_result":
                acks.setdefault(item.get("tool_use_id"), idx)
    # The synthesis is the actor's longest own text; short trailing texts are
    # status lines written after late notifications.
    synthesis = max(texts, key=lambda t: len(t[1]), default=(None, ""))
    if not (final.get("result") or "").strip():
        final["result"] = synthesis[1]
        final["result_source"] = "longest_assistant_text"
    agents = [c for c in calls if c["name"] in ("Agent", "Task")]
    for a in agents:
        a["completed_line"] = (completions.get(a["id"]) or {}).get("line")
        a["report"] = handbacks.get(a["id"])
    first_ack = min((acks.get(a["id"], 10**9) for a in agents), default=None)
    batch = [a for a in agents if first_ack is not None and a["line"] < first_ack]
    # A report reaches the model when a turn is triggered by that subagent's
    # hand-back (result origin.senderTaskId); stream order of system events
    # alone does not prove the model had read it.
    # Result events can be flushed after later texts, so match the synthesis
    # turn by its result text rather than by line position.
    head = synthesis[1][:200]
    synth_turn = next((ln for ln, _, text in turns if head and text.startswith(head)), None)
    delivered = {}
    for ln, sender, _ in turns:
        if sender and sender not in delivered:
            delivered[sender] = ln
    for a in agents:
        tid = (completions.get(a["id"]) or {}).get("task_id")
        a["delivered_turn_line"] = delivered.get(tid)
    actor.update({
        "final": final,
        "synthesis_line": synthesis[0],
        "tool_counts": {n: sum(1 for c in calls if c["name"] == n) for n in sorted({c["name"] for c in calls})},
        "agent_calls": agents,
        "agents_parallel": len(batch) >= 2,
        "parallel_batch": [a["description"] for a in batch],
        "sequential_agents": [a["description"] for a in agents if a not in batch],
        "synthesis_after_all_candidates": (None if not batch else
                                           all(a["delivered_turn_line"] is not None and synth_turn is not None
                                               and a["delivered_turn_line"] <= synth_turn for a in batch)),
        "tool_calls": calls,
    })
    if "pre" in actor:
        post = tree_digest(actor["ws"])
        actor["product_changed"] = sorted(k for k in set(actor["pre"]) | set(post) if actor["pre"].get(k) != post.get(k))
        del actor["pre"]
    return actor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-workers", type=int, default=6)
    ap.add_argument("--reanalyze", action="store_true", help="re-run analysis on an existing --out directory")
    args = ap.parse_args()
    if args.reanalyze:
        out = Path(args.out).resolve()
        record = json.loads((out / "outcomes.json").read_text())
        record["actors"] = [analyze(a) for a in record["actors"]]
        (out / "outcomes.json").write_text(json.dumps(record, ensure_ascii=False, indent=1))
        for a in record["actors"]:
            print(a["name"], a["cell"], a["arm"], "batch", a["parallel_batch"], "sequential", a["sequential_agents"],
                  "synthesis_after_all", a["synthesis_after_all_candidates"], "tools", a["tool_counts"])
        return
    spec = json.loads(Path(args.spec).read_text())
    out = Path(args.out).resolve()
    if out.exists():
        sys.exit(f"{out} exists; use a fresh output directory")
    (out / "transcripts").mkdir(parents=True)
    actors, lock = prepare(spec, out)
    print(json.dumps({"lock": lock, "actors": [(a["name"], a["cell"], a["arm"]) for a in actors]}), flush=True)
    with concurrent.futures.ThreadPoolExecutor(args.max_workers) as pool:
        done = list(pool.map(lambda a: analyze(run_actor(a, spec, out)), actors))
    record = {"spec": spec, "lock": lock, "repo_head": git("rev-parse", "HEAD").strip(), "actors": done}
    (out / "outcomes.json").write_text(json.dumps(record, ensure_ascii=False, indent=1))
    for a in done:
        print(a["name"], a["cell"], a["arm"], "exit", a["exit_code"], "cost", (a["final"] or {}).get("total_cost_usd"),
              "agents", len(a["agent_calls"]), "parallel", a["agents_parallel"],
              "synthesis_after_all", a["synthesis_after_all_candidates"], "changed", len(a["product_changed"]))


if __name__ == "__main__":
    main()
