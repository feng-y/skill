# Autonomous Taskbook

Use only after Stable Intent. Produce one authoritative taskbook an Executor can run without ordinary Human orchestration.

Render the final taskbook in the exact order below. Keep each section's authority and evidence role distinct; vary detail with the work, but do not merge, reorder, or hide required content in another section.

Compile only information that constrains a future decision, execution step, recovery action, or complete-Goal proof. Keep large supporting material by reference; state global facts once and Task-local differences only; omit superseded discussion and inactive detail.

For research, selection, or decision work, use the same fixed sections. In Execution, use evidence-producing investigations or decisions instead of implementation Tasks. Each conclusion needs a source/date or reproducible probe; fabricated citations, unrun “measurements”, and filler findings are failure. A well-evidenced dead end may satisfy a bounded learning Goal. Stop at the stated budget and deliver the best-supported conclusion plus counterevidence and unresolved alternatives; do not add another output section.

## Contract Header

State six things briefly:

- this taskbook is the execution source;
- the one Human-owned Goal;
- Why and the completed world;
- the declared delivery this taskbook closes;
- priority order when requirements conflict;
- hard rules versus guidance.

## 1. Delegated Decisions

Place compiler-owned defaults here, before boundaries and execution, so the Human can inspect and correct them before Handoff.

For each unconfirmed reversible choice that preserves Stable Intent: decision → default → basis → cost if wrong → detection or rollback. Defaults may close an execution branch; they may not change the Goal, confirmed boundaries, acceptance requirements, or Human authority.

If no such choice remains, state `None`; do not invent a decision to fill the section.

## 2. Boundaries and Authority

Use an allowed write-scope whitelist. When file scope is insufficient, also bound dependency changes, permissions, external-system writes, destructive actions, and other irreversible side effects. Name protected tests, schemas, acceptance scripts, CI, baselines, and other judges. Call out tempting side work and irreversible actions.

State what the Executor may decide or adapt inside Stable Intent and protected proof. State the route when work would exceed that authority: record a blocker pending explicit Human authority for a high-risk or irreversible action, return to Intent Take when the Goal or a confirmed boundary would change, or block when no safe work remains.

## 3. Current Reality and Task 0

Record evidenced facts and baselines; mark unverified claims.

Here, the implementation note means the repository or runtime's existing implementation record, or its normal equivalent; Prompt Atlas does not require a new filename or artifact.

Task 0 runs before material change. It binds repo/worktree/target, verifies critical commands and judges, detects no-op checks, and emits a short opening receipt: the understood Goal, initial route or order when material, largest current risk, and any disagreement between the taskbook, execution reality, or Executor understanding. If its findings or receipt change execution, record the evidence and resulting route in the implementation note. If reality or understanding differs:

- correct a clear taskbook misunderstanding and continue without Human input;
- replan when Goal and boundaries hold;
- park only the affected branch while safe work remains;
- block with the exact resolving condition when no safe work remains;
- return to Intent Take when Goal or a confirmed boundary would change.

Reuse evidence whose basis remains valid; do not repeat discovery ceremonially.

## 4. Execution

Order Tasks by real dependency. Each Task states:

- observable result and starting point;
- dependencies and write ownership;
- hard constraints;
- verification command or evidence procedure;
- machine-judgable PASS condition;
- reverse validation when failure could be silent;
- evidence invalidated by upstream change.

Keep simple work linear. When real branches, dependencies, shared writes, or a join would be hidden by a linear list, read [execution-graph.md](execution-graph.md) and compile the minimum dependency structure into ordinary Tasks.

## 5. Execution Rules and Continuity

- use one implementation note for material decisions, evidence-changing deviations, replans, and blockers; avoid routine progress narration and separate progress or blocker files;
- after any interruption, session change, or Executor handoff, read this taskbook and any existing implementation note before acting; recover still-valid decisions, evidence, blockers, and remaining work, and do not repeat discovery or completed work unless an upstream change or new evidence invalidated what it proved;
- when blocked, record the blocker, relevant evidence or attempts, the resolving condition, and any safe remaining work;
- do not skip tests, weaken assertions, narrow the judged population, mock away the object, swallow failures, edit the judge, or accept a lower baseline unless Stable Intent requires it;
- every retry changes the hypothesis or approach; stop known-bad routes immediately; three failures against one acceptance condition in one route force replan, branch switch, rollback, `BLOCK`, or `ESCALATE`;
- roll back unauthorized regression and report failure truthfully;
- follow repository branch, PR, and pre-submit rules.

The Executor may adapt remaining work inside Stable Intent and protected proof; record material replans in the implementation note.

## 6. Completion and Acceptance

Require complete-Goal evidence, boundary and judge preservation, actual command output or reproducible proof, truthful residuals or blockers, and a stop budget or truthful blocker. Local Task PASS is not complete-Goal PASS. Bind independent acceptance when required. If that required Acceptor or accepting environment is unavailable, cap the result at `ready for independent acceptance`; otherwise judge completion from the applicable visible and reserved acceptance.

Do not expose reserved private checks in the taskbook. State visible acceptance and any required independent accepting boundary; private check contents remain outside the taskbook and follow the lifecycle in [completion-trust.md](completion-trust.md).

The final report states `PASS`, `ready for independent acceptance`, or the exact non-PASS route; the delivered result; the evidence that supports the judgment; exact residuals or blockers; and the next legitimate route. Do not replace evidence with activity narration.

Before Handoff, verify one Goal and one declared delivery; at least one Task or required Task 0 can start immediately; every dependency is grounded; each shared mutable surface has one owner; authority-sensitive operations are bounded; every branch rejoins or has an explicit terminal route; and complete-Goal proof remains possible. Do not compile scheduler, lease, or fixed Agent topology.

One taskbook must close the declared delivery in one execution effort. One execution effort means one authoritative taskbook and one closed delivery, not one Agent, one session, or one linear run. The Executor may resume sessions, delegate, parallelize, or use a dependency graph when useful while preserving one Goal, clear write ownership, and complete-Goal acceptance. If the delivery cannot close under that contract, return to Intent Take to narrow the Human-owned delivery; do not split the Goal into multiple taskbooks.
