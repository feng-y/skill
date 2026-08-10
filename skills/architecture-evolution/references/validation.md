# Evaluate Architecture Intent

本文件只用于显式 smoke/eval，正常运行禁止读取。

## Static smoke

检查：

- 主目标是构造 Architecture Intent，不是完成目标设计或实现；
- 主流程仍为 `Ground → Discover → Shape → Challenge and constrain`，没有新增 round / execution 阶段；
- 运行时引用为 `rules.md`、`brooks-constraints.md` 和 `intent-contract.md`；`legacy-lenses.md` 只在 legacy/compat/identity 信号出现时加载；
- Reality 分开观察 Business semantics、Ownership & lifecycle、Consumer knowledge/reassembly、Source dependency、Runtime control/consumption，但只输出实际改变 judgment 的 evidence，不生成五面审计表；
- `consumer reassembly` 是 cross-cutting signal，不是第五个 architecture direction；纯 composition-root wiring 不自动算 reassembly；
- 四个方向完整保留：Business Semantic Integrity、Stable Abstraction with Explicit Variation、Cohesive Capability Ownership、Unidirectional Policy Dependency；
- 一个 intent 只选择一个 primary architecture direction，其他命中作为 consequence 或 design obligation；
- Architecture contribution 连接 evolution horizon、domain/identity constraint、target pressure 与 durable capability；四个方向只描述结构杠杆；
- broad next-direction 请求执行 `target + evolution vocabulary` 的有界检索，不在第一份 repo-level 文档处停止，也不以 system identity、ADR、hard boundary 或最近 subsystem objective 代替 evolution horizon；
- AI-native / agentic engineering 是明确 horizon 时，Contribution 必须落到 agent intervention、independent verification 与跨局部重构仍成立的 durable capability，不能只写口号；
- Design obligations 只输出当前 intent 实际相关的项，不机械填满 semantics / variation / ownership / reassembly / dependency；
- ownership intent 只把 owner scope 扩到 evidence 支持的 invariant 边界；capability ownership 不自动推导 request execution / orchestration ownership；
- 相邻 subsystem 已有正确 authoritative owner 时，当前 intent 只要求稳定 relation/contract，不默认吞并其内部 config/resource/lifecycle；
- `Real Evolution` 要求至少一个旧路径、重复知识、caller knowledge/reassembly、无效抽象、兼容分支或反向依赖退出；
- reasoning distinction 可以先用于解释，不能因为被命名就自动物化为 type/provider/adapter/layer/public seam；
- Material Unknown 存在时使用 `claim at risk → minimal probe → evidence → intent changed / retained`；没有 material unknown 时整个 section 省略，禁止制造；
- legacy identity 只有在当前 rename/delete/replacement 依赖它时才升级为 material unknown，否则进入 `Must preserve` 或 out of scope；
- Success evidence 以稳定 acceptance rule 为主；会随 runtime/config/deployment binding、changed boundary/ownership 或时间变化的对象只作为 current snapshot evidence，并在实现时重新推导 affected scope；
- Challenge 检查 local escalation、false unification、historical difference lock-in、speculative abstraction、complexity relocation、consumer reassembly、owner-scope expansion、snapshot freeze 和 replacement reality；
- Brooks R1–R6 被保留为下游架构设计逐步吸收的约束，不被降级为可选提示；
- Brooks constraint 的数量不是失败标准：全部 R1–R6 有独立 evidence 时允许全部出现；禁止的是无 evidence 的机械补齐；
- Brooks optional proof vocabulary 包含 ownership closure、mechanical boundary protection、stable public test surface、complexity relocation，但不是 intent 阶段的新 completion checklist；
- intent 阶段只携带相关 Brooks constraints/proof expectation，不做全量扫描、Severity、PASS/RETRY、Health Score 或完整报告；
- `brooks-constraints.md` 只在 intent 方向稳定后加载；
- 不存在 Design ready、Architecture Design Contract、round shape、one-module execution owner、implementation slices、completion workflow 或 Northstar handoff；
- 输出只有 `No architecture intent / Intent unresolved / Architecture intent ready`；
- intent contract 描述 outcome、decisive reality/evidence、boundary、适用 design obligations、progressive constraints、按需 material-unknown control 和稳定 success evidence，不提前编译实现步骤；
- 不调用外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill；
- README usage 与 SKILL.md 的适用边界、三种状态和“只构造 intent”终点一致；
- README 明确用户不需要预先提供候选、架构原则、Brooks 风险、最终设计或完整证据；
- README 的例子只提供模块/症状/模糊方向，不要求用户先完成 architecture analysis；
- README 对目标设计已明确、完整设计、任务书、code review 或直接实现请求明确要求跳过本 Skill；
- README 不建立固定下游 Skill 或 handoff 链路。

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

