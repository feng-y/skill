---
name: shape-intent
description: "Use when an engineering intent is understood but not concrete enough to commit: make the decisive target observable with the cheapest useful core-path draft, usage/interface draft, architecture sketch, or disposable prototype before implementation decomposition."
---

# Shape Intent · 把关键意图变成可审查的形状

Shape Intent 是 **concrete shaping specialist**：当 Intent 已经大体理解，但仅靠 prose 仍可能导向 materially different 的核心路径、边界、接口或体验时，用最便宜的 concrete artifact 让差异变得可观察、可反馈。

它不拥有 binding Goal / Human choice，不推导长期 Target Architecture，不编译 Taskbook，也不接管 implementation。被 Northstar 调用时，Northstar 仍是 Intent take / compile 的 canonical owner；被 Architecture Evolution 调用时，AE 仍拥有结构判断；Executor 仍拥有可替换 How。

核心规则：**如果同一段文字仍容许两个 materially different、看起来都“合理”的目标，不要先拆任务；先把决定性差异具体化。**

## 何时使用

适合这些情况：

- 中大型 migration / refactor / execution optimization 的目标核心路径、ownership、boundary 或 dataflow 需要先看清；
- API、CLI、schema、workflow 或 user interaction 只有看到具体 usage 才能可靠判断；
- Human 或 caller 已经知道问题方向，但对目标形态仍难以仅靠文字作出反应；
- 静态讨论已经不能继续降低 decision uncertainty，而一个廉价、可丢弃的 prototype 能直接暴露差异。

不要把它变成固定阶段：

- map 与 repo/runtime territory 仍有事实缺口时，交 `$unknowns-first`；
- 长期 responsibility、module boundary、dependency direction 或 Target Architecture 本身未定时，交 `$architecture-evolution`；
- Intent 已经足以让 fresh Executor 在 binding boundary 内开始，剩余差异只属于 implementation How 时直接返回 caller；
- trivial / local change 不为“流程完整”额外生成 Draft。

## 先找需要被看见的 Decision

开始前只锁定一个当前 material decision：**哪一个差异如果仍被误解，会改变 Goal、核心路径、ownership、binding boundary、interface / usage 或 accepted outcome？**

已有 authority / Evidence 足够时直接使用，不重复调查。若生成 artifact 依赖一个尚未核实的 repo/runtime fact，不猜测 Target；返回该事实缺口，让 caller 用 `$unknowns-first` 关闭或显式保留 dependency。

然后选择能让这个 decision 变得可判断的最小 representation。Artifact 是手段，不是新的 SOT、审批阶段或必交模板。

## 选择最便宜的 Representation

### Core Path Draft

核心 execution path、ownership、boundary、dataflow 或旧路径退出是决定性问题时优先使用。改造已有系统通常用 `Current → Target`，只保留 material nodes 和会改变判断的信息。

按需显式展示：谁拥有关键语义、哪些 boundary 改变、哪些旧路径删除/折叠、哪些 invariants 必须保持、哪些 evidence/verification point 能证明目标成立。不要把 file/helper/patch 顺序或完整 implementation plan 塞进图里。

### Usage / Interface Draft

consumer-facing contract、API、CLI、schema、config 或 workflow 是决定性问题时，从真实或明确标注的示例 usage 开始。让 caller 能看到“如何使用 / 会看到什么 / 哪个 contract 被承诺”，再反推必要 boundary；不为解释实现而展开内部步骤。

### Architecture Sketch

当结构方向已经由 authority、Northstar 或 `$architecture-evolution` 给出，但仍需要把候选 Target / boundary 具体化以便比较或纠正时使用。它负责 **render judgment**，不替 AE 重新决定长期 responsibility 或 dependency direction。

### Prototype

只有 Draft / Sketch 仍不足以回答当前 decision 时才做。Prototype 只回答一个 material question，保持 cheap、reversible、disposable；可以是最小交互、mock、throwaway code 或其他可体验 artifact。

不把 prototype 自动 productionize，不为了“代码质量”补持久化、通用抽象、完整测试、兼容层或 rollout。除非这些本身决定当前问题，否则答案应比 prototype 活得更久。

## 对齐 Loop

先交付 concrete artifact，再暴露 caller 真正需要判断的 decision surface。收到 correction / Evidence 后，只修改受影响的 path、boundary、usage 或 prototype，不重做已经闭合的部分。

如果 caller 指明该 decision 是 Human-owned，就把 artifact 用作 Human reaction surface；否则不要凭空增加审批点。已有 authority 足以关闭的判断可以直接返回 shaped result。

只在新反馈仍可能 materially 改变目标形态时继续 loop；剩余差异都只是 Executor How 时停止 shaping，把控制权还给 caller。

## 返回什么

优先返回 artifact 本身，并只附带当前需要的：

- 它正在暴露的 material decision；
- 已被接受 / 修正的 target、boundary、ownership、usage 或 invariant；
- artifact 新产生的 decision-relevant Evidence；
- 仍会改变目标形态的 unresolved point。

不要在这里生成 Taskbook、issue graph、PR split 或实现 checklist。需要执行时由 Northstar 根据 shaped intent 编译；需要长期架构判断时回 AE；需要 territory proof 时回 Unknowns First。

## 常见错误

- 把 Draft 写成另一份 spec / Taskbook，导致对齐工件比要对齐的问题更大。
- 看到“中大型需求”就固定要求 prototype；静态 Draft 足够时不要写代码。
- 用 prototype 的存在证明 Target 正确；artifact 只能提供 reaction / Evidence，不能替 Human 或 authority 拍板。
- 在 repo reality 未核实时画出貌似完整的 Target，并把假设伪装成事实。
- Core Path 尚未对齐就开始 task decomposition，再靠执行结果反推真正架构。
- Human 已给出明确 correction 后继续扩大探索，而不是只重开受影响 decision。
