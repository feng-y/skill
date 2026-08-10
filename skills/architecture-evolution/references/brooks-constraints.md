# Progressive Brooks Architecture Constraints

只在 Architecture Intent 的方向已经基本稳定、需要挑战其是否会把复杂度转移、错误统一语义或扩大 ownership 时读取。初始 Ground / Discover 阶段不要加载。

Brooks 在这里是**内部架构 challenge 约束**，不是最终 Architecture Intent 的 section、独立 Skill、全量扫描器或报告模板。约束按工作成熟度逐步吸收：

```text
Architecture Evolution → relevant constraints challenge intent / target identity
Target design → constraints become design decisions
Implementation / acceptance → constraints obtain code and test evidence
```

## Level 1 — Architecture Intent

只识别与当前 pressure、boundary、desired end state 和 possible target identity 直接相关的 Brooks 风险，用它们回答：

- 这个 intent 是否只是把复杂度搬到别处；
- caller / consumer knowledge 是否真的下降；
- 是否把不同 bounded context 错误统一；
- ownership 是否扩大到 evidence 不支持的 execution / orchestration 或相邻 subsystem；
- 新 abstraction 是否有真实 replacement / exit；
- dependency direction 是否变得更稳定而非更隐蔽。

challenge 的结果只能有三种：

1. **reject** — 候选 intent / target identity 不成立；
2. **narrow** — 缩小 intent、owner scope、variation 或 boundary；
3. **guard** — intent 保留，但把会改变其含义的限制用普通架构语言沉淀到 Direction / Boundary / Must preserve / Replacement。

不要把 Brooks 编号、风险表、proof expectation、PASS/RETRY、Health Score 或 challenge 过程写入最终 Architecture Intent。约束数量本身也不是质量信号：只使用有当前 evidence 的约束，不为了覆盖 R1–R6 而机械补齐。

## Level 2 — Target design

后续形成目标架构时，才把相关约束物化为明确设计决定：

- constraint 由哪个 contract、module、variation point 或 dependency boundary 承担；
- 哪个旧知识、路径、判断或依赖因此退出；
- 哪个 guard 防止错误统一、过度抽象或机械倒置依赖；
- 什么设计证据可以说明约束被满足。

这些问题属于 Target Design，不属于 Architecture Evolution。Architecture Intent 可以指出少量 target identity，但不能提前回答上述 responsibility placement。

## Level 3 — Implementation and acceptance

实现与验收阶段使用代码、测试、replay、依赖检查或迁移证据证明约束成立。此时才可以根据实际范围决定是否需要完整 R1–R6 扫描。

## Constraint vocabulary

- `R6 Domain Model Distortion` — 设计必须表达真实业务语义，不能按现有代码形状错误合并 bounded context。
- `R2 Change Propagation` — 共同规则或 variation 的变化应限制在权威位置和明确边界内。
- `R3 Knowledge Duplication` — 同一业务决定、配置解释或路径选择只能有一个权威来源。
- `R4 Accidental Complexity` — 新 abstraction 必须吸收真实变化并替代旧结构，不能只是增加 facade、manager、registry 或 mode flag。
- `R5 Dependency Disorder` — 源码依赖应符合 `policy → contract ← implementation`，底层不能通过 callback、global state 或 registry 反向控制 policy。
- `R1 Cognitive Overload` — capability/module 应隐藏必要复杂度，让 caller 少知道步骤、状态、顺序和实现类型。

## Proof vocabulary for downstream work

下面的 proof 只帮助 Architecture Evolution 判断一个候选是否只是口号；真正的 proof obligation 属于后续 Target Design / Implementation / Acceptance，不进入 Intent 输出。

| Proof | What later evidence should establish |
| --- | --- |
| Ownership closure | fact/state 对 owner 私有、lifetime 正确、consumer 经稳定 boundary 使用、无 sidecar truth；有 generation 时不混用；不要求把相邻 subsystem 的合法 ownership 一并集中 |
| Mechanical boundary | dependency/construction/publication/ownership guard 在适用时可以实际 fail；不能机械表达时允许 evidence-based guard，不新增形式化基础设施 |
| Stable public test surface | 重要 invariant 可从 public capability behavior 验证，不依赖 private-field、friend access、内部 load-order 或具体 implementation 形状 |
| Complexity relocation | duplicated policy/fact、consumer reassembly、distributed lifecycle/publication knowledge、sidecar truth 或 reverse-control burden 至少一项真实下降，而非只移动位置或减少 LOC |

字段换位置、getter 换名字、manager 包一层、helper/adapter 吸收热点 LOC，都不单独构成上述 proof。

## Guards

- 不同 bounded context 的相似规则不自动统一；
- 真实吸收 vendor churn 的 adapter 可以保留；
- composition root 可以知道具体 implementation，但不能承载业务 policy；
- capability ownership 不自动包含 request execution / orchestration ownership；
- 相邻 subsystem 已有正确 authoritative owner 时，优先稳定 contract/relation，而不是为“闭合”集中全部资源；
- 简单 DTO、边界 record 和清晰线性实现不因“简单”自动成为问题；
- 深模块内部可以复杂，关键是复杂度没有泄漏给 caller；
- 迁移期双轨可以暂时存在，但必须有 authoritative path 和退出条件。

## Boundary

Architecture Evolution 只使用相关 Brooks 约束来 challenge、reject、narrow 或 guard 当前 intent / target identity，不输出 Brooks table，也不声称约束已经满足。禁止调用、加载、路由到或依赖任何外部 Brooks / brooks-lint Skill、配置、报告、Health Score 或 workflow。
