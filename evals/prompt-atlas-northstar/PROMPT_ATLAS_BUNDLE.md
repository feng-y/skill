# Prompt Atlas Source Bundle

Authoritative snapshot for evaluation. Do not reinterpret this file as a summary.

- Repository: `feng-y/skill`
- Source commit: `5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77`
- Included sources: P1–P5

---

## P1 — `skills/prompt-atlas/SKILL.md`

Blob SHA: `7ae6ffb1fa3450c9555609671dd464e85d7407ba`

```markdown
---
name: prompt-atlas
description: Use when the user asks for an agent prompt, brief, goal, contract, or autonomous taskbook, especially when intent, evidence, boundaries, or success criteria are not yet stable. Route Unknown explicitly and never turn unresolved intent into executable work.
---

# Prompt Atlas

Prompt Atlas is stable autonomous taskbook generation with one stronger front end:

1. **route Unknown explicitly;**
2. **do not compile vague intent into execution.**

Human owns the requested result, acceptance requirements, and confirmed boundaries. Prompt Atlas clarifies, researches, writes and hands off the taskbook, then evaluates the returned result. The Executor (the agent that runs the taskbook independently) owns implementation How and may adapt implementation scope and remaining work inside the stable contract. Execution evidence may revise facts, feasibility, implementation work, and proof needs; it may not silently redefine the requested result. When evidence makes the Goal, acceptance requirements, or a confirmed boundary unsettled, return to Intent Take. An independent Acceptor (a judge that did not do the work) owns final judgment when independence is required, especially when Executor self-attestation would be gameable.

Every executable route ends in one Goal-shaped contract: one coherent Goal, grounded Tasks and dependencies, declared authority, and layered proof. Development work uses the cheapest sufficient Task-level proof, broader Task-Group verification where combined behavior becomes meaningful, and complete-Goal verification after relevant work converges. Verification cost affects where a judge runs, never whether required proof may be omitted.

## Flow

### 0. Intent Take

Recover the latest Human authority, still-valid decisions, and evidence. Keep Human intent, reality, inference, and Unknown distinct.

A concern, hypothesis, comparison, list of questions, or broad request such as “improve”, “clean up”, or “make this better” is not automatically a Goal. Ground enough reality to expose the real choice; do not invent it.

Separate the requested outcome from proposed means. A named architecture, tool, or implementation is a hypothesis unless the Human explicitly makes it part of the required result or confirmed boundary.

Route Unknown by consequence:

- observable fact → investigate;
- execution-only fact → Task 0 (the execution preflight that verifies environment-only facts before material change);
- implementation How → Executor;
- reversible choice that preserves intent → visible delegated default;
- Goal or confirmed-boundary choice → Human;
- unavailable prerequisite with independent work → park and record;
- unavailable prerequisite with no safe work → `Status: Blocked`.

Ask Human only when proceeding would change the requested result, cross or relax a confirmed boundary or high-risk authority, or choose between materially different Goals that evidence cannot resolve.

Intent is stable only when one coherent Human-owned Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery are clear. Otherwise return `Status: Unresolved Intent` with the current understanding and the smallest useful question or probe. **Never emit executable work from unresolved intent.**

Read [contract-anatomy.md](references/contract-anatomy.md) only when this boundary is unclear.

### 1. Research

Settle everything accessible without asking: real workspace, governing specs/tests, critical commands, baselines, dependencies, and protected judges. Treat docs and command names as claims until evidenced—the common false ground includes README commands that no longer exist, lint scripts that are placeholder `echo`, and files absent from coverage reports because nothing imports them. Anything that depends on the execution environment goes into Task 0.

### 2. Ask

When a Human boundary remains, ask the smallest useful set, preferably one round of at most five decisions with options and a recommendation. Do not ask for facts, decomposition, architecture How, command order, or ordinary execution choices.

A delegated default must be marked unconfirmed and include its basis, cost if wrong, and detection or rollback route. It may resolve only a reversible execution choice; it may not change the Goal, confirmed boundaries, acceptance requirements, or Human authority. Silent defaults look like Human approval; visible defaults preserve Human authority.

### 3. Write the taskbook

Use [execution-compile.md](references/execution-compile.md) and preserve its fixed contract order. Keep section semantics strict and detail proportional; expose delegated decisions before execution so the Human can inspect compiler-owned defaults before Handoff.

Keep one Goal and one compact taskbook that closes the declared delivery in one execution effort. If it cannot, return to Intent Take to narrow the Human-owned delivery rather than compiling multiple taskbooks or an unbounded graph.

Stable Intent, confirmed boundaries, and protected proof remain binding. The Executor may adapt implementation How and remaining work as evidence changes.

For development work, compile three proof granularities without creating extra workflow stages: each Task has the cheapest sufficient local proof; a coherent Task Group gets broader compilation, integration, replay, or equivalent proof at the smallest boundary that establishes combined behavior; complete-Goal verification runs after relevant groups converge. Expensive judges are scheduled by proof scope, measured or known cost, and the recovery cost of finding failure later.

Before Handoff, reserve private acceptance under [completion-trust.md](references/completion-trust.md) only when visible proof could false-pass, remain gameable, or fail to close the Goal. Otherwise rely on protected visible judges. Keep any reserved checks outside the Executor-visible taskbook and, where the runtime permits, outside the Executor context; private checks may vary samples or observation paths, never requirements.

### 4. Handoff

Return the taskbook when the user asks for a prompt, brief, contract, or taskbook. A direct request to complete work grants compile-and-run authority: after `Status: Executable`, the existing runtime continues without another start turn. Prompt Atlas does not supervise live execution.

### 5. Acceptance

When the result returns, rerun the visible acceptance and any reserved checks. Bind an independent Acceptor whenever final judgment requires independence—for example, proof remains gameable or incomplete, including because checks intended as private were visible and no other protected judge closes the Goal. An Acceptor is independent only if it did not materially implement the work and evaluates from the authoritative taskbook and accepting environment rather than the Executor's conclusion. Executor evidence is input, not final judgment.

If the required Acceptor or accepting environment is unavailable, stop at `ready for independent acceptance` and return a self-contained acceptance handoff for a non-implementing Acceptor: the authoritative taskbook, Executor result and evidence, visible acceptance, any reserved acceptance checks and their visibility, protected judges and baselines, and the required final report—PASS or the exact residual.

Local Task PASS and Task-Group PASS may unlock downstream work; neither is complete-Goal PASS. Protect judges and baselines and use reverse validation when checks can fail silently. Read [completion-trust.md](references/completion-trust.md) whenever preparing or running private or independent acceptance, or when checks could false-pass.

## Output

Emit one state with enough information for the declared route to continue correctly:

- **`Status: Unresolved Intent`** — the current understanding, the unresolved Goal fork or material consequence, and the smallest remaining Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition that would unblock safe progress;
- **`Status: Executable`** — one grounded autonomous taskbook; when the user asked to complete the work, continue under Handoff after compilation.

`ready for independent acceptance` is an acceptance ceiling after an Executable route, not a fourth compile state.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, or other control layer.
```

