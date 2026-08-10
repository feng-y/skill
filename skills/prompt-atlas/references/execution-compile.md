# Autonomous Taskbook: turn a stable Goal into an execution contract

Use only after Goal is settled. Produce a taskbook that is **complete enough under current Evidence without guessing the future**, so a fresh Executor can see the known global structure and advance independently.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is semantic ownership / proof chain, not a fixed temporal sequence. Keep **one fact, one owner**: compile every Task, relationship, and Verification obligation already established by current Evidence; delay only work whose existence, scope, or concrete action still materially depends on future Evidence.

## Goal

Write one Human-owned Goal: desired result, what must remain true, and final delivery. Include Why only when it changes tradeoffs. Confirmed boundaries, authorization limits, protected side effects, or unconfirmed delegated defaults appear only when they actually constrain execution, and only once. Explicit Human verification requirements belong to Verification, not Goal.

Do not add Completion/Acceptance semantics.

## Execution / Graph

Compile the **best-known complete execution structure supported by current Evidence**. Do not give only the next step, and do not simulate an unknown future.

A Task is an executable delta. Normally it contains only:

- observable result;
- a non-obvious starting point / Task-local hard constraint when needed;
- one local check only when it is already applicable and decides whether execution may progress.

Do not repeat Goal, global boundaries, shared Reality, repo rules, or Goal-level Verification inside each Task. Work that current Evidence already proves must exist, has a sufficiently stable boundary, and has a real relationship should be compiled once. Keep simple work linear; read [execution-graph.md](execution-graph.md) only when a real dependency, parallel relation, shared write, Task Group boundary, or join changes execution judgment. Delay materialization only when the work's **existence, affected scope, or necessary relationship** still depends on future Evidence.

Any Human-confirmed execution strategy, scope boundary, or must-preserve constraint is part of the current contract input and must not be replaced by model-invented decomposition. When current Evidence already supports a safe bounded ready frontier, express it directly; consumer, dependency, history, or implementation Unknown that does not block that frontier must not be materialized as prerequisite work. **The ready frontier says what can execute now; it does not redefine the Human-owned Goal. Seeing only a subset of leaf work must not turn the Goal into `Layer 1`, a phase, or a local cleanup.** The Graph stop boundary comes from Goal / confirmed boundaries, and adjacent residual discovered during execution does not automatically expand scope.

**Task 0** is optional, bounded execution warmup. Use it only when a missing execution-time fact blocks selection of the first safe material action, or when required Verification explicitly requires a trigger to be settled before the first material action. It is not a second Research phase, a default checklist, a full reachability inventory, or a collection point for ordinary execution Unknown. If current ready work can begin safely, leave other facts to the Executor to obtain only when they actually affect that work.

Runtime progression stays:

```text
ready work → execute / probe / applicable Verification → Evidence → update affected Execution / Graph / Verification → Completion Hook → continue / expand / stop / block
```

Reuse compiled work while it remains valid; new Evidence repairs only contingent / invalidated parts. If several new probes/tasks could close the same material gap, prefer the lower-cost one that is more likely to change Execution / Verification judgment. Continue in the same taskbook while Goal, confirmed boundaries, Human authority, and required Verification stay stable; cross those stable boundaries only through [SKILL.md](../SKILL.md).

## Verification

Task / Task Group / Goal are **placement granularity**, not a requirement to fill three levels of Verification roadmap at Compile time:

- **Task** — compile a known local check when it already applies and controls progression; runtime-triggered obligations join when they become applicable;
- **Task Group** — when known combined behavior needs separate proof, compile one check at the smallest meaningful combined boundary; contingent joins materialize only after Evidence establishes them;
- **Goal** — preserve delivery-level coverage required by repo authority or explicit Human verification requirements; do not predeclare an extra “final verification command”.

Compile known Verification obligations and trustworthy concrete action/scope now. When provider, target, scope, or whether an obligation triggers still depends on change surface, binding/config, provider validity, or other execution reality, preserve the stable trigger/authority and materialize the corresponding action only after the fact becomes true.

Goal-level Verification is a **coverage boundary** consumed by the Completion Hook: reuse still-valid lower-level Evidence and add only real coverage gaps or invalidated checks. Required scope follows actual impact/reachability and repo authority. Expected `0-diff`, cleanup, or refactor cannot downgrade already-triggered requirements. A provider is only a claim until it is shown to really run, cover the claim, and propagate failure; when trust and coverage are equal, prefer the lower-cost provider whose failure signal narrows the problem space more effectively.

Read [verification-trust.md](verification-trust.md) only when ordinary repo Verification may false-pass, be directly targetable, fail silently, or genuinely require independent Evidence.

## Evidence

Compile proof / trust requirements, not future results. Runtime Evidence keeps only material facts needed for judgment and the next decision: provider/probe, target/revision, material binding/config, verdict/exit, and raw output or a stable artifact/reference.

Executor narration or self-declared `PASS` is not Evidence. When the judging side can access the authoritative environment at reasonable cost, reacquire final-judgment-critical repo-authoritative Evidence directly; otherwise require reproducible provenance. Missing, stale, under-covered, or judge-weakened Evidence cannot support PASS.

Evidence invalidates only affected conclusions: reuse results while their premises remain valid. When new Evidence disproves an old claim, replace or invalidate it at its original semantic owner rather than keeping conflicting states simultaneously valid.

## Completion Hook

The taskbook carries a completion judgment without adding a Completion layer/schema/state/Acceptor. At each material Evidence update, it reads only **Goal / constraints + triggered required Verification + current valid Evidence** and decides:

- whether the Goal's material outcome has minimum sufficient Evidence;
- whether must-preserve conditions, confirmed boundaries, Human authority, and repo hard constraints still hold;
- whether every triggered required Verification obligation has trustworthy, still-valid Evidence.

If all hold, `STOP` without manufacturing a Final Verification Task. If a material gap remains, continue existing work or materialize only the contingent work / Verification that can close that gap. If no safe route remains, return accurate `BLOCKED` / non-PASS. Completed Tasks or an empty frontier are not completion conditions by themselves.

Final reporting contains only actual delivery, decisive Evidence, exact residual/blocker if any, and the next legitimate route.

## Handoff check

Before Handoff, confirm only:

- Goal and each material authority have exactly one owner;
- all required Tasks / relations / Verification obligations already established by current Evidence are sufficiently compiled rather than hidden for artificial laziness;
- the ready frontier has not narrowed the Human Goal, and any Human-confirmed execution strategy or stop boundary has not been rewritten by the model;
- contingent work is not speculatively materialized, and at least one Task or truly necessary Task 0 can start immediately;
- required Verification is non-duplicated and the Completion Hook can judge stop / continue / block from existing semantic owners;
- discovery / Evidence whose premises have not changed is not reacquired, and no Completion/Acceptance, scheduler, Graph engine, or fixed Agent topology has been added.

If content does not change execution judgment, omit it.