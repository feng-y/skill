# Intent Contract quality

Use this reference when contract quality is not obvious. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

A contract is sufficient when the next consumer can act correctly without re-deriving what the user means. Across the five semantics, preserve only what can change downstream judgment: the actual outcome rather than suggested means, material facts and uncertainty, authoritative boundaries and user-owned priorities, the work to do now without pre-solving downstream choices, and result-oriented closure backed by trusted evidence or a real blocker.

Prefer material context over broad background. Preserve implementation freedom where multiple paths satisfy the same intent. Surface material user-owned decisions instead of silently choosing them. More fields, context, constraints, or prose do not improve the contract unless they change downstream judgment or remove a material failure mode.

## Stability

Compression, handoff, and later evidence may enrich the contract but must not silently change authority or state:

- settled user intent, corrections, priorities, and user-owned boundaries change only with new user authority;
- territory facts and constraints follow current authoritative evidence and may change with better evidence without rewriting user intent;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable.

Shortening removes redundancy, not authority, uncertainty, priority, proof obligation, or the distinction between target and current state.

The contract is consumer-ready when the next consumer does not need to reinterpret the goal, rediscover a settled decision, infer who owns a material constraint, or guess what is verified versus unresolved. These distinctions must remain recoverable but need not become extra output fields.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).
