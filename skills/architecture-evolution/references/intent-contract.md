# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取和输出。本文件只定义最终 Intent 的物理形状；architecture judgment、ready/discriminator 规则由 `SKILL.md` / `rules.md` 拥有，不在这里复制第二套判定逻辑。

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

- 一个 intent；描述 outcome，不提前指定实现模式、任务拆分或迁移步骤；
- 只输出当前仍有效的 architecture judgment / evidence；旧 snapshot 若已被 authoritative reality 推翻，只保留必要 provenance，不与新判断并列为 active state；
- `Observed / Inferred / Unknown` 不混写；Material Unknown、snapshot evidence 和 guard 只在适用时出现，不填空占位；
- primary direction、Design obligations、Brooks constraints、replacement / exit 和 success evidence 只输出当前 evidence 实际支持的内容；
- 目标设计、任务拆分、迁移步骤和实现属于后续工作。
