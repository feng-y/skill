# Execution Compile

Use this reference when Stage 2 needs more detail on fixed Task 0, taskbook structure, work graph, progress/blocker state, retry/stop rules, role boundaries, or completion trust. Execution Compile consumes Stable Intent IR and emits one executable taskbook or a truthful blocker; it does not execute the taskbook or become a runtime controller.

## Outcome

Produce the smallest complete taskbook that lets a capable downstream runtime finish the full Goal with stable opening alignment, bounded failure handling, recoverable state, and trustworthy acceptance.

Keep four logical roles explicit:

- **Human / Intent authority** — owns the requested outcome, confirmed boundaries, and material trade-offs;
- **Prompt Atlas compiler** — grounds reality, closes ordinary pre-run choices, freezes the taskbook and proof obligations, then stops at handoff;
- **Executor** — owns local How, actions, evidence, route adaptation, and progress/blocker updates inside the taskbook;
- **Acceptor** — judges the complete Goal when independent acceptance is required. The Executor may not alter protected judging surfaces or substitute self-approval for Acceptor PASS.

These are responsibility boundaries, not a requirement for a new manager process, scheduler, or multi-agent framework.

## 1. Ground execution reality

Inspect the smallest authoritative surface that determines:

- the actual repository, branch/worktree, target, and governing specifications;
- critical commands, baselines, tests, schemas, and protected verifiers;
- real dependencies, shared mutable surfaces, and ownership conflicts;
- the execution envelope, including access, time, Human availability, and acceptance requirements.

A fact, command, baseline, or verifier is confirmed only when evidence supports it. Documentation, conventions, and command names are claims, not verified state. Run or inspect accessible authoritative surfaces during compile; anything unavailable remains an explicit Task 0 check or blocker.

Do not Ask Human for facts the repository, environment, or another authoritative source can settle.

## 2. Compile fixed Task 0

Every `Status: Executable` taskbook begins with an explicit **Task 0**. It must complete before material modification.

Task 0 always:

1. binds the actual repo, branch/worktree, target, and governing surfaces;
2. restates the Goal, confirmed boundaries, initial execution order, and largest known risk;
3. runs or verifies the critical commands, baselines, and judging surfaces on which execution depends;
4. initializes the work graph and `.scratch/<project>/PROGRESS.md`;
5. routes any disagreement before sunk cost.

For a clear local task, Task 0 may be one compact node and a short opening receipt. For riskier work, include the minimum extra probes, baseline capture, protected-surface checks, or dependency validation needed to avoid doing the wrong work correctly.

Task 0 outcomes are fixed:

- **align** — begin material work;
- **route revision** — facts or initial plan differ, but intent and confirmed boundaries still hold; revise the graph and continue;
- **unresolved intent** — progress requires changing intent or a confirmed boundary, or materially different Goals remain plausible;
- **branch blocker** — record the branch in `BLOCKED.md`, park it, and continue independent safe work;
- **global blocker** — return `Status: Blocked` with the exact missing and resolving conditions.

Task 0 may not defer a Human decision already visible during compile.

## 3. Use the fixed six-section taskbook

Every executable taskbook uses these sections:

### 1. Purpose and Goal

State why the work exists and the complete final state. Preserve user-requested outcomes and the design intent needed for execution judgment.

### 2. Grounded State and Task 0

Separate verified facts, unverified claims, baselines, critical commands, judging surfaces, opening alignment, and Task 0 outcome routes.

### 3. Decisions, Authority, and Boundaries

State:

- Human-owned decisions and confirmed boundaries;
- visible delegated defaults, their basis, consequence if wrong, and rollback/replan route;
- allowed write scope and shared mutable surfaces;
- protected tests, verifiers, schemas, baselines, and acceptance criteria;
- explicit prohibited changes.

Implementation How remains Executor-owned unless the Human made it part of the required result.

### 4. Work Graph and Execution Rules

Every taskbook expresses an execution topology.

A simple task uses a linear graph:

```text
Task 0 → Implement → Verify → Global Gate
```

Expand the graph only when real dependencies, independent ready work, branch parking, shared ownership, evidence invalidation, or joins must be explicit.

Each material node should identify:

- its result;
- readiness dependencies;
- write ownership when shared surfaces exist;
- local evidence;
- what downstream evidence becomes stale if it changes.

The graph may adapt as evidence changes the execution theory, provided Goal, confirmed boundaries, and proof obligations remain unchanged. Record material replans in `PROGRESS.md`.

### 5. Progress, Blockers, and Continuity

For repository execution, Task 0 initializes:

```text
.scratch/<project>/PROGRESS.md
```

