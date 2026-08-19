# RDR — Remote Diagnostic Runtime

RDR is a small Python remote runtime for system diagnosis when SSH is unavailable.

The AI agent stays in the development environment. The remote side contains no LLM or diagnostic reasoning. RDR exposes the target runtime with local-like primitives so existing Linux diagnostic workflows remain usable remotely.

For deployment, access policy, token rotation, smoke tests, failure isolation, and log/perf/core/OOM usage, read [`DEPLOYMENT.md`](DEPLOYMENT.md).

## Scope

RDR intentionally does not provide `perf`, log, OOM, core-dump, or metrics-specific APIs. Existing tools remain the diagnostic interface:

```bash
rg ERROR server.log
pidstat -tid -p "$pid" 1 5
perf stat -p "$pid" -- sleep 10
perf record -F 99 -g -p "$pid" -o /tmp/perf.data -- sleep 20
perf report -i /tmp/perf.data
gdb ./server core.xxx
journalctl -k
cat /sys/fs/cgroup/.../memory.events
curl localhost:8080/metrics
```

The design goal is **Local Parity**: if an engineer or local agent can investigate through a terminal, the same workflow should remain possible through RDR.

## Runtime primitives

The current protocol provides:

- token-authenticated persistent TCP connection
- one-shot shell execution with stdout/stderr streaming, timeout, and cancellation
- PTY terminal with input/output, resize, and signals
- file upload/download
- runtime identity

The data plane uses framed messages:

1. 4-byte big-endian JSON-header length
2. UTF-8 JSON header
3. optional binary payload declared by `payload_size`

## Client CLI

The client surface is intentionally close to SSH/scp:

```bash
rdr connect HOST:PORT
rdr exec HOST:PORT 'ps -ef'
rdr identity HOST:PORT
rdr get HOST:PORT:/tmp/perf.data ./perf.data
rdr put ./inspect.py HOST:PORT:/tmp/inspect.py
```

The client reads `~/.config/rdr/access.json` by default. `RDR_ACCESS_CONFIG` or command-local `--access-config` can override it.

## Quick local smoke test

```bash
cd rdr
python -m pip install -e .

cp config/access.example.json /tmp/rdr-access.json
# Replace the placeholder token in /tmp/rdr-access.json.

rdr-server \
  --host 127.0.0.1 \
  --port 19090 \
  --access-config /tmp/rdr-access.json \
  --global-access-config /tmp/nonexistent-rdr-global.json
```

From another terminal:

```bash
export RDR_ACCESS_CONFIG=/tmp/rdr-access.json
rdr identity 127.0.0.1:19090
rdr exec 127.0.0.1:19090 'uname -a'
rdr connect 127.0.0.1:19090
```

Production and shared/global access semantics are authoritative in [`DEPLOYMENT.md`](DEPLOYMENT.md); do not copy them into another runtime document.
