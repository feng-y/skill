# RDR 部署与使用手册

本文描述 RDR（Remote Diagnostic Runtime）`0.6.x` 的部署、访问与运行边界。

RDR 的定位是远端运行环境：Claude Code、Codex 或工程师留在开发环境做 reasoning、代码阅读和决策，RDR Server 只把真实 Runtime Host 以接近本地 Terminal 的方式暴露出来。RDR 不运行 AI，也不提供 `perf` / `gdb` / OOM 等专用诊断 API。

最短安装与验证路径见 [`GUIDE.md`](GUIDE.md)；能力总览见 [`README.md`](README.md)。

## 1. 部署模型

推荐形态：

```text
Development Environment

Claude Code / Codex / Engineer
            |
            | rdr CLI / RDR Client
            | TCP + access token
            v
------------------------------------------------
Runtime Host

RDR Server                 Main Service
independent process         independent process
     |                           |
     +---- same runtime visibility ----+
     |
     +-- exec / stateful PTY / file
     +-- logs / proc / cgroup
     +-- perf / gdb / core
     +-- localhost metrics when network namespace is shared
```

RDR 可以和主服务一起构建、发布和升级，但应保持独立进程与可诊断的 failure domain。主服务 crash、deadlock、SIGKILL 或 HTTP 不可用时，RDR 应继续工作。

如果 OOM 是主要诊断场景，不要让 RDR 和主服务共享一个会整体被 OOM kill 的 failure domain。部署验收应包含“主服务异常后 RDR 仍可连接”。

## 2. Runtime 要求

Server 与 Client 都需要 Python 3.10+。推荐安装同一个 wheel：

```bash
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/python -m pip install /path/to/rdr_runtime-0.6.0-py3-none-any.whl
```

RDR 核心 runtime 无第三方依赖，但目标环境需要自行提供实际使用的系统工具，例如：

```text
perf
gdb
pidstat
rg
journalctl
```

为了达到 Local Parity，RDR 进程必须拥有真实诊断所需的 visibility 与权限：

- 目标服务 PID / thread 可见
- `/proc` 可见
- cgroup 可见
- 日志目录可见
- core dump、binary、symbols 可见
- `perf` / ptrace / kernel log 所需权限
- 查询 localhost metrics 时能访问对应 network namespace

RDR 不绕过 Linux permission、namespace、ptrace 或 perf policy。

## 3. 网络

默认监听：

```text
0.0.0.0:19090
```

开发环境需要能访问该 TCP 端口，SSH 可以不开。

当前 RDR Protocol 不自带 TLS。应运行在已有可信内部网络边界内，不要直接暴露到公网或不可信网络。

## 4. Access / Token

Access config 只表达允许访问的 token：

```json
{
  "tokens": ["token-a", "token-b"]
}
```

历史配置中的 `enabled` 没有任何 runtime 语义，会被忽略。

默认配置来源：

```text
local:  /etc/rdr/access.json
global: /data/bucket/rdr/access.json
static: RDR_TOKEN at process startup
```

Server effective tokens 是三个来源的并集：

```text
effective tokens
= local.tokens UNION global.tokens UNION static RDR_TOKEN
```

因此：

- 清空某一个文件只撤销该来源，不会覆盖其他来源。
- 要拒绝所有认证，必须保证所有 token 来源都为空。
- local/global 文件支持 watcher 更新；默认每 30 秒检查一次。
- 启动时注入的 `RDR_TOKEN` 是静态来源，修改需要重启进程。
- 文件不存在可以启动；文件存在但非法则启动失败，不静默绕过。
- effective token 为空时 Server 仍可启动并监听，但认证返回 `server token not configured`。

Managed CLI 的 `--token` 仅保留兼容；推荐使用 access config 或 `RDR_TOKEN`，避免 token 出现在 shell history 或启动记录中。

Client token 解析：

```text
RDR_TOKEN > client access config 的第一个 token
```

认证失败区分：

- client 本地无可用 token/config：本地配置错误，连接前失败
- server effective token 为空：`server token not configured`
- server 已有 token 但不匹配：`invalid token`

Token revoke 会关闭当前 authenticated connections，并终止 runtime-owned stateful terminals，避免已撤销 credential 留下长期后台 session。

## 5. 启动 Server

### 5.1 前台 / supervisor

```bash
/opt/rdr/venv/bin/rdr-server \
  --host 0.0.0.0 \
  --port 19090 \
  --access-config /etc/rdr/access.json \
  --global-access-config /data/bucket/rdr/access.json \
  --access-poll-seconds 30
```

生产长期运行建议交给 systemd、supervisor 或容器 runtime。

关键要求：

1. RDR 与主服务是独立进程。
2. RDR 异常退出后可由 supervisor 重启。
3. 主服务退出或重启时不要顺带杀掉 RDR。
4. 隔离不能破坏 RDR 对目标 PID、cgroup、日志、binary/core 的 visibility。

### 5.2 Managed Server

无 supervisor 的环境可使用：

```bash
rdr server start
rdr server status
rdr server stop
```

`start` 负责后台进程、pid file、log file 和 listener readiness。无 token 时仍会启动；`status` 会报告：

