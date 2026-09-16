---
name: eval
description: "Use when building, auditing, or evolving reproducible behavioral evaluations for agents, prompts, skills, tools, or harness changes. Turn a material behavior into a discriminative Task + representative Environment + hard-to-game Verifier, run it with an available backend, inspect trajectories, and iterate until the measurement is trustworthy."
---

# Eval · Agent behavior evaluation engineering

Eval 负责一个独立问题：**Agent / Skill / prompt / tool / harness 的行为是否真的具备或改善了某个能力，以及怎样把它变成可信、可重复的 measurement。**

它不验证产品/工程 claim，不拥有 Intent、Architecture 或 implementation，也不绑定某个 eval framework。`$verify` 负责 engineering claim → proof；`$eval` 负责 agent behavior → reproducible measurement。

## 什么时候调用

当 Skill / prompt / routing / tool / harness 改动需要 behavioral Evidence，真实 trace 暴露稳定 agent failure，已有 eval 无判别力 / 易 reward-hack，或需要把 scenario smoke 升级成 executable behavioral eval 时调用 `$eval`。

产品功能、迁移等价、性能、structural completion 等 engineering claim 仍交 `$verify`。

## 从真实行为出发

先恢复会决定目标行为的真实 agent surface：instructions、model config、tools / permissions / side effects、Skills / harness、repo / data / services、existing evals，以及可用 trace 中的 messages、tool calls、results / errors、state changes 与 artifacts。

Trace 是 observed Evidence，不是 golden truth。没有 trace 时可以从 repo contract + real task shape 构建第一版，但不要虚构 production pattern 或 frequency。

目标 capability / failure 必须 material、可区分、可重复观察。只有“什么能力值得长期测”或 tradeoff 真正属于 Human commitment 时才 Ask Human；repo / tool / runtime 事实自己调查。

## 稳定 Eval 模型

一个 executable behavioral eval 至少包含：

1. **Task** — candidate 收到的 organic instruction / interaction；
2. **Environment** — 决定行为的 repo、tools、data、permissions、state 与 relevant failure modes；
3. **Verifier** — 根据 independent observable Evidence 判断 behavior / outcome；
4. **Run Evidence / Trajectory** — messages、tool calls / actions、state changes、artifacts、verifier Evidence / judgment 与 run identity。

Harbor、clean-session runner、trajectory recorder、containerized task runner 或 project-local evaluator 都只是 backend，不属于 Eval semantic identity。

## 设计约束

- Task 不泄漏 expected Skill / tool / route、rubric、golden 或 variant identity；一个 case 优先暴露少量 decisive discriminator。
- multi-turn behavior 必须保留同一 agent context；不要把连续 Human clarification 拆成互不相关的 clean sessions。
- Environment 只复现会改变目标 behavior 的现实；高成本或 production-write dependency 可以 simulate，但必须保留相关 contract 与 observable consequence。
- 比较 base / candidate 时，除被测配置外尽量固定 Task、Environment、tool semantics 与 run policy；环境 identity 不可信时结果是 `inconclusive`。
- Verifier 优先使用 deterministic state / artifact / side-effect、实际 tool calls / arguments / results，再使用 independent semantic judge；candidate self-report 不能证明动作发生。
- 主动检查 proxy completion、golden leakage、string/parser shortcut、claimed-but-unperformed action 和 verifier 看不到的 side effect 等 reward-hack path。

## 运行与迭代

运行后同时检查 agent trajectory 与 verifier Evidence / trajectory；不能只看 final reward 或 agent 自我解释。

失败先判断来自 **candidate behavior** 还是 **Task / Environment / Verifier**。measurement 有问题时先修 eval 并重跑；measurement 可信且暴露稳定 behavior gap 后，才改 Skill / prompt / tool / harness，并用同一 eval 重新比较。

不要把 case-specific answer 写进 runtime prompt。One-shot PASS 只是 smoke；有 stochasticity 或 behavioral-uplift claim 时，需要重复、尽量 blinded / sanitized 的对比，并记录 model / prompt / Skill / repo / tool / harness identity 与必要成本 guardrail。

## 边界与输出

- `$verify`：产品 / 工程 claim → proof obligation → Evidence → `proven / false / unproven`。
- `$eval`：agent behavior → Task + Environment + Verifier → reproducible measurement。
- Northstar / Beacon / AE / Unknowns First 继续拥有各自 engineering semantics；Eval 只测它们的 agent behavior，不替它们做 semantic judgment。

返回最小充分 Eval artifact：Capability / failure、Task、Environment、Verifier、backend binding、Run Evidence / Trajectory，以及 `trustworthy / needs-eval-fix / inconclusive` measurement status。持久化到 `evals/` 或项目既有 eval surface，不创建第二份 Intent、implementation plan 或 product verification SOT。
