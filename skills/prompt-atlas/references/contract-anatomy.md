# Stable Intent IR

Use this reference when Stage 1 intent quality or stability is not obvious. This is a quality reference for Intent Take, not a second workflow and not the executable carrier.

## Purpose

Intent Take should converge on source semantics that Execution Compile can lower without rediscovering what the user means or silently inventing authority.

Preserve only information that can change downstream judgment:

- the desired end state and the real problem being solved;
- decision-relevant Why / design intent;
- current territory facts, provenance, evidence state, and material unknowns;
- Human-confirmed choices, priorities, approvals, and boundaries;
- the current task scope when it differs from the broader Goal;
- what observable result and proof would count as success;
- requested delivery semantics when material.

Do not carry conversation history, rejected reasoning, or implementation detail merely because it appeared earlier.

## Authority

Keep authority classes distinct:

- **User-owned intent** — Goal, explicit requested outcomes, confirmed decisions, user-owned priorities, scope/approval boundaries, and protected proof requirements change only with new user authority.
- **Territory reality** — authoritative code, tests, traces, schemas, artifacts, measurements, and other evidence may revise facts, feasibility, necessary work inside settled boundaries, and proof obligations without rewriting intent.
- **Inference / recommendation** — useful for judgment but not settled authority.
- **Unknown** — remains unknown until evidence or Human authority resolves it.

Explicit requested outcomes are not disposable implementation suggestions. Grounding may expose prerequisites, wider necessary implementation or verification scope inside settled boundaries, higher cost, or infeasibility; it must not silently weaken, defer, split out, or replace an authoritative outcome.

## Why / design intent

Preserve rationale when it can guide unforeseen execution choices. A useful Why explains the underlying problem, undesirable structural property, or desired direction beyond the literal surface change.

For example, “delete five fixed SessionData dict members” is a target change; “remote dict should not require a growing fixed SessionData staging layer” is a design intent that helps reject a superficially compliant replacement cache.

Do not preserve rationale that only explains how the conversation arrived here.

## Grounding

Ground only unknowns needed to know what the user means, whether an explicit outcome is feasible inside settled authority, or what proof semantics must be preserved. Prefer the smallest authoritative check and references to rich existing artifacts.

For repo work:

- include governing local constraints or acceptance paths when they change meaning or proof obligation;
- capture a sourced baseline when success is relative to current behavior or measurement;
- distinguish verified facts, inference, and unknowns;
- if evidence challenges an explicit outcome, first determine whether prerequisites, wider necessary work, or stronger proof can preserve it inside settled boundaries;
- leave broader work-surface discovery, dependency mapping, implementation design, and execution command validation to Execution Compile unless needed for intent stability.

## Human decisions

Ask only when available evidence cannot settle a material choice that changes user-owned outcome, accepted behavior, scope or priority, approval, or a protected proof rule.

Do not ask because:

- the same outcome requires more implementation work;
- repo discovery widens necessary scope inside already settled boundaries;
- implementation How has several reasonable options;
- the executor will need to decompose or replan work.

When a Human choice is needed, expose the smallest useful surface with materially distinct options and a concise recommendation. A bounded conditional/default may be shown only as visibly unconfirmed when it preserves Goal and confirmed boundaries, is reversible or safely detectable if wrong, and does not impersonate Human authority. Rewriting or repetition cannot turn that default into a confirmed decision.

If authoritative evidence proves the requested outcome infeasible and no meaningful Human choice remains, return the exact blocker rather than manufacturing a decision.

## Stability test

Stable Intent IR is sufficient when Execution Compile no longer needs to rediscover:

- what problem is actually being solved and why;
- what complete outcome must remain true;
- which choices and boundaries are Human-authoritative;
- which facts are verified versus inferred or unknown;
- what success and trusted proof mean;
- what requested delivery semantics must survive lowering.

Implementation discovery, task decomposition, dependency mapping, local architecture How, execution topology, command order, retry policy, and runtime state do not make intent unstable unless resolving them would change the user-owned semantics above.

## Unresolved output

When intent is not stable, return the best current intent snapshot plus only the smallest decision, focused probe, bounded conditional/default, or blocker needed for another alignment turn. Do not pad unresolved intent into an executable contract.

A later turn may converge the intent when it adds new user authority or authoritative territory evidence. Self-review on unchanged information can improve consistency or wording but cannot promote inference, recommendation, default, or uncertainty into settled intent.

## Boundary with Execution Compile

Stable Intent IR is compiler input, not the first half of the final taskbook.

Execution Compile may:

- ground implementation territory needed for a truthful graph;
- close material execution branches from intent, constraints, and evidence;
- derive Task / Issue boundaries and dependencies;
- lower proof semantics into verifier topology and a Global Gate;
- create AFK/recovery/continuity semantics.

It may not reinterpret Goal, silently alter Human authority, or print the full Intent IR and then append an execution section. The final executor-facing artifact should contain only the lowered semantics that matter to execution judgment.