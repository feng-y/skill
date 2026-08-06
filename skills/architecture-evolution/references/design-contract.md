# Architecture Design Contract

Use this output after diagnosis. Keep it short enough to guide implementation, but complete enough that Northstar or an Executor does not need to rediscover the architecture judgment.

Do not turn it into a repo-wide architecture report or an implementation task list.

```markdown
# Architecture Design Contract

Status: No architecture change | Design ready | Research required | Decision required

## Target

- Target:
- Trigger:
- Scope:
- Out of scope:

## Current reality

### Observed

Facts directly supported by code, call paths, config, tests, runtime evidence, history, or current ADRs.

### Inferred

Architecture interpretation supported by the observations.

### Unknown

Only items that can change ownership, seam, compatibility, dependency direction, or verification. For each item, name the next closer: repo research, runtime probe, Human decision, or stop.

## Primary rule violation

- Rule:
- Evidence:
- Why this is architectural rather than a local implementation issue:
- Root-cause responsibility / variation / seam error:
- Counterexample checked:
- Confidence:

## Secondary signals

At most two. State why they are not primary and why they are deferred.

## Target design

### Responsibility map

| Responsibility | Owner | Input | Output | Owned truth/state | Must not own |
| --- | --- | --- | --- | --- | --- |

### Variation ownership

| Variation | Current locations | Target owner | Handling |
| --- | --- | --- | --- |

### Dependency direction

Describe the stable flow, stable contract, and volatile implementation direction. Name any forbidden edge that should disappear.

### Target seam

- Interface/capability:
- Callers still need to know:
- Callers no longer need to know:
- Behavior/state/order hidden behind the seam:
- Why this seam is real now:

## Design delta

### Keep

What remains canonical.

### Move

Which responsibility, state, or decision moves from where to where.

### Merge

Which duplicate interpretations or shallow modules become one capability.

### Delete

Which switch, wrapper, special entry, fact source, compatibility branch, or old test surface should disappear.

### Do not change

Protected scope that prevents redesign drift.

## Protected behavior

List implementation obligations that the design does not permit to drift:

- input/output semantics;
- error behavior;
- configuration compatibility;
- ordering and lifecycle;
- side effects and external contracts;
- necessary performance or observability boundary.

State acceptable differences separately. Do not claim these behaviors are already verified unless evidence was actually run.

## Improvement verification

| Dimension | Before | Expected after | How to verify |
| --- | --- | --- | --- |
| Change locality | | | |
| Ownership concentration | | | |
| Dependency stability | | | |
| Caller knowledge | | | |
| Replacement/deletion | | | |

## Challenge result

- New wrapper/layer risk:
- Speculative abstraction risk:
- Real business difference preservation:
- Complexity relocation check:
- Old path still carrying weight:
- ADR/compatibility conflict:

## Decision or next handoff

For `Design ready`, state the single recommended design and the smallest implementation boundary that can prove it.

For `Research required`, state the exact evidence probe and which design field it can change.

For `Decision required`, state the Human-owned tradeoff, available options, recommendation, and why repo evidence cannot decide.

For `No architecture change`, state why the evidence supports a local change instead.
```

## Output discipline

- One primary rule violation, not a smell inventory.
- One recommended design, unless a real Human-owned tradeoff remains.
- Evidence and inference remain separate.
- `Delete` cannot be empty without an explicit explanation of what knowledge burden or invalid edge is still removed.
- Improvement verification describes observable deltas, not “cleaner,” “more elegant,” “more SOLID,” or pattern names.
- Implementation sequencing belongs in the downstream taskbook, not here.