通过：形成一个 intent，说明 why now、desired end state、primary direction、boundary、适用 design obligations、progressive constraints 和退出目标；不直接输出 class 拆分方案，也不为无关方向制造 obligation。

### P6 — Multiple symptoms, one intent

用户列出抽象泄漏、模块过大、反向依赖和测试脆弱。

通过：找到能解释主要压力的一个 primary direction；其他症状作为 consequence、constraint 或 out of scope，不并列输出多个改造项目。

### P7 — Reality axes do not substitute for each other

源码依赖已经很干净，只有一个 Provider 接口，但 runtime resource 仍由 caller 创建和 retain，多个 consumer 各自解释 lifecycle。

通过：不能因为 dependency/type surface 干净就判断 ownership 已闭合；Reality 明确区分 source dependency 与 runtime ownership，intent 可落在 Cohesive Capability Ownership，并把 caller lifecycle knowledge 作为退出目标。

### P8 — Consumer reassembly is evidence, not a fifth direction

consumer 必须组合 config、provider type、runtime handle 和调用顺序才能使用一个能力。

通过：识别 `consumer reassembly` 为 architecture signal；根据根因选择 Stable Abstraction 或 Cohesive Capability Ownership 之一作为 primary direction，不新增 `Consumer Boundary` 第五方向。

### P9 — Ownership scope follows the invariant

一个发布型 capability owner 需要闭合 generation/resource/config invariant；相邻 orchestration 当前拥有目标绑定、sequencing、并发和结果对齐。

通过：owner 的命名和 scope 必须匹配当前 evidence。若证据只支持 published / execution-ready capability，则不得仅因 caller reassembly 将其命名成 execution owner；若另有证据证明 execution invariant 本身也属于该 capability，则可以扩大 owner scope。Boundary / Must preserve 明确记录未被当前 intent 改变的责任。

### P10 — Ownership closure does not imply centralization

当前 capability consumer 直接读取相邻 feature/runtime subsystem 的内部 config 与 resource；该 subsystem 自身已有清楚的 authoritative owner。

通过：intent 要求 consumer 不再重组相邻 subsystem 内部事实，并通过稳定 capability relation/contract 消费；不得默认把相邻 subsystem 的 config、resource、lifecycle 全部迁入当前 owner。只有 evidence 证明相邻 ownership 自身错误时才改变它。

### P11 — Stable acceptance rule versus current snapshot

当前 repo 可以枚举三个受影响 replay app，但这些 app 由 production config / deployment binding 动态决定。

通过：Success evidence 写成“实现时根据最终 changed boundary/ownership 与届时 effective runtime/config/deployment state 重新推导 affected targets，并覆盖全部受影响对象”；replay 在该 case 中是适用的 proof。当前三个 app 可以作为 `Current snapshot evidence`，不能冻结为长期 acceptance set。

### P12 — Architecture altitude before local target shape

repo 已声明扩大可独立验证的 AI intervention surface，并点名一个历史 module 作为高价值切口；另有 repo strategic identity、subsystem objective 和 module-local ownership pressure。

通过：Intent 用 `AI-native horizon → identity/domain constraint → module pressure → durable capability` 说明 agent intervention 如何更有界且可独立验证；局部 provider / consumer / ownership 收紧只进入 obligation 或下游 target design。

失败：primary intent 只输出 cohesive owner、truthful provider、stable interface；只连接 subsystem objective；用 strategic identity / hard boundary 替代 AI-native evolution authority；或只有 AI-native 标签而没有 intervention / verification evidence。

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

### B3 — Ownership closure proof

intent 指向把 runtime state 收敛给一个 capability owner。

通过：相关 R1/R3 proof expectation 可以要求后续证明 private ownership、真实 lifetime、consumer 通过 owner boundary 读取、无 sidecar truth、generation 不混用；Intent 不规定具体字段迁移顺序，也不声称这些 proof 已通过；相邻 subsystem 的合法 ownership 不因该 proof 被一并集中。

### B4 — Boundary/test/relocation proof remains progressive

intent 声称建立更稳定 boundary 并减少 caller knowledge。

通过：可以携带“关键 boundary 在可机械表达时应有 fail-able guard”“重要 invariant 从 public capability surface 验证”“distributed knowledge/consumer reconstruction 真正下降”等 proof expectation；不能把这些变成 intent 阶段必须执行的 architecture test、CI 或完整 completion gate，也不能机械输出全部四种 proof。

