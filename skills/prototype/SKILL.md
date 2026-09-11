---
name: prototype
description: "Caller-neutral engineering prototyping: when an Intent exists, develop its single core Prototype, with views and experiments supporting that whole. For standalone requests, serve the original caller without inventing an Intent; never own acceptance, Architecture, proof judgment, or production implementation."
---

# Prototype · 让已理解语义的具体形态可观察

Prototype 是 **caller-neutral、主要由 model 按需调用的 concrete-shaping specialist**。当 caller 已经理解自己负责的语义，但核心路径、ownership surface、boundary、interface、usage 或 interaction 仍隐含、断裂或存在 material ambiguity，妨碍当前判断时，用最低成本的可观察 representation 把差异暴露出来，再把 correction / Evidence 返回**原 caller**。

`Prototype` 不等于一定写代码，也不等于交互 HTML。Core Path、Usage / Interface Draft、state transition、mock 或 throwaway code 都可以是 prototype surface；选择的是**能够回答当前 material decision 的最低成本表示 / 试验**，不是最便宜或最容易展示的 artifact。

Prototype 不拥有 canonical Intent / Issue，不决定长期 Target Architecture，不定义 verification claim，不编译 execution Graph，也不进入 production implementation。**谁调用 Prototype，谁继续拥有原来的 semantic judgment。**

## 调用模型：model-invoked，不绑定 Northstar

Prototype 通常不是 Human 需要主动选择的入口。当前 semantic owner 在需要展开连贯形态、通过试验决定形态，或已有明确的可丢弃试验委托时按需调用 `$prototype`；直接委托本身不要求再制造 shape ambiguity。

典型 caller：

- **Northstar**：建立或修正这个 Intent 的同一个主 Prototype，使 Human 能看见并澄清 / 确认核心形态；选型或明确实做需要的试验支撑它，而不是另开 Prototype；
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

## 一个 Intent 只有一个主 Prototype

主 Prototype 是本轮 intended change 的整体核心形态，不是一次调用、一个局部 decision 或单项试验。关联同一个 Intent 的调用都从现有主 Prototype、主 Draft 与 caller / Human correction 出发，修正同一个核心对象；尚未建立时先形成能呈现核心方案的 best-known 形态，未决部分如实标出。

视图、局部 code spike、benchmark、baseline 对照和迭代版本都只是这个主 Prototype 的组成或支撑，不能各自成为并行 Prototype。局部展开要说明它如何连回整体路径与已有边界；若整个核心路径尚未呈现，不能把局部生命周期演示或一组实验当作主 Prototype 已完成。独立 Intent 可以各有一个主 Prototype；独立 AE / Verify 或实验委托仍返回原 caller，不为此制造新的 Intent。

先判断：**Human / caller 能否从这一个主 Prototype 看见本轮真正要改成什么样，并针对它提出修正？** 只改受影响部分、保留仍成立的整体关系，不重新生成多个替代主件，也不为了整体性穷尽实现细节。待 Human 确认的选择保持明确，Prototype 不代替 Northstar ask Human，不把可演示或可运行当作预期已确认。

没有核心形态缺口且没有待完成的明确试验委托时，直接返回现有结果。试验所需现状身份或 binding fact 未核实时，先关闭该事实或报告 gap；试验本身要回答的可行性 / 成本未知不是拒绝试验的理由。长期 owner、accepted outcome 与 proof sufficiency 仍归各自 owner；完整的核心形态不扩大 Prototype 的决策权。

## 选择最低成本的 representation

### Core Path

核心 execution path、ownership surface、boundary、dataflow 或旧路径退出是决定性问题时使用。已有系统改造通常用紧凑的 `Current → Intended`，只保留 material nodes、boundary change、removed path 与必须保持的 invariant。

### Usage / Interface Draft

consumer-facing API、CLI、schema、config、workflow 或 interaction 是决定性问题时，从具体 usage / observable behavior 开始。只展开会改变 caller judgment 的内部 boundary。

### Disposable Prototype

当选择取决于实际运行的可行性、行为差异或成本时，static representation 不足以关闭问题；用户明确委托本轮实做时，也不能用图或计划代替。围绕当前 decisive uncertainty 生成并运行最小、可丢弃的目标语言 code spike / timing probe，或复用已有可执行实验。若待决问题只是形态、用法或交互理解，静态或交互表示可能已经充分。

不要为了 production quality 补持久化、通用抽象、完整测试、兼容层或 rollout；但回答当前问题所必需的行为 / 等价性检查与 baseline/treatment 测量不能省略。Prototype 提供试验 artifact 与实际 observation，proof obligation 与 Evidence 是否足以支持可行性、等价性或性能 claim 由 `$verify` 判断；试验收益不等于生产收益。代码存在、HTML 可点击或展示完整不构成这类证明，不能把仍会影响形态选择的实测降格为以后再做的 verification mechanics。

## 候选对比

候选对比用于修正同一个主 Prototype，不产生多个并行主 Prototype。只比较能改变当前选择的差异，使用可比的 representation / 输入条件；已明确委托的对照或试验不因展示数量而静默丢弃。区分当前形态、待确认差异与淘汰解释，不把对比表当作最终核心方案，也不替 caller / Human 采用方案。

## 返回 caller

返回最小充分结果：

- 关联 Intent 时，同一个主 Prototype 的当前核心形态，以及本次修正如何融入它；独立委托则返回 caller 所需结果，不制造完整 Intent；
- 必要的局部视图 / 对照 / 试验，明确它们支撑核心方案的哪一部分，不把它们交成多个 Prototype；
- 已观察到的 path、ownership surface、boundary、usage、interface 或 invariant 差异；
- 新产生的 decision-relevant Evidence；实做试验需区分实际执行与未执行，保留可复现入口、输入 / 配置身份及观察结果的引用；
- 仍会改变 concrete shape 的 unresolved point。

**不要替 caller 宣布最终 semantic decision。** caller 根据自己的 owner 职责消费 correction / Evidence：Northstar 更新 Intent，AE 更新 Target judgment，Verify 更新 observable / proof surface，Unknowns First 回到原 decision owner。

已有 Intent 时，Northstar 围绕这个主 Prototype 完成必要的 Human 澄清 / 确认，并同步主 Draft；局部支持材料不成为第二套方案。AE / Verify 的独立调用仍返回原 caller，不因此创建 Intent 或强制经过 Northstar。

Prototype 不生成 Taskbook、issue graph、PR split、implementation checklist、verification workflow 或第二份 Intent SOT。

## 停止条件

完成被委托的修正或实做后，连同它在同一个主 Prototype 中的位置与观察结果交回 caller。局部委托完成不等于整个主 Prototype 或 Intent 已收敛；关联 Intent 的 Human 预期尚待澄清 / 确认时由 Northstar 处理；独立委托保持原 caller，不代替 Human 回答。结果可以支持采用、淘汰、修正，也可以不足以判断，不强制正收益或无限试验。局部演示、未运行代码不替代约定实做；真实 blocker 如实返回。caller 保留采用与整合，Verify 保留 proof 判断。
