# Completion Trust

Use this reference when completion can false-pass or needs a fresh or independent accepting boundary.

## Proof

Preserve four properties:

1. **Directness** — evidence should demonstrate the required behavior; build, lint, or coverage are not substitutes when they do not prove it.
2. **Failure sensitivity** — a critical verifier must be shown to fail when the protected property is deliberately broken, then restored.
3. **Integrity** — protect the Judge, Population, Object, Metric, baselines, and failure propagation from silent weakening.
4. **Independence** — when Executor self-attestation is gameable or incomplete, final acceptance belongs to a fresh or independent boundary.

Skipping tests, weakening assertions, narrowing coverage, mocking away the object under test, swallowing failures, or editing the judge is not completion unless that proof-surface change is explicitly part of the Goal and preserves equivalent trust.

## Placement

Attach proof to the work it proves. A simple graph keeps local proof inside execution:

```text
Task 0 → Execute with local proof → Global Gate
```

Add a separate `Verify` node only for integration, cross-result, hidden, fresh-context, or independent proof.

Local PASS may unlock dependent work; it never closes the complete Goal. The Global Gate checks the requested result, confirmed boundaries, protected proof surfaces, regressions, residuals, and delivery.

## Independent acceptance

When independence is required, the taskbook states the property, required separation, and accepting boundary without exposing private or hidden cases. The Executor cannot author the decisive oracle and certify itself.

If the runtime cannot provide that boundary, visible work may finish, but the completion ceiling is `ready for independent acceptance`, not `PASS`.

Insufficient, compromised, skipped, fabricated, or stale proof is unmet. Upstream changes invalidate downstream proof when they affect what it established.
