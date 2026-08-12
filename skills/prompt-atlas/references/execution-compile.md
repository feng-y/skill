# When a simple Taskbook is not enough

Read only after the Goal is settled, when the work is long enough to require several genuinely different judgments, real dependencies, stronger verification, or cross-session continuation.

This file still serves one question:

> **What would a fresh Executor misjudge, or fail to prove, if it were omitted?**

## Write judgments, not Research

Facts the Executor can reliably recompute from repo/runtime reality should usually stay out. Keep non-obvious facts whose omission would make the Executor delete the wrong thing, preserve the wrong thing, cross a boundary, or miss required verification. More Research should compress into fewer stable judgments, not more instructions.

Still-valid work already in the workspace is the execution starting point. Do not redo it, do not shrink the Goal to match the current diff, and do not treat “already changed” as correctness Evidence.

A baseline belongs in the Taskbook only when it helps show coverage or distinguish “already broken” from “this change broke it.” Commands, targets, and parameters must come from real authority rather than invention.

## Split work only where judgment changes

If many instances can be handled by the same rule, keep one work unit and let the Executor scan the full surface. Do not split by file, function, or currently discovered instance. Split only when the outcome, judgment, real dependency, or required proof is materially different.

If one missing fact makes even the first safe material change impossible, put closing that fact first; do not turn it into another broad Research phase.

Most work does not need a Graph. Write relations only when the relation itself changes execution choices: B truly consumes A's result, two units can safely run in parallel, several units write the same authoritative surface, or a combined result needs joint verification. Include relations current Evidence already proves; do not predict contingent work that only future Evidence can reveal. One blocked branch must not freeze unrelated work.

## Say what proves completion, not how to debug

Verification fixes what must be proven. Build/test/replay order, “test after every file,” and other failure-localization tactics belong to the Executor unless Human/repo authority makes them binding.

If the Taskbook relies on a baseline as a premise, the Executor re-obtains it before the first work that depends on it. A mismatch invalidates only dependent work and Evidence; still-valid parts continue.

Do not turn a Research candidate into `0-hit / 0-count` merely because it was found. A zero check is binding only when the item is already proven to belong to what must disappear and zero itself is part of the completion claim.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add another judging mechanism.

Failure must stay honest too: if a trusted baseline goes green→red, recover it or report the regression; if the same approach keeps failing without new Evidence, change to a justified strategy, switch to independent work, or report a blocker. Never manufacture success through skip/todo, weakened assertions, deleting live tests, mocking away the target, swallowing failures, or `|| true`.

## Make long work resumable

For a longer autonomous run, use existing `implement-notes` to record progress, material decisions/Evidence, blockers, and the resume point. A new session restores from there and repeats only work whose premise changed or whose Evidence went stale. Do not create a second Taskbook, persistent Graph model, or manager state.
