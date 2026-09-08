#!/usr/bin/env bash
# Build and verify the rdr package.
#
# Produces dist/*.tar.gz and dist/*.whl, then verifies the wheel in a
# throwaway venv: the test suite runs against the installed wheel (not the
# source tree), and both console entry points are smoke-checked.
#
# Usage:
#   bash build.sh
#   RDR_BUILD_PYTHON=python3.12 bash build.sh   # pick interpreter
set -euo pipefail

package_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$package_root"

PYTHON="${RDR_BUILD_PYTHON:-python3}"

if ! "$PYTHON" -c 'import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)'; then
    echo "error: Python >= 3.10 required, found $("$PYTHON" -V 2>&1)" >&2
    exit 1
fi

echo "== clean =="
rm -rf build dist src/*.egg-info
find src tests -name '__pycache__' -type d -exec rm -rf {} +

workdir="$(mktemp -d)"
trap 'rm -rf "$workdir"' EXIT

echo "== build sdist + wheel =="
"$PYTHON" -m venv "$workdir/build-venv"
"$workdir/build-venv/bin/pip" install --quiet build
"$workdir/build-venv/bin/python" -m build --outdir dist

wheel="$(ls dist/*.whl)"
sdist="$(ls dist/*.tar.gz)"

echo "== verify wheel in fresh venv =="
"$PYTHON" -m venv "$workdir/verify-venv"
"$workdir/verify-venv/bin/pip" install --quiet pytest "$wheel"
verify_python="$workdir/verify-venv/bin/python"
rdr_bin="$workdir/verify-venv/bin/rdr"

# cwd is the package root (src layout), so "import rdr" resolves to the
# installed wheel; a broken wheel fails here instead of at deployment time.
"$verify_python" -m pytest tests -q

"$verify_python" - <<'EOF'
import glob
import zipfile

wheel = glob.glob("dist/*.whl")[0]
names = zipfile.ZipFile(wheel).namelist()
assert any(name == "rdr/server.py" for name in names), "runtime modules missing"
assert not any(name.startswith("tests/") for name in names), "tests leaked into wheel"
print("wheel contents ok")
EOF

"$verify_python" -c "import rdr; print('version:', rdr.__version__)"
"$rdr_bin" --help > /dev/null
"$workdir/verify-venv/bin/rdr-server" --help > /dev/null
echo "entry points ok"

echo "== managed server e2e: configured token =="
e2e_port=$((20000 + RANDOM % 10000))
export RDR_TOKEN="build-e2e-token"
export RDR_ACCESS_CONFIG="$workdir/missing-access.json"
export RDR_GLOBAL_ACCESS_CONFIG="$workdir/missing-global.json"
"$rdr_bin" server start \
    --host 127.0.0.1 --port "$e2e_port" \
    --pid-file "$workdir/server.pid" --log-file "$workdir/server.log"
"$rdr_bin" server status \
    --port "$e2e_port" --pid-file "$workdir/server.pid"
"$rdr_bin" server stop --pid-file "$workdir/server.pid"
"$verify_python" - "$e2e_port" <<'EOF'
import socket
import sys

port = int(sys.argv[1])
try:
    socket.create_connection(("127.0.0.1", port), timeout=0.5)
except OSError:
    print("listener closed after stop")
    sys.exit(0)
sys.exit("listener still open after stop")
EOF

echo "== managed server e2e: token not configured =="
unset RDR_TOKEN
no_token_port=$((20000 + RANDOM % 10000))
"$rdr_bin" server start \
    --host 127.0.0.1 --port "$no_token_port" \
    --pid-file "$workdir/no-token.pid" --log-file "$workdir/no-token.log"
if "$rdr_bin" server status \
    --port "$no_token_port" --pid-file "$workdir/no-token.pid" \
    >"$workdir/no-token-status.txt" 2>&1; then
    cat "$workdir/no-token-status.txt"
    "$rdr_bin" server stop --pid-file "$workdir/no-token.pid" || true
    echo "error: token-less server status unexpectedly succeeded" >&2
    exit 1
fi
cat "$workdir/no-token-status.txt"
grep -q "auth: server token not configured" "$workdir/no-token-status.txt"
"$rdr_bin" server stop --pid-file "$workdir/no-token.pid"

echo "== artifacts =="
ls -lh "$wheel" "$sdist"

cat <<EOF

== next steps ==
# server host: install into a dedicated venv, then start and verify
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/pip install "$package_root/$wheel"
/opt/rdr/venv/bin/rdr server start --token <token>   # or: RDR_TOKEN=<token>, or /etc/rdr/access.json
/opt/rdr/venv/bin/rdr server status

# dev host: separate client venv
python3 -m venv ~/.local/share/rdr/venv
~/.local/share/rdr/venv/bin/pip install "$package_root/$wheel"
RDR_TOKEN=<token> rdr identity <server-host>:19090

full flow: rdr/GUIDE.md
EOF
