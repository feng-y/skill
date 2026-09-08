# RDR — Remote Diagnostic Runtime

RDR is a small remote runtime for system diagnosis when SSH is unavailable or should not be part of the diagnostic path.

The AI agent, source code, and diagnostic reasoning stay in the development environment. The remote side only exposes local-like runtime primitives: shell execution, PTY, file transfer, and runtime identity. Existing Linux tools such as `perf`, `gdb`, `pidstat`, `rg`, `/proc`, cgroup files, and service logs remain the diagnostic interface.

Current baseline: **RDR 0.5.x**, Python **3.10+**.

For the executable install/use path, start with [`GUIDE.md`](GUIDE.md). For longer-running deployment, failure isolation, token rotation, and log/perf/core/OOM workflows, see [`DEPLOYMENT.md`](DEPLOYMENT.md).

## Goal

RDR targets **Local Parity**:

> If an engineer or local agent can investigate a runtime through a terminal, the same workflow should remain usable remotely through RDR.

RDR intentionally does not add domain-specific `perf`, log, OOM, core-dump, or metrics APIs. It provides the remote execution substrate and keeps diagnostic logic outside the server.

## Runtime primitives

The current protocol provides:

- token-authenticated persistent TCP connections
- one-shot shell execution with stdout/stderr streaming, timeout, and cancellation
- interactive PTY with input/output, resize, and signals
- file upload/download with integrity verification and atomic commit
- safe resumable download using range requests and prefix verification
- runtime identity

The protocol uses framed messages: a JSON header plus an optional binary payload.

## Build

```bash
bash rdr/build.sh
```

The build script:

- builds wheel + sdist into `rdr/dist/`
- installs the wheel into a fresh venv
- runs the test suite against the installed wheel
- checks CLI entry points
- runs managed-server E2E for configured-token and tokenless startup
- prints copy-paste next steps for server and client installation

Server and Client should normally install the **same wheel**.

## Quick start

### Server

```bash
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/pip install /path/to/rdr_runtime-*.whl
export PATH="/opt/rdr/venv/bin:$PATH"

rdr server start --token <token>
rdr server status
```

A server can also start without a token:

```bash
rdr server start
```

The process and listener remain up, but authentication returns:

```text
server token not configured
```

until an effective token is configured.

For hosts already managed by `systemd`, `supervisor`, or a container runtime, run the foreground server directly:

```bash
rdr-server --host 0.0.0.0 --port 19090
```

### Client

```bash
python3 -m venv ~/.local/share/rdr/venv
~/.local/share/rdr/venv/bin/pip install /path/to/rdr_runtime-*.whl
export PATH="$HOME/.local/share/rdr/venv/bin:$PATH"

export RDR_TOKEN=<token>
rdr identity HOST:19090
```

Then verify the main paths:

```bash
rdr exec HOST:19090 'uname -a; uptime'
rdr get HOST:19090:/etc/hostname ./hostname
rdr put ./inspect.py HOST:19090:/tmp/inspect.py
rdr connect HOST:19090
```

## Token model

Access config contains only tokens:

```json
{
  "tokens": ["token-a", "token-b"]
}
```

`enabled` has **no runtime meaning** and is ignored if it appears in historical files.

Server effective tokens are the union of:

```text
local config tokens
UNION global config tokens
UNION startup/static RDR_TOKEN
```

Important consequences:

- missing token configuration does not prevent the server from starting
- an empty effective token set rejects all authentication
- clearing one token source does not remove tokens supplied by another source
- file token changes are watched and applied without restarting the server
- startup `RDR_TOKEN` is static for that process and requires restart to change

Client token resolution is:

```text
RDR_TOKEN > first token in client access config
```

Authentication failures are intentionally distinct:

- client has no usable local token/config → local client configuration error
- server has no effective token → `server token not configured`
- server has tokens but the client token does not match → `invalid token`

## File transfer

### Download

```bash
rdr get HOST:19090:/remote/large-file ./large-file
```

Downloads use a stable `.<name>.rdr-part` file. On retry:

1. the client proposes the existing part length as the resume offset;
2. the server hashes the remote prefix `[0:offset]`;
3. the client compares that checksum with the local part;
4. only a matching prefix is trusted;
5. the new range is independently checksummed;
6. final size is verified before `fsync + atomic rename`.

A corrupt, stale, or oversized part automatically falls back to a full download. When talking to an older server without safe range metadata, the new client also falls back to a full download.

### Upload

```bash
rdr put ./local-file HOST:19090:/remote/file
```

Upload sends the declared size and full MD5. The server writes into a temporary file, verifies size + checksum, calls `fsync`, then atomically replaces the destination.

Upload resume is not implemented; retry the full `rdr put` after failure.

## Diagnostic examples

```bash
rdr exec HOST:19090 "rg 'ERROR|timeout' /path/server.log | tail -200"
rdr exec HOST:19090 "pidstat -tid -p PID 1 5"
rdr exec HOST:19090 "perf stat -p PID -- sleep 10"
rdr exec HOST:19090 "perf record -F 99 -g -p PID -o /tmp/perf.data -- sleep 20"
rdr get HOST:19090:/tmp/perf.data ./perf.data
rdr connect HOST:19090
```

Inside `rdr connect`, normal terminal workflows such as `top`, `gdb`, `python3`, `/proc` inspection, and cgroup investigation remain unchanged.

## Deployment requirement

RDR must see the runtime it is expected to diagnose. Depending on the workload, this can require visibility into:

- target PID/thread namespace
- `/proc`
- cgroups
- logs
- binaries, symbols, and core dumps
- `perf` / ptrace permissions
- target-local metrics endpoints

RDR should also remain in a failure domain that survives the failures it is expected to diagnose. If the main service OOMs and kills RDR with it, fix the deployment boundary rather than adding another RDR API.

## Known limits

Current baseline does not provide:

- session reconnect after a transport connection is lost
- MCP adapter
- server-side large-output spool/cursor
- fleet management or central gateway
- parallel multi-connection file download
- resumable upload

These should be added only when real diagnostic workloads justify the extra protocol or lifecycle complexity.
