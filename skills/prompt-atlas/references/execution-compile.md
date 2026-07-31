# Execution Compile

Use this reference when Stage 2 needs more detail on authority boundaries, execution shape, branch closure, continuity, or proof topology. Execution Compile consumes Stable Intent IR and emits one executable carrier; it does not execute the carrier or own live run state.

## Outcome

Produce the smallest truthful carrier that lets a capable downstream runtime keep making correct progress without using Human interaction as ordinary orchestration.

Use two lenses:

- **Authority** — what remains Human-owned, what the compiler may decide visibly on the Human's behalf, what execution may adapt inside Stable Intent, and what boundary judges completion when separation is required.
- **Control protocol** — the minimum action loop, dependencies, evidence routes, continuity, and acceptance needed for this task.

These are design lenses, not a runtime framework. Prefer a simple executor with clear boundaries. Add graph structure, durable state, separate control, or independent acceptance only when the task actually needs them.

## 1. Ground execution reality

Inspect the smallest authoritative surface that can determine:

- the actual target or workspace;
- governing specs, tests, schemas, and protected verifiers;
- material baselines and critical commands;
- real work dependencies and shared mutable surfaces;
- the execution envelope, including Human availability and continuity limits.

A fact, command, baseline, or verifier is confirmed only when evidence supports it. If a prerequisite is unverified, make its check an initial execution action when safe work can continue; otherwise expose the true blocker.

Treat unknown as a routing signal:

- factual unknown → inspect or probe;
- local implementation unknown → let execution choose or experiment;
- execution-theory unknown → learn and replan inside Stable Intent;
- safely delegable pre-run choice → compiler selects a visible default;
- non-delegable Human-owned uncertainty → ask;
- inaccessible required evidence or authority → block truthfully after safe work is exhausted.

Grounding may change candidate work boundaries, dependencies, proof topology, or continuity needs. It may not change Stable Intent.

**Complete when:** every carrier-shaping factual claim is verified, visibly unverified, or converted into an initial probe or exact blocker.

## 2. Close pre-run decisions

Keep three default responsibilities clear:

- **Human / Intent authority** — owns Goal, accepted behavior, Human-owned scope or priority, approval, and protected proof rules.
- **Prompt Atlas compiler** — grounds current reality, asks only for non-delegable decisions, closes safely delegable choices visibly, and compiles the carrier; it stops at handoff.
- **Execution runtime** — owns local How, actions, evidence, and evidence-driven adaptation of the remaining plan inside Stable Intent and protected boundaries.

Completion may be judged by the execution runtime for narrow low-risk work. Use a separate or fresh **acceptance boundary** only when governing rules or proof risk require independence.

Do not create a separate control owner merely because execution may revise a plan or Graph. Add one only when the actual environment requires protected centralized control—for example, conflicting concurrent writers, high-risk shared state, or a governing approval boundary. Even then, describe the needed boundary rather than prescribing an agent topology.

Close a branch before execution when different answers materially change the Goal-preserving execution envelope, scope authority, protected proof, irreversible action, or another decision that the runtime cannot safely infer or reverse. Use Stable Intent, governing constraints, and evidence first.

A choice is safely delegable when all of the following hold:

- the Goal and Human-owned boundaries are already closed;
- the choice does not change accepted behavior, approval, protected proof, or an irreversible/high-risk authorization;
- evidence, repository convention, or stated priorities support a reasonable preferred choice;
- the choice is reversible or a mismatch can be detected early enough to limit harm;
- the consequence of a wrong choice is bounded and reportable.

Record each delegated decision with:

- the selected default;
- its basis;
- its visibly unconfirmed status;
- the consequence if wrong;
- the mismatch signal and rollback or replan route.

For **artifact-only**, a broader visible recommended default may be carried because the caller can review or change it before execution. For **compile-and-run**, the default itself must be safe to execute without another Human turn. An executable task alone does not authorize compile-and-run.

Batch the remaining non-delegable Human-owned choices into the smallest pre-run decision surface. If a material branch cannot be closed by evidence, execution freedom, or a safe delegated default, return `Status: Execution Decision`. If evidence exposes a new Human-owned Goal/boundary choice or shows that the Goal cannot be preserved inside confirmed boundaries, return `Status: Unresolved Intent`.

**Complete when:** no foreseeable ordinary execution event requires Human orchestration; delegated decisions are explicit and safe for the handoff mode; local reversible How and evidence-driven replanning remain execution-owned.

## 3. Compile the minimum execution shape

Start with a **direct loop**:

```text
act → observe → evaluate → continue / repair / replan / exit
```

For a simple task, one current action, its local check, and the complete-Goal gate are enough.

Introduce Task / Issue nodes and Graph edges only when real dependencies, independent ready work, shared ownership, evidence flow, or recovery need to be explicit. A node is a bounded outcome with only the Context, Dependencies, Boundaries, and Verify evidence needed to judge it locally. An edge exists only when it changes readiness, proof, invalidation, or routing—not to serialize prose.

For parallel work, prefer disjoint write domains. Assign one owner per shared mutable surface, make joins explicit, and invalidate downstream evidence when upstream changes affect what it proved.

Keep the initial structure small. The execution runtime may add, remove, split, merge, or reroute remaining work as evidence changes the execution theory, provided Stable Intent, protected boundaries, and completion semantics remain unchanged. Trusted completed work remains complete unless new evidence invalidates it.

**Complete when:** the runtime can identify the first safe evidence-producing action, real dependencies are represented only where needed, and the complete Goal remains reachable.

## 4. Preserve autonomous progress

Make only the material routes explicit:

- local mismatch → repair or change local approach;
- local PASS → retain the evidence and continue authorized downstream work;
- blocked branch → park it and continue independent safe work;
- evidence invalidates the execution theory → revise the remaining plan or Graph;
- revision would change Human-owned Intent, approval, or protected proof → return to Intent Take;
- local evidence appears complete → evaluate the complete Goal, not automatic completion.

Continue a repair or replan only while the next attempt has a credible path to new evidence or progress and remains within the available budget. When repeated attempts stop producing evidence gain, no materially different safe approach remains, or the budget is exhausted, exit with the truthful `BLOCK` or `ESCALATE` route instead of looping ceremonially.

After execution starts, Human interaction is reserved for genuinely new authority boundaries:

- new evidence changes Human-owned Intent or approval;
- an irreversible or high-risk action requires authorization;
- no safe work remains and progress depends on Human authority.

Test failure, command drift, local architecture choice, retry, task decomposition, or remaining-plan revision inside Stable Intent are not by themselves HITL.

A local checkpoint judges a bounded result. The **Global Gate** judges the complete Goal. Do not add generic review stages merely because the task is large; add proof structure only when the Goal, mutable surface, or governing verifier requires it.

**Complete when:** ordinary uncertainty has a non-Human next action, a genuine authority crossing has a Human route, stalled loops terminate truthfully, and local PASS cannot bypass complete-Goal acceptance.

## 5. Compile continuity only when needed

Continuity is required when work may outlive one context, pause on external or Human input, span independent actors, or invalidate earlier evidence.

Require only enough semantic state to resume without replaying the conversation:

- Goal and still-binding decisions by reference;
- current execution structure and ready/active/completed/parked work;
- completed evidence and what it proves;
- stale or invalidated evidence and why;
- active blockers and exact missing input;
- accepted replans or pending authority decisions;
- remaining complete-Goal conditions;
- next safe work.

For long-running or cross-context repository work, default to a project-specific workspace:

```text
.scratch/<project>/IMPLEMENTATION_NOTES.md
```

The downstream runtime initializes and maintains it. The file is case-local runtime material, not repository source of truth, and should not be committed or promoted automatically.

Use one concise file by default. Add per-agent or append-only receipts only when real concurrency, independent acceptance, or interruption risk makes a single writer unsafe. Keep private acceptance cases outside Executor-visible state.

A useful shape is:

```markdown
# Implementation Notes

## Goal and boundaries
## Current work and progress
## Evidence and invalidation
## Decisions and blockers
## Remaining acceptance
## Next work
```

Use less structure when the same semantics remain clear.

**Complete when:** a fresh runtime can identify the truthful current state and next safe action without reconstructing the run from chat history.

## 6. Close acceptance, delivery, and handoff

The complete-Goal gate must state:

- what evidence closes the Goal rather than merely showing activity;
- which judging surfaces are protected from modification;
- whether execution self-acceptance is sufficient;
- when fresh context, hidden checks, or independent acceptance is required;
- what residuals or blockers must be reported rather than hidden.

Use the existing verdicts:

- `PASS`
- `RETRY`
- `BLOCK`
- `ESCALATE`

A non-PASS verdict routes to more evidence-producing work, replanning, a true blocker, or the relevant authority boundary. It cannot be rewritten into completion.

When independent acceptance is required, compile the accepting boundary and private-proof retention requirement. Before execution begins, the caller/runtime must either bind or reserve that boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter cannot claim an equivalent PASS.

Define Delivery separately from proof: artifacts, evidence summary, residuals, and next actions.

Default to **artifact-only**. Use **compile-and-run** only when the caller explicitly requests or owns execution continuation and an execution runtime is available. After `Status: Executable`, Prompt Atlas stops and that caller immediately uses the carrier as the execution source without another Human “start” turn.

In compile-and-run mode, the same physical agent may compile and execute sequentially, but execution follows the carrier rather than continuing compilation by improvisation.

**Complete when:** the completion boundary is trustworthy, any required independent acceptance is bound/reserved or honestly capped, delegated decisions are safe for the selected mode, and the caller knows whether to return the carrier or start execution.

## Executable readiness

Emit `Status: Executable` only when:

- Stable Intent remains valid;
- every foreseeable non-delegable Human-owned decision exposed by current intent and evidence is closed;
- every delegated default is explicit and safe for the selected handoff mode;
- every ordinary execution uncertainty has a non-Human route;
- the first safe evidence-producing action is clear;
- required continuity can be bound before it is needed;
- required independent acceptance is bound/reserved, or completion is explicitly capped at `ready for independent acceptance`;
- the handoff mode is known and compile-and-run has explicit caller authority.

This bar reduces ordinary post-compile HITL. It does not require all unknowns to be eliminated and does not pretend new runtime evidence can never expose a new authority boundary.

## Research and decision work

Use the same direct-loop default. Gather sources, test hypotheses, compare options, and synthesize evidence. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness. A well-supported dead end can be a completed result. Respect explicit budgets; otherwise stop when further work no longer changes the decision materially enough to justify its cost.

## Carrier quality

A fresh downstream runtime should be able to determine, without replaying the conversation:

- why the work exists and what final state is required;
- what is authoritative, verified, inferred, unknown, or visibly delegated;
- what remains Human-owned and what execution may adapt;
- the first safe action and any real dependencies;
- how evidence changes the next action;
- what can continue when one branch blocks;
- when continued repair/replan should stop;
- what state must survive interruption;
- what evidence closes the complete Goal;
- whether execution starts immediately or the carrier is returned;
- what must be delivered.

Use less structure when these semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, handoff ambiguity, or loss of continuity.
