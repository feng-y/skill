#!/usr/bin/env python3

import argparse
import concurrent.futures
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import time
import uuid
from pathlib import Path


HISTORICAL_BASE_SHA = "8ba940f9e7d72d2b33d8137420de14523772bc43"
HISTORICAL_CANDIDATE_SHA = "4d9e65c294f826b16451f006ac7c7bb0480ff4d6"
MODEL = "gpt-5.6-sol"
REASONING = "high"
CLI_VERSION = "codex-cli 0.154.0"
TIMEOUT_SECONDS = 1200
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SKILL_REPO = Path(__file__).resolve().parents[2]
DISABLED_HOST_SKILLS = (
    "/root/.agents/skills/architecture-evolution/SKILL.md",
    "/root/.agents/skills/beacon/SKILL.md",
    "/root/.agents/skills/northstar/SKILL.md",
    "/root/.agents/skills/unknowns-first/SKILL.md",
    "/root/.agents/skills/verify/SKILL.md",
    "/root/.agents/skills/eval/SKILL.md",
)
SKILLS_CONFIG = "skills.config=[" + ",".join(
    f'{{path="{path}",enabled=false}}' for path in DISABLED_HOST_SKILLS
) + "]"

CASES = {
    "C1": [
        "/northstar 分析 Hermes 同时原生支持 Spec 和 ModelRequest 的方案，目标是不再做完整转换，同时保持现有 Spec 行为。调查必要事实并给出推荐 Draft，先不要修改产品代码。",
        "开始实现，按这个方案改。",
        "我说的透明双支持不是再包一层 adapter，把 ModelRequest 重建成接近 Spec 的对象；我期望两个 PB 的同语义字段直接复用同一套访问能力。这个属于原来‘透明’的意思。",
    ],
    "C2": [
        "review 这个 PR，评估是否可以合入；有 blocker 就告诉我。",
        "直接合入。",
    ],
    "C3": [
        "我们已经确定 protobuf SDK 要让单 message 和 repeated message 使用同一套访问抽象，调用方不应该关心字段来自哪种容器。现在只把 accessor 的具体接口形态做成一个可检查的 draft，其他设计保持不变。",
        "repeated 子 message 这里不能复制或迁移数据，要保持共享/零拷贝访问；其他接口和语义都保持原样。",
    ],
}


def run_command(args, *, cwd=None, env=None, timeout=120, input_text=None):
    process = subprocess.Popen(
        args,
        cwd=cwd,
        env=env,
        stdin=subprocess.PIPE if input_text is not None else subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        start_new_session=True,
    )
    try:
        stdout, stderr = process.communicate(input=input_text, timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGTERM)
        try:
            stdout, stderr = process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            stdout, stderr = process.communicate()
        return 124, stdout, stderr + f"\nTIMEOUT after {timeout}s\n"
    return process.returncode, stdout, stderr