```text
process: ... alive
listener 127.0.0.1:19090: open
auth: server token not configured
```

并返回 non-zero，以区分“进程已启动”和“已可认证使用”。

### 5.3 Stateful Terminal attachment 数

同一个 stateful terminal 默认允许 **2** 个 active attachment，适合 Agent + human 同时观察或操作。

Server-wide 配置：

```bash
RDR_TERMINAL_MAX_ATTACHMENTS=1 rdr server start
```

前台 server 可显式指定：

```bash
rdr-server --port 19090 --terminal-max-attachments 4
```

需要严格独占 terminal 时设为 `1`。

## 6. Client 与 Agent 发现路径

开发环境安装同一个 wheel，并把 `rdr` 放入 PATH。

CLI 的 Agent-facing discovery 由 help 自己承担：

```bash
rdr --help
rdr connect --help
```

顶层区分两种 execution shape：

```text
stateless: rdr exec / identity / get / put
stateful:  rdr connect
```

一次性远端命令优先：

```bash
rdr exec HOST:19090 'command'
```

需要远端进程跨多轮 interaction 或 transport reconnect 保留 state 时，使用 stateful terminal：

```bash
rdr connect HOST:19090 --terminal-id debug
```

后续可通过：

```bash
rdr connect HOST:19090 --attach debug
```

重新 attach 同一个远端 PTY/process。

无需为 GDB、perf 或其他具体程序建立 RDR 专用 Skill/API；Agent 可以在需要时从 CLI help 发现 terminal 能力，再直接使用原生 Linux 工具。

## 7. Stateful Terminal

RDR `0.6.x` 的核心语义是：

> terminal/process lifetime belongs to the RDR runtime; TCP connections attach to it.

也就是：

```text
Agent connection A ----\
                       > terminal debug --> gdb / shell / REPL
Human connection B ----/
```

连接断开只 detach 当前 attachment，不 terminate 远端 process。

### 7.1 创建 / attach

```bash
rdr connect HOST:19090 --terminal-id core-debug
rdr connect HOST:19090 --attach core-debug
```

远端 process state 由原进程保存，例如 GDB 当前 thread/frame、shell variable、Python REPL state。

### 7.2 多 attachment

默认最多 2 个 connection 同时 attach：

- output 广播给所有 active attachment
- 每个 attachment 都可输入
- 输入按 frame 串行写入同一个 PTY
- `terminal.close()` 是全局结束，terminate terminal/process，对所有 attachment 生效
- 需要独占控制时把 server attachment limit 配成 1

V1 没有 per-terminal ACL；server token 集合是当前信任边界。

### 7.3 Detach / reconnect / replay

当 attachment 数变成 0，terminal 进入 detached 状态，但 process 继续运行。

此时 RDR 为该 terminal 保留最多 **4 MiB** output。第一个重新 attach 的 connection 会先收到 retained output，再接收 live output。

如果 detached output 超过 4 MiB，最旧内容被丢弃，client 会暴露 replay truncated 状态。

如果始终还有另一个 attachment 在线，则 terminal 从未进入 0-attachment 状态；V1 不为离线 viewer 保存 per-attachment catch-up cursor。

### 7.4 生命周期

```text
transport/client disconnect  -> detach current attachment, process survives
terminal.detach()             -> detach current attachment, process survives
terminal.close()              -> terminate terminal/process
remote process exits          -> terminal ends
token revoke                  -> terminate active/detached terminal
rdr server stop/shutdown      -> terminate all terminals
RDR server process restart    -> V1 cannot restore prior terminals
```

因此当前支持 **transport reconnect**，但不支持 **跨 RDR server process restart 的 session persistence**。

## 8. Stateless Operations

以下调用仍是 connection-scoped、一次性语义：

```bash
rdr identity HOST:19090
rdr exec HOST:19090 'uname -a'
rdr get HOST:19090:/remote/path ./local
rdr put ./local HOST:19090:/remote/path
```

`exec` 的 transport 断开会结束该 connection 所拥有的 command。需要长生命周期、需要跨 reconnect 保持 process state 的工作，应放入 stateful terminal，而不是为具体工具增加专用 API。

## 9. Perf

Perf 是 RDR 的通用 Linux-tool 场景。

一次性采样优先使用 stateless exec：

```bash
rdr exec HOST:19090 "pidstat -tid -p PID 1 5"
rdr exec HOST:19090 "perf stat -p PID -- sleep 10"
rdr exec HOST:19090 \
  "perf record -F 99 -g -p PID -o /tmp/rdr-perf.data -- sleep 20"
rdr exec HOST:19090 \
  "perf report -i /tmp/rdr-perf.data --stdio --percent-limit 0.5"
```

需要持续交互的 `perf top` / interactive `perf report` 可以直接运行在 stateful terminal 中。

大文件尽量留在远端，只在确有需要时下载：

```bash
rdr get HOST:19090:/tmp/rdr-perf.data ./rdr-perf.data
```

## 10. Core Dump / GDB

Core 很大时优先留在远端。复杂交互可使用稳定 terminal：

