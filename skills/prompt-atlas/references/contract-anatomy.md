# Stable Intent IR

Use this reference when Stage 1 authority or stability is not obvious. Stable Intent is source semantics for Execution Compile, not an executor-facing taskbook.

## What to preserve

Keep only information that can change downstream judgment:

- the desired end state and underlying problem;
- decision-relevant **Why / design intent**;
- current territory facts, provenance, evidence state, and material unknowns;
- Human-confirmed choices, priorities, approvals, and boundaries;
- current task scope when it differs from the broader Goal;
- observable success and trusted proof semantics;
- requested delivery semantics when material.

Conversation history, rejected reasoning, and implementation detail are context only when they still affect one of those semantics.

## Authority

Keep these classes distinct:

- **User-owned intent** — requested outcomes, confirmed decisions, user-owned priorities, scope/approval boundaries, and protected proof requirements. These change only with new user authority.
- **Territory reality** — authoritative code, tests, traces, schemas, artifacts, measurements, and other evidence. Better evidence may revise facts, feasibility, necessary work inside settled boundaries, and proof obligations without rewriting intent.
- **Inference / recommendation** — useful judgment, not settled authority.
- **Unknown** — unresolved until evidence or Human authority settles it.

An explicit requested outcome remains authoritative even when grounding reveals more work, stronger proof, or higher cost. If it cannot be preserved inside settled boundaries, surface the conflict rather than silently weakening the outcome.

## Why / design intent

Preserve rationale when it helps a later executor choose among unforeseen but valid paths. A useful Why names the underlying problem, undesirable property, or desired direction beyond the literal surface edit. Drop rationale that only narrates how the conversation arrived here.

## Grounding

Ground the smallest set of unknowns needed to establish meaning, feasibility inside settled authority, or success/proof semantics. Prefer authoritative evidence and rich existing references.

For repo work, preserve governing constraints or acceptance paths when they affect meaning or proof, and capture a sourced baseline when success is relative to current behavior. Leave work-surface discovery, dependency mapping, command validation, and implementation design to Execution Compile unless they are required for intent stability.

## Human decisions

Ask only when evidence cannot settle a material choice that changes user-owned outcome, accepted behavior, scope/priority, approval, or a protected proof rule. More work, wider necessary implementation scope inside settled boundaries, several valid implementation approaches, or future replanning do not by themselves require Human input.

When a Human choice is needed, expose the smallest useful decision surface with materially distinct options and a concise recommendation. A default may remain visibly unconfirmed only when it preserves Goal and confirmed boundaries and is reversible or safely mismatch-detectable; it never becomes Human authority through repetition.

If evidence proves the requested outcome infeasible and there is no meaningful Human choice, return the blocker rather than manufacturing a decision.

## Stability

Stable Intent is sufficient when Execution Compile no longer needs to rediscover:

- the problem and complete requested outcome;
- Human-authoritative choices and boundaries;
- which material facts are verified, inferred, or unknown;
- what trusted success means;
- delivery semantics that must survive lowering.

Implementation discovery, decomposition, dependency mapping, local architecture How, execution topology, command order, retries, and runtime state remain Stage 2/runtime concerns unless resolving them would change those source semantics.

When intent is not stable, return the best current intent plus only the smallest decision, probe, conditional/default, or blocker needed for another alignment turn. New user authority or authoritative evidence can move it forward; rewriting alone cannot turn uncertainty into fact or authority.

## Boundary with Execution Compile

Execution Compile may ground implementation territory, close material execution branches, derive Task / Issue boundaries and dependencies, and lower proof semantics into execution topology. It may not reinterpret Goal or Human authority.

The final executable artifact contains only the lowered semantics that matter to execution judgment; it is not Stable Intent followed by an execution appendix.