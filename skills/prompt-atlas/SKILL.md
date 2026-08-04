---
name: prompt-atlas
description: Use when the user asks for an agent prompt, brief, goal, contract, or autonomous taskbook, especially when intent, evidence, boundaries, or success criteria are not yet stable. Route Unknown explicitly and never turn unresolved intent into executable work.
---

# Prompt Atlas

Prompt Atlas is stable autonomous taskbook generation with one stronger front end:

1. **route Unknown explicitly;**
2. **do not compile vague intent into execution.**

Human owns the result and confirmed boundaries. Prompt Atlas clarifies, researches, writes and hands off the taskbook, then evaluates the returned result. The Executor (the agent that runs the taskbook independently) owns implementation How. An independent Acceptor (a judge that did not do the work) owns final judgment when independence is required, especially when Executor self-attestation would be gameable.

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

### 2. Ask

When a Human boundary remains, ask the smallest useful set, preferably one round of at most five decisions with options and a recommendation. Do not ask for facts, decomposition, architecture How, command order, or ordinary execution choices.

A delegated default must be marked unconfirmed and include its basis, cost if wrong, and detection or rollback route. Silent defaults look like Human approval; visible defaults preserve Human authority.

### 3. Write the taskbook

Use [execution-compile.md](references/execution-compile.md). Render the final taskbook in its fixed contract order: Contract Header; Delegated Decisions; Boundaries and Authority; Current Reality and Task 0; Execution; Execution Rules and Continuity; Completion and Acceptance. Keep section semantics strict and detail proportional. Put delegated decisions before execution so the Human can inspect and correct compiler-owned defaults before Handoff.

Keep one Goal and one compact taskbook that closes the declared delivery in one execution effort. If it cannot, return to Intent Take to narrow the Human-owned delivery rather than compiling multiple taskbooks or an unbounded graph.

Stable Intent, confirmed boundaries, and protected proof remain binding. The Executor may adapt implementation How and remaining work as evidence changes.

Before Handoff, reserve private acceptance under [completion-trust.md](references/completion-trust.md). Keep it outside the Executor-visible taskbook and, where the runtime permits, outside the Executor context; private checks may vary samples or observation paths, never requirements.

### 4. Handoff

Return the taskbook when the user asks for a prompt, brief, contract, or taskbook. A direct request to complete work grants compile-and-run authority: after `Status: Executable`, the existing runtime continues without another start turn. Prompt Atlas does not supervise live execution.

### 5. Acceptance

When the result returns, rerun the visible acceptance and reserved checks. Bind an independent Acceptor whenever final judgment requires independence—for example, proof remains gameable or incomplete, including because checks intended as private were visible and no other protected judge closes the Goal. An Acceptor is independent only if it did not materially implement the work and evaluates from the authoritative taskbook and accepting environment rather than the Executor's conclusion. Executor evidence is input, not final judgment.

If the required Acceptor or accepting environment is unavailable, stop at `ready for independent acceptance` and return a self-contained acceptance handoff for a non-implementing Acceptor: the authoritative taskbook, Executor result and evidence, visible acceptance, reserved acceptance checks and their visibility, protected judges and baselines, and the required final report—PASS or the exact residual.

Local task PASS is not complete-Goal PASS. Protect judges and baselines and use reverse validation when checks can fail silently. Read [completion-trust.md](references/completion-trust.md) whenever preparing or running private or independent acceptance, or when checks could false-pass.

## Output

Emit one state with enough information for the declared route to continue correctly:

- **`Status: Unresolved Intent`** — the current understanding, the unresolved Goal fork or material consequence, and the smallest remaining Human decision or evidence probe;
- **`Status: Blocked`** — the exact non-intent blocker and the condition that would unblock safe progress;
- **`Status: Executable`** — one grounded autonomous taskbook; when the user asked to complete the work, continue under Handoff after compilation.

`ready for independent acceptance` is an acceptance ceiling after an Executable route, not a fourth compile state.

Prompt Atlas does not add a scheduler, manager daemon, workflow owner, or other control layer.
