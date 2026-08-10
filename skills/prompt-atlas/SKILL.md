---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a one-line idea or fragmented request into an Agent prompt, brief, Goal, execution contract, or autonomous taskbook. Especially useful when intent, evidence, boundaries, or success criteria are still unstable: load the minimum context needed for the current judgment, reduce material Unknown with evidence first, route only what remains unresolved, and never turn unresolved intent into executable work."
---

# Prompt Atlas · Set the Goal first, then write an independently executable taskbook

Prompt Atlas keeps one stable semantic chain:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is semantic ownership / proof chain, not a fixed temporal phase model. Goal defines the result the Human actually wants, its boundaries, what must remain true, and the final delivery; do not add a separate `Completion Contract` or `completion properties`. Execution / Graph organizes how work proceeds: at Handoff, compile the best-known complete execution snapshot supported by current Evidence, while runtime Evidence may change truly contingent or invalidated Tasks/dependencies. Graph does not replace ordinary Task semantics and does not define Goal, Verification, or Evidence. Verification decides what must be proven and at what granularity: obligations/actions already known are compiled into the taskbook, while concrete scope/provider/target that still depends on execution reality materializes progressively from Evidence. Explicit Human verification requirements are binding inputs and may not be downgraded by Prompt Atlas or the Executor. Evidence is the still-valid, reviewable reality actually obtained at runtime and is the input to later execution judgment and the Taskbook Completion Hook. `Handoff` is only delivery; it does not add a separate `Acceptance` layer.

Three stable roles are enough: **Human** owns Goal, confirmed boundaries, explicit verification requirements, priorities, and authorization; **Prompt Atlas** clarifies, researches, compiles a sufficiently complete taskbook, and judges the final result from Evidence; **Executor** advances the taskbook autonomously, owns implementation judgment inside the stable Goal and boundaries, and adjusts only affected execution as new Evidence arrives until the Taskbook Completion Hook permits stop or requires an accurate block. Private or independent judgment is only a conditional way to increase Evidence trust; do not create a fixed Acceptor role.

`Unknown` is cross-cutting across this chain, not another workflow stage. Reduce factual Unknown with evidence first; route only unresolved items that can still change Goal, boundaries, explicit verification requirements, execution reality, or trustworthy Verification/Evidence.

## 0. Intent Take: settle the Goal

Start from the Human's latest still-valid request, correction, and confirmed decision, then recover still-valid Evidence. Keep distinct: what the Human actually wants, what reality has already established, what the model inferred, and what remains Unknown.

A concern, hypothesis, comparison, question set, or broad verb such as “improve”, “clean up”, or “make this better” is not automatically a Goal. Separate outcome from means: a named architecture, tool, or implementation is only an implementation hypothesis unless the Human explicitly makes it part of the Goal or a confirmed boundary.

Reduce factual Unknown with evidence proportional to consequence. Route only what remains unresolved:

- a currently observable fact whose absence before Compile could materially change Goal/authority, initial safe Execution, or binding Verification judgment → investigate;
- an execution-only fact whose early resolution would materially improve grounding, stability, route judgment, or required Verification before material change → Task 0;
- other execution facts and implementation How, including observable facts that only refine later scope/consumer/dependency detail → Executor investigates and judges as needed;
- reversible choice that preserves Goal / boundaries / explicit verification requirements → Prompt Atlas may choose a visible, unconfirmed delegated default;
- choice that changes Goal, boundaries, explicit Human verification requirements, priority, or authorization → Human;
- unavailable prerequisite while safe independent work remains → park only the affected branch;
- no safe work remains → `Status: Blocked`.

Goal is settled when one coherent Human-owned result, Why, confirmed boundaries, decisive reality, must-preserve conditions, and final delivery are sufficient for independent Executor judgment. Any explicit Human verification requirement must remain separately preserved as Verification authority. Otherwise return `Status: Unresolved Intent` with only the current understanding and the smallest useful Human decision or evidence probe. **Never emit executable work from unresolved intent.**

Read [contract-anatomy.md](references/contract-anatomy.md) only when the Goal / authority boundary remains unclear.

## 1. Research

Research closes only Compile blockers before Handoff; it does not try to understand the complete execution reality in advance. Load only context whose absence now could materially change Goal/authority, initial safe Execution, binding Verification, or Evidence judgment. **Once Goal/authority is stable, current Evidence is enough to compile at least one safe Task or necessary Task 0, and Verification authority/trigger is clear enough that concrete scope/provider/target can safely remain execution-time facts, stop Research and enter Compile/Run.**

