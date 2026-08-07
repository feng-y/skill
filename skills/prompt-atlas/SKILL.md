---
name: prompt-atlas
description: Use when the user asks for an agent prompt, brief, goal, contract, or autonomous taskbook, especially when intent, evidence, boundaries, or success criteria are not yet stable. Route Unknown explicitly and never turn unresolved intent into executable work.
---

# Prompt Atlas

Prompt Atlas is stable autonomous taskbook generation with one stronger front end:

1. **route Unknown explicitly;**
2. **do not compile vague intent into execution.**

Human owns the requested result, acceptance requirements, confirmed boundaries, explicit priorities, and authorization. Prompt Atlas clarifies, researches, writes and hands off the taskbook, then evaluates the returned result. The Executor (the agent that runs the taskbook independently) owns implementation How and may adapt implementation scope and remaining work inside the stable contract. Execution evidence may revise facts, feasibility, implementation work, and proof needs; it may not silently redefine the requested result. When evidence makes the Goal, acceptance requirements, or a confirmed boundary unsettled, return to Intent Take. An independent Acceptor (a judge that did not do the work) owns final judgment when independence is required, especially when Executor self-attestation would be gameable.

Every executable route ends in one Goal-shaped contract: one coherent Goal, a finite set of non-substitutable completion properties, grounded Tasks and dependencies, declared authority, and layered proof. Development work uses the cheapest sufficient Task-level proof, broader Task-Group verification where combined behavior becomes meaningful, and complete-Goal verification after relevant work converges. Verification cost affects where a judge runs, never whether required proof may be omitted.

## Flow

### 0. Intent Take

Recover the latest Human authority, still-valid decisions, and evidence. Keep Human intent, reality, inference, and Unknown distinct.

A concern, hypothesis, comparison, list of questions, or broad request such as “improve”, “clean up”, or “make this better” is not automatically a Goal. Ground enough reality to expose the real choice; do not invent it.

Separate the requested outcome from proposed means. A named architecture, tool, or implementation is a hypothesis unless the Human explicitly makes it part of the required result or confirmed boundary.

Route Unknown by consequence:

- observable fact → investigate;
- execution-only fact → Task 0 (the execution preflight that verifies environment-only facts before material change);
- implementation How → Executor;
- reversible choice that preserves intent → visible delegated default;
- Goal or confirmed-boundary choice → Human;
- unavailable prerequisite with independent work → park and record;
- unavailable prerequisite with no safe work → `Status: Blocked`.

Ask Human only when proceeding would change the requested result, cross or relax a confirmed boundary or high-risk authority, or choose between materially different Goals that evidence cannot resolve.

Intent is stable only when one coherent Human-owned Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery are clear. Otherwise return `Status: Unresolved Intent` with the current understanding and the smallest useful question or probe. **Never emit executable work from unresolved intent.**

Read [contract-anatomy.md](references/contract-anatomy.md) only when this boundary is unclear.

### 1. Research

Settle everything accessible without asking: real workspace, governing specs/tests, critical commands, baselines, dependencies, and protected judges. Treat docs and command names as claims until evidenced—the common false ground includes README commands that no longer exist, lint scripts that are placeholder `echo`, and files absent from coverage reports because nothing imports them. Anything that depends on the execution environment goes into Task 0.

Before Handoff, derive the verification focus from the Goal, completion properties, real change impact/reachability, and material failure risks; then read the repo verification authority for that change surface. Compile every mandatory gate already triggered by known facts, place execution-only trigger derivation in Task 0, and never downgrade a triggered gate because the change is “only cleanup” or expected `0-diff`.

### 2. Ask

When a Human boundary remains, ask the smallest useful set, preferably one round of at most five decisions with options and a recommendation. Do not ask for facts, decomposition, architecture How, command order, or ordinary execution choices.

A delegated default must be marked unconfirmed and include its basis, cost if wrong, and detection or rollback route. It may resolve only a reversible execution choice; it may not change the Goal, confirmed boundaries, acceptance requirements, or Human authority. Silent defaults look like Human approval; visible defaults preserve Human authority.

### 3. Write the taskbook

Use [execution-compile.md](references/execution-compile.md) and preserve its fixed contract order. Keep section semantics strict and detail proportional; expose delegated decisions before execution so the Human can inspect compiler-owned defaults before Handoff.

