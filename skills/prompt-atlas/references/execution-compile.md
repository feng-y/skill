# Execution Compile

Use this reference when Stage 2 needs more detail on authority boundaries, execution shape, branch closure, Task 0, continuity, or proof topology. Execution Compile consumes Stable Intent IR and emits one executable carrier; it does not execute the carrier or own live run state.

## Outcome

Produce the smallest truthful carrier that lets a capable downstream runtime keep making correct progress without using Human interaction as ordinary orchestration.

Use two lenses:

- **Authority** — what remains Human-owned, what the compiler may decide visibly, what execution may adapt, and what boundary judges completion when separation is required.
- **Control protocol** — the minimum action loop, dependencies, evidence routes, continuity, and acceptance needed for this task.

These are design lenses, not a runtime framework. Prefer one capable executor with clear boundaries. Add graph structure, durable state, separate control, or independent acceptance only when the task actually needs them.

## 1. Ground execution reality

Inspect the smallest authoritative surface that can determine:

- the actual target or workspace;
- governing specs, tests, schemas, and protected verifiers;
- material baselines and critical commands;
- real work dependencies and shared mutable surfaces;
- the execution envelope, including Human availability and continuity limits.

A fact, command, baseline, or verifier is confirmed only when evidence supports it. Do not Ask Human for facts the repository, environment, or another authoritative source can settle.

### Task 0

Use **Task 0** only when a carrier-shaping fact cannot be verified during compile but can be checked safely before modification. Typical checks include:

- target workspace and required files exist;
- named commands run rather than no-op or false-green;
- captured baselines still match;
- governing verifier and protected surfaces are intact;
- assumed dependency or runtime capability is available.

Task 0 is an execution preflight, not deferred intent clarification. Its result routes as follows:

- fact matches → continue;
- fact differs but intent and confirmed boundaries still hold → revise the plan and continue;
- fact differs and would require changing intent or a confirmed boundary, or reveals confused intent → return to Intent Take;
- verification is unavailable → park the affected branch and continue independent safe work, or return the exact blocker when none remains.

**Complete when:** every carrier-shaping factual claim is verified, visibly unverified, converted into Task 0, or exposed as an exact blocker.

## 2. Close pre-run decisions

Keep three default responsibilities clear:

- **Human / Intent authority** — owns the requested result and confirmed boundaries.
- **Prompt Atlas compiler** — grounds reality, asks only at the Human boundary, makes safe delegated choices visibly, and compiles the carrier; it stops at handoff.
- **Execution runtime** — owns local How, actions, evidence, and evidence-driven adaptation inside intent and confirmed boundaries.

Ask Human only when:

1. proceeding would **change intent**;
2. proceeding would **change a confirmed boundary** or require irreversible/high-risk authorization;
3. the current request still **confuses materially different intents** after accessible grounding.

Do not ask for necessary implementation expansion, dependency discovery, task decomposition, local architecture, command order, or ordinary execution choices when intent and boundaries remain intact.

Before returning `Status: Execution Decision`, try in order:

- authoritative evidence;
- execution-owned How;
- a visible delegated default that preserves intent and confirmed boundaries.

A delegated default needs a reasonable evidence- or convention-backed choice and must be reversible or reliably mismatch-detectable. Record the selection, basis, visibly unconfirmed status, consequence if wrong, and rollback/replan route.

For **artifact-only**, the default remains reviewable and becomes execution input only when the caller accepts, edits, or forwards the carrier. For **compile-and-run**, it must be safe to execute without another Human turn. An executable task alone does not authorize compile-and-run.

**Complete when:** no foreseeable ordinary execution event requires Human orchestration; only the three Ask Human boundaries remain Human-owned.

## 3. Compile the minimum execution shape

Start with a direct loop:

```text
act → observe → evaluate → continue / repair / replan / exit
```

For a simple task, one current action, its local check, and the complete-Goal gate are enough.

Introduce Task / Issue nodes and edges only when real dependencies, independent ready work, shared ownership, evidence flow, or recovery need to be explicit. An edge exists only when it changes readiness, proof, invalidation, or routing—not to serialize prose.

For parallel work, prefer disjoint write domains. Assign one owner per shared mutable surface, make joins explicit, and invalidate downstream evidence when upstream changes affect what it proved.

Keep the initial structure small. Execution may add, remove, split, merge, or reroute remaining work as evidence changes the execution theory, provided intent, confirmed boundaries, and completion obligations remain unchanged.

**Complete when:** the runtime can identify the first safe evidence-producing action, real dependencies are represented only where needed, and the complete Goal remains reachable.

