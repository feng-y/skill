# Architecture Intent Rules

只在方向仍模糊、需要区分架构 intent 与局部修改时读取。

## Start from pressure

有效 intent 必须能追溯到真实压力：

- 同一业务规则或配置解释反复在多处修改；
- 新需求持续增加特殊入口、mode flag 或 provider/family switch；
- 事故、回归或测试脆弱性集中在同一结构边界；
- 调用者必须知道内部步骤、状态、生命周期或实现类型；
- 一个模块同时承受多个不相关变化；
- 新抽象增加，但旧路径、旧事实源和旧判断仍存在；
- common/core/Harness/Runtime 被具体场景或 provider 牵引。

文件大、函数长、目录不整齐、模式不优雅或单次局部修改，不单独构成架构 intent。

## Architecture or local

只有同时满足以下大部分条件，才形成 architecture intent：

- 压力会重复出现或恢复成本高；
- 一个结构原因造成多个可观察后果；
- 影响跨越单个局部实现，但仍能限定边界；
- 需要重新确定业务语义、责任 owner、稳定 contract 或依赖方向；
- 可以说明完成后什么旧知识、路径、判断或依赖会退出。

否则给出局部修改边界，不升级。

## Four architecture directions

这四个方向必须保留。它们用于构造 intent，而不是要求当前阶段完成目标设计。一个 intent 选择一个 primary direction，其他命中只作为 consequence 或 design obligation。

1. **Business Semantic Integrity**
   - 是否存在同一业务的多套语义或事实解释？
   - 是否可能错误合并不同 bounded context？

2. **Stable Abstraction with Explicit Variation**
   - 调用者是否依赖实现差异而不是业务能力？
   - 哪些差异可能是 essential，哪些只是历史残留？

3. **Cohesive Capability Ownership**
   - 完整 capability、invariant、状态和生命周期是否有 owner？
   - 是否由 caller、helper 和全局对象共同拼装？

4. **Unidirectional Policy Dependency**
   - 稳定 policy 是否被 provider、场景或 implementation 反向定义或控制？
   - 是否存在 `common→scenario`、`policy→provider` 或隐式控制反转？

## Real Evolution gate

Intent 必须指向真实减少，而不是新增一层。至少能提出一个后续需要证明的退出目标：

- 平行业务语义；
- 重复事实解释；
- 调用者内部知识；
- 无效抽象或特殊入口；
- 反向或循环依赖；
- 永久兼容分支。

如果只能说“增加 facade/interface/manager/registry”，intent 尚未成立。

## Challenge the intent

在 ready 前寻找会推翻或缩小方向的反证：

- 问题是否其实是局部修复；
- 是否错误统一不同 bounded context；
- 是否把历史偶然差异永久化；
- 是否诱导 union interface、mode flag、额外 wrapper 或 speculative seam；
- 是否把复杂度转移到 helper、adapter、registry、配置或 caller；
- 是否没有真实 replacement/exit；
- 是否存在代码无法裁决的 Human-owned 业务或兼容决定。

反证成立时修改或撤销 intent；不成立时保留最重要 guard。

## Progressive Brooks constraints

Brooks 是架构设计约束，按成熟度逐步吸收：

```text
Architecture Intent
→ 识别与方向相关的 Brooks constraints
→ Target design 把 constraints 变成设计决定
→ Implementation / acceptance 用代码和测试证明
```

Intent 阶段只识别相关约束：

- `R6 Domain Model Distortion` — intent 与后续设计必须表达真实业务，不能按代码形状错误统一；
- `R2 Change Propagation` — 共同规则和 variation 的变化应收敛到权威位置；
- `R3 Knowledge Duplication` — 同一业务决定和事实解释应只有一个权威来源；
- `R4 Accidental Complexity` — 新 abstraction 必须吸收真实变化并替代旧结构；
- `R5 Dependency Disorder` — 设计应恢复 `policy → contract ← implementation`，并消除隐式反向控制；
- `R1 Cognitive Overload` — capability/module 应让 caller 少知道步骤、状态、顺序和实现类型。

每项相关约束写：

```text
Risk → Design constraint → Why applicable → Guard → Proof expected
```

合理的 bounded context、vendor adapter、composition root、简单 DTO 和深模块内部复杂度都需要应用 guard，不能机械报错。完整规则按需读取 `brooks-constraints.md`。

## Intent quality gate

`Architecture intent ready` 必须满足：

1. 一个明确方向，不是候选列表；
2. 有真实 pressure 和代码证据；
3. 说明为什么是架构问题而不是局部修复；
4. 选择一个 primary architecture direction；
5. desired end state 描述结果，不锁死实现模式；
6. in scope、out of scope 和 must preserve 清楚；
7. 后续设计 obligations 明确；
8. 至少一个可观察的 replacement/exit 目标；
9. 一个关键 Unknown 已关闭，或明确不会阻止 intent；
10. success evidence 可验证；
11. 已检查最重要反例和 guard；
12. 已携带与当前方向相关、需要下游逐步吸收的 Brooks constraints。
