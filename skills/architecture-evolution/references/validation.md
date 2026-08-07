# Evaluate Architecture Evolution

本文件只用于 Skill smoke/eval，正常运行禁止读取。运行时设计验证见 [verification.md](verification.md)。

## Static smoke

冻结当前 branch/head 后检查：

- frontmatter 与 `agents/openai.yaml` 可解析；
- `SKILL.md` 的相对引用均存在；
- 正常架构分析不指示读取本文件；
- 四条设计 Principle 与一个 `Real Evolution` Gate 在 `SKILL.md`、`rules.md` 和 `design-contract.md` 中一致；
- verification 不定义自有五维体系，直接使用内置 Brooks R1–R6；
- 任何运行时文件都不得调用、加载、路由到或依赖外部 Brooks / brooks-lint Skill、配置、报告模板、Health Score 或 workflow；
- Brooks finding 结构为 `Severity → Symptom → Source → Consequence → Remedy → How to verify`；
- `No finding` 必须带 false-positive guard；
- Architecture Design Contract 只有在 `Design ready + Brooks PASS + 用户要求实现` 时才能输出 `Handoff: Ready`；
- handoff 只包含 `Source / Scope / Delta / Proof`，不复制完整架构决定；
- Source 指向的 Architecture Design Contract 是唯一架构事实源；
- Northstar 的 handoff 入口按需读取 `references/architecture-design-handoff.md`，不得重新裁决架构决定；
- agent prompt 不重复注入完整规则；
- 四种状态名称一致；
- 非 `Design ready` 状态不会输出 canonical abstraction、Design Delta、Brooks constraints 或可执行 handoff；
- Northstar 仍拥有 Goal、授权、任务书、执行与完整验收。

任何失败都先修结构，不进入 behavioral eval。

## Scenario smoke

### P1 — Split business semantics

FeatureStreaming 与 Predict 各有 ParseRequest 路径，输入输出主体一致，但错误、配置解释、日志/metrics 和少量兼容行为不同。

通过：

- 选择 Principle 1；
- 先证明哪些语义属于同一业务；
- 区分 essential 与 accidental differences；
- 定义一个 canonical business capability；
- 不把所有差异机械删除，也不保留两套 canonical path；
- Brooks constraints 至少检查 `R6 Domain Model Distortion`、`R2 Change Propagation` 和 `R3 Knowledge Duplication`。

### P2 — False unified abstraction

已有公共 base/interface，但包含 mode flag、optional provider config 和多个默认空实现；调用者仍按 family/provider switch 并选择特殊入口。

通过：

- 选择 Principle 2；
- 识别“统一形状但未统一语义”；
- 从共同业务需要定义 stable abstraction；
- 将真实差异放入明确 variation point；
- 删除 union contract、外部 switch 或特殊入口，不再增加 facade；
- Brooks constraints 至少检查 `R4 Accidental Complexity`、`R3 Knowledge Duplication`、`R2 Change Propagation` 和 `R5 Dependency Disorder`。

### P3 — Non-cohesive capability

模块混合核心业务、provider 选择、metrics/debug、cache、compatibility 和资源生命周期；另一部分完整能力又散落在 helper 与调用者中。

通过：

- 选择 Principle 3；
- 用一句话定义完整 capability 和 invariant；
- 区分 intrinsic behavior、private collaborator 与独立责任；
- 不做 one-module-per-concern；
- 收回调用顺序、状态与生命周期，减少 caller knowledge；
- Brooks constraints 至少检查 `R1 Cognitive Overload`、`R2 Change Propagation` 和 `R4 Accidental Complexity`。

### P4 — Reverse policy dependency

通用 Harness/Runtime 或稳定 core 直接依赖具体 Application workflow、provider package 或场景配置；底层通过 callback/global state/registry 反向决定上层路由。

通过：

- 选择 Principle 4；
- 同时检查源码依赖和控制流依赖；
- contract 从稳定 policy 的需要定义；
- implementation 朝 contract 提供能力；
- 删除至少一条 common→scenario、policy→provider 或隐式反向控制边；
- Brooks constraints 以 `R5 Dependency Disorder` 为主要 finding，并检查其 `R2 Change Propagation` 后果。

### H1 — Ready handoff to Northstar

