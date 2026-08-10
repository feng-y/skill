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
- 可以说明完成后什么旧知识、路径、判断、责任或依赖会退出。

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

`Consumer reassembly` 是 cross-cutting signal，不是独立 architecture direction。

当调用者为了使用一个 capability，仍需重新组合本应属于 capability owner 的 configuration、implementation、lifecycle、ordering、identity 或 access facts，则 capability boundary 尚未闭合。纯 composition-root wiring 不自动构成 consumer reassembly：如果它只选择具体 implementation、没有承载业务 policy、runtime sequencing、lifecycle ownership 或 capability usage knowledge，则保留为合法组装边界。

### Ownership scope

`Cohesive Capability Ownership` 只要求当前 capability 的 invariant、state/lifetime 和 usage contract 闭合；它本身不证明 execution、orchestration 或相邻 subsystem 也应归同一 owner。

ownership 只能扩到 evidence 支持的 invariant 边界。`capability ownership` 不自动蕴含 `execution ownership`，`ownership closure` 也不自动要求 `ownership centralization`。如果相邻 feature/runtime/resource subsystem 已有内聚 owner，不因当前 caller reassembly 就默认把其内部 config、resource 或 lifecycle 全部迁入当前 owner；只有 evidence 证明该 ownership 本身错误时才改变它。

## Architecture diagnosis directions

下面四个方向必须保留，作为内部 architecture discriminator；它们帮助解释压力、挑战 intent 和生成目标 architecture identity，**不是最终 artifact 的固定 taxonomy**，也不要求向用户输出名称。

一个 intent 可以同时命中多个 lens；reasoning 中可以选择一个 primary direction 强制收敛，但最终输出必须来自具体代码现实，而不是从 taxonomy 名称反推设计。

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

Intent 必须指向真实减少，而不是新增一层。至少能提出一个后续需要实现的退出目标：

- 平行业务语义；
- 重复事实解释；
- 调用者内部知识或 capability reassembly；
- 无效抽象或特殊入口；
- 反向或循环依赖；
- 永久兼容分支。

如果只能说“增加 facade/interface/manager/registry”，intent 尚未成立。

## Explain first, materialize later

用于解释现实的 distinction 或 partition 可以先停留在 reasoning vocabulary。**Observed partition 是 evidence，不是 architecture boundary。** 只有 evidence 表明新的 seam 会承载稳定 semantics/invariant、闭合 ownership、承载 essential variation 或形成长期 change boundary 时，才把它作为 possible target identity 交给后续设计；否则保留为解释模型或 guard。

Possible target identity 只描述基本架构形态，例如稳定 semantic owner、generation-scoped capability、独立 execution capability 或 policy/implementation dependency relation。它不能规定具体 class、interface、API、adapter、对象组合、调用流程或 responsibility placement。

## Material unknown falsification

只有会改变 Architecture Intent、Boundary 或 target architecture identity 的 unknown 才是 material unknown。存在这类 unknown 时，关闭它至少使用下面的控制链：

```text
Claim at risk
→ Minimal territory probe
→ Evidence
→ Intent changed / retained
```

- `Claim at risk`：明确哪个 architecture judgment 会被该未知推翻或缩小；
- `Minimal territory probe`：只调查足以裁决该 claim 的最小事实；
- `Evidence`：记录代码、runtime、历史或 Human 决定；
- `Intent changed / retained`：明确 evidence 如何改变或保留 intent/boundary/target identity。

如果当前没有 material unknown，不要为了满足输出结构制造一个。若 unknown 被命名后不改变任何下一步，它不是 material control signal，不要把它作为正式 blocker 装饰输出。

## Evidence and judgment lifetime

Architecture reality、material claim 和由其支持的 architecture judgment 都有前提。保持 **one judgment, one active owner**：同一事实或判断只保留一份当前 authoritative state，历史说明可以作为 provenance，但不能和已更新判断并列为 active truth。

