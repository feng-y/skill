# Architecture Design Contract

Choose exactly one status and emit only the section for that status. Do not fill a complete design template when evidence is insufficient or architecture work is unnecessary.

## Status: No architecture change

Use when the evidence supports a local implementation issue rather than a responsibility, variation, dependency, or seam problem.

```markdown
Status: No architecture change

## Target

- Target:
- Trigger:
- Scope:

## Observed evidence

Facts showing ownership and change boundaries are already local enough.

## Why this is not an architecture problem

Explain why the candidate signals do not establish a rule violation. Include the counterexample considered.

## Local change boundary

State the smallest implementation area that should change and what should remain untouched.
```

Do not output a target seam, responsibility redesign, or `Keep / Move / Merge / Delete` section.

## Status: Research required

Use when a repo or runtime fact can materially change the owner, seam, dependency direction, compatibility boundary, or design verdict.

```markdown
Status: Research required

## Target

- Target:
- Trigger:
- Scope:

## Confirmed reality

### Observed

Facts already supported by evidence.

### Inferred

Only conclusions that remain valid across the unresolved alternatives.

## Design-changing Unknown

- Unknown:
- Why it changes the design:
- Current alternatives:

## Minimum evidence probe

- Probe:
- Evidence source:
- Which design field it can change:
- Next status after the result:
```

Do not invent the target seam or full Design Delta before the Unknown closes.

## Status: Decision required

Use when repo evidence cannot decide a Human-owned long-term or high-cost boundary commitment.

```markdown
Status: Decision required

## Target

- Target:
- Trigger:
- Scope:

## Confirmed reality

### Observed

Facts supported by evidence.

### Common design boundary

Only architecture conclusions shared by all viable options.

## Human-owned decision

- Decision:
- Why evidence cannot decide it:

## Options

| Option | Boundary/ownership consequence | Cost/risk | Reversibility |
| --- | --- | --- | --- |

## Recommendation

Give one recommendation, its basis, and the consequence of choosing differently.
```

Do not manufacture a single complete design while the decision is open.

## Status: Design ready

Use only when the primary rule violation, root cause, target owner, seam, and observable improvement are sufficiently grounded.

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

Facts directly supported by code, call paths, config, tests, runtime evidence, history, or current ADRs.

### Inferred

Architecture interpretation supported by the observations.

### Residual Unknown

Only items that do not change the selected design. State their implementation or verification impact.

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

Which switch, wrapper, special entry, fact source, compatibility branch, old test surface, caller knowledge, or invalid dependency should disappear.

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

## Next handoff

State the single recommended design and the smallest implementation boundary that can prove it.
```

## Output discipline

- One primary rule violation, not a smell inventory.
- One recommended design for `Design ready`.
- Evidence and inference remain separate.
- Every `Design ready` must contain a concrete `Delete`. When no physical code is deleted, name the caller knowledge, duplicate decision, or invalid dependency that disappears.
- Improvement verification describes observable deltas, not “cleaner,” “more elegant,” “more SOLID,” or pattern names.
- Implementation sequencing belongs in the downstream taskbook, not here.
