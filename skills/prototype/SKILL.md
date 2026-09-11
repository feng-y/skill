---
name: prototype
description: "Caller-neutral model-invoked concrete-shaping specialist: when an already-understood engineering intent, structural judgment, or accepted claim still permits materially different concrete paths, usage, interfaces, or interactions, expose the difference with the cheapest inspectable representation and return correction / Evidence to the caller."
---

# Prototype · 让已理解语义的具体形态可观察

Prototype 是 **caller-neutral、主要由 model 按需调用的 concrete-shaping specialist**。当 caller 已经理解自己负责的语义，但仅靠 prose 仍可能被解释成 materially different 的核心路径、ownership surface、boundary、interface、usage 或 interaction 时，用最低成本的可观察 representation 把差异暴露出来，再把 correction / Evidence 返回**原 caller**。

`Prototype` 不等于一定写代码。Core Path、Usage / Interface Draft、state transition、mock 或 throwaway code 都可以是 prototype surface；选择能关闭当前 material decision 的最便宜形态。

Prototype 不拥有 canonical Intent / Issue，不决定长期 Target Architecture，不定义 verification claim，不编译 execution Graph，也不进入 production implementation。**谁调用 Prototype，谁继续拥有原来的 semantic judgment。**

## 调用模型：model-invoked，不绑定 Northstar

Prototype 通常不是 Human 需要主动选择的入口。Human 提出需求或 correction 后，由当前 semantic owner 判断是否存在 concrete-shape ambiguity，再按需调用 `$prototype`。

典型 caller：

- **Northstar**：Intent 已理解，但 core path / usage / interface 仍有 materially different 解释；
- **Architecture Evolution**：structural question 已经明确，但需要把候选 owner / boundary / dependency 对 consumer path 的具体影响变得可观察，才能完成自己的 Target judgment；
- **Verify**：authoritative claim 已经成立，但真实 usage / path / interaction 的具体形态仍有 materially different 解释，导致无法稳定 observable surface；
- **Unknowns First**：事实已经关闭后，剩下的问题其实不是“事实是什么”，而是 concrete shape 应如何被看见；可以调用 Prototype，再把结果返回原 decision owner；
- **其他 caller**：只要它已经拥有当前 semantic question，且剩余问题确实是 concrete shape，而不是事实、长期 architecture、proof sufficiency 或 implementation How。

Prototype 返回后，不自动转交 Northstar。caller 消费结果并决定是否更新自己的 judgment；只有 durable Intent 改变时才 fold 回 Northstar / Issue，只有长期 structural premise 改变时才回 AE。

## 调用边界

适合：

- outcome / semantic question 已理解，但核心 execution path / ownership surface / boundary 仍可能有两种 materially different 解释；
- API、CLI、schema、config、workflow 或 interaction 只有看到具体 usage 才能可靠判断；
- static draft 不能回答一个 material experiential / empirical decision，需要最小可丢弃实现直接观察。

不应调用或应立即返回 caller：

- producer / consumer / runtime path / baseline 等 territory fact 未核实，且事实不同会改变 shape：交 `$unknowns-first`；
- 长期 responsibility、knowledge ownership、dependency direction 或 Target Architecture 本身未定：交 `$architecture-evolution`；
- completion/safety claim 已明确，剩余问题只是如何证明与 Evidence 是否充分：交 `$verify`；
- 当前 semantic judgment 已经足以让 caller / fresh Executor 继续，剩余差异只是 implementation How；
- trivial / local change 不为流程完整额外生成 artifact。

## 一次只关闭一个 material shape decision

先问：

> **哪一个仍隐含的 concrete difference，如果理解错了，会改变 caller 当前拥有的 outcome、核心路径、ownership surface、binding boundary、interface / usage 或 accepted result？**

没有这样的差异就停止。

若 representation 依赖未核实的 repo/runtime fact，不用假设补全；返回具体 Evidence gap 及其 shape impact。

## 选择最低成本的 representation

### Core Path

核心 execution path、ownership surface、boundary、dataflow 或旧路径退出是决定性问题时使用。已有系统改造通常用紧凑的 `Current → Intended`，只保留 material nodes、boundary change、removed path 与必须保持的 invariant。

### Usage / Interface Draft

consumer-facing API、CLI、schema、config、workflow 或 interaction 是决定性问题时，从具体 usage / observable behavior 开始。只展开会改变 caller judgment 的内部 boundary。

### Disposable Prototype

只有 static representation 仍不足以回答当前 decision 时才写。只回答一个问题，保持 cheap、reversible、disposable；可以是最小交互、mock、throwaway code、timing probe 或其他可体验 artifact。

不要为了 production quality 补持久化、通用抽象、完整测试、兼容层或 rollout，除非这些本身就是当前 decision。

## 候选对比

当 2–3 个 materially different concrete shapes 都仍合理、且比较本身能帮助 caller 关闭 decision 时，用**同一种 representation**对比它们。只比较 decision-relevant ownership surface、boundary、contract、commitment 与 Evidence；不为了探索充分制造候选，也不替 caller / Human 关闭它们拥有的 choice。

## 返回 caller

返回最小充分结果：

- 当前 material shape decision；
- concrete representation / candidate contrast；
- 已观察到的 path、ownership surface、boundary、usage、interface 或 invariant 差异；
- 新产生的 decision-relevant Evidence；
- 仍会改变 concrete shape 的 unresolved point。

**不要替 caller 宣布最终 semantic decision。** caller 根据自己的 owner 职责消费 correction / Evidence：Northstar 更新 Intent，AE 更新 Target judgment，Verify 更新 observable / proof surface，Unknowns First 回到原 decision owner。

Prototype 不生成 Taskbook、issue graph、PR split、implementation checklist、verification workflow 或第二份 Intent SOT。

## 停止条件

只要仍有 material ambiguity 会改变 caller 当前 semantic judgment，就继续最小 shaping；当剩余差异都属于 implementation How、verification mechanics 或已经由 caller 足够判断时停止。Human / caller correction 只重开受影响 surface，不重做已经闭合的部分。
