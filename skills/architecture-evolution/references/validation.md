# Evaluate Architecture Intent

本文件只用于显式 smoke/eval，正常运行禁止读取。

## Static smoke

检查：

- 主目标是构造 Architecture Intent，不是完成目标设计或实现；
- 主流程为 `Ground → Discover → Shape → Challenge and constrain`；
- 运行时引用为 `rules.md`、`brooks-constraints.md` 和 `intent-contract.md`；
- 四个方向完整保留：Business Semantic Integrity、Stable Abstraction with Explicit Variation、Cohesive Capability Ownership、Unidirectional Policy Dependency；
- 一个 intent 只选择一个 primary architecture direction，其他命中作为 consequence 或 design obligation；
- `Real Evolution` 要求至少一个旧路径、重复知识、caller knowledge、无效抽象、兼容分支或反向依赖退出；
- Challenge 检查 local escalation、false unification、historical difference lock-in、speculative abstraction、complexity relocation 和 replacement reality；
- Brooks R1–R6 被保留为下游架构设计逐步吸收的约束，不被降级为可选提示；
- intent 阶段只携带相关 Brooks constraints，不做全量扫描、Severity、PASS/RETRY、Health Score 或完整报告；
- `brooks-constraints.md` 只在 intent 方向稳定后加载；
- 不存在 Design ready、Architecture Design Contract 或 Northstar handoff；
- 输出只有 `No architecture intent / Intent unresolved / Architecture intent ready`；
- intent contract 描述 outcome、boundary、design obligations、progressive constraints、unknown 和 success evidence，不提前编译实现步骤；
- 不调用外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill。

## Scenario smoke

### P1 — Business semantics direction

用户说历史模块中两条路径长期重复修改，但不确定应合并还是保留。

通过：

- primary direction 为 Business Semantic Integrity；
- intent 说明应统一哪些业务语义、保留哪些 bounded-context 或 essential differences；
- 相关 Brooks constraints 至少包含 R6，并按证据决定是否携带 R2/R3；
- 不提前决定具体 interface。

### P2 — Stable abstraction direction

调用者持续按 provider/family switch，公共接口充满 mode flag 和 optional 参数。

通过：

- primary direction 为 Stable Abstraction with Explicit Variation；
- intent 指向调用者依赖业务能力、真实差异进入明确 variation；
- 相关 constraints 至少包含 R4，并按证据决定是否携带 R2/R3；
- 不能只输出“新增 interface/manager”。

### P3 — Cohesive ownership direction

完整能力由 caller、helper、global state 和多个生命周期对象共同拼装。

通过：

- primary direction 为 Cohesive Capability Ownership；
- intent 要求后续设计确定 capability、invariant、状态和生命周期 owner；
- 相关 constraints 至少包含 R1，并按证据决定是否携带 R2/R4；
- 不机械拆成 one-module-per-concern。

### P4 — Dependency direction

稳定 core/Harness/Runtime 被 provider 和具体场景持续牵引，底层通过 callback 或 registry 控制上层路由。

通过：

- primary direction 为 Unidirectional Policy Dependency；
- intent 指向恢复 `policy → contract ← implementation`，并同时处理源码依赖和隐式控制；
- 相关 constraints 至少包含 R5，并按证据决定是否携带 R2；
- composition-root guard 正确应用。

### P5 — Fuzzy module direction

用户只说“这个历史模块边界混乱，下一步应该怎么演进”。代码显示重复业务判断、caller 拼装顺序和多次兼容分支修改。

通过：形成一个 intent，说明 why now、desired end state、primary direction、boundary、design obligations、progressive constraints 和退出目标；不直接输出 class 拆分方案。

### P6 — Multiple symptoms, one intent

用户列出抽象泄漏、模块过大、反向依赖和测试脆弱。

通过：找到能解释主要压力的一个 primary direction；其他症状作为 consequence、constraint 或 out of scope，不并列输出多个改造项目。

### B1 — Progressive Brooks absorption

Architecture Intent 已稳定，主要问题是平行业务语义和重复配置解释。

通过：

- intent 只携带直接相关的 R6/R3，必要时携带 R2；
- 每项使用 `Risk → Design constraint → Why applicable → Guard → Proof expected`；
- 不为覆盖 R1–R6 添加无关 constraint；
- 明确目标设计负责把 constraint 变成设计决定，实现/验收负责取得证据。

### B2 — Constraint expansion later

目标设计阶段发现 composition 和 runtime control 引入新的依赖风险。

通过：允许下游继续吸收 R5；Architecture Intent 不需要事先机械预测全部风险，也不因此被判定失败。

### N1 — Local fix

问题只是 off-by-one、日志字段或机械迁移。

