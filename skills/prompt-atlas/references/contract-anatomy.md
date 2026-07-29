# Intent Contract anatomy

Use this reference when compiling or validating an Intent Contract, especially when deciding whether the contract is complete enough, stable enough, and ready for downstream consumption. It defines contract quality, not the intake workflow.

A good contract is the smallest artifact that preserves the user's intended change and lets the next consumer proceed without re-deriving requirement meaning. Optimize for downstream goal attainment, not descriptive completeness, field fullness, or brevity by itself.

## 1. Completeness

The five semantics are complete when each carries the minimum information needed for the next consumer to judge correctly:

- **Goal** — the outcome to change, why it matters when that affects judgment, and the separation between desired result and suggested means.
- **Current Context** — only facts, evidence, baselines, and uncertainty that can change the contract or route; keep verified, inferred, and unmeasured states distinguishable.
- **Boundary** — hard invariants, acceptable differences, approval or write limits, protected proof rules, and any user-owned priority needed to resolve competing constraints. Keep advice and recommendations out of the hard-boundary class.
- **Immediate Task** — what should be completed now, at the right abstraction level for the next consumer, without pre-solving implementation choices that belong downstream.
- **Success / Stop** — the achieved result and evidence that close the work, plus only real blockers or proof conditions that prevent safe closure. A success criterion is not evidence that success has already been achieved.

Do not add information merely to make a field look complete. Missing detail is acceptable when it cannot change downstream judgment; missing material semantics are not.

## 2. Stability

Compression, handoff, and later enrichment must preserve semantic ownership and evidence state:

- settled user intent remains settled until the user corrects it; contradictory territory evidence may invalidate assumptions, feasibility, or route, but must not silently rewrite the user's intended outcome;
- a hard boundary does not degrade into advice, and advice does not become a hard boundary without authority from the source that owns that decision or territory;
- a recommendation remains advisory until confirmed;
- a reversible default remains visibly unconfirmed;
- an unknown, inference, or proof gap does not become a current fact or completion claim through rewriting;
- superseded meaning is replaced rather than accumulated beside current intent;
- downstream implementation judgment stays downstream unless the user makes it part of intent or authoritative territory evidence makes it a real constraint.

Shortening removes redundancy, not authority, uncertainty, priority, proof obligation, or the distinction between target state and current state.

## 3. Goal attainment

Use the contract to maximize the probability that downstream work achieves the user's real goal.

- Prefer material context over broad background.
- Preserve flexibility where multiple implementations can satisfy the same intent.
- Do not over-constrain the consumer with user-suggested means, Atlas preferences, or speculative architecture choices.
- Surface material user-owned decisions rather than silently choosing a direction that changes Goal or Boundary.
- Carry enough evidence and proof obligation to prevent a plausible false success, but leave concrete verifier mechanics to the owning downstream capability.
- Treat interaction and output budgets as normal operating envelopes. If fitting a budget would materially reduce correctness, completeness, intent fidelity, or goal attainment, exceed it rather than weaken the contract.

The contract is not improved by adding more context, constraints, or prose unless they change downstream judgment or reduce a material failure mode.

## 4. Downstream acceptance

A consumer-ready contract makes these states recoverable without reopening intake:

- **Settled** — user intent, corrections, hard boundaries, and confirmed priorities that downstream work should not re-litigate without new owning-authority input or contradictory territory evidence that changes feasibility or route.
- **Flexible** — implementation choices and recommendations the downstream consumer may adapt while preserving Goal and Boundary.
- **Unresolved** — remaining user-owned decisions, material unknowns, proof gaps, or blockers whose owner and consequence are explicit.
- **Evidence state** — whether a material claim is verified, inferred, unmeasured, or awaiting a named proof obligation.

The next consumer may enrich implementation knowledge and current evidence, but should not need to ask what the user meant, rediscover a settled decision, infer whether a constraint is hard, or guess whether a completion criterion has already been satisfied.

When correctness or completion is material, apply [completion-trust.md](completion-trust.md) so the contract also carries the necessary proof integrity and independent-acceptance obligations.

## Final quality test

Before handing off, reject or repair the contract if any of these are true:

- the next consumer still has to reinterpret the user's real goal;
- a material decision or constraint has no recoverable owner;
- current fact, inference, recommendation, default, and proof gap can be mistaken for one another;
- the contract forces an implementation choice that is not actually user-owned or territory-constrained;
- the artifact is concise only because material intent or evidence was compressed away;
- Success / Stop describes work performed rather than the result or trusted evidence that matters.