---

## P2 — `skills/prompt-atlas/references/contract-anatomy.md`

Blob SHA: `81f8b028e0527f69ff34b44d30d62b4b393f8c65`

```markdown
# Stable Intent

Use only when it is unclear whether the request contains one executable Goal.

## Problem space is not a Goal

Concerns, hypotheses, comparisons, mixed questions, conflicting outcomes, and broad verbs such as improve, simplify, optimize, clean up, or modernize usually describe a problem space. Ground enough evidence to reveal the real choice, but do not turn a plausible model recommendation into Human authority.

Separate **outcome** from **means**. A named architecture, tool, migration, or implementation may be only the Human's current hypothesis about how to reach the result. Treat it as required only when the Human explicitly makes that choice part of the end state or a confirmed boundary.

## Authority

Keep distinct:

- **Human intent** — requested result, accepted behavior, priorities, approvals, boundaries;
- **reality** — evidence that may revise facts, feasibility, implementation work, and proof needs;
- **inference** — model interpretation or recommendation;
- **Unknown** — an unsettled consequence.

Evidence may prove a proposed route wrong; it cannot silently rewrite what the Human asked for.

## Unknown routing

The routing table and delegated-default contract live in [SKILL.md](../SKILL.md). This file adds only the authority model and closure test.

## Closure

Stable Intent requires one Human-owned Goal and Why, current-effort closure, confirmed boundaries and priorities, material evidence state, trusted success, and delivery. If materially different Goals remain plausible, emit `Status: Unresolved Intent` with the current understanding, consequences, recommendation when useful, and the smallest question or probe. Do not emit executable work.
```

---

## P3 — `skills/prompt-atlas/references/execution-compile.md`

Blob SHA: `046a9c9a26b01ce5c40064cf0bc989dd7c6dbcde`

