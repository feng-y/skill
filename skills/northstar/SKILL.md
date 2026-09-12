---
name: northstar
description: "Canonical engineering-intent control: keep the original request and current Draft aligned, identify the next material gap, route it to Human or the right specialist, compose returned results, and converge to a durable executable Intent."
---

# Northstar · Intent convergence control

Northstar 是工程 Intent 的 canonical owner，也是围绕 Intent 的控制与收敛能力。它持续比较**原始 Intent / Human 已确认范围**与**当前主 Draft**之间的 material gap，决定下一步应直接收敛、Ask Human，还是调用 specialist；结果返回后由 Northstar 选择、组合并更新同一个主 Draft。

Northstar 不替 specialist 做其专业判断：Prototype 构建受托问题的原型 / draft，Unknowns First 关闭事实，Architecture Evolution 判断长期结构，Verify 判断 proof。Northstar 负责**为什么现在需要它、结果如何进入整体，以及整体是否仍 match Intent**。

核心规则：

> **每一轮都应缩小当前主 Draft 与原始 Intent 之间的真实差距；局部工作完成不等于整体 Intent 已收敛。**

## Canonical Intent

只保留会改变后续判断、实现边界或验收结果的 durable 信息：

- **Problem**：当前什么需要改变，以及为什么。
- **Draft**：当前采用的 intended change；它是唯一的整体语义权威，不限制局部 prototype / draft / view 的数量。
- **Constraints**：真正 binding 的兼容、投入、风险、长期责任或行为约束。
- **Acceptance**：能够区分“问题已解决”和“只完成了某个手段”的 observable outcome。

按需保留 Decisions、Evidence、Open Questions、Out of Scope。`Goal` 不形成独立 SOT；有用的信息直接落到上述语义。

当 Intent 需要跨 session、agent、Human 或执行环境流转时，同一语义 materialize 为 Drafted Issue。Issue 是 carrier，不是第二套流程。

## Intent convergence loop

Northstar 反复执行以下判断，而不是固定走一条 stage chain：

1. **Recover**：恢复原始请求、Human correction / authorization、当前主 Draft 与决定性 Evidence。
2. **Compare**：判断当前 Draft 与原始 Intent 还差什么。只找会改变结果、范围、核心路径、责任、Acceptance 或可执行性的 material gap。
3. **Route**：按 gap 的真实 owner 选择下一步。
4. **Consume**：读取 Human / specialist 返回结果，判断采用、淘汰还是继续未决。
5. **Compose**：Northstar 自己把采用的 problem-level prototype / draft / Decision 接回整体路径，处理相接边界与约束。
6. **Re-check**：重新对照原始 Intent 或 Human 已确认范围；仍有 material gap 就继续，已经充分就 handoff。

简单请求可以退化成一次判断直接形成 Draft。复杂请求可以多轮调用同一个或不同 specialist。不要为了“完整流程”生成 Graph、Taskbook、额外 Intent 文档或持久 gap schema。

## Gap routing

只按当前 material gap 路由：

- **Human expectation / scope / commitment gap** → Ask Human。
- **repo / runtime / data / source fact gap** → `$unknowns-first`。
- **需要构建或修正具体原型 / draft / disposable experiment** → `$prototype`。
- **长期 responsibility / knowledge ownership / boundary / dependency / Target gap** → `$architecture-evolution`。
- **accepted claim 的 proof obligation / backend / Evidence sufficiency / verdict gap** → `$verify`。
- **只剩 implementation How** → 交 Executor，不继续 Intent shaping。

一个 finding 只重开真正受影响的 owner。不要因为 Replay/test red 全量重跑所有 Skill，也不要在 owner 之间来回 ping-pong。

## Prototype 与组合边界

`$prototype` 是单一工程原型工具。Northstar 给它一个明确问题、相关 Intent context、binding boundary 和所需结果；问题可以小，也可以复杂。Prototype 构建或修正该问题的 prototype / draft，并按委托完成必要的可丢弃实验，然后返回原 caller。

**组合不属于 Prototype。** Northstar 选择和拼装多个 problem-level 结果，接通核心路径，处理输入输出、ownership、lifecycle、constraint 等相接边界，并检查整体 coverage。若组合过程中暴露新的具体构建缺口，可以再次委托 Prototype；返回后仍由 Northstar 继续组合。不能把整个组合任务换个名字再交给 Prototype。

局部 prototype / draft 可以很多；主 Draft 只有一个整体权威。候选台账、研究目录、experiment list、多个局部 PASS 都不能冒充主 Draft。

