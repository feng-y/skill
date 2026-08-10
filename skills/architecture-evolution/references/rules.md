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

## Architecture altitude

Architecture intent 不只回答局部 hotspot 应变成什么；它必须说明为什么当前 area 值得成为 architecture evolution，以及它推进什么上位、可持续的结果。

先恢复竞争中的 horizon，并按它们回答的问题区分 authority：

- **Evolution authority** 回答 current stage、next evolution、engineering north-star、构建目标或高价值方向，拥有 architecture altitude；
- **Identity / domain / constraint authority** 回答系统是什么、主导业务边界、subsystem 责任、ADR 或 hard boundary，只约束 intent 与 must-preserve；即使被标为高优先级，也不因约束力强而自动变成 evolution outcome；
- **Target reality** 用代码、runtime、config、tests 与 history 证明 pressure 和局部结构杠杆，不自动拥有上位方向。

广义 next-direction 请求不能在第一份 repo-level 文档处停止：完成 target reality 后，必须做一次 `target name + current stage / next evolution / north-star / building goal` 的 repo-wide 有界检索；这是 direction-selection probe，不改变 repo route。再用 identity/domain/constraint authority 校验边界。architecture direction 文档可以拥有方向判断，即使它位于 knowledge layer 或不拥有 execution route；若它明确点名 area、把它列为高价值切口或必要能力，不得用更近的 subsystem objective、ADR 或 hard boundary 替代。无法裁决 authority 时保留 Material Unknown。current-stage objective 与 long-term north-star 同时存在时，选择当前可验证的结果，并说明它如何推进长期 north-star。

每个候选用一条 contribution chain 接受 altitude 检查：

```text
Evolution horizon
→ domain / identity constraint
→ target pressure
→ durable architecture capability
```

四个 architecture directions 只描述实现该结果的主要结构杠杆。provider / consumer / ownership / interface 收紧通常只是 obligation 或 target-design candidate；downstream design / goal compiler 不应再调查“为什么这个 target 值得推进”，但 intent 仍不得预选 class、interface、owner layout、迁移步骤或具体验证套餐。

当 repo 明确以 **AI-native / agentic engineering** 为 horizon，且当前 area 位于其因果链时，Contribution 必须使用 repo 自己的目标语义说明 agent intervention 如何变得更可发现、更有界或更便宜，结果如何独立验证，以及为何这项能力跨一次局部重构仍成立；局部 deepening 或 “AI-friendly” 标签不能替代该结果。

## Architecture reality lenses

恢复现实不是画一张统一的结构图。按当前 evidence 分开判断下面几个观察面；只展开会改变 intent 的部分：

1. **Business semantics** — 哪些路径表达同一业务能力，哪些属于不同 bounded context；事实和规则的权威解释在哪里。
2. **Ownership & lifecycle** — config、runtime resource、state、publication、reload 和 lifetime 由谁真正拥有。
3. **Consumer knowledge / reassembly** — caller 是否仍需知道并组合 implementation、configuration、ordering、lifecycle、identity 或 access facts 才能使用 capability。
4. **Source dependency** — source-level contract、policy、implementation 的依赖方向是否稳定。
5. **Runtime control / consumption** — 谁在运行时选择、构造、驱动和消费 capability；clean type dependency 不自动证明 runtime ownership 正确。

一个观察面整洁不能替另一个观察面作证。例如：single provider type 不等于 single business semantic owner；clean interface 不等于 consumer 已停止 reassembly；clean dependency graph 不等于 runtime ownership 已闭合。

### Consumer reassembly

`Consumer reassembly` 是 cross-cutting signal，不是第五个 architecture direction。

当调用者为了使用一个 capability，仍需重新组合本应属于 capability owner 的 configuration、implementation、lifecycle、ordering、identity 或 access facts，则 capability boundary 尚未闭合。它通常会指向 Stable Abstraction、Cohesive Capability Ownership，以及 R1/R2/R3 的相关设计约束。

纯 composition-root wiring 不自动构成 consumer reassembly：如果它只选择具体 implementation、没有承载业务 policy、runtime sequencing、lifecycle ownership 或 capability usage knowledge，则保留为合法组装边界。

### Ownership scope