## 4. Preserve autonomous progress

Make only material routes explicit:

- local mismatch → repair or change local approach;
- local PASS → retain evidence and continue authorized downstream work;
- blocked branch → park it and continue independent safe work;
- evidence invalidates the execution theory → revise remaining work;
- revision triggers change intent, change boundary, or confused intent → return to Intent Take;
- local evidence appears complete → evaluate the complete Goal, not automatic completion.

Continue repair or replan only while the next attempt has a credible path to new evidence or progress and remains within budget. When repeated attempts stop producing evidence gain, no materially different safe approach remains, or the budget is exhausted, exit with truthful `BLOCK` or `ESCALATE` rather than looping ceremonially.

After execution starts, ordinary test failure, command drift, local architecture choice, retry, task decomposition, necessary implementation expansion, or remaining-plan revision are not by themselves HITL.

A local checkpoint judges a bounded result. The **Global Gate** judges the complete Goal. Do not add generic review stages merely because the task is large.

**Complete when:** ordinary uncertainty has a non-Human next action, the Human boundary is explicit, stalled loops terminate truthfully, and local PASS cannot bypass complete-Goal acceptance.

## 5. Compile continuity only when needed

Continuity is required when work may outlive one context, pause on external or Human input, span independent actors, or invalidate earlier evidence.

Require only enough semantic state to resume without replaying the conversation:

- Goal and still-binding decisions by reference;
- current ready/active/completed/parked work;
- completed evidence and what it proves;
- stale or invalidated evidence and why;
- active blockers and exact missing input;
- accepted replans or pending Human decisions;
- remaining complete-Goal conditions;
- next safe work.

For long-running or cross-context repository work, default to:

```text
.scratch/<project>/IMPLEMENTATION_NOTES.md
```

The downstream runtime initializes and maintains it. The file is case-local runtime material, not repository source of truth, and should not be committed or promoted automatically.

Use one concise file by default. Add per-agent or append-only receipts only when real concurrency, independent acceptance, or interruption risk makes a single writer unsafe. Keep private acceptance cases outside Executor-visible state.

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

A non-PASS verdict routes to more evidence-producing work, replanning, a true blocker, or the relevant Human boundary. It cannot be rewritten into completion.

When independent acceptance is required, compile the accepting boundary and private-proof retention requirement. Before execution begins, the caller/runtime must either bind or reserve that boundary, or explicitly freeze the run's completion ceiling at `ready for independent acceptance`. The latter cannot claim an equivalent PASS.

Define Delivery separately from proof: artifacts, evidence summary, residuals, and next actions.

Default to **artifact-only**. Use **compile-and-run** only when the caller explicitly requests or owns execution continuation and a runtime is available. After `Status: Executable`, Prompt Atlas stops and that caller immediately uses the carrier as the execution source without another Human “start” turn.

**Complete when:** the completion boundary is trustworthy, required independent acceptance is bound/reserved or honestly capped, delegated defaults are safe for the mode, and the caller knows whether to return the carrier or start execution.

## Executable readiness

Emit `Status: Executable` only when:

- the Goal is clear and intent remains unchanged;
- no foreseeable Ask Human boundary remains open;
- carrier-shaping facts are verified, assigned to Task 0, or truthfully blocked;
- delegated defaults are explicit and safe for the handoff mode;
- ordinary execution uncertainty has a non-Human route;
- the first safe evidence-producing action is clear;
- required continuity and acceptance can be bound before they are needed;
- the handoff mode is known and compile-and-run has explicit caller authority.

This bar reduces ordinary post-compile HITL. It does not require all unknowns to be eliminated and does not pretend new evidence can never expose a real Human boundary.

## Research and decision work

Use the same direct-loop default. Gather sources, test hypotheses, compare options, and synthesize evidence. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness. A well-supported dead end can be a completed result. Respect explicit budgets; otherwise stop when further work no longer changes the decision materially enough to justify its cost.

## Carrier quality

A fresh runtime should be able to determine, without replaying the conversation:

- why the work exists and what final state is required;
- what is authoritative, verified, inferred, unknown, or visibly delegated;
- what remains Human-owned and what execution may adapt;
- whether Task 0 is required and what its outcomes mean;
- the first safe action and real dependencies;
- how evidence changes the next action;
- what can continue when one branch blocks;
- when repair/replan should stop;
- what state must survive interruption;
- what evidence closes the complete Goal;
- whether execution starts immediately or the carrier is returned;
- what must be delivered.

Use less structure when these semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, handoff ambiguity, or loss of continuity.
