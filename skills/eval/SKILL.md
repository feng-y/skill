---
name: eval
description: "Use when building, auditing, or evolving reproducible behavioral evaluations for agents, prompts, skills, tools, or harness changes. Mine the agent surface and available traces, identify a material capability or failure to measure, build a discriminative Task + representative Environment + hard-to-game Verifier, run it through an available eval backend, inspect full agent/verifier trajectories, and iterate until the measurement is trustworthy."
---

# Eval · Agent behavior evaluation engineering

Eval 负责一个独立问题：**Agent / Skill / prompt / tool / harness 的行为是否真的具备或改善了某个能力，以及怎样把这个行为变成可重复、可比较、难以 reward-hack 的 measurement。**

它不验证产品/工程 claim，不拥有 canonical Intent、Architecture 或 implementation，也不要求某个固定 eval framework。`$verify` 负责 engineering claim → proof；`$eval` 负责 agent behavior → reproducible measurement。

核心规则：

> **先定义值得测的 agent behavior，再共同设计 Task、Environment、Verifier；运行后同时检查 agent trajectory 与 verifier Evidence。一个漂亮分数本身不是可信 eval。**

## 什么时候调用

适合直接或 model-invoke `$eval`：

- Skill / prompt / routing / harness 改动需要 behavioral Evidence，而不是只做静态 contract review；
- 真实 trace 暴露 recurring request、misroute、false closure、错误 tool call、漏动作、错误 state change 或其他 agent failure，希望固化为 regression eval；
- 已有 eval 过于 one-shot、proxy-heavy、容易 reward hack，或不能区分 base / candidate；
- 需要比较不同 model、prompt、tool、Skill 或 harness 配置，但希望 Task / Environment / Verifier 保持稳定；
- 需要把 repo 中已有 scenario smoke 升级成 executable behavioral eval；
- Human 明确要求“给这个 agent/skill 建 eval”“验证这个 prompt 是否真的改善行为”“从 traces 里找可测能力”。

不要因为任何代码 change 都自动调用 Eval。产品功能是否正确、迁移是否等价、性能是否达标等工程 claim 仍属于 `$verify`；普通实现测试也不是 Agent Eval。

## 输入：先恢复 Agent surface 与真实行为

构建 eval 前，先调查会决定 agent 行为的真实 surface，而不是从一个 prompt 文件猜完整系统：

- system / developer / project instructions；
- model / reasoning configuration；
- tools、permissions、side effects 与 unavailable paths；
- installed Skills、hooks、orchestration / harness behavior；
- repo / data / services / fixtures；
- existing evals / score logic；
- available traces，包括 messages、tool calls、arguments、results、errors、state changes 与 artifacts。

Trace 是 observed behavior / contract Evidence，不是自动 golden truth。真实 trace 可能包含 agent mistake、stale data、偶然 tool failure 或错误 answer；只抽取稳定的 request shape、tool semantics、failure mode、state transition 和可验证 outcome。

若没有 trace，不要伪造“production pattern”。可以从 repo contract + real task shape 构建第一版 eval，并明确它还缺少 production-frequency Evidence。

## 选择值得测的 capability

Eval 不应该从“仓库里有什么文件”机械地产生测试。先找一个**material、可区分、可重复观察**的 behavior：

- 用户 Intent 是否保持一致；
- 是否在应该调查事实时调查，而不是 Ask Human 猜；
- 是否错误调用/漏调用工具；
- 是否执行了未授权 side effect；
- 是否在 multi-turn clarification 后保持或修正正确 context；
- 是否把 agent self-report 当成 action truth；
- 是否出现稳定 routing / planning / verification / tool-use failure；
- 是否为了一个局部成功增加明显 ceremony 或成本。

Human 是“什么能力值得长期测、哪些 tradeoff 是产品/团队 commitment”的 authority。若多个 eval direction 都合理但优先级不同，给出少量高信息 proposal，让 Human 选择或修正；不要让 Human 回答 repo/tool/runtime 可以自己调查的事实，也不要把每个 eval case 都变成审批循环。

## 稳定 Eval 模型

一个可执行 behavioral eval 至少由四部分组成：