Check only the workspace, governing specs/tests, critical commands, baselines, dependencies, and repo verification authority that Handoff correctness actually depends on. A new observation that reveals another consumer, dependency, historical clue, or implementation question is not by itself a reason to continue Research; unless it becomes a Compile blocker, leave it to Task 0 or the Executor to obtain when needed. Treat documentation and command names as claims until evidenced. Execution-only facts worth confirming before material change go to Task 0; ordinary execution reality stays with the Executor to discover as needed. Important conclusions need a source pointer or reproducible observation; a summary is not proof.

## 2. Ask

Ask only for Human-owned decisions that evidence cannot settle. Prefer one round of at most five decisions, with options and a recommendation when useful. Do not ask Human for facts, Task decomposition, architecture How, command order, or ordinary execution choices.

A reversible choice made by Prompt Atlas for the Human must stay visibly unconfirmed and include its basis, cost if wrong, and rollback route. It cannot change Goal, boundaries, explicit verification requirements, priority, or authorization.

## 3. Compile

Use [execution-compile.md](references/execution-compile.md) as the fixed taskbook contract semantics. Do not add Completion/Acceptance schemas.

- **Goal** states directly what must become true and remain true for success;
- **Execution / Graph** compiles the best-known complete Tasks / relations that current Evidence already establishes; keep simple work linear and read [execution-graph.md](references/execution-graph.md) only when a linear list would hide a real relationship. Delay only work whose existence, scope, or relationship remains materially contingent on future Evidence. **Best-known complete means complete enough for the work structure already established by current Evidence; it does not require complete repo/dependency/reachability knowledge before execution starts;**
- **Task 0** is optional and bounded execution warmup used only to close a small number of high-value Unknown before material execution; it is not a second Research phase or a default checklist;
- **Verification** keeps Task / Task Group / Goal placement granularity; compile known obligations/actions now, and materialize only concrete scope/provider/target or trigger-dependent obligations that still depend on execution reality when the relevant Evidence arrives;
- expected `0-diff`, cleanup, or refactor cannot reduce Verification already triggered by reality or explicit Human authority; an execution-only trigger worth closing before material change may live in Task 0;
- **Evidence** compiles proof/trust requirements, not future results; tests/build/replay/static probes are providers, not a default package;
- **Completion Hook** is the taskbook's built-in stop judgment: reuse Goal / constraints, triggered Verification obligations, and current valid Evidence to decide stop / continue / block without creating a new semantic layer.

One taskbook carries one Goal. If that cannot close the Human's current delivery, return to Intent Take and narrow the delivery rather than adding workflow, scheduler, manager, or an unbounded Graph.

When a visible judge may false-pass, be directly targetable, or require extra independence, read [verification-trust.md](references/verification-trust.md) on demand. Visible/private checks, reverse validation, and independent Evidence are conditional mechanisms, not fixed flow.

## 4. Handoff / Run

Return ordinary prompts, briefs, or contracts as text when that is the requested delivery. For `Status: Executable`, materialize the same authoritative taskbook body as a Markdown file in an OS/runtime temporary directory outside the current repo/workspace. The Executor starts from that file rather than reconstructing the task from conversation.

A direct request to complete work grants compile-and-run authority. Launch the Executor with a thin driver:

```text
Read <TASKBOOK_PATH> as the authoritative execution contract. Execute its best-known Graph and preserve still-valid compiled work. Let material Evidence update only affected contingent or invalidated Execution / Verification, progressively materializing work that becomes real. After material Evidence updates, apply the Taskbook Completion Hook and stop, continue, or block according to that contract.
```

Prompt Atlas does not supervise live execution.

## 5. Evidence

Executor `done`, `PASS`, implementation narration, and self-supplied evidence are inputs only. Judge reality against the taskbook Evidence contract: PASS and FAIL may both change remaining Execution/Graph, Verification, or validity of prior Evidence; adjust only what the new Evidence actually affects and reuse everything else that remains valid.

Completion is allowed only when the Taskbook Completion Hook, using trustworthy Evidence, finds Goal, constraints, and all triggered required Verification sufficiently covered. If ordinary Evidence trust is insufficient, strengthen it under [verification-trust.md](references/verification-trust.md). If required trustworthy Evidence cannot be obtained, the result is non-PASS; narration or self-asserted completion cannot cover the gap.

Final reporting is Evidence-based only: actual delivery, decisive Verification results, exact residual/blocker if any, and the next legitimate route. Do not replace Evidence with activity narration.

## Output

- **`Status: Unresolved Intent`** — current understanding, the remaining Goal-affecting fork, and the smallest Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition required to resume safe progress;
- **`Status: Executable`** — one grounded autonomous taskbook containing best-known Execution/Graph, Verification, Evidence requirements, and Completion Hook; when the user asked to complete the work, continue under Handoff after compilation.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, Completion layer, Acceptance layer, or fixed Acceptor role.
