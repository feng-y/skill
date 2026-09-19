"""Summarize judged rows without pooling variants or treating them as proof."""
import argparse
from collections import defaultdict
import json
from pathlib import Path

FIELDS = [
    "intent_fidelity",
    "fact_grounding",
    "evidence_concretization",
    "architecture_reaction",
    "verification_fidelity",
    "targeted_reentry",
    "valid_work_preserved",
    "final_state_valid",
]
NEGATIVE = ["unnecessary_owner_call", "human_fact_question"]


def load_rows(path: Path) -> list[dict]:
    rows, seen = [], set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError("expected an object")
            for field in ("variant", "case_id"):
                value = row.get(field)
                if not isinstance(value, str) or not value.strip() or value != value.strip():
                    raise ValueError(f"{field} must be a non-empty, trimmed string")
            if type(row.get("repeat")) is not int or row["repeat"] < 1:
                raise ValueError("repeat must be a positive integer")
            key = (row["variant"], row["case_id"], row["repeat"])
            if key in seen:
                raise ValueError(f"duplicate run identity {key}")
            for field in FIELDS + NEGATIVE:
                if field not in row or (row[field] is not None and type(row[field]) is not bool):
                    raise ValueError(f"{field} must be present and boolean or null")
            seen.add(key)
            rows.append(row)
        except ValueError as exc:
            raise ValueError(f"line {line_number}: {exc}") from exc
    if not rows:
        raise ValueError("no eval rows")
    return rows


def validate_pairing(rows: list[dict], base: str, candidate: str) -> None:
    if base == candidate:
        raise ValueError("base and candidate must be distinct variants")
    arms = {
        variant: {(r["case_id"], r["repeat"]): r for r in rows if r["variant"] == variant}
        for variant in (base, candidate)
    }
    if not arms[base] or not arms[candidate]:
        raise ValueError("missing variant in comparison input")
    if arms[base].keys() != arms[candidate].keys():
        raise ValueError("base/candidate case/repeat sets differ; no paired comparison")
    for key, left in arms[base].items():
        right = arms[candidate][key]
        for field in FIELDS + NEGATIVE:
            if (left[field] is None) != (right[field] is None):
                raise ValueError(f"applicability mismatch at {key}: {field}")


def counts(rows: list[dict], field: str) -> tuple[int, int]:
    values = [r[field] for r in rows if r[field] is not None]
    desired = field not in NEGATIVE
    return sum(value is desired for value in values), len(values)


def ratio(value: tuple[int, int]) -> str:
    passed, total = value
    return f"{passed}/{total}" if total else "n/a"


def report(rows: list[dict], base: str | None, candidate: str | None) -> str:
    groups = defaultdict(list)
    for row in rows:
        groups[row["variant"], row["case_id"]].append(row)
    lines = ["Descriptive judged-row counts only; not trajectory validation or proof of uplift."]
    for (variant, case), members in sorted(groups.items()):
        lines.append(f"\nvariant={variant} case={case} runs={len(members)}")
        for field in FIELDS + NEGATIVE:
            suffix = " clean" if field in NEGATIVE else ""
            lines.append(f"{field}: {ratio(counts(members, field))}{suffix}")
    if base is None:
        lines.append("\nNo paired comparison; select --base and --candidate explicitly.")
        return "\n".join(lines)
    for case in sorted({r["case_id"] for r in rows if r["variant"] == base}):
        lines.append(f"\ncomparison={base}->{candidate} case={case}")
        for field in FIELDS + NEGATIVE:
            left = counts(groups[base, case], field)
            right = counts(groups[candidate, case], field)
            suffix = " clean" if field in NEGATIVE else ""
            delta = f"; delta {100 * (right[0] / right[1] - left[0] / left[1]):+.1f} pp" if left[1] else ""
            lines.append(f"{field}: {ratio(left)} -> {ratio(right)}{suffix}{delta}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results", type=Path)
    parser.add_argument("--base", help="Exact base variant label for paired comparison")
    parser.add_argument("--candidate", help="Exact candidate variant label for paired comparison")
    args = parser.parse_args()
    if (args.base is None) != (args.candidate is None):
        parser.error("--base and --candidate must be provided together")
    try:
        rows = load_rows(args.results)
        if args.base is not None:
            validate_pairing(rows, args.base, args.candidate)
    except (OSError, UnicodeError, ValueError) as exc:
        parser.error(str(exc))
    print(report(rows, args.base, args.candidate))


if __name__ == "__main__":
    main()
