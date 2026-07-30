# Completion trust

Use this reference only when the result needs a material correctness or completion claim. Current models already verify routine work; add only task-specific proof, false-pass, independence, and receipt obligations that change trust.

## Trust decisions

Apply in order:

1. **Direct proof** — identify evidence that reaches the requested behavior or result: a target test, replay/trace, contract comparison, known input/output, runtime observation, decision-grade source set, or reproducible manual check. Preserve a governing repo-local acceptance path instead of replacing it with an easier proxy. Build, lint, coverage, summaries, and model review are supporting signals unless they directly prove the Goal.
2. **Command and baseline truth** — record whether critical gates and baselines were actually observed. If accessible during intake, run them. Otherwise mark them `unverified` and make verification an initial Loop action. A missing, empty, or false-green command is new State and an `UNMET` reason, not evidence of completion or an automatic excuse to stop.
3. **Failure sensitivity** — when a gate is new, changed, proxy-only, silent on failure, or plausibly false-green, require evidence that it distinguishes right from wrong. The executor may use a known-failure case, red-to-green check, mutation, reverse validation, or another suitable method. Do not add this branch when the existing authoritative gate is already trustworthy for the claimed property.
4. **Integrity boundary** — freeze any dimension through which an easier false pass could be manufactured:
   - **Judge** — rules, assertions, thresholds, or acceptance code;
   - **Population** — samples, paths, cases, or coverage surface;
   - **Object** — the real subject rather than a narrower, skipped, or mocked substitute;
   - **Metric** — definition, range, comparison, and baseline.

   Name only plausible shortcuts. Typical mappings are relaxed assertions or changed acceptance code → Judge; skipped tests or narrowed cases → Population; mocking/substitution → Object; moved thresholds or baselines → Metric. A result obtained by weakening a frozen dimension is `UNMET`.
   When a baseline is protected, a regressed result remains `UNMET`; restore it, find another valid route, or stop honestly if no route remains inside authority.
5. **Independent challenge** — executor self-attestation is sufficient when direct proof reaches the target, the gate is failure-sensitive where needed, plausible shortcuts are frozen, and residual risk is controlled. Require a fresh-context verifier or governing external acceptance only when a repo/user rule requires it or material residual risk remains—for example executor-designed proof, a critical user path, behavior-preserving migration, or architecture work whose claimed structural gain lacks strong direct evidence. Until required acceptance passes, the state is `ready for independent acceptance`, not complete.
6. **Completion receipt** — map each Goal condition to the actual evidence and result that supports it, state material baseline deltas, and disclose remaining uncertainty or compromised checks. A completion sentence without inspectable evidence does not change proof state.

For maintainability, evolvability, or architecture quality, immediate functional tests are indirect evidence. Require repo-specific structural evidence for the claimed gain and record any material Architecture Intent delta. Do not claim long-horizon quality from executor opinion alone.

## Placement

- **State** — governing gates, verified/unverified command state, baseline and source, false-green risk, proof gaps, and available independent acceptance.
- **Constraints** — write scope and selected Judge/Population/Object/Metric invariants.
- **Loop** — actions needed to establish proof, failure sensitivity, or independent acceptance; local evidence produced by structured tasks.
- **Evaluation** — the global evidence map, the rule that insufficient/compromised proof remains `UNMET`, and whether external acceptance is part of `MET`.
- **Output** — the completion/block receipt with actual results and remaining uncertainty.
- **Control** — risk-triggered independent challenge and any explicit proof budget; not a blanket review stage.

Do not compile fixed retry counts, rollback scripts, verifier topology, or generic final-review instructions. An `UNMET` proof state feeds the next useful action; it becomes a blocker only when no safe action can obtain the required evidence inside settled authority.

## Visible-contract boundary

Prompt Atlas can freeze proof rules and require independent acceptance, but it cannot place a genuinely hidden test inside the same executor-visible contract or create fresh context by declaration. Hidden checks and verifier isolation belong to the runtime, harness, governing CI, or a separate accepting agent. If that capability is required but unavailable, report `ready for independent acceptance` or `Status: Unresolved`; do not claim parity through self-review.
