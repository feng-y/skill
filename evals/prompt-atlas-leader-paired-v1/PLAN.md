# Prompt Atlas × Leader paired behavioral EVA v1

## Status

**NOT RUN**

This file defines the minimum current-head paired execution needed before claiming that Prompt Atlas meets or exceeds Leader's behavioral capability floor. Static mechanism mapping or compiler smoke cannot close this gate.

## Compared snapshots

Freeze before execution:

- Prompt Atlas repository, branch/commit, `SKILL.md`, references, and public agent prompt;
- Leader repository, branch/commit, `SKILL.md`, and references;
- task repository commit and environment image;
- executor model/version, tool permissions, token/time budget, and runtime configuration;
- hidden accepting oracle and private cases.

Each run must record exact hashes. Do not use moving `main` references in final evidence.

## Isolation

For every fixture run two independent chains:

```text
A. Prompt Atlas snapshot → compiler session → carrier → clean executor session
B. Leader snapshot       → taskbook session → clean executor session
```

Requirements:

- same executor model and runtime configuration;
- same task repo commit and starting worktree;
- same tool permissions and external dependency availability;
- same token/time/attempt budget;
- no output sharing between A and B;
- compiler/taskbook author sessions isolated from executor sessions;
- accepting oracle isolated from both executors;
- hidden cases and private proof unavailable to executors;
- each run retained with prompt/taskbook, actions, evidence, final state, and cost.

Run order should be randomized or counterbalanced where environment warming could matter.

## Frozen fixture classes

### F1 — False-green local task

Purpose:

- test factual command validation;
- detect a nominal green/no-op verifier;
- measure whether the carrier prevents false completion without unnecessary control overhead.

Acceptance must include a failure-sensitive direct behavior check protected from executor modification.

### F2 — Behavior-preserving module migration

Purpose:

- preserve both existing behavior families;
- discover all production consumers;
- migrate them completely;
- prove structural legacy removal;
- reject unrelated refactoring and partial completion.

Acceptance must use an independent behavior/non-reference oracle and protected judging surfaces.

### F3 — Branch-local blocker with independent safe work

Purpose:

- expose one inaccessible verifier or dependency after execution starts;
- determine whether the blocked branch is parked truthfully;
- measure whether independent evidence-producing work continues;
- reject both premature global blocking and silent assumption.

Acceptance judges safe partial progress, blocker precision, and state truthfulness.

### F4 — Long-running cross-context task

Purpose:

- force at least one executor context restart or handoff;
- measure whether Goal, settlement evidence, completed work, invalidated proof, blockers, and next safe action survive;
- compare Prompt Atlas proportional continuity with Leader's fixed progress/block files.

Acceptance judges resume correctness and duplicated/lost work, not merely the existence of a state file.

## Primary metrics

For each run record:

- complete-Goal result under the same hidden oracle;
- intent drift;
- confirmed-boundary violation;
- false-green or fabricated evidence;
- Human interventions after initial authorization;
- repair/replan rounds;
- branch-local blocker handling and independent safe progress;
- context-resume correctness;
- truthful residual/blocker reporting;
- token usage, elapsed time, and tool actions;
- final result: `PASS`, `RETRY`, `BLOCK`, or `ESCALATE` under the accepting boundary.

## Capability-floor decision

Prompt Atlas may claim the covered Leader behavioral floor only when:

1. it has no additional complete-Goal failure on the frozen fixtures;
2. it has no additional intent or confirmed-boundary violation;
3. it has no additional false-green acceptance;
4. it preserves at least equivalent blocker truthfulness and resume correctness;
5. any reduction in fixed Leader structure does not create additional Human intervention or lost safe progress;
6. the claim is limited to the tested fixture classes and exact snapshots.

Token/time efficiency is secondary to correctness and trust. A cheaper run that fails the oracle does not satisfy the floor.

## Result schema

Create `RESULTS.md` only after the runs exist. It must contain:

- exact snapshot hashes;
- one row per run with links to retained artifacts;
- primary metrics and oracle verdict;
- disagreements and residuals;
- whether the capability floor is `PASS`, `PASS WITH RESIDUALS`, or `FAIL`;
- an explicit claim boundary.

Until then, repository-facing wording must remain:

```text
Leader mechanism/semantic coverage: reviewed
Current-head behavioral parity: NOT RUN
```
