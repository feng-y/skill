# Verification / Evidence Trust

Read only when ordinary repo verification may false-pass, be gameable, fail silently, or the result genuinely needs extra independence. Prefer existing protected repo verification when it already covers the Goal; do not add private or independent judges merely to appear stricter.

## Evidence trust

- **Prove the provider really works.** A documented command, script, or CI entry is only a claim until availability and failure propagation are evidenced. Check before Handoff when possible; execution-only facts belong in Task 0. Missing, no-op, or non-propagating checks do not produce valid Evidence.
- **Prove the actual claim.** Build, lint, coverage, activity, or a local test proves only behavior it actually covers. A provider cannot establish facts outside its observed scope.
- **Follow the real affected surface.** Verification scope follows actual change surface, effective binding/config, and real consumers/targets. Cleanup/refactor labels and expected `0-diff` do not reduce required Verification.
- **Keep premises fresh.** Version, environment, target, binding/config, or upstream behavior changes may stale Evidence when they affect what it proved; unaffected Evidence remains reusable.
- **Protect the judge.** Unless Goal explicitly requires a judge change and equivalent trustworthy Verification remains, do not weaken assertions, shrink coverage, skip tests, mock away the tested object, lower thresholds, swallow failure propagation, or edit verification scripts to manufacture PASS.
- **Protect baselines.** Regression against an authoritative baseline is not acceptable merely because the new path is simpler or cheaper. Freeze only baselines the repo itself treats as authoritative; do not manufacture metrics.

## Evidence must be judgeable

Executor `PASS`, summaries, screenshots-as-description, or “should pass” are not Evidence. Critical Evidence should answer: **what ran, against which target/revision/config, what result occurred, and where the raw/reproducible output lives.**

When Prompt Atlas or the judging boundary can access the authoritative repo/runtime, reacquire final-judgment-critical repo-authoritative Evidence at reasonable cost rather than relying only on Executor narration. Do not mechanically rerun every still-valid Task-local check.

When the judging boundary cannot access the environment, Evidence must travel with enough provenance: actual command/probe, target/revision, material config/binding, exit/verdict, and machine-judgeable raw output or a stable artifact/reference. Unreviewable second-hand summaries remain an evidence gap.

## Reverse validation

When a critical check could no-op, false-green, or fail silently, create one bounded controlled failure, confirm that the judge turns red, restore state, then run the normal Verification. Reverse validation proves the judge signal path, not Goal behavior itself.

## Visible and private Evidence

**Visible Verification** is Executor-visible and is the default. If protected repo tests, replay, CI, schema, or other judges are sufficient, do not add private checks.

Use a small amount of **private Evidence** only when a visible judge can be directly targeted, fixed samples can be overfit, or public Verification is insufficient for a trustworthy judgment. Private checks must derive from the same public Goal and required Verification; they may vary samples or observation paths but cannot add hidden requirements. To count as private, form them before implementation and isolate them from the Executor when the runtime allows it.

If a private check is disclosed to the Executor before implementation, it becomes visible Evidence. It may still be useful, but it no longer carries private-test independence.

## Independent Evidence

When Executor self-proof remains gameable, visible/private judges are still manipulable, or task risk genuinely requires independence, a non-implementing subject may reacquire Evidence in the authoritative environment.

Independence means the subject did not materially implement the work and independently faces the Goal, repo verification authority, protected baselines, and real environment. Model/provider identity alone neither proves nor defeats independence.

Independent Evidence is a conditional trust mechanism, not a fixed Acceptor role or Acceptance workflow. If required independent Evidence cannot be obtained, report the exact evidence gap; do not downgrade it into PASS.

## Non-PASS

Fabricated, skipped, stale, under-covered, unreviewable, judge-weakened, or improperly claimed private/independent Evidence cannot support PASS.

The next legitimate route is to obtain new valid Evidence, adjust remaining Execution/Graph and reverify, report a truthful blocker, or return to the relevant Human-owned Goal/authority boundary. Do not hide evidence gaps behind completion or acceptance terminology.
