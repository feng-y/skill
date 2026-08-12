# When a simple Taskbook is not enough

Read only after Goal is settled, when the work is long, needs several different judgments, has real ordering constraints, needs stronger verification, or must continue across sessions.

Keep asking one question:

> **What would a fresh Executor misjudge, or fail to prove, if it were omitted?**

## Write judgments, not Research notes

Facts the Executor can reliably recompute from repo/runtime reality usually stay out. Keep facts whose omission would make the Executor remove the wrong thing, preserve the wrong thing, cross a boundary, or miss required verification. Deeper Research should compress into fewer stable judgments, not a longer fact dump.

Still-valid work already in the workspace is the starting point. Do not redo it, shrink Goal to match the current diff, or treat “already changed” as correctness Evidence.

A baseline belongs in the Taskbook only when it helps show that nothing was missed or separates “already broken” from “this change broke it.” Commands, targets, and parameters must come from the real environment rather than invention.

## Split work only when the judgment changes

If many objects can be handled by the same rule, keep them as one piece of work and let the Executor scan the agreed area. Do not split by file, function, or currently discovered instance. Split only when the local result, judgment rule, real dependency, or required proof is materially different.

If one missing fact makes even the first safe material change impossible, put closing that fact first; do not turn it into another broad Research phase.

Most tasks do not need an execution graph. Write a relation only when it changes what can happen next: B must wait for A's result, two pieces can safely run in parallel, several pieces write the same authoritative file, or several pieces must be verified together. Include only relations current reality already proves. Work that can only be discovered later should be added when it becomes real. One blocked branch must not freeze unrelated work.

## Say what proves Goal, not how to debug

The Taskbook states what Evidence must exist when Goal is complete. Build/test/replay order, “test after every file,” and other failure-localization tactics belong to the Executor unless Human/repo rules make them binding.

If the Taskbook relies on a baseline as a premise, the Executor re-obtains it before the first work that depends on it. A mismatch invalidates only dependent work and Evidence; still-valid parts continue.

Finding a candidate during Research does not make `0-hit / 0-count` binding. Use a zero check only when the item is already proven to be something that must disappear and zero itself is part of Goal.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add another judging mechanism.

Failure must stay honest: if a trusted baseline goes green→red, recover it or report the regression; if the same approach keeps failing without new Evidence, change to a justified strategy, switch to independent work, or report a blocker. Never manufacture success through skip/todo, weakened assertions, deleting live tests, mocking away the target, swallowing failures, or `|| true`.

## Make long work resumable

For a longer autonomous run, use existing `implement-notes` to record progress, material decisions and Evidence, blockers, and where the next session should resume. A new session reads it first and repeats only work whose premise changed or whose Evidence went stale. Do not create a second Taskbook, persistent execution graph, or manager state.
