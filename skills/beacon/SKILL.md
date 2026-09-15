---
name: beacon
description: "Use when a caller already understands its semantic question but one bounded part of the intent still permits materially different concrete paths, usage, interfaces, interactions, or artifacts. Make that local intent concrete with the cheapest inspectable representation and return correction or Evidence to the original caller."
---

# Beacon

Beacon is a caller-neutral, primarily model-invoked specialist for making one bounded part of an already-understood intent concrete enough to inspect and compose.

Beacon does not require a prototype. It may use a Core Path, Usage / Interface Draft, behavior example, config or schema shape, UI draft, minimal implementation, experiment, or disposable prototype. Choose the cheapest representation that closes the current material local decision.

The caller keeps semantic ownership. Beacon does not own canonical Intent / Issue, Target Architecture, verification judgment, execution planning, or production implementation.

## Invocation

Beacon is model-invoked and not bound to Northstar. A semantic owner calls `$beacon` when its semantic question is already understood but one bounded concrete shape remains materially ambiguous.

Typical callers:

- Northstar: a local part of Intent still has materially different core-path, usage, interface, or artifact interpretations.
- Architecture Evolution: a structural question is clear, but a concrete consumer path or boundary surface is needed to judge the Target.
- Verify: the claim is clear, but the concrete observable path is ambiguous.
- Unknowns First: factual uncertainty is closed and the remaining question is concrete shape.

Beacon returns its result to the original caller. It does not automatically transfer work to Northstar.

## Boundary

Use Beacon only when a concrete difference can still change the caller's semantic judgment.

Route elsewhere when:

- territory facts are unresolved and could change the shape: `$unknowns-first`;
- long-term responsibility, ownership, dependency, or Target Architecture is undecided: `$architecture-evolution`;
- the remaining problem is proof sufficiency: `$verify`;
- only implementation How remains: return to the caller / Executor.

## One bounded decision

Close one material local decision at a time. If no concrete difference would change outcome, core path, ownership surface, binding boundary, interface, usage, or accepted result, stop.

## Representation

Prefer the cheapest inspectable representation:

1. Core Path for execution path, ownership surface, boundary, or dataflow.
2. Usage / Interface Draft for API, CLI, schema, config, workflow, or interaction.
3. Concrete Artifact when static representation is insufficient: behavior example, UI draft, minimal implementation, timing probe, experiment, or disposable prototype.

Artifacts stay cheap, reversible, and disposable unless durability is itself part of the current decision.

## Return

Return only what the caller needs:

- the material local decision;
- the concrete representation or candidate contrast;
- decision-relevant path / boundary / usage / interface differences;
- new Evidence;
- unresolved points that still change the concrete shape.

Do not announce the final semantic decision for the caller. Do not generate a second Intent SOT, Taskbook, issue graph, PR split, implementation checklist, or verification workflow.

The Beacon result remains a bounded, non-authoritative input until the caller adopts it. In a wider model invocation, deliver the scoped result as a distinct return to the caller before caller judgment continues; do not collapse the Beacon return and the caller's final handoff into one undifferentiated answer. The caller still owns selection, composition, and the final semantic judgment. This transient return boundary is not a new persistent artifact or workflow stage.
