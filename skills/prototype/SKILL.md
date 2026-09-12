---
name: prototype
description: "A caller-neutral tool for solving a concrete engineering problem with an inspectable prototype and draft, or a delegated disposable experiment. Outputs can be composed by the caller; do not own overall Intent, Architecture, proof judgment, or production implementation."
---

# Prototype · 解决具体问题，产出可组合的原型与 draft

Prototype 是 **caller-neutral、主要由 model 按需调用的工程原型工具**。围绕一个已理解的具体问题，产出可观察的原型及描述其 intended shape 的 draft；也可受托将已有部分组合呈现。产物可以由 caller 与其他原型 / draft 继续组合，而不是天然等于整个 Intent 的唯一原型。

`Prototype` 不等于一定写代码，也不等于交互 HTML。Core Path、Usage / Interface Draft、state transition、mock 或 throwaway code 都可以是 prototype surface；选择的是**能够回答当前 material decision 的最低成本表示 / 试验**，不是最便宜或最容易展示的 artifact。

Prototype 不拥有 canonical Intent / Issue，不决定长期 Target Architecture，不定义 verification claim，不编译 execution Graph，也不进入 production implementation。**谁调用 Prototype，谁继续拥有原来的 semantic judgment。**

## 调用模型：model-invoked，不绑定 Northstar

Prototype 通常不是 Human 需要主动选择的入口。当前 semantic owner 在需要展开连贯形态、通过试验决定形态，或已有明确的可丢弃试验委托时按需调用 `$prototype`；直接委托本身不要求再制造 shape ambiguity。

典型 caller：

- **Northstar**：针对 Intent 中一个需要具体化的问题产出原型与局部 draft，或组合已有部分呈现完整路径；Northstar 负责与原始 Intent 对齐、Human 澄清确认和主 Draft 整合；
- **Architecture Evolution**：structural question 已经明确，但需要把候选 owner / boundary / dependency 对 consumer path 的具体影响变得可观察，才能完成自己的 Target judgment；
- **Verify**：authoritative claim 已经成立，但真实 usage / path / interaction 的具体形态仍有 materially different 解释，导致无法稳定 observable surface；
- **Unknowns First**：事实已经关闭后，剩下的问题其实不是“事实是什么”，而是 concrete shape 应如何被看见；可以调用 Prototype，再把结果返回原 decision owner；
- **其他 caller**：已理解问题且需要 concrete surface 或明确委托可丢弃试验；不借此转移事实、长期 Architecture、proof judgment 或生产 implementation 的责任。

Prototype 返回后，不自动转交 Northstar。caller 消费结果并决定是否更新自己的 judgment；只有 durable Intent 改变时才 fold 回 Northstar / Issue，只有长期 structural premise 改变时才回 AE。

## 调用边界

适合：

- outcome / semantic question 已理解，但核心 execution path / ownership surface / boundary 仍有会改变 caller judgment 的缺口；不要求先凑出两种候选；
- API、CLI、schema、config、workflow 或 interaction 只有看到具体 usage 才能可靠判断；
- 选型依赖运行观察，或 caller / Human 明确要求完成可丢弃代码试验；形态已明确不取消这项委托。

不应调用或应立即返回 caller：

- producer / consumer / runtime path / baseline 等 territory fact 未核实，且事实不同会改变 shape：交 `$unknowns-first`；
- 长期 responsibility、knowledge ownership、dependency direction 或 Target Architecture 本身未定：交 `$architecture-evolution`；
- 已有真实 artifact / backend，剩余只需定义证明或判读 Evidence，不需构造试验形态：交 `$verify`；被 Verify 委托构造可丢弃试验时，完成 artifact / observation 后交回 Verify，不因它拥有 proof 判断就退回未做的委托；
- 没有待完成的明确试验委托，当前形态已足够且余下只是生产 implementation How 时，直接返回；trivial / local change 不为流程完整额外生成 artifact。

## 围绕一个问题产出可组合结果

一个问题是能连贯讨论和判断的工程问题，不是机械地只许回答一个字段或一个 decision，也不要求每次承包整个 Intent。共同决定该问题的路径、dataflow、boundary 或 lifecycle 一起展开；简单 Intent 可以一次覆盖，复杂 Intent 可以产生多个局部原型与 draft，之后组合为完整原型。

