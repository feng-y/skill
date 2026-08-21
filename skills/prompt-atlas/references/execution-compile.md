# When a simple Taskbook is not enough

Read only after Goal is settled and complexity itself changes the Graph structure of Execution or Verification judgment. This reference helps Prompt Atlas compile a complex handoff; it does not redefine Goal or design the Executor's patch, debugging flow, or scheduler.

## Execution

Compile a complex Goal's Execution as the **best-known complete Graph** a fresh Executor can directly advance:

- separate material work cuts when distinct outcomes, responsibilities, binding boundaries, or real dependencies change execution judgment;
- preserve an Evidence-backed material cut / relation when omitting it would only force the Executor to rediscover it;
- express dependency only when a real prerequisite, shared authoritative surface / conflict, jointly required outcome, or equivalent relation truly changes Executor choice;
- keep file/function/helper/caller detail, local edit order, patch shape, and local checks as How by default.

Graph completeness follows current **decision-relevant knowledge**. When current Evidence establishes `A → {B,C} → D`, express that structure now instead of hiding B/C/D merely to stay lazy or thin. Stop at the current frontier only when B/C/D existence, scope, or dependency still depends on future execution Evidence from A; extend the Graph after Evidence makes the downstream work real. **Best-known complete is not research-complete**: do not expand inventory, prove candidate implementations, scan territory that can only change How, or invent placeholder nodes/phases/taxonomy merely to complete the Graph.

Taskbook prose order does not create dependency. Work without a real dependency remains independent rather than being forced serial or parallel; one blocked branch does not freeze unrelated work; cohesive work is not fragmented merely to expose parallelism. A simple or linear task is only a degenerate Graph and does not require a diagram, Graph schema, or explicit node object.

## Unknowns and baselines

When an open fact determines whether material work is valid, crosses a binding boundary, or can start safely, Prompt Atlas establishes it upstream or keeps it as an explicit Unknown / dependency. When different answers change only implementation choice, leave it to the Executor.

A baseline belongs in the Taskbook only when it actually carries scope, coverage, attribution, or “pre-existing vs introduced regression” judgment. A concrete command / target / parameter is retained only when repo authority confirms it and omission would mislead. Research discovering a command is not sufficient reason to freeze it. The Executor re-obtains a baseline from current reality when first materially relying on it; mismatch makes only dependent work / Evidence stale.

## Verification / Evidence

Verification does not map one-to-one to implementation work or Graph nodes. Fix the completion claim first, then choose Evidence:

1. Evidence must first meet the confidence required by the claim.
2. Among paths that meet that threshold, prefer the lower-cost and more direct one.
3. Reuse authoritative tests/builds/replays/integration/runtime Evidence when they directly prove the claim.
4. Add the smallest focused test / check for new behavior, durable regression risk, or claims existing Evidence cannot reliably cover.

Do not require failing-test-first by default, and do not skip necessary regression Evidence merely because unit tests are expensive.

When current reality establishes a test/build/replay/integration path that directly covers key completion claims and an abstract obligation alone would let a fresh Executor under-verify with cheaper local checks, retain it as the **current fallback verification path**. It is a proof backstop, not an implementation plan or permanent command checklist. If implementation, binding, or reality makes it stale, the Executor re-derives coverage from repo authority and obtains equivalent or stronger Evidence.

A completion report / artifact needs producer, provenance, readiness, consumer, failure-semantics, or other authority investigation before handoff only when final judgment truly depends on it. If it is merely a replaceable candidate verifier, do not expand Research to preselect verifier topology.

At execution end, Evidence must support Goal, binding constraints, and completion claims rather than activity narration, self-reported PASS, or task completion. Read [verification-trust.md](verification-trust.md) only for a concrete risk that implementation is wrong while checks still show PASS, and add only the smallest check that can falsify that risk.

## Loop

Prompt Atlas does not own cross-session progress, retry, debugging, or the runtime scheduler, but the Taskbook must evolve cleanly through the host execution loop: `Graph → Executor outcome / candidate Evidence → Taskbook + current reality judgment → established Evidence / new reality → affected Graph`.

Executor reports, task checklists, and test output are candidate Evidence / navigation until independently verified; they cannot directly change reality or the Graph. Only established new Evidence / reality recomputes the dependency cone it actually affects. Extend the Graph when it makes contingent work real; remove a branch / dependency when Evidence proves it absent; split, merge, or reorder remaining work when scope, binding, or material relations change; and recompute corresponding Verification when completion claims / coverage are affected. Unrelated branches, still-valid work, and Evidence remain valid. Completed work does not reopen mechanically merely because the Graph changes, unless its Evidence premise or proven behavior was affected.

The Graph is the structure of Execution inside the Taskbook, not another runtime object. Do not add persistent Graph state, node taxonomy, a scheduler, manager protocol, or a second Taskbook merely to use Graph / Loop. Reuse host progress/state when it already exists; Prompt Atlas does not invent one when it does not.
