# Verification / Evidence Trust

Read only when Evidence trust or independence can change completion judgment. Provider executability, claim coverage, Evidence freshness/provenance/reuse, and ordinary scope judgment remain owned by [execution-compile.md](execution-compile.md).

Default to existing protected repo Verification when it sufficiently covers the Goal. An explicit Human or repo-verification-authority requirement for independent verification remains binding.

## Trust judgment

When no binding independence requirement exists, ask one question: **is there a concrete and material failure mode that could let the Executor obtain visible PASS while the Goal or required Verification is not actually established?**

If not, stop adding judge machinery. If yes, name that failure mode and add only the minimum trust Evidence needed to falsify it. Typical causes are a judge that does not observe the real target, an Executor-controlled or directly targetable oracle/fixed sample, material coverage or scope supported only by the implementer's own derivation, or decisive Evidence available only as Executor self-report. General uncertainty is not a trust gap; ordinary coverage/scope remains an execution-compile judgment.

## Judge integrity

Unless Human/Goal authority explicitly permits a judge change and equivalent trustworthy Verification remains, do not manufacture PASS by weakening assertions or coverage, skipping checks, mocking away the real object, lowering thresholds, swallowing failure propagation, or editing verification scripts. Breaking an authoritative baseline is a regression; freeze metrics such as test count, coverage, schema, or replay baseline only when the repo itself treats them as judges.

When a critical judge may no-op, false-green, or fail silently, create one bounded controlled failure, confirm that the signal turns red, restore state, then run normal Verification. Reverse validation proves judge integrity, not Goal behavior.

## Visible and private Evidence

**Visible Verification** is Executor-visible and is the default. Use a small amount of **private Evidence** only when the Trust judgment identifies a failure mode that isolated observation can actually falsify, or binding authority itself requires private verification.

Private checks must derive from the same public Goal and Verification requirement and cannot add hidden requirements. They may vary samples, scope derivation, or observation paths, but must target the identified gap. To carry private-evidence value, form them before implementation and isolate them from the Executor when the runtime allows it; disclosure before implementation reduces them to visible Evidence. More private checks do not add trust by count alone.

## Independent Evidence

Use independent Evidence when Executor self-proof is insufficient, visible/private judges remain manipulable, a material coverage/claim conclusion depends only on the implementer's own derivation, or binding authority explicitly requires independent reacquisition.

Independence comes from not materially implementing the work and independently facing the Goal, repo verification authority, protected baselines, and real environment. Model/provider identity alone neither proves nor defeats independence.

Independent Evidence is a conditional trust mechanism, not a fixed Acceptor role or Acceptance workflow. If required independent Evidence cannot be obtained, report the exact evidence gap; do not downgrade it into PASS.

## Non-PASS

Fabricated, skipped, stale, under-covered, unreviewable, judge-weakened, materially contradictory, improperly claimed private Evidence, or missing required independent Evidence cannot support PASS.

The next legitimate route is to obtain new valid Evidence, adjust remaining Execution/Graph and reverify, report a truthful blocker, or return to the relevant Human-owned Goal/authority boundary. Do not hide evidence gaps behind completion or acceptance terminology.
