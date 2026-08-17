# When a simple Taskbook is not enough

Read only after Goal is settled and complexity itself changes execution judgment, for example distinct outcomes / boundaries, real dependencies, later work that only execution Evidence can reveal, or cross-session continuation. This file only decides how those differences enter the Taskbook. It does not redefine Goal or precompile an implementation work plan for the Executor.

## Execution granularity

A Taskbook does not decompose implementation tasks for the Executor. Separate content only when a different result, judgment rule, binding constraint, or real dependency changes execution choice. Otherwise state one outcome / judgment over the open surface and let the Executor decide files, functions, work order, and local checks from the current repo.

A concrete edit point, helper, caller, or test found during Research does not gain authority merely because it is known. Unless the representation itself is fixed by Human / repo authority, or omitting it would make a fresh Executor judge incorrectly, cross a boundary, or fail to prove completion, keep it out of the Taskbook.

If an unresolved fact determines whether material work is safe, keep it as an Unknown / dependency and state what it changes. Do not expand that into a procedural `check X → edit Y` sequence.

## When only part is safe to advance

**The work that is safe now must not replace the full Goal.**

If current reality supports only part of the work, keep the full Goal and identify only the safe frontier current Evidence establishes. As execution Evidence makes later work decidable, update the affected part then. Adjacent residue does not enter Goal merely because it was discovered.

Usually no execution graph is needed. Record a relation only when it changes Executor choice, such as a real prerequisite, parallel conflict, shared authoritative surface, or results that must be verified together. Record only relations current reality supports. Work that depends on future Evidence enters only when that Evidence makes it real. A blocked branch must not freeze unrelated work.

## Starting point and baseline

Still-valid workspace changes aligned with Goal are the execution starting point. Do not redo them, do not shrink Goal to the current diff, and do not treat “already changed” as correctness Evidence.

A baseline belongs in the Taskbook only when it changes later judgment or distinguishes “already broken” from “this change broke it.” Whether a concrete command / target / parameter may be fixed follows the main Skill's Verification evidence rule: reality Evidence must show not only that it exists and has the intended semantics, but also that this concrete form adds decision value to completion judgment. Otherwise keep only the verification obligation.

If later judgment depends on a baseline, the Executor re-obtains it when first truly relying on it. A mismatch invalidates only work and Evidence that depended on that premise; still-valid work remains reusable.

## Verification and final judgment

Verification does not map one-to-one to implementation work. Start from completion claims, then decide what authoritative Evidence each claim needs. Combine Evidence that covers several changes; separate independent claims even when they come from one change.

Verification granularity follows **the behavior, boundary, risk, and authority that must be proven**, not the number of commits, files, tasks, or local tests. Prefer final observable behavior and long-lived constraints. Unit/build checks may contribute Evidence, but proximity to a change does not make them sufficient proof of Goal completion.

At execution end, judge the result again from Goal, binding constraints, completion claims, and current Evidence. A landed patch, completed task list, or green tests cannot substitute for that judgment. When Evidence covers only local implementation, preserve the material gap instead of promoting local PASS to Goal completion.

The Taskbook freezes what must be proven for Goal completion, not how the Executor debugs. A candidate discovered during Research does not automatically become a `0-hit / 0-count` requirement; use that only when the object has been proven to need removal and zero itself is part of Goal.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add extra judging machinery. Never manufacture success with skip/todo, weakened assertions, deleted live tests, mocked-away targets, swallowed failures, or `|| true`.

## Continue across sessions

Cross-session progress mechanisms belong to the Executor / runtime, not the Taskbook protocol. Continue from the same Taskbook, current reality, and still-valid Evidence, redoing only work whose premise changed or Evidence became stale. Do not create a Prompt Atlas-specific persistent Graph, manager state, or second Taskbook.
