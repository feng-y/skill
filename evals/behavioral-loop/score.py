import json
import sys

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

rows = []
with open(sys.argv[1], encoding="utf-8") as f:
    for line in f:
        if line.strip():
            rows.append(json.loads(line))

if not rows:
    raise SystemExit("no eval rows")

for field in FIELDS:
    values = [r[field] for r in rows if r.get(field) is not None]
    result = "n/a" if not values else f"{sum(v is True for v in values)}/{len(values)}"
    print(f"{field}: {result}")

for field in NEGATIVE:
    values = [r[field] for r in rows if r.get(field) is not None]
    result = "n/a" if not values else f"{sum(v is False for v in values)}/{len(values)} clean"
    print(f"{field}: {result}")
