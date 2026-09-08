# When a simple Taskbook is not enough

Read only after Intent take has settled Goal, Human-owned choices, and binding boundaries far enough that a fresh Executor does not need to redo intent judgment and can safely begin material work, and complexity itself changes the Graph structure of Execution or Verification judgment. This reference does not define Intent compile itself or redefine Intent / Goal. The executable contract from Intent compile must already be established; this reference only helps Prompt Atlas structure complex Execution / Verification and does not design the Executor's patch, debugging flow, or scheduler.

## Execution

The Graph structures only established Execution inside the executable contract; it cannot determine Intent, Goal, or binding constraints in reverse. Compile a complex Goal's Execution as the **best-known complete Graph** a fresh Executor can directly advance:

- separate material work cuts when distinct outcomes, responsibilities, binding boundaries, or real dependencies change execution judgment;
- give every material work cut an independently judgeable material outcome / responsibility / binding boundary: when it fails, the judge can identify which material outcome is false rather than turning one Verification claim into an Execution cut;
- preserve an Evidence-backed material cut / relation when omitting it would only force the Executor to rediscover it;
- express dependency only when a real prerequisite, shared authoritative surface / conflict, jointly required outcome, or equivalent relation truly changes Executor choice;
- keep file/function/helper/caller detail, local edit order, patch shape, implementation choice, and local checks as How by default.

Graph completeness follows current **decision-relevant knowledge**. When current Evidence establishes `A → {B,C} → D`, express that structure now instead of hiding B/C/D merely to stay lazy or thin. Stop at the current frontier only when B/C/D existence, scope, or dependency still depends on future execution Evidence from A; extend the Graph after Evidence makes the downstream work real. **Best-known complete is not research-complete**: do not expand inventory, prove candidate implementations, scan territory that can only change How, or invent placeholder nodes/phases/taxonomy merely to complete the Graph.

Taskbook prose order does not create dependency. Work without a real dependency remains independent rather than being forced serial or parallel; one blocked branch does not freeze unrelated work; cohesive work is not fragmented merely to expose parallelism. A simple or linear task is only a degenerate Graph and does not require a diagram, Graph schema, or explicit node object.

## Scope, dependencies, and replacement completion

Define scope through a discriminator / authority / territory / exclusions that a fresh Executor can recompute from current reality rather than freezing the file/caller/line inventory captured during Research. Retain a concrete inventory only when authority binds the set itself, or reality cannot reproduce it reliably and omission would be material; then preserve the source identity needed to judge authority, provenance, and freshness. Inventories and session-local artifacts remain navigation / candidate Evidence and do not prove completion.

An Evidence condition becomes a dependency only when its absence makes downstream material work invalid, crosses a binding boundary, prevents safe start, or makes the outcome unjudgeable. Ordinary ordering or “check first to be safe” does not create a gate.

When Goal replaces a live path, authority, data flow, or workload, retain only the contract-required real transition/adoption and exit of legacy authority/residue that are material to the whole Goal. Code landing, local green, or a new path being available does not prove those outcomes. Replaceable migration How stays with the Executor; long-lived boundary/dependency forks route to `$architecture-evolution`; investment, compatibility, or risk commitments return to the Human.

## Independently judgeable slices

Slicing is not translating Goal into more tasks. It finds boundaries at which a **material outcome can be established or falsified independently**. Judge a slice by its judgment surface rather than file count, team ownership, or apparent parallelism:

- when two proposed slices can only be judged after both are complete and they have no independent responsibility / binding / outcome, merge them into one cohesive cut;
- when one slice hides several material outcomes, responsibilities, or binding boundaries that can succeed or fail independently, and those differences change Executor choice or later dependency judgment, split it;
- when several independently failing compatibility / behavior / real-exit claims only prove one cohesive responsibility outcome, keep one Execution cut and preserve separate judgment surfaces in Verification. An independently falsifiable claim does not automatically create an independent Execution cut;
- independent judgment does not require `one cut → one test`. A completion claim may span multiple cuts, and one cut may require several Evidence sources; Verification remains organized by Goal-level claims;
- preserve only enough relationship for a fresh Executor / judge to know why the cut is material to Goal, what it depends on, and what Evidence can establish or falsify the relevant claim. This may be written directly in prose; it does not create an Evidence Graph schema, ledger, or second contract.

This keeps a local error closer to its responsibility / outcome boundary instead of letting an unreviewed decision silently contaminate later Graph work. It does not require the implementation to become an opaque black box, and it does not prevent the judge from reading code when code is needed as current-reality Evidence.

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

Prompt Atlas does not own cross-session progress, retry, debugging, or the runtime scheduler, but the Taskbook must evolve cleanly through the host execution loop: `Graph → Executor outcome / Evidence → Taskbook + current reality judgment → verified Evidence / new reality → affected Graph`.

Executor reports, task checklists, and test output are candidate Evidence / navigation until independently verified; they cannot directly change reality or the Graph. Only verified new Evidence / reality recomputes the dependency cone it actually affects. Extend the Graph when it makes contingent work real; remove a branch / dependency when Evidence proves it absent; split, merge, or reorder remaining work when scope, binding, or material relations change; and recompute corresponding Verification when completion claims / coverage are affected. Unrelated branches, still-valid work, and Evidence remain valid. Completed work does not reopen mechanically merely because the Graph changes, unless its Evidence premise or proven behavior was affected.

The Graph is the structure of Execution inside the Taskbook, not another runtime object. Do not add persistent Graph state, node taxonomy, a scheduler, manager protocol, or a second Taskbook merely to use Graph / Loop. Reuse host progress/state when it already exists; Prompt Atlas does not invent one when it does not.