向 caller 交代本产物解决什么、依赖什么、覆盖到哪里，以及组合会用到的输入输出、约束和未决关系；按问题保留必要内容，不强制 schema、框架或第二份文档。受托组合时实际接通各部分并暴露相接处的冲突和缺口，不把文件索引或多个局部演示称为完整原型。局部试验通过也不证明整体兼容或整体 Acceptance。

问题过大或无法在原约束下组合时，返回具体范围与取舍建议；关联 Intent 的收窄由 Northstar ask Human 处理，不能自行丢掉要求来宣布完成。caller 仍拥有采用与整体整合；新的长期结构选择归 AE，proof 判断归 Verify。直接调用不要求先建立 Northstar Intent。

没有待解决的具体形态问题且没有明确试验委托时，直接返回现有结果。试验所需现状身份或 binding fact 未核实时先关闭或报告 gap；试验要回答的可行性 / 成本未知不是拒绝试验的理由。只修正受影响部分，不为完整感重做已成立的结果或扩大决策权。

## 选择最低成本的 representation

### Core Path

核心 execution path、ownership surface、boundary、dataflow 或旧路径退出是决定性问题时使用。已有系统改造通常用紧凑的 `Current → Intended`，只保留 material nodes、boundary change、removed path 与必须保持的 invariant。

### Usage / Interface Draft

consumer-facing API、CLI、schema、config、workflow 或 interaction 是决定性问题时，从具体 usage / observable behavior 开始。只展开会改变 caller judgment 的内部 boundary。

### Disposable Prototype

当选择取决于实际运行的可行性、行为差异或成本时，static representation 不足以关闭问题；用户明确委托本轮实做时，也不能用图或计划代替。围绕当前 decisive uncertainty 生成并运行最小、可丢弃的目标语言 code spike / timing probe，或复用已有可执行实验。若待决问题只是形态、用法或交互理解，静态或交互表示可能已经充分。

不要为了 production quality 补持久化、通用抽象、完整测试、兼容层或 rollout；但回答当前问题所必需的行为 / 等价性检查与 baseline/treatment 测量不能省略。Prototype 提供试验 artifact 与实际 observation，proof obligation 与 Evidence 是否足以支持可行性、等价性或性能 claim 由 `$verify` 判断；试验收益不等于生产收益。代码存在、HTML 可点击或展示完整不构成这类证明，不能把仍会影响形态选择的实测降格为以后再做的 verification mechanics。

## 候选对比

候选原型 / draft 可以是替代方案，也可以是可组合部分，必须区分二者；相互排斥的候选不能仅为完整而强行拼接。只比较或组合能改变当前判断的部分，使用可比的 representation / 输入条件。明确委托的工作不因展示数量而静默丢弃；区分当前候选、未决关系与淘汰解释，不把对比表当作已采用的整体方案，也不替 caller / Human 接受范围变化。

## 返回 caller

返回最小充分结果：

- 当前问题对应的原型与 draft，或本次受托组合后的完整路径；原型可以直接承载 draft，不要求两个文件；
- 适用范围、必要的相接关系、对照或试验，以及与 caller 已给定 Intent / 约束的关系；
- 已观察到的 path、ownership surface、boundary、usage、interface 或 invariant 差异；
- 新产生的 decision-relevant Evidence；实做试验需区分实际执行与未执行，保留可复现入口、输入 / 配置身份及观察结果的引用；
- 仍会改变 concrete shape 的 unresolved point。

**不要替 caller 宣布最终 semantic decision。** caller 根据自己的 owner 职责消费 correction / Evidence：Northstar 更新 Intent，AE 更新 Target judgment，Verify 更新 observable / proof surface，Unknowns First 回到原 decision owner。

已有 Intent 时，Northstar 组合采用的局部原型 / draft，检查原始需求覆盖，并通过必要的 Human 澄清 / 确认收敛主 Draft。Prototype 提供具体产物，不接管整体 Intent。AE / Verify 的独立调用仍返回原 caller，不因此创建 Intent 或强制经过 Northstar。

Prototype 不生成 Taskbook、issue graph、PR split、implementation checklist、verification workflow 或第二份 Intent SOT。

## 停止条件

完成被委托问题的原型 / draft、组合或实做后，连同覆盖范围、观察结果与未决关系交回 caller。局部完成不等于整体 Intent 已覆盖；必要的 Human 范围和取舍决定仍归原 caller / Northstar 处理。结果可以支持组合、采用、淘汰、修正，也可以不足以判断，不强制正收益或无限试验。局部演示、未运行代码不替代约定实做；真实 blocker 如实返回。caller 保留整体采用与整合，Verify 保留 proof 判断。
