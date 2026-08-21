#!/usr/bin/env python3

import argparse
import json
import statistics
import sys
from collections import defaultdict


ARMS = ("base", "candidate")
PAIR_EQUAL_FIELDS = (
    "target_repo",
    "target_ref",
    "model",
    "prompt_sha256",
    "human_response_profile",
    "tool_profile",
    "host_config",
)


def pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def num(value: float) -> str:
    if abs(value) >= 1000:
        return f"{value:,.0f}"
    return f"{value:.2f}"


def relative_delta(base: float, candidate: float):
    if base == 0:
        return None if candidate != 0 else 0.0
    return (candidate - base) / base


def load(path):
    records = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{lineno}: invalid JSON: {exc}") from exc
            validate_record(record, f"{path}:{lineno}")
            records.append(record)
    if not records:
        raise ValueError("no records")
    return records


def require(record, key, where):
    if key not in record:
        raise ValueError(f"{where}: missing field {key!r}")
    return record[key]


def non_negative_number(value, name, where):
    if not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0:
        raise ValueError(f"{where}: {name} must be a non-negative number")


def validate_record(record, where):
    if not isinstance(record, dict):
        raise ValueError(f"{where}: record must be an object")
    for key in (
        "case_id",
        "arm",
        "skill_ref",
        "target_repo",
        "target_ref",
        "model",
        "prompt_sha256",
        "human_response_profile",
        "tool_profile",
        "host_config",
    ):
        value = require(record, key, where)
        if not isinstance(value, str) or not value:
            raise ValueError(f"{where}: {key} must be a non-empty string")
    repeat = require(record, "repeat", where)
    if not isinstance(repeat, int) or isinstance(repeat, bool) or repeat < 1:
        raise ValueError(f"{where}: repeat must be a positive integer")
    if record["arm"] not in ARMS:
        raise ValueError(f"{where}: arm must be one of {ARMS}")

    for key in (
        "first_handoff_latency_ms",
        "input_tokens_to_handoff",
        "output_tokens_to_handoff",
        "tool_calls_to_handoff",
        "total_input_tokens",
        "total_output_tokens",
        "total_tool_calls",
    ):
        non_negative_number(require(record, key, where), key, where)

    clarifications = require(record, "clarifications", where)
    if not isinstance(clarifications, list):
        raise ValueError(f"{where}: clarifications must be a list")
    for item in clarifications:
        if not isinstance(item, dict) or not isinstance(item.get("contract_changing"), bool):
            raise ValueError(f"{where}: every clarification needs boolean contract_changing")

    compiled_work = require(record, "compiled_work", where)
    if not isinstance(compiled_work, list) or not compiled_work:
        raise ValueError(f"{where}: compiled_work must be a non-empty list")
    for item in compiled_work:
        if not isinstance(item, dict) or not isinstance(item.get("evidence_supported"), bool):
            raise ValueError(f"{where}: every compiled_work item needs boolean evidence_supported")

    if not isinstance(require(record, "executor_reinterpretation", where), bool):
        raise ValueError(f"{where}: executor_reinterpretation must be boolean")


def validate_pairs(records):
    grouped = defaultdict(dict)
    for record in records:
        key = (record["case_id"], record["repeat"])
        arm = record["arm"]
        if arm in grouped[key]:
            raise ValueError(f"duplicate {arm} record for case={key[0]!r} repeat={key[1]}")
        grouped[key][arm] = record

    missing = []
    for key, arms in sorted(grouped.items()):
        for arm in ARMS:
            if arm not in arms:
                missing.append((key, arm))
    if missing:
        detail = ", ".join(f"{case}/{repeat}:{arm}" for ((case, repeat), arm) in missing)
        raise ValueError(f"incomplete pairs: {detail}")

    for (case_id, repeat), arms in sorted(grouped.items()):
        base = arms["base"]
        candidate = arms["candidate"]
        if base["skill_ref"] == candidate["skill_ref"]:
            raise ValueError(f"case={case_id!r} repeat={repeat}: base and candidate skill_ref must differ")
        for field in PAIR_EQUAL_FIELDS:
            if base[field] != candidate[field]:
                raise ValueError(
                    f"case={case_id!r} repeat={repeat}: paired field {field!r} differs "
                    f"({base[field]!r} != {candidate[field]!r})"
                )
    return grouped


def rate(records, numerator, denominator):
    n = sum(numerator(record) for record in records)
    d = sum(denominator(record) for record in records)
    if d == 0:
        return 0.0
    return n / d


def aggregate(records):
    return {
        "handoff_latency_ms": statistics.median(r["first_handoff_latency_ms"] for r in records),
        "unnecessary_clarification_rate": rate(
            records,
            lambda r: sum(1 for q in r["clarifications"] if not q["contract_changing"]),
            lambda r: len(r["clarifications"]),
        ),
        "speculative_task_rate": rate(
            records,
            lambda r: sum(1 for w in r["compiled_work"] if not w["evidence_supported"]),
            lambda r: len(r["compiled_work"]),
        ),
        "executor_reinterpretation_rate": sum(1 for r in records if r["executor_reinterpretation"]) / len(records),
        "tokens_to_handoff": statistics.median(
            r["input_tokens_to_handoff"] + r["output_tokens_to_handoff"] for r in records
        ),
        "tool_calls_to_handoff": statistics.median(r["tool_calls_to_handoff"] for r in records),
        "total_tokens": statistics.median(r["total_input_tokens"] + r["total_output_tokens"] for r in records),
        "total_tool_calls": statistics.median(r["total_tool_calls"] for r in records),
    }


