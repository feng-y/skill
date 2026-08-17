# Architecture Evolution

Architecture Evolution（AE）用于判断一个长期存在的模块、能力或边界是否值得发生架构变化，并收敛当前范围内最可信的目标结构与下一步演进。

它不是架构审计器，也不是通用重构建议器。看到大文件、重复、复杂目录、历史兼容或一次迁移很困难，并不自动意味着需要改架构。AE 先恢复责任、权威、依赖、通用/特化和信息隐藏，再判断当前现实是否与长期结构发生了值得处理的张力。

运行时语义以 [`SKILL.md`](SKILL.md) 为准；本 README 只解释能力定位和使用方式，不定义第二套规则。

## 什么时候使用

适合这些问题：

- 一个历史模块不断吸收新责任，长期边界已经不清楚；
- 同一类需求反复跨多个 owner、权威来源或验证面修改；
- 当前实现与已有架构意图冲突，但不确定是实现漂移还是旧意图已经过时；
- 通用与特化的边界不稳定，持续出现 provider、registry、switch 或兼容路径；
- 已经知道若干架构 gap，但需要判断哪一刀现在最值得推进；
- 想判断一次重构是否是真正的架构演进，而不是把旧复杂度包进新抽象。

不适合直接使用 AE 的情况：

- 单个 bug、dead code、机械清理；
- 一次性的目录整理或 namespace 迁移；
- 纯实现设计，例如类、接口、文件、配置或测试工具怎么写；
- 目标本身还没有收敛，真正问题是需求 shaping；
- 性能问题还没有 profiling、SLO 或资源证据。

## AE 实际判断什么

AE 的主线可以理解为：

```text
Repo reality
    ↓
Scoped strategic design
    ↓
Architecture or local?
    ↓
Long-term target structure
    ↓
Worth changing now?
    ↓
Highest-leverage evolution
    ↓
≤ 3 architecture improvements
```

### 1. 先恢复长期结构

AE 先判断当前范围内：

- 谁应该拥有相关知识、状态、权威和生命周期；
- 依赖长期应该往哪走；
- 什么语义真正通用，什么差异应该保持特化；
- 调用方需要知道什么，哪些复杂性应该被边界隐藏。

当前代码只证明现实，旧架构文档只证明已有意图。两者都不能直接代替战略设计。

### 2. 再判断是否值得改架构

只有长期责任、依赖、抽象或权威边界真的需要变化，才升级为架构问题。

证据通常来自两类情况：

- 持续、重复或已经明确的未来变化被当前结构放大；
- 当前现实持续偏离最可信的战略设计，并造成理解、切分、修改或验证摩擦。

文件大小、目录形状、代码重复和一次迁移困难，只能触发调查，不能单独证明架构演进有价值。

### 3. 从正确方案中选最高杠杆的一刀

目标结构不是待办清单。现实与目标之间的每个 gap 都只是候选。

当多个方向都符合目标结构时，AE 优先选择能让同类持续或已明确未来变化少跨责任、权威、依赖和验证面的方向，同时要求旧知识、旧权威、旧依赖或旧特殊路径真实退出。

这不等于追求单模块或最少文件。不能通过吞并真实独立责任、复制权威事实或隐藏真实跨边界语义来制造表面局部性。

## 结果可能是什么

一次 AE 不一定产生重构计划。合理结果包括：

- **局部判断**：问题不是架构问题，应留在当前实现范围解决；
- **保持未决**：关键事实或人的业务/兼容/风险决定会改变目标结构；
- **战略设计结论**：目标结构已经更清楚，但当前没有值得立即改 repo 的内容；
- **架构演进方案**：给出不超过 3 个当前最值得推进、能够独立改善结构并让旧结构退出的改进项。

AE 停在架构结果和结构完成条件，不提前规定类、接口、文件、配置、MR 拆分或具体测试工具。

## 与其他 Skill 的关系

- **Northstar / Prompt Atlas**：负责把人的目标收敛成高质量执行契约；当问题本身是长期结构判断时，可把架构部分交给 AE。
- **Unknowns First**：适合在真正阻塞判断的事实还不清楚时缩小未知；AE 自己只保留会改变架构判断的关键未知。
- **实现者 / Executor**：AE 给出结构结果，实现者决定具体代码和迁移方式。

## 快速开始

最小调用：

```text
Use $architecture-evolution on <module-or-capability>.
Given its current pressure and repo reality, decide the long-term structure and the highest-value architecture improvements worth advancing now.
```

更好的输入不是“请重构这个目录”，而是给出：

```text
Area: <模块或能力>
Pressure: <真实工程摩擦、重复变化或已明确未来要求>
Known constraints: <业务、兼容、部署、性能等已绑定约束>
Question: <你希望 AE 判断的架构问题>
```

完整操作方式见 [`OPERATIONS.md`](OPERATIONS.md)。

## 权威来源

- [`SKILL.md`](SKILL.md)：正常 runtime 的权威语义；
- [`references/strategic-design.md`](references/strategic-design.md)：目标结构不清时的战略设计；
- [`references/rules.md`](references/rules.md)：难判时的少量 discriminator；
- [`references/legacy-lenses.md`](references/legacy-lenses.md)：旧身份、兼容和权威退出；
- [`references/brooks-constraints.md`](references/brooks-constraints.md)：复杂度仍可疑时的反证；
- [`references/validation.md`](references/validation.md)：只用于显式 smoke/eval，不进入正常 runtime。
