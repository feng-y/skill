---
name: prompt-atlas
description: Compile a raw or evolving request into stable intent and a compact executable taskbook. Use when intent, authority, handoff, continuity, or trusted completion must survive into downstream work.
---

# Prompt Atlas

Two stages:

1. **Intent Take** — close the Goal, Why, authority, boundaries, and success.
2. **Execution Compile** — lower Stable Intent into one taskbook or an exact blocker.

Read [contract-anatomy.md](references/contract-anatomy.md) for intent edge cases, [execution-compile.md](references/execution-compile.md) for execution edge cases, and [completion-trust.md](references/completion-trust.md) when proof can false-pass or needs independence.

## Intent Take

Recover the request from the latest Human authority, still-valid decisions, and evidence. Keep Human intent, territory reality, inference, and unknown distinct. Evidence may revise facts, feasibility, implementation work, and proof obligations; it may not rewrite intent.

Ask Human only when proceeding would:

1. change the requested result;
2. cross or relax a confirmed boundary or require high-risk authorization;
3. choose between materially different Goals that evidence cannot resolve.

Investigate accessible facts; assign execution-only checks to Task 0; leave implementation How to execution. A delegated default must preserve intent and boundaries, be visible, and be reversible or reliably mismatch-detectable.

Intent is stable when one coherent Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery are clear, with no Human boundary open.

## Execution Compile

Ground the real workspace, governing specs/tests, baselines, dependencies, and critical verifiers. Treat documentation and named commands as claims until evidenced.

Freeze Goal, Human authority, confirmed boundaries, protected proof surfaces, completion obligations, and handoff mode. The Executor owns implementation How and may adapt the remaining graph inside that envelope.

Every `Status: Executable` taskbook has six compact sections:

1. Purpose and Goal
2. Grounded State and Task 0
3. Decisions, Authority, and Boundaries
4. Work Graph and Execution Rules
5. Progress, Blockers, and Continuity
6. Acceptance and Delivery

**Task 0 is always explicit and runs before material modification.** It binds repo/worktree/target, restates Goal/order/risk, confirms critical commands/baselines/judges, initializes graph and progress state, then starts, replans inside the frozen envelope, parks a blocked branch, blocks truthfully, or returns to Intent Take. Reuse fresh authoritative evidence; recheck only missing, stale, disputed, environment-dependent, or invalidated facts.

Execution rules:

- Smallest graph first: `Task 0 → Execute with local proof → Global Gate`. Add nodes only for real dependencies, ownership, joins, or proof needs.
- Protect tests, verifiers, schemas, baselines, and acceptance criteria. Skipping, weakening, mocking away, swallowing failures, or editing the judge is not completion.
- Every retry needs a materially different hypothesis or approach. Stop known-bad paths immediately; after three failures against the same acceptance condition in the same route, replan, switch branch, roll back, `BLOCK`, or `ESCALATE`.
- Roll back unauthorized regressions below a verified baseline.
- Repository work initializes `.scratch/<project>/PROGRESS.md`; create `BLOCKED.md` only for a real blocker. Keep both concise, local, and uncommitted.
- Local PASS proves only its node. The Global Gate closes the complete Goal and boundaries. Required independent acceptance cannot be replaced by Executor self-approval.

If one execution effort cannot reasonably close the Goal, split it into independently completable taskbooks instead of growing the graph without bound. For research or decision work, use the same sections and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness.

## Output

Emit one state:

- **`Status: Unresolved Intent`** — smallest remaining Human decision or unavailable probe;
- **`Status: Blocked`** — exact non-intent blocker and resolving condition;
- **`Status: Executable`** — one six-section taskbook.

Return artifacts when asked for a prompt, brief, contract, or taskbook. A direct request to complete work grants compile-and-run authority; the existing runtime continues after `Status: Executable` without another start turn.

Prompt Atlas compiles the taskbook. It does not own live scheduling or supervision and does not require a new control layer or multiple agents.