def checked(args, *, cwd=None, env=None, timeout=120, input_text=None):
    code, stdout, stderr = run_command(
        args, cwd=cwd, env=env, timeout=timeout, input_text=input_text
    )
    if code != 0:
        raise RuntimeError(
            f"command failed ({code}): {args!r}\nstdout:\n{stdout}\nstderr:\n{stderr}"
        )
    return stdout


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8", errors="replace")).hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def install_skills(home, skill_sha):
    home.mkdir(parents=True)
    auth = Path("/root/.codex/auth.json")
    if not auth.is_file():
        raise RuntimeError(f"missing Codex auth file: {auth}")
    (home / "auth.json").symlink_to(auth)

    archive = subprocess.Popen(
        ["git", "archive", skill_sha, "skills"],
        cwd=SKILL_REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    extract = subprocess.run(
        ["tar", "-x", "-C", str(home)],
        stdin=archive.stdout,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if archive.stdout is not None:
        archive.stdout.close()
    archive_stderr = archive.stderr.read().decode("utf-8", errors="replace")
    archive_code = archive.wait()
    if archive_code != 0 or extract.returncode != 0:
        raise RuntimeError(
            "skill extraction failed: "
            + archive_stderr
            + extract.stderr.decode("utf-8", errors="replace")
        )
    for required in ("eval", "northstar", "beacon"):
        if not (home / "skills" / required / "SKILL.md").is_file():
            raise RuntimeError(f"missing installed skill: {required}")


def init_fixture_repo(repo, case_id):
    shutil.copytree(FIXTURES / case_id.lower(), repo)
    checked(["git", "init", "-q"], cwd=repo)
    checked(["git", "config", "user.email", "eval@example.invalid"], cwd=repo)
    checked(["git", "config", "user.name", "Behavioral Eval"], cwd=repo)
    checked(["git", "add", "-A"], cwd=repo)
    checked(["git", "commit", "-q", "-m", f"fixture {case_id}"], cwd=repo)


def git_output(repo, *args):
    return checked(["git", *args], cwd=repo, timeout=180)


def artifact_files(repo):
    captured = {}
    for relative in (
        "docs/accessor-interface-draft.md",
        "docs/accepted-context.md",
        "hermes/access.py",
        "hermes/engine.py",
        "tests/test_engine.py",
        "app/config.txt",
        ".eval/pr-state.json",
        ".eval/tool-log.jsonl",
    ):
        path = repo / relative
        if path.is_file():
            value = path.read_text(encoding="utf-8", errors="replace")
            captured[relative] = {
                "sha256": sha256_text(value),
                "content": value[:100_000],
                "truncated": len(value) > 100_000,
            }
    return captured


def snapshot(repo, state_dir, label):
    state_dir.mkdir(parents=True, exist_ok=True)
    head = git_output(repo, "rev-parse", "HEAD").strip()
    status = git_output(repo, "status", "--porcelain=v1", "--untracked-files=all")
    diff = git_output(repo, "diff", "--binary", "HEAD")
    diff_stat = git_output(repo, "diff", "--stat", "HEAD")
    patch_path = state_dir / f"{label}.patch"
    patch_path.write_text(diff, encoding="utf-8")
    result = {
        "label": label,
        "head": head,
        "status": status,
        "diff_sha256": sha256_text(diff),
        "diff_bytes": len(diff.encode("utf-8")),
        "diff_stat": diff_stat,
        "patch": str(patch_path),
        "artifact_files": artifact_files(repo),
    }
    write_json(state_dir / f"{label}.json", result)
    return result


def parse_thread_id(events):
    for line in events.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "thread.started" and event.get("thread_id"):
            return event["thread_id"]
    return None


def run_actor_turn(run_dir, home, repo, turn_number, prompt, thread_id=None):
    final_path = run_dir / f"turn-{turn_number}-final.md"
    common = [
        "--ignore-user-config",
        "--json",
        "-m",
        MODEL,
        "-c",
        f'model_reasoning_effort="{REASONING}"',
        "-c",
        'approval_policy="never"',
        "-c",
        'sandbox_mode="danger-full-access"',
        "-c",
        SKILLS_CONFIG,
        "--dangerously-bypass-approvals-and-sandbox",
        "--output-last-message",
        str(final_path),
    ]
    if thread_id is None:
        command = [
            "codex",
            "exec",
            *common,
            "-C",
            str(repo),
            "-",
        ]
    else:
        command = ["codex", "exec", "resume", *common, thread_id, "-"]

    env = os.environ.copy()
    env["CODEX_HOME"] = str(home)
    started = time.time()
    code, stdout, stderr = run_command(
        command,
        cwd=repo,
        env=env,
        timeout=TIMEOUT_SECONDS,
        input_text=prompt,
    )
    elapsed = time.time() - started
    (run_dir / f"turn-{turn_number}.jsonl").write_text(stdout, encoding="utf-8")
    (run_dir / f"turn-{turn_number}.stderr.txt").write_text(stderr, encoding="utf-8")
    meta = {
        "turn": turn_number,
        "exit_code": code,
        "elapsed_seconds": elapsed,
        "prompt_sha256": sha256_text(prompt),
        "thread_id": thread_id or parse_thread_id(stdout),
        "final_message": final_path.read_text(encoding="utf-8", errors="replace")
        if final_path.is_file()
        else "",
    }
    write_json(run_dir / f"turn-{turn_number}-meta.json", meta)
    return meta


def run_one(spec, output_root, revisions):
    case_id, arm, repeat, run_id = spec
    run_dir = output_root / "runs" / run_id
    home = run_dir / "codex-home"
    repo = run_dir / "workspace"
    run_dir.mkdir(parents=True)
    skill_sha = revisions[arm]
    install_skills(home, skill_sha)
    init_fixture_repo(repo, case_id)
    target_ref = git_output(repo, "rev-parse", "HEAD").strip()
    target_repo = f"fixture:{case_id}"

    manifest = {
        "run_id": run_id,
        "case_id": case_id,
        "arm": arm,
        "repeat": repeat,
        "skill_sha": skill_sha,
        "target_repo": target_repo,
        "target_ref": target_ref,
        "model": MODEL,
        "reasoning": REASONING,
        "cli_version": CLI_VERSION,
        "sandbox": "danger-full-access",
        "approval_policy": "never",
        "disabled_host_skill_paths": list(DISABLED_HOST_SKILLS),
        "human_response_policy": "frozen-turns-only/no-extra-answer",
        "timeout_seconds_per_turn": TIMEOUT_SECONDS,
        "actor_workspace": str(repo),
        "actor_home": str(home),
        "prompts_sha256": [sha256_text(prompt) for prompt in CASES[case_id]],
    }
    write_json(run_dir / "manifest.json", manifest)
    snapshots = [snapshot(repo, run_dir / "state", "turn-0")]
    turns = []
    thread_id = None
    for number, prompt in enumerate(CASES[case_id], 1):
        turn = run_actor_turn(run_dir, home, repo, number, prompt, thread_id)
        turns.append(turn)
        if thread_id is None:
            thread_id = turn["thread_id"]
        snapshots.append(snapshot(repo, run_dir / "state", f"turn-{number}"))
        if turn["exit_code"] != 0 or not thread_id:
            break

    session_files = [str(path) for path in home.glob("sessions/**/*.jsonl")]
    result = {
        **manifest,
        "thread_id": thread_id,
        "turns": turns,
        "snapshots": snapshots,
        "session_files": session_files,
        "completed_all_turns": len(turns) == len(CASES[case_id])
        and all(turn["exit_code"] == 0 for turn in turns),
    }
    write_json(run_dir / "run-result.json", result)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--max-workers", type=int, default=3)
    parser.add_argument("--case", choices=["all", *CASES], default="all")
    parser.add_argument(
        "--base-sha",
        required=True,
        help=f"Base skill revision. Historical accepted measurement used {HISTORICAL_BASE_SHA}.",
    )
    parser.add_argument(
        "--candidate-sha",
        required=True,
        help=(
            "Candidate skill revision. Historical accepted measurement used "
            f"{HISTORICAL_CANDIDATE_SHA}."
        ),
    )
    args = parser.parse_args()

    output_root = args.output_root.resolve()
    if output_root.exists() and any(output_root.iterdir()):
        raise SystemExit(f"output root must be empty or absent: {output_root}")
    output_root.mkdir(parents=True, exist_ok=True)
    cases = list(CASES) if args.case == "all" else [args.case]
    revisions = {"base": args.base_sha, "candidate": args.candidate_sha}
    specs = []
    for case_id in cases:
        for repeat in range(1, 4):
            for arm in ARMS:
                specs.append((case_id, arm, repeat, uuid.uuid4().hex[:12]))

    suite = {
        "base_sha": revisions["base"],
        "candidate_sha": revisions["candidate"],
        "target_environment": "revision-independent executable fixtures",
        "model": MODEL,
        "reasoning": REASONING,
        "cli_version": CLI_VERSION,
        "run_count": len(specs),
        "runs": [
            {"case_id": case, "arm": arm, "repeat": repeat, "run_id": run_id}
            for case, arm, repeat, run_id in specs
        ],
    }
    write_json(output_root / "suite-manifest.json", suite)

    results = []
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.max_workers) as pool:
        futures = {
            pool.submit(run_one, spec, output_root, revisions): spec
            for spec in specs
        }
        for future in concurrent.futures.as_completed(futures):
            spec = futures[future]
            try:
                result = future.result()
                results.append(result)
                print(
                    f"done {result['case_id']} {result['arm']} r{result['repeat']} "
                    f"{result['run_id']} turns={len(result['turns'])}",
                    flush=True,
                )
            except Exception as exc:
                failures.append({"spec": spec, "error": repr(exc)})
                print(f"failed {spec}: {exc}", file=sys.stderr, flush=True)

    write_json(output_root / "actor-results.json", results)
    write_json(output_root / "actor-failures.json", failures)
    print(f"output_root={output_root}")
    print(f"completed={len(results)} failed={len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
