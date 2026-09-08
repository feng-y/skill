# RDR 快速上手 Guide

当前基线：RDR `0.6.x`。最短可执行路径：构建 package → 安装并启动 server → 配 token → 安装 client → 验证。
本文是可直接执行的上手路径；更完整的部署背景、长期运维和诊断场景见 [`DEPLOYMENT.md`](DEPLOYMENT.md)。

## 0. 前置

- Server 与 Client 都需要 Python 3.10+
- 开发环境能访问 server 的 TCP 端口（默认 `19090`），SSH 可以不开
- `perf` / `gdb` / `pidstat` 等诊断工具 RDR 不负责安装，目标机缺什么先装什么
- Server 与 Client 推荐安装**同一个 wheel**；滚动升级时先升级 server，再升级 client

## 1. 构建并分发 package

在任一有 repo 的机器构建：

```bash
bash rdr/build.sh          # 产出 rdr/dist/*.whl + *.tar.gz，并执行测试、wheel 与 managed-server E2E
ls rdr/dist/*.whl
```

把同一个 `rdr_runtime-*.whl` 分发到 server host 与开发机。分发方式使用现有制品系统、文件共享或已有拷贝通道；RDR 本身不要求 SSH。

不需要 wheel 时，也可以在有 repo 的机器直接安装：

```bash
pip install ./rdr
```

## 2. 安装并启动 Server（远端主机）

建议 server 使用独立 venv：

```bash
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/python -m pip install /path/to/rdr_runtime-*.whl
export PATH="/opt/rdr/venv/bin:$PATH"

# 需要生成新 token 时
python3 -c "import secrets; print(secrets.token_urlsafe(24))"
```

### 配置 token（可选；优先级：`--token` > `RDR_TOKEN` > 文件）

Server 可以先在没有 token 的状态启动；listener 正常存在，但任何认证都会返回 `server token not configured`，`rdr server status` 也会以 non-zero 报告这一状态。需要建立可用连接时，通过以下任一方式配置 token：

1. `RDR_TOKEN` 环境变量 —— 启动进程时读取，修改后需要重启
2. `rdr server start --token <token>` —— 启动时一次性指定
3. `/etc/rdr/access.json` 文件 —— 生产推荐，支持 30s 热更新与轮换；server 已启动时创建该文件也会被 watcher 发现

```bash
mkdir -p /etc/rdr && cat > /etc/rdr/access.json <<'EOF'
{
  "tokens": ["<token>"]
}
EOF
chmod 600 /etc/rdr/access.json
```

有效 token 是 local config、global config 与启动时 `RDR_TOKEN` 的**并集**。`enabled` 没有任何 runtime 语义；历史配置里即使存在也会被忽略。把某一个配置文件改成 `tokens: []` 只会撤销该来源；如果要临时拒绝所有认证，需要确保所有 token 来源都为空。启动时注入的 `RDR_TOKEN` 不会被 watcher 热更新，移除它需要重启 server。

0.6.x 起，terminal/process 可以在 transport 断开后继续存在。为了保持 access boundary，**token revoke 会终止当前 active/detached terminal**；server shutdown 也会清理全部 terminal。

### 启动

**托管方式**（无 supervisor 的环境推荐）：

```bash
rdr server start          # token 可选；无 token 也启动并监听
rdr server status         # process / listener / auth；只有 auth 可用时 exit 0
rdr server stop           # 优雅终止
```

**前台方式**（交给 supervisor / systemd 托管）：

```bash
rdr-server --host 0.0.0.0 --port 19090
```

### 判断 server 启动成功

- `rdr server start` 就绪后打印 `rdr server ready: pid=... listen=...`
- `rdr server status` 分别报告 process / listener / auth
- 无 server token 时显示 `auth: server token not configured` 并返回 non-zero
- 前台模式 stdout 出现 `RDR server ready on ...`
- 最终从开发环境执行 `rdr identity HOST:19090` 验证网络 + auth + protocol