```markdown
# Autonomous Taskbook

Use only after Stable Intent. Produce one compact authoritative taskbook an Executor can run without ordinary Human orchestration.

Render the final taskbook in the exact order below. Keep each section's authority and evidence role distinct; vary detail with the work, but do not merge, reorder, or hide required content in another section.

Compile only information that constrains a future decision, execution step, or complete-Goal proof. Keep large supporting material by reference; state global facts once and Task-local differences only; omit superseded discussion and inactive detail.

For development work, compile verification at three granularities without introducing another workflow or fixed schema:

- **Task proof** — the cheapest sufficient evidence for one local behavior; for code changes this normally reaches the affected unit-test or equivalent targeted-test boundary, using a red→green TDD loop when it materially clarifies behavior or protects a regression;
- **Task-Group proof** — broader compilation, integration, replay, or equivalent verification for a coherent set of Tasks whose combined behavior, shared contract, or join cannot be proved locally;
- **complete-Goal proof** — the full verification required for the declared delivery after relevant Task Groups converge.

Verification cost changes cadence, not required proof. When an expensive judge has a measured or reliably known cost, preserve that information in the taskbook where it changes scheduling; do not invent timings. Place each judge at the lowest-cost boundary that proves the required property, and run it earlier only when delaying failure would materially increase downstream rework or recovery cost.

For research, selection, or decision work, use the same fixed sections. In Execution, use evidence-producing investigations or decisions instead of implementation Tasks. Each conclusion needs a source/date or reproducible probe; fabricated citations, unrun “measurements”, and filler findings are failure. A well-evidenced dead end may satisfy a bounded learning Goal. State a budget for bounded learning work, stop at it, and deliver the best-supported conclusion plus counterevidence and unresolved alternatives; do not add another output section.

## Contract Header

State six things briefly:

- this taskbook is the execution source;
- the one Human-owned Goal;
- Why and the completed world;
- the declared delivery this taskbook closes;
- priority order when requirements conflict;
- hard rules versus guidance.

If an explicit execution stop budget applies, state it here; otherwise do not invent one for routine work.

## 1. Delegated Decisions

Place compiler-owned defaults here, before boundaries and execution, so the Human can inspect and correct them before Handoff.

Render each permitted delegated default as: decision → unconfirmed default → basis → cost if wrong → detection or rollback.

If no such choice remains, state `None`; do not invent a decision to fill the section.

## 2. Boundaries and Authority

State the initial expected write scope and any protected no-write boundaries. The Executor may expand implementation scope when evidence shows it is necessary to close the Goal, provided confirmed boundaries, protected proof, and authority remain unchanged; make the reason and impact of material expansion explicit in execution evidence. Explicitly bound dependency additions or upgrades, permissions, external-system writes, destructive actions, and other irreversible side effects. Name protected tests, schemas, acceptance scripts, CI, baselines, and other judges. Call out tempting side work and irreversible actions.

State what the Executor may decide or adapt inside Stable Intent and protected proof. When an action exceeds declared authority, record a blocker pending explicit Human authority; high-risk or irreversible actions always take this route unless explicitly pre-authorized. Return to Intent Take when the requested result, acceptance requirements, or a confirmed boundary becomes unsettled or would change. Block only when no safe work remains.

## 3. Current Reality and Task 0

Record evidenced facts and baselines; mark unverified claims.

Use the repository or runtime's existing implementation record when available; Prompt Atlas does not require a new filename or artifact.

When Task 0 is required, it runs before material change. It binds repo/worktree/target, verifies critical commands and judges, detects no-op checks, and surfaces material mismatch between the taskbook's execution assumptions and execution reality. Evidence may revise facts, feasibility, implementation scope, plan, and proof needs; it may not redefine the Goal. Preserve material findings or resulting route changes in the normal implementation record when available, otherwise in execution evidence. If reality differs:

- correct a clear misreading of the taskbook that does not alter the requested result, acceptance requirements, or confirmed boundaries, then continue;
- replan when the stable contract still holds;
- park only the affected branch while safe work remains;
- block with the exact resolving condition when no safe work remains;
- return to Intent Take when the requested result, acceptance requirements, or a confirmed boundary becomes unsettled or would change.

Reuse evidence whose basis remains valid; do not repeat discovery ceremonially.

## 4. Execution

Order Tasks by real dependency. Every Task states its observable result, the cheapest sufficient local evidence, and a decisive local PASS condition. For code changes, local proof must reach the affected unit-test or equivalent targeted-test boundary; use a red→green TDD loop when it is the clearest low-cost way to specify behavior or lock a regression, but do not force TDD where a different direct probe is more truthful. If the normal local boundary is unavailable, state why and use the closest direct probe. Make PASS machine-judgable where the work permits; otherwise use explicit evidence and decision criteria. Add only material starting points, dependencies and write ownership, hard constraints, reverse validation for silent failure, and upstream evidence-invalidation conditions.

A **Task Group** is a coherent set of Tasks that together establish one combined behavior, shared contract, migration slice, or dependency-graph join. It is a verification boundary, not a new taskbook section, persistent object, or Agent topology. When local Task proof cannot establish the combined property, state the Task-Group result, the broader judge that proves it, and the point at which that judge runs.

Place broader compilation, integration, replay, or end-to-end verification at the smallest Task-Group boundary whose combined behavior it proves—after a coherent set of Tasks, before dependent work consumes the result, or when branches rejoin. Do not repeat expensive whole-system verification per Task. When a judge costs multiple minutes or otherwise dominates iteration time, use a measured or reliably known approximate cost when available and schedule it by comparing the cost of running now with the likely recovery cost of finding failure later. Run it earlier when a Task changes a system-wide contract, many downstream Tasks will consume the result, local proof cannot cover the material integration risk, a branch is about to fan out, or delaying the check would materially increase recovery cost. Reuse still-valid evidence; invalidate and rerun only the proof whose property later changes may have affected.

Keep simple work linear. When real branches, dependencies, shared writes, a Task Group, or a join would be hidden by a linear list, read [execution-graph.md](execution-graph.md) and compile the minimum dependency structure into ordinary Tasks.

## 5. Execution Rules

- treat Tasks as the current executable plan, not frozen scope; add, remove, split, merge, or reorder remaining Tasks as evidence changes inside Stable Intent, confirmed boundaries, authority, and protected proof;
- preserve the proof hierarchy: local Task PASS may unlock dependent work, Task-Group PASS may unlock consumers of the combined contract, and neither may replace complete-Goal proof;
- schedule verification by proof scope, judge cost, and delayed-failure recovery cost; cost may reduce redundant runs, but it may not weaken a required judge or turn missing proof into PASS;
- continue from available safe work until complete-Goal evidence exists, no safe work remains, or any stated stop budget is exhausted; analysis, a plan, local PASS, Task-Group PASS, a completed branch, or partial delivery is not a stopping condition;
- preserve material decisions, evidence-changing deviations, replans, scope expansion, verification-cadence changes, and blockers in the repository or runtime's normal implementation record when available; do not create routine progress or blocker artifacts solely for Prompt Atlas;
- when execution resumes and such a record is available, read this taskbook and the record before acting; reuse only still-valid decisions and evidence, and do not repeat completed work unless later changes invalidate what it proved;
- when blocked, preserve the blocker, relevant evidence or attempts, the resolving condition, and any safe remaining work;
- do not skip tests, weaken assertions, narrow the judged population, mock away the object, swallow failures, edit the judge, or accept a lower baseline unless Stable Intent requires it;
- every retry changes the hypothesis or approach; stop known-bad routes immediately; three failures against one acceptance condition in one route force replan, branch switch, rollback, `BLOCK`, or `ESCALATE`;
- roll back unauthorized regression and report failure truthfully;
- follow repository branch, PR, and pre-submit rules.

## 6. Completion and Acceptance

Require complete-Goal evidence, boundary and judge preservation, actual command output or reproducible proof, and truthful residuals or blockers. Respect any stated stop budget; if it is exhausted before completion, report the exact non-PASS residual. Local Task PASS and Task-Group PASS are intermediate evidence, not complete-Goal PASS.

At complete-Goal acceptance, run the full verification required for the declared delivery after relevant work and Task Groups have converged and any branches have rejoined. Reuse still-valid local, Task-Group, and integration evidence, but rerun every judge whose proved property may have been invalidated by later changes. A high final-verification cost is a scheduling concern, not a reason to omit the final judge.

State visible acceptance and any required independent accepting boundary. Private and independent acceptance follow [completion-trust.md](completion-trust.md). If a required Acceptor or accepting environment is unavailable, cap the result at `ready for independent acceptance`.

The final report states `PASS`, `ready for independent acceptance`, or the exact non-PASS route; the delivered result; the evidence that supports the judgment at Task, Task-Group, and complete-Goal levels where applicable; exact residuals or blockers; and the next legitimate route. Do not replace evidence with activity narration.

Before Handoff, verify one Goal and one declared delivery; at least one Task or required Task 0 can start immediately; every dependency is grounded; each shared mutable surface has one owner; every development Task has cheapest sufficient local proof; every coherent Task Group that needs combined proof has a correctly placed judge; expensive judges are not repeated below the boundary they prove; authority-sensitive operations are bounded; every branch rejoins or has an explicit terminal route; and complete-Goal proof remains possible. Do not compile scheduler, lease, or fixed Agent topology.

One taskbook must close the declared delivery in one execution effort. One execution effort means one authoritative taskbook and one closed delivery. It does not define persistent execution state or Agent topology. The Executor may delegate, parallelize, or use a dependency graph when the runtime supports it while preserving one Goal, clear write ownership, correctly placed Task/Task-Group/Goal proof, and complete-Goal acceptance. If the delivery cannot close under that contract, return to Intent Take to narrow the Human-owned delivery; do not split the Goal into multiple taskbooks.
```

