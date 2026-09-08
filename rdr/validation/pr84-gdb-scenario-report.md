# PR84 GDB 场景验证报告（stateful terminal）

- 验证对象：PR #84 `rdr/stateful-terminal`，commit `978a4cc`，版本 0.6.0
- 验证日期：2026-09-08
- 验证环境：本机隔离实例（`/tmp/pr84-venv`，127.0.0.1:19091）；gdb 目标为一次性测试进程（`gcc -g` 编译的循环程序）；**生产实例（19090）与生产进程未参与**

## 0. 构建门禁

```text
bash rdr/build.sh
60+13 → 70 passed, 6 subtests passed
托管 E2E：有 token 实例 auth: ok；无 token 实例 auth: server token not configured（non-zero）
产物：rdr_runtime-0.6.0-py3-none-any.whl
```

## 1. 场景设定

DEPLOYMENT.md 原已知限制："connection 断开后的 session reconnect 未实现；PTY/GDB 现场不保证继续存在"。本验证检验 PR84 的核心不变量：

> terminal/进程生命周期属于 RDR runtime；TCP 连接只是 attach。

目标进程：`gcc -g -O0` 编译的 `while(1){work(1);sleep(2);}` 循环程序（有符号、有可观测状态），gdb 从 PTY 内 attach 它。

## 2. 逐步结果

| # | 步骤 | 结果 |
|---|---|---|
| 1 | PTY 内 `gdb -q -p <pid>` attach | ✓ 到达 `(gdb)` 提示符，目标进入 tracing stop（`/proc/<pid>/stat` = `t`） |
| 2 | `bt 5` 执行 | ✓ 输出含 `#0` 栈帧 |
| 3 | **传输层粗暴断连**（`client.close()`：不发协议告别、不发 terminal.close） | ✓ gdb 进程与被停住的目标**全部存活**（runtime 持有 terminal，会话未死） |
| 4 | 新连接 `attach_terminal(<同一 terminal_id>)` | ✓ `replayed_bytes=286`，**断连期间产出的 bt 输出被 replay 回放** |
| 5 | 同一 gdb 会话内继续 `info threads` | ✓ 交互延续（非新会话） |
| 6 | `detach` | ✓ 目标进程状态回到 `S`，恢复运行 |
| 7 | `quit` | ✓ 终端生命周期闭环：事后 attach 同 id 报 `unknown terminal` |

## 3. 边界确认（来自分支测试套件 test_stateful_terminal.py）

- 显式 `terminal.close`、token 撤销、远程进程退出、RDR server 关闭 → 仍然正确清理 terminal
- 默认并发 attach 上限 2（`RDR_TERMINAL_MAX_ATTACHMENTS` / `--terminal-max-attachments`），第 3 个被拒
- replay buffer 上限 4 MiB，仅在零 attach 时保留

## 4. 结论

- **PR84 支持 GDB/core 场景的目标**：分析会话跨传输断连存活、结果经 replay 不丢失、同一会话可继续交互、生命周期与访问边界不放宽。
- 原"session reconnect 未实现"限制被精确移除；未引入 SessionManager / GDB 专用 API / 持久化，复杂度收敛。
- 附带确认：分支在既有续传实现上增加了 `prefix_checksum`（part 文件前缀校验，防远端文件变更后误续传），配套 `test_resume_integrity.py`。

## 5. 复现要点

```bash
# 1) 构建并部署隔离实例
bash rdr/build.sh
python3 -m venv /tmp/pr84-venv
/tmp/pr84-venv/bin/pip install rdr/dist/rdr_runtime-0.6.0-py3-none-any.whl
RDR_TOKEN=<token> /tmp/pr84-venv/bin/rdr-server --host 127.0.0.1 --port 19091 &

# 2) 目标进程（无副作用，可随时 kill）
gcc -g -O0 -o /tmp/gdb_target /tmp/gdb_target.c && /tmp/gdb_target &

# 3) 场景：client1 open_terminal → gdb -p <pid> → bt → 传输断开 →
#    client2 attach_terminal(同 id) → 确认 replay 与 bt 输出 → detach → quit
```

注意：gdb attach 必然 ptrace-stop 目标进程（tracing stop），"无损 attach"不存在；本验证全部使用一次性测试进程，生产进程的 gdb 分析需单独约定冻结窗口。
