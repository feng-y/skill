# Evaluate Architecture Evolution

本文件只用于显式 smoke/eval，正常运行禁止读取。运行时设计验证见 [verification.md](verification.md)。

## Static smoke

冻结当前 branch/head 后检查：

- frontmatter 与 `agents/openai.yaml` 可解析；
- `SKILL.md` 的相对引用都存在；
- 正常运行不读取本文件；
- 主流程为 `Frame → Discover → Select one → Ground → Diagnose → Design → Grill → Verify`；
- 输入既支持开放范围，也支持已知热点；
- 开放范围最多三个候选，最终只选择一个热点；
- 已知热点也要验证真实变化压力和架构价值；
- 四条 Principle 与 `Real Evolution` Gate 在 `SKILL.md`、`rules.md` 和 `design-contract.md` 中一致；
- Grill 检查现实反证、差异、抽象、内聚、依赖、迁移、复杂度转移和删除真实性；
- Verify 直接使用内置 Brooks R1–R6，不定义第二套评分体系；
- 运行时不调用或依赖外部 Wayfinder、Improve、Grill、Brooks Skill 或 workflow；
- Architecture Design Contract 包含 opportunity selection、一个 primary break、一个推荐设计、Grill record、Brooks constraints 和具体 Delete；
- 不包含 Northstar handoff、跨 Skill 协议或实现 workflow；
- agent prompt 不重复注入完整规则；
- 五种状态名称一致：`No architecture opportunity / Opportunity selected / Research required / Decision required / Design ready`。

任何失败都先修结构，不进入 behavioral eval。

## Scenario smoke

### O1 — Open-area discovery

用户只给出一个历史模块，存在多次 provider 分支修改、调用者顺序拼装、旧 facade 并存和一处局部大函数。

通过：

- 从变化历史、调用和测试恢复最多三个候选；
- 不把大函数单独当作架构机会；
- 根据 pressure、leverage、boundary、replacement 和 evidence 选择一个热点；
- 其余候选只写 defer reason；
- 继续设计时只围绕选中热点展开。

### O2 — Selection-only request

用户只问“这个模块下一步最值得做的架构改进是什么”。

通过：输出 `Status: Opportunity selected`；包含选中热点、证据、为什么不是局部修改、deferred candidates 和下一步分析边界；不提前伪造完整目标架构或 Brooks PASS。

### O3 — Known hotspot

用户明确指出 FeatureStreaming 与 Predict 的 ParseRequest 平行路径。

通过：

- 不进行无边界全仓库搜索；
- 验证该热点有真实变化压力和结构后果；
- 检查是否存在更底层的同一业务语义分裂；
- 若只是局部差异则返回 `No architecture opportunity`；否则进入 Ground。

### P1 — Split business semantics

两条路径主体输入输出一致，但错误、配置解释、日志/metrics 和兼容行为不同。

通过：

- 选择 Principle 1；
- 先证明哪些语义属于同一业务；
- 区分 essential 与 accidental differences；
- 定义 canonical capability；
- 不删除真实差异，也不保留两套 canonical path；
- Brooks 至少检查 R6、R2、R3。

### P2 — False unified abstraction

已有公共 base/interface，但包含 mode flag、optional provider config、默认空实现和调用者 switch。

通过：

- 选择 Principle 2；
- 识别“统一形状但未统一语义”；
- 从共同业务需要定义 stable abstraction；
- 把真实差异放入明确 variation point；
- 删除 union contract、外部 switch 或特殊入口，不新增 facade；
- Brooks 至少检查 R4、R3、R2、R5。

### P3 — Non-cohesive capability

模块混合核心业务、provider 选择、metrics/debug、cache、compatibility 和资源生命周期；完整能力又散落在 helper 与 caller。

通过：

- 选择 Principle 3；
- 用一句话定义 capability 和 invariant；
- 区分 intrinsic behavior、private collaborator 与独立责任；
- 不做 one-module-per-concern；
- 收回调用顺序、状态与生命周期；
- Brooks 至少检查 R1、R2、R4。

### P4 — Reverse policy dependency

稳定 core/Harness/Runtime 依赖具体 Application workflow 或 provider，底层通过 callback/global state/registry 决定上层路由。

通过：

- 选择 Principle 4；
- 同时检查源码依赖和运行控制；
- contract 从稳定 policy 的需要定义；
- 删除至少一条 common→scenario、policy→provider 或隐式反向控制；
- Brooks 以 R5 为主要 finding，并检查 R2 后果。

### G1 — Grill rejects attractive design

初始设计提出统一 interface 和 registry，但代码显示两个 bounded context 的错误语义与生命周期不同，registry 仍由 provider 决定 policy 路由。

通过：

- Grill 引用代码、测试或文档反证；
- 拒绝错误业务统一和隐藏反向控制；
- 修改、缩小或撤销设计；
- Grill record 记录实际 correction，不以解释维护原方案。

### G2 — Migration reality

目标设计看似合理，但旧入口仍有活跃消费者，兼容承诺和删除条件不明确。

通过：不能写 `Design ready`；可由 repo/runtime 证据关闭时返回 `Research required`，需要 Human 业务承诺时返回 `Decision required`。

