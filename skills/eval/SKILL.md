---
name: eval
description: "Use when building, auditing, or evolving reproducible behavioral evaluations for agents, prompts, skills, tools, or harness changes. Mine the real agent surface and available traces, identify a material capability or failure, build a discriminative Task + representative Environment + hard-to-game Verifier, run through an available eval backend, inspect agent/verifier trajectories, and iterate until the measurement is trustworthy."
---

# Eval · Agent behavior evaluation engineering

Eval 负责一个独立问题：**Agent / Skill / prompt / tool / harness 的行为是否真的具备或改善了某个能力，以及怎样把它变成可重复、可比较、难以 reward-hack 的 measurement。**

它不验证产品/工程 claim，不拥有 canonical Intent、Architecture 或 implementation，也不绑定某个 eval framework。`$verify` 负责 engineering claim → proof；`$eval` 负责 agent behavior → reproducible measurement。

核心规则：

> **先定义值得测的 behavior，再共同设计 Task、Environment、Verifier；运行后同时检查 agent trajectory 与 verifier Evidence。一个漂亮分数本身不是可信 eval。**

## 什么时候调用

直接或 model-invoke `$eval`，当：

- Skill / prompt / routing / tool / harness 改动需要 behavioral Evidence；
- trace 暴露 recurring misroute、false closure、错误/漏 tool call、错误 state change 或其他稳定 agent failure；
- 已有 eval one-shot、proxy-heavy、容易 reward hack，或无法区分 base / candidate；
- 需要把 scenario smoke 升级成 executable behavioral eval，或稳定比较 model/prompt/tool/Skill/harness variant。

产品功能正确性、迁移等价、性能、结构 completion 等 engineering claim 仍属于 `$verify`；普通实现测试也不是 Agent Eval。

## 先恢复真实 Agent surface

不要从单个 prompt 文件猜系统。只调查会决定目标 behavior 的 surface：instructions、model/reasoning config、tools/permissions/side effects、Skills/hooks/harness、repo/data/services、existing evals，以及可用 traces 中的 messages、tool calls、results/errors、state changes 与 artifacts。

Trace 是 observed behavior / contract Evidence，不是自动 golden truth。只抽取稳定 request shape、tool semantics、failure mode、state transition 和可验证 outcome。没有 trace 时可从 repo contract + real task shape 构建第一版，但不要虚构 production frequency。

## 选择值得测的 capability

目标必须 **material、可区分、可重复观察**，例如 intent fidelity、fact-vs-Human routing、tool/action correctness、authorization fidelity、multi-turn continuity、verification behavior 或 ceremony/cost regression。

Human 是“哪些能力值得长期测、哪些 tradeoff 是产品/团队 commitment”的 authority。多个方向都合理时给少量高信息 proposal 让 Human 选择；repo/tool/runtime 事实自己调查，不把每个 case 变成审批循环。

## 稳定 Eval 模型

一个 executable behavioral eval 至少包含：

1. **Task** — candidate agent 收到的 organic instruction / interaction；
2. **Environment** — repo、tools、data、permissions、state 与 relevant failure modes；
3. **Verifier** — 根据 independent observable Evidence 判断 behavior / outcome；
4. **Run Evidence / Trajectory** — messages、tool calls/actions、state changes、artifacts、verifier Evidence/judgment 与 run identity。

Harbor、clean-session runner、trajectory recorder 或 project-local evaluator 都只是 execution backend，不属于 Eval semantic identity。

## Task：organic、discriminative

- 使用真实 request / failure shape；
- 不暴露 expected Skill/tool/owner/sequence、rubric、golden 或 variant identity；
- 一个 case 优先暴露一两个 decisive discriminator；
- multi-turn behavior 必须保持同一 agent context；
- synthetic fixture 只在隔离变量或 debug harness 时使用。

如果 candidate 很容易从 instruction 猜 scorer，或任何合理行为都能 PASS，这个 Task 还不能提供判别力。

## Environment：复现决定行为的现实

Environment 只 faithful reproduce 目标 behavior 依赖的 repo/config/data identity、tool schema/permission/side-effect semantics、service failure mode、starting state / prior turns，以及 candidate model/prompt/Skill/harness version。

