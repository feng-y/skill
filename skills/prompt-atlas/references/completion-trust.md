# Completion trust

Use this reference when the requested result needs a correctness or completion claim. Intent Take owns the evidence and trust obligations carried in the contract, including any authoritative acceptance path that governs the claimed property; each downstream consumer owns concrete invocation, enforcement, and verifier protocol.

## Selection grammar

Apply these decisions in order:

1. **Proof obligation** — identify evidence that directly demonstrates the intended behavior or result: a target test, replay or trace, contract comparison, known input/output, runtime observation, or reproducible manual check. When an authoritative repo-local acceptance path already governs the claimed property, preserve it as the proof obligation rather than replacing it with a more convenient weaker check. Treat build, lint, coverage, and other proxies only as supporting signals. If direct proof is missing, carry the missing verifier as a required precondition when a named downstream check can settle the claim without changing direction or boundary and safe work remains clear; otherwise carry it as a proof gap. Never promote a missing verifier to a verified current fact.
   For maintainability, evolvability, architecture quality, or long-horizon codebase health, immediate functional tests and executor/model review are only indirect evidence. Require repo-specific evidence for the claimed structural gain and any material Architecture Intent update. Require Human review or another independent acceptance path only when the user or governing repo rule requires it, or when material residual risk remains after the strongest available direct, failure-sensitive verification.
2. **Failure sensitivity** — when a gate is new, changed, proxy-only, silent on failure, or otherwise capable of false-green, require evidence that it can distinguish right from wrong. The consumer chooses reverse validation, a known-failure case, red-to-green proof, or another suitable realization.
3. **Integrity boundary** — when a cheaper false pass is plausible, select and freeze the applicable dimensions in Constraints: **Judge** (rules, thresholds, assertions), **Population** (samples, paths, coverage surface), **Object** (the real subject rather than a narrower or mocked substitute), and **Metric** (definition, range, comparison baseline). A result obtained by violating one cannot receive `MET`.
4. **Self-attestation policy** — allow executor-declared completion when Proof directly reaches the target, the gate has failure sensitivity, plausible shortcuts are frozen, and remaining risk is controlled. Treat migrations, behavior preservation, user-visible critical paths, executor-designed proof, and architecture work as reasons to strengthen or independently challenge the evidence, not as automatic disqualifiers. Require external acceptance only when the user or governing repo rule requires it, or when material residual risk remains after those checks. When required, the executor may reach `ready for independent acceptance`, not `complete`, until the external judgment passes.

## Placement grammar

- **State** — existing gates or governing acceptance paths, their strength or false-green risk, relevant baselines with source and evidence state, available independent verifier, and whether relevant facts are verified, inferred, or still unmeasured.
- **Constraints** — write scope and the selected Judge, Population, Object, and Metric invariants.
- **Loop** — missing proof actions, required verification prerequisites, and artifacts needed for trusted evaluation or independent acceptance.
- **Evaluation** — evidence required for `MET`, the rule that insufficient or compromised proof remains `UNMET`, and whether external acceptance is part of the Goal condition.

Do not compile retry counts, failure rounds, rollback plans, time or round budgets, or executor topology. An `UNMET` proof state feeds the next loop action; it becomes a blocker only when no safe action can obtain the required evidence inside settled authority.