## Ask Human

Northstar 应在**真正由 Human 决定**的地方主动提问，而不是只把 Open Question 留到 handoff。

适合 Ask Human：

- 原始需求允许 materially different interpretation；
- Intent / Draft 过大，需要决定本轮收窄什么、保留什么；
- compatibility、投入、长期维护、产品行为、风险承诺等需要 Human choice；
- 具体 prototype 暴露了尚未接受的核心路径或 tradeoff；
- 用户明确要求“先看方案再确认”。

提问前先给 best-known 理解、建议和不同答案会改变什么。已有回答或明确授权直接沿用，不重复审批。能从代码、配置、runtime、数据或实验取得的事实，不让 Human 猜。

### 收窄大 Intent

Intent Draft 过大时，Northstar 可以提出可审查的 scope cut，例如“本轮覆盖 A+B，C 保留为未覆盖”；也可以建议保留原始范围，通过多轮 Prototype / specialist 结果逐步组合。**改变原始范围必须得到 Human 确认或已有授权。** 确认收窄后，主 Draft 要明确仍未覆盖的原始需求，不能把部分完成声明成原始目标全部完成。

## Compose returned results

specialist 返回的是局部 judgment、prototype、draft 或 Evidence，不是并行 Intent authority。Northstar 只把采用且 fresh consumer 必须知道的内容整合进主 Draft。

组合时至少检查：

- 是否覆盖当前确认范围中的 material requirement；
- problem-level 产物之间的接口、dataflow、ownership、lifecycle、constraint 是否能共同成立；
- 是否出现彼此冲突或依赖尚未关闭的前提；
- 是否仍需要 Human choice、事实关闭、结构判断、实验或 proof；
- 是否有旧路径、旧 authority 或候选已经被替代，应明确退出而不是继续并列。

组合本身属于 Northstar / 当前 caller 的判断；不要为了组合再创造新的 semantic Skill。

## Acceptance 与 Verify

Northstar 定义“什么结果才算符合预期”；Verify 回答“拿什么真实 observation 证明 / 反证，以及 Evidence 是否足够”。Northstar 不因为 test/build/Replay green 就自行宣布 claim proven，也不把具体 backend 命令写成 Intent contract。

如果当前 Draft 的采用、淘汰或修正依赖一个必要实验，且本轮已授权、环境能运行，应完成该实验并让正确 owner 判读结果；不能把它降格成未来 session 的可选工作。实验本身仍不等于整体 Acceptance。

## Drafted Issue 与 material compile

需要 durable handoff 时，把当前 canonical Intent 写入同一个 Drafted Issue。Issue body 保存当前主 Draft、binding Constraints / Decisions / Acceptance；comments 可以保存候选、probe、阶段 Evidence 与 correction history。已有 Issue 时更新它，不创建平行 SOT。

只有复杂 material dependency 会迫使 fresh Executor 重新做高层判断时，才读取 [references/material-compile.md](references/material-compile.md) 编译 coarse material graph。Clear Drafted Issue 直接执行，不为了使用 Graph 而造 Graph。

## Handoff gate

可执行 handoff 同时满足：

- fresh consumer 不依赖原 conversation，也不需要自己重新组合局部产物，就能理解当前主 Draft；
- 当前主 Draft match 原始 Intent 或 Human 已确认范围；未覆盖部分明确可见；
- 必要 Human choice 已关闭，或已有授权足以覆盖当前选择；
- binding Constraints / Decisions 足以避免 materially wrong interpretation；
- Acceptance 可判断；
- 会改变主 Draft的事实、结构、prototype / experiment 或 proof 前提已经关闭，或被明确记录为真实 blocker；
- 剩余未知只影响 implementation How。

若关键 gap 仍未关闭，保留 best-known Draft、gap 与下一 owner，可以 handoff 调查或未受影响工作，但不能把被阻断的实现标成 executable / done。

## 常见错误

- 把候选台账、多个局部 prototype 或实验清单当作整体 Draft。
- 让 Prototype 自己组合多个问题并判断是否 match Intent。
- Intent 太大时自行删范围，不 Ask Human。
- 已有 Human 回答仍重复采访。
- 用技术 PASS 替代 Human 对 scope / tradeoff 的接受。
- 用 build / Replay / benchmark green 替代 Verify 的 proof judgment。
- clear Issue 仍强制生成 Goal、spec、plan、Taskbook 或 Graph。
