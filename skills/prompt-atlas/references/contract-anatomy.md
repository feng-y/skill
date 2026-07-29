# Intent artifact quality

Use this reference when intent-artifact quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

An artifact is sufficient when the next consumer can act correctly without re-deriving what the user means. Across the five semantics, preserve only what can change downstream judgment: the actual outcome rather than suggested means, material facts and uncertainty, authoritative boundaries and user-owned priorities, the work to do now without pre-solving downstream choices, and result-oriented closure backed by trusted evidence or a real blocker.

A repo-scoped artifact is incomplete when an authoritative local constraint or acceptance rule can materially change Boundary, proof obligation, route, or completion but is left for the next consumer to rediscover. Preserve the governing requirement, not its downstream execution procedure.

Prompt Atlas supports iterative intent convergence but does not own continuation across turns. Each invocation should produce the best current artifact or the smallest useful decision surface and stop. A later invocation may improve intent fidelity when it carries new user authority, authoritative territory evidence, changed external constraints, or downstream evidence that reveals a mismatch. Repeated self-refinement on the same information may improve consistency, completeness, or expression, but is quality review rather than evidence of intent convergence.

Prefer material context over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More fields, context, constraints, prose, or internal review rounds do not improve the artifact unless they change downstream judgment or remove a material failure mode. The artifact may identify the next owner or capability, but must not absorb that owner's planning, implementation, verification execution, or other downstream work; naming the destination does not start it.

When a target consumer or carrier is known, adapt representation to how that consumer can use the intent directly. This may change ordering, density, framing, or references, but not settled meaning, authority, uncertainty, boundaries, proof obligations, or responsibility ownership. A Leader input, Wayfinder brief, plan prompt, final model prompt, and generic Intent Contract may therefore look different while carrying the same material intent.

## Stability

Compression, handoff, later evidence, and subsequent alignment turns may enrich the artifact but must not silently change authority or state:

- Goal, user-owned priorities, confirmed decisions, and user-owned boundaries change only with new user authority;
- still-valid settled semantics from a prior Atlas artifact provide the baseline for a later alignment turn; inferred, unknown, or unverified state remains such until authority or evidence changes it;
- territory facts and constraints follow current authoritative evidence and may change with better evidence without rewriting user-owned intent;
- downstream results or feedback may reveal mismatch, infeasibility, or missing evidence, but do not by themselves override a confirmed user decision;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting or repeated self-review;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable.

Shortening, self-review, or carrier adaptation removes redundancy and improves expression; it does not create new authority. None may change settled intent, erase uncertainty, weaken proof obligations, or blur the distinction between target and current state.

The artifact is consumer-ready when the next consumer does not need to reinterpret the goal, rediscover a settled decision or governing acceptance requirement, infer who owns a material constraint, or guess what is verified versus unresolved. These distinctions must remain recoverable but need not become extra output fields.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).