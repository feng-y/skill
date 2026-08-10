# Architecture Intent Rules

只在需要 architecture judgement 时读取。本文件不定义 Flow，也不定义最终输出模板。

## Start from pressure

有效 intent 必须能追溯到真实压力，例如：

- 同一业务规则或配置解释反复在多处修改；
- 新需求持续增加特殊入口、mode flag 或 provider/family switch；
- 事故、回归或测试脆弱性集中在同一结构边界；
- 调用者必须知道内部步骤、状态、生命周期或实现类型；
- 一个模块同时承受多个不相关变化；
- 新抽象增加，但旧路径、旧事实源和旧判断仍存在；
- common/core/Harness/Runtime 被具体场景或 provider 牵引。

文件大、函数长、目录不整齐、模式不优雅或单次局部修改，不单独构成 architecture intent。

## Architecture or local

形成 architecture intent 通常需要同时看到：

- pressure 会重复出现或恢复成本高；
- 一个结构原因造成多个可观察后果；
- 影响跨越单个局部实现，但仍能限定边界；
- 需要重新确定业务语义、责任 owner、稳定 contract 或依赖方向；
- 可以说明完成后什么旧知识、路径、判断、责任或依赖会退出。

否则保持局部，不升级。

## Reality lenses

只展开会改变判断的观察面：

1. **Business semantics** — 哪些路径表达同一业务，哪些属于不同 bounded context；事实和规则的权威解释在哪里。
2. **Ownership & lifecycle** — config、runtime resource、state、publication、reload 和 lifetime 由谁真正拥有。
3. **Consumer knowledge / reassembly** — caller 是否仍需组合 implementation、configuration、ordering、lifecycle、identity 或 access facts 才能使用 capability。
4. **Source dependency** — policy、contract、implementation 的源码依赖方向是否稳定。
5. **Runtime control / consumption** — 谁在运行时选择、构造、驱动和消费 capability。

一个观察面整洁不能替另一个作证：clean interface 不等于 ownership 已闭合；clean dependency graph 不等于 runtime control 正确。

### Consumer reassembly

当 caller 仍需重新组合本应属于 capability owner 的 configuration、implementation、lifecycle、ordering、identity 或 access facts，capability boundary 尚未闭合。

纯 composition-root wiring 不自动算 reassembly：如果它只选择 implementation，没有承载业务 policy、runtime sequencing、lifecycle ownership 或 usage knowledge，就是合法组装边界。

### Ownership scope

Capability ownership 只闭合当前 capability 的 invariant、state/lifetime 和 usage contract，不自动包含 request execution、orchestration 或相邻 subsystem。

ownership 只能扩到 evidence 支持的 invariant。相邻 subsystem 已有正确 authoritative owner 时，优先稳定 relation/contract，不默认把其 config、resource、lifecycle 一并集中。

## Architecture diagnosis directions

下面四个方向是内部 discriminator，不是最终 artifact 的固定 taxonomy。一个 intent 可以同时命中多个 lens，最终判断必须来自具体 evidence。

1. **Business Semantic Integrity**
   - 同一业务是否存在多套语义或事实解释？
   - 是否可能错误合并不同 bounded context？

2. **Stable Abstraction with Explicit Variation**
   - caller 是否依赖 implementation difference 而不是业务能力？
   - 哪些 variation 是 essential，哪些只是历史残留？
   - current implementation partition 本身不证明 variation 应长期存在。

3. **Cohesive Capability Ownership**
   - capability、invariant、state、lifetime 是否有清楚 owner？
   - 是否仍由 caller、helper、global state 共同拼装？

4. **Unidirectional Policy Dependency**
   - 稳定 policy 是否被 provider、场景或 implementation 反向定义或控制？
   - 是否存在 `common→scenario`、`policy→provider` 或隐式反向控制？

## Real Evolution

Intent 必须指向真实减少，而不是再加一层。至少应有一项旧东西真正退出：

- 平行业务语义；
- 重复事实解释；
- caller 内部知识或 capability reassembly；
- 无效抽象或特殊入口；
- 反向或循环依赖；
- 永久兼容分支。

如果只能说“增加 facade/interface/manager/registry”，intent 尚未成立。

Observed partition 是 evidence，不是 architecture boundary。只有它承载稳定 semantics/invariant、闭合 ownership、essential variation 或长期 change boundary 时，才值得成为后续设计的基本形态。

好的 architecture direction 优先表达为少量 stable invariant / boundary：什么必须始终成立，哪些变化仍允许局部自主。不要把 class/API/library choice 当成架构规范。一个 invariant 稳定到值得长期约束时，应能被 repo structure、文档或工具清楚表达；本 Skill 只识别这个 judgement，不设计具体 lint/test。

## Material unknown

只有会改变 intent 或 boundary 的 unknown 才是 Material Unknown。

```text
Claim at risk → Minimal probe → Evidence → Intent changed / retained
```

未关闭的 Material Unknown ⇒ `Status: Intent unresolved`。不会改变判断的 unknown 不升级；已经关闭的 unknown 不继续作为 active blocker。

## Evidence lifetime

同一事实或 judgment 只保留一份当前 authoritative state。前提未变就复用；新 authoritative evidence 改变前提时，只 reopen 并替换受影响判断，不把新旧 snapshot 并列为 active truth。

## Challenge

重点找会推翻或缩小 intent 的反证：

- 其实只是局部修复；
- false-unify 不同 bounded context；
- 把历史偶然差异永久化；
- speculative abstraction 或 mode/union interface；
- complexity 只是搬到 helper/adapter/registry/caller；
- consumer reassembly 仍然存在；
- ownership 无证据扩到 execution/orchestration/adjacent subsystem；
- 没有真实 replacement / exit；
- 存在代码无法裁决的 Human-owned 业务或兼容决定。

需要 Brooks 约束时读取 `brooks-constraints.md`；Brooks 只帮助 challenge judgement，不形成独立报告。
