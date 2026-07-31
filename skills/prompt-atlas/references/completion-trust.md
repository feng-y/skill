# Completion Trust

Use this reference only when the Goal or governing repo contract makes correctness/completion proof material. It is not a generic instruction to add another review, re-check, or verifier to every task.

Intent Take preserves **what must be proven**. Execution Compile decides whether that obligation has orchestration meaning as local proof, a verifier node, or the Global Gate. The executor runs the visible proof but cannot weaken its semantics or self-certify evidence that requires an independent boundary.

## Proof semantics

Preserve the minimum proof properties needed for the claim:

1. **Directness** — prefer evidence that demonstrates the intended behavior/result. Existing authoritative acceptance paths outrank convenient proxies such as build, lint, or coverage when those proxies do not prove the target property.
2. **Failure sensitivity** — when a new or changed gate could false-pass, require evidence that it can distinguish right from wrong.
3. **Integrity boundary** — when a cheaper false pass is plausible, freeze the material **Judge, Population, Object, and Metric** so downstream work cannot silently weaken assertions, shrink coverage, substitute a narrower/mock object, alter thresholds, bypass failure propagation, or reduce a protected baseline.
4. **Independent acceptance** — when executor self-attestation remains gameable or incomplete, final completion belongs to a fresh/independent accepting boundary.

Intent Take need not choose exact commands, retry patterns, or verifier implementation when those are execution How.

## Lower into the graph

Execution Compile attaches proof where it matters:

- local proof belongs to the node whose outcome it establishes;
- a separate verifier node exists only when proof spans upstream results or genuinely needs fresh/independent judgment;
- the Global Gate stays distinct from local completion;
- protected Judge / Population / Object / Metric and non-regression semantics stay binding;
- executor-owned evidence stops at `ready for independent acceptance` when another boundary owns final judgment.

Verification topology follows the property being proven, not a default always-review workflow.

## Visible-contract boundary

A hidden oracle, manager-side spot check, fresh-context challenge, or other mechanism whose strength depends on executor independence stays outside the executor-visible carrier. Prompt Atlas may state the property and accepting boundary; it must not expose hidden cases or let the executor author the decisive oracle and then certify itself.

If the runtime/harness cannot provide a required independent boundary, the graph may end at `ready for independent acceptance`; it must not claim equivalent proof.

## Runtime truth

Insufficient, compromised, narrowed, skipped, fabricated, or stale proof is `UNMET`. A local PASS can unlock dependent work without proving the whole Goal. Failed proof returns to evidence-producing work or replanning while safe work remains. Environment unavailability stays explicit. Upstream changes invalidate downstream evidence when the change affects what that evidence proved.
