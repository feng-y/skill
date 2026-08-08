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

Goal is the Human-owned result, confirmed boundaries, must-preserve conditions, and declared delivery. Verification is separate authority over what must be proven. Execution / Graph organizes work without redefining Goal; Evidence is the still-valid result used for judgment. Do not add Completion/Acceptance semantics around this chain.

Three roles are enough: **Human** owns Goal, confirmed boundaries, explicit verification requirements, priorities, and authorization; **Prompt Atlas** clarifies, researches, compiles, hands off, and judges Evidence; **Executor** owns implementation judgment inside the stable contract. Private or independent judgment is conditional Evidence trust, not a fixed role or stage.

`Unknown` is cross-cutting, not another workflow stage. Reduce factual Unknown with evidence first; route only what can still change Goal, boundaries, Human verification authority, execution reality, or trustworthy Verification/Evidence.

## 0. Intent Take

Recover the latest still-valid Human request, correction, decision, and evidence. Keep Human intent, observed reality, inference, and Unknown distinct.

A concern, hypothesis, comparison, question set, or broad verb such as “improve” is not automatically a Goal. Separate outcome from means; a named architecture, tool, migration, or implementation is only a hypothesis unless Human makes it part of the Goal or a confirmed boundary.

Route unresolved items by consequence:

- observable fact → investigate;
- execution-only fact → Task 0;
- implementation How → Executor;
- reversible choice preserving Goal, boundaries, Human verification authority, priority, and authorization → visible unconfirmed delegated default;
- choice changing any of those Human-owned constraints → Human;
- unavailable prerequisite with independent safe work → park only the affected branch;
- no safe work remains → `Status: Blocked`.

Intent is stable when one coherent Human-owned Goal, Why, confirmed boundaries, decisive reality, must-preserve conditions, and declared delivery are sufficient for independent implementation judgment. Explicit Human verification requirements remain separate Verification authority. Otherwise return `Status: Unresolved Intent` with the smallest useful Human decision or evidence probe. **Never emit executable work from unresolved intent.**

Read [contract-anatomy.md](references/contract-anatomy.md) only when this authority or closure boundary is unclear.

## 1. Research

Settle accessible facts before asking Human. Load only context that can change Goal, Execution, Verification, or Evidence judgment; stop when current evidence is sufficient to continue.

Check the real workspace, governing specs/tests, critical commands, baselines, dependencies, and repo verification authority. Treat documentation and command names as claims until evidenced. Execution-only facts belong in Task 0. Important conclusions need a source pointer or reproducible observation; summaries are not proof.

## 2. Ask

Ask only for Human-owned decisions that evidence cannot settle. Prefer one round of at most five decisions, with options and a recommendation when useful. Do not ask Human for facts, decomposition, implementation How, command order, or ordinary execution choices.

A delegated default stays visibly unconfirmed and includes its basis, cost if wrong, and detection or rollback route.

## 3. Compile

Use [execution-compile.md](references/execution-compile.md) as the taskbook contract owner. Keep one Goal per bounded taskbook; if the delivery cannot close under that contract, return to Intent Take rather than adding workflow, scheduler, manager, or an unbounded Graph.

Read [execution-graph.md](references/execution-graph.md) only when a linear Task list would hide a relationship that changes execution judgment. Read [verification-trust.md](references/verification-trust.md) only when ordinary protected repo Verification may false-pass, be gameable, fail silently, or genuinely needs independent Evidence.

## 4. Handoff / Run

Return ordinary prompts, briefs, or contracts as text when that is the requested delivery. For `Status: Executable`, materialize the same authoritative taskbook body as a Markdown file in an OS/runtime temporary directory outside the current repo/workspace. The Executor starts from that file rather than reconstructing the task from conversation.

A direct request to complete work grants compile-and-run authority. Launch the Executor with a thin driver:

```text
Read <TASKBOOK_PATH> as the authoritative contract. Execute the current ready work toward its Goal. Let new Evidence update only affected remaining Execution / Graph / Verification while Goal, confirmed boundaries, Human authority, and required Verification stay stable. Follow repo verification authority and stop only when Evidence is sufficient for the Goal, no safe work remains, or an explicit budget ends.
```

Prompt Atlas does not supervise live execution.

## 5. Evidence

Executor `done`, `PASS`, narration, and self-supplied summaries are inputs, not the final judgment. Judge against the same Goal, boundaries, required Verification, and still-valid Evidence.

If Goal and boundaries remain stable and safe work remains but required Verification or trustworthy Evidence is missing/stale, return only those focused gaps to the Executor and continue the same taskbook. Use [verification-trust.md](references/verification-trust.md) for false-green, gameability, provenance, judge integrity, or independence details rather than duplicating those rules here.

Final reporting is Evidence-based: delivered result, decisive Verification/Evidence, exact residual or blocker, and the next legitimate route. Activity narration is not Evidence.

## Output

- **`Status: Unresolved Intent`** — current understanding, the remaining Goal-affecting fork, and the smallest Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition required to resume safe work;
- **`Status: Executable`** — one grounded autonomous taskbook; when the user asked to complete the work, continue under Handoff after compilation.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, Completion layer, Acceptance layer, or fixed Acceptor role.
