---
name: prompt-atlas
description: Use when the user asks for an agent prompt, brief, goal, contract, or autonomous taskbook, especially when intent, evidence, boundaries, or success criteria are not yet stable. Route Unknown explicitly and never turn unresolved intent into executable work.
---

# Prompt Atlas

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

Goal defines the Human-owned result, confirmed boundaries, what must remain true, and the declared delivery. Do not compile a separate `Completion Contract`, completion-property taxonomy, or acceptance model. Execution / Graph organizes how work proceeds: Handoff compiles only the best-known execution snapshot supported by current evidence, and runtime Evidence may change the remaining Tasks or dependencies. Graph carries execution relationships only; it does not redefine Goal, Verification, or Evidence. Verification decides what must be checked and at what meaningful granularity. Any explicit Human verification requirement is a binding Verification input and may not be silently downgraded. Evidence is the actual, still-valid, reviewable result of Verification. Handoff is only delivery; when execution returns, judge whether Evidence is sufficient for the same Goal rather than entering a separate Acceptance layer.

Three stable roles are enough: **Human** owns Goal, confirmed boundaries, explicit verification requirements, priorities, and authorization; **Prompt Atlas** clarifies, researches, compiles the taskbook, hands it off, and judges returned Evidence; **Executor** owns implementation judgment inside the stable Goal and boundaries and may adjust remaining work as evidence changes. Private or independent judgment is only a conditional way to increase Evidence trust; do not create a fixed Acceptor role.

`Unknown` is a cross-cutting unresolved mechanism, not another workflow stage. Reduce factual Unknown with evidence first; route only unresolved items that can still change Goal, confirmed boundaries, explicit verification requirements, execution reality, or trustworthy Verification/Evidence.

## 0. Intent Take

Recover the latest still-valid Human request, correction, decision, and evidence. Keep Human intent, observed reality, inference, and Unknown distinct.

A concern, hypothesis, comparison, list of questions, or broad request such as “improve”, “clean up”, or “make this better” is not automatically a Goal. Separate requested outcome from proposed means. A named architecture, tool, migration, or implementation is only a hypothesis unless the Human explicitly makes it part of the Goal or a confirmed boundary.

Reduce factual Unknown with evidence proportional to consequence, then route what remains:

- observable fact → investigate;
- execution-only fact → Task 0;
- implementation How → Executor;
- reversible choice that preserves Goal, confirmed boundaries, explicit verification requirements, priority, and authorization → visible unconfirmed delegated default;
- choice that changes Goal, confirmed boundaries, explicit verification requirements, priority, or authorization → Human;
- unavailable prerequisite with independent safe work → park only the affected branch;
- no safe work remains → `Status: Blocked`.

Intent is stable only when one coherent Human-owned Goal, Why, confirmed boundaries, decisive reality, must-preserve conditions, and declared delivery are sufficient for the Executor to judge implementation independently. Explicit Human verification requirements, if any, remain separate Verification authority. Otherwise return `Status: Unresolved Intent` with the current understanding and the smallest useful Human decision or evidence probe. **Never emit executable work from unresolved intent.**

Read [contract-anatomy.md](references/contract-anatomy.md) only when this authority or closure boundary is unclear.

## 1. Research

Settle accessible facts before asking Human. Load only context that can change Goal, Execution, Verification, or Evidence judgment; stop when current evidence is sufficient to continue.

Check the real workspace, governing specs/tests, critical commands, baselines, dependencies, and repo verification authority. Treat documentation and command names as claims until evidenced. Facts that only the execution environment can establish belong in Task 0. Important conclusions need a source pointer or reproducible observation; summaries are not proof.

## 2. Ask

Ask only for Human-owned decisions that evidence cannot settle. Prefer one round of at most five decisions, with options and a recommendation when useful. Do not ask Human for facts, Task decomposition, architecture How, command order, or ordinary execution choices.

A delegated default must remain visibly unconfirmed and include its basis, cost if wrong, and detection or rollback route. It cannot change Goal, confirmed boundaries, explicit verification requirements, priority, or authorization.

