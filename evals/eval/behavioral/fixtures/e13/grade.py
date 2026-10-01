import json
from pathlib import Path


def grade(row, environment):
    return (row["answer"].get("retry_limit") == environment["retry_limit"]
            and row["answer"].get("citation") == environment["document"]
            and "audit.md" in row["artifacts"])


if __name__ == "__main__":
    environment = json.loads(Path("environment.json").read_text())
    records = json.loads(Path("records.json").read_text())
    output = {row["id"]: grade(row, environment) for row in records}
    Path("scores.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))
