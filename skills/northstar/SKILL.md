---
name: northstar
description: "Canonical engineering-intent skill: turn a conversation, request, incident, or external signal into durable executable meaning; materialize it as a Drafted Issue when it must survive the current session."
---

# Northstar · 工程 Intent 的 canonical owner

Northstar 负责把当前 conversation、外部请求、incident 或已有讨论收敛成**稳定、可交接的工程 Intent**。当 Intent 需要跨 session、agent、Human 或执行环境流转时，Northstar 将同一份语义 materialize 为 Drafted Issue；Issue 是 Intent 的 durable carrier，不是另一套语义阶段。

Northstar 不拥有独立 Goal 层，不默认生成 Taskbook，不负责 proof sufficiency judgment，也不持续监督 Executor。PR 是 realized Change / Delivery surface。普通 implementation-local checks 属于 Executor；当 completion / safety claim 的 verification 本身需要独立设计或判断时，交 `$verify`。

核心规则：

> **原 conversation 消失后，fresh consumer 仍应知道当前问题、准备改成什么样、哪些约束不能破坏、什么结果算成立，以及哪些关键决定已经关闭。**

## Intent 的最小语义

只保留会改变后续判断、实现边界或验收结果的 durable 信息，不为了模板完整制造字段：

- **Problem**：当前什么需要改变，以及为什么现状不满足预期。
- **Draft**：每个 Intent 的唯一主 Draft，表达 intended change 的具体形态；按问题选择最低成本的 `Current → Intended`、core path、ownership/boundary、usage、interface、schema、state transition 等 representation。
- **Constraints**：真正 binding、违反后会改变 accepted outcome、兼容、投入、风险或长期责任的约束。
- **Acceptance**：能够区分“问题已解决”和“只是完成了某个手段”的 observable outcome / completion claim。

按需增加 Decisions、Evidence、Open Questions、Out of Scope。只保留后续 fresh consumer 真正需要的内容。

不维护独立 `Goal` 字段。抽象 outcome 只有在增加实际 decision information 时才保留，并直接落实到 Problem、Constraint、Decision 或 Acceptance，而不是形成第二层 SOT。

## 一个 Intent，一个主 Draft

从已有 context 建立并持续修正同一个主 Draft。它是 canonical intended change，不是多个 specialist 输出的集合，也不等于只能有一个物理文件；多个视图和候选对比可以支撑它，但必须能区分当前采用的形态、未决选择与已被替代的解释。独立 Intent 各自拥有主 Draft，不强行合并。

Draft 的充分性看**连贯的 material change 是否已经可交接**，不看字数或调用次数。把共同决定核心路径、dataflow、ownership / lifecycle 或 binding boundary 的部分连起来；只展开会改变 intended outcome 或让 fresh Executor 被迫重新做高层判断的关系。局部变更可以只有几句话，不要求穷尽 implementation How。

specialist 返回后，Northstar 必须把采用的 correction / Decision 整合进这个主 Draft，并检查受影响部分与其余部分是否仍一致。不能只转贴局部答案，让 fresh Executor 自行拼出 intended change。仍有 material shape gap 才继续按需 shaping；已有 Draft 已充分时直接交接，不为流程完整调用 Prototype。

## Acceptance 定义预期，Verify 负责验证

Northstar 必须让 material Acceptance **可判断**，但不需要在这里选择 backend 或写具体 proof plan。

- Northstar：什么结果才算符合预期；
- Verify：什么真实 observation 能证明/反证这个 claim，选择什么 backend，现有 Evidence 是否足够；
- backend：实际运行 test/build/Replay/runtime/data/profile 等并返回 observation。

如果 Acceptance 只能靠“完成某个实现步骤”表达，继续收敛 outcome；如果 Acceptance 已明确但 proof route 不清、baseline/oracle 复杂或 false-pass risk material，可调用 `$verify`。不要因为项目有 Replay 就把 Replay 命令写进 Intent contract。

## 先综合已有上下文，不重新采访

优先消费当前 conversation 已经形成的 Human requirement、correction、decision 与 Evidence。不要因为进入 Northstar 就重做完整访谈。

Human requirement 与 reality claim 分开：Human 有权给出的要求可以 binding；关于 producer、consumer、owner、runtime behavior、baseline 等事实必须由 territory Evidence 支持。一个未决答案只有在仍会 materially 改变 Problem、Draft、Constraint、Acceptance 或 Human commitment，且无法从 territory / authority 得到时，才暴露为 Human decision。

## 按需调用 specialist

Northstar 拥有 Intent，不复制 specialist 的责任：

