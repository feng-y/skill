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
        if p.is_file() and not rel.startswith((".git/", ".agents/")):
            out[rel] = sha256_file(p)
    return out


def git(*args, cwd=REPO):
    return subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True, text=True).stdout


def install_arm(dest, ref, skills):
    """Copy Skill sources for one arm. ref='WORKTREE' uses the working tree."""
    blobs = {}
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
        prompt = Path(cell["prompt_file"]).read_text()
        for arm, count in cell["arms"].items():
            for _ in range(count):
                name = names.pop()
                ws = out / "ws" / name
                shutil.copytree(fixture, ws, ignore=shutil.ignore_patterns(".git"))
                subprocess.run(["git", "init", "-q"], cwd=ws, check=True)
                subprocess.run(["git", "add", "-A"], cwd=ws, check=True)
                subprocess.run(["git", "-c", "user.email=dev@example.com", "-c", "user.name=dev", "commit", "-qm", "init"], cwd=ws, check=True)
                (ws / ".git" / "info" / "exclude").write_text(".agents/\n")
                blobs = install_arm(ws / ".agents" / "skills", spec["arms"][arm], cell.get("skills", spec["skills"]))
                actors.append({
                    "name": name, "cell": cell["id"], "arm": arm, "ws": str(ws),
                    "prompt": prompt.replace("{ws}", str(ws)),
                    "disallowed_tools": cell.get("disallowed_tools", []),
                    "skill_sha256": blobs, "pre": tree_digest(ws),
                })
    lock = {"rubric": str(rubric), "rubric_sha256": sha256_file(rubric), "locked_at": datetime.now(timezone.utc).isoformat()}
    return actors, lock


def run_actor(actor, spec, out):
    tmp = out / "tmp" / actor["name"]
    tmp.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "TMPDIR": str(tmp)}
    allowed = [t for t in spec.get("allowed_tools", DEFAULT_TOOLS).split() if t not in actor["disallowed_tools"]]
    cmd = [sys.executable, spec.get("claude", "/root/.claude/launch-direct.py"), "-p", actor["prompt"],
           "--model", spec["model"], "--output-format", "stream-json", "--verbose",
           "--allowedTools", " ".join(allowed),
           "--max-budget-usd", str(spec.get("max_budget_usd", 3))]
    if actor["disallowed_tools"]:
        cmd += ["--disallowedTools", " ".join(actor["disallowed_tools"])]
    transcript = out / "transcripts" / f"{actor['name']}.jsonl"
    start = time.time()
    with open(transcript, "w") as fh:
        proc = subprocess.run(cmd, cwd=actor["ws"], env=env, stdout=fh, stderr=subprocess.PIPE, text=True, timeout=spec.get("timeout_s", 1200))
    actor["exit_code"] = proc.returncode
    actor["wall_s"] = round(time.time() - start, 1)
    actor["stderr_tail"] = proc.stderr[-2000:]
    actor["transcript"] = str(transcript)
    return actor


def analyze(actor):
    calls, results, final, texts = [], {}, {}, []
    order = 0
    for line in open(actor["transcript"]):
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        if ev.get("type") == "result":
            final = {k: ev.get(k) for k in ("result", "total_cost_usd", "num_turns", "is_error", "session_id")}
        content = (ev.get("message") or {}).get("content") or []
        for item in content if isinstance(content, list) else []:
            if not isinstance(item, dict):
                continue
            order += 1
            if item.get("type") == "text" and ev.get("type") == "assistant":
                texts.append(item.get("text") or "")
            if item.get("type") == "tool_use":
                inp = item.get("input") or {}
                entry = {"order": order, "id": item["id"], "name": item["name"]}
                if item["name"] in ("Agent", "Task"):
                    entry["description"] = inp.get("description")
                    entry["prompt"] = inp.get("prompt")
                elif item["name"] == "Bash":
                    entry["command"] = (inp.get("command") or "")[:400]
                calls.append(entry)
            elif item.get("type") == "tool_result":
                results.setdefault(item.get("tool_use_id"), order)
    if texts and not (final.get("result") or "").strip():
        # A session woken by background-task notifications ends with an empty
        # result event; the actor's real answer is its last assistant text.
        final["result"] = texts[-1]
        final["result_source"] = "last_assistant_text"
    agents = [c for c in calls if c["name"] in ("Agent", "Task")]
    first_result = min((results.get(a["id"], 10**9) for a in agents), default=None)
    # Agents issued before any Agent result returned form the parallel batch
    # (e.g. candidates); later calls such as an independent judge are sequential.
    parallel_batch = [a["description"] for a in agents if first_result is not None and a["order"] < first_result]
    post = tree_digest(actor["ws"])
    actor.update({
        "final": final,
        "tool_counts": {n: sum(1 for c in calls if c["name"] == n) for n in sorted({c["name"] for c in calls})},
        "agent_calls": agents,
        "agents_parallel": len(parallel_batch) >= 2,
        "parallel_batch": parallel_batch,
        "sequential_agents": [a["description"] for a in agents if a["description"] not in parallel_batch],
        "product_changed": sorted(k for k in set(actor["pre"]) | set(post) if actor["pre"].get(k) != post.get(k)),
        "tool_calls": calls,
    })
    del actor["pre"]
    return actor


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--out", required=True)
    ap.add_argument("--max-workers", type=int, default=6)
    args = ap.parse_args()
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
              "agents", len(a["agent_calls"]), "parallel", a["agents_parallel"], "changed", len(a["product_changed"]))


if __name__ == "__main__":
    main()