目标设计已经 `Design ready`，Brooks constraints 为 `PASS`，用户明确要求开始实现。

通过：

- Architecture Design Contract 输出 `Handoff: Ready`；
- `Source` 只提供 Design Contract 引用与 repo snapshot；
- `Scope` 只约束 target、最小实现范围和 do-not-change；
- `Delta` 只传 `Keep / Move / Merge / Delete`；
- `Proof` 只传 preserve、prove 和 return-when；
- handoff 不复制 canonical capability、variation、module ownership 或 dependency direction；
- Northstar 从 Source 读取架构决定，并把 Scope、Delta、Proof 编译进现有六节任务书；
- 用户已要求实现时，Northstar 达到 `Status: Executable` 后直接 compile-and-run；
- Task 0 只验证合同与当前 repo reality，没有重新执行 Architecture Evolution；
- 只影响实现细节的新证据在合同内重新规划；命中 `Proof.Return when` 时返回 Architecture Evolution。

### N1 — No architecture change

owner、业务语义和依赖方向都清楚，只是局部 off-by-one、日志字段或机械迁移。

通过：`No architecture change`；只输出证据、局部原因与修改边界；无 canonical abstraction、Design Delta、Brooks constraints 或 handoff。

### N2 — Legitimately different business

两个 bounded context 使用相似数据结构，但具有不同 invariant、错误语义和生命周期。

通过：不得为了复用强行统一；返回 `No architecture change`，或只指出局部重复但明确排除业务合并。若进入 constraints scan，`R6` 必须应用 bounded-context guard，不得产生 false finding。

### N3 — Justified adapter

一个薄 adapter 只负责隔离高频变化的外部 vendor protocol，调用者不再依赖 vendor 类型。

通过：`R4 Accidental Complexity` 为 `No finding`，并写明“真实吸收外部变化”的 guard；不得为了消除薄层而重新泄漏 vendor knowledge。

### N4 — Composition root

composition root 显式构造具体 implementation 并注入 policy contract，不承载业务决策。

通过：`R5 Dependency Disorder` 为 `No finding`，并应用 composition-root guard；不得机械要求 composition root 只依赖 abstraction。

### N5 — Handoff not authorized

目标设计为 `Design ready + Brooks PASS`，但用户只要求设计，或 Brooks verdict 为 `RETRY`。

通过：`Handoff: None`；不得把设计合同伪装为 Northstar 可执行授权，不得自动进入实现。

### R1 — Research required

无法从静态代码判断两条 legacy path 是否仍承载相同业务，运行流量、消费者或错误契约证据缺失。

通过：`Research required`；只输出已确认事实、一个会改变 same-business judgment 的 Unknown、最小探针和受影响字段；不提前设计 abstraction、生成 Brooks verdict 或 handoff。

### R2 — Handoff invalidated by current code

Northstar Task 0 发现当前代码已经改变，新证据使 Source 中的业务判断、essential difference、目标结构或 `Proof.Preserve` 不再成立。

通过：命中 `Proof.Return when`，停止受影响实现并返回 Architecture Evolution；不得由 Northstar 自行修改目标架构后继续。仍有独立安全工作时可以保留，但不能消费已失效设计。

### D1 — Decision required

代码证据已恢复，但某个历史兼容行为究竟是长期业务 contract，还是可删除的迁移残留，需要产品/平台 owner 作高代价承诺。

通过：`Decision required`；只输出共同业务边界、Human-owned 决策、少量选项和推荐；不伪造唯一语义、Remedy、删除承诺或 handoff。

Scenario smoke 是合同审计，不等于 clean-session behavioral eval。

## Paired behavioral eval

在支持隔离 clean session 的 runtime 中，对同一任务和 repo snapshot 运行：

```text
A. 同模型，不加载 architecture-evolution
B. 同模型、工具和预算，加载 architecture-evolution
```

冻结任务、repo commit、可见文档、模型版本、工具权限和预算；两臂不得共享输出。

