# Intent Contract quality

Use this reference when compiling or validating an Intent Contract. Add detail only when it improves downstream goal attainment or preserves stability; this is a quality reference, not a second intake workflow.

## Goal attainment

A contract is sufficient when the next consumer can act correctly without re-deriving what the user means. The five semantics should carry only what can change downstream judgment:

- **Goal** — the intended outcome, why it matters when that affects judgment, and the separation between result and suggested means.
- **Current Context** — material facts, evidence, baselines, and uncertainty; keep verified, inferred, and unmeasured states distinguishable.
- **Boundary** — hard invariants, acceptable differences, approval or write limits, protected proof rules, and user-owned priorities when material. Advice stays advisory.
- **Immediate Task** — what should be completed now at the right abstraction level, without pre-solving implementation choices that belong downstream.
- **Success / Stop** — the achieved result and trusted evidence that would close the work, or a real blocker that prevents safe closure. A success criterion is not evidence that success has already been achieved.

Prefer material context over broad background, preserve implementation freedom where multiple paths satisfy the same intent, and surface user-owned decisions instead of silently choosing them. Carry enough proof obligation to prevent plausible false success, while leaving concrete verifier mechanics to the owning downstream capability. Interaction and output budgets are normal operating envelopes; exceed them when fitting the budget would materially reduce correctness, intent fidelity, or goal attainment.

More fields, context, constraints, or prose do not improve the contract unless they change downstream judgment or remove a material failure mode.

## Stability

Compression, handoff, and later evidence may enrich the contract but must not silently change ownership or state:

- user-settled intent, corrections, priorities, and user-owned boundaries change only with new user authority;
- territory facts and constraints belong to current authoritative evidence and may change with better evidence without rewriting user intent;
- recommendations remain advisory and reversible defaults remain visibly unconfirmed;
- unknowns, inferences, and proof gaps do not become current facts or completion claims through rewriting;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint;
- target conditions, current proof state, and accepted completion remain distinguishable.

Shortening removes redundancy, not authority, uncertainty, priority, proof obligation, or the distinction between target and current state.

The contract is consumer-ready when the next consumer does not need to reinterpret the goal, rediscover a settled decision, infer who owns a material constraint, or guess what is verified versus unresolved. These distinctions must remain recoverable but need not become extra output fields.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md).

## Final check

Repair the contract if the next consumer still has to reinterpret the user's goal, a material decision or constraint has no recoverable owner, a fact, recommendation, default, or proof gap can be mistaken for another, implementation is constrained without authority, material intent was compressed away, or Success / Stop describes work performed rather than the result and evidence that matter.
