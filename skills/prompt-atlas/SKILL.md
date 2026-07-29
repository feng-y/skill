---
name: prompt-atlas
description: Stably compile a one-sentence goal or scattered, evolving cross-turn hints into a consumer-ready Intent Contract or requested carrier. Support human-driven iterative intent alignment across separate invocations by preserving settled semantics, incorporating new user authority, and refreshing territory grounding from authoritative evidence. In explicit Artifact mode, render stable intent as a strongly structured agent-facing contract with Goal, Context, Decisions, Constraints, Task, Success Criteria, Output, and Handoff. Hand off only when remaining uncertainty can no longer materially change the settled intent contract. Use when the user asks to clarify, consolidate, prepare, hand off, or rewrite a requirement or prompt, or when a broader workflow explicitly needs intent intake before direct, design, planning, issue, or execution work. Explicit /prompt-atlas use returns the compiled artifact as the terminal result of this invocation.
---

# Prompt Atlas

Perform request-scoped Intent Take. Recover what the user is actually trying to change, ground the context that matters, resolve only decisions that genuinely belong to the user, and leave the next consumer a contract that does not require rediscovering requirement meaning, authority, constraints, or completion criteria.

Compile five minimum semantics internally:

- **Goal** — the desired end state and real problem being solved;
- **Current Context** — only current facts, evidence, motivation, and bounded uncertainty that affect judgment;
- **Boundary** — invariants, acceptable differences, scope, approval limits, protected evaluation or proof rules when material, and any user-owned priority needed to resolve competing constraints;
- **Immediate Task** — what should be completed now without prescribing implementation procedure;
- **Success / Stop** — the observable result and evidence that close the work, or what real blocker prevents closure.

Keep these semantics distinct during reasoning. In Artifact mode, do not collapse a stable result into free-form prose merely for human editability. Compile it into the fixed agent-facing contract below. Structure is part of contract correctness: current frontier-model guidance favors explicit goals, relevant context, constraints, success/evidence requirements, output expectations, and clear separation rather than requiring the next agent to infer those roles from prose. Prompt Atlas adds Decisions and Handoff to preserve Human authority and downstream consumption.

Prompt Atlas owns intent understanding and carrier compilation, including explicit Human authority where it materially affects downstream judgment. It does not own architecture choice, implementation planning, execution, or a durable repo-identity harness. New user authority may revise user-owned intent; territory evidence may revise facts, feasibility, necessary scope, proof state, or route without silently rewriting that intent. Repeated self-refinement on unchanged information is quality review, not new intent. Each invocation terminates after delivering either a stable structured artifact with Handoff or the smallest useful unresolved decision/probe/blocker. Handoff is explicit consumption guidance, not a transition into downstream work.

Choose the output mode from the invocation:

- **Artifact mode** — default for explicit `/prompt-atlas` use and direct requests to clarify, consolidate, prepare, hand off, or rewrite a requirement. When stable, return the fixed agent-facing contract with Handoff and stop. When stable compilation is not possible, return only the smallest necessary decision surface, probe, bounded conditional/default, or blocker and stop.
- **Embedded mode** — only when another capability or workflow explicitly invokes Prompt Atlas as an intake sub-capability. Return the compiled intent in the caller's requested carrier or schema and stop Prompt Atlas. Do not infer Embedded mode merely because the ultimate task could later be designed or executed; let the caller own downstream routing unless it asks for a handoff judgment.

Use detailed guidance only when relevant: [contract-anatomy.md](references/contract-anatomy.md) for contract goal attainment and stability, and [completion-trust.md](references/completion-trust.md) for correctness or completion claims.

## Intent Take

### 1. Recover

Recover from the current request, relevant corrections, prior decisions, and examples. When a prior Atlas artifact exists, use still-valid settled semantics as the baseline rather than restarting from raw history. The current user owns intent; current authoritative evidence owns territory. Latest explicit corrections supersede older meaning. Only new user authority may change Goal, user-owned priorities, confirmed decisions, user-owned boundaries, or an explicit requested end state. Better territory evidence may update Context, feasibility, proof obligations, route, or necessary implementation and verification scope without silently rewriting those user-owned semantics. Treat explicit requested outcomes as authoritative until the user supersedes them; do not silently downgrade, defer, split out, or replace one because grounding reveals risk or extra work. Recover desired outcomes separately from suggested means and hard constraints.