`Cohesive Capability Ownership` 只要求当前 capability 的 invariant、state/lifetime 和 usage contract 闭合；它本身不证明 execution、orchestration 或相邻 subsystem 也应归同一 owner。

当 ownership 是 primary direction，或 ownership relation 会改变 intent boundary / obligation 时，只记录会改变判断的关系：

- 当前 owner 真正闭合的是哪项 capability / invariant；
- 已存在的 execution/orchestration responsibility 是否需要保留，或者有什么 evidence 证明它也属于当前 capability；
- consumer reassembly 是否跨入一个已有 authoritative owner 的相邻 subsystem，因而只需要稳定 relation / contract。

ownership 只能扩到 evidence 支持的 invariant 边界。`capability ownership` 不自动蕴含 `execution ownership`，`ownership closure` 也不自动要求 `ownership centralization`。如果相邻 feature/runtime/resource subsystem 已有内聚 owner，不因当前 caller reassembly 就默认把其内部 config、resource 或 lifecycle 全部迁入当前 owner；只有 evidence 证明该 ownership 本身错误时才改变它。

## Four architecture directions

这四个方向必须保留。它们用于构造 intent，而不是要求当前阶段完成目标设计。一个 intent 选择一个 primary direction，其他命中只作为 consequence 或 design obligation。

1. **Business Semantic Integrity**
   - 是否存在同一业务的多套语义或事实解释？
   - 是否可能错误合并不同 bounded context？

2. **Stable Abstraction with Explicit Variation**
   - 调用者是否依赖实现差异而不是业务能力？
   - 哪些差异可能是 essential，哪些只是历史残留？
   - variation 只有在 evidence 证明它对应稳定 semantic / invariant difference 时才进入长期抽象；current implementation partition 本身不构成 variation。

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
- 调用者内部知识或 capability reassembly；
- 无效抽象或特殊入口；
- 反向或循环依赖；
- 永久兼容分支。

如果只能说“增加 facade/interface/manager/registry”，intent 尚未成立。

## Explain first, materialize later

用于解释现实的 distinction 或 partition 可以先停留在 reasoning vocabulary。**Observed partition 是 evidence，不是 architecture boundary。** 只有 evidence 表明新的 seam 会承载稳定 semantics/invariant、闭合 ownership、承载 essential variation、形成长期 change boundary 或建立稳定 verification surface 时，才交给后续设计物化；否则保留为解释模型或 guard。

## Material unknown falsification

只有会改变 Architecture Intent、Boundary 或 Design Obligation 的 unknown 才是 material unknown。存在这类 unknown 时，关闭它至少使用下面的控制链：

```text
Claim at risk
→ Minimal territory probe
→ Evidence
→ Intent changed / retained
```

- `Claim at risk`：明确哪个 architecture judgment 会被该未知推翻或缩小；
- `Minimal territory probe`：只调查足以裁决该 claim 的最小事实；
- `Evidence`：记录代码、runtime、历史或 Human 决定；
- `Intent changed / retained`：明确 evidence 如何改变或保留 intent/boundary/obligation。

如果当前没有 material unknown，不要为了满足输出结构制造一个。若 unknown 被命名后不改变任何下一步，它不是 material control signal，不要把它作为正式 blocker 装饰输出。

## Evidence and judgment lifetime

Architecture reality、material claim 和由其支持的 architecture judgment 都有前提。保持 **one judgment, one active owner**：同一事实或判断只保留一份当前 authoritative state，历史说明可以作为 provenance，但不能和已更新判断并列为 active truth。

- 支撑 judgment 的代码、runtime、binding/config、业务语义、owner boundary 或 Human authority 前提未变化时，直接复用已有 Evidence 和判断；不要因为从 Ground 进入 Discover / Shape / Challenge、换了 lens 或开始 Brooks 检查就重新发现、重新论证；
- 新 authoritative Evidence 改变前提时，只 reopen 受影响的 claim，并在原 semantic owner 处替换或失效旧判断；只传播到受影响的 Intent / Boundary / Design Obligation / Success evidence，不重算无关部分；
- 新旧 snapshot 不得同时作为有效依据。若需要保留旧状态解释历史，只标为 provenance / prior snapshot，不参与当前 architecture judgment；
- 具体 evidence provider 由后续 design / implementation 根据 repo verification authority 和最终 change surface 选择；provider 本身是稳定受保护判卷标准，或当前必须点名才能消除歧义时，才在 intent 中固定入口；
- affected scope 会随 runtime/config/deployment binding、changed boundary/ownership 或时间变化时，必须保留 scope derivation，并在实现验证时按最终 change surface 与届时 effective reality 重新推导；
- 会动态变化的具体对象列表只能作为 current snapshot evidence，除非它本身就是稳定 contract；
- replay 只是适用时的一种 evidence provider，不是所有 architecture intent 的固定验收机制。