### B5 — All Brooks risks may be genuinely relevant

一个历史热点同时存在 caller cognitive load、重复 family/config 解释、change propagation、已有 facade 未替代旧路径、反向 policy dependency 和真实 bounded-context variation。

通过：如果 R1–R6 每项都有独立 current evidence 和具体 design constraint，可以全部携带；不得仅因“覆盖太全”删除真实约束。反之，没有 evidence 的条目即使为了表格完整也不能出现。

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

通过：`Intent unresolved`；指出 `Claim at risk`，只执行一个能改变 intent 的最小 probe，不提前携带猜测性的 constraints。

### R2 — Human decision

某兼容行为是长期业务 contract 还是迁移残留，代码无法裁决。

通过：`Intent unresolved`；Human 决定必须明确对应会改变的 claim/boundary/exit，不伪造方向或退出承诺。

### R3 — Material unknown falsification

当前推断“两条路径属于同一业务”，但缺少一个关键 consumer 的语义证据。

通过：输出 `claim at risk → minimal probe → evidence → intent changed / retained`；如果 probe 证明 consumer 属于不同 bounded context，则修改或撤销原 intent。仅列出“需要确认 consumer”但继续沿原方向推进视为失败。

### R4 — No manufactured unknown

业务语义、owner boundary、consumer 和 runtime evidence 已足以支持一个 bounded intent，没有会改变方向的未决事实。

通过：`Architecture intent ready` 直接省略 `Material unknown` section；不得为了满足 contract 人为提出一个无法改变判断的“待确认项”，也不输出 `None` 占位。

### L1 — Compat token is not runtime state

一个历史 token 已不再影响 runtime branch，但仍用于 parse/serialization/deployment identity。

通过：按需加载 `legacy-lenses.md`；不因 runtime 无 effect 就要求删除 token，intent 区分 runtime retirement 与 compatibility/identity obligation。

### L2 — Search absence is not death proof

repo 内找不到某 provider identity 或 config key 的直接 reader，但它可能出现在 generated config、registration 或 repo 外 deployment。

通过：不得以 local grep absence 宣布 dead；只有当前 rename/delete/exit 依赖该 identity 时才升级为 material unknown，否则将其放入 `Must preserve` 或 out of scope，避免无界研究。

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

vendor adapter 吸收真实外部变化，composition root 只做 wiring，不承载业务 policy、runtime sequencing、lifecycle ownership 或 capability usage knowledge。

通过：R4/R5 和 consumer-reassembly guard 正确应用，不为了“吸收 Brooks”或“关闭 reassembly”而删除合理边界。

### G5 — Explain first, materialize later

分析发现 provider/support/worker 三个角色对解释当前系统有帮助，但当前 caller、ownership、variation 和 verification evidence 都不需要新的 public seam。

通过：这些 distinction 只保留为 reasoning vocabulary；不得因为已命名就输出三个新接口/层。只有 evidence 能证明 seam 收敛真实 burden 时，才形成下游 design obligation。

## Usage smoke

### U1 — Minimal vague input

README 用户只提供一个模块和“边界不对、分支越来越多”的模糊感觉，没有预先整理证据、候选或架构原则。

通过：这是有效用法；Skill 自己检查 repo evidence、恢复 pressure 并判断是否存在 architecture intent。不得要求用户先列 Brooks 风险或选择四个方向。

### U2 — Known hotspot without solution

README 用户指出两条平行路径，但明确不知道应合并、适配还是保持不同。

通过：这是有效用法；Skill 先恢复业务现实和 essential difference，再形成 intent obligations，不把用户列出的三个方向当成预设答案。

### U3 — Broad next-direction request

README 用户只提供模块/能力并问“下一步最值得推进的架构方向是什么”。

通过：这是有效用法；Skill 从真实 change pressure 中构造一个 intent，不从代码审美随机挑一个重构点，也不输出候选项目列表。

### U4 — User should not pre-analyze

用户问“调用前是否需要先整理 Brooks R1–R6、四个架构方向、历史 commit 和候选方案”。

通过：README 应明确回答“不需要”；用户只需给最小 repo 范围和当前担忧，能由 repo/runtime 查到的事实由 Skill 自己查。

### U5 — Skip when intent is already stable or execution is requested

用户已经有稳定 Architecture Intent、目标 contract、实现边界和成功标准，只想继续设计/实现；或者当前请求本身就是完整设计、任务书、code review 或直接实现。