### 2. Ground

Investigate only unknowns whose answers could materially change Goal, Constraints, Task, Success Criteria, or safe route. Prefer the smallest authoritative check and rich existing references. When territory evidence challenges an explicit user-owned outcome, investigate enough to characterize the conflict and determine whether the outcome can still be satisfied by adding prerequisites, widening necessary scope within current user-owned boundaries and approval limits, or strengthening proof. If satisfying it would cross such a boundary or approval limit, preserve that conflict for Human resolution rather than silently expanding authority. For repo-scoped work, include governing repo-local constraints or acceptance rules when they can materially change Constraints, Success Criteria, required evidence, or route; preserve the governing requirement, not downstream execution procedure. Capture a sourced baseline whenever the requested change is judged relative to current behavior or measurement, and keep evidence state and mismatch consequence explicit. Preserve material uncertainty instead of inventing certainty or asking the user for facts the environment can settle. Broader implementation investigation remains downstream unless needed to know what the user means or whether a user-owned outcome is actually feasible.

### 3. Resolve human decisions

Resolve only material decisions that available evidence cannot settle and that genuinely belong to the user. If grounding cannot resolve a conflict while preserving an explicit user-owned outcome, surface the conflict with the material evidence, materially distinct options, and one concise recommendation before weakening, deferring, splitting, replacing, or otherwise changing that outcome. If authoritative evidence already proves the outcome infeasible within the settled Constraints and no meaningful user choice remains, return the blocker rather than posing a false question. Do not ask merely because satisfying the same outcome requires more implementation work, broader necessary scope, or stronger verification when those consequences remain inside settled user-owned boundaries and approval limits; absorb them when evidence makes them clear. If a required consequence crosses user-owned scope or approval authority, ask.

As the normal interaction budget, aim for one compact round with no more than five questions. For each question, prefer 2–4 materially distinct options and one concise recommendation with its basis. If that budget would materially reduce goal attainment or stability, exceed it rather than omit a necessary user decision. Do not silently choose a direction or present a recommendation/default as confirmed user intent. A reversible default is allowed only when it leaves Goal and user-owned Constraints unchanged, the cost of being wrong is bounded and reversible, and mismatch is detectable; never use a default to change an explicit requested end state. Mark it visibly as unconfirmed. When a Human decision is required, expose the smallest useful decision surface and stop; do not manufacture another internal round by answering it on the user's behalf.

### 4. Compile and validate

Compile the best current intent when the five internal semantics appear ready for the next consumer. Before treating the artifact as stable, verify that every explicit user-owned requested outcome is still represented with the same authority or has been explicitly superseded by the user. Omission, silent weakening, deferral, or extraction into a later task is semantic drift.

Then classify every material remaining uncertainty before Handoff. If resolving an uncertainty could materially change **Goal, Decisions, Constraints or approval scope, Task, Success Criteria, or Output**, intent is not yet stable: settle it through authoritative grounding when evidence can answer it; otherwise expose the smallest Human decision and stop. Do not ask merely because a downstream fact or implementation choice is unknown. Uncertainty may pass downstream when resolving it changes only territory facts, implementation choices, or solution How while leaving those settled contract semantics intact.

Prefer rich existing references—code, tests, traces, artifacts, schemas, rubrics—over replaying their contents.

For stable Artifact mode, emit these canonical headings in this exact order regardless of response language; localize the section contents, not the field names:

1. **Goal** — desired end state. State what should be true when the work succeeds, not merely why the work is useful and not an implementation checklist.
2. **Context** — only relevant motivation, current territory facts, evidence state, and material unknowns. Keep fact, inference, and unknown distinguishable. Do not hide constraints or Human decisions here.
3. **Decisions** — only material choices explicitly confirmed by the user, including approvals that downstream must not reopen. Do not put model recommendations, reversible defaults, guesses, or territory facts here. If there are no additional confirmed decisions beyond the explicit request, state that briefly rather than inventing one.
4. **Constraints** — hard boundaries, invariants, acceptable differences, scope/approval limits, user-owned priorities when needed, and protected oracle/evaluation rules that downstream must not weaken or bypass. Do not turn implementation convenience into a constraint.
5. **Task** — what this pass must accomplish now. Keep it outcome-oriented and implementation-neutral; do not expand into patch decomposition, task sequencing, exact commands, or executor procedure.
6. **Success Criteria** — observable conditions and required evidence needed to claim completion. Preserve authoritative acceptance paths such as replay/diff when they govern the claimed property. Distinguish the target result from evidence proving it; do not reduce behavioral proof to convenient proxies such as build/lint alone.
7. **Output** — required downstream deliverable or response format when the user or named consumer specifies one. If no extra output shape is required, state that the downstream consumer's normal deliverable applies; do not invent formatting requirements.
8. **Handoff** — make downstream consumption unambiguous with `Route`, `Reason`, and `Use`.

Field boundaries are strict: **Goal** is the end state; **Task** is the current instruction; **Context** is territory reality and motivation; **Decisions** records Human authority; **Constraints** defines what cannot drift or be crossed; **Success Criteria** defines what result/evidence closes the work; **Output** defines delivery shape, not correctness.

For Handoff routing:

- **Direct Execute** — choose when remaining uncertainty is implementation-level and execution does not first require a material architecture or solution commitment about responsibility boundaries, structural decomposition, interfaces, migration strategy, or another design choice that materially shapes How. `Use` must explicitly tell the Human to pass the entire contract as the execution agent's task input. When unattended/long-running execution is directly useful, it may additionally say to pass the same complete contract to Leader to compile a `/goal` taskbook. Leader is an execution carrier, not a third top-level route.
- **Wayfinder** — choose when Goal and Constraints are stable but a material architecture or solution commitment still must be made before execution. `Use` must explicitly tell the Human to pass the entire contract to Wayfinder as design input; Wayfinder resolves How without reopening settled Goal, Decisions, or Constraints.

Route by residual solution uncertainty, not task size. Handoff must not restate the whole artifact, invent a requirement, weaken a proof obligation, or import the downstream capability's plan. It never starts the next capability.

The fixed Artifact-mode structure is an intent contract, not an execution taskbook. Do not import Leader-owned Task 0, patch-by-patch sequencing, exact acceptance command order, retry/rollback loops, PROGRESS/BLOCKED mechanics, or execution rules. If a concrete command or procedure is itself user-owned intent, preserve it in the appropriate field; otherwise leave execution procedure downstream.

For repo-changing work, make write scope explicit in **Constraints** when implicit scope is unsafe. Prompt Atlas is done when the next consumer can continue without re-deriving Goal, Context, Human Decisions, Constraints, Task, completion evidence, expected Output, or how to consume the artifact. Downstream work may enrich implementation knowledge and current evidence, but settled user intent changes only with new user authority. A proof gap cannot become completion through handoff.

When material uncertainty still prevents stable compilation, expose only the next useful alignment outcome: a focused `probe`, a Human `ask`, a bounded conditional/default, or the exact blocker, then stop. Do not emit the fixed downstream contract or Handoff while user-owned intent or required grounding is unresolved. Further intent convergence requires a later invocation with new user authority; new authoritative territory evidence may improve grounding without changing user-owned intent. Without either new signal, additional self-review may improve consistency or expression but must not promote inference, recommendation, default, or uncertainty into settled intent.

If the user requests a fresh-session handoff, save the same structured artifact as Markdown in the operating system temporary directory, reference existing artifacts rather than copying them, redact sensitive context, add `Suggested skills`, and return the absolute path.

## Output

In Artifact mode, stable output uses the eight-section contract above in that order. Section structure is mandatory even when content is brief. In **Handoff**, always emit `Route`, `Reason`, and `Use`; `Use` identifies the full artifact as the unit passed downstream. Keep the body dense and avoid explanatory prose outside the contract. Treat brevity as a budget, not a completion gate: never compress away a required authority distinction, material uncertainty, constraint, evidence obligation, or output requirement. In Embedded mode, honor the caller's carrier/schema while preserving the same intent semantics and authority boundaries. In both modes, delivery ends the Prompt Atlas invocation.