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

Keep simple work as one coarse Task or the shortest linear structure; do not split Tasks just to describe the future up front. Refine Tasks and read [execution-graph.md](execution-graph.md) only when current Evidence shows a real dependency, parallelism, shared write, Task-Group boundary, or join that changes execution judgment. Do not materialize downstream Tasks whose existence depends on Evidence not yet obtained: execute the current frontier first, then expand only what new Evidence makes real.

Use **Task 0** only for a compile-time-known premise that matters before material change but can be established only in the execution environment. Task 0 is not another research phase.

Runtime progression is simply:

```text
ready work → execute / probe → Evidence → update remaining Graph → continue
```

Evidence may add, remove, split, merge, or reorder remaining work while Goal, confirmed boundaries, Human authority, and required Verification remain stable. Reuse completed work whose Evidence premises still hold. If execution crosses those stable boundaries, route back through [SKILL.md](../SKILL.md) rather than encoding another control flow here.

## Verification

Write each Verification obligation once, at the lowest meaningful boundary:

- **Task** — cheapest sufficient local check when it controls progression;
- **Task Group** — one broader check at the smallest combined boundary when local checks cannot prove combined behavior;
- **Goal** — remaining delivery-level coverage required by repo authority or explicit Human verification requirements.

Goal-level Verification is a final **coverage boundary**, not an extra mandatory command. Reuse valid lower-level Evidence; run only required checks that remain uncovered or were invalidated.

Required Verification follows actual impact/reachability and repo verification authority. Expected `0-diff`, cleanup, or refactor does not downgrade an already-triggered requirement. Concrete providers come from the repo verification system and prove only what they actually cover; execution-only provider/binding triggers belong in Task 0.

Read [verification-trust.md](verification-trust.md) only when normal protected repo Verification may false-pass, be gameable, fail silently, or genuinely needs independent Evidence.

## Evidence

Do not restate the Verification plan. Preserve only Evidence needed to judge material claims: actual provider/probe, target/revision and material binding/config when relevant, verdict/exit, and raw output or stable artifact/reference.

Executor narration or self-declared `PASS` is input, not final Evidence. Reacquire final-judgment-critical repo-authoritative Evidence when the judging side can do so at reasonable cost; otherwise require reproducible provenance. Missing, stale, under-covered, or judge-weakened Evidence is non-PASS.

Final reporting stays small: delivered result, decisive Evidence, exact residual/blocker if any, and the next legitimate route. Do not replay task history.

## Handoff check

Before Handoff, confirm only:

- one stable Goal and material authority constraints are represented once;
- at least one Task or necessary Task 0 is actionable, with only currently justified Tasks/relations materialized;
- required Verification is non-duplicated and Goal-level coverage remains reachable;
- final Evidence can be judged without adding Completion/Acceptance, scheduler, Graph engine, or fixed Agent topology.

If content does not change execution judgment, omit it.