def render_metric(name, base, candidate, is_rate=False):
    display = pct if is_rate else num
    if is_rate:
        delta_text = f"{(candidate - base) * 100:+.2f} pp"
    else:
        delta = relative_delta(base, candidate)
        delta_text = "n/a" if delta is None else f"{delta * 100:+.2f}%"
    return f"| {name} | {display(base)} | {display(candidate)} | {delta_text} |"


def guardrail_status(base, candidate, tolerance, relative=False):
    if relative:
        if base == 0:
            return "PASS" if candidate == 0 else "REGRESS"
        return "PASS" if candidate <= base * (1 + tolerance) else "REGRESS"
    return "PASS" if candidate <= base + tolerance else "REGRESS"


def sample_readiness(pairs):
    repeats_by_case = defaultdict(set)
    for case_id, repeat in pairs:
        repeats_by_case[case_id].add(repeat)
    case_count = len(repeats_by_case)
    min_repeats = min(len(repeats) for repeats in repeats_by_case.values())
    return case_count, min_repeats, case_count >= 5 and min_repeats >= 3


def main():
    parser = argparse.ArgumentParser(description="Score paired Northstar clean-session behavioral eval records")
    parser.add_argument("results", help="JSONL run records")
    parser.add_argument("--rate-tolerance", type=float, default=0.02, help="allowed absolute quality-rate regression (default: 0.02)")
    parser.add_argument("--cost-tolerance", type=float, default=0.10, help="allowed relative latency/token/tool regression (default: 0.10)")
    args = parser.parse_args()

    try:
        records = load(args.results)
        pairs = validate_pairs(records)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    by_arm = {arm: [r for r in records if r["arm"] == arm] for arm in ARMS}
    stats = {arm: aggregate(by_arm[arm]) for arm in ARMS}
    base = stats["base"]
    candidate = stats["candidate"]
    case_count, min_repeats, claim_ready = sample_readiness(pairs)

    print(f"pairs: {len(pairs)}  cases: {case_count}  min repeats/case: {min_repeats}")
    print(f"base runs: {len(by_arm['base'])}  candidate runs: {len(by_arm['candidate'])}")
    print(f"behavioral-claim sample readiness: {'PASS' if claim_ready else 'SMOKE ONLY'}")
    print()
    print("| metric | base | candidate | candidate vs base |")
    print("| --- | ---: | ---: | ---: |")
    print(render_metric("first executable handoff latency (ms)", base["handoff_latency_ms"], candidate["handoff_latency_ms"]))
    print(render_metric("unnecessary clarification rate", base["unnecessary_clarification_rate"], candidate["unnecessary_clarification_rate"], True))
    print(render_metric("speculative task rate", base["speculative_task_rate"], candidate["speculative_task_rate"], True))
    print(render_metric("Executor reinterpretation rate", base["executor_reinterpretation_rate"], candidate["executor_reinterpretation_rate"], True))
    print(render_metric("tokens to first executable handoff", base["tokens_to_handoff"], candidate["tokens_to_handoff"]))
    print(render_metric("tool calls to first executable handoff", base["tool_calls_to_handoff"], candidate["tool_calls_to_handoff"]))
    print(render_metric("total tokens", base["total_tokens"], candidate["total_tokens"]))
    print(render_metric("total tool calls", base["total_tool_calls"], candidate["total_tool_calls"]))

    quality = {
        "unnecessary clarification": guardrail_status(base["unnecessary_clarification_rate"], candidate["unnecessary_clarification_rate"], args.rate_tolerance),
        "speculative task": guardrail_status(base["speculative_task_rate"], candidate["speculative_task_rate"], args.rate_tolerance),
        "Executor reinterpretation": guardrail_status(base["executor_reinterpretation_rate"], candidate["executor_reinterpretation_rate"], args.rate_tolerance),
    }
    efficiency = {
        "handoff latency": guardrail_status(base["handoff_latency_ms"], candidate["handoff_latency_ms"], args.cost_tolerance, relative=True),
        "tokens to handoff": guardrail_status(base["tokens_to_handoff"], candidate["tokens_to_handoff"], args.cost_tolerance, relative=True),
        "tool calls to handoff": guardrail_status(base["tool_calls_to_handoff"], candidate["tool_calls_to_handoff"], args.cost_tolerance, relative=True),
    }

    print()
    print("quality guardrails:")
    for name, status in quality.items():
        print(f"- {name}: {status}")
    print("efficiency guardrails:")
    for name, status in efficiency.items():
        print(f"- {name}: {status}")

    regressed = [name for name, status in {**quality, **efficiency}.items() if status != "PASS"]
    if regressed:
        print("\nresult: REGRESSION in " + ", ".join(regressed))
        return 1
    if not claim_ready:
        print("\nresult: NON-REGRESSION within configured tolerances; sample is smoke-only")
        return 0
    print("\nresult: NON-REGRESSION within configured tolerances; sample is claim-ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
