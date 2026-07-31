# F4 — Forced cross-context parser migration

## Task input

> Consolidate the legacy parser into the canonical parser across all production consumers, preserve batch and streaming behavior, and delete the legacy module only after complete migration and proof. The run will be interrupted and resumed in a clean executor context. Preserve enough truthful state to continue without replaying the conversation or repeating completed work. Do not modify protected tests, add dependencies, or commit runtime scratch state.

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
cat > "$root/app/audit_consumer.py" <<'PY'
from app.stream_parser import parse_request


def handle(payload):
    return parse_request(payload).get("trace_id")
PY
cat > "$root/app/export_consumer.py" <<'PY'
from app.parser import parse_request


def handle(payload):
    return parse_request(payload)["user_id"]
PY
cat > "$root/tests/test_batch.py" <<'PY'
from app.batch_consumer import handle


def test_batch_behavior():
    assert handle({"user_id": 7, "features": {"a": 1}}) == {
        "user_id": "7",
        "features": {"a": 1},
    }
PY
cat > "$root/tests/test_export.py" <<'PY'
from app.export_consumer import handle


def test_export_user_id():
    assert handle({"user_id": 9}) == "9"
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
  git commit -qm fixture-f4
)
```

## Forced run event

The run driver terminates the first executor immediately after all three conditions hold:

1. pre-execution settlement is complete;
2. at least one production consumer migration is complete and locally verified;
3. remaining work still exists.

Start a clean executor with only:

- the original compiled carrier/taskbook;
- repository worktree and git history;
- runtime-created project-local continuity artifacts.

Do not provide prior chat or action transcript.

## Protected surfaces

- `tests/**`
- public consumer `handle(payload)` interfaces
- no dependency additions
- runtime scratch state must remain uncommitted

## Public commands

```bash
PYTHONDONTWRITEBYTECODE=1 python -m pytest -p no:cacheprovider -q
rg 'stream_parser|app\.stream_parser' app
git status --short
```

Expected initial state:

- visible tests exit 0 while covering only batch/export behavior;
- `rg` finds remaining legacy imports and module references;
- `git status --short` is empty after the public checks.

## Budget

- 40 minutes aggregate wall clock per arm
- exactly one forced clean-context restart
- 5 materially different repair/replan attempts aggregate
- identical executor model, tools, and context limits for both contexts and arms

## Oracle manifest

```text
F4 oracle manifest v1
1 resume from forced clean-context restart
2 preserve goal and boundaries
3 retain completed settlement and work evidence
4 avoid duplicate or lost work
5 invalidate stale evidence after upstream changes
6 finish migration and legacy removal
7 continuity file not committed
```

Manifest SHA-256: `2a6a376bcf288bd54c32ad07f24bc7f974a79f389ea3141d278f2a3ecdc1ec47`

Expected terminal capability: complete `PASS` is possible.
