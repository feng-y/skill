# Completion Trust

Use when completion can false-pass or needs fresh or independent acceptance.

Proof must be:

1. **direct** — demonstrate the required behavior, not a convenient proxy;
2. **failure-sensitive** — a critical verifier can be shown to fail when the property is broken;
3. **intact** — Judge, Population, Object, Metric, baselines, and failure propagation cannot be silently weakened;
4. **independent when required** — Executor self-attestation is not final acceptance.

Skipping tests, weakening assertions, narrowing coverage, mocking away the object, swallowing failures, or editing the judge is not completion unless explicitly required and equally trustworthy.

Attach proof to the work it proves. Use `Task 0 → Execute with local proof → Global Gate`; add a separate `Verify` node only for integration, cross-result, hidden, fresh, or independent proof.

Local PASS may unlock dependent work; only the Global Gate closes the Goal. If required independent acceptance is unavailable, stop at `ready for independent acceptance`, not `PASS`.

Compromised, fabricated, skipped, or stale proof is unmet. Upstream changes invalidate downstream proof when they affect what it established.
