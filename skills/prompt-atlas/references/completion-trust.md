# Completion Trust

Use when a task can appear complete without proving the requested result.

## Proof rules

- **Prove the property directly.** Build, lint, coverage, or activity are not substitutes when they do not establish the Goal.
- **Prove the judge can fail.** When a critical check could no-op or false-pass, create a bounded failure, show the signal, restore the state, then run the normal proof.
- **Freeze the judge.** The Executor may not weaken assertions, shrink the judged population, substitute a mock for the real object, lower thresholds, bypass failure propagation, skip tests, or edit acceptance criteria unless Stable Intent explicitly requires that change and preserves equivalent trust. Common cheap compliance shapes include `.skip`, deleting tests, and swallowing failure with `|| true`; these are false completion, not clever shortcuts.
- **Preserve baselines.** A cheaper result below an evidenced baseline is regression, not completion, unless explicitly authorized.

Attach local proof to each task. Local PASS may unlock dependent work; it does not close the complete Goal. Upstream changes invalidate downstream evidence when they affect what it proved.

## Private acceptance

Before Handoff, derive and reserve a small private acceptance set—normally two or three checks—against the public Goal, boundaries, and completion properties. Keep it outside the Executor-visible taskbook and freeze it before execution. Private checks may use unlisted samples or a different observation route, never hidden requirements.

After execution, rerun the visible judges and then the reserved private checks before final PASS. A failed private check is an exact residual against the public contract, not a new requirement.

## Independent acceptance

Use an independent Acceptor (a judge that did not do the work) when the same agent implemented the work or Executor self-attestation remains gameable or incomplete. Bind it, or reserve the accepting boundary, before execution. Executor implementation notes and evidence are input, not final judgment.

If the accepting environment is unavailable, return a self-contained acceptance handoff with the authoritative taskbook, Executor result and evidence, visible acceptance, reserved private checks, protected judges and baselines, and the required final report—PASS or the exact residual. The highest honest result remains `ready for independent acceptance`, not `PASS`.

Compromised, fabricated, skipped, or stale proof is unmet. Non-PASS routes to new evidence, a materially different plan, a truthful blocker, or the relevant Human boundary; it is never rewritten as completion.
