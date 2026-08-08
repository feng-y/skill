# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取和输出。

```markdown
# Architecture Intent

Status: Architecture intent ready

## Direction
- Intent:
- Why now:
- Desired end state:
- Primary architecture direction:
  - Business Semantic Integrity / Stable Abstraction with Explicit Variation / Cohesive Capability Ownership / Unidirectional Policy Dependency

## Reality
- Area:
- Observed pressure:
- Structural consequence:
- Why architectural rather than local:
- Decisive reality and evidence:

## Boundary
- In scope:
- Out of scope:
- Must preserve:

## Design obligations
- <只写与当前 intent 相关的 Business semantics / Essential variation / Ownership / Consumer reassembly / Dependency direction obligation>
- Replacement / exit: <至少一个必须退出的旧路径、知识、判断或依赖>

## Progressive Brooks constraints

| Risk | Design constraint | Why applicable | Guard | Proof expected |
| --- | --- | --- | --- | --- |

## Challenge
- Counterexample checked:
- Applicable guard: <only when needed>

## Success evidence
- Stable acceptance rule: <直接引用当前 intent 已承诺的关键 outcome / invariant / must-preserve / replacement，说明实现完成时哪些必须得到实际证明；不要另写第二套完成条件。affected scope 动态变化时写届时的 scope derivation；具体 evidence provider 由后续按 repo verification authority 和最终 change surface 选择，除非 provider 本身是稳定受保护判卷标准或必须点名才能消除歧义>
- Replacement evidence: <证明旧路径、知识、判断或依赖确实退出>
```

只写与当前 pressure、desired end state 和 primary architecture direction 直接相关的 Brooks constraints，不为覆盖 R1–R6 而制造无关内容。

如果 affected scope 会动态变化，或当前具体样本有助于说明 grounding，可以在 `Success evidence` 后按需追加；两项都只在适用时写，不填 `None`：

```markdown
## Current snapshot evidence
- Scope derivation: <仅在 affected scope 动态变化时，说明实现验证如何从最终 change surface 与届时 effective binding/config/runtime reality 推导受影响范围>
- Current snapshot: <仅在当前样本有助于 grounding 时记录；除非本身是稳定 contract，否则不得冻结为长期验收集合>
```

只有真实存在会改变 intent、boundary 或 design obligation 的 material unknown 时，才在 `Success evidence` 前追加：

```markdown
## Material unknown
- Claim at risk:
- Minimal probe:
- Evidence:
- Intent changed / retained:
```

## Discipline

- 一个 intent，不输出候选清单；
- 描述 outcome，不提前指定实现模式；
- `Observed / Inferred / Unknown` 不混写；
- Reality 只保留实际改变判断的 semantics / ownership / consumer / source dependency / runtime control 证据，不机械输出五面审计；
- Design obligations 只输出适用项，不为覆盖四个方向或 consumer reassembly 而填满固定字段；
- 必须说明为什么不是局部修改；
- 四个架构方向必须保留为 intent shaping lenses，并选择一个 primary direction；
- consumer reassembly 是 cross-cutting signal，不是第五个架构方向；观察到的 usage partition 只形成 evidence，不自动定义长期 public abstraction；
- Stable Abstraction 的 variation 必须由稳定 semantic / invariant difference 支撑；current implementation partition 只作为 evidence，不自动成为长期 taxonomy；
- ownership materially shapes intent 时，owner scope 只能扩到 evidence 支持的 invariant；preserved execution/orchestration 或 adjacent subsystem ownership 只有会改变 boundary/obligation 时才需要显式记录；不得无证据扩大或集中 ownership；
- 必须保留真实业务差异和 Protected behavior；
- `Real Evolution` 必须提出至少一个具体退出目标；
- Material Unknown 存在时必须通过 `claim at risk → minimal probe → evidence → intent changed / retained` 进入控制；不存在时不输出该 section，禁止制造；
- Challenge 必须检查 false unification、历史差异固化、speculative abstraction、复杂度转移、consumer reassembly、owner-scope expansion、退出真实性，以及是否在缺少 stable semantic / invariant evidence 时把 current implementation/snapshot partition 冻结成长期 architecture contract；
- reasoning distinction 或 observed partition 不自动物化为 architecture artifact；
- Brooks 是下游架构设计逐步吸收的约束；intent 只携带相关约束和必要 proof expectation，不输出全量风险表、Severity、PASS/RETRY 或 Health Score；
- Success evidence 直接引用 intent 已承诺的结果、invariant、must-preserve 和 replacement，不再转写第二套完成语义；具体 provider 由后续基于 repo verification authority 和最终 change surface 选择，动态当前对象只作为 snapshot evidence；
- 目标设计、任务拆分、迁移步骤和实现属于后续工作。
