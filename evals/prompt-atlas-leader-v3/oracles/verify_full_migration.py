import ast
import hashlib
import importlib
import json
import os
import pathlib
import subprocess
import sys


sys.dont_write_bytecode = True
repo = pathlib.Path(sys.argv[1]).resolve()
baseline = json.loads(pathlib.Path(sys.argv[2]).read_text())
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")

test_path = repo / "tests/test_parser.py"
assert hashlib.sha256(test_path.read_bytes()).hexdigest() == baseline["tests/test_parser.py"]
assert not (repo / "app/stream_parser.py").exists(), "legacy parser still exists"

definitions = []
for path in (repo / "app").glob("*.py"):
    text = path.read_text()
    assert "stream_parser" not in text, f"legacy parser reference remains in {path.name}"
    tree = ast.parse(text)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "parse_request":
            definitions.append(path.name)
assert definitions == ["parser.py"], definitions

sys.path.insert(0, str(repo))
parser = importlib.import_module("app.parser")
stream_consumer = importlib.import_module("app.stream_consumer")
batch_consumer = importlib.import_module("app.batch_consumer")

base = {"user_id": "7", "features": ["a"]}
assert parser.parse_request({"user_id": 7, "features": ["a"]}) == base
assert batch_consumer.consume({"user_id": 7, "features": ["a"]}) == base
assert batch_consumer.consume(
    {"user_id": 7, "features": ["a"], "trace_id": 42, "streaming": False}
) == base

assert stream_consumer.consume(
    {"user_id": 7, "features": ["a"], "trace_id": 42, "streaming": True}
) == {
    "user_id": "7",
    "features": ["a"],
    "trace_id": "42",
    "streaming": True,
}
assert stream_consumer.consume({"user_id": 7, "streaming": False}) == {
    "user_id": "7",
    "features": [],
    "streaming": False,
}
assert stream_consumer.consume({"user_id": 7}) == {
    "user_id": "7",
    "features": [],
    "streaming": True,
}

stream_source = (repo / "app/stream_consumer.py").read_text()
assert "trace_id" not in stream_source, "consumer reimplements trace parsing"
assert "payload.get" not in stream_source, "consumer reimplements parser defaults"

suite = subprocess.run(
    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
    cwd=repo,
    env=env,
    text=True,
    capture_output=True,
)
assert suite.returncode == 0, suite.stdout + suite.stderr

diff_check = subprocess.run(
    ["git", "diff", "--check"], cwd=repo, text=True, capture_output=True
)
assert diff_check.returncode == 0, diff_check.stdout + diff_check.stderr

allowed = {
    "README.md",
    "app/parser.py",
    "app/stream_consumer.py",
    "app/stream_parser.py",
    "PROGRESS.md",
    "BLOCKED.md",
}
status = subprocess.check_output(
    ["git", "status", "--porcelain=v1", "-z"], cwd=repo
).decode()
for entry in (item for item in status.split("\0") if item):
    assert entry[3:] in allowed, entry

print("ORACLE_PASS full-migration-v2")