通过：README 明确应跳过 Architecture Evolution；不得为了使用 Skill 而重新把稳定 intent 打散，也不得把直接执行请求改写成新的 intent 工作流。

### U6 — Usage does not create workflow coupling

用户读完 README 后询问“Architecture Evolution 是否必须 handoff 到某个特定 Skill”。

通过：答案是否；README 只说明 intent ready 后进入正常下游设计/执行，不规定固定 Skill、状态协议或 handoff contract。

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
| Reality separation | 用单一结构信号替代业务/ownership/runtime 判断 | 部分区分 | semantics/ownership/consumer/source/runtime 按证据区分且只展开相关面 |
| Intent discovery | 罗列症状/方案 | 有方向但不稳定 | 一个能解释压力的 architecture intent |
| Architecture altitude | 局部 target shape 或 system identity 冒充 evolution outcome | 提到上位目标但贡献不可验证 | evolution authority、pressure、durable capability 与 success evidence 闭合 |
| Direction judgment | 未分类或多方向并推 | 方向大致正确 | 一个 primary direction，consumer reassembly 等信号正确降为 consequence/obligation |
| Intent quality | 模式或任务列表 | outcome 部分清楚 | why now/end state/boundary/适用 obligations 完整且无机械填表 |
| Ownership scope | 从 reassembly 直接推导更大的 owner | owner 大致正确但 relation 含糊 | owner scope 匹配 invariant evidence，execution/orchestration 与 adjacent ownership relation 清楚且不机械分离/集中 |
| Evidence lifetime | 冻结当前 app/target/config 枚举 | 有稳定规则但 snapshot 混写 | stable acceptance rule + 动态 affected-scope derivation 清楚，current snapshot 单独标记 |
| Progressive constraints | 无 Brooks、机械全扫或因“太多”删真实约束 | 有相关 constraint 但边界含糊 | 约束逐项 evidence-driven；数量不作为质量启发式；必要 proof expectation 准确 |
| Unknown falsification | 猜测、制造 unknown、只命名 unknown 或不改变行动 | 有 probe 但 claim/影响不清 | material unknown 有则 claim+probe+evidence+changed/retained 完整；无则整节省略 |
| Challenge quality | 自我确认 | 检查有限 | 主动检查 false unification/speculation/reassembly/owner-scope/snapshot/relocation/exit/guards |
| Materialization discipline | 每个角色都物化为 seam | 大体克制 | explain first，只有 evidence 支持才形成 public seam obligation |
| Scope control | 多方向并推或恢复 round workflow | 大体受控 | 一个 intent，不提前设计/实现，不引入 execution owner/round shape |
| Status judgment | 状态错误 | 正确但冗长 | 正确且最小充分 |
| Invocation discipline | 要求用户先做 architecture analysis 或误用已稳定/直接执行任务 | 大体知道何时调用 | 从最小模糊输入自助恢复 evidence，且在 intent 已稳定或请求已进入设计/执行时正确退出 |

## V0 pass gate

1. P1–P12 中 B 臂的 `Reality separation + Intent discovery + Architecture altitude + Direction judgment + Intent quality + Ownership scope` 比 A 臂高至少 2 分；
2. B1–B5 中 Brooks constraints/proof vocabulary 被正确渐进吸收：不丢失、不机械前置、不因条目数量误判；
3. N1–N3、R1–R4、L1–L2、G1–G5 路由和 guards 正确；
4. U1–U6 usage smoke 全部通过；README 不要求用户预先做候选分析、原则选择或 Brooks 扫描，并正确排除已稳定 intent 与直接设计/执行请求；
5. 每个 ready 输出只有一个 intent 和一个 primary direction；consumer reassembly 不成为第五方向；
6. 每个 ready 输出都有 Architecture contribution；局部 target shape 不替代上位 outcome；
7. intent 描述 outcome，不锁死实现模式；reasoning distinction 不自动物化；Design obligations 只输出适用项；
8. ownership claim 只扩到 evidence 支持的 invariant；不得从 capability ownership 无证据推导更大的 execution/orchestration owner，也不得无证据集中相邻 subsystem 的合法 ownership；
9. 至少一个具体 replacement/exit obligation；
10. 相关 Brooks constraints 有 Design constraint、Why applicable、Guard 和必要的 Proof expected；全部 R1–R6 独立有 evidence 时允许全部出现；
11. Material Unknown 存在时必须真正改变或保留 architecture judgment；不存在时整节省略，禁止制造或输出占位；
12. Success evidence 使用稳定 acceptance rule；动态 affected targets/config 在实现验收时重新推导，当前枚举只作为 snapshot evidence；
13. legacy identity 不因 local search absence 自动被判 dead，也不因潜在 repo 外使用而无条件阻塞；
14. 未形成目标设计时，不声称 proof 已满足、行为等价、迁移完成或维护成本下降；
15. 不调用外部 Skill，不生成完整 Brooks 报告或 Health Score；README 不创建固定下游 handoff；
16. 不恢复 round shapes、one-module execution-owner、next-slice progression 或 completion workflow。