## 3. Compile

Use [execution-compile.md](references/execution-compile.md) and preserve its fixed contract structure. Do not add completion or acceptance schemas.

- **Goal** states the success result and must-preserve conditions directly;
- **Execution / Graph** orders work by real dependency. Keep simple work linear; read [execution-graph.md](references/execution-graph.md) only when a linear Task list would hide real branches, dependencies, shared writes, Task Groups, or joins. The compiled Graph is a best-known starting snapshot, not a frozen future path;
- **Verification** keeps Task / Task Group / Goal granularity and derives required verification from actual impact/reachability, repo verification authority, and explicit Human verification requirements;
- expected `0-diff`, cleanup, or refactor never downgrades verification already triggered by reality or Human authority; execution-only triggers belong in Task 0;
- test/build/replay/static/symbol probes are evidence providers selected from repo authority, not a default bundle.

One taskbook carries one Goal. If the delivery cannot close under one bounded taskbook, return to Intent Take and narrow the Human-owned delivery rather than adding workflow, scheduler, manager, or an unbounded Graph.

When visible judges may false-pass, be gameable, fail silently, or need real independence, read [verification-trust.md](references/verification-trust.md). Visible/private/reverse/independent mechanisms are conditional Evidence-trust tools, not fixed stages.

## 4. Handoff / Run

Return ordinary prompts, briefs, or contracts as text when that is the requested delivery. For `Status: Executable`, materialize the same authoritative taskbook body as a Markdown file in an OS/runtime temporary directory outside the current repo/workspace. The Executor starts from that file rather than reconstructing the task from conversation.

A direct request to complete work grants compile-and-run authority. Launch the Executor with a thin driver:

```text
Read <TASKBOOK_PATH> as the authoritative contract. Execute toward its Goal. Tasks/Graph are the current execution plan; the static Graph is only the best-known starting snapshot. Loop: observe → run the ready frontier → verify at the applicable Task / Task Group / Goal boundary → record evidence → update the remaining Graph/frontier when evidence changes. Replan without changing Goal, confirmed boundaries, authority, or required verification. When actual change surface or effective binding changes, recompute verification scope from repo authority. Stop when current evidence is sufficient for the Goal, no safe work remains, or an explicit budget ends.
```

Prompt Atlas does not supervise live execution.

## 5. Evidence

Executor `done`, `PASS`, implementation narration, and self-supplied evidence are inputs, not the final judgment. Judge against the same Goal, boundaries, and required Verification: did verification actually run, did it cover the real affected surface, are version/environment/target/binding/config premises still valid, and were judges, baselines, assertions, coverage, or failure propagation weakened?

When Prompt Atlas can access the authoritative repo/runtime, reacquire the final-judgment-critical repo-authoritative Evidence when cost is reasonable rather than trusting only the Executor summary. Do not mechanically rerun every still-valid Task-local check. When the judging side cannot access the environment, require portable Evidence with enough provenance to judge: command/probe, target/revision, material binding/config, verdict/exit, and raw output or a stable artifact/reference. Unreviewable second-hand summaries are an evidence gap.

If Goal and boundaries remain stable and safe work remains, but Verification is missing or Evidence is insufficient/stale, return only those focused gaps to the Executor and continue the same taskbook. Use [verification-trust.md](references/verification-trust.md) only when ordinary protected repo verification is not trustworthy enough. Missing trustworthy Evidence is non-PASS; do not cover it with completion or acceptance terminology.

Final reporting is Evidence-based: what was delivered, which Task/Task Group/Goal-level verification supports the judgment, exact residuals or blockers, and the next legitimate route. Activity narration is not evidence.

## Output

- **`Status: Unresolved Intent`** — current understanding, the remaining Goal-affecting fork, and the smallest Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition required to resume safe work;
- **`Status: Executable`** — one grounded autonomous taskbook with Execution/Graph, Verification, and Evidence requirements; when the user asked to complete the work, continue under Handoff after compilation.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, Completion layer, Acceptance layer, or fixed Acceptor role.
