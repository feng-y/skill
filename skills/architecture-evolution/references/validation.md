# Evaluate Architecture Intent

本文件只用于显式 smoke/eval，正常运行禁止读取。

## Static smoke

检查：

- 主目标是构造 Architecture Intent，不是完成目标设计或实现；
- 主流程只有 `Ground → Discover → Shape → Challenge`；
- 运行时引用仅为 `rules.md` 和 `intent-contract.md`；
- 不存在 Design ready、Architecture Design Contract、Brooks 全量扫描、Health Score 或 Northstar handoff；
- Brooks R1–R6 只作为 intent challenge 的风险提问；
- 输出只有 `No architecture intent / Intent unresolved / Architecture intent ready`；
- intent contract 描述 outcome、boundary、obligations、unknown 和 success evidence，不提前编译实现步骤；
- 不调用外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill。

## Scenario smoke

### P1 — Fuzzy module direction

用户说“这个历史模块边界混乱，下一步应该怎么演进”。代码显示重复业务判断、caller 拼装顺序和多次兼容分支修改。

通过：形成一个 intent，说明 desired end state、为什么是架构问题、必须回答的 ownership/semantic 问题和退出目标；不直接输出 class 拆分方案。

### P2 — Multiple symptoms, one intent

用户列出抽象泄漏、模块过大、反向依赖和测试脆弱。

通过：找到能解释主要压力的一个方向；其他症状作为 consequence 或 out of scope，不并列输出多个改造项目。

### P3 — Known hotspot, unclear direction

用户指出 FeatureStreaming 与 Predict 存在平行 ParseRequest 路径，但不确定是合并、适配还是保留差异。

通过：恢复同一业务判断和 essential difference 的关键 evidence，形成“应统一什么、必须保留什么”的 intent obligations；不提前决定具体接口。

### P4 — Architecture intent with dependency pressure

稳定 core 被 provider 和具体场景持续牵引。

通过：intent 指向恢复 policy/contract/implementation 边界，并要求至少一条反向知识或依赖退出；不要求在本阶段给出完整模块图。

### N1 — Local fix

问题只是 off-by-one、日志字段或机械迁移。

通过：`No architecture intent`；输出局部边界，不发明架构方向。

### N2 — No real pressure

代码不够优雅，但没有重复变化、事故、caller friction 或明确业务需求。

通过：`No architecture intent`；不得从审美和模式偏好发明 intent。

### N3 — Design already clear

用户已经给出目标 contract、模块边界、迁移步骤和验收标准。

通过：说明本 Skill 不适用；不重复重构明确 intent。

### R1 — Evidence missing

存在多个可能方向，但无法确认消费者、变化频率或业务等价性。

通过：`Intent unresolved`；只保留一个会改变 intent 的 Unknown 和最小探针。

### R2 — Human decision

某兼容行为是长期业务 contract 还是迁移残留，代码无法裁决。

通过：`Intent unresolved`；标明需要 Human 决定及其影响，不伪造方向。

### G1 — False architecture escalation

大函数和目录结构看起来差，但压力来自一个局部错误。

通过：challenge 后撤销 architecture intent。

### G2 — False unification

两条相似路径属于不同 bounded context。

通过：intent 不要求业务统一；记录 bounded-context guard。

### G3 — Speculative abstraction

候选 intent 只能描述“新增 interface/manager”，无法说明什么旧知识或路径退出。

通过：intent 不 ready；返回 unresolved 或 no intent。

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
| Architecture judgment | 局部问题升级或漏判 | 部分正确 | local/architecture 边界和关键 lenses 正确 |
| Intent quality | 模式或任务列表 | outcome 部分清楚 | why now/end state/boundary/obligations 完整 |
| Unknown control | 猜测或发散 | 有 unknown | 一个关键 unknown + 最小关闭方式 |
| Challenge quality | 自我确认 | 检查有限 | 主动检查 false unification/speculation/exit/guards |
| Scope control | 多方向并推 | 大体受控 | 一个 intent，不提前设计或实现 |
| Status judgment | 状态错误 | 正确但冗长 | 正确且最小充分 |

## V0 pass gate

1. P1–P4 中 B 臂的 `Intent discovery + Intent quality` 比 A 臂高至少 2 分；
2. N1–N3、R1–R2、G1–G3 路由正确；
3. 每个 ready 输出只有一个 intent；
4. intent 描述 outcome，不锁死实现模式；
5. 至少一个具体 replacement/exit obligation；
6. 未形成目标设计时，不声称行为等价、迁移完成或维护成本下降；
7. 不调用外部 Skill，不生成 Brooks 报告或 Health Score。

## Failure classes

- `pressure-free-intent` — 从审美发明方向；
- `local-escalation` — 局部问题被升级成架构 intent；
- `intent-sprawl` — 多个方向同时推进；
- `solution-first` — 先定模式再寻找问题；
- `false-unification` — 错误合并不同业务；
- `historical-difference-lock-in` — 把偶然差异永久化；
- `speculative-intent` — 只能新增抽象，不能说明退出目标；
- `unknown-swallowed` — 关键未知被猜测填补；
- `premature-design` — intent 阶段输出完整设计或实现步骤；
- `status-leakage` — 非 ready 状态输出稳定 intent。

Static/scenario smoke 只证明文本机制一致；paired eval 才能衡量冻结样本上的相对收益。
