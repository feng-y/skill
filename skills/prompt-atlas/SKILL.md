---
name: prompt-atlas
description: Intent-first specialization of autonomous taskbook generation. It routes Unknown explicitly and never turns a vague request or unresolved intent into executable work. Once intent is stable, it compiles a compact taskbook with grounded facts, Task 0, boundaries, progress, stop rules, and trusted acceptance.
---

# Prompt Atlas

Prompt Atlas keeps the stable taskbook discipline and strengthens its front end in two ways:

1. **Unknown is routed explicitly.**
2. **A vague request or vague intent never becomes executable work.**

Use [contract-anatomy.md](references/contract-anatomy.md) when Goal or authority is unclear, [execution-compile.md](references/execution-compile.md) for taskbook shape, and [completion-trust.md](references/completion-trust.md) when proof can false-pass or needs independence.

## Stage 1 — Intent Take

Recover the request from the latest Human authority, still-valid decisions, and relevant evidence. Keep four things distinct:

- **Human intent** — requested result, priorities, approvals, and confirmed boundaries;
- **territory reality** — code, tests, schemas, traces, artifacts, measurements, and other evidence;
- **inference** — model interpretation or recommendation, not Human authority;
- **Unknown** — something whose consequence is not settled yet.

Route Unknown instead of treating every gap as a Human question:

- evidence can settle it now → investigate;
- it depends on the execution environment → put the check in Task 0;
- it is implementation How → let the Executor decide and verify;
- one reasonable reversible choice preserves intent → record a visible delegated default and its rollback route;
- it changes the Goal or a confirmed boundary, or materially different Goals remain plausible → Ask Human;
- a prerequisite is unavailable but independent work remains → park that part in `BLOCKED.md`;
- no safe route remains → return `Status: Blocked` with the exact resolving condition.

A concern, aspiration, hypothesis, comparison, list of questions, or broad request such as “improve”, “clean up”, or “make this better” is not automatically a Goal. Ground enough reality to expose the real choice, but do not invent the choice.

Ask Human only when proceeding would:

1. change the requested result;
2. cross or relax a confirmed boundary or require irreversible/high-risk authority;
3. choose between materially different Goals that evidence cannot resolve.

Intent is stable only when there is one coherent Human-owned Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery. Until then, do **not** emit `Status: Executable`; return `Status: Unresolved Intent` with the current understanding and the smallest useful question or probe.

## Stage 2 — Execution Compile

Enter only after Stable Intent. Research accessible facts yourself: bind the real workspace, find the governing specs/tests, run or verify critical commands, capture relevant baselines, and mark anything still unverified.

Compile one compact autonomous taskbook. Its opening tells the Executor that the taskbook is the execution source, to resume from `PROGRESS.md`, why the work matters, the priority order when requirements conflict, and which statements are hard rules versus guidance.

Then use six sections, in this order:

1. **Delegated decisions** — every unconfirmed default, why it is reasonable, and the cost if wrong.
2. **Boundaries** — allowed write scope, protected judging surfaces, prohibited side work, and irreversible actions.
3. **Current state and Task 0** — evidenced facts, baselines, unverified claims, and the opening checks.
4. **Task N** — ordered work; each task states its result, dependencies, hard constraints, verification command and machine-judgable outcome.
5. **Rules** — progress/blocker behavior, anti-false-green rules, retry/rollback, and repository discipline.
6. **Completion conditions** — complete-Goal evidence, boundary preservation, residuals, delivery, and stop budget.

**Task 0 is always explicit and runs before material change.** It verifies the bound repo/worktree/target, critical commands, baselines, and judges; writes a short opening receipt with Goal, order, largest risk, and disagreement; then starts, revises the remaining plan inside Stable Intent, parks a blocked branch, blocks truthfully, or returns to Intent Take. Reuse fresh authoritative evidence; recheck only missing, stale, disputed, environment-dependent, or invalidated facts.

Keep the taskbook executable without ordinary Human orchestration:

- maintain `.scratch/<project>/PROGRESS.md`; record real blockers and resolving conditions in `.scratch/<project>/BLOCKED.md`;
- use the smallest real dependency graph; give shared mutable surfaces one owner and invalidate downstream evidence when upstream changes affect it;
- protect tests, verifiers, schemas, baselines, and acceptance criteria; skipping, weakening, mocking away, swallowing failures, or editing the judge is not completion;
- use reverse validation when a critical check could fail silently;
- every retry must change the hypothesis or approach; stop known-bad paths immediately; three failures against the same acceptance condition in one route force a replan, branch switch, rollback, `BLOCK`, or `ESCALATE`;
- roll back unauthorized regression below a verified baseline;
- local PASS proves only its task; complete only when the full Goal and confirmed boundaries pass final acceptance;
- the Executor may adapt implementation How and remaining work, but may not rewrite Stable Intent or protected proof.

If one execution effort cannot reasonably close the Goal, split it into independently completable taskbooks. For research or decision work, keep the same discipline but replace implementation metrics with sourced conclusions, counterevidence, reproducibility, residual unknowns, and an explicit research budget.

## Output

Emit one state and stop:

- **`Status: Unresolved Intent`** — current understanding plus the smallest Human decision or probe needed;
- **`Status: Blocked`** — Stable Intent exists, but a non-intent prerequisite prevents safe progress; include the exact resolving condition;
- **`Status: Executable`** — one autonomous taskbook.

Return the artifact when the user asks for a prompt, brief, contract, or taskbook. A direct request to complete work grants compile-and-run authority: after `Status: Executable`, the existing runtime continues without another start turn.

Prompt Atlas compiles; it does not add a scheduler, manager daemon, or new control layer.