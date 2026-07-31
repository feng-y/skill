# Prompt Atlas × Leader paired behavioral EVA v1

## Status

**NOT RUN**

This directory defines the minimum current-head paired execution needed before claiming that Prompt Atlas meets or exceeds Leader's behavioral capability floor. Static mechanism mapping or compiler smoke cannot close this gate.

## Preregistered fixtures

The exact synthetic repositories, task inputs, protected surfaces, forced events, budgets, and public oracle manifests are frozen in [`FIXTURES.md`](FIXTURES.md).

- F1 — false-green discount normalization
- F2 — behavior-preserving parser migration
- F3 — branch-local blocker with independent safe work
- F4 — forced cross-context migration

Do not replace these tasks with later-selected examples. Any fixture correction creates a new fixture version and invalidates earlier runs for that fixture.

## Fixture infrastructure self-check

Before freezing an EVA run, execute:

```bash
python evals/prompt-atlas-leader-paired-v1/validate-fixtures.py
```

The self-check must PASS before either arm starts. It verifies:

- every repository generator executes and creates a committed Git repository;
- every public oracle-manifest hash matches its registered text;
- public commands return the preregistered initial result;
- Python bytecode and pytest caches do not dirty the worktree;
- the private verifier required by F3 remains unavailable.

Fixture generators include only Python-cache ignore rules. They do not ignore `.scratch`, so F4 can still detect accidentally committed or hidden continuity state.

## Compared snapshots

Freeze before execution:

- Prompt Atlas repository commit, `SKILL.md`, references, and public agent prompt blobs;
- Leader repository commit, `SKILL.md`, and reference blobs;
- fixture file blob and generated task-repository initial commit;
- executor model/version, tool permissions, token/time budget, and runtime configuration;
- base environment image hash with Bash, Git, Python 3, pytest, and ripgrep versions;
- private oracle implementation SHA-256 matching the registered public manifest.

Do not use moving `main` references in final evidence.

## Visibility boundary

The evaluator/controller may read `PLAN.md`, `FIXTURES.md`, fixture specifications, public oracle manifests, and private oracle implementations.

Compiler/taskbook and executor sessions receive only:

- the exact fixture task input;
- the generated task repository and allowed runtime tools;
- for a resumed F4 executor, the original carrier/taskbook, current task worktree/history, and runtime-created continuity artifacts.

Do not mount or expose this evaluation repository, fixture specification files, public oracle manifests, private cases, private oracle implementation, another arm's artifacts, or evaluator notes to compilers or executors. The public manifest is public for preregistration and auditability, not part of the executor-visible contract.

## Isolation

For every fixture run two independent chains:

```text
A. Prompt Atlas snapshot → isolated compiler session → carrier → clean executor session
B. Leader snapshot       → isolated taskbook session → taskbook → clean executor session
```

Requirements:

- byte-identical generated starting repository for A and B;
- same base environment image, executor model, and runtime configuration;
- same tool permissions and external dependency availability;
- same token/time/attempt budget;
- no output sharing between A and B;
- compiler/taskbook author sessions isolated from executor sessions;
- accepting oracle isolated from both executors;
- each run retained with compiler artifact, actions, evidence, final state, and cost.

Run order must be randomized or counterbalanced and recorded before the first arm starts. Environment warming must not favor one arm.

## Forced-event handling

- F3 must run without `private-tax-verifier` or an equivalent dataset in both arms.
- F4 must enforce the clean-context restart at the preregistered point. The resumed executor receives only the original carrier/taskbook, current worktree/history, and runtime-created continuity artifacts—not prior chat or action transcript.

A run that does not apply its forced event is invalid rather than a partial result.

## Primary metrics

For each arm record:

- complete-Goal result under the same private oracle;
- intent drift;
- confirmed-boundary violation;
- false-green or fabricated evidence;
- Human interventions after initial authorization;
- repair/replan rounds;
- branch-local blocker handling and independent safe progress;
- context-resume correctness;
- truthful residual/blocker reporting;
- token usage, elapsed time, and tool actions;
- final `PASS`, `RETRY`, `BLOCK`, or `ESCALATE` under the accepting boundary.

## Capability-floor decision

Prompt Atlas may claim the covered Leader behavioral floor only when:

1. it has no additional complete-Goal failure on the registered fixtures;
2. it has no additional intent or confirmed-boundary violation;
3. it has no additional false-green acceptance;
4. it preserves at least equivalent blocker truthfulness and resume correctness;
5. reduced fixed structure does not create additional Human intervention or lost safe progress;
6. the claim is limited to the registered fixture versions and exact snapshots.

Token/time efficiency is secondary to correctness and trust. A cheaper run that fails the oracle does not satisfy the floor.

## Result schema

Create `RESULTS.md` only after all valid runs exist. It must contain:

- exact snapshot, fixture, generated-repository, environment-image, and private-oracle hashes;
- fixture self-check output and tool versions;
- model/tool versions and arm order/randomization seed;
- one row per arm with links to retained artifacts;
- primary metrics and oracle verdict;
- invalid runs and reasons;
- disagreements and residuals;
- capability-floor verdict: `PASS`, `PASS WITH RESIDUALS`, or `FAIL`;
- explicit claim boundary.

Until then, repository-facing wording remains:

```text
Leader mechanism/semantic coverage: reviewed
Current-head behavioral parity: NOT RUN
```