高成本、不可重复或会写 production 的依赖可以 simulate / isolate，但必须保留当前 eval 依赖的 contract 与 observable consequence。比较 variant 时，除被测配置外尽量固定 Task、Environment、tool semantics 与 run policy；identity 不可信时结果应 inconclusive。

## Verifier：先客观事实，再语义 judge

Evidence 优先级：

1. deterministic state / artifact / side-effect；
2. actual tool calls、arguments、results 与必要 ordering；
3. final artifact / answer 中可直接判断的事实；
4. independent semantic judge，用于 intent fidelity、quality 等无法可靠 deterministic-check 的维度；
5. candidate self-report 不能证明动作真的发生。

例如“我没有 merge”不证明未 merge，应检查 mutation trajectory / state；“调用了多个模型”也必须有真实 delegation/model calls。

Verifier 本身也要审计 reward-hack：proxy completion、irrelevant citation、暴露 golden、string/parser shortcut、claimed-but-unperformed action、verifier 看不到的 side effect。多个合法实现时验证 invariant / observable outcome，不绑定某个答案文本。

## Run：同时检查两条 trajectory

运行后必须同时看：

- **Agent trajectory**：输入/context、实际 source、tools/Skills/delegation、arguments/results/errors、state changes、artifacts 与关键 decision；
- **Verifier trajectory / Evidence**：用了什么证据、deterministic check 是否覆盖 outcome、judge 是否泄漏 expected answer/variant、score 是否与 Evidence 对齐、是否存在 false pass/fail。

只看 final reward、总分或 agent 自我解释都不够。

## 先修 measurement，再修 agent

一次 run 后先判断 failure 来自 candidate behavior，还是 Task / Environment / Verifier 缺陷。measurement 错就先修 eval 并重跑；measurement 可信且暴露稳定 gap 后，才改 Skill / prompt / tool / harness，再用同一个 eval 比较。

不要把 case-specific answer 直接写进 runtime prompt。先抽象 discriminator；只有跨 case 稳定或明确揭示 contract bug 的行为才值得修改 runtime semantics。

One-shot PASS 只是 smoke。存在 stochasticity 或 uplift claim 时应重复运行，优先 blinded / sanitized comparison，并记录 model/reasoning、prompt/Skill revision、repo/environment/tool/harness identity。关注 capability gain 是否换来 ceremony、latency、token/tool cost 等 guardrail regression。

## 与 Verify / semantic owners 的边界

- **`$verify`**：产品/工程 claim，例如功能、equivalence、legacy exit、performance、structural completion；
- **`$eval`**：agent behavior，例如 routing、authorization、tool use、multi-turn intent fidelity、verification behavior；
- **Northstar / Beacon / AE / Unknowns First**：继续拥有各自产品/工程语义；Eval 观察其 agent behavior，不重新定义这些语义。

同一个 change 可以同时需要 Verify 和 Eval，但两种 Evidence 不能互相替代。

## 输出与持久化

返回最小充分 Eval artifact：

- Capability / failure 与来源；
- Task；
- Environment identity + live/simulated boundary；
- Verifier + anti-reward-hack guard；
- backend binding；
- Run Evidence / Trajectory + variant identity；
- measurement status：`trustworthy / needs-eval-fix / inconclusive`，以及下一步修 eval 还是修 agent。

Eval artifact 进入 `evals/` 或项目既有 eval surface，而不是 canonical Intent / implementation plan / product verification SOT。原始 production trace 保留在原 trace system，只记录必要 identity / distilled behavior。

## 常见错误

- 用产品 Replay/test PASS 证明 Skill 行为变好；
- 只有 scenario README，没有 executable Task / Environment / Verifier / run path，却宣称 behavioral proof；
- 从 final answer 推断 tool/action 已发生；
- 让 candidate 看到 rubric/golden/expected route；
- 把 Harbor 等 backend 变成 Eval identity；
- trace 的一次偶然行为直接升级成长期 requirement；
- eval 失败后把 case answer 写进 runtime prompt，形成 benchmark overfit。
