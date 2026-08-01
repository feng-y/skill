# Completion Trust

Use when a task can appear complete without proving the requested result.

## Proof rules

- **Prove the property directly.** Build, lint, coverage, or activity are not substitutes when they do not establish the Goal.
- **Prove the judge can fail.** When a critical check could no-op or false-pass, create a bounded failure, show the signal, restore the state, then run the normal proof.
- **Freeze the judge.** The Executor may not weaken assertions, shrink the judged population, substitute a mock for the real object, lower thresholds, bypass failure propagation, skip tests, or edit acceptance criteria unless Stable Intent explicitly requires that change and preserves equivalent trust. Common cheap compliance shapes include `.skip`, deleting tests, and swallowing failure with `|| true`; these are false completion, not clever shortcuts.
- **Preserve baselines.** A cheaper result below an evidenced baseline is regression, not completion, unless explicitly authorized.

Attach local proof to each task. Local PASS may unlock dependent work; it does not close the complete Goal. Upstream changes invalidate downstream evidence when they affect what it proved.

## Independent acceptance

Use a fresh or independent Acceptor (a judge that did not do the work) when Executor self-attestation remains gameable or incomplete. Bind or preserve the accepting boundary before execution. An accepting boundary that exists only in the author's current session is broken: a new conversation must be able to recover it and judge the result. Keep visible criteria with the taskbook; keep hidden cases and private proof outside the Executor-visible taskbook. If no accepting environment exists, the highest honest result is `ready for independent acceptance`, not `PASS`.

Compromised, fabricated, skipped, or stale proof is unmet. Non-PASS routes to new evidence, a materially different plan, a truthful blocker, or the relevant Human boundary; it is never rewritten as completion.
