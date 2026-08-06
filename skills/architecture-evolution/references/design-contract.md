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

## Evidence state

### Observed
<代码、调用、配置、状态、测试、运行证据、历史或 ADR 可直接证明的事实>

### Inferred
<由证据支持的业务与架构解释>

### Residual Unknown
<不会改变当前业务定义和目标结构，只影响实现或验证的事项>

## Business reality

### Current paths
| Path / entry | Business purpose | Input / output / error | State / lifecycle | Current owner | Evidence |
| --- | --- | --- | --- | --- | --- |

### Same business judgment
- Same capability:
- Evidence:
- Different capability or bounded-context exclusions:
- Counterexample checked:

### Shared semantics
- Canonical input:
- Canonical output:
- Error semantics:
- Invariants:
- State / lifecycle:
- Required side effects:

### Difference classification
| Difference | Essential or accidental | Evidence / reason | Target handling |
| --- | --- | --- | --- |

## Primary architecture break
- Principle:
- Structural consequence:
- Evidence:
- Root cause:
- Why architectural rather than local:
- Counterexample checked:
- Confidence:

## Secondary consequences
<最多两个；说明它们如何由主要根因产生，以及为什么不单独设计第二套方案>

## Target architecture

### Canonical business capability
- Name:
- Responsibility:
- Business contract:
- Owned invariants:
- Must remain distinct from:

### Stable abstraction
- Capability surface:
- Callers provide:
- Callers receive:
- Callers no longer know:
- Why this abstraction is stable:

### Explicit variation points
| Variation | Why essential | Owner | Input / output | Hidden implementation detail |
| --- | --- | --- | --- | --- |

### Cohesive module design
| Module / internal collaborator | Complete responsibility | Owned state / lifecycle | Public or private | Must not own |
| --- | --- | --- | --- | --- |

### Dependency direction
- Policy layer:
- Stable capability:
- Implementation / adapter layer:
- Composition owner:
- Upward evidence / result path:
- Forbidden edges to remove:

## Design delta

### Keep
<已正确表达业务或稳定 contract 的现有部分>

### Move
<责任、状态、生命周期或 variation 从哪里移动到哪里>

### Merge
<哪些平行业务、重复抽象或浅模块收敛成一个 capability>

### Delete
<哪些旧路径、特殊入口、switch、事实解释、wrapper、反向依赖或调用者知识退出>

### Do not change
<防止扩大重设计的受保护范围>

## Protected behavior
- Input / output:
- Errors:
- Config compatibility:
- State / lifecycle:
- Order:
- Side effects / external contracts:
- Performance / observability boundary:
- Essential differences to preserve:
- Acceptable differences:

## Improvement verification
| Dimension | Before | Expected after | How to verify |
| --- | --- | --- | --- |
| Business semantic integrity | | | |
| Variation containment | | | |
| Capability cohesion | | | |
| Unidirectional dependency | | | |
| Real replacement | | | |

## Real Evolution challenge
- False business unification risk:
- Union abstraction / mode-flag risk:
- Over-splitting or mixed-responsibility risk:
- Reverse dependency or control risk:
- Complexity relocation risk:
- Old path still carrying weight:
- ADR / compatibility conflict:

## Next handoff
<单一推荐设计，以及能够证明 canonical capability 与最小 replacement 的实现边界>
```

## Discipline

- 一个主要架构断点，不输出 smell 清单；
- 先证明“同一业务”，再设计统一抽象；
- 本质差异必须保留并拥有明确 variation point；
- 只给一个推荐设计；
- `Observed / Inferred / Unknown` 不混写；
- 必须有具体 `Delete`；没有物理删除时，写明消失的平行业务语义、调用者知识、重复判断或反向依赖；
- improvement 只能写可观察 delta，不能只写“统一”“解耦”“更 SOLID”；
- 实现顺序属于下游任务书，不写进本合同。