Before expanding Tasks, compile the Goal into a finite set of non-substitutable completion properties. Each is independently necessary for complete-Goal PASS; evidence for one property cannot compensate for another. Use the verification focus and repo verification authority to compile mandatory gates and evidence needs. Verification focus is a judgment, not a new taskbook section or fixed field; choose concrete providers from the repo verification system rather than defaulting to a build/test/replay bundle.

Keep one Goal and one compact taskbook that closes the declared delivery in one execution effort. If it cannot, return to Intent Take to narrow the Human-owned delivery rather than compiling multiple taskbooks or an unbounded graph.

Stable Intent, confirmed boundaries, and protected proof remain binding. The Executor may adapt implementation How and remaining work as evidence changes.

For development work, compile three proof granularities without creating extra workflow stages: each Task has the cheapest sufficient local proof from the repo verification system; a coherent Task Group gets broader proof at the smallest boundary that establishes combined behavior; complete-Goal verification runs after relevant groups converge. Expensive judges are scheduled by proof scope, measured or known cost, and the recovery cost of finding failure later.

Before Handoff, reserve private acceptance under [completion-trust.md](references/completion-trust.md) only when visible proof could false-pass, remain gameable, or fail to close the Goal. Otherwise rely on protected visible judges. Keep any reserved checks outside the Executor-visible taskbook and, where the runtime permits, outside the Executor context; private checks may vary samples or observation paths, never requirements.

### 4. Handoff

Return ordinary prompts, briefs, or contracts as text when that is the requested delivery. For `Status: Executable`, materialize the same authoritative taskbook body as a Markdown file in an OS/runtime temporary directory outside the current repo/workspace; do not hardcode `/tmp`. The TUI may show the body, summary, and path, but the Executor starts from that file rather than reconstructing the task from conversation. If materialization fails, return the text but do not claim execution started.

A direct request to complete work grants compile-and-run authority. After the taskbook file exists, launch the Executor with a thin driver rather than another orchestration prompt:

```text
Read <TASKBOOK_PATH> as the authoritative contract. Execute toward its Goal; Tasks are the current dependency graph, not the completion condition. Loop: observe → run ready work → verify with the repo's applicable verification system → update evidence/graph. Replan as evidence changes without changing Goal, boundaries, authority, or mandatory gates. Stop only when the Completion Contract is proven, no safe work remains, or an explicit budget ends.
```

Prompt Atlas does not supervise live execution. When the Executor returns, continue into the same Acceptance flow; Prompt Atlas retains Goal-level judgment.

### 5. Acceptance

Judge against the same authoritative taskbook: Goal, Completion Contract, confirmed boundaries, and mandatory gates. Executor `done`, `PASS`, and self-supplied evidence are acceptance inputs, not the final verdict. When the Goal and boundaries remain stable, safe executable work remains, and a completion property is unsatisfied or evidence/gates are missing or stale, return only those focused gaps to the Executor and continue the same taskbook instead of recompiling it. Return to Intent Take/Human only when safe progress requires changing the requested result, acceptance requirements, a confirmed boundary, explicit Human priority, or authority.

When the result returns, rerun the visible acceptance and any reserved checks. Bind an independent Acceptor whenever final judgment requires independence—for example, proof remains gameable or incomplete, including because checks intended as private were visible and no other protected judge closes the Goal. An Acceptor is independent only if it did not materially implement the work and evaluates from the authoritative taskbook and accepting environment rather than the Executor's conclusion. Executor evidence is input, not final judgment.

If the required Acceptor or accepting environment is unavailable, stop at `ready for independent acceptance` and return a self-contained acceptance handoff for a non-implementing Acceptor: the authoritative taskbook, Executor result and evidence, visible acceptance, any reserved acceptance checks and their visibility, protected judges and baselines, and the required final report—PASS or the exact residual.

Local Task PASS and Task-Group PASS may unlock downstream work; neither is complete-Goal PASS. Protect judges and baselines and use reverse validation when checks can fail silently. Read [completion-trust.md](references/completion-trust.md) whenever preparing or running private or independent acceptance, or when checks could false-pass.

## Output

Emit one state with enough information for the declared route to continue correctly:

- **`Status: Unresolved Intent`** — the current understanding, the unresolved Goal fork or material consequence, and the smallest remaining Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition that would unblock safe progress;
- **`Status: Executable`** — one grounded autonomous taskbook; when the user asked to complete the work, continue under Handoff after compilation.

`ready for independent acceptance` is an acceptance ceiling after an Executable route, not a fourth compile state.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, or other control layer.
