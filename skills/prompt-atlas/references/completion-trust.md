# Completion trust

Use this reference when the requested result needs a material correctness or completion claim. Intent Take preserves what must be proven; Execution Compile lowers that proof obligation into verifier nodes, local checks, and the Global Gate. The executor runs visible checks but must not weaken their protected semantics or self-certify evidence that requires an independent boundary.

## Stage 1 — preserve proof semantics

Intent Take should identify and preserve the proof obligation that follows from the user's Goal and governing repo reality:

1. **Direct proof** — prefer evidence that demonstrates the intended behavior or result: a target test, replay or trace, contract comparison, known input/output, runtime observation, or reproducible manual check. When an authoritative repo-local acceptance path already governs the claimed property, preserve it rather than replacing it with a weaker convenient proxy. Build, lint, coverage, and similar signals are supporting evidence unless they directly prove the target property.
2. **Failure sensitivity** — when a gate is new, changed, proxy-only, silent on failure, or otherwise capable of false-green, preserve the requirement that it demonstrate the ability to distinguish right from wrong.
3. **Integrity boundary** — when a cheaper false pass is plausible, preserve the applicable **Judge**, **Population**, **Object**, and **Metric** dimensions so downstream work cannot narrow or substitute them silently. This includes protecting the acceptance surface from shortcuts such as weakening assertions, shrinking covered inputs, substituting a mock/narrower object, changing thresholds, bypassing failure propagation, or reducing a baseline when those would invalidate the claimed property.
4. **Independent acceptance need** — when executor self-attestation would be weak or gameable, preserve that completion requires an independent accepting boundary rather than letting executor-designed evidence become final proof.

Intent Take does not need to decide the exact command sequence, retry pattern, or verifier implementation when those are execution How.

## Stage 2 — compile verification structure

Execution Compile maps preserved proof semantics into the execution graph:

- attach local proof to the Task / Issue node whose outcome it establishes;
- create separate verification nodes when proof must observe multiple upstream results or needs fresh context / independent judgment;
- keep the **Global Gate** distinct from local node completion;
- bind protected Judge / Population / Object / Metric semantics into Boundaries and Verification so a cheaper substitute cannot complete the Goal;
- preserve sourced baselines and non-regression obligations when success depends on comparison with current behavior;
- make a newly created or materially changed gate demonstrate failure sensitivity when false-green is plausible;
- when independent acceptance is required, cap executor-owned evidence at `ready for independent acceptance`; only the independent boundary can satisfy global completion.

Verification topology should follow what must be proven, not a generic always-review stage. A simple task may have one local check plus the Global Gate. A behavior-preserving migration may require replay/diff, roundtrip proof, negative/failure-sensitivity evidence, or an independent acceptance node when governing coverage is incomplete.

## Visible-contract boundary

A genuinely hidden oracle, manager-side spot check, fresh-context challenge, or other acceptance mechanism whose strength depends on the executor not seeing it must stay outside the executor-visible carrier. Prompt Atlas may compile the requirement for independent acceptance and the property/boundary it must judge, but it must not expose the hidden cases or let the executor author the decisive oracle and then call itself complete.

If the runtime/harness cannot provide the required independent boundary, the executable graph may end at `ready for independent acceptance`; it must not fabricate parity with hidden or fresh-context verification.

## Runtime trust rules

During execution:

- insufficient, compromised, narrowed, skipped, fabricated, or stale proof is `UNMET`;
- local PASS unlocks dependent work but does not imply global completion;
- a failed verifier routes back to evidence-producing work or replanning while safe work remains;
- environment unavailability must remain explicit; it cannot be converted into a passing claim;
- when upstream changes invalidate downstream evidence, that evidence must be re-established before it can support completion;
- the executor may revise implementation How and the remaining graph, but may not silently weaken the proof obligation or integrity boundary.

## Placement

The final executable carrier should make trust semantics visible where they affect judgment:

- **State** — existing gates, baselines, proof state, available verifier, and verified/inferred/unmeasured status;
- **Decisions** — material verification ownership or branch choices already closed, with basis;
- **Boundaries** — protected Judge / Population / Object / Metric and any governing no-bypass or non-regression rule;
- **Graph** — verifier nodes and dependencies where verification has real orchestration meaning;
- **Verification** — local proof obligations, failure sensitivity, independent acceptance boundary, and the Global Gate;
- **Runtime** — failed or stale proof returns to work; only trusted Global Gate satisfaction completes.

Do not compile fixed retry counts, arbitrary failure-round budgets, mandatory progress files, or verifier topology that the task does not need. Those are execution mechanisms, not proof semantics.