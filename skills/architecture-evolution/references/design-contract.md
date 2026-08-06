# Architecture Design Contract

只选择一个状态，并只输出该状态需要的信息。证据不足或无需架构调整时，不填写完整设计模板。

## Status: No architecture change

```markdown
Status: No architecture change

## Target
- Target:
- Trigger:
- Scope:

## Observed evidence
<证明 owner 与变化边界已经足够局部的事实>

## Why local
<为什么候选 signal 不构成规则违反；包含检查过的反例>

## Local change boundary
<最小修改区域，以及明确不应扩大到的结构>
```

禁止输出 target seam、责任重构或 Design Delta。

## Status: Research required

```markdown
Status: Research required

## Target
- Target:
- Trigger:
- Scope:

## Confirmed reality
### Observed
### Inferred

## Design-changing Unknown
- Unknown:
- Why it changes the design:
- Current alternatives:

## Minimum probe
- Probe:
- Evidence source:
- Design field affected:
- Next status after result:
```

Unknown 关闭前，不设计 target seam 或完整 Delta。

## Status: Decision required

```markdown
Status: Decision required

## Target
- Target:
- Trigger:
- Scope:

## Confirmed reality
### Observed
### Common design boundary

## Human-owned decision
- Decision:
- Why repo evidence cannot decide it:

## Options
| Option | Boundary / ownership consequence | Cost / risk | Reversibility |
| --- | --- | --- | --- |

## Recommendation
<一个推荐、依据，以及选择其他方案的后果>
```

只写各选项共享的已确认边界，不伪造唯一设计。

## Status: Design ready

```markdown
# Architecture Design Contract

Status: Design ready

## Target
- Target:
- Trigger:
- Scope:
- Out of scope:

## Current reality
### Observed
<代码、调用、配置、测试、历史或 ADR 可直接证明的事实>

### Inferred
<由证据支持的架构解释>

### Residual Unknown
<不会改变当前设计，只影响实现或验证的事项>

## Primary rule violation
- Rule:
- Evidence:
- Why architectural:
- Root cause:
- Counterexample checked:
- Confidence:

## Secondary signals
<最多两个；说明为什么不在本轮处理>

## Target design
### Responsibility map
| Responsibility | Owner | Input | Output | Owned truth / state | Must not own |
| --- | --- | --- | --- | --- | --- |

### Variation ownership
| Variation | Current locations | Target owner | Handling |
| --- | --- | --- | --- |

### Dependency direction
<稳定主流程、稳定 contract、易变 implementation，以及应消失的依赖边>

### Target seam
- Capability:
- Callers still know:
- Callers no longer know:
- Hidden behavior / state / order:
- Why this seam is real now:

## Design delta
### Keep
### Move
### Merge
### Delete
### Do not change

## Protected behavior
- Input / output:
- Errors:
- Config compatibility:
- Order / lifecycle:
- Side effects / external contracts:
- Performance / observability boundary:
- Acceptable differences:

## Improvement verification
| Dimension | Before | Expected after | How to verify |
| --- | --- | --- | --- |
| Change locality | | | |
| Ownership concentration | | | |
| Dependency stability | | | |
| Caller knowledge | | | |
| Replacement | | | |

## Challenge result
- New layer risk:
- Speculative abstraction risk:
- Real difference preserved:
- Complexity relocation:
- Old path still carrying weight:
- ADR / compatibility conflict:

## Next handoff
<单一推荐设计，以及能够证明它的最小实现边界>
```

## Discipline

- 一个主要规则违反，不输出 smell 清单；
- `Design ready` 只给一个推荐设计；
- `Observed / Inferred / Unknown` 不混写；
- 每个 `Design ready` 必须有具体 `Delete`；没有物理删除时，写明消失的调用者知识、重复判断或无效依赖；
- improvement 只能写可观察 delta，不能只写“更优雅”“更 SOLID”；
- 实现顺序属于下游任务书，不写进本合同。
