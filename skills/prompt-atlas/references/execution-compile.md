# When a simple Taskbook is not enough

Read only after Goal is settled but the task is long, needs several different judgments, real ordering, stronger Verification, or continuation across sessions. This file only keeps a complex Taskbook executable; it does not redefine Goal or Human / Executor responsibility.

## How to split implementation work

If one result and judgment apply to a set of objects, keep them as one piece of work and let the Executor scan the agreed scope. Do not split by file, function, or currently discovered instance. Split only when the local result, judgment rule, real dependency, or binding constraint is different.

Each piece of work should say what must be true when it is done, what judgment applies, and how it truly relates to other work. It is not a predicted patch. Do not default to `edit file A → add helper B → update caller C → run test D` as task granularity.

If one fact blocks the first safe material work, put that check first. Do not turn it into another broad Research phase.

## When only part is safe to advance

**The work that is safe now must not replace the full Goal.**

If current reality supports only part of the work, advance only that part while keeping the full Human Goal. As new Evidence makes later work decidable, add it then. Adjacent residue also does not enter Goal merely because it was discovered.

Usually no execution graph is needed. Write a relation only when it changes the next choice: B truly waits for A, two items can safely run in parallel, several items write the same authoritative surface, or several results must be verified together. Write only relations current reality supports; work that depends on future Evidence should be added only when it becomes real. A blocked branch must not freeze unrelated work.

## Starting point and baseline

Still-valid workspace changes aligned with Goal are the execution starting point. Do not redo them, do not shrink Goal to the current diff, and do not treat “already changed” as correctness Evidence.

A baseline belongs in the Taskbook only when it helps detect missing coverage or distinguish “already broken” from “this change broke it.” Whether a concrete command / target / parameter may be fixed in the Taskbook follows the main Skill's Verification evidence rule: without reality Evidence that it exists and has the intended semantics, keep only the verification obligation instead of inventing a command.

If later judgment depends on a baseline, the Executor re-obtains it before first relying on it. A mismatch invalidates only work and Evidence that depended on that premise; still-valid work remains reusable.

## How to split Verification

Verification does not map one-to-one to implementation work. Start from completion claims, then decide what authoritative Evidence each claim needs. If one Evidence path covers several implementation changes, combine it. If one implementation change carries several independent claims, verify them separately.

Verification granularity follows **the behavior, boundary, risk, and authority that must be proven**, not the number of commits, files, or tasks. Prefer final observable behavior and long-lived constraints. Local unit/build checks may contribute Evidence, but being close to an implementation step does not make them sufficient proof of Goal completion.

The Taskbook freezes what must be proven for Goal completion, not how the Executor debugs. A candidate discovered during Research does not automatically become a `0-hit / 0-count` requirement; use that only when the object has been proven to need removal and zero itself is part of Goal.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add extra judging machinery.

Failure must remain honest. If a trusted baseline turns green→red, recover or report it accurately. If the same approach fails repeatedly without new Evidence, switch to a justified strategy, work an independent branch, or report a blocker. Never manufacture success with skip/todo, weakened assertions, deleted live tests, mocked-away targets, swallowed failures, or `|| true`.

## Continue across sessions

For a longer run, use existing `implement-notes` for progress, key decisions/Evidence, blockers, and the resume point. A new session reads it first and redoes only work whose premise changed or Evidence became stale. Do not create a second Taskbook, persistent Graph, or manager state.
