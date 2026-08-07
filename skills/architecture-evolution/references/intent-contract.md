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
- Stable acceptance rule: <实现完成时必须成立的 invariant / proof，以及动态 affected scope 的推导方法>
- Replacement evidence: <证明旧路径、知识、判断或依赖确实退出>
```

只写与当前 pressure、desired end state 和 primary architecture direction 直接相关的 Brooks constraints，不为覆盖 R1–R6 而制造无关内容。

如果当前具体 app、target、config、binding 或文件样本有助于说明 grounding，可以在 `Success evidence` 后追加：

```markdown
## Current snapshot evidence
- <只记录当前观察到的具体样本；除非它本身是稳定 contract，否则不得冻结为长期验收集合>
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
- consumer reassembly 是 cross-cutting signal，不是第五个架构方向；
- ownership intent 必须界定当前 capability 要闭合的 invariant/contract，并说明它与 request/execution/orchestration 以及相邻 subsystem ownership 的关系；不得从 capability ownership 无证据扩张出更大的 execution ownership，也不得为闭合当前 capability 无证据集中相邻 subsystem 的合法 ownership；
- 必须保留真实业务差异和 Protected behavior；
- `Real Evolution` 必须提出至少一个具体退出目标；
- Material Unknown 存在时必须通过 `claim at risk → minimal probe → evidence → intent changed / retained` 进入控制；不存在时不输出该 section，禁止制造；
- Challenge 必须检查 false unification、历史差异固化、speculative abstraction、复杂度转移、consumer reassembly、owner-scope expansion 和退出真实性；
- reasoning distinction 不自动成为 type、provider、adapter、layer 或 public seam；
- Brooks 是下游架构设计逐步吸收的约束；intent 只携带相关约束和必要 proof expectation，不输出全量风险表、Severity、PASS/RETRY 或 Health Score；
- Success evidence 必须以稳定 acceptance rule 为主；会随 runtime/config/deployment binding、changed boundary/ownership 或时间变化的具体对象只作为 current snapshot evidence，并在实现验收时重新推导 affected scope；
- 目标设计、任务拆分、迁移步骤和实现属于后续工作。
