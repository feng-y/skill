---
name: prompt-atlas
description: Two-stage compiler for turning a raw or evolving request into an executable agent handoff. Intent Take converges on Stable Intent without inventing Human authority. Execution Compile lowers that intent into a compact execution taskbook with grounded reality, explicit authority, fixed Task 0, a minimal work graph, progress and blocker state, bounded retry, and trusted completion. Use for requirement clarification, task preparation, handoff, or when another workflow needs stable intent or an executable carrier.
---

# Prompt Atlas

Prompt Atlas has two stages:

1. **Intent Take** — establish what should be achieved, why it matters, what is authoritative, and what would count as success.
2. **Execution Compile** — lower Stable Intent into one compact, grounded taskbook that a capable runtime can execute without using Human interaction as ordinary orchestration.

Stable Intent is source semantics, not the first half of the final taskbook. Execution Compile transforms it into an executor-facing representation; it does not append execution prose to an Intent Contract or reinterpret settled intent.

Trust a capable frontier model with routine implementation How and local adaptation. Encode the structure that materially improves execution stability: intent, authority, Task 0, real dependencies, bounded retry, progress/blocker state, and trusted acceptance.

Use Prompt Atlas when intent, authority, handoff, execution uncertainty, continuity, or trusted completion must survive into execution. When the user only needs a direct answer and no execution or handoff semantics must survive, answer directly. Clear local tasks still use the same carrier structure, but each section may collapse to one line.

Use progressive disclosure:

- [contract-anatomy.md](references/contract-anatomy.md) when intent authority, Goal closure, or stability is unclear;
- [execution-compile.md](references/execution-compile.md) when Task 0, execution shape, work graph, progress state, retry/stop rules, or acceptance needs judgment;
- [completion-trust.md](references/completion-trust.md) when completion can false-pass or needs an independent acceptance boundary.

## Stage 1 — Intent Take

Recover the current request from the user's latest authority, still-valid prior decisions, and relevant context. Preserve explicit requested outcomes unless the user supersedes them. Keep the **Why / design intent** when it will help a later executor choose correctly in situations the prompt cannot predict.

Distinguish missing reality from an unclosed or confused Goal. Evidence can resolve facts; it cannot choose between materially different outcomes the Human may want. When the prompt is still a concern, hypothesis, comparison, or active deliberation, ground only enough context to make the real choice clear, then ask the smallest useful question.

Ask Human only when one of these boundaries is reached:

- **change intent** — proceeding would change the requested outcome, accepted behavior, or a design direction the Human made part of the result;
- **change boundary** — proceeding would cross or relax confirmed scope, constraints, approval, protected proof, or require an irreversible/high-risk authorization;
- **confused intent** — materially different Goal interpretations remain plausible after accessible grounding.

Do not ask for facts evidence can settle, necessary implementation expansion inside settled boundaries, architecture How, task decomposition, or ordinary execution choices. Treat unknown as a routing signal: investigate factual unknowns, leave local How to execution, let Execution Compile make safe visible defaults, and Ask Human only at the boundaries above.

A safe delegated default must preserve the current intent and boundaries, have a reasonable evidence- or convention-backed choice, and be reversible or reliably mismatch-detectable. Keep it visibly unconfirmed with its basis, consequence if wrong, and rollback or replan route. It may close execution orchestration; it may not silently change what the Human asked for.

When the Human defines a scope or classification rule but is unsure which concrete entities satisfy it, preserve the rule as authority and derive membership from evidence. Ask again only when the residual classification depends on Human meaning rather than observable reality.

Treat Intent Take as a convergence loop across turns: recover the candidate Goal, confirmed authority, still-valid evidence, and remaining decision surface; reconcile each new Human message or authoritative fact rather than restarting discovery. Rewriting alone cannot promote inference into authority.

Intent is stable when Execution Compile no longer needs to rediscover the problem, complete outcome, confirmed boundaries, or trusted success semantics, and none of the three Ask Human conditions remains. If it is not stable, perform accessible focused grounding first, then return the current understanding plus only the smallest unresolved decision, unavailable probe, or blocker.

When stable, treat the result as **Stable Intent IR** and continue to Stage 2.

## Stage 2 — Execution Compile

Execution Compile ends when it produces one executable taskbook or a truthful non-intent blocker and stops.

Keep four logical roles explicit:

- **Human / Intent authority** — owns the requested result, confirmed boundaries, and material trade-offs;
- **Prompt Atlas compiler** — grounds reality, closes ordinary pre-run choices, freezes the taskbook and proof obligations, then stops at handoff;
- **Executor** — performs local How, gathers evidence, adapts the route, and maintains progress/blocker state inside the taskbook;
- **Acceptor** — judges the complete Goal when independent acceptance is required. The Executor cannot alter protected judging surfaces or claim the Acceptor's PASS.

Roles are responsibility boundaries, not a requirement to create a new controller or always use multiple agents.

Ground enough execution reality to identify the actual workspace, governing specs/tests, material baselines, dependencies, and critical verifiers. Documentation, conventions, and named commands are claims rather than verified state: verify them now when the authoritative surface is accessible; otherwise keep them as explicit Task 0 checks or blockers.

### Fixed Task 0

Every `Status: Executable` taskbook begins with an explicit **Task 0** that must complete before material modification. Task 0 is always visible; its size is proportional.

At minimum it must:

- bind the actual repo, branch/worktree, target, and governing surfaces;
- restate the Goal, confirmed boundaries, initial execution order, and largest known risk;
- run or verify the critical commands, baselines, and judging surfaces on which the route depends;
- initialize the execution graph and progress state;
- route disagreement before sunk cost.

For a clear local task, Task 0 may be one compact item and a short opening receipt. For riskier work, it may include more probes, baseline capture, protected-surface checks, or dependency validation. It must never defer a Human decision already visible during compile.

Task 0 routes are fixed:

- reality and understanding align → begin material work;
- facts or route differ but intent and confirmed boundaries hold → revise the graph and continue;
- progress requires changing intent or a confirmed boundary, or intent becomes confused → return `Status: Unresolved Intent`;
- a non-intent prerequisite blocks all safe work → return `Status: Blocked` with the exact missing condition;
- one branch blocks but independent safe work remains → record it in `BLOCKED.md`, park that branch, and continue.

### Fixed taskbook skeleton

Every executable carrier uses these six sections. Keep each section as short as the task allows, but do not omit the semantics.

1. **Purpose and Goal** — why the work exists and the complete final state.
2. **Grounded State and Task 0** — verified facts, unverified claims, baselines, critical commands, opening alignment, and Task 0 routes.
3. **Decisions, Authority, and Boundaries** — Human-owned decisions, visible delegated defaults, allowed scope, protected surfaces, and prohibited changes.
4. **Work Graph and Execution Rules** — tasks, dependencies, owners for shared mutable surfaces, local checks, retry/stop rules, and the Global Gate. A simple task uses a linear graph: `Task 0 → Implement → Verify → Global Gate`.
5. **Progress, Blockers, and Continuity** — required state files, current/completed/parked work, evidence, blockers, invalidated evidence, and next safe action.
6. **Acceptance and Delivery** — complete-Goal proof, independent acceptance boundary when required, residuals, and deliverables.

Serialize information only when omitting it could change execution judgment, authority, routing, verification, recovery, acceptance, or handoff. The skeleton is stable; implementation How remains task-shaped.

### Execution stability rules

The taskbook must carry these rules:

- before material work, Task 0 verifies the bound target, critical commands/baselines, and judging surfaces;
- tests, verifiers, schemas, baselines, and acceptance criteria are protected unless the taskbook explicitly authorizes changing them;
- every retry must use a materially different hypothesis or approach;
- after the same acceptance check fails three consecutive attempts, the current route must stop: replan, switch branch, roll back, or report `BLOCK`/`ESCALATE`;
- if results regress below the verified baseline without explicit authorization, roll back the regression and report it truthfully;
- local PASS proves only the current node; completion requires the complete Goal to pass the Global Gate;
- required independent acceptance cannot be replaced by Executor self-approval.

### Progress and blocker state

For repository execution, Task 0 initializes:

```text
.scratch/<project>/PROGRESS.md
```

Keep it concise and update it after each material checkpoint with: Goal reference, completed/current/next work, evidence and what it proves, remaining complete-Goal conditions, and any stale evidence.

When a real blocker appears, create or update:

```text
.scratch/<project>/BLOCKED.md
```

Record the blocked branch, attempts made, exact missing condition, resolving condition, and independent safe work that can continue. These files are case-local runtime state, not repository source of truth, and should not be committed or promoted automatically.

### Readiness

`Status: Executable` means:

- the Goal and confirmed boundaries are stable;
- no foreseeable Ask Human boundary remains open;
- Task 0 can begin safely and has complete routes;
- the six-section taskbook is complete;
- the work graph exposes real order, dependencies, shared ownership, and the Global Gate;
- progress/blocker state and retry/stop rules are specified;
- delegated defaults are visible and safe for the handoff mode;
- acceptance, independent acceptance when required, and delivery are unambiguous.

For research or decision work, keep the same skeleton but adapt the graph and acceptance to evidence-bearing source/probe/synthesis work. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness rather than inventing code-style metrics.

## Compilation completion bar

Before emitting a terminal state, confirm:

- no unresolved **change intent**, **change boundary**, or **confused intent** condition remains;
- every critical fact is evidenced or has a truthful Task 0 or blocking route;
- local implementation How has not been promoted into Human-owned intent;
- the six sections, fixed Task 0, graph, progress/blocker rules, and stop conditions are present;
- acceptance closes the complete Goal without relying on a manipulable false-green path;
- handoff authority and artifact-only versus compile-and-run continuation are unambiguous.

## Output and handoff

Emit one terminal state and stop:

- **`Status: Unresolved Intent`** — current understanding plus the smallest probe or Human decision needed because intent would change, a confirmed boundary would change, or intent remains confused.
- **`Status: Blocked`** — Stable Intent is clear, but required evidence, access, capability, or another non-intent prerequisite is unavailable and no safe execution route remains; include the exact blocker and resolving condition.
- **`Status: Executable`** — one six-section executor-facing taskbook satisfying the readiness condition above.

Default to **artifact-only** when the user asks for a prompt, brief, contract, taskbook, or other handoff artifact. When another workflow calls Prompt Atlas, that caller owns whether the taskbook is returned or immediately bound to execution. When the user directly requests completion of work in the available environment, that request supplies compile-and-run authority: `Status: Executable` is the handoff boundary, Prompt Atlas stops, and the existing caller/runtime executes the taskbook without another Human “start” turn.

Prompt Atlas does not own live execution state, scheduling, retries, or supervision. It compiles the taskbook, state requirements, and decision routes; the existing runtime performs them. Do not introduce a separate controller merely to execute these rules.

In artifact-only mode, delegated defaults remain visibly reviewable and become execution input only when the caller accepts, edits, or forwards the taskbook.

When independent acceptance is required, the taskbook must state the accepting boundary and private-proof requirement. Before execution begins, the caller/runtime must either bind or reserve that boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter cannot claim an equivalent PASS.

For `Status: Executable`, do not prepend the Stable Intent IR or emit a second execution variant. Keep the six sections concise, but never compress away a requested outcome, authority distinction, material dependency, Task 0 check, protected proof surface, graph edge, stop rule, progress/blocker requirement, recovery requirement, handoff requirement, or trusted proof obligation.
