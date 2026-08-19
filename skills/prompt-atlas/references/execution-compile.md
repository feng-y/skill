# When a simple Taskbook is not enough

Read only after Goal is settled and complexity itself changes execution or Verification judgment, for example distinct outcomes / boundaries, real dependencies, later work that only execution Evidence can reveal, verification cost / Evidence selection that changes completion proof, or cross-session continuation. This file only decides how those differences enter the Taskbook. It does not redefine Goal or precompile a file-by-file or function-by-function implementation plan for the Executor.

## Execution granularity

A Taskbook should still compile a complex Goal to a level a fresh Executor can directly advance. Separate work when a distinct outcome / responsibility, binding boundary, or real dependency changes execution judgment. Also preserve a material cut when collapsing it would force a fresh Executor to rediscover something already supported by sufficient Evidence. In contrast, files, functions, helpers, call order, and local checks remain Executor How recovered from the current repo; do not expand them into a predicted-patch checklist merely to make the Taskbook look more executable.

A concrete edit point, helper, caller, or test found during Research does not gain authority merely because it is known. Unless the representation itself is fixed by Human / repo authority, or omitting it would make a fresh Executor judge incorrectly, cross a boundary, or fail to prove completion, keep it out of the Taskbook.

If an unresolved fact determines whether material work is safe, keep it as an Unknown / dependency and state what it changes. Do not expand that into a procedural `check X → edit Y` sequence.

## When only part is safe to advance

**The work that is safe now must not replace the full Goal.**

If current reality supports only part of the work, keep the full Goal and identify only the safe frontier current Evidence establishes. As execution Evidence makes later work decidable, update the affected part then. Adjacent residue does not enter Goal merely because it was discovered.

Usually no execution graph is needed. Record a relation only when it changes Executor choice, such as a real prerequisite, independently parallel work, a parallel conflict, shared authoritative surface, or results that must be verified together. Record only relations current reality supports. Work that depends on future Evidence enters only when that Evidence makes it real. A blocked branch must not freeze unrelated work.

## Starting point and baseline

Still-valid workspace changes aligned with Goal are the execution starting point. Do not redo them, do not shrink Goal to the current diff, and do not treat “already changed” as correctness Evidence.

A baseline belongs in the Taskbook only when it changes later judgment or distinguishes “already broken” from “this change broke it.” A concrete command / target / parameter may be included as a **current fallback verification path** when reality Evidence shows that it exists, has the intended semantics, directly covers a completion claim or key risk, and omitting it would materially increase under-verification risk. That path is not permanent authority and does not freeze the corresponding implementation.

If later judgment depends on a baseline, the Executor re-obtains it when first truly relying on it. A mismatch invalidates only work and Evidence that depended on that premise; still-valid work remains reusable.

## Verification and final judgment

Verification does not map one-to-one to implementation work. Start from completion claims, then decide what authoritative Evidence each claim needs. Combine Evidence that covers several changes; separate independent claims even when they come from one change.

First require Evidence to provide sufficient confidence for the completion claim. Among verification paths that meet that bar, prefer the lower-cost and more direct one rather than requiring a failing test before implementation by default. Reuse authoritative existing tests, builds, replays, integration checks, or runtime Evidence when they directly prove the claim. Add the smallest focused test / check when new behavior, a durable regression risk, or a claim not reliably covered by existing Evidence requires it. For complex legacy / infrastructure boundaries, broad mock- or fixture-heavy unit tests that merely mirror implementation detail without adding material confidence are not a default obligation.

When current reality establishes a set of tests / builds / replays / integration checks that directly covers key completion claims, and a purely abstract obligation would let a fresh Executor substitute a cheaper but insufficient check, keep that set as the **current fallback verification path** in the Taskbook. This is a verification backstop, not an implementation plan. The Executor still owns the exact verifier composition. If implementation, binding, or reality changes make the current path inaccurate, re-derive the verifier from repo authority and obtain equivalent or stronger Evidence; do not mechanically run stale commands and do not reduce coverage merely because the path changed.

Verification granularity follows **the behavior, boundary, risk, and authority that must be proven**, not the number of commits, files, tasks, or local tests. Prefer final observable behavior and long-lived constraints. Unit/build checks may contribute Evidence, but proximity to a change does not make them sufficient proof of Goal completion.

At execution end, judge the result again from Goal, binding constraints, completion claims, and current Evidence. A landed patch, completed task list, or green tests cannot substitute for that judgment. When Evidence covers only local implementation, preserve the material gap instead of promoting local PASS to Goal completion.

The Taskbook freezes what must be proven for Goal completion, not how the Executor debugs. A candidate discovered during Research does not automatically become a `0-hit / 0-count` requirement; use that only when the object has been proven to need removal and zero itself is part of Goal.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add extra judging machinery. Never manufacture success with skip/todo, weakened assertions, deleted live tests, mocked-away targets, swallowed failures, or `|| true`.

## Continue across sessions

Cross-session progress mechanisms belong to the Executor / runtime, not the Taskbook protocol. Continue from the same Taskbook, current reality, and still-valid Evidence, redoing only work whose premise changed or Evidence became stale. Do not create a Prompt Atlas-specific persistent Graph, manager state, or second Taskbook.