Success evidence 直接从当前 Architecture Intent 已承诺的结果、invariant、must-preserve、boundary 和 replacement/exit 推导**必须证明什么**；不要再把这些 claim 转写成第二套完成条件。当前具体样本可以保留来证明 intent grounded，但必须标明它是 `current evidence`，不能替代稳定 acceptance rule。

## Challenge the intent

Challenge 从**当前仍有效的 best-known intent** 出发寻找会推翻、缩小或改变 boundary/obligation 的反证；前提没有变化的 judgment 直接复用，不重新跑一遍完整 architecture analysis、所有 reality lenses 或 Brooks 清单。

重点检查：

- 问题是否其实是局部修复；
- 是否把局部 target shape、最近的 subsystem objective、system identity、ADR 或 hard boundary 冒充为 evolution outcome；
- 是否在第一份 repo-level 文档处停止，漏掉更高、更当前或明确点名 area 的 evolution authority；
- 是否错误统一不同 bounded context；
- 是否把历史偶然差异永久化；
- 是否诱导 union interface、mode flag、额外 wrapper 或 speculative seam；
- 是否把复杂度转移到 helper、adapter、registry、配置或 caller；
- consumer reassembly 是否仍存在，只是换了位置；
- 是否从 capability ownership 无证据推导出更大的 execution / orchestration ownership；
- 是否为了闭合当前 capability，把相邻 subsystem 的合法 authoritative ownership 也集中进来；
- 是否在缺少 stable semantic / invariant / change-boundary evidence 时，把 current implementation/snapshot partition 冻结成长期 architecture contract；
- 是否没有真实 replacement/exit；
- 是否存在代码无法裁决的 Human-owned 业务或兼容决定。

反证成立时替换或缩小受影响 judgment；不成立时保留最重要 guard。

## Progressive Brooks constraints

Brooks 是架构设计约束，按成熟度逐步吸收：

```text
Architecture Intent
→ 识别与方向相关的 Brooks constraints
→ Target design 把 constraints 变成设计决定
→ Implementation / verification 用代码和测试证明
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
4. Architecture contribution 闭合 `evolution horizon → domain/identity constraint → target pressure → durable capability`；没有 authoritative horizon 时，只从跨边界 pressure 推导最小 durable outcome，不发明战略口号；
5. 四个 architecture directions 之一被选为主要结构杠杆，但不替代 Architecture contribution；
6. downstream design / goal compiler 无需重新发现“为什么值得推进”，同时 intent 不锁死 target design 或实现模式；
7. desired end state 描述结果，不锁死实现模式；
8. in scope、out of scope 和 must preserve 清楚；
9. 只保留与当前 intent 相关、后续设计真正需要回答的 obligations；
10. ownership materially shapes intent 时，owner scope 只扩到 evidence 支持的 invariant，并只记录会改变 boundary 的 preserved / adjacent ownership relation；
11. 至少一个可观察的 replacement/exit 目标；
12. 若存在 material Unknown，已通过 falsification chain 关闭，或明确为什么它不会阻止 intent；不存在时不制造；
13. success evidence 直接引用 Architecture contribution 与当前 intent 的关键 claim；AI-native / agentic horizon 适用时证明 intervention boundary 与 independent verification；动态 scope 有 derivation，具体 provider 只在其本身属于稳定判卷标准或必须消除歧义时固定；
14. 已检查最重要反例、architecture altitude、consumer reassembly、owner-scope 和 materialization guard；
15. 已携带与当前方向相关、需要下游逐步吸收的 Brooks constraints。