## 3. 安装 Client（开发环境）

Client 使用独立 venv，不与远端 server 共享运行时：

```bash
python3 -m venv ~/.local/share/rdr/venv
~/.local/share/rdr/venv/bin/pip install /path/to/rdr_runtime-*.whl
export PATH="$HOME/.local/share/rdr/venv/bin:$PATH"    # 可放入 ~/.bashrc
```

Client token 二选一：

```bash
export RDR_TOKEN=<token>
```

或：

```bash
mkdir -p ~/.config/rdr
cat > ~/.config/rdr/access.json <<'EOF'
{
  "tokens": ["<token>"]
}
EOF
chmod 600 ~/.config/rdr/access.json
```

`RDR_TOKEN` 优先于 client access config 的第一个 token。

认证失败明确区分：

- client 本地没有可用 token：CLI 在连接前直接报本地 token/config 错误
- server effective token 为空：`server token not configured`
- server 已配置 token，但 client token 不匹配：`invalid token`

## 4. 基础验证

```bash
rdr identity HOST:19090                         # hostname/pid/uid：认证 + 通道正常
rdr exec HOST:19090 'uname -a; uptime'          # one-shot 命令
rdr get HOST:19090:/etc/hostname ./hostname     # 下载
rdr put ./inspect.py HOST:19090:/tmp/inspect.py # 上传
rdr connect HOST:19090                           # 交互 PTY
```

建议首次部署至少验证 `identity / exec / get / put / connect` 五条路径。

## 5. 有状态任务：GDB / Shell / REPL

`identity / exec / get / put` 是一次请求即可完成的无状态操作。GDB、shell、Python REPL、`top`、`perf report` 等交互程序不同：状态保存在远端进程和 PTY 中，需要跨多轮 Agent 交互继续存在。

RDR 0.6.x 的 terminal 生命周期属于 **RDR runtime**，不是某条 TCP connection：

```text
connection A --attach--> terminal core-debug --> gdb

connection A 断开
                         terminal core-debug --> gdb 继续运行

connection B --attach--> terminal core-debug --> 同一个 gdb
```

### 创建稳定 terminal

复杂任务建议显式指定 terminal id：

```bash
rdr connect HOST:19090 --terminal-id core-debug
```

CLI 会在进入 raw terminal 前打印 terminal id。正常在远端 shell/GDB 中执行 `exit` 会结束该 terminal。

### transport 断开后恢复

如果 client/transport 意外断开，而远端进程仍在：

```bash
rdr connect HOST:19090 --attach core-debug
```

GDB 的当前 thread/frame、shell 变量、REPL state 等仍在原进程中，不需要重新启动工具。

### detached output

terminal detached 时，RDR 在 server 内保留最多 **4 MiB** 的输出。重新 attach 时会 replay 这部分 output，再继续实时输出。

如果 detached 期间输出超过 buffer，最旧部分会被丢弃；CLI 会明确警告 replay 被截断。这个 buffer 用于短期 reconnect，不是 large-output spool。

### 生命周期语义

- transport/client disconnect → **detach，不 kill process**
- `terminal.detach()` → 主动 detach，process 继续
- `terminal.close()` → terminate remote terminal/process
- remote process 自己退出 → terminal 结束
- token revoke → 清理 active + detached terminal
- `rdr server stop` / server shutdown → 清理全部 terminal
- RDR server process restart → 当前 V1 **不能恢复**之前的 terminal

同一个 terminal 同时只允许一个 active connection attach。当前 V1 以 server token 集合作为信任边界，没有 per-terminal ACL，也还没有 terminal list/discovery。

### Core dump 示例

```bash
rdr connect HOST:19090 --terminal-id core-debug
```

远端：

```gdb
gdb /path/server /path/core
info threads
thread 17
bt full
frame 8
info locals
```

如果中间连接断开：