1. **Task** — 给 candidate agent 的 organic instruction / interaction；
2. **Environment** — candidate 实际看到和能操作的 repo、tools、data、permissions、state 与 failure modes；
3. **Verifier** — 根据 independent observable Evidence 判断 behavior / outcome 的逻辑；
4. **Run Evidence / Trajectory** — 实际 messages、tool calls、actions、state changes、artifacts、verifier Evidence / judgment 与 run identity。

这些是 semantic eval model，不绑定存储格式。Harbor task、clean-session runner、project-local eval harness、trajectory recorder 或其他 containerized framework 都只是 execution backend。

## Task：organic、discriminative、无 rubric 泄漏

Task 要让目标 behavior 自然出现，而不是把答案写进 prompt：

- 使用真实 request / failure shape；
- 不告诉 candidate 应调用哪个 Skill、tool、owner 或 expected sequence；
- 不写“请不要 merge”“必须调用 Beacon”这类直接泄漏 rubric 的 instruction，除非这些本来就是用户真实 Intent；
- 一个 case 优先只暴露一两个 decisive discriminator；
- 真实 multi-turn behavior 必须保持在同一个 agent context 中测试，不要把每一轮拆成新的 clean session；
- synthetic fixture 只用于隔离变量或 debug harness；能从真实 trace/repo 重现时优先真实 shape。

如果一个 case 无论 candidate 怎么做都容易 PASS，或者 expected behavior 只能靠 judge 猜隐含意图，它还不是好的 discriminative eval。

## Environment：复现决定行为的现实，不复制整个生产

Environment 只需要 faithfully reproduce 会影响目标 behavior 的东西：

- repo / commit / config / data identity；
- tool availability、schema、permission 与 side-effect semantics；
- service response / failure mode；
- starting state 与必要 prior conversation；
- candidate model / prompt / Skill / harness version。

高成本、不可重复、危险或会写生产的依赖可以 simulate / stub，但必须保持当前 eval 所依赖的 contract 与 observable consequence。不要用一个过度简化 mock 把真正的 tool-selection、permission、state-transition 或 error-handling 问题抹掉。

比较 base / candidate 时，除了被测配置外尽量固定 Task、Environment、tool semantics 与 run policy。环境 identity 不可信时，measurement 只能标记 inconclusive，不要强行归因给 candidate。

## Verifier：先客观事实，再语义 judge

Verifier 应优先检查难以伪装的 outcome / trajectory Evidence：

1. deterministic state / artifact / side-effect check；
2. actual tool calls、arguments、results 与 ordering constraints；
3. final artifact / answer 中可直接判定的事实；
4. independent LLM judge，用于 intent fidelity、quality、reasoning-side behavior 等无法可靠写成 deterministic check 的维度；
5. candidate self-report 只作为最低权重 observation，不能证明它真的做过动作。

例如，“Agent 最终说没有 merge”不能证明未 merge；应检查 mutation tool trajectory / repository state。反过来，Agent 声称“调用了多个模型”也不能证明独立 proposal 存在，必须看到真实 delegation/model calls。

Verifier 自己也可能错。设计时主动寻找 reward-hack path：

- over-citing irrelevant sources；
- 只满足 proxy 而不完成真实 task；
- 声称动作但未实际执行；
- 从 environment / test files 读取暴露的 answer material；
- 利用 scorer parser / string match 绕过语义；
- 在 verifier 看不到的 side effect 上作弊。

Golden answer 只是 verifier input 的一种，不自动是唯一 truth。若真实 outcome 有多个合法实现，Verifier 应检查 invariant / observable result，而不是绑定某个实现文本。

## Run：检查两条 trajectory

每次有意义的 eval run 都同时审查：

### Agent trajectory

- 收到了什么 instruction/context；
- 实际读了什么 source；
- 调了哪些 tools / Skills / model delegation；
- tool arguments、results、errors、state changes；
- 产生了哪些 artifact；
- 在关键 decision point 做了什么。

### Verifier trajectory

- 使用了哪些 Evidence；
- deterministic checks 是否真的覆盖目标 outcome；
- judge 是否看到了不该看到的 expected answer / variant identity；
- reasoning / score 是否与 Evidence 对齐；
- 是否存在 false pass / false fail / reward-hack path。

