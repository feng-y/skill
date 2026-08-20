# When a simple Taskbook is not enough

Read only after Goal is settled and complexity itself changes Execution or Verification judgment. This reference helps Prompt Atlas compile a complex handoff; it does not redefine Goal or design the Executor's patch, debugging flow, or scheduler.

## Execution

Compile a complex Goal to material granularity a fresh Executor can directly advance:

- separate material work cuts when distinct outcomes, responsibilities, binding boundaries, or real dependencies change execution judgment;
- preserve an Evidence-backed material cut when omitting it would only force the Executor to rediscover it;
- keep file/function/helper/caller detail, local edit order, patch shape, and local checks as How by default.

Taskbook prose order does not create dependencies. Record only relations that truly change Executor choice, such as a real prerequisite, shared authoritative surface / conflict, or a result that must be jointly accepted. Work without such a relation is neither forced serial nor forced parallel, and cohesive work is not fragmented merely to expose parallelism.

When reality supports only part of the Goal now, keep the full Goal and shrink only the current safe frontier. Work that depends on future execution Evidence is added only after it becomes real. A blocked branch does not freeze unrelated work.

## Unknowns and baselines

When an open fact determines whether material work is valid, crosses a binding boundary, or can start safely, Prompt Atlas establishes it upstream or keeps it as an explicit Unknown / dependency. When different answers change only implementation choice, leave it to the Executor.

A baseline belongs in the Taskbook only when it actually carries scope, coverage, attribution, or “pre-existing vs introduced regression” judgment. A concrete command / target / parameter is retained only when repo authority confirms it and omission would mislead. Research discovering a command is not sufficient reason to freeze it. The Executor re-obtains a baseline from current reality when first materially relying on it; mismatch makes only dependent work / Evidence stale.

## Verification / Evidence

Verification is not mapped one-to-one to implementation work. Fix the completion claim first, then choose Evidence:

1. Evidence must first meet the confidence required by the claim.
2. Among paths that meet that threshold, prefer the lower-cost and more direct one.
3. Reuse authoritative tests/builds/replays/integration/runtime Evidence when they directly prove the claim.
4. Add the smallest focused test / check for new behavior, durable regression risk, or claims existing Evidence cannot reliably cover.

Do not require failing-test-first by default, and do not skip necessary regression Evidence merely because unit tests are expensive.

When current reality establishes a test/build/replay/integration path that directly covers key completion claims and an abstract obligation alone would let a fresh Executor under-verify with cheaper local checks, retain it as the **current fallback verification path**. It is a proof backstop, not an implementation plan or permanent command checklist. If implementation, binding, or reality makes it stale, the Executor re-derives coverage from repo authority and obtains equivalent or stronger Evidence.

A completion report / artifact needs producer, provenance, readiness, consumer, failure-semantics, or other authority investigation before handoff only when final judgment truly depends on it. If it is merely a replaceable candidate verifier, do not expand Research to preselect verifier topology.

At execution end, Evidence must support Goal, binding constraints, and completion claims rather than activity narration, self-reported PASS, or task completion. Read [verification-trust.md](verification-trust.md) only for a concrete risk that implementation is wrong while checks still show PASS, and add only the smallest check that can falsify that risk.

## Continuation

Cross-session progress, resume state, retry, and debugging loops belong to Executor / runtime rather than Prompt Atlas Taskbook protocol. When new Evidence invalidates a premise, recompute only its dependency cone; still-valid Goal, work, and Evidence remain reusable.
