# RDR 部署与使用手册

本文描述 RDR（Remote Diagnostic Runtime）的当前部署和使用方式。RDR 远端不运行 AI；Claude Code、Codex 或工程师在开发环境做分析，RDR 只提供接近本地 Terminal 的远端运行环境。

当前版本以 `rdr-server` + `rdr` CLI 为基线。MCP adapter 尚未实现。

## 1. 部署目标

推荐部署形态：

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
     +-- shell / PTY / file
     +-- logs / proc / cgroup
     +-- perf / gdb / core
     +-- localhost metrics when network namespace is shared
```

RDR 可以和主服务一起构建、发布和升级，但必须是独立进程。主服务 crash、deadlock、SIGKILL 或 HTTP 不可用时，RDR 应继续工作。

如果 OOM 是主要诊断场景，不要让 RDR 和主服务共享一个会整体被 OOM kill 的 failure domain。实际部署需要验证主服务内存失控后 RDR 是否仍然存活。

## 2. 运行要求

RDR Server 和开发侧 Client 都需要 Python 3.10+。

推荐 Server 使用独立 venv：

```bash
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/python -m pip install /path/to/skill/rdr
```

安装后：

```text
/opt/rdr/venv/bin/rdr-server
/opt/rdr/venv/bin/rdr
```

核心 runtime 无第三方依赖。

RDR 自己不会安装 `perf`、`gdb`、`pidstat` 等诊断工具。需要使用什么工具，目标运行环境就必须已经具备什么工具。

为了达到 Local Parity，RDR 进程必须拥有实际诊断所需的 runtime visibility：

- 目标服务 PID / thread 可见
- `/proc` 可见
- cgroup 可见
- 日志目录可见
- core dump、binary 和 symbols 可见
- `perf` / ptrace / kernel log 所需权限
- 查询 `localhost` metrics 时，与目标服务处于可访问的 network namespace

MVP 内部环境可以先给 RDR 与人工登录调试相同的权限，再根据真实使用收紧。

## 3. 网络

RDR 默认监听：

```text
0.0.0.0:19090
```

开发环境必须能访问这个 TCP 端口。SSH 可以保持关闭。

当前 RDR Protocol 不自带 TLS。第一版只应运行在已有可信内部网络边界内，不要直接暴露到公网或不可信网络。

端口可以修改：

```bash
/opt/rdr/venv/bin/rdr-server --host 0.0.0.0 --port 19090
```

## 4. Access Config

RDR 使用同一个 access-config schema 表达一件事：

- 哪些 token 可以访问

Schema：

```json
{
  "tokens": [
    "token-a",
    "token-b"
  ]
}
```

关闭 RDR 用 `rdr server stop`；临时拒绝所有认证用空的 `tokens: []`。历史文件里可能还有 `"enabled"` 键，读取时会被忽略，不再有任何效果。

仓库模板：

```text
rdr/config/access.example.json
```

真实 token 不进入 repo。

### 4.1 单机配置

默认路径：

```text
/etc/rdr/access.json
```

示例：

```json
{
  "tokens": [
    "host-token"
  ]
}
```

建议：

```bash
chmod 600 /etc/rdr/access.json
```

单机关闭 RDR：

```bash
rdr server stop
```

临时拒绝所有认证（进程保留，listener 保留）：

```json
{
  "tokens": []
}
```

### 4.2 全域配置

默认路径：

```text
/data/bucket/rdr/access.json
```

这是共享 bucket 已经挂载到本机文件系统后的普通文件。RDR 不访问 S3 API，也没有 S3 access key / secret key / boto3 依赖。

示例：

```json
{
  "tokens": [
    "global-token"
  ]
}
```

全域关闭：把共享文件的 `tokens` 置空，所有读取它的 RDR 实例会断开 active sessions 并拒绝认证（进程仍存活，彻底关闭需逐机 `rdr server stop`）。

### 4.3 单机 + 全域组合语义

两份配置使用同一 schema。

```text
effective tokens
= local.tokens UNION global.tokens UNION static env token
```

因此：

- 全域 token 可以访问所有读取该全域文件的机器。
- 单机 token 可以补充某台机器独有的访问能力。
- 单机文件启动时可以不存在；此时 server 仍可启动和监听，只是没有 local policy/token。
- 单机文件如果存在但配置非法，RDR 启动失败，不静默忽略。
- 全域文件启动时可以不存在。
- 如果全域文件存在但配置非法，RDR 启动失败，不静默绕过全域配置。
- 单机或全域文件一旦成功读取过，后续文件/mount/读取临时失败时保持对应 last-known policy。
- effective token 为空不等于无认证：listener 可以存在，但所有认证都失败，并明确返回 `server token not configured`。

默认每 30 秒检查一次：

```bash
--access-poll-seconds 30
```

需要更快生效可以缩短，但它不是实时配置协议。

## 5. 启动 RDR Server

推荐命令：

```bash
/opt/rdr/venv/bin/rdr-server \
  --host 0.0.0.0 \
  --port 19090 \
  --access-config /etc/rdr/access.json \
  --global-access-config /data/bucket/rdr/access.json \
  --access-poll-seconds 30 \
  -v