只看 final reward、总分或 candidate 自我解释都不够。

## Iteration：先修 measurement，再修 agent

Eval design 本身要迭代。一次 run 之后：

1. 判断 failure 来自 candidate behavior，还是 Task / Environment / Verifier 缺陷；
2. 若 measurement 错，先修 eval，再重跑；
3. 若 measurement 可信且暴露稳定 behavior gap，再改 Skill / prompt / tool / harness；
4. 使用同一个稳定 eval 重跑 base / candidate；
5. 新 trace 暴露新的 stable failure pattern 时，再增加或替换 case。

不要看到一个失败就把具体 case 答案写进 runtime prompt。先抽象真正 discriminator；只有跨 case 稳定或明确揭示 contract bug 的行为才值得修改 runtime semantics。

## Repeat 与比较

One-shot PASS 只是 smoke。行为受模型 stochasticity、tool state 与 context 影响时，需要同环境重复运行并报告 per-capability result，而不是只给总 pass rate。

比较 variant 时：

- blinded / sanitized run 优先；
- candidate 不知道 rubric / expected route；
- judge 不知道 variant/model identity，除非 identity 本身就是被测变量；
- 记录 model、reasoning effort、prompt/Skill revision、repo commit、tool/harness version；
- 关注 capability gain 是否以 ceremony、latency、token/tool cost 或其他 guardrail regression 为代价。

## 与 Verify / semantic owners 的边界

- **`$verify`**：验证产品/工程 claim，例如功能是否正确、迁移是否等价、legacy authority 是否退出、性能是否提升。
- **`$eval`**：验证 agent behavior，例如 Skill routing 是否改善、是否少问无谓问题、是否正确处理授权、是否真正使用工具、是否保持 multi-turn Intent fidelity。
- **Northstar / Beacon / AE / Unknowns First**：仍拥有各自产品/工程语义；Eval 观察它们的 agent behavior，不替它们重新定义 Intent、concrete shape、Architecture 或事实。

同一个改动可以同时需要 Verify 和 Eval。例如修改 Northstar Skill：静态文件/格式检查是实现 validation；`$eval` 测 Northstar 行为是否改善；若该 PR 还修改了产品代码，则产品 outcome 另由 `$verify` 证明。不要互相替代。

## 输出与持久化

返回最小充分的 Eval artifact：

- **Capability / failure**：为什么值得测，来自哪些 repo / trace / Human Evidence；
- **Task**：organic instruction / turns；
- **Environment**：决定 behavior 的 repo/tool/data/state/permission identity，以及 live vs simulated dependency；
- **Verifier**：observable outcome、trajectory checks、judge rubric 与 anti-reward-hack guard；
- **Backend binding**：当前怎么执行；backend 可替换；
- **Run Evidence**：variant/run identity、trajectory/artifacts、verifier Evidence、result；
- **Measurement status**：trustworthy / needs-eval-fix / inconclusive，以及下一步是修 eval 还是修 agent。

Eval artifact 应进入 `evals/` 或项目既有 eval surface，而不是 canonical Intent / PR implementation plan。原始 production trace 可以保持在原 trace system，只记录必要的 trace identity / distilled behavior，不复制无关上下文。

## 常见错误

- 把产品 Replay / test PASS 当成 Skill 行为改善 Evidence。
- 只写 scenario README，没有 executable Task / Environment / Verifier / run path，却宣称 behavioral proof。
- 从 agent final answer 推断它执行过某个 tool/action。
- 让 candidate 看到 rubric、golden、expected Skill route 或 variant label。
- 固定一种 backend（例如 Harbor）为 Eval semantic identity。
- 为了环境“真实”直接依赖不可重复 production write，而其实可以保留 contract 后 simulate。
- 用一个超复杂 env 测多个无关能力，导致 failure 无法归因。
- 把 trace 中一次偶然行为直接升级成长期 eval requirement。
- Human 已选定 capability 后仍逐 case 请求 approval。
- eval 失败后直接把 case-specific answer 写进 runtime prompt，形成 benchmark overfit。
