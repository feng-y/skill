---
name: northstar
description: "Clarify engineering intent with the Human, compose problem-level prototypes and drafts into one coherent intended change, and confirm scope adjustments when needed. Materialize the accepted meaning as a Drafted Issue for durable handoff."
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

## 围绕原始 Intent 组合主 Draft

`$prototype` 是解决具体问题的工具，可以产出对应的原型与 draft。一个 Intent 可以使用多个这样的产物；Northstar 负责选择、组合和修正，形成与原始 Intent 匹配的主 Draft，必要时搭起可观察的完整原型。唯一的是当前 intended change 的语义权威，不是局部原型、draft、视图、文件或调用的数量。局部 draft 可以保留，但不能各自改写整体 Intent。

组合不是串接文件或候选台账。把采用的部分沿核心路径连起来，检查相接处的输入输出、责任、生命周期、约束与 Acceptance 是否一致，以及原始需求是否被覆盖；局部结果成立不代表组合后成立。只展开会改变整体判断的关系，不制造统一拼装协议或穷尽 implementation How。出现事实缺口、新结构选择或 proof gap 时仍交对应 owner。

主 Draft 表达当前采用的整体方案，而不是研究目录或 backlog。候选可以替换、组合；采用的部分与未决项必须区分。Northstar 将 specialist 结果与 Human correction 整合回同一主 Draft；改变范围必须得到 Human 确认或已有明确授权，不能为了凑出可交付结果而悄悄删掉原始需求。

选型或组合依赖必要试验且当前已授权、环境能够执行时，继续取得并由对应 owner 判读结果；不能以“已委派”或产物集合代替整体收敛。清晰小任务可以直接形成简短 Draft，不要求调用 Prototype 或再造总原型。整体已足够且本轮前置委托已完成时交接，不接管后续生产实现或持续调度。

## Acceptance 定义预期，Verify 负责验证

Northstar 必须让 material Acceptance **可判断**，但不需要在这里选择 backend 或写具体 proof plan。

- Northstar：什么结果才算符合预期；
- Verify：什么真实 observation 能证明/反证这个 claim，选择什么 backend，现有 Evidence 是否足够；
- backend：实际运行 test/build/Replay/runtime/data/profile 等并返回 observation。

如果 Acceptance 只能靠“完成某个实现步骤”表达，继续收敛 outcome；如果 Acceptance 已明确但 proof route 不清、baseline/oracle 复杂或 false-pass risk material，可调用 `$verify`。不要因为项目有 Replay 就把 Replay 命令写进 Intent contract。

## Ask Human：澄清、收窄与确认组合

先吸收已有要求、回答、correction 与授权，不重新做完整访谈。Northstar 可以展示 best-known Draft、局部原型或组合后的核心路径，帮助 Human 对具体方案作出反应；不必等所有技术问题关闭才问。

- **澄清**：需求含义、期望、范围或约束仍有会改变方案的歧义时，说明当前理解与差异，提出针对性问题。
- **收窄或组合**：Intent Draft 过大、难以在当前范围完整呈现或兑现时，先给可审查的建议：收窄本轮解决的问题，或保留原始目标、组合已有原型 / draft。说明各自覆盖什么、暂不覆盖什么以及关键取舍，再 ask Human 确认需要改变的范围或承诺。已经授权且不改变范围的技术组合可直接推进，不把“大”本身变成审批理由。
- **确认**：具体形态暴露了尚未接受的核心路径或取舍，或用户明确要求先看后确认时，展示方案、建议与影响，取得确认或修正。性能或正确性通过不能代替 Human 的预期与承诺。

每次问题都应指出不同答案会改变什么。回答更新同一主 Draft 及受影响的原型 / 组合关系；Human 接受收窄后，明确本轮范围和原始请求中尚未覆盖的部分，不能宣称原始大目标已全部完成。已有明确答案或授权就直接沿用，不重复确认；不受待答选择影响的工作继续推进。

repo / runtime / producer / baseline 等可调查事实优先用 Evidence 关闭，只有 Human 掌握的事实才向其询问。可向 Human 询问时实际提出问题，而不是仅把待确认项留在 handoff；不能凭模型偏好、测试通过或沉默替 Human 接受未授权的范围变化。

## 按需调用 specialist

Northstar 拥有 Intent，不复制 specialist 的责任：

- **factual territory unknown**，且事实不同会改变 Intent → `$unknowns-first`；
- **一个具体问题需要原型 / draft、已有部分需要组合呈现，或本轮明确委托了可丢弃试验** → `$prototype`；带上相关 Intent、现有 Draft、binding context 与要解决的问题，允许局部产物并说明组合所需关系；形态已明确也不取消明确实做；
- **长期 responsibility、knowledge ownership、boundary、variation、dependency 或 Target Architecture 需要判断** → `$architecture-evolution`；
- **material completion / safety claim 需要 proof obligation、real-artifact verification 或 sufficiency judgment** → `$verify`。

specialist 产出的局部原型、draft、candidate 与 Evidence 由 Northstar 按整体需求选择和组合，不是并行的 Intent 权威。只将采用且后续 fresh consumer 必须知道的结果整合回当前 Intent / Issue；AE 保留 Target judgment，Verify 保留 proof judgment，Unknowns First 只关闭事实。Proof 命令、临时 output、replay artifact 默认留在 Verify/PR/runtime surface，不塞进 Issue body。

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

- fresh consumer 不依赖原 conversation 或自行拼接局部产物，就能理解与原始 Intent 或 Human 已确认范围匹配的主 Draft；组合关系连贯、关键需求没有遗漏，未覆盖的部分明确；
- 必要的 Human 澄清与确认已完成，或已有明确授权覆盖当前选择；不能把可运行、测量通过当成 Human 已认可核心方案；
- binding Constraint / Decision 足以防止 materially wrong interpretation；
- Acceptance 足以区分真实 outcome 与只完成手段；
- 剩余未知只影响 Executor How；会改变当前 Draft 采用、组合、淘汰或修正的必要试验已有相应 owner 判读的结果，不把尚未验证的关键假设标成已收敛；
- 若需要 tracker handoff，canonical Issue 已创建或更新。

若事实、必要试验或 Human-owned choice 仍阻断 material shape，保留 best-known 主 Draft、具体 blocker 与下一步 owner；可以交接调查或未受影响的工作，但不能把被阻断部分标为可执行实现 handoff。Draft 足够可实现与本轮委托已完成是两个判断：用户明确要求在本轮完成的原型 / 比较尚未完成时，不能因有了 Draft 就宣布任务完成，或未经授权改成未来工作。缺执行能力时如实报告，用户明确限定为调研 / 中间交接时遵循该范围；不为形成 Draft 强制运行未来产品的全部验收，也不猜测 territory 或代替 Human 承诺。

## 常见错误

- 把 Goal、spec、plan、Taskbook 都做成并行 SOT。
- clear Issue 仍强制经过 compile / Graph。
- 把 `$prototype` 的 artifact 当作新的 authority，而不是 reaction surface。
- 让 AE 的 Program convenience 反向改写 Intent。
- 在 Northstar 内选择 test/Replay/runtime backend 并自行判断 proof sufficiency。
- 把 Issue 切成适配单次 agent context 的细粒度 ticket。
- 把任何 red finding 都当成 Intent 错误；只有 intended change / binding premise 本身被 authoritative Evidence 反证才回流。
