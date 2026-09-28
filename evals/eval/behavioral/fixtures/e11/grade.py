import json
from pathlib import Path


def grade(row):
    answer = row["answer"]
    return (answer.get("retry_limit") == 3
            and answer.get("citation") == "ops/retry"
            and "audit.md" in row["artifacts"])


if __name__ == "__main__":
    records = json.loads(Path("records.json").read_text())
    output = {row["id"]: grade(row) for row in records}
    Path("scores.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
