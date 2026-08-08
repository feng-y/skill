# Autonomous Taskbook

Use only after Goal is stable. Produce the smallest truthful taskbook that lets an Executor start safely and continue by judgment.

Semantic ownership stays fixed:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

Physical structure is sparse. **One fact, one owner.** Materialize only information that changes execution judgment; omit empty sections, repeated context, and speculative future work. The taskbook is a starting contract, not a full simulation of execution.

## Goal

Write one concise Human-owned Goal: desired result, must-preserve conditions, and declared delivery. Include Why only when it changes a tradeoff.

Represent confirmed boundaries, authorization limits, protected side effects, or an unconfirmed delegated default only when they materially constrain execution, and state them once. Human explicit verification requirements belong to Verification, not Goal.

Do not add Completion/Acceptance semantics.

## Execution / Graph

Compile the **minimum currently justified executable structure**.

A Task is an executable delta, not a miniature prompt. Normally it contains only:

- observable result;
- a non-obvious starting point or Task-local hard constraint, if needed;
- one local check only when that check decides whether execution may progress.

Do not repeat Goal, global boundaries, shared reality, repo rules, or Goal-level Verification inside Tasks.

Keep simple work coarse and linear. Read [execution-graph.md](execution-graph.md) only when current Evidence shows a real dependency, parallelism, shared write, Task-Group boundary, or join that changes execution judgment. Do not materialize downstream Tasks whose existence depends on Evidence not yet obtained. Runtime Graph/frontier evolution is owned by that reference; do not restate it here.

Use **Task 0** only for a compile-time-known premise that matters before material change but can be established only in the execution environment. Task 0 is not another research phase.

If execution discovers facts that cross stable Goal, confirmed boundaries, Human authority, or required Verification, route back through [SKILL.md](../SKILL.md) rather than encoding another control flow here.

## Verification

Write each Verification obligation once, at the lowest meaningful boundary:

- **Task** — cheapest sufficient local check when it controls progression;
- **Task Group** — one broader check at the smallest combined boundary when local checks cannot prove combined behavior;
- **Goal** — remaining delivery-level coverage required by repo authority or explicit Human verification requirements.

Goal-level Verification is a final **coverage boundary**, not an extra mandatory command. Reuse valid lower-level Evidence; run only required checks that remain uncovered or were invalidated.

Required Verification follows actual impact/reachability and repo verification authority. Expected `0-diff`, cleanup, or refactor does not downgrade an already-triggered requirement. Concrete providers come from the repo verification system and prove only what they actually cover; execution-only provider/binding triggers belong in Task 0.

Read [verification-trust.md](verification-trust.md) only when ordinary protected repo Verification may false-pass, be gameable, fail silently, or genuinely needs independent Evidence. Judge protection, reverse/private/independent Evidence, and detailed provenance rules are owned there.

## Evidence

Do not restate the Verification plan. Preserve only Evidence needed to judge material claims: what actually ran, the relevant target/revision or binding/config when needed, verdict/exit, and raw output or a stable artifact/reference.

Executor narration or self-declared `PASS` is not enough. Missing, stale, under-covered, unreviewable, or judge-weakened Evidence is non-PASS; trust mechanics live in [verification-trust.md](verification-trust.md).

Final reporting stays small: delivered result, decisive Evidence, exact residual/blocker if any, and the next legitimate route. Do not replay task history.

## Handoff check

Before Handoff, confirm only:

- one stable Goal and material authority constraints are represented once;
- at least one Task or necessary Task 0 is actionable, with only currently justified work materialized;
- required Verification is non-duplicated and Goal-level coverage remains reachable;
- final Evidence can be judged without adding Completion/Acceptance, scheduler, Graph engine, or fixed Agent topology.

If content does not change execution judgment, omit it.
