---
name: prototype
description: "Make already-understood engineering intent inspectable before commitment: use the cheapest Core Path, Usage / Interface Draft, or disposable Prototype to expose materially different concrete shapes and return correction / Evidence to the caller."
---

# Prototype · 让 Intent 的具体形态可观察

Prototype 是 **concrete-shaping specialist**。当 Intent 已经大体理解，但仅靠 prose 仍可能被解释成 materially different 的核心路径、ownership、boundary、interface、usage 或 interaction 时，用最低成本的可观察 representation 把差异暴露出来，再把 correction / Evidence 返回 caller。

`Prototype` 不等于一定写代码。Core Path、Usage / Interface Draft、state transition、mock 或 throwaway code 都可以是 prototype surface；选择能关闭当前 material decision 的最便宜形态。

Prototype 不拥有 canonical Intent / Issue，不决定长期 Target Architecture，不编译 execution Graph，不进入 production implementation。

## 调用边界

适合：

- outcome 已理解，但核心 execution path / ownership / boundary 仍可能有两种 materially different 解释；
- API、CLI、schema、config、workflow 或 interaction 只有看到具体 usage 才能可靠判断；
- static draft 不能回答一个 material experiential / empirical decision，需要最小可丢弃实现直接观察。

不应调用或应立即返回 caller：

- producer / consumer / runtime path / baseline 等 territory fact 未核实，且事实不同会改变 shape：交 `$unknowns-first`；
- 长期 responsibility、knowledge ownership、dependency direction 或 Target Architecture 本身未定：交 `$architecture-evolution`；
- 当前 Intent 已经足以让 fresh Executor 在 binding boundary 内开始，剩余差异只是 implementation How；
- trivial / local change 不为流程完整额外生成 artifact。

## 一次只关闭一个 material shape decision

先问：

> **哪一个仍隐含的 concrete difference，如果理解错了，会改变 intended outcome、核心路径、ownership、binding boundary、interface / usage 或 accepted result？**

没有这样的差异就停止。

若 representation 依赖未核实的 repo/runtime fact，不用假设补全；返回具体 Evidence gap 及其 shape impact。

## 选择最低成本的 representation

### Core Path

核心 execution path、ownership、boundary、dataflow 或旧路径退出是决定性问题时使用。已有系统改造通常用紧凑的 `Current → Intended`，只保留 material nodes、boundary change、removed path 与必须保持的 invariant。

### Usage / Interface Draft

consumer-facing API、CLI、schema、config、workflow 或 interaction 是决定性问题时，从具体 usage / observable behavior 开始。只展开会改变 contract 的内部 boundary。

### Disposable Prototype

只有 static representation 仍不足以回答当前 decision 时才写。只回答一个问题，保持 cheap、reversible、disposable；可以是最小交互、mock、throwaway code、timing probe 或其他可体验 artifact。

不要为了 production quality 补持久化、通用抽象、完整测试、兼容层或 rollout，除非这些本身就是当前 decision。

## 候选对比

当 2–3 个 materially different concrete shapes 都仍合理、且比较本身能帮助关闭 decision 时，用**同一种 representation**对比它们。只比较 decision-relevant ownership、boundary、contract、commitment 与 Evidence；不为了探索充分制造候选，也不替 Human 关闭 Human-owned choice。

## 返回 caller

返回最小充分结果：

- 当前 material shape decision；
- concrete representation / candidate contrast；
- 已接受或修正的 path、ownership、boundary、usage、interface 或 invariant；
- 新产生的 decision-relevant Evidence；
- 仍会改变 concrete shape 的 unresolved point。

caller 将 durable correction fold 回 Northstar Intent / Issue，或继续调用 AE / Unknowns。Prototype 不生成 Taskbook、issue graph、PR split、implementation checklist 或第二份 Intent SOT。

## 停止条件

只要仍有 material ambiguity 会改变 concrete intended shape，就继续最小 shaping；当剩余差异都属于 Executor How 时停止。Human correction 只重开受影响 surface，不重做已经闭合的部分。
