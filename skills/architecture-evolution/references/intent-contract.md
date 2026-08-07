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
- Key evidence:

## Boundary
- In scope:
- Out of scope:
- Must preserve:

## Design obligations
- Business semantics to unify or keep distinct:
- Essential variations to preserve:
- Capability / ownership question to resolve:
- Dependency direction to establish:
- Old path, knowledge or dependency that must exit:

## Progressive Brooks constraints

| Risk | Design constraint | Why applicable | Guard | Proof expected |
| --- | --- | --- | --- | --- |

只写与当前 pressure、desired end state 和 primary architecture direction 直接相关的约束，不为覆盖 R1–R6 而制造无关内容。

## Unknown and guard
- Key Unknown:
- How it was closed or why it does not block intent:
- Counterexample checked:
- Applicable guard:

## Success evidence
- Evidence that the intent was implemented correctly:
- Evidence that replacement actually happened:
```

## Discipline

- 一个 intent，不输出候选清单；
- 描述 outcome，不提前指定实现模式；
- `Observed / Inferred / Unknown` 不混写；
- 必须说明为什么不是局部修改；
- 四个架构方向必须保留为 intent shaping lenses，并选择一个 primary direction；
- 必须保留真实业务差异和 Protected behavior；
- `Real Evolution` 必须提出至少一个具体退出目标；
- Challenge 必须检查 false unification、历史差异固化、speculative abstraction、复杂度转移和退出真实性；
- Brooks 是下游架构设计逐步吸收的约束；intent 只携带相关约束，不输出全量风险表、Severity、PASS/RETRY 或 Health Score；
- 目标设计、任务拆分、迁移步骤和实现属于后续工作。