```

两个配置路径已有默认值，因此也可以：

```bash
/opt/rdr/venv/bin/rdr-server --host 0.0.0.0 --port 19090 -v
```

也可以通过环境变量覆盖路径：

```bash
export RDR_ACCESS_CONFIG=/etc/rdr/access.json
export RDR_GLOBAL_ACCESS_CONFIG=/data/bucket/rdr/access.json
/opt/rdr/venv/bin/rdr-server --port 19090
```

没有 access.json 时，可以用 `RDR_TOKEN` 直接提供 token（见 4.4）：

```bash
RDR_TOKEN=<token> /opt/rdr/venv/bin/rdr-server --port 19090
```

也可以完全不提供 token：server 进程和 listener 正常启动，但认证不可用，直到 watcher 读取到有效 token 或进程带 token 重启：

```bash
/opt/rdr/venv/bin/rdr-server --port 19090
# client auth -> server token not configured
```

已有配置文件如果非法仍然是启动错误；“允许无 token 启动”只针对配置文件不存在或有效配置的 effective token 为空，不会绕过非法配置。

### 5.1 使用 supervisor 常驻

RDR 自己不 daemonize。生产/线下长期运行应交给现有 supervisor、容器 runtime 或 systemd。

关键要求只有三个：

1. RDR 与主服务是独立进程。
2. RDR 异常退出后由 supervisor 重启。
3. 主服务退出或重启时，不要顺带杀掉 RDR。

如果使用 systemd，可以参考：

```ini
[Unit]
Description=RDR Remote Diagnostic Runtime
After=network.target

[Service]
Type=simple
ExecStart=/opt/rdr/venv/bin/rdr-server \
  --host 0.0.0.0 \
  --port 19090 \
  --access-config /etc/rdr/access.json \
  --global-access-config /data/bucket/rdr/access.json \
  --access-poll-seconds 30
Restart=always
RestartSec=2

