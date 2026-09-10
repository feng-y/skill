---
name: intent-shape
description: "Concrete-shaping specialist for engineering intent that is understood but not concrete enough to commit: expose the decisive Target with the cheapest inspectable Core Path, Usage / Interface Draft, or disposable Prototype before the caller freezes intent or execution."
---

# Intent Shape · 把已理解的 Intent 具体化到可提交

Intent Shape 是 **concrete Target shaping specialist**。当 caller 已经大体恢复 Intent / Human choice，但仅靠 prose 仍可能被解释成 materially different 的核心路径、ownership、boundary、interface 或 usage 时，用最低成本的 concrete representation 把差异变得可观察、可反馈，然后把 correction / Evidence 返回 caller。

调用方继续拥有 binding Intent、canonical Issue / artifact、Human-owned choice 与后续 compile。Intent Shape 不接管完整 Intent research，不决定长期 Target Architecture，不编译执行 Graph，不拆实现任务，也不进入 production implementation。

核心规则：**如果同一份已理解 Intent 仍容许两个 materially different、看起来都合理的 Target，不要先拆任务；先把会改变承诺的差异具体化。**

## 调用边界

适合这些情况：

- migration / refactor / execution optimization 的目标核心路径、ownership、boundary、dataflow 需要先对齐；
- API、CLI、schema、config、workflow 或 interaction 只有看到具体 usage 才能可靠判断；
- Intent / choice 已大体明确，但 Human / caller 仍需要看到目标形态才能给出有效 correction；
- 静态 Draft 不能回答一个 material experiential / empirical decision，需要最小 prototype 直接观察。

不应调用或应立即返回 caller：

- 当前 producer / consumer / runtime path / baseline 等 territory fact 尚未核实时，返回缺失 Evidence；caller 可按需调用 `$unknowns-first`；
- 长期 responsibility、module boundary、dependency direction 或 Target Architecture 本身未定时，返回缺失的结构判断；caller 可按需调用 `$architecture-evolution`；
- Intent 已经足以让 fresh consumer / Executor 在 binding boundary 内开始，剩余差异只是 implementation How；
- trivial / local change 不为“流程完整”额外生成 Draft。

## 输入只保留当前 Decision 所需内容

使用 caller 已经形成的 Intent / choice、binding constraints 与相关 Evidence，不重新做完整 Intent take。先锁定一个 material decision：

> **哪一个仍隐含的 Target 差异，如果理解错了，会改变 intended outcome、核心路径、ownership、binding boundary、interface / usage 或 accepted result？**

没有这样的差异就停止并返回 caller。

若 representation 依赖未核实的 repo/runtime fact，不用假设补全 Target。返回具体缺口及其影响，不把 artifact presence 当成 Evidence。

## 使用最低成本的 Representation

Artifact 是判断手段，不是新的 SOT、审批阶段或必交模板。

### Core Path Draft

核心 execution path、ownership、boundary、dataflow 或旧路径退出是决定性问题时优先使用。已有系统改造通常用 `Current → Target`，只保留 material nodes 和会改变判断的信息。

按需显式展示 ownership、boundary change、removed / collapsed path、必须保持的 invariant，以及真正决定该 Target 是否成立的 Evidence / Verification point。不要加入 file/helper/patch 顺序或完整 implementation plan。

### Usage / Interface Draft

consumer-facing contract、API、CLI、schema、config、workflow 或 interaction 是决定性问题时，从具体 usage / observable behavior 开始。让 Human 能看到“怎么用、会看到什么、承诺了什么”，只展开会改变 contract 的内部 boundary。

### Prototype

只有静态 Draft 仍不足以回答当前 material decision 时才做。Prototype 只回答一个问题，保持 cheap、reversible、disposable；可以是最小交互、mock、throwaway code、timing probe 或其他可体验 artifact。

在与 decision 匹配的 surface 上观察结果。不要为 production quality 补持久化、通用抽象、完整测试、兼容层或 rollout；除非这些本身就是当前 decision 的内容。Prototype 的代码可以丢，得到的 decision / Evidence 应能留下。

## 必要时用同形态对比，而不是扩大流程

当两个或更多 materially different Target 都仍合理、且比较本身能帮助关闭当前 decision 时，用**同一种 representation** 展示最多 2–3 个真正不同的候选，例如两份 Core Path 或两种 Usage。

只比较 decision-relevant 的差异、trade-off、binding impact 与 Evidence。不要为了“探索充分”固定制造候选，也不要替 Human 关闭 Human-owned choice；已有 authority 能裁决时直接收敛。

## 对齐与停止

先交付 artifact 和明确的 decision surface。收到 Human correction 或新 Evidence 后，只重开受影响的 path、boundary、usage 或 prototype，不重做已闭合部分。

只要仍有一个 material ambiguity 会改变 Target，就继续最小 shaping；当剩余差异都属于 Executor How 时停止。Intent Shape 不顺势进入 implementation，也不因为 artifact 看起来可实现就把它升级成 production design。

## 返回 caller

返回足以让调用方继续更新 canonical Issue / Intent judgment / compile 的最小结果：

- 当前 material decision；
- concrete artifact 或候选对比；
- 已接受 / 修正的 Target、ownership、boundary、usage 或 invariant；
- artifact 新产生的 decision-relevant Evidence；
- 仍会改变 Target 的 unresolved point。

不要生成 Taskbook、issue graph、PR split、实现 checklist 或第二份 Intent SOT。调用方消费 correction / Evidence 后决定更新 Drafted Issue、继续 shaping、调用其他 specialist，或进入 execution / compile。

## 常见错误

- 把 Draft 写成另一份 spec / Taskbook，导致对齐工件比 decision 本身更大。
- 看到“中大型需求”就固定 prototype；Core Path 或 Usage 已足够时不要写代码。
- 事实未知时画出完整 Target，把假设伪装成 repo reality。
- Target Architecture 尚未判断时在这里替 AE 做长期结构选择。
- Core Path 尚未对齐就开始 task decomposition，再靠实现结果反推真正目标。
- Human 已 correction 后继续扩大探索，而不是只修改受影响 surface。
- 把 prototype 或 draft 当成 binding approval；最终承诺仍由 Human authority / caller 的 canonical intent owner 决定。
