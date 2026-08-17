# When a simple Taskbook is not enough

Read only after Goal is settled but the task is long, needs several different judgments, real dependencies, stronger Verification, or continuation across sessions. This file helps a complex Taskbook stay **decision-complete while implementation-open**. It does not redefine Goal or precompile the Executor's patch.

## Keep Execution at judgment granularity

A Taskbook is not a task list. If one result, judgment, and binding constraint govern a set of objects, express that level once and let the Executor find the full surface in the real repo. Split only when the local result, judgment rule, real dependency, or binding constraint is different.

Each piece needs only to say what must be true when done, what judgment governs the scope, and what real dependency connects it to other results. If steps can change order, file, helper/class, or local implementation without changing Goal, risk, or completion proof, do not encode them. `edit A → add B → update C → run D`, file/symbol/line names, candidate classes, and the current patch idea are implementation intelligence by default, not execution contract.

A concrete detail belongs only when **removing it would allow the Executor to produce an implementation that still appears to satisfy the high-level wording while violating authority / boundary / risk / completion contract**. “Already discovered,” “likely to change,” or “helps a fresh Executor start faster” is not enough. Navigation that can be cheaply and reliably recomputed from current repo/runtime stays with the Executor.

Usually no execution graph is needed. State a relation only when the relation itself changes the correct execution choice: one result truly depends on Evidence from another, two changes contend for the same authoritative surface, or several results jointly satisfy one completion claim. Do not promote ordinary construction order into dependency.

## When only part is safe to advance

**The work that is safe now must not replace the full Goal.**

If reality supports only part of the Goal, preserve the full Goal and state only the current material boundary and why the rest is not yet decidable. Handle later work when execution Evidence makes it real. Adjacent residue does not enter Goal merely because it was discovered.

A blocked branch must not freeze unrelated material work, but Prompt Atlas does not need to pre-slice every possible branch into future tasks. Preserve only dependencies that already change the current execution choice.

## Starting point and baseline

Still-valid workspace changes aligned with Goal are the execution starting point. Do not redo them, shrink Goal to the current diff, or treat “already changed” as correctness Evidence.

Starting reality keeps only facts that change Goal, a binding boundary, a material dependency, or completion proof. Concrete code anchors, file inventories, and discovered surfaces that the Executor can reliably reconstruct from the authoritative repo do not need a second copy in the Taskbook; reference existing authority when needed.

A baseline belongs only when it distinguishes “already broken” from “this change broke it,” or otherwise changes completion judgment. Finding an existing command / target / parameter does not make it Taskbook contract. Fix it only when it is itself an authoritative acceptance interface, an irreplaceable risk falsification, or omitting it would make the completion claim ambiguous. Otherwise keep only the verification obligation and let the Executor select the real Evidence path.

If later judgment depends on a baseline, the Executor re-obtains it before first relying on it. A mismatch invalidates only work and Evidence that depended on that premise; still-valid work remains reusable.

## Verification follows claims, not construction items

Verification does not map one-to-one to Execution. Start from Goal completion claims, then decide what authoritative Evidence each claim needs. Combine scopes when one Evidence path covers them; separate independent claims even if they arise from one implementation surface.

Verification granularity follows **the behavior, boundary, risk, and authority that must be proven**, not the number of commits, files, tasks, or discovered tests. Prefer final observable behavior and long-lived constraints. Local unit/build checks may contribute Evidence, but proximity to a code change does not make them sufficient proof of Goal completion.

The Taskbook freezes what must be proven, not how the Executor debugs. A case found during Research is Evidence / a risk example by default, not automatically a checklist item. Keep a concrete case or target only when authority fixes it or it is an irreplaceable falsification boundary. A discovered candidate does not automatically become a `0-hit / 0-count` requirement; use that only when the object has been proven to require removal and zero itself is part of Goal.

If there is a concrete risk that the implementation is wrong while checks still show PASS, read [verification-trust.md](verification-trust.md). Otherwise do not add extra judging machinery.

Failure must remain honest. If a trusted baseline turns green→red, recover or report it accurately. If the same approach fails repeatedly without new Evidence, switch to a justified strategy, work an independent branch, or report a blocker. Never manufacture success with skip/todo, weakened assertions, deleted live tests, mocked-away targets, swallowed failures, or `|| true`.

## Continue across sessions

For a longer run, use existing `implement-notes` for progress, key decisions/Evidence, blockers, and the resume point. A new session reads it first and redoes only work whose premise changed or Evidence became stale. Do not create a second Taskbook, persistent Graph, or manager state.
