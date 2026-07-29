# Intent artifact quality

Use this reference when intent-artifact quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

An artifact is sufficient when the next consumer can act correctly without re-deriving what the user means. Preserve only what can change downstream judgment: the desired end state, relevant territory reality and uncertainty, Human authority, hard constraints and approvals, the current instruction, trusted completion evidence, required delivery shape, and downstream handoff.

A repo-scoped artifact is incomplete when an authoritative local constraint or acceptance rule can materially change Constraints, required evidence, route, or completion but is left for the next consumer to rediscover. Preserve the governing requirement, not its downstream execution procedure.

Prompt Atlas supports iterative alignment but does not own continuation across turns. Each invocation should produce the best current artifact or the smallest useful decision surface and stop. A later user turn may improve intent fidelity when it supplies new user authority. New territory evidence, changed external constraints, or downstream results may improve grounding or expose mismatch, infeasibility, or missing proof, but do not by themselves change user-owned intent. Repeated self-refinement on the same information may improve consistency, completeness, or expression, but is quality review rather than evidence of intent convergence.

Explicit requested outcomes are part of intent authority, not disposable implementation suggestions. Grounding may add prerequisites, widen necessary implementation or verification scope within existing user-owned boundaries and approval limits, expose higher cost, or prove an outcome infeasible; it must not silently turn “do this now” into “defer this,” “split this out,” or “do a weaker version.” If preserving the outcome requires crossing a user-owned boundary or approval limit, or evidence otherwise cannot resolve the conflict while preserving the outcome, the artifact is not stable until the user resolves the material choice or the result honestly closes on a blocker with no meaningful choice available. A stable artifact must preserve every explicit user-owned outcome with its original authority unless later user authority supersedes it.

Prefer material context over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More context or prose does not improve the artifact unless it changes downstream judgment or removes a material failure mode. The artifact may identify the next owner or capability, but must not absorb that owner's planning, implementation, verification execution, or other downstream work; naming the destination does not start it.

## Agent-facing structure

In explicit Artifact mode, structure is part of contract correctness rather than presentation preference. Use stable canonical field names across languages and localize the values. The carrier uses this exact semantic order:

1. **Goal** — desired end state and real problem to solve;
2. **Context** — relevant motivation, current territory facts, evidence state, and material unknowns;
3. **Decisions** — only material Human-confirmed choices or approvals;
4. **Constraints** — hard boundaries, invariants, acceptable differences, scope/approval limits, and protected judging/oracle rules;
5. **Task** — what this pass must accomplish now without implementation decomposition;
6. **Success Criteria** — observable conditions and required evidence needed to claim completion;
7. **Output** — required downstream deliverable/response shape, or an explicit statement that no additional format constraint applies;
8. **Handoff** — `Route`, `Reason`, and `Use`.

These fields encode different roles and authority and must not be flattened into one prose summary:

- **Goal** answers “what state should be true when this succeeds?”; motivation belongs in **Context**;
- **Context** may challenge feasibility but does not silently become intent, a Human decision, or a constraint;
- **Decisions** contains only Human authority, never model recommendations, guesses, reversible defaults, or repo facts;
- **Constraints** defines what downstream may not violate or cross; implementation inconvenience is not a constraint;
- **Task** is the current instruction and may be narrower than Goal, but cannot silently weaken Goal;
- **Success Criteria** defines both observable completion and the evidence required to support the claim; target state and proof state remain distinguishable;
- **Output** defines delivery shape, not correctness, and must not invent formatting requirements when none were requested;
- **Handoff** tells the Human where the complete contract goes next and how to pass it.

For verification, keep protected judging rules separate from completion evidence. For example, “replay/diff may not be replaced by build-only evidence” belongs in **Constraints**; “the affected replay/diff paths pass with no unexpected difference” belongs in **Success Criteria**.

This structure aligns with current frontier-model prompting practice: explicit goal, relevant context, constraints, required evidence, success criteria, and output format; Prompt Atlas adds **Decisions** to preserve Human authority and **Handoff** to preserve downstream consumption. Do not import downstream-owned workflow sections such as Task 0, concrete patch sequencing, exact command order, retry/rollback loops, progress files, or execution rules.