### N1 — Local change only

owner、业务语义和依赖方向清楚，只是 off-by-one、日志字段或机械迁移。

通过：`No architecture opportunity`；只输出证据、为何不升级和局部边界；无 candidate design、Grill 或 Brooks verdict。

### N2 — No real pressure

代码看起来不够优雅，但没有重复变化、调用者摩擦、事故、理解成本或明确需求。

通过：`No architecture opportunity`；不得从审美或模式偏好发明改造。

### N3 — Legitimately different business

两个 bounded context 使用相似数据结构，但 invariant、错误和生命周期不同。

通过：不得为了复用强行统一；R6 应应用 bounded-context guard。

### N4 — Justified adapter / composition root

薄 adapter 隔离 vendor protocol；composition root 构造具体实现但不承载业务决策。

通过：R4/R5 为 `No finding`，分别应用 adapter 与 composition-root guard。

### R1 — Evidence missing

开放范围发现多个信号，但无法确认变化频率、消费者或业务等价性。

通过：`Research required`；只输出会改变选择或设计的一个 Unknown、最小探针和受影响结论；不伪造热点排序或目标设计。

### D1 — Human-owned decision

某兼容行为是长期 contract 还是迁移残留，代码无法裁决。

通过：`Decision required`；输出共同事实、Human-owned 取舍、少量选项和推荐；不伪造删除承诺。

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
| Opportunity discovery | 审美或随机点 | 有信号但无 consequence | 从真实 pressure 形成有边界候选 |
| Selection quality | 多热点并推或任意选择 | 有选择但依据弱 | 一个热点，leverage/replacement/evidence 清楚 |
| Evidence grounding | 审美判断 | 部分证据 | Observed / Inferred / Unknown 分离 |
| Business judgment | 未判断同一/不同业务 | 有判断但无证据 | canonical capability 与排除边界有证据 |
| Difference classification | 全合并或全保留 | 部分分类 | essential / accidental 明确可验证 |
| Primary diagnosis | 罗列 smell | 找到症状 | 一个 Principle 根因 + consequence + 反例 |
| Target architecture | 模式名或空泛目标 | 部分可用 | business/abstraction/module/dependency 一致 |
| Grill quality | 自我确认 | 检查但无修正 | 主动找反证并修改/撤销错误设计 |
| Brooks constraints | 无审计或自造指标 | 部分风险 | R1–R6、Iron Law、severity、guard 完整 |
| Scope/status | 全仓库扩张或状态错 | 大体受控 | 一个热点、正确状态、最小充分输出 |

## V0 pass gate

1. O1、O3 中 B 臂的 `Opportunity discovery + Selection quality` 比 A 臂高至少 2 分；
2. P1–P4 至少三个案例中，B 臂的 `Business judgment + Primary diagnosis + Target architecture + Grill quality` 比 A 臂高至少 2 分；
3. 开放范围最多三个候选，最终只推进一个热点；
4. 正样本只选择一个 primary architecture break 和一个推荐设计；
5. N1–N4、R1、D1 状态与 guards 正确；
6. 每个 `Design ready` 明确 selected opportunity、canonical capability、essential differences、stable abstraction、cohesive module、dependency direction 和具体 Delete；
7. Grill 有实际反证检查和设计 correction；
8. Brooks 扫描 R1–R6，主要 finding 有完整 Iron Law 链路，没有未处理 Critical；
9. 运行时不调用外部 Matt/Brooks Skill，不出现 Northstar handoff；
10. 未执行实现证据时，不声称行为保持、迁移完成、旧路径删除或维护成本下降。

## Failure classes

- `pressure-free-opportunity` — 从审美或模式偏好发明架构工作；
- `opportunity-miss` — 漏掉最强变化压力；
- `selection-sprawl` — 多个平级热点同时推进；
- `weak-selection` — 选择没有 leverage、replacement 或 evidence 支撑；
- `same-business miss` — 错误判断同一/不同业务；
- `difference collapse` — 本质差异被错误消除；
- `historical difference preserved` — 偶然差异被永久化；
- `abstraction shell` — 只新增 facade/interface，旧语义仍平行；
- `cohesion miss` — 能力继续由调用者组装或模块继续混合；
- `reverse dependency miss` — 类型或控制流反向依赖未消除；
- `grill theater` — 只写通过，没有实际反证或 correction；
- `brooks coverage miss` — R1–R6 未完整扫描；
- `guard miss` — 合理 bounded context、adapter 或 composition root 被误报；
- `external-skill-dependency` — 调用或依赖外部 Wayfinder/Improve/Grill/Brooks Skill；
- `scope expansion` — 局部机会扩大成全仓库重设计；
- `status leakage` — 非 Design ready 状态输出完整目标设计或 Brooks PASS。

同一种 failure 在两个代表性案例重复后，才修改 Principle 或流程。不要为了单个 miss 扩大 Skill。

## Claim boundary

Static/scenario smoke 只能证明文本机制一致；paired eval 只能证明冻结样本上的相对设计质量。它们不证明实现正确、行为等价、迁移完成、实际删除或生产维护成本下降。
