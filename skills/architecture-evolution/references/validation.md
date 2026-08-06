# Evaluate Architecture Evolution

本文件只用于 Skill smoke/eval，正常运行禁止读取。运行时设计验证见 [verification.md](verification.md)。

## Static smoke

冻结当前 branch/head 后检查：

- frontmatter 与 `agents/openai.yaml` 可解析；
- `SKILL.md` 的相对引用均存在；
- 正常架构分析不指示读取本文件；
- 四条 Principle 与一个 `Real Evolution` Gate 在 `SKILL.md`、`rules.md`、`design-contract.md` 和 `verification.md` 中一致；
- agent prompt 不重复注入完整规则；
- 四种状态名称一致；
- 非 `Design ready` 状态不会输出 canonical abstraction 或 Design Delta；
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
- 不把所有差异机械删除，也不保留两套 canonical path。

### P2 — False unified abstraction

已有公共 base/interface，但包含 mode flag、optional provider config 和多个默认空实现；调用者仍按 family/provider switch 并选择特殊入口。

通过：

- 选择 Principle 2；
- 识别“统一形状但未统一语义”；
- 从共同业务需要定义 stable abstraction；
- 将真实差异放入明确 variation point；
- 删除 union contract、外部 switch 或特殊入口，不再增加 facade。

### P3 — Non-cohesive capability

模块混合核心业务、provider 选择、metrics/debug、cache、compatibility 和资源生命周期；另一部分完整能力又散落在 helper 与调用者中。

通过：

- 选择 Principle 3；
- 用一句话定义完整 capability 和 invariant；
- 区分 intrinsic behavior、private collaborator 与独立责任；
- 不做 one-module-per-concern；
- 收回调用顺序、状态与生命周期，减少 caller knowledge。

### P4 — Reverse policy dependency

通用 Harness/Runtime 或稳定 core 直接依赖具体 Application workflow、provider package 或场景配置；底层通过 callback/global state/registry 反向决定上层路由。

通过：

- 选择 Principle 4；
- 同时检查类型依赖和控制流依赖；
- contract 从稳定 policy 的需要定义；
- detail 朝 capability 提供实现；
- 删除至少一条 common→scenario、policy→provider 或隐式反向控制边。

### N1 — No architecture change

owner、业务语义和依赖方向都清楚，只是局部 off-by-one、日志字段或机械迁移。

通过：`No architecture change`；只输出证据、局部原因与修改边界；无 canonical abstraction 或 Design Delta。

### N2 — Legitimately different business

两个 bounded context 使用相似数据结构，但具有不同 invariant、错误语义和生命周期。

通过：不得为了复用强行统一；返回 `No architecture change`，或只指出局部重复但明确排除业务合并。

### R1 — Research required

无法从静态代码判断两条 legacy path 是否仍承载相同业务，运行流量、消费者或错误契约证据缺失。

通过：`Research required`；只输出已确认事实、一个会改变 same-business judgment 的 Unknown、最小探针和受影响字段；不提前设计 abstraction。

### D1 — Decision required

代码证据已恢复，但某个历史兼容行为究竟是长期业务 contract，还是可删除的迁移残留，需要产品/平台 owner 作高代价承诺。

通过：`Decision required`；只输出共同业务边界、Human-owned 决策、少量选项和推荐；不伪造唯一语义或删除承诺。

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
| Improvement proof | 只说统一/解耦 | 有 before/after | 五个维度可观察并有具体 replacement |
| Status judgment | 状态错误/泄漏 | 正确但偏重 | 正确且最小充分 |

## V0 pass gate

1. P1–P4 至少三个案例中，B 臂的 `Business judgment + Primary diagnosis + Target architecture + Improvement proof` 比 A 臂高至少 2 分；
2. 正样本只选择一个 primary architecture break；
3. B 臂的 Scope control 和 Unification restraint 不低于 A 臂；
4. N1、N2、R1、D1 状态正确且无 status leakage；
5. 每个 `Design ready` 明确 canonical capability、essential differences、stable abstraction、cohesive module、dependency direction 和具体 replacement/delete；
6. 未执行实现证据时，不声称行为保持、业务完全等价、迁移完成或旧路径已经删除。

失败分类：

- `signal miss` — 关键业务或调用证据未找到；
- `same-business miss` — 错误判断同一/不同业务；
- `difference collapse` — 本质差异被错误消除；
- `historical difference preserved` — 偶然差异被永久化；
- `abstraction shell` — 只新增 facade/interface，旧语义仍平行；
- `cohesion miss` — 模块继续混合或能力继续由调用者组装；
- `reverse dependency miss` — 类型或控制流反向依赖未消除；
- `scope expansion` — 一个热点扩大成全仓库重设计；
- `false positive` — 局部任务被升级成架构工作；
- `unverifiable gain` — 改进没有可观察 before/after；
- `status leakage` — 非 ready 状态仍输出目标设计。

同一种 failure 在两个代表性案例重复出现后，才修改 Principle。不要为了单个 miss 扩大 Skill。

## Claim boundary

Static/scenario smoke 只能证明合同和文本机制一致；paired eval 只能证明冻结样本上的设计质量差异。实现正确性、行为对等、迁移完成、实际删除和生产维护成本都需另行验证。
