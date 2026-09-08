# RDR 快速上手 Guide

最短可执行路径：装 server → 启动 → 配 token → 装 client → 验证。
Access 组合语义、轮换流程、故障语义、supervisor 常驻的**权威版本**在 [`DEPLOYMENT.md`](DEPLOYMENT.md)，本文不复制，有冲突以它为准。

## 0. 前置

- 两侧都要 Python 3.10+
- 开发环境能访问 server 的 TCP 端口（默认 `19090`），SSH 可以不开
- `perf` / `gdb` / `pidstat` 等诊断工具 RDR 不负责安装，目标机缺什么先装什么

## 1. 构建 package（任一台有 repo 的机器）

```bash
bash rdr/build.sh          # 产出 rdr/dist/*.whl + *.tar.gz，自动跑测试 + wheel 验证
```

不想构建时也可以直接从 repo 目录安装：`pip install ./rdr`。

## 2. 安装并启动 Server（远端主机）

安装（单 package，同时提供 `rdr-server` 与 client 入口 `rdr`）：

```bash
python3 -m venv /opt/rdr/venv
/opt/rdr/venv/bin/python -m pip install rdr_runtime-*.whl
export PATH="/opt/rdr/venv/bin:$PATH"

# 需要新 token 时
python3 -c "import secrets; print(secrets.token_urlsafe(24))"
```

### 配置 token（可选；优先级：`--token` > `RDR_TOKEN` > 文件）

Server 可以先在没有 token 的状态启动；listener 正常存在，但任何认证都会返回 `server token not configured`，`rdr server status` 也会以 non-zero 报告这一状态。需要建立可用连接时，再通过以下任一方式配置 token：

1. `RDR_TOKEN` 环境变量 —— 固定变量，启动进程时读取
2. `rdr server start --token <token>` —— 启动时一次性指定
3. `/etc/rdr/access.json` 文件 —— 生产推荐，支持 30s 热更新与轮换；server 已启动时创建该文件也会被 watcher 发现：

   ```bash
   mkdir -p /etc/rdr && cat > /etc/rdr/access.json <<'EOF'
   {
     "tokens": ["<token>"]
   }
   EOF
   chmod 600 /etc/rdr/access.json
   ```

### 启动

**托管方式**（推荐；安装与启动分离，自带状态与停止）：

```bash
rdr server start          # token 可选；无 token 也启动并监听
rdr server status         # 进程 / 监听 / 认证状态；只有认证可用时 exit 0
rdr server stop           # 优雅终止
```

**前台方式**（交给 supervisor / systemd 托管时用）：

```bash
rdr-server --host 0.0.0.0 --port 19090
```

### 判断 server 启动成功

- 托管方式：`rdr server start` 就绪后打印 `rdr server ready: pid=... listen=...`
- `rdr server status` 会分别报告 process / listener / auth；无 server token 时显示 `auth: server token not configured` 并返回 non-zero
- 前台方式：stdout 出现一行 `RDR server ready on ...`
- 从开发环境最终确认：`rdr identity HOST:19090` 有响应

token 语义细节（热更新、轮换、global config 组合）以 DEPLOYMENT.md §4/§10/§11 为准：env token 不参与热更新；文件存在但非法时启动失败；关闭 RDR 用 `rdr server stop`，临时拒绝所有认证把 `tokens` 置空。

## 3. 安装 Client（开发环境）

```bash
python3 -m venv ~/.local/share/rdr/venv
~/.local/share/rdr/venv/bin/pip install rdr_runtime-*.whl
export PATH="$HOME/.local/share/rdr/venv/bin:$PATH"    # 放进 ~/.bashrc
```

client 认证 —— 二选一：

- `export RDR_TOKEN=<token>`（优先级高于文件，免配置）
- `~/.config/rdr/access.json`（与 server 同 schema，使用其中第一个 token）

> **server 与 client 用两个独立 venv。** server 是远端诊断的生命线；client 可随时重装、升级，不应与 server 共享运行时。

## 4. 验证

```bash
rdr identity HOST:19090                        # 返回 hostname/pid/uid 即认证 + 通道通
rdr exec HOST:19090 'uname -a; uptime'         # one-shot 命令
rdr get HOST:19090:/etc/hostname ./hostname    # 下载
rdr put ./inspect.py HOST:19090:/tmp/inspect.py # 上传
rdr connect HOST:19090                          # 交互 PTY（top / gdb / python3）
```

认证失败明确区分：client 自己没有可用 token 时在本地直接报配置错误；server 尚未配置任何 token 时返回 `server token not configured`；server 已配置 token 但 client token 不匹配时返回 `invalid token`。

## 5. 日常使用姿势

```bash
rdr exec HOST:19090 "rg 'ERROR|timeout' /path/server.log | tail -200"   # 命令靠近数据
rdr exec HOST:19090 "pidstat -tid -p PID 1 5"                            # 先低成本观察
rdr exec HOST:19090 "perf record -F 99 -g -p PID -o /tmp/perf.data -- sleep 20"
rdr exec HOST:19090 "perf report -i /tmp/perf.data --stdio --percent-limit 0.5"
```

大日志、core、OOM / cgroup 的完整工作流见 DEPLOYMENT.md §9。原则：采样和 core 留在远端，只把 Evidence 拉回开发环境。

## 6. 故障速查

| 现象 | 先查 |
|---|---|
| connection refused | server 进程在吗（`rdr server status`）→ 端口在听吗（`ss -tlnp \| grep 19090`）→ 网络可达吗 |
| server token not configured | server 已启动，但还没有任何有效 token；配置 `/etc/rdr/access.json` 或带 token 重启 |
| invalid token | server 已有 token；检查 client 实际使用的 `RDR_TOKEN`（否则文件第一个）是否在 server 的有效集合里 |
| 能连上但看不到业务进程 | runtime visibility 问题：PID namespace / cgroup / mount，与 RDR 协议无关（DEPLOYMENT.md §12） |
| server 与主服务一起被 OOM | 部署 failure domain 未隔离，先修部署而不是加 API |