[Install]
WantedBy=multi-user.target
```

实际用户、权限、cgroup 和 namespace 按目标服务环境配置。不要为了形式上的隔离导致 RDR 看不到真实 PID、cgroup、日志或 core。

### 5.2 托管启动（无 supervisor 的环境）

`rdr server start` 提供托管后台启动：detached 进程、pid file、日志文件、listener 就绪自检。安装与启动因此分离 —— pip 装完后，启动/状态/停止都是独立命令：

```bash
rdr server start    # token 可选；优先级 --token > RDR_TOKEN > access config
rdr server status   # 进程 / listener / auth；只有 auth=ok 时 exit 0
rdr server stop
```

没有 token 时 `start` 仍成功，`status` 会报告：

```text
process: ... alive
listener 127.0.0.1:19090: open
auth: server token not configured
```

并返回 non-zero。这样区分“server 已经启动”与“server 已可认证使用”。

默认 pid file `/run/rdr/server.pid`（不可写时回退 `~/.rdr/`），日志 `/var/log/rdr/server.log`（同样回退），可用 `--pid-file` / `--log-file` 覆盖。`rdr-server` 前台进程语义不变；生产长期运行仍建议 supervisor / systemd，托管启动适合无 init 体系的容器或临时环境。

## 6. 开发侧 Client

开发环境安装同一个 package：

```bash
python3 -m venv ~/.local/share/rdr/venv
~/.local/share/rdr/venv/bin/python -m pip install /path/to/skill/rdr
```

可以把下面路径加入 `PATH`：

```text
~/.local/share/rdr/venv/bin
```

客户端默认读取：

```text
~/.config/rdr/access.json
```

例如：

```json
{
  "tokens": [
    "global-token"
  ]
}
```

建议：

```bash
chmod 600 ~/.config/rdr/access.json
```

也可以通过环境变量覆盖：

```bash
export RDR_ACCESS_CONFIG=/path/to/access.json
```

或者在某一次命令上覆盖：

```bash
rdr connect HOST:19090 --access-config /path/to/access.json
```

客户端使用 token list 中的第一个 token 发起认证。设置了 `RDR_TOKEN` 时优先使用它，可以完全不需要 access.json：

```bash
RDR_TOKEN=<token> rdr identity HOST:19090
```

认证失败有三种明确语义：

- client 本地没有可用 token：CLI 在连接前直接报告本地 token/config 错误。
- server effective token 为空：握手返回 `server token not configured`。
- server 已有 token，但 client token 不匹配：握手返回 `invalid token`。

### 6.1 CLI 形态

主入口接近 SSH：

```bash
rdr connect HOST:PORT
```

其他命令：

```bash
rdr exec HOST:PORT 'command'
rdr identity HOST:PORT
rdr get HOST:PORT:/remote/path LOCAL_PATH
rdr put LOCAL_PATH HOST:PORT:/remote/path
```

IPv6 用 bracket 形式：

```bash
rdr connect '[::1]:19090'
rdr get '[::1]:19090:/tmp/file' ./file
```

## 7. 认证与长会话

RDR 的认证单位是 **transport connection**，不是每条命令。

```text
TCP connect
    ↓
auth(token)       # 一次
    ↓
ready
    ↓
exec / PTY / file / ...
```

如果 server 尚未配置 token，`auth(token)` 会得到 `server token not configured`；如果 server 已配置 token 但值不匹配，则得到 `invalid token`。两者不会合并成同一个错误。

因此一个稳定的长 `connect` 会话只认证一次：

```bash
rdr connect HOST:19090
```

只要这个 TCP connection 不断，PTY 中运行 `top`、`gdb`、`perf`、shell command 都不会重复认证。

如果连接断开并重建，新 connection 必须重新认证一次。CLI 会再次读取本地 access config，不需要人工重新输入 token。

当前版本还没有 session reconnect，所以：

```text
TCP connection 断开
→ PTY/GDB 现场不保证继续存在
```

后续即使实现 session reconnect，也必须先认证新的 transport connection，再 attach 原 session。

`rdr exec`、`identity`、`get`、`put` 都是独立 CLI invocation，因此每个 invocation 建立一次 connection、认证一次、完成后关闭。

## 8. 启动后 Smoke Test

### 8.1 Identity

```bash
rdr identity HOST:19090
```

### 8.2 One-shot exec

```bash
rdr exec HOST:19090 'uname -a; id; pwd; ps -ef | head'
```

### 8.3 Interactive PTY

```bash
rdr connect HOST:19090
```

进入以后至少验证：

```bash
tty
ps -ef
top
python3
```

如果目标环境有 `gdb` / `perf`，继续验证：

```bash
gdb --version
perf --version
```

### 8.4 File transfer

```bash
rdr get HOST:19090:/etc/hostname ./remote-hostname
```

上传临时诊断脚本：

```bash
rdr put ./inspect.py HOST:19090:/tmp/inspect.py
```

## 9. 日常使用

### 9.1 大日志

不要下载整份日志。让命令靠近数据，只把 Evidence 返回开发环境。

```bash
rdr exec HOST:19090 "rg 'ERROR|timeout' /path/server.log | tail -200"
```

找到 request / line 后再取上下文：

```bash
rdr exec HOST:19090 "sed -n '182900,183050p' /path/server.log"
```

### 9.2 Metrics

如果 metrics 在目标运行环境 localhost：

```bash
rdr exec HOST:19090 "curl -s localhost:8080/metrics | grep request_latency"
```

如果这里访问不到而主服务本身可以访问，优先检查 RDR 与主服务是否处于不同 network namespace。

### 9.3 Perf

先做低成本观察：

```bash
rdr exec HOST:19090 "pidstat -tid -p PID 1 5"
```

然后：

```bash
rdr exec HOST:19090 "perf stat -p PID -- sleep 10"
```

采样数据尽量留在远端：

```bash
rdr exec HOST:19090 \
  "perf record -F 99 -g -p PID -o /tmp/rdr-perf.data -- sleep 20"

