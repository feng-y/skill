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
- 只给一个推荐设计；
- `Observed / Inferred / Unknown` 不混写；
- 必须有具体 `Delete`；没有物理删除时，写明消失的调用者知识、重复判断或无效依赖；
- improvement 只能写可观察 delta，不能只写“更优雅”“更 SOLID”；
- 实现顺序属于下游任务书，不写进本合同。
