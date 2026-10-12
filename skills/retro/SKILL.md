---
name: retro
description: "Human-invoked retrospective on real agent work. Read the session transcript (current by default, or named Claude Code / Codex transcripts) and the project feedback log, find the moments where the agent was corrected or struggled, check what was already in effect, and propose traced fixes routed to the target repo or to this Skill system. Nothing is applied until the Human picks."
disable-model-invocation: true
---

# Retro · 复盘真实工作

Retro 回答一个独立问题：**这段真实工作里，agent 在哪些具体时刻被纠正或吃了亏，下次靠改什么让它不再发生。**

它只在 Human 调用时运行。它改环境，不改这次工作的产物：不修本次的 bug，不做 code review，不证明 behavior uplift。

## 读什么

- **Session**：默认当前 session；Human 指定时读具名的 Claude Code / Codex transcript。用 `python3 scripts/session_turns.py --current` 或 `python3 scripts/session_turns.py <transcript>...` 列出每个 Human turn、它之前的 assistant 结论，以及之后到下一个 Human turn 之间的 tool 调用、失败与中断；再按行号回读需要的原文。复盘覆盖全部 Human turn，被截断的长 turn（粘贴的 review、日志）读全文，输出开头写明读过的行范围。只读被复盘的工作，不跨 workspace 或其他 session 搜索。
- **项目 feedback log**（项目已有 work-notes 位置，否则 `.agents/feedback-log.md`）：存在就读，未收录的条目一并处理。
- **项目 contract**：当时生效的 AGENTS.md / CLAUDE.md、已加载的 Skill、项目文档与 check 命令（lint / test / hook / CI）。Human 要求时再读 commit / revert / review 历史。

## 找时刻

候选只来自 record 中的具体时刻：Human 纠正、同一纠正重复出现、被推翻或自己撤回的结论、review finding、Human 中断、Human 代做 agent 有权限做的事、长时间搜索或反复失败的 tool 路径、缺少关键信息访问。

每个候选必须给出 transcript 行号（或 log / commit 指针）和原话；指不到具体时刻就丢弃。Human 提出新需求、改变主意或表达偏好不是纠正。不为凑类别编造通用建议；没有值得改的就直说。

## 归因与分流

先确认**当时生效**的规则：项目 contract、当时加载的 Skill。

- **`pending`**：当时生效的规则已覆盖但没被执行。引用该条款，不提议同义规则；提议的是结构化手段（check、harness、tool）或测量为什么没被执行。规则只存在于当时未加载的 Skill 或文件中时不是 `pending`，写明覆盖在哪，由 Eval 判断装上后是否有效。
- **`target-repo`**：项目缺 check、pointer、文档、权限或信息访问。给出能成立的最强修复：结构（唯一 owner、删掉旧路径）> 类型 > check / lint / hook / CI > test > 导航 pointer > prose。已有但没接上或已坏的 check，修复就是接上它。AGENTS.md / CLAUDE.md 只放 pointer，不堆规则。新 check 必须能在这次真实错误上失败。
- **`skill`**：本 Skill system 的指引缺失或误导，换个 repo 也会犯。写抽象 shape 与 source pointer，不带私有上下文。单条是 hypothesis；runtime 改动只能来自 Eval 证明的稳定 gap，retro 不给 disposition。
- **`none`**：一次性失误、偏好、agent 控制之外。

## 输出

按严重度排序（后果与复发可能，不看语气轻重）。每条：时刻（指针 + 原话）、发生了什么、原因、归因 / 落点、提议的改动、怎么确认改动有效。最后请 Human 逐条选择。

## 落地

只做 Human 选中的条目，不 commit / push，除非另有授权：

- `target-repo`：在项目内按正常改动实施。
- `skill` / `pending`：workspace 中有本 Skill system 的 `evals/feedback/LEDGER.md` 时追加一行（disposition `open`）；否则追加到项目 feedback log，写明当时结论、纠正及来源、决定性 Evidence pointer、原因与落点，等待 intake。

## 边界

- Eval 只度量：retro 不声称 behavior 变好，ledger 行的 disposition 与关闭仍属于 repo 维护流程。
- Bearing 可以把 retro 输出或 ledger 当作 feedback 信号判断改进方向；retro 不排定投资。
- Northstar 的 Taskbook 与 worker return 流程不变；retro 读 feedback log，不写 Taskbook。
