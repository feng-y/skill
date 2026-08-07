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

### Source
- Design: <本合同的路径或稳定引用>
- Snapshot: <产生本设计的 repo commit / branch>

### Scope
- Target: <本次实现的 capability / module / hotspot>
- Implement: <证明目标设计成立所需的最小代码与迁移范围>
- Do not change: <本轮禁区与不可重判的设计边界引用>

### Delta
- Keep:
- Move:
- Merge:
- Delete:

### Proof
- Preserve: <Protected behavior 引用>
- Prove: <实现后必须取得的代码、测试、迁移与删除证据>
- Return when: <新证据使本合同中的业务判断、essential difference、目标结构或 Protected behavior 不再成立>

Authority：`Source` 指向的 Architecture Design Contract 是架构决定的唯一事实源。Northstar 只编译实现、迁移和验收，不复制或重新裁决架构；`Proof.Return when` 命中时停止受影响实现并返回 Architecture Evolution。
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
- handoff 只传 `Source / Scope / Delta / Proof`；完整架构决定保留在 Source 指向的合同中；
- 实现顺序属于 Northstar 任务书。
