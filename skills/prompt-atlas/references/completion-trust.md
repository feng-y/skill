# Completion trust

Use this reference when the requested result needs a correctness or completion claim. Intent Take owns the evidence and trust obligations carried in the contract; each downstream consumer owns concrete commands, checks, enforcement, and verifier protocol.

## Selection grammar

Apply these decisions in order:

1. **Proof obligation** — identify evidence that directly demonstrates the intended behavior or result: a target test, replay or trace, contract comparison, known input/output, runtime observation, or reproducible manual check. Treat build, lint, coverage, and other proxies only as supporting signals. If direct proof is missing, carry the evidence type to obtain in Immediate Task and forbid a completion claim in Success / Stop until it exists.
2. **Failure sensitivity** — when a gate is new, changed, proxy-only, silent on failure, or otherwise capable of false-green, require evidence that it can distinguish right from wrong. The consumer chooses reverse validation, a known-failure case, red-to-green proof, or another suitable realization.
3. **Integrity boundary** — when a cheaper false pass is plausible, select and freeze the applicable dimensions in Boundary: **Judge** (rules, thresholds, assertions), **Population** (samples, paths, coverage surface), **Object** (the real subject rather than a narrower or mocked substitute), and **Metric** (definition, range, comparison baseline). A result obtained by violating one does not satisfy Success.
4. **Self-attestation policy** — allow executor-declared completion only when Proof directly reaches the target, the gate has failure sensitivity, plausible shortcuts are frozen, and risk is low with narrow scope. Otherwise require independent acceptance, especially for indirect proof, remaining gameability, migrations or behavior preservation, user-visible critical paths, proof designed by the executor, or completion that depends on overall user intent. When required, the executor may reach `ready for independent acceptance`, not `complete`, until the external judgment passes.

## Placement grammar

- **Current Context** — existing gates, their strength or false-green risk, relevant baselines, and available independent verifier.
- **Boundary** — write scope and the selected Judge, Population, Object, and Metric invariants.
- **Immediate Task** — missing proof type, required failure sensitivity, and artifacts needed for independent acceptance.
- **Success / Stop** — evidence required for completion, the rule that insufficient or compromised proof cannot complete, and whether the terminal is `complete` or `ready for independent acceptance`.

Do not compile retry counts, failure rounds, rollback plans, time or round budgets, continuity protocols, or executor topology. Here, Stop means a true blocker, insufficient trusted evidence, or a boundary against further scope—not how an execution loop limits loss.
