---
name: prompt-atlas
description: Two-stage compiler for turning a raw or evolving request into stable intent and a compact executable taskbook. Use when intent, authority, handoff, execution continuity, or trusted completion must survive into downstream work.
---

# Prompt Atlas

Prompt Atlas has two stages:

1. **Intent Take** — close the Goal, Why, authority, boundaries, and success semantics.
2. **Execution Compile** — lower Stable Intent into one compact taskbook or an exact blocker.

Use [contract-anatomy.md](references/contract-anatomy.md) when intent is unclear, [execution-compile.md](references/execution-compile.md) for execution-shape edge cases, and [completion-trust.md](references/completion-trust.md) when proof can false-pass or needs independence.

## Intent Take

Recover the current request from the latest Human authority, still-valid decisions, and relevant evidence. Preserve explicit outcomes and decision-relevant Why. Separate:

- **Human intent** — requested result, confirmed decisions, and boundaries;
- **territory reality** — code, tests, schemas, traces, measurements, and other evidence;
- **inference** — model judgment or recommendation;
- **unknown** — not yet settled.

Evidence may revise facts, feasibility, implementation work, and proof obligations; it may not silently rewrite Human intent.

Ask Human only when proceeding would:

1. change the requested result;
2. cross or relax a confirmed boundary or require high-risk authorization;
3. choose between materially different Goals that evidence cannot resolve.

Investigate accessible facts, leave implementation How to execution, assign execution-only checks to Task 0, and use a visible delegated default only when it preserves intent and boundaries and is reversible or reliably mismatch-detectable.

Stable Intent is reached when one coherent Goal, its Why, confirmed boundaries, material evidence state, trusted success, and delivery semantics are clear, and none of the three Human boundaries remains open.

## Execution Compile

Ground the smallest authoritative surface needed to identify the real workspace, governing specs/tests, material baselines, dependencies, and critical verifiers. Treat documentation, conventions, and command names as claims until evidenced.

Freeze the Goal, Human authority, confirmed boundaries, protected proof surfaces, completion obligations, and handoff mode. The Executor owns implementation How and may revise the remaining work graph inside that envelope.

Every `Status: Executable` taskbook uses six compact sections:

1. **Purpose and Goal**
2. **Grounded State and Task 0**
3. **Decisions, Authority, and Boundaries**
4. **Work Graph and Execution Rules**
5. **Progress, Blockers, and Continuity**
6. **Acceptance and Delivery**

### Task 0

Task 0 is always explicit and completes before material modification. It must:

- bind the repo, branch/worktree, target, and governing surfaces;
- restate the Goal, initial order, and main risk;
- confirm critical commands, baselines, and judging surfaces;
- initialize the graph and repository progress state;
- route disagreement before sunk cost.

Reuse authoritative, fresh compiler evidence. Recheck only what is missing, stale, environment-dependent, disputed, or invalidated.

Task 0 either aligns and starts work, revises the remaining graph inside the frozen envelope, parks a blocked branch while safe work continues, returns `Status: Blocked`, or returns `Status: Unresolved Intent`.

### Execution rules

- Use the smallest graph that preserves real dependencies. A simple task is `Task 0 → Execute with local proof → Global Gate`; add a separate `Verify` node only for integration, cross-result, fresh, hidden, or independent proof.
- Protect tests, verifiers, schemas, baselines, and acceptance criteria unless changing them is explicitly part of the Goal. Skipping, weakening, mocking away, swallowing failures, or editing the judge is not completion.
- Every retry needs a materially different hypothesis or approach. Stop a known-bad approach immediately. After three consecutive failures against the same acceptance condition in the same route, replan, switch branch, roll back, `BLOCK`, or `ESCALATE`.
- Roll back unauthorized regressions below a verified baseline.
- For repository execution, initialize `.scratch/<project>/PROGRESS.md`; create `.scratch/<project>/BLOCKED.md` only when a real blocker appears. Keep both concise, case-local, and uncommitted.
- Local PASS proves only its node. Completion requires the complete Goal and confirmed boundaries to pass the Global Gate. When independent acceptance is required, Executor evidence stops at `ready for independent acceptance`.

Do not compile a taskbook whose Goal cannot reasonably close as one execution effort; split it into independently completable taskbooks instead of relying on unlimited graph growth.

For research or decision work, keep the same sections; use source/probe/synthesis work and judge completion by provenance, counterevidence, residual unknowns, and decision usefulness.

## Output and handoff

Emit one terminal state:

- **`Status: Unresolved Intent`** — the smallest remaining Human decision or unavailable probe;
- **`Status: Blocked`** — the exact non-intent blocker and resolving condition;
- **`Status: Executable`** — one six-section taskbook satisfying the rules above.

Return the taskbook for prompt, brief, contract, or taskbook requests. A direct request to complete work in the available environment supplies compile-and-run authority: after `Status: Executable`, the existing runtime executes it without another Human start turn.

Prompt Atlas compiles the taskbook; it does not own live scheduling, retries, or supervision, and it does not require multiple agents or a new control layer.
