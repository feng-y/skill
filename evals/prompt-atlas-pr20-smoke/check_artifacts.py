from pathlib import Path
import re

root = Path(__file__).resolve().parents[2]
text = Path(__file__).with_name("ARTIFACTS.md").read_text()
compile_contract = (root / "skills/prompt-atlas/references/execution-compile.md").read_text()
graph_contract = (root / "skills/prompt-atlas/references/execution-graph.md").read_text()

for phrase in (
    "consumes an upstream result",
    "Do not add transitive or merely sequential edges",
):
    assert phrase in graph_contract, phrase

for phrase in (
    "Compile only information that constrains a future decision",
    "dependency changes, permissions, external-system writes",
    "emits a short opening receipt",
    "correct a clear taskbook misunderstanding",
    "at least one Task or required Task 0 can start immediately",
    "authority-sensitive operations are bounded",
    "Do not compile scheduler, lease, or fixed Agent topology",
):
    assert phrase in compile_contract, phrase

case_pattern = re.compile(r"^## (S\d+) — .*?\n\n```markdown\n(.*?)\n```", re.M | re.S)
cases = dict(case_pattern.findall(text))
assert set(cases) == {f"S{i}" for i in range(1, 7)}, sorted(cases)

headings = [
    "## Contract Header",
    "## 1. Delegated Decisions",
    "## 2. Boundaries and Authority",
    "## 3. Current Reality and Task 0",
    "## 4. Execution",
    "## 5. Execution Rules and Continuity",
    "## 6. Completion and Acceptance",
]

for name in ("S1", "S2", "S3", "S4", "S6"):
    body = cases[name]
    assert body.startswith("Status: Executable"), name
    positions = [body.index(h) for h in headings]
    assert positions == sorted(positions), (name, positions)
    assert "### Task " in body, name
    assert "multiple taskbooks" not in body.lower(), name
    assert "node schema" not in body.lower(), name
    assert "taskgroup" not in body.lower(), name
    assert "graph dsl" not in body.lower(), name
    assert "agent a" not in body.lower() and "agent b" not in body.lower(), name

for name in ("S1", "S3", "S6"):
    body = cases[name].lower()
    assert "may run in parallel" not in body, name
    assert "execution graph" not in body and "dependency graph" not in body, name

s2 = cases["S2"].lower()
for phrase in ("depends on task 1", "may run in parallel", "after both tasks 2 and 3 pass"):
    assert phrase in s2, phrase
assert "one owner" in s2
assert "evidence is invalid" in s2 and "must be rerun" in s2
assert "only this complete result may close the goal" in s2

s3 = cases["S3"].lower()
assert "one linear pass" in s3
assert "many files" in s3

s4 = cases["S4"].lower()
assert "parked branch" in s4
assert "global failure" in s4
assert "resolving condition" in s4

s5 = cases["S5"]
assert s5.startswith("Status: Unresolved Intent")
assert all(h not in s5 for h in headings)

s6 = cases["S6"].lower()
assert "ready for independent acceptance" in s6
assert "reserved private-check contents are not included" in s6
assert "global pass" in s6

print("PR20_SMOKE_PASS cases=6 executable=5 unresolved=1")
