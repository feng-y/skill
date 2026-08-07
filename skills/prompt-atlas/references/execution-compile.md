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