- **factual territory unknown**，且事实不同会改变 Intent → `$unknowns-first`；
- **Intent 已理解，但主 Draft 的 concrete shape 仍有 material gap** → `$prototype`；带上现有 Draft、binding context 与缺口，委托足以连贯呈现受影响核心路径的 surface，不把耦合关系拆成互不相干的局部问题；
- **长期 responsibility、knowledge ownership、boundary、variation、dependency 或 Target Architecture 需要判断** → `$architecture-evolution`；
- **material completion / safety claim 需要 proof obligation、real-artifact verification 或 sufficiency judgment** → `$verify`。

specialist 的多个 view / candidate / Evidence 都不是并行主 Draft。Northstar 只将采用且后续 fresh consumer 必须知道的 correction 整合回当前 Intent / Issue；AE 保留 Target judgment，Verify 保留 proof judgment，Unknowns First 只关闭事实。Proof 命令、临时 output、replay artifact 默认留在 Verify/PR/runtime surface，不塞进 Issue body。

## Drafted Issue

当 Intent 需要脱离当前 conversation 流转时，Drafted Issue 是 canonical durable surface。Issue body 保存当前 intended change；comments 保存讨论历史、probe 结果、候选方案、阶段性 Evidence 与 correction trail。

只有 fresh consumer 后续必须知道的信息才 fold back 到 body。新的 binding constraint、accepted Draft correction、durable decision 或改变完成定义的 Acceptance 应回写；普通 reasoning、进度和 implementation How 不应不断膨胀 Issue body。

用户明确要求创建或更新 Issue，且当前环境存在已授权 tracker action 时，直接创建 / 更新真实 Issue，不停在 Markdown 草稿等待再次确认。已有 canonical Issue 时优先更新它，不创建平行 SOT。

Issue 按 cohesive engineering outcome / responsibility boundary 切，不按一次 model context、一个文件或一个 agent session 切。Execution orchestration / control plane 位于 Northstar 语义之外；它可以依据 tracker / runtime state 控制工作何时以及由谁继续，但不能定义或改写 Intent、material Graph 或 Acceptance。

## Material compile 只在真正需要时出现

一个 Drafted Issue 已足以让 fresh Executor 在 binding boundary 内开始时，直接交执行，不为了流程完整生成 Graph / Taskbook。

只有 material work / dependency 本身复杂到 Issue 仍不足以安全交接时，才读取 [references/material-compile.md](references/material-compile.md)，从已经成立的 Intent / Intended Draft 编译 coarse material work 与真实 dependency。Compile 不能反向发明 Intent，也不能用 task decomposition 发现 Target。

## Evidence feedback

Research、execution、review 和 verifier/backend 都可能产生 observation；只有经过足够核实的 Evidence 才改变 semantic owner。按真正受影响的 surface 回流：

- factual premise 不清 → `$unknowns-first`；
- verified reality 证明 Intent Draft / Constraint / Acceptance 本身错误或失效 → 只重开 Northstar 中受影响的部分；
- already-understood Intent 出现新的 material concrete-shape ambiguity → `$prototype`；
- 出现此前未决的长期 structure fork → `$architecture-evolution`；
- 当前 claim 需要定义/补足 verification 或判定 sufficiency → `$verify`；
- Intent 仍成立，但 verified Evidence 改变复杂 material work / dependency → 只重进 material compile 的 affected cone。

不要因为 Replay/test red 就自动重写 Intent，也不要因为 build/test/replay green 就宣布 Intent 正确。Backend observation 必须先对应到 authoritative claim。

## 停止条件

可执行实现 handoff 必须同时满足：

- fresh consumer 不依赖原 conversation 或自行拼接 specialist 输出，就能理解 Problem 与唯一主 Draft 的连贯 material change；
- binding Constraint / Decision 足以防止 materially wrong interpretation；
- Acceptance 足以区分真实 outcome 与只完成手段；
- 剩余未知只影响 Executor How，不再隐藏会改变 intended shape / binding commitment 的选择；
- 若需要 tracker handoff，canonical Issue 已创建或更新。

若事实或 Human-owned choice 仍阻断 material shape，保留 best-known 主 Draft、具体 blocker 与下一步 owner；可以交接调查或未受影响的工作，但不能把被阻断部分标为可执行实现 handoff。不能为了 Draft 看起来完整而猜测 territory 或代替 Human 承诺。

## 常见错误

- 把 Goal、spec、plan、Taskbook 都做成并行 SOT。
- clear Issue 仍强制经过 compile / Graph。
- 把 `$prototype` 的 artifact 当作新的 authority，而不是 reaction surface。
- 让 AE 的 Program convenience 反向改写 Intent。
- 在 Northstar 内选择 test/Replay/runtime backend 并自行判断 proof sufficiency。
- 把 Issue 切成适配单次 agent context 的细粒度 ticket。
- 把任何 red finding 都当成 Intent 错误；只有 intended change / binding premise 本身被 authoritative Evidence 反证才回流。
