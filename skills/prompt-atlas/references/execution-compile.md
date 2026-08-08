# Autonomous Taskbook

Use only after Goal is stable. Produce one compact authoritative taskbook that lets an Executor start safely and continue by judgment rather than by replaying a verbose plan.

The semantic ownership stays fixed:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

The physical taskbook is **sparse**. A section or clause exists only when it changes execution judgment. State each fact once under its semantic owner; later sections reference or consume it instead of restating it. Do not fill empty structure, summarize the same constraint per Task, or describe future work merely because it is imaginable.

The taskbook is a truthful starting contract, not a complete simulation of the future. Compile the **minimum currently justified executable structure**: enough to start, expose real dependencies, preserve authority, and make required Verification possible. Runtime Evidence may expand or revise the remaining work.

## Goal

Write one concise Human-owned Goal: the result that must become true, what must remain true, and the declared delivery. Add Why only when it changes a tradeoff or execution judgment.

Keep confirmed boundaries, authorization limits, protected side effects, or an unconfirmed delegated default here only when they materially constrain execution. Do not repeat them inside every Task. Human explicit verification requirements do **not** belong to Goal; preserve them under Verification.

Goal itself defines success. Do not add a Completion Contract, completion properties, Acceptance layer, or another done taxonomy.

## Execution / Graph

Execution contains only work current evidence justifies.

A Task is an **executable delta**, not a miniature prompt. Normally it needs only:

- the observable result;
- a non-obvious starting point or hard local constraint, only when needed;
- the cheapest sufficient local check, only once, when that check is needed to decide progression.

Do not copy Goal, global boundaries, shared reality, repo-wide rules, or Goal-level Verification into each Task.

Keep work linear when sequence is enough. Read [execution-graph.md](execution-graph.md) only when real dependency, parallelism, shared writes, a Task-Group boundary, or a join changes execution judgment. Graph expresses those relationships only; omit transitive edges and mere sequence.

Do not materialize speculative downstream Tasks or edges just to make the plan look complete. If current evidence justifies Task A but B/C/D depend on what A discovers, compile A and the known decision boundary; let Evidence determine B/C/D at runtime.

### Current reality and Task 0

Record only reality that changes execution or Verification. Keep supporting detail by source/reference rather than copying it into the taskbook.

Use **Task 0** only for a premise that is already known to matter at compile time but can be established only in the execution environment before material change—for example actual worktree/target binding, provider availability, effective config, or an execution-only Verification trigger. Task 0 is not a second research phase.

When Task 0 or later execution changes implementation reality, update only the remaining Execution / Graph and any affected Verification. Reuse completed work and Evidence whose premises remain valid.

### Runtime progression

Executor works the current ready frontier:

```text
ready work → execute / probe → Evidence → update remaining Graph → continue
```

A newly discovered fact is resolved inline when it changes the current execution judgment. If one branch is blocked but independent work is ready, continue it. A join waits only for real dependencies. Completed work is not reopened unless its Evidence premise or required combined Verification was invalidated.

Return to Human/Intent Take only when safe continuation requires changing Goal, a confirmed boundary, explicit Human verification authority, priority, or authorization. Otherwise adjust execution locally.

## Verification

Verification is written where it is first needed and not duplicated elsewhere.

- **Task-level** — attach the cheapest sufficient local check to the Task once when it controls progression.
- **Task-Group** — write one broader check at the smallest meaningful combined boundary or join when local checks cannot prove the combined behavior.
- **Goal-level** — state only the remaining delivery-level coverage obligations: explicit Human verification requirements plus repo-required Verification not already fully represented by lower-level checks.

Goal-level Verification is a final **coverage boundary**, not a mandatory extra final command. Reuse still-valid Task / Task-Group Evidence and run only required checks that remain uncovered or were invalidated.

Required Verification follows actual impact/reachability, repo verification authority, and explicit Human verification requirements. Trace changed owner/shared responsibility/system contract to effective binding/config and affected consumers/targets when that changes proof scope. Cleanup/refactor labels and expected `0-diff` never downgrade already-triggered Verification.

Concrete test/build/replay/static/symbol providers come from the repo verification system and prove only what they actually cover. Do not compile a fixed bundle. A documented provider is a claim until availability and failure propagation are evidenced; verify it before Handoff when possible, otherwise Task 0 owns that premise.

Read [verification-trust.md](verification-trust.md) only when normal protected repo Verification may false-pass, be gameable, fail silently, or genuinely needs independent Evidence.

## Evidence

The taskbook specifies what Evidence must be retained; it does not repeat the Verification plan as prose.

Evidence used for judgment must make the material claim reproducible: what provider/probe ran, against which target/revision and material binding/config, what verdict/exit occurred, and where raw output or a stable artifact/reference lives. Keep this proportional; do not attach ceremonial metadata that cannot change judgment.

Executor `done`, `PASS`, implementation narration, and second-hand summaries are inputs, not final Evidence. When the judging side can access the authoritative environment, reacquire final-judgment-critical repo-authoritative Evidence at reasonable cost rather than mechanically rerunning every local check. Missing, stale, under-covered, or judge-weakened Evidence is non-PASS.

The final report states only: delivered result, decisive Evidence, exact residual/blocker if any, and the next legitimate route. Do not replay the task history.

## Compile check

Before Handoff, ensure only that:

- one stable Goal and declared delivery exist;
- material authority/boundary constraints are represented once;
- at least one Task or required Task 0 is actionable;
- only currently justified Tasks/relations are materialized;
- required Verification is placed at the lowest meaningful Task / Task-Group / Goal boundary without duplication;
- Goal-level coverage remains possible;
- Evidence can be judged from authoritative or reproducible results;
- no Completion/Acceptance layer, scheduler, manager, Graph engine, persistent Graph state, or fixed Agent topology was introduced.

If an item does not change execution judgment, omit it rather than filling the taskbook for structural completeness.