rdr exec HOST:19090 \
  "perf report -i /tmp/rdr-perf.data --stdio --percent-limit 0.5"
```

只有本地确实需要 `perf.data` 时再下载：

```bash
rdr get HOST:19090:/tmp/rdr-perf.data ./rdr-perf.data
```

### 9.4 Core Dump / GDB

Core 很大时优先留在远端。

打开长期交互连接：

```bash
rdr connect HOST:19090
```

然后直接使用正常 GDB 工作流：

```bash
gdb /path/server /path/core
```

例如：

```text
(gdb) info threads
(gdb) thread 17
(gdb) bt
(gdb) frame 8
(gdb) info locals
(gdb) p variable
```

Claude Code / Codex 可以同时读取开发机 repo 源码，再根据远端 GDB Evidence 继续交互。

当前版本尚未实现 session reconnect。RDR connection 中断时，交互 GDB session 不保证保留；长时间 core 分析需要注意这一限制。

### 9.5 OOM / cgroup

主服务异常后，RDR 应仍然可连接。

```bash
rdr connect HOST:19090
```

常见调查：

```bash
cat /sys/fs/cgroup/.../memory.events
cat /sys/fs/cgroup/.../memory.stat
cat /proc/PID/status
cat /proc/PID/smaps_rollup
journalctl -k
dmesg | tail -200
```

如果主服务 OOM 后 RDR 也消失，优先修部署 failure domain，而不是增加 RDR API。

## 10. Access 运维

### 10.1 全域新增 token

先保留旧 token，同时加入新 token：

```json
{
  "tokens": [
    "old-token",
    "new-token"
  ]
}
```

等待一个 poll 周期后，将开发侧 `~/.config/rdr/access.json` 的第一个 token 切换为新 token。

验证：

```bash
rdr identity HOST:19090
```

最后从 server access config 删除旧 token。

删除 token 会关闭当前 active sessions，客户端需要重新连接并认证。这是有意行为，避免被撤销的 credential 保持长期 session。

### 10.2 单机临时 token

只修改：

```text
/etc/rdr/access.json
```

加入一个仅该机器认可的 token，不修改全域文件。

### 10.3 单机关闭

```bash
rdr server stop
```

只临时拒绝认证（保留进程与 listener）时，把 `/etc/rdr/access.json` 的 `tokens` 置空即可，一个 poll 周期内 active sessions 会结束。

### 10.4 全域关闭

向共享文件写入：

```json
{
  "tokens": []
}
```

路径：

```text
/data/bucket/rdr/access.json
```

所有读取到这份配置的 RDR 实例会断开 active sessions 并拒绝认证。彻底关闭进程需逐机执行 `rdr server stop`。

### 10.5 恢复

将对应 scope 恢复为：

```json
{
  "tokens": [
    "valid-token"
  ]
}
```

一个 poll 周期内恢复认证；client 重建连接即可。

### 4.4 环境变量 token

`RDR_TOKEN` 是第三种 token 来源，适合 pip 安装后的直接启动：

```bash
pip install rdr-runtime
RDR_TOKEN=<token> rdr-server --port 19090
```

语义：

- server：`RDR_TOKEN` 作为额外 token 加入并集；local config 不存在也不阻止启动。
- server：local/global/static token 全部为空时仍启动 listener，但认证返回 `server token not configured`。
- client：`RDR_TOKEN` 优先于 access config 的第一个 token，适合临时验证：

  ```bash
  RDR_TOKEN=<token> rdr exec HOST:19090 'uname -a'
  ```

- `RDR_TOKEN` 与文件 token 一样只影响"谁能认证"；关闭 RDR 用 `rdr server stop`，临时拒绝所有认证把文件 `tokens` 置空。
- local config 文件存在但非法时，即使设置了 `RDR_TOKEN`，启动仍然失败；“文件不存在”与“文件非法”是两种不同状态。
- token 轮换（10.1）仍以文件为准；env token 不参与 poll 热更新，改动需重启进程。

## 11. 配置失败语义

| 场景 | 行为 |
|---|---|
| local config 启动时不存在，且无其他 token | RDR 启动并监听；认证返回 `server token not configured`；managed `status` non-zero |
| local config 启动时不存在，但设置了 `RDR_TOKEN` | 以 `RDR_TOKEN` 启动 |
| local config 启动时存在但非法（即使设置了 `RDR_TOKEN`） | RDR 启动失败 |
| global config 启动时不存在 | 按当前 local/static policy 启动；没有 token 也允许启动 |
| global config 启动时存在但非法 | RDR 启动失败 |
| local config 从未成功读过且不存在，后续创建有效文件 | watcher 读取并应用新 local policy/token |
| local config 已成功读过，随后暂时不可读/非法 | 保持 last-known local policy |
| global config 从未成功读过且不存在 | 继续使用当前 local/static policy |
| global config 已成功读过，随后 bucket/mount 暂时不可读 | 保持 last-known global policy |
| access policy apply 临时失败 | 保持旧 effective policy，下一个 poll 继续重试 |
| access watcher 非预期退出 | RDR Server 退出，由 supervisor 重启 |

这个语义同时保证两点：部署可以先启动 RDR 再配置 credential；配置文件一旦存在或曾生效，非法/临时失败不会被静默当成“开放访问”。effective token 为空始终意味着“认证不可用”，不是“无需认证”。

## 12. 常见问题

### `rdr: cannot read config ~/.config/rdr/access.json`

这是 client 本地没有可用 token/config。客户端默认读取：

```text
~/.config/rdr/access.json
```

创建这个文件，或者通过：

```bash
export RDR_ACCESS_CONFIG=/path/to/access.json
```

覆盖。

### Connection refused

依次检查：

1. `rdr-server` process 是否存在（`rdr server status`）。
2. RDR 是否在 `19090` listen。
4. 开发环境到目标端口的网络是否允许。
5. access watcher 是否异常退出并被 supervisor 重启。

### server token not configured

Server 已启动并监听，但当前 effective token 集为空。配置 `/etc/rdr/access.json`（watcher 会自动发现），或者带 `RDR_TOKEN` / `--token` 重启 server。

### invalid token

Server 已经配置至少一个 token，但当前 client token 不在：

```text
local.tokens UNION global.tokens UNION static env token
```

这与 `server token not configured` 是不同错误。

### 能执行 shell，但看不到主服务 PID / cgroup / core

这是 runtime visibility 问题，不是 RDR Protocol 问题。检查 PID namespace、mount、cgroup 和文件系统可见性。

### `perf` / `gdb` Permission denied

检查 RDR process 的 uid、capability、ptrace/perf policy。RDR 不会绕过操作系统权限。

### `curl localhost:<metrics-port>` 失败

检查 RDR 和主服务是否处于同一 network namespace，或者改用主服务实际可达地址。

### 主服务 OOM 后 RDR 也被杀

说明两者 failure domain 没有隔离。优先调整 process/cgroup/container 部署，使 RDR 保留最小独立生存空间。

## 13. 文件传输层保证

传输是核心基础组件，以下保证内建在协议里：

- **双向**：`get`（server → client）与 `put`（client → server）
- **完整性**：双向流式计算 md5，`file.done` / `file.put.done` 携带 checksum，接收端**校验通过才原子落盘**（临时文件 + fsync + rename）；不一致即报错并丢弃临时文件
- **长度核对**：`put.start` 声明 size，server 校验写入字节数；download 校验收到的总长与 server 报告的 file size 一致
- **分片与续传**：`file.get` 支持 `offset`（range 原语）；client 下载自动断点续传 —— 中断后重试从已有的 `. <name>.rdr-part` 续传，每个分片独立 md5 校验；陈旧/超长的 part 文件自动重新开始
- **错误清理**：连接断开、取消、校验失败都会清理临时文件，目标路径要么是完整旧文件、要么是完整新文件，不会出现半截文件

已知取舍：续传的分片校验不重算整个文件的 md5（避免服务端全文件重读）；需要整文件强校验时删除 part 文件重新完整下载。

## 14. 当前已知限制

当前基线尚未实现：

- MCP adapter
- connection 断开后的 session reconnect
- server-side 大输出 spool / cursor
- fleet management / central gateway
- perf/log/core/OOM 专用 API（这是明确的 non-goal，除非真实使用 Evidence 证明需要）

第一阶段验收标准仍然是 Local Parity：与真正登录服务器相比，开发环境的调查能力不应有明显损失。