```bash
rdr connect HOST:19090 --attach core-debug
```

继续原来的 GDB state：

```gdb
p variable
x/32gx ptr
```

程序接口同样支持：

```python
terminal = await client.open_terminal(
    command="gdb /path/server /path/core",
    terminal_id="core-debug",
)
await terminal.write(b"info threads\n")
await terminal.detach()

# new RDRClient connection
terminal = await client.attach_terminal("core-debug")
await terminal.write(b"thread 17\n")
```

## 6. 文件传输

### 下载：`rdr get`

```bash
rdr get HOST:19090:/remote/large-file ./large-file
```

下载使用稳定临时文件 `.<name>.rdr-part`：

- 中断后再次执行相同命令会尝试从现有 part 继续，而不是直接覆盖目标文件
- 续传前，server 会计算远端 `[0:offset]` 的 MD5，client 与本地 part prefix 比较；prefix 不一致会自动从 0 重新下载
- 新传输的 range 也有独立 MD5，最终再核对完整文件长度
- 只有校验完成后才 `fsync + atomic rename` 到目标路径；失败时现有目标文件不被半截内容覆盖
- 中断时 `.rdr-part` 会保留，用于下一次安全续传
- 如果连接的是不支持安全 range 元数据的旧 server，新 client 会自动退化为从 0 完整下载

续传减少的是网络传输量；为了确认已有 part 与当前远端文件一致，resume 会读取并 hash 已有 prefix。

### 上传：`rdr put`

```bash
rdr put ./local-file HOST:19090:/remote/file
```

上传会把本地文件 size 与完整 MD5 发送给 server；server 在临时文件中写入、核对 size + checksum、`fsync`，校验成功后才原子替换目标路径。上传当前**不支持断点续传**；失败后重新执行 `rdr put`。

## 7. 日常诊断

```bash
rdr exec HOST:19090 "rg 'ERROR|timeout' /path/server.log | tail -200"
rdr exec HOST:19090 "pidstat -tid -p PID 1 5"
rdr exec HOST:19090 "perf record -F 99 -g -p PID -o /tmp/perf.data -- sleep 20"
rdr exec HOST:19090 "perf report -i /tmp/perf.data --stdio --percent-limit 0.5"
```

大日志、core、OOM / cgroup 的完整工作流见 `DEPLOYMENT.md` §9。原则：采样和大文件尽量留在远端，只把需要的 Evidence 拉回开发环境。

## 8. 故障速查

| 现象 | 先查 |
|---|---|
| connection refused | `rdr server status` → `ss -tlnp \| grep 19090` → 网络可达性 |
| server token not configured | server 已启动但 effective token 为空；检查 local/global/env 三个来源 |
| invalid token | server 已有 token；检查 client 实际使用的 `RDR_TOKEN`（否则文件第一个）是否在 server effective token 集合里 |
| `terminal is already attached` | 同一个 stateful terminal 当前被另一 connection attach；先结束/断开原 attachment |
| `unknown terminal` | terminal 已退出、被 close、token revoke/server shutdown 清理，或 RDR server 已重启 |
| reconnect 后提示 replay truncated | detached 期间输出超过 4 MiB；state 仍在，但最旧输出已被丢弃 |
| `get` 反复从 0 开始 | part 与远端 prefix 不一致，或 server 不支持安全 range；删除 `.rdr-part` 可强制完整下载 |
| `get` checksum / size mismatch | 不会提交目标文件；保留 Evidence 后重试，必要时删除 `.rdr-part` 做完整下载 |
| `put` checksum / size mismatch | server 不会提交临时文件；重新执行 `rdr put` |
| 能连上但看不到业务进程 | runtime visibility 问题：PID namespace / cgroup / mount，见 `DEPLOYMENT.md` §12 |
| server 与主服务一起被 OOM | 部署 failure domain 未隔离，先修部署而不是增加 RDR API |
