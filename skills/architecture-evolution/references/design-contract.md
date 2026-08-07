# Architecture Design Contract

只在 `Status: Design ready` 时读取和输出。

```markdown
# Architecture Design Contract

Status: Design ready

## Search frame
- Area:
- Change pressure:
- Scope:
- Out of scope:

## Opportunity selection

| Candidate | Pressure evidence | Structural consequence | Candidate boundary | What could exit | Decision |
| --- | --- | --- | --- | --- | --- |

- Selected opportunity:
- Why this one now:
- Why architectural rather than local:
- Deferred candidates and reason:

## Evidence
### Observed
### Inferred
### Residual Unknown

## Business reality

### Current paths
| Path / entry | Business purpose | Contract / lifecycle | Current owner | Evidence |
| --- | --- | --- | --- | --- |

### Same-business judgment
- Canonical capability:
- Shared semantics:
- Different-business exclusions:
- Counterexample checked:

### Difference classification
| Difference | Essential or accidental | Evidence | Target handling |
| --- | --- | --- | --- |

## Primary architecture break
- Principle:
- Structural consequence:
- Root cause:
- Evidence:
- Counterexample checked:
- Confidence:

## Secondary consequences
<最多两个；说明它们如何由主要根因产生>

## Target architecture

### Canonical business capability
- Name / responsibility:
- Input / output / errors:
- Invariants / state / lifecycle:
- Must remain distinct from:

### Stable abstraction
- Capability surface:
- Callers provide / receive:
- Callers no longer know:
- Why stable:

### Explicit variation points
| Variation | Why essential | Owner | Contract | Hidden detail |
| --- | --- | --- | --- | --- |

### Cohesive module design
| Module / collaborator | Complete responsibility | Owned state / lifecycle | Public or private | Must not own |
| --- | --- | --- | --- | --- |

### Dependency direction
- Source dependency: `policy → contract ← implementation`
- Runtime control: policy invokes downward; result / evidence returns upward
- Composition owner:
- Forbidden edges to remove:

## Design delta
### Keep
### Move
### Merge
### Delete
### Do not change

## Protected behavior
- Inputs / outputs / errors:
- Config / compatibility:
- State / lifecycle / order:
- Side effects / external contracts:
- Performance / observability:
- Essential and acceptable differences:

## Grill record

| Challenge | Counterevidence checked | Result | Design correction |
| --- | --- | --- | --- |
| Reality conflict | | | |
| False unification / difference collapse | | | |
| Union abstraction / speculative seam | | | |
| Mixed or over-split ownership | | | |
| Reverse dependency / hidden control | | | |
| Complexity relocation | | | |
| Migration and deletion reality | | | |

## Brooks constraints

| Risk | Severity | Symptom | Source | Consequence | Remedy in target design | How to verify | Residual / tradeoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5 Dependency Disorder | | | | | | | |
| R6 Domain Model Distortion | | | | | | | |
| R2 Change Propagation | | | | | | | |
| R3 Knowledge Duplication | | | | | | | |
| R4 Accidental Complexity | | | | | | | |
| R1 Cognitive Overload | | | | | | | |

- Brooks verdict: PASS / RETRY

## Implementation boundary
- Minimum replacement slice:
- Required migration / deletion evidence:
- Design assumptions that must be re-opened if disproved:
```

## Discipline

- 开放范围最多三个有证据候选，最终只选择一个热点；
- 已知热点也必须证明它是架构机会，而不是局部修复；
- 一个主要架构断点、一个推荐设计；
- `Observed / Inferred / Unknown` 不混写；
- 先证明“同一业务”，再设计统一抽象；
- 本质差异必须保留在明确 variation point；
- `Delete` 必须具体；没有物理删除时，写明消失的平行业务语义、调用者知识、重复判断或反向依赖；
- Grill 必须记录实际检查的反证和由此发生的设计修正，不得只写“通过”；
- Brooks constraints 必须扫描 R1–R6；适用 finding 使用 `Severity → Symptom → Source → Consequence → Remedy → How to verify`；
- `No finding` 也要写最关键 false-positive guard；
- 不调用或依赖外部 Wayfinder、Improve、Grill 或 Brooks Skill；
- 不生成 Health Score；未完成实现和代码扫描时，不声称行为保持、迁移完成或旧路径已经删除；
- 实现顺序属于下游工作，不在本合同中展开成任务书。
