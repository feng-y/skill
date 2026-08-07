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

用于解释现实的 role、provider、primary/support、variation、ownership 或阶段性 distinction，可以先停留在 reasoning vocabulary。发现一个有用概念，不等于应该创建一个新的 type、adapter、provider、layer 或 public seam。

只有当前 evidence 表明新的 seam 会实际收敛 ownership、减少 caller knowledge、承载 essential variation 或建立更稳定的 verification surface 时，才把它交给后续设计物化。否则保留为解释模型或 guard。

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

## Evidence lifetime

Success evidence 要区分**稳定验收规则**与**当前 snapshot evidence**。

- 稳定验收规则描述实现完成时必须成立的 invariant 和 proof；只有 affected scope 会随 runtime/config/deployment binding、changed boundary/ownership 或时间变化时，才同时写明届时的 scope 推导方法；
- 会动态变化的具体对象列表只能作为 current snapshot evidence，除非它本身就是稳定 contract；
- 对动态 affected targets，应在实现验收时根据最终 changed boundary/ownership 与届时 effective runtime/config/deployment state 重新推导并覆盖全部受影响对象；replay 是适用时的一种 proof，而不是所有 architecture intent 的固定验收机制。

当前具体样本可以保留来证明 intent grounded，但必须标明它是 `current evidence`，不能替代稳定 acceptance rule。

## Challenge the intent

在 ready 前寻找会推翻或缩小方向的反证：

- 问题是否其实是局部修复；
- 是否错误统一不同 bounded context；
- 是否把历史偶然差异永久化；
- 是否诱导 union interface、mode flag、额外 wrapper 或 speculative seam；
- 是否把复杂度转移到 helper、adapter、registry、配置或 caller；
- consumer reassembly 是否仍存在，只是换了位置；
- 是否从 capability ownership 无证据推导出更大的 execution / orchestration ownership；
- 是否为了闭合当前 capability，把相邻 subsystem 的合法 authoritative ownership 也集中进来；
- success evidence 是否把动态 snapshot 冻结成长期 contract；
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
7. 只保留与当前 intent 相关、后续设计真正需要回答的 obligations；
8. ownership materially shapes intent 时，owner scope 只扩到 evidence 支持的 invariant，并只记录会改变 boundary 的 preserved / adjacent ownership relation；
9. 至少一个可观察的 replacement/exit 目标；
10. 若存在 material Unknown，已通过 falsification chain 关闭，或明确为什么它不会阻止 intent；不存在时不制造；
11. success evidence 使用稳定 acceptance rule；只有 affected scope 动态变化时才要求 scope derivation，当前样本只作为 snapshot evidence；
12. 已检查最重要反例、consumer reassembly、owner-scope 和 materialization guard；
13. 已携带与当前方向相关、需要下游逐步吸收的 Brooks constraints。
