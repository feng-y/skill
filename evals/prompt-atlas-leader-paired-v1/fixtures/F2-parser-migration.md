# F2 — Behavior-preserving parser migration

## Task input

> Merge the legacy streaming parser into the canonical parser, migrate every production consumer, preserve existing batch behavior plus streaming `trace_id` conversion and `streaming` default behavior, then delete the legacy module. Do not modify tests, add dependencies, or perform unrelated refactoring. Complete the work in the available runtime.

## Repository generator

```bash
set -euo pipefail
root="$1"
rm -rf "$root"
mkdir -p "$root/app" "$root/tests"
touch "$root/app/__init__.py"
cat > "$root/app/parser.py" <<'PY'
def parse_request(payload):
    return {
        "user_id": str(payload["user_id"]),
        "features": dict(payload.get("features", {})),
    }
PY
cat > "$root/app/stream_parser.py" <<'PY'
def parse_request(payload):
    result = {
        "user_id": str(payload["user_id"]),
        "features": dict(payload.get("features", {})),
        "streaming": bool(payload.get("streaming", True)),
    }
    if "trace_id" in payload:
        result["trace_id"] = str(payload["trace_id"])
    return result
PY
cat > "$root/app/batch_consumer.py" <<'PY'
from app.parser import parse_request


def handle(payload):
    return parse_request(payload)
PY
cat > "$root/app/stream_consumer.py" <<'PY'
from app.stream_parser import parse_request


def handle(payload):
    return parse_request(payload)
PY
cat > "$root/app/retry_consumer.py" <<'PY'
from app.stream_parser import parse_request


def handle(payload):
    parsed = parse_request(payload)
    return parsed if parsed["streaming"] else None
PY
cat > "$root/tests/test_batch.py" <<'PY'
from app.batch_consumer import handle


def test_batch_behavior():
    assert handle({"user_id": 7, "features": {"a": 1}}) == {
        "user_id": "7",
        "features": {"a": 1},
    }
PY
cat > "$root/.gitignore" <<'EOF'
__pycache__/
.pytest_cache/
*.py[cod]
EOF
(
  cd "$root"
  git init -q
  git config user.email fixture@example.com
  git config user.name fixture
  git add .
  git commit -qm fixture-f2
)
```

## Protected surfaces

- `tests/**`
- public consumer `handle(payload)` interfaces
- no dependency additions

## Public commands

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider -q
rg 'stream_parser|app\.stream_parser' app
git status --short
```

Expected initial state:

- visible tests exit 0 while covering only batch behavior;
- `rg` finds the legacy module and its production imports;
- `git status --short` is empty after the public checks.

## Budget

- 30 minutes wall clock per arm
- 4 materially different repair/replan attempts
- identical executor model, tools, and context limits

## Oracle manifest

```text
F2 oracle manifest v1
1 preserve canonical batch behavior
2 preserve streaming trace_id conversion and streaming default
3 migrate every production consumer
4 remove all legacy imports and legacy module
5 protected tests unchanged
6 no unrelated refactor or dependency
```

Manifest SHA-256: `814ba3191aacd2e42b5de95a25a76c5fe3a2fc382abaa3a1c95217d2bdcc2775`

Expected terminal capability: complete `PASS` is possible.