- 支撑 judgment 的代码、runtime、binding/config、业务语义、owner boundary 或 Human authority 前提未变化时，直接复用已有 Evidence 和判断；不要因为从 Ground 进入 Discover / Shape / Challenge、换了 lens 或开始 Brooks 检查就重新发现、重新论证；
- 新 authoritative Evidence 改变前提时，只 reopen 受影响的 claim，并在原 semantic owner 处替换或失效旧判断；只传播到受影响的 Intent / Boundary / target identity，不重算无关部分；
- 新旧 snapshot 不得同时作为有效依据。若需要保留旧状态解释历史，只标为 provenance / prior snapshot，不参与当前 architecture judgment；
- 动态变化的具体对象列表只是 current evidence，除非它本身就是稳定 contract；最终输出只保留足以解释 intent 的决定性证据，不冻结实现验收集合。

## Challenge the intent

Challenge 从**当前仍有效的 best-known intent** 出发寻找会推翻、缩小或改变 boundary/target identity 的反证；前提没有变化的 judgment 直接复用，不重新跑一遍完整 architecture analysis、所有 reality lenses 或 Brooks 清单。

重点检查：

- 问题是否其实是局部修复；
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

反证成立时替换或缩小受影响 judgment；不成立时只把会改变最终 intent 含义的 guard 沉淀为普通架构语言。`Counterexample checked`、taxonomy 命中和 challenge 过程本身不进入最终 artifact。

## Brooks challenge

Brooks 是内部 architecture challenge lens，不是 Architecture Intent 的输出 section：

```text
Best-known intent / possible target identity
→ relevant Brooks challenge
→ reject / narrow / guard
→ Architecture Intent
```

- `R6 Domain Model Distortion` — 不能按代码形状错误统一真实不同的业务语义；
- `R2 Change Propagation` — 共同规则和 variation 的变化应收敛到权威位置；
- `R3 Knowledge Duplication` — 同一业务决定和事实解释应只有一个权威来源；
- `R4 Accidental Complexity` — 新 abstraction 必须吸收真实变化并替代旧结构；
- `R5 Dependency Disorder` — 设计方向不能强化反向 policy/control dependency；
- `R1 Cognitive Overload` — capability/module 应让 caller 少知道步骤、状态、顺序和实现类型。

Brooks 编号、Risk/Guard/Proof 表、PASS/RETRY、Health Score 和完整 proof expectation 不输出。完整 guard 按需读取 `brooks-constraints.md`。

## Intent quality gate

`Architecture intent ready` 必须满足：

1. 仍然只有一个明确 intent，不是并列多个改造项目；
2. 有真实 pressure 和代码证据；
3. 能用一个 architecture problem identity 解释主要压力，并说明为什么是架构问题而不是局部修复；
4. 能解释当前结构形成的关键背景，尤其是已失效的历史前提、variation 或 boundary 假设；
5. desired end state 描述结果和基本 architecture identity，不锁死实现模式；
6. 如果存在多个值得比较的 target identity，只保留 1–3 个基本形态，并且它们仍服务于同一个 intent；
7. in scope、out of scope 和 must preserve 清楚；
8. ownership materially shapes intent 时，owner scope 只扩到 evidence 支持的 invariant；
9. 至少一个可观察的 replacement/exit 目标；
10. 若存在 material Unknown，已通过 falsification chain 关闭，或明确为什么它阻止 ready；不存在时不制造；
11. 已检查最重要反例、consumer reassembly、owner-scope、false unification、complexity relocation 和 materialization guard；
12. Brooks 只用于内部 challenge，最终 artifact 不泄漏 Brooks 表、taxonomy、counterexample 或 proof machinery；
13. 输出没有进入具体 class/interface/API/adapter、responsibility placement、调用/执行流、迁移步骤、implementation slice 或 verification plan；一旦需要回答这些问题，就停止并交给后续目标设计。