通过：`No architecture intent`；输出局部边界，不发明架构方向或 Brooks constraints。

### N2 — No real pressure

代码不够优雅，但没有重复变化、事故、caller friction 或明确业务需求。

通过：`No architecture intent`；不得从审美和模式偏好发明 intent。

### N3 — Design already clear

用户已经给出目标 contract、模块边界、迁移步骤和验收标准。

通过：说明本 Skill 不适用；不重复重构明确 intent。

### R1 — Evidence missing

存在多个可能方向，但无法确认消费者、变化频率或业务等价性。

通过：`Intent unresolved`；只保留一个会改变 intent 的 Unknown 和最小探针，不提前携带猜测性的 constraints。

### R2 — Human decision

某兼容行为是长期业务 contract 还是迁移残留，代码无法裁决。

通过：`Intent unresolved`；标明需要 Human 决定及其影响，不伪造方向或退出承诺。

### G1 — False architecture escalation

大函数和目录结构看起来差，但压力来自一个局部错误。

通过：challenge 后撤销 architecture intent。

### G2 — False unification

两条相似路径属于不同 bounded context。

通过：intent 不要求业务统一；记录 bounded-context guard，R6 不产生机械统一约束。

### G3 — Speculative abstraction

候选 intent 只能描述“新增 interface/manager”，无法说明什么旧知识或路径退出。

通过：intent 不 ready；返回 unresolved 或 no intent。

### G4 — Legitimate adapter and composition root

vendor adapter 吸收真实外部变化，composition root 只做 wiring。

通过：R4/R5 guard 正确应用，不为了“吸收 Brooks”而删除合理边界。

## Paired behavioral eval

同一模型、repo snapshot 和预算：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 `0–2`：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Pressure grounding | 审美判断 | 部分 evidence | 真实 pressure、consequence 和 boundary 清楚 |
| Intent discovery | 罗列症状/方案 | 有方向但不稳定 | 一个能解释压力的 architecture intent |
| Direction judgment | 未分类或多方向并推 | 方向大致正确 | 一个 primary direction，其他命中正确降为 consequence/obligation |
| Intent quality | 模式或任务列表 | outcome 部分清楚 | why now/end state/boundary/obligations 完整 |
| Progressive constraints | 无 Brooks 或机械全扫 | 有相关 constraint 但边界含糊 | 相关约束准确、guard 和 proof expected 清楚，可供下游逐步吸收 |
| Unknown control | 猜测或发散 | 有 unknown | 一个关键 unknown + 最小关闭方式 |
| Challenge quality | 自我确认 | 检查有限 | 主动检查 false unification/speculation/exit/guards |
| Scope control | 多方向并推 | 大体受控 | 一个 intent，不提前设计或实现 |
| Status judgment | 状态错误 | 正确但冗长 | 正确且最小充分 |

## V0 pass gate

1. P1–P6 中 B 臂的 `Intent discovery + Direction judgment + Intent quality` 比 A 臂高至少 2 分；
2. B1–B2 中 Brooks constraints 被正确渐进吸收，既不丢失也不机械全扫；
3. N1–N3、R1–R2、G1–G4 路由和 guards 正确；
4. 每个 ready 输出只有一个 intent 和一个 primary direction；
5. intent 描述 outcome，不锁死实现模式；
6. 至少一个具体 replacement/exit obligation；
7. 相关 Brooks constraints 有 Design constraint、Why applicable、Guard 和 Proof expected；
8. 未形成目标设计时，不声称 constraint 已满足、行为等价、迁移完成或维护成本下降；
9. 不调用外部 Skill，不生成完整 Brooks 报告或 Health Score。

## Failure classes

- `pressure-free-intent` — 从审美发明方向；
- `local-escalation` — 局部问题被升级成架构 intent；
- `intent-sprawl` — 多个方向同时推进；
- `direction-loss` — 四个方向之一被删除、弱化或无法表达；
- `solution-first` — 先定模式再寻找问题；
- `false-unification` — 错误合并不同业务；
- `historical-difference-lock-in` — 把偶然差异永久化；
- `speculative-intent` — 只能新增抽象，不能说明退出目标；
- `brooks-loss` — Brooks 被降成可选提示，未进入 design obligations；
- `brooks-frontload` — intent 阶段机械展开 R1–R6、Severity 或 PASS/RETRY；
- `guard-miss` — 合理 bounded context、adapter、composition root 或深模块被误报；
- `unknown-swallowed` — 关键未知被猜测填补；
- `premature-design` — intent 阶段输出完整设计或实现步骤；
- `status-leakage` — 非 ready 状态输出稳定 intent。

Static/scenario smoke 只证明文本机制一致；paired eval 才能衡量冻结样本上的相对收益。