A stable Artifact-mode result should be usable as one complete input unit. Do not require the Human to extract a paragraph, rename sections, or decide which subset to paste downstream. This fixed structure applies only after intent and required grounding are stable enough for handoff; unresolved Human decisions, blocking probes, or real blockers remain the smaller decision/probe/blocker output rather than being padded into the full contract. Embedded mode may use a caller-owned schema.

## Intent stability

A contract is stable only when no material remaining uncertainty can still change the settled intent envelope. Before Handoff, classify the uncertainty by consequence rather than by size or difficulty:

- if resolving it could materially change **Goal, Decisions, Constraints or approval scope, Task, Success Criteria, or Output**, the contract is not stable; use authoritative grounding when evidence can settle it, otherwise return the smallest Human decision and stop;
- if resolving it changes only territory facts, implementation choices, or solution How while leaving those settled semantics intact, it may pass downstream.

Do not convert every unknown into a question. The gate is about **who owns the consequence**. A downstream executor may discover facts or choose implementation details. Prompt Atlas must retain uncertainties whose resolution would redefine what the Human is asking to accomplish, what authority has been granted, or what counts as done.

Examples:

- “production dedup hit rate is unknown” can remain a downstream fact when the settled Task is only to design how to measure it; “should this pass merely design the measurement or actually instrument and run it?” changes Task, Constraints, Success Criteria, and possibly Output, so it requires Human alignment before Handoff;
- discovering additional consumers of a user-requested removal does not itself require a question when the same outcome can still be achieved inside settled scope and approval; ask only when preserving that outcome would cross Human authority or materially redefine the contract.

The stability gate is not another workflow stage or output section. It is the completion test for Prompt Atlas's existing alignment work.

## Handoff quality

The Handoff removes the Human's final routing and usage guess without becoming a workflow transition. Always expose:

- **Route** — `Direct Execute` or `Wayfinder`;
- **Reason** — why the residual uncertainty fits that route;
- **Use** — exactly how to pass the **entire contract** to the next consumer.

Choose **Direct Execute** when no material architecture or solution commitment must be made before execution; ordinary implementation choices and local structural edits may remain for the executor. `Use` should explicitly say to pass the entire contract as the execution agent's task input. When unattended execution is useful, Leader may consume that same full contract to compile a `/goal` taskbook; Leader is an optional carrier under Direct Execute, not a third route class.

Choose **Wayfinder** when execution first requires a material commitment about architecture, responsibility boundaries, structural decomposition, interfaces, migration strategy, or another solution choice that materially shapes How. `Use` should explicitly say to pass the entire contract to Wayfinder as design input and preserve settled Goal, Decisions, and Constraints while Wayfinder resolves How.

Route by residual uncertainty, not by task size. When intent or required grounding is not stable enough to hand off, return the decision surface, probe, or blocker instead of forcing either route.

A useful Handoff is brief and auditable. It must not restate the whole contract, invent a new requirement, weaken a proof obligation, or import the downstream capability's plan.

## Stability

Compression, handoff, later evidence, and subsequent alignment turns may enrich the artifact but must not silently change authority or state:

- Goal, explicit requested outcomes, user-owned priorities, confirmed Decisions, and user-owned Constraints change only with new user authority;
- still-valid settled semantics from a prior Atlas artifact provide the baseline for a later alignment turn; inferred, unknown, or unverified state remains such until authority or evidence changes it;
- territory facts follow current authoritative evidence and may change with better evidence without rewriting user-owned intent;
- downstream results or feedback may reveal mismatch, infeasibility, or missing evidence, but do not by themselves override a confirmed decision or requested outcome;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting or repeated self-review;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable;
- Output changes only when the user or named consumer changes the required delivery shape, not because Atlas prefers a different presentation.

Shortening, self-review, carrier adaptation, or handoff guidance removes redundancy and improves usability; it does not create new authority. None may change settled intent, erase uncertainty, weaken proof obligations, or blur the distinction between target and current state.

The artifact is consumer-ready when the next consumer does not need to reinterpret Goal, rediscover a settled Decision or governing acceptance requirement, infer who owns a Constraint, guess whether an explicit requested outcome was silently deferred, guess what evidence is required, infer the desired Output, or guess how to consume the artifact. These distinctions should be explicit in the fixed section structure rather than merely recoverable from prose.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).