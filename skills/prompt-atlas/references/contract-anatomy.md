# Stable Intent IR

Use this reference when Stage 1 authority, Goal closure, or stability is not obvious. Stable Intent is source semantics for Execution Compile, not an executor-facing taskbook.

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

- **User-owned intent** — requested outcome, accepted behavior, confirmed decisions, and boundaries. These change only with new user authority.
- **Territory reality** — authoritative code, tests, traces, schemas, artifacts, measurements, and other evidence. Better evidence may revise facts, feasibility, necessary implementation work, and proof obligations without rewriting intent.
- **Inference / recommendation** — useful model judgment, including a candidate Goal or delegated default, but not Human-confirmed authority.
- **Unknown** — unresolved until evidence, execution, a visible delegated default, or Human authority settles its consequence.

An explicit requested outcome remains authoritative even when grounding reveals more work, stronger proof, or higher cost. Surface a true conflict rather than silently weakening it.

## Why / design intent

Preserve rationale when it helps execution choose correctly in cases the prompt cannot predict. A design direction is Human-owned when the Human made it part of the desired result or boundary. Routine architecture choices remain implementation How when they preserve that meaning.

## Grounding

Ground the smallest set of unknowns needed to establish Goal meaning, closure, confirmed boundaries, or trusted success. Prefer authoritative evidence and rich existing references.

For repo work, preserve governing constraints or acceptance paths when they affect meaning or proof, and capture a sourced baseline when success is relative to current behavior. Leave work-surface discovery, dependency mapping, command validation, and implementation design to Execution Compile unless they are required for intent stability.

Grounding should reduce the Human decision surface, not replace it. Do not ask the Human for facts authoritative evidence can settle, and do not keep researching merely to avoid a real Human decision.

When a required fact or disagreement is accessible now, perform the focused check during compile. When a critical precondition, carrier-versus-reality disagreement, or executor understanding can only be settled in the execution environment but still before material modification, let Execution Compile create Task 0. Task 0 may expose a Human boundary that was impossible to see earlier, but it must not postpone one already visible during compile.

When the Human defines a scope or classification rule but is unsure which concrete entities satisfy it, preserve the rule as authority and derive membership from evidence. Ask again only when the residual classification depends on Human meaning rather than observable reality.

## Ask Human boundary

Ask only when at least one of these is true:

1. **Change intent** — proceeding would change the requested outcome, accepted behavior, or a design direction the Human made part of the result.
2. **Change boundary** — proceeding would cross or relax confirmed scope, constraints, approval, protected proof, or require irreversible/high-risk authorization.
3. **Confused intent** — materially different Goal interpretations remain plausible after accessible grounding.

These are consequence tests, not keyword tests. “Scope”, “architecture”, or “core” does not automatically mean Human-owned.

Necessary implementation expansion inside settled intent and boundaries is not a boundary change. Redefining what is in or out of the Goal is. Choosing an architecture that preserves the requested result is How; discarding a requested design direction is an intent change.

## Unknown routing

Unknown exists to reduce unnecessary Human questions, not eliminate Human judgment.

Route it in this order:

- evidence can settle it during compile → investigate;
- it can only be settled in the execution environment before material modification → Task 0 to verify the precondition, expose disagreement, and align executor understanding;
- it changes only local implementation How or execution theory → let execution choose, experiment, or replan;
- a reasonable choice preserves intent and boundaries and is reversible or reliably mismatch-detectable → visible delegated default;
- it reaches one of the Ask Human boundaries → ask the smallest useful question;
- required evidence or authority is inaccessible but independent safe work remains → preserve the blocker and park the affected branch;
- required evidence, access, or capability is inaccessible and no safe route remains → return `Status: Blocked` with the exact resolving condition.

A delegated default is visibly unconfirmed. Record its basis, consequence if wrong, and detection or rollback route. It may close ordinary orchestration; it may not silently change intent or confirmed boundaries.

## Goal closure

A Goal is closed when existing Human authority establishes one coherent requested end state and what the current work is expected to accomplish. It need not settle implementation How or every broader future decision.

A prompt may instead expose a problem space: concern, hypothesis, competing questions, possible end states, or active deliberation. Ground only enough context to expose the materially different interpretations, then return the smallest useful choice with consequences and a recommendation. A model-proposed Goal remains inference until the Human confirms, selects, or corrects it.

Do not over-block execution. If the Human already established a complete minimum outcome, broader concerns, later go/no-go choices, and implementation unknowns remain separate unless they actually trigger an Ask Human boundary.

## Human and delegated decisions

When an Ask Human boundary remains, expose the smallest decision surface: materially distinct options, why they differ, and a concise recommendation. Inference, recommendation, or a delegated default must not hide that decision.

More work, wider necessary implementation scope, several valid implementation approaches, or future replanning do not by themselves require Human input.

A delegated default is allowed when it preserves intent and confirmed boundaries, has a reasonable evidence- or convention-backed choice, and is reversible or safely mismatch-detectable. For **artifact-only**, it remains reviewable until the caller accepts, edits, or forwards the carrier. For **compile-and-run**, it must be safe to execute without another Human turn.

If evidence proves the requested result infeasible and there is no meaningful Human choice, return the blocker rather than manufacturing a decision.

## Intent convergence runtime

Intent Take runs as an interactive compile-time convergence loop. Across turns, recover only:

- the candidate or confirmed Goal;
- Human-confirmed authority and boundaries;
- still-valid evidence and material unknowns;
- the smallest remaining Ask Human decision, unavailable probe, or blocker.

Reconcile each new Human message or authoritative fact with that state. Preserve still-valid facts and decisions; do not restart discovery merely because a new turn began. Rewriting alone cannot turn inference into authority.

The loop exits when Stable Intent is reached or the smallest unresolved decision/probe/blocker has been returned.

## Stability

Stable Intent is sufficient when Execution Compile no longer needs to rediscover:

- the problem and complete requested outcome;
- Human-confirmed boundaries;
- which material facts are verified, inferred, or unknown;
- what trusted success means;
- delivery semantics that must survive lowering.

It also requires that none of the three Ask Human conditions remains. Context and execution unknowns may remain when they can be investigated, handled by Task 0 before material modification, delegated visibly, or resolved downstream without changing intent or boundaries.

Implementation discovery, decomposition, dependency mapping, architecture How, command order, retries, and runtime state remain Stage 2/runtime concerns unless they trigger an Ask Human boundary.

## Boundary with Execution Compile

Execution Compile may ground implementation territory, create Task 0 to settle critical preconditions and handoff disagreement, close ordinary execution branches with evidence or visible delegated defaults, derive work dependencies, and lower proof semantics into execution shape. It may not silently change intent or confirmed boundaries.

If Stage 2 or Task 0 evidence triggers **change intent**, **change boundary**, or **confused intent**, return to Intent Take before affected modification. If a non-intent prerequisite is unavailable, park only the affected branch while safe work remains; otherwise return `Status: Blocked`.

The final executable artifact contains only the lowered semantics that matter to execution judgment; it is not Stable Intent followed by an execution appendix.