## Failure classes

- `pressure-free-intent` — 从审美发明方向；
- `local-escalation` — 局部问题被升级成架构 intent；
- `local-target-substitution` — 局部 capability / ownership / interface target 合理，却替代了 area 对上位 evolution objective 的贡献；
- `nearest-horizon-substitution` — 用最近的 subsystem objective 或 system identity 替代更高、仍有效且明确依赖当前 area 的 evolution horizon；
- `reality-collapse` — 用 clean interface/provider/dependency 等单一信号替代 semantics、ownership 或 runtime reality 判断；
- `consumer-reassembly-miss` — caller 仍重组 capability facts，但被误判为 boundary 已闭合；
- `consumer-reassembly-false-positive` — 把纯 composition-root wiring 误判为 capability reassembly；
- `ownership-scope-creep` — 从 capability ownership 无证据扩张到更大的 execution、orchestration、scheduling、result policy 等 ownership；
- `ownership-centralization` — 为关闭 caller reassembly，把已有正确 owner 的相邻 subsystem config/resource/lifecycle 一并集中到当前 owner；
- `snapshot-freeze` — 把当前 app/target/config/deployment 枚举冻结成长期 acceptance contract，而不是保留稳定 affected-scope 推导规则；
- `intent-sprawl` — 多个方向同时推进；
- `direction-loss` — 四个方向之一被删除、弱化或无法表达；
- `fifth-direction-creep` — 把 consumer reassembly、provider role 等 signal 升级成新的 architecture principle；
- `obligation-checklist-creep` — 为覆盖固定类别而输出与当前 intent 无关的 design obligations；
- `solution-first` — 先定模式再寻找问题；
- `false-unification` — 错误合并不同业务；
- `historical-difference-lock-in` — 把偶然差异永久化；
- `speculative-intent` — 只能新增抽象，不能说明退出目标；
- `materialization-creep` — reasoning role 被自动物化成 type/provider/adapter/layer；
- `brooks-loss` — Brooks 被降成可选提示，未进入 design obligations；
- `brooks-frontload` — intent 阶段机械展开 R1–R6、Severity、PASS/RETRY 或执行 proof；
- `brooks-cardinality-heuristic` — 仅因 Brooks 条目数量多就删除有独立 evidence 的真实约束，或因数量少就认为覆盖不足；
- `proof-overreach` — intent 阶段声称 ownership closure、mechanical guard、stable test surface 或 complexity reduction 已被实现证明；
- `proof-checklist-creep` — 无论适用性都机械携带四种 optional proof；
- `guard-miss` — 合理 bounded context、adapter、composition root 或深模块被误报；
- `unknown-swallowed` — 关键未知被猜测填补；
- `unknown-decoration` — 命名 material unknown 但没有 claim/probe/evidence/judgment change；
- `unknown-manufacture` — 没有会改变 intent 的 unknown，仍为了合同格式人为制造或输出占位 section；
- `legacy-runtime-collapse` — 把 parse/serialization/deployment identity 错当成 runtime behavior 或反过来；
- `search-absence-deletion` — 因 local search 无 reader 就宣告 identity/config 可以删除；
- `legacy-scope-explosion` — identity 不影响当前 exit 仍因潜在 repo 外使用而无限扩查；
- `premature-design` — intent 阶段输出完整设计或实现步骤；
- `workflow-regression` — 恢复 round shape、execution owner、next-slice 或 completion workflow；
- `status-leakage` — 非 ready 状态输出稳定 intent；
- `usage-prework` — README 让用户先整理候选、原则、Brooks 风险或完整 evidence 才能调用；
- `usage-overreach` — README 暗示 Skill 会直接产出完整设计、迁移方案或实现；
- `usage-coupling` — README 建立固定下游 Skill 或 handoff 协议；
- `usage-misroute` — README 把已稳定 intent、完整设计、code review 或直接实现请求重新路由回 Architecture Evolution。

Static/scenario/usage smoke 只证明文本机制一致；paired eval 才能衡量冻结样本上的相对收益。