每项 `0–2` 分：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Evidence grounding | 审美判断 | 部分证据 | Observed / Inferred / Unknown 分离 |
| Business judgment | 未判断同一/不同业务 | 有判断但无证据 | canonical capability、共同语义与排除边界有证据 |
| Difference classification | 全部合并或全部保留 | 部分分类 | essential / accidental differences 明确且可验证 |
| Primary diagnosis | 漏掉或罗列 smell | 找到症状 | 四条 Principle 中一个根因 + consequence + 反例 |
| Target architecture | 模式名或空泛目标 | 部分可用 | business、abstraction、module、dependency 相互一致 |
| Scope control | 全面重构 | 大体局部 | 一个目标、一个主断点、明确不做什么 |
| Unification restraint | 新增壳层或错误合并 | 混合 | 拒绝 union abstraction，并保留真实业务差异 |
| Brooks constraints | 无风险审计或自造指标 | 部分风险/链路不完整 | R1–R6 全扫描；finding 符合 Iron Law、severity 与 guard；Remedy 已进入设计；无外部 Skill 依赖 |
| Handoff discipline | 重复设计或越权 handoff | 协议/路由部分正确 | Source/Scope/Delta/Proof 最小充分；Source 单一事实源；Task 0 与 return route 正确 |
| Status judgment | 状态错误/泄漏 | 正确但偏重 | 正确且最小充分 |

## V0 pass gate

1. P1–P4 至少三个案例中，B 臂的 `Business judgment + Primary diagnosis + Target architecture + Brooks constraints` 比 A 臂高至少 2 分；
2. 正样本只选择一个 primary architecture break；
3. B 臂的 Scope control 和 Unification restraint 不低于 A 臂；
4. N1–N5、R1–R2、D1 状态、Brooks guards 和 handoff route 正确，无 status leakage；
5. 每个 `Design ready` 明确 canonical capability、essential differences、stable abstraction、cohesive module、dependency direction 和具体 replacement/delete；
6. Brooks constraints 扫描 R1–R6，主要 finding 有完整 Iron Law 链路，没有未处理的 Critical finding；
7. 残留 Warning 必须写明业务 tradeoff、owner 和验证边界；
8. 运行时不调用或依赖任何外部 Brooks Skill；
9. `Handoff: Ready` 只在有效条件下产生，协议仅传 `Source / Scope / Delta / Proof`，Northstar 不重新裁决架构；
10. 命中 `Proof.Return when` 时返回 Architecture Evolution；
11. 未执行实现证据时，不声称行为保持、业务完全等价、迁移完成或 finding 已经消失。

失败分类：

- `signal miss` — 关键业务或调用证据未找到；
- `same-business miss` — 错误判断同一/不同业务；
- `difference collapse` — 本质差异被错误消除；
- `historical difference preserved` — 偶然差异被永久化；
- `abstraction shell` — 只新增 facade/interface，旧语义仍平行；
- `cohesion miss` — 模块继续混合或能力继续由调用者组装；
- `reverse dependency miss` — 类型或控制流反向依赖未消除；
- `brooks coverage miss` — R1–R6 未完整扫描；
- `iron-law miss` — finding 缺少 Source、Consequence 或设计内 Remedy；
- `guard miss` — 合理 adapter、composition root 或 bounded context 被误报；
- `external-brooks-dependency` — 调用、加载、路由到或依赖外部 Brooks Skill；
- `invalid-handoff` — 非 Design ready、Brooks 未 PASS、无实现授权或四块协议缺失却输出 Ready；
- `duplicated-handoff` — handoff 重复复制完整架构决定而不是引用 Source；
- `architecture-rejudgment` — Northstar 重新裁决已确认架构决定；
- `invalidation-swallowed` — `Proof.Return when` 被当作普通重新规划吞掉；
- `scope expansion` — 一个热点扩大成全仓库重设计；
- `false positive` — 局部任务被升级成架构工作；
- `unverifiable gain` — Remedy 没有具体验证方法；
- `status leakage` — 非 ready 状态仍输出目标设计、Brooks verdict 或 handoff。

同一种 failure 在两个代表性案例重复出现后，才修改 Principle、constraints 或 handoff。不要为了单个 miss 扩大 Skill。

## Claim boundary

Static/scenario smoke 只能证明合同和文本机制一致；paired eval 只能证明冻结样本上的设计质量差异。Brooks constraints 只验证目标设计是否处理已识别风险，handoff 只引用已确认设计并传执行边界；二者都不证明实现正确、行为对等、迁移完成、实际删除或生产维护成本下降。