Keep it concise. Update after each material checkpoint with:

- Goal reference;
- completed, current, and next work;
- evidence and what it proves;
- stale or invalidated evidence and why;
- parked branches;
- remaining complete-Goal conditions.

When a real blocker appears, create or update:

```text
.scratch/<project>/BLOCKED.md
```

Record:

- blocked branch or whole-task scope;
- attempts made;
- exact missing condition;
- resolving condition;
- independent safe work that can continue.

These files are case-local runtime state, not repository source of truth, and should not be committed or promoted automatically.

### 6. Acceptance and Delivery

State:

- what evidence closes the complete Goal rather than merely showing activity;
- which judging surfaces are protected;
- whether Executor self-acceptance is sufficient;
- whether fresh context, hidden checks, or an independent Acceptor is required;
- what residuals or blockers must be reported;
- deliverables and evidence summary.

## 4. Apply fixed retry and stop rules

The taskbook must include these execution rules:

- every retry uses a materially different hypothesis or approach;
- after the same acceptance check fails three consecutive attempts, stop the current route and choose one: replan, switch branch, roll back, `BLOCK`, or `ESCALATE`;
- do not disguise repeated variants of the same failed approach as a new attempt;
- if results regress below a verified baseline without explicit authorization, roll back the regression and report it truthfully;
- a branch-local blocker does not block independent safe work;
- no safe route or no new evidence-producing approach means truthful exit, not ceremonial looping.

The fixed count is a final mechanical guardrail, not permission to repeat a known-bad approach three times.

## 5. Protect proof and completion

Tests, verifiers, schemas, baselines, and acceptance criteria are protected unless the taskbook explicitly authorizes changing them. Passing by skipping tests, weakening assertions, mocking the object under test, deleting coverage, swallowing failures, or editing the judge is not completion unless the Goal explicitly requires that proof-surface change and preserves equivalent trust.

Use failure-sensitivity checks when a critical verifier could no-op or false-pass: deliberately create a bounded failure, prove the signal fires, restore the state, then run the normal proof.

A local checkpoint proves only its graph node. The **Global Gate** judges the complete Goal and all confirmed boundaries. Local PASS cannot imply task completion.

Use the verdicts:

- `PASS`
- `RETRY`
- `BLOCK`
- `ESCALATE`

A non-PASS verdict routes to evidence-producing work, a materially different plan, a parked branch, a true blocker, or the relevant Human boundary. It cannot be rewritten into completion.

When independent acceptance is required, the taskbook names the Acceptor boundary and private-proof requirement. Before execution begins, the caller/runtime must bind or reserve it, or freeze the completion ceiling at `ready for independent acceptance`. Executor self-approval cannot claim equivalent PASS.

## 6. Handoff modes

Use **artifact-only** when the user asks for a prompt, brief, contract, taskbook, or another handoff artifact. Delegated defaults remain reviewable and become execution input only when the caller accepts, edits, or forwards the taskbook.

A direct request to complete work in the available environment supplies **compile-and-run** authority. After `Status: Executable`, Prompt Atlas stops and the existing runtime executes the taskbook without another Human start turn.

Prompt Atlas compiles the structure and routes; it does not own live scheduling, retries, state mutation, or supervision. Do not introduce a separate control layer merely to run the taskbook.

## Executable readiness

Emit `Status: Executable` only when:

- Goal and confirmed boundaries are stable;
- no foreseeable Ask Human boundary remains open;
- critical facts are evidenced or assigned to Task 0 with truthful routes;
- fixed Task 0 is explicit and precedes material modification;
- all six taskbook sections are present;
- the graph exposes order, dependencies, shared ownership, branch parking, and the Global Gate at the level the task requires;
- `PROGRESS.md` and `BLOCKED.md` behavior is specified;
- retry/stop and baseline-regression rules are explicit;
- protected proof surfaces and acceptance authority are clear;
- handoff mode and delivery are unambiguous.

If a required non-intent prerequisite prevents all safe work, emit `Status: Blocked`. A branch-local blocker may remain in an executable taskbook when it is recorded, parked, and independent safe work can continue.

## Research and decision work

Use the same six-section skeleton. Task 0 verifies source access, scope, decision criteria, and reproducibility. The graph may be source collection → counterevidence → synthesis → decision gate. Progress state records sources, claims, unresolved contradictions, and next probes. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness rather than inventing code-style metrics.

## Information budget

The structure is fixed; detail is not. Keep a section to one line when that preserves its semantics. Retain information only when omission could change execution judgment, authority, routing, verification, recovery, acceptance, or handoff. Do not restate repository facts a capable runtime can inspect immediately unless they anchor one of those decisions.
