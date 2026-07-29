# Intent artifact quality

Use this reference when intent-artifact quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

An artifact is sufficient when the next consumer can act correctly without re-deriving what the user means. Across the five internal semantics, preserve only what can change downstream judgment: the actual outcome rather than suggested means, material facts and uncertainty, authoritative boundaries and user-owned priorities, the work to do now without pre-solving downstream choices, and result-oriented closure backed by trusted evidence or a real blocker.

A repo-scoped artifact is incomplete when an authoritative local constraint or acceptance rule can materially change Boundary, proof obligation, route, or completion but is left for the next consumer to rediscover. Preserve the governing requirement, not its downstream execution procedure.

Prompt Atlas supports iterative alignment but does not own continuation across turns. Each invocation should produce the best current artifact or the smallest useful decision surface and stop. A later user turn may improve intent fidelity when it supplies new user authority. New territory evidence, changed external constraints, or downstream results may improve grounding or expose mismatch, infeasibility, or missing proof, but do not by themselves change user-owned intent. Repeated self-refinement on the same information may improve consistency, completeness, or expression, but is quality review rather than evidence of intent convergence.

Explicit requested outcomes are part of intent authority, not disposable implementation suggestions. Grounding may add prerequisites, widen necessary implementation or verification scope within existing user-owned boundaries and approval limits, expose higher cost, or prove an outcome infeasible; it must not silently turn “do this now” into “defer this,” “split this out,” or “do a weaker version.” If preserving the outcome requires crossing a user-owned boundary or approval limit, or evidence otherwise cannot resolve the conflict while preserving the outcome, the artifact is not stable until the user resolves the material choice or the result honestly closes on a blocker with no meaningful choice available. A stable artifact must preserve every explicit user-owned outcome with its original authority unless later user authority supersedes it.

Prefer material context over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More context or prose does not improve the artifact unless it changes downstream judgment or removes a material failure mode. The artifact may identify the next owner or capability, but must not absorb that owner's planning, implementation, verification execution, or other downstream work; naming the destination does not start it.

## Agent-facing structure

In explicit Artifact mode, structure is part of contract correctness rather than presentation preference. The stable carrier uses this semantic order, localized to the response language:

1. **Why this work exists / 这活为什么干** — problem, motivation, desired end state;
2. **Confirmed decisions / 已确认的决策** — only material user-confirmed choices;
3. **Boundaries / 界限** — invariants, scope/approval limits, and protected oracle/evaluation rules that downstream must not weaken or bypass;
4. **Current reality & material unknowns / 当前事实与关键未知** — grounded facts, evidence state, residual uncertainty;
5. **This task / 本次要完成** — requested outcomes for this pass without patch decomposition;
6. **Done when / 完成条件** — observable completion result and required evidence;
7. **Handoff** — `Route`, `Reason`, and `Use`.

These sections encode different authority and must not be flattened into one prose summary. In particular:

- user decisions must not be mixed with model recommendations;
- territory facts must not become boundaries merely because they make implementation inconvenient;
- **Boundaries** protects invariants and judging rules, while **Done when** states the actual result/evidence required to close the work;
- proof obligations must not be weakened into generic build/lint activity.

For example, “replay/diff may not be replaced by build-only evidence” is a protected judging rule and may belong in **Boundaries**; “the affected replay/diff paths pass with no unexpected difference” is a completion condition and belongs in **Done when**.

This structure is intentionally an intent-side projection of a strong execution contract. Do not import downstream-owned sections such as Task 0, concrete patch sequencing, exact verification command order, retry/rollback loops, progress files, or execution rules. Material invariants belong in **Boundaries**; governing proof results belong in **Done when**; concrete execution procedure belongs to the next capability.

A stable Artifact-mode result should be usable as one complete input unit. Do not require the Human to extract a paragraph, rename sections, or decide which subset to paste downstream.

## Handoff quality

The Handoff removes the Human's final routing and usage guess without becoming a workflow transition. Always expose three subfields:

- **Route** — `Direct Execute` or `Wayfinder`;
- **Reason** — why the residual uncertainty fits that route;
- **Use** — exactly how to pass the **entire contract** to the next consumer.

Choose **Direct Execute** when no material architecture or solution commitment must be made before execution; ordinary implementation choices and local structural edits may remain for the executor. `Use` should explicitly say to pass the entire contract as the execution agent's task input. When unattended execution is useful, Leader may consume that same full contract to compile a `/goal` taskbook; Leader is an optional carrier under Direct Execute, not a third route class.

Choose **Wayfinder** when execution first requires a material commitment about architecture, responsibility boundaries, structural decomposition, interfaces, migration strategy, or another solution choice that materially shapes How. `Use` should explicitly say to pass the entire contract to Wayfinder as design input and preserve settled What while Wayfinder resolves How.

Route by residual uncertainty, not by task size. When intent or required grounding is not stable enough to hand off, return the decision surface, probe, or blocker instead of forcing either route.

A useful Handoff is brief and auditable. It must not restate the whole contract, invent a new requirement, weaken a proof obligation, or import the downstream capability's plan.

## Stability

Compression, handoff, later evidence, and subsequent alignment turns may enrich the artifact but must not silently change authority or state:

- Goal, explicit requested outcomes, user-owned priorities, confirmed decisions, and user-owned boundaries change only with new user authority;
- still-valid settled semantics from a prior Atlas artifact provide the baseline for a later alignment turn; inferred, unknown, or unverified state remains such until authority or evidence changes it;
- territory facts and constraints follow current authoritative evidence and may change with better evidence without rewriting user-owned intent;
- downstream results or feedback may reveal mismatch, infeasibility, or missing evidence, but do not by themselves override a confirmed user decision or requested outcome;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting or repeated self-review;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable.

Shortening, self-review, carrier adaptation, or handoff guidance removes redundancy and improves usability; it does not create new authority. None may change settled intent, erase uncertainty, weaken proof obligations, or blur the distinction between target and current state.

The artifact is consumer-ready when the next consumer does not need to reinterpret the goal, rediscover a settled decision or governing acceptance requirement, infer who owns a material constraint, guess whether an explicit requested outcome was silently deferred, guess what is verified versus unresolved, or guess how to consume the artifact. These distinctions should be explicit in the fixed section structure rather than merely recoverable from prose.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).