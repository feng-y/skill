# Progressive Brooks Architecture Constraints

只在 Architecture Intent 的方向已经稳定、需要形成下游设计义务时读取。初始 Ground / Discover 阶段不要加载。

Brooks 在这里是**架构设计约束**，不是独立 Skill、全量扫描器或报告模板。约束按工作成熟度逐步吸收：

```text
Intent → relevant constraints
Target design → constraints become design decisions
Implementation / acceptance → constraints obtain code and test evidence
```

## Level 1 — Intent

只识别与当前 pressure、boundary 和 desired end state 直接相关的约束。把它们写入 Architecture Intent 的 `Progressive design constraints`，不要为了覆盖 R1–R6 而制造无关内容。

每项只写：

```text
Risk → Design constraint → Why applicable → Guard → Proof expected
```

此阶段不输出 severity、finding、PASS/RETRY、Health Score 或完整 Remedy。

## Level 2 — Target design

后续形成目标架构时，把相关约束吸收为明确设计决定：

- constraint 由哪个 contract、module、variation point 或 dependency boundary 承担；
- 哪个旧知识、路径、判断或依赖因此退出；
- 哪个 guard 防止错误统一、过度抽象或机械倒置依赖；
- 什么设计证据可以说明约束被满足。

只有设计范围扩大、风险交叉或证据表明可能遗漏时，才继续展开其他 Brooks 约束。

## Level 3 — Implementation and acceptance

实现与验收阶段使用代码、测试、replay、依赖检查或迁移证据证明约束成立。此时才可以根据实际范围决定是否需要完整 R1–R6 扫描。

## Constraint vocabulary

- `R6 Domain Model Distortion` — 设计必须表达真实业务语义，不能按现有代码形状错误合并 bounded context。
- `R2 Change Propagation` — 共同规则或 variation 的变化应限制在权威位置和明确边界内。
- `R3 Knowledge Duplication` — 同一业务决定、配置解释或路径选择只能有一个权威来源。
- `R4 Accidental Complexity` — 新 abstraction 必须吸收真实变化并替代旧结构，不能只是增加 facade、manager、registry 或 mode flag。
- `R5 Dependency Disorder` — 源码依赖应符合 `policy → contract ← implementation`，底层不能通过 callback、global state 或 registry 反向控制 policy。
- `R1 Cognitive Overload` — capability/module 应隐藏必要复杂度，让 caller 少知道步骤、状态、顺序和实现类型。

## Guards

- 不同 bounded context 的相似规则不自动统一；
- 真实吸收 vendor churn 的 adapter 可以保留；
- composition root 可以知道具体 implementation，但不能承载业务 policy；
- 简单 DTO、边界 record 和清晰线性实现不因“简单”自动成为问题；
- 深模块内部可以复杂，关键是复杂度没有泄漏给 caller；
- 迁移期双轨可以暂时存在，但必须有 authoritative path 和退出条件。

## Boundary

Architecture Evolution 只把相关 Brooks 约束携带到 intent 中，不完成目标设计，也不声称约束已经满足。禁止调用、加载、路由到或依赖任何外部 Brooks / brooks-lint Skill、配置、报告、Health Score 或 workflow。