```bash
rdr connect HOST:19090 --terminal-id core-debug
```

然后正常运行：

```bash
gdb /path/server /path/core
```

例如：

```text
(gdb) info threads
(gdb) thread 17
(gdb) bt full
(gdb) frame 8
(gdb) info locals
(gdb) p variable
```

如果 transport 中断，新 connection 重新认证后：

```bash
rdr connect HOST:19090 --attach core-debug
```

会回到同一个 GDB process/PTY，继续之前的 state。

Live `gdb -p PID` 会 ptrace-stop 目标进程。这是 GDB/Linux 行为，不是 RDR 可以消除的副作用；生产进程 attach 应按实际冻结窗口和变更流程执行。

## 11. OOM / cgroup / logs

这些也保持通用 Linux workflow：

```bash
rdr exec HOST:19090 "rg 'ERROR|timeout' /path/server.log | tail -200"
rdr exec HOST:19090 "cat /proc/PID/smaps_rollup"
rdr exec HOST:19090 "cat /sys/fs/cgroup/.../memory.events"
rdr exec HOST:19090 "journalctl -k | tail -200"
```

如果主服务 OOM 后 RDR 也消失，应修复部署 failure domain，而不是增加 RDR API。

## 12. File Transfer

### 12.1 Download

```bash
rdr get HOST:19090:/remote/file ./file
```

下载使用稳定 `.<name>.rdr-part`：

- 中断后重试会尝试从现有 part 继续
- resume 前 server hash 远端 `[0:offset]` prefix，client 与本地 part prefix 比较
- prefix 不一致、part 过长或旧 server 缺少安全 range metadata 时自动从 0 重下
- 新传输 range 独立计算 MD5
- 最终核对 assembled size
- 成功后 `fsync + atomic rename`
- 失败/中断时保留 `.rdr-part`，目标文件不会被半截内容覆盖

Resume 节省的是网络传输量；为了确认已有 part 与当前远端文件一致，server 仍需要读取/hash remote prefix。

### 12.2 Upload

```bash
rdr put ./local-file HOST:19090:/remote/file
```

Client 发送 size + full MD5；Server 写临时文件，任一 chunk 使接收字节数超过声明 size 时立即拒绝并清理该 upload；完整接收后继续校验 size/checksum、`fsync`，成功后才 atomic replace 目标路径。

Upload 当前不支持 resume，失败后重新执行完整 `rdr put`。

## 13. Access 运维

Token 轮换推荐先增加新 token，再切 client，最后删除旧 token：

```json
{
  "tokens": ["old-token", "new-token"]
}
```

删除一个实际生效的 token 会关闭 authenticated connections，并清理 active/detached stateful terminals。这是访问边界的一部分。

如果要拒绝所有认证，请确认：

```text
local.tokens = []
global.tokens = []
no startup RDR_TOKEN
```

单独把某一个来源改成 `tokens: []` 不足以覆盖其他来源。

## 14. Smoke Test

首次部署至少验证：

```bash
rdr identity HOST:19090
rdr exec HOST:19090 'uname -a; id; pwd'
rdr get HOST:19090:/etc/hostname ./remote-hostname
rdr put ./inspect.py HOST:19090:/tmp/inspect.py
rdr connect HOST:19090
```

Stateful 能力需要验证时：

```bash
rdr connect HOST:19090 --terminal-id smoke-session
# 在远端设置可观察 state，然后断开 transport
rdr connect HOST:19090 --attach smoke-session
```

完整 package/test gate：

```bash
bash rdr/build.sh
```

## 15. 故障速查

| 现象 | 先查 |
|---|---|
| connection refused | server process / listener / 网络可达性 |
| server token not configured | effective token 三个来源是否全部为空 |
| invalid token | client 实际 token 是否在 server effective token 集合中 |
| terminal attachment limit reached | 当前 attachment 数；必要时调 `RDR_TERMINAL_MAX_ATTACHMENTS` 后重启 |
| unknown terminal | process 已退出、被 close、token revoke/server shutdown 清理，或 server 已重启 |
| replay truncated | 0 attachment 期间 output 超过 4 MiB |
| 看不到目标 PID/core/cgroup | namespace / mount / runtime visibility |
| perf/gdb Permission denied | uid / capability / ptrace / perf policy |
| 主服务 OOM 后 RDR 也消失 | failure domain 未隔离 |
| get 从 0 开始 | prefix 不匹配、part 过长或 server 不支持安全 range |
| put checksum/size mismatch | 临时文件不会 commit；修复后重试完整 upload |

## 16. 当前边界

RDR `0.6.x` 当前不提供：

- 跨 RDR server process restart 的 terminal/session persistence
- per-attachment output cursor / large-output spool
- terminal discovery/listing 与 per-terminal ACL
- MCP adapter
- fleet management / central gateway
- parallel multi-connection download
- resumable upload
- perf/log/core/OOM 专用 API

这些能力只有在真实使用 Evidence 证明存在稳定需求时再增加。当前验收标准仍是 Local Parity：与直接进入目标运行环境相比，Agent/工程师不应因为远程边界失去主要调查能力。
