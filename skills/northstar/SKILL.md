---
name: northstar
description: "Canonical engineering-intent skill: turn a conversation, request, incident, or external signal into durable executable meaning; materialize it as a Drafted Issue when it must survive the current session."
---

# Northstar · 工程 Intent 的 canonical owner

Northstar 负责把当前 conversation、外部请求、incident 或已有讨论收敛成**稳定、可交接的工程 Intent**。当 Intent 需要跨 session、agent、Human 或执行环境流转时，Northstar 将同一份语义 materialize 为 Drafted Issue；Issue 是 Intent 的 durable carrier，不是另一套语义阶段。

Northstar 不再拥有独立 Goal 层，不默认生成 Taskbook，不负责 verification / outcome judgment，也不持续监督 Executor。PR 是 realized Change / Delivery surface；`$replay` 负责依据当前 authoritative contract 验证真实 outcome。

核心规则：

> **原 conversation 消失后，fresh consumer 仍应知道当前问题、准备改成什么样、哪些约束不能破坏、什么结果算成立，以及哪些关键决定已经关闭。**

## Intent 的最小语义

只保留会改变后续判断、实现边界或验收结果的 durable 信息，不为了模板完整制造字段：

- **Problem**：当前什么需要改变，以及为什么现状不满足预期。
- **Draft**：intended change 的具体形态；按问题选择最低成本的 `Current → Intended`、core path、ownership/boundary、usage、interface、schema、state transition 等 representation。
- **Constraints**：真正 binding、违反后会改变 accepted outcome、兼容、投入、风险或长期责任的约束。
- **Acceptance**：能够区分“问题已解决”和“只是完成了某个手段”的 observable outcome / completion claim。

按需增加：

- **Decisions**：已经关闭、后续不应重新猜的 material choice；
- **Evidence**：会改变 Draft / Decision / Acceptance 的 repo、runtime、data 或 authoritative source；
- **Open Questions**：仍会 materially 改变 accepted outcome、boundary 或 commitment 的未决点；
- **Out of Scope**：只有容易被合理误解成 scope 时才保留。

不维护独立 `Goal` 字段。抽象 outcome 只有在增加实际 decision information 时才保留，并直接落实到 Problem、Constraint、Decision 或 Acceptance，而不是形成第二层 SOT。

## 先综合已有上下文，不重新采访

优先消费当前 conversation 已经形成的 Human requirement、correction、decision 与 Evidence。不要因为进入 Northstar 就重做完整访谈。

Human requirement 与 reality claim 分开：Human 有权给出的要求可以 binding；关于 producer、consumer、owner、runtime behavior、baseline 等事实必须由 territory Evidence 支持。一个未决答案只有在仍会 materially 改变 Problem、Draft、Constraint、Acceptance 或 Human commitment，且无法从 territory / authority 得到时，才暴露为 Human decision。

## 按需调用 specialist

Northstar 拥有 Intent，不复制 specialist 的责任：

- **territory fact 未知**，且事实不同会改变 Intent：调用 `$unknowns-first`，消费最小 Evidence；
- **Intent 已理解，但同一 prose 仍允许 materially different 的 concrete shape**：调用 `$prototype`，消费 Core Path / Usage / disposable Prototype 带来的 correction / Evidence；
- **长期 responsibility、knowledge ownership、boundary、variation、dependency 或 Target Architecture 需要判断**：调用 `$architecture-evolution`，消费结构 decision；
- **实现完成后的 claim verification / false-pass / outcome judgment**：交 `$replay`，Northstar 不替 Replay 设计 verifier 或独立判卷。

specialist 结果不创建第二份 Intent SOT。只把后续 fresh consumer 必须知道的 durable Decision、Draft correction、Constraint、Acceptance 或 Evidence fold back 到当前 Intent / Issue。

## Drafted Issue

当 Intent 需要脱离当前 conversation 流转时，Drafted Issue 是 canonical durable surface。Issue body 保存当前 intended change；comments 保存讨论历史、probe 结果、候选方案、阶段性 Evidence 与 correction trail。

只有 fresh consumer 后续必须知道的信息才 fold back 到 body。新的 binding constraint、accepted Draft correction、durable decision 或改变完成定义的 Acceptance 应回写；普通 reasoning、进度和 implementation How 不应不断膨胀 Issue body。

用户明确要求创建或更新 Issue，且当前环境存在已授权 tracker action 时，直接创建 / 更新真实 Issue，不停在 Markdown 草稿等待再次确认。已有 canonical Issue 时优先更新它，不创建平行 SOT。

Issue 按 cohesive engineering outcome / responsibility boundary 切，不按一次 model context、一个文件或一个 agent session 切。Execution orchestration / control plane 位于 Northstar 语义之外；它可以依据 tracker / runtime state 控制工作何时以及由谁继续，但不能定义或改写 Intent。

## Material compile 只在真正需要时出现

一个 Drafted Issue 已足以让 fresh Executor 在 binding boundary 内开始时，直接交执行，不为了流程完整生成 Graph / Taskbook。

只有 material work / dependency 本身复杂到 Issue 仍不足以安全交接时，才读取 [references/material-compile.md](references/material-compile.md)，从已经成立的 Intent / Intended Draft 编译 coarse material work 与真实 dependency。Compile 不能反向发明 Intent，也不能用 task decomposition 发现 Target。

## 与 Replay 的反馈边界

Northstar 定义 Acceptance；Replay 负责证明或反证它。

Replay 返回后按 owner 路由：

- implementation / behavior 未满足当前 Intent → 留在 PR / Executor 修复；
- Evidence 不足 → Replay 继续补足 claim-relevant proof；
- verified reality 证明 Intent Draft / Constraint / Acceptance 本身错误或失效 → 只重开 Northstar 中受影响的部分；
- 出现此前未决的长期 structure fork → 交 `$architecture-evolution`；
- 需要改变投入、兼容、长期维护或风险 commitment → 回 Human，经 Northstar 更新 canonical Intent。

不要因为 Replay red 就自动重写 Intent，也不要因为 tests green 就宣布 Intent 正确。

## 停止条件

满足以下条件就停止 Intent shaping：

- fresh consumer 不依赖原 conversation 就能理解 Problem 与 intended Draft；
- binding Constraint / Decision 足以防止 materially wrong interpretation；
- Acceptance 足以区分真实 outcome 与只完成手段；
- 剩余未知只影响 Executor How，或已作为真实 blocker / Open Question 暴露；
- 若需要 tracker handoff，canonical Issue 已创建或更新。

## 常见错误

- 把 Goal、spec、plan、Taskbook 都做成并行 SOT。
- clear Issue 仍强制经过 compile / Graph。
- 把 `$prototype` 的 artifact 当作新的 authority，而不是 reaction surface。
- 让 AE 的 Program convenience 反向改写 Intent。
- 在 Northstar 内选择 replay/test/runtime verifier 并持续判卷。
- 把 Issue 切成适配单次 agent context 的细粒度 ticket。
- PR 只暴露 implementation bug 时频繁 churn Intent；只有 intended change 本身被反证才回流。
