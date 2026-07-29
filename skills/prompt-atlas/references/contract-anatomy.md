# Intent artifact quality

Use this reference when intent-artifact quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

An artifact is sufficient when the next consumer can act correctly without re-deriving what the user means. Across the five semantics, preserve only what can change downstream judgment: the actual outcome rather than suggested means, material facts and uncertainty, authoritative boundaries and user-owned priorities, the work to do now without pre-solving downstream choices, and result-oriented closure backed by trusted evidence or a real blocker.

A repo-scoped artifact is incomplete when an authoritative local constraint or acceptance rule can materially change Boundary, proof obligation, route, or completion but is left for the next consumer to rediscover. Preserve the governing requirement, not its downstream execution procedure.

Prompt Atlas supports iterative alignment but does not own continuation across turns. Each invocation should produce the best current artifact or the smallest useful decision surface and stop. A later user turn may improve intent fidelity when it supplies new user authority. New territory evidence, changed external constraints, or downstream results may improve grounding or expose mismatch, infeasibility, or missing proof, but do not by themselves change user-owned intent. Repeated self-refinement on the same information may improve consistency, completeness, or expression, but is quality review rather than evidence of intent convergence.

Explicit requested outcomes are part of intent authority, not disposable implementation suggestions. Grounding may add prerequisites, widen necessary implementation or verification scope within existing user-owned boundaries and approval limits, expose higher cost, or prove an outcome infeasible; it must not silently turn “do this now” into “defer this,” “split this out,” or “do a weaker version.” If preserving the outcome requires crossing a user-owned boundary or approval limit, or evidence otherwise cannot resolve the conflict while preserving the outcome, the artifact is not stable until the user resolves the material choice or the result honestly closes on a blocker with no meaningful choice available. A stable artifact must preserve every explicit user-owned outcome with its original authority unless later user authority supersedes it.

Prefer material context over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More fields, context, constraints, prose, or internal review rounds do not improve the artifact unless they change downstream judgment or remove a material failure mode. The artifact may identify the next owner or capability, but must not absorb that owner's planning, implementation, verification execution, or other downstream work; naming the destination does not start it.

When a target consumer or carrier is known, adapt representation to how that consumer can use the intent directly. This may change ordering, density, framing, or references, but not settled meaning, authority, uncertainty, boundaries, proof obligations, or responsibility ownership. A Leader input, Wayfinder brief, plan prompt, final model prompt, and generic Intent Contract may therefore look different while carrying the same material intent.

For a stable Artifact-mode result, the handoff hint should remove the Human's final routing guess without becoming a workflow transition. Choose **Direct Execute** when no material architecture or solution commitment must be made before execution; ordinary implementation choices and local structural edits may remain for the executor. Choose **Wayfinder** when execution first requires a material commitment about architecture, responsibility boundaries, structural decomposition, interfaces, migration strategy, or another solution choice that materially shapes How. Route by residual uncertainty, not by task size. Leader is an optional carrier for Direct Execute, not a third route class. When intent or required grounding is not stable enough to hand off, return the decision surface, probe, or blocker instead of forcing either route.

A useful handoff hint is brief and auditable: name the route, state the reason in terms of the remaining uncertainty, and tell the Human how to consume the artifact. It must not restate the whole contract, invent a new requirement, weaken a proof obligation, or import the downstream capability's plan.

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

The artifact is consumer-ready when the next consumer does not need to reinterpret the goal, rediscover a settled decision or governing acceptance requirement, infer who owns a material constraint, guess whether an explicit requested outcome was silently deferred, or guess what is verified versus unresolved. In Artifact mode, a stable result is handoff-ready when the Human also does not need to infer whether the remaining work is execution-ready or still requires material design. These distinctions must remain recoverable but need not become extra output fields.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).