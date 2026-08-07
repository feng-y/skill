# Architecture Design Contract

只在 `Status: Design ready` 时读取和输出。

```markdown
# Architecture Design Contract

Status: Design ready

## Target
- Target:
- Trigger:
- Scope:
- Out of scope:

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
- Why architectural:
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

## Real Evolution challenge
- False unification:
- Union abstraction / mode flags:
- Mixed or over-split modules:
- Reverse dependency / control:
- Complexity relocation:
- Old path still load-bearing:
- ADR / compatibility conflict:

## Northstar handoff

仅当用户明确要求进入实现且 `Brooks verdict: PASS` 时填写 `Ready`；用户只要设计时写 `None`。

- Handoff: None / Ready
- Design source: <本合同的路径、引用或稳定标识，以及产生判断的 repo snapshot>
- Goal seed: <实现已确认目标架构、保留 Protected behavior，并让 Delete 中的旧结构退出>
- Target: <capability / module / hotspot>
- Architecture decisions: <canonical capability、stable abstraction、variation points、cohesive ownership、dependency direction>
- Design delta: <Keep / Move / Merge / Delete / Do not change>
- Implementation boundary: <证明目标设计成立所需的最小代码与迁移范围>
- Protected behavior: <必须保持的行为与允许差异的引用>
- Verification obligations: <Brooks findings、残留风险和实现后必须取得的代码/测试证据>
- Design invalidation triggers: <会推翻同一业务判断、essential difference、目标 contract 或 Protected behavior 的新证据>

Authority：Northstar 可以编译任务书、安排实现切片、迁移顺序和验收；不得重新选择业务语义、抽象、模块 owner 或依赖方向。Task 0 若发现 design invalidation trigger，必须停止受影响实现并回到 Architecture Evolution，而不是在 Northstar 内改写架构。
```

## Discipline

- 先证明“同一业务”，再设计统一抽象；
- 本质差异必须保留在明确 variation point；
- 一个主要架构断点、一个推荐设计；
- `Observed / Inferred / Unknown` 不混写；
- `Delete` 必须具体；没有物理删除时，写明消失的平行业务语义、调用者知识、重复判断或反向依赖；
- Brooks constraints 必须扫描 R1–R6；适用 finding 使用 `Severity → Symptom → Source → Consequence → Remedy → How to verify`；
- `Source` 引用 Brooks risk code 及对应经典原则或 smell；
- `No finding` 也要写最关键 false-positive guard；
- 不调用或依赖外部 Brooks / brooks-lint Skill；
- 不生成 Health Score；未完成实现和全仓库扫描时，分数没有可信含义；
- 只有 `Design ready + Brooks PASS + 用户要求实现` 才输出 `Handoff: Ready`；其他情况不得伪造可执行 handoff；
- handoff 固化架构决定和失效条件，不编排实现步骤；实现顺序属于 Northstar 任务书。
