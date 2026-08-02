# Autonomous Taskbook

Use only after Stable Intent. Produce one compact taskbook an Executor can run without ordinary Human orchestration.

## Opening

State four things briefly:

- this taskbook is the execution source;
- Why and the completed world;
- priority order when requirements conflict;
- hard rules versus guidance.

## 1. Delegated decisions

For each unconfirmed choice: question → default → basis → cost if wrong → detection or rollback. Defaults may close orchestration, never change Stable Intent.

## 2. Boundaries

Use an allowed write-scope whitelist. Name protected tests, schemas, acceptance scripts, CI, baselines, and other judges. Call out tempting side work and irreversible actions.

## 3. Current state and Task 0

Record evidenced facts and baselines; mark unverified claims.

Here, the implementation note means the repository or runtime's existing implementation record, or its normal equivalent; Prompt Atlas does not require a new filename or artifact.

Task 0 runs before material change. It binds repo/worktree/target, verifies critical commands and judges, and detects no-op checks. If its findings change execution, record the evidence and resulting route in the implementation note. If reality differs:

- replan when Goal and boundaries hold;
- park only the affected branch while safe work remains;
- block with the exact resolving condition when no safe work remains;
- return to Intent Take when Goal or a confirmed boundary would change.

Reuse evidence whose basis remains valid; do not repeat discovery ceremonially.

## 4. Task N

Order by real dependency. Each task states:

- observable result and starting point;
- dependencies and write ownership;
- hard constraints;
- verification command or evidence procedure;
- machine-judgable PASS condition;
- reverse validation when failure could be silent;
- evidence invalidated by upstream change.

Keep simple work linear. Expand a graph only for real branches, dependencies, shared writes, joins, or evidence invalidation. Give every shared mutable surface one owner.

## 5. Rules

- use one implementation note for material decisions, evidence-changing deviations, replans, and blockers; avoid routine progress narration and separate progress or blocker files;
- after any interruption, session change, or Executor handoff, read this taskbook and any existing implementation note before acting; recover still-valid decisions, evidence, blockers, and remaining work, and do not repeat discovery or completed work unless an upstream change or new evidence invalidated what it proved;
- when blocked, record the blocker, relevant evidence or attempts, the resolving condition, and any safe remaining work;
- do not skip tests, weaken assertions, narrow the judged population, mock away the object, swallow failures, edit the judge, or accept a lower baseline unless Stable Intent requires it;
- every retry changes the hypothesis or approach; stop known-bad routes immediately; three failures against one acceptance condition in one route force replan, branch switch, rollback, `BLOCK`, or `ESCALATE`;
- roll back unauthorized regression and report failure truthfully;
- follow repository branch, PR, and pre-submit rules.

The Executor may adapt remaining work inside Stable Intent and protected proof; record material replans in the implementation note.

## 6. Completion conditions

Require complete-Goal evidence, boundary and judge preservation, actual command output or reproducible proof, truthful residuals or blockers, and a stop budget or truthful blocker. Local task PASS is not complete-Goal PASS. Bind independent acceptance when required; otherwise cap at `ready for independent acceptance`.

One taskbook must close the declared delivery in one execution effort. One execution effort means one authoritative taskbook and one closed delivery, not one Agent, one session, or one linear run. The Executor may resume sessions, delegate, parallelize, or use a dependency graph when useful while preserving one Goal, clear write ownership, and complete-Goal acceptance. If the delivery cannot close under that contract, return to Intent Take to narrow the Human-owned delivery; do not split the Goal into multiple taskbooks.

## Research and decision work

Use the same structure with a bounded learning goal. Each conclusion needs a source/date or reproducible probe; fabricated citations, unrun “measurements”, and filler findings are failure. A well-evidenced dead end may be valid. Stop at the stated budget and deliver the best-supported conclusion plus unresolved alternatives.