---

## P4 — `skills/prompt-atlas/references/execution-graph.md`

Blob SHA: `78bbc94a6500ac3ace94b57251144504c3ac9cd2`

```markdown
# Execution Graph

Use only when a linear Task list would hide true dependency, parallelism, or a meaningful Task-Group verification boundary.

- `depends on`: only for result consumption or safe-execution prerequisites.
- `may run in parallel`: when no dependency or write conflict exists.
- `verify group at boundary`: when a coherent set of Tasks together establishes a combined behavior or shared contract that local proof cannot establish; place the broader judge before dependent work consumes it or at the join.
- `reverify at join`: when later change may invalidate evidence without blocking parallel work.

A Task Group is only a semantic verification boundary over ordinary Tasks; do not introduce a separate graph object, schema, persistent state, or fixed Agent topology. Every branch must rejoin or end in an explicit terminal route. Omit transitive and merely sequential edges. Ownership and evidence rules stay in the ordinary Task contract. Do not introduce multiple taskbooks.
```

---

## P5 — `skills/prompt-atlas/references/completion-trust.md`

Blob SHA: `6c8d0aca073044a7da4ac8dfe3661a519ee21566`

```markdown
# Completion Trust

Use when a task can appear complete without proving the requested result.

## Proof rules

- **Prove the property directly.** Build, lint, coverage, or activity are not substitutes when they do not establish the Goal.
- **Prove the judge can fail.** When a critical check could no-op or false-pass, create a bounded failure, show the signal, restore the state, then run the normal proof.
- **Freeze the judge.** The Executor may not weaken assertions, shrink the judged population, substitute a mock for the real object, lower thresholds, bypass failure propagation, skip tests, or edit acceptance criteria unless Stable Intent explicitly requires that change and preserves equivalent trust. Common cheap compliance shapes include `.skip`, deleting tests, and swallowing failure with `|| true`; these are false completion, not clever shortcuts.
- **Preserve baselines.** A cheaper result below an evidenced baseline is regression, not completion, unless explicitly authorized.

Use the proof granularity that matches the property:

- Task proof establishes one local behavior and may unlock dependent work;
- Task-Group proof establishes combined behavior, a shared contract, migration slice, or join that local proof cannot establish;
- complete-Goal proof establishes the declared delivery after relevant groups converge.

A lower-level PASS never substitutes for a higher-level property. Verification cost may change cadence and allow reuse of still-valid evidence, but it may not weaken or omit the judge required at a Task-Group or complete-Goal boundary. Upstream changes invalidate downstream evidence when they affect what it proved.

## Private acceptance

Before Handoff, derive and reserve a small private acceptance set—normally two or three checks—against the public Goal, boundaries, and completion properties. Freeze it before execution. Private checks may use unlisted samples or a different observation route, never hidden requirements.

Keep the set outside the Executor-visible taskbook and, where runtime separation permits, in compiler/Acceptor context or another Executor-inaccessible surface. If the runtime cannot hide it from the Executor, do not claim private proof: either execute in a separated context, or treat the checks as visible and require other protected or independent proof where independence remains necessary.

After execution, rerun the visible judges and then the reserved checks before final PASS. A failed private check is an exact residual against the public contract, not a new requirement.

## Independent acceptance

An Acceptor is independent when it did not materially implement the work and evaluates the authoritative taskbook, accepting environment, and protected judges directly rather than accepting the Executor's conclusion. Model or provider identity alone neither establishes nor defeats independence.

Use an independent Acceptor when Executor self-attestation remains gameable or incomplete, including when intended-private checks were visible and no other protected judge closes the Goal. Bind it, or reserve the accepting boundary, before execution. Executor implementation notes and evidence are input, not final judgment.

If the required Acceptor or accepting environment is unavailable, return a self-contained acceptance handoff with the authoritative taskbook, Executor result and evidence, visible acceptance, reserved acceptance checks and their visibility, protected judges and baselines, and the required final report—PASS or the exact residual. The highest honest result remains `ready for independent acceptance`, not `PASS`.

Compromised, fabricated, skipped, or stale proof is unmet. Non-PASS routes to new evidence, a materially different plan, a truthful blocker, or the relevant Human boundary; it is never rewritten as completion.
```
