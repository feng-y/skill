# Execution Compile

Use this reference when Stage 2 needs more detail on authority boundaries, execution shape, branch closure, Task 0, continuity, or proof topology. Execution Compile consumes Stable Intent IR and emits one executable carrier or a truthful blocker; it does not execute the carrier or own live run state.

## Outcome

Produce the smallest truthful carrier that lets a capable downstream runtime keep making correct progress without using Human interaction as ordinary orchestration. When that is impossible for a non-intent reason, return the exact blocker instead of asking an intent question or pretending the carrier is executable.

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

Use **Task 0** when a critical precondition, carrier-versus-reality disagreement, or likely executor misunderstanding cannot be settled during compile but can be settled safely before material modification. Do not add it to a simple task when no material pre-run uncertainty exists.

Task 0 may:

- verify the target workspace, required files, dependencies, and runtime capability;
- prove that named commands and verifiers run rather than no-op or false-green;
- confirm captured baselines and protected judging surfaces;
- test assumptions on which the execution route depends;
- compare execution reality with the carrier's grounded state and delegated defaults;
- require a brief opening receipt stating the understood Goal, initial route or order when material, main risk, and any disagreement or unverified assumption.

The opening receipt is an alignment signal, not a new approval ceremony or mandatory durable file. It lets a misunderstanding be corrected before sunk cost. Task 0 may expose a true Human decision earlier than ordinary execution would, but it must not postpone a change-intent, change-boundary, or confused-intent decision already visible during compile.

Route Task 0 outcomes as follows:

- preconditions and understanding align → retain the opening receipt and begin material work;
- executor understanding differs but the carrier is clear → correct the understanding from the carrier and continue without Human input;
- facts or initial execution theory differ but intent and confirmed boundaries still hold → revise the route or plan, record the reason, and continue;
- evidence reveals that progress requires changing intent, changing a confirmed boundary, or choosing between materially different Goals → stop affected work and return to Intent Take before modification;
- one precondition cannot be settled but independent safe work remains → preserve the exact disagreement or blocker, park the affected branch, and continue;
- no safe work remains → return `Status: Blocked` with the exact missing condition and resolving path.

**Complete when:** the carrier identifies every material pre-run precondition or disagreement that must be settled, the opening alignment needed to expose misunderstanding, and a non-ambiguous route for each possible result.

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

Close ordinary pre-run choices in this order:

- use authoritative evidence when it determines the answer;
- use Task 0 when the decision depends on execution-only reality or handoff alignment that must be settled before material work;
- leave local How and uncertain execution-theory choices to the runtime;
- use a visible delegated default when one reasonable choice preserves intent and confirmed boundaries.

A delegated default needs a reasonable evidence- or convention-backed choice and must be reversible or reliably mismatch-detectable. Record the selection, basis, visibly unconfirmed status, consequence if wrong, and rollback/replan route.

For **artifact-only**, the default remains reviewable and becomes execution input only when the caller accepts, edits, or forwards the carrier. For **compile-and-run**, it must be safe to execute without another Human turn. An executable task alone does not authorize compile-and-run.

If no pre-run choice is clearly superior but all choices stay inside intent and confirmed boundaries, preserve the decision surface for execution rather than creating another Human gate.

**Complete when:** no foreseeable ordinary execution event requires Human orchestration; only the three Ask Human boundaries remain Human-owned, and material pre-run disagreement has an evidence or Task 0 route.

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

- Task 0 misunderstanding with a clear carrier → correct understanding and continue;
- Task 0 factual or planning mismatch inside the settled envelope → revise the route before material work;
- local mismatch → repair or change local approach;
- local PASS → retain evidence and continue authorized downstream work;
- blocked branch → park it and continue independent safe work;
- evidence invalidates the execution theory → revise remaining work;
- revision triggers change intent, change boundary, or confused intent → return to Intent Take;
- no safe work remains because of a non-intent prerequisite → return `BLOCK` with the exact condition;
- local evidence appears complete → evaluate the complete Goal, not automatic completion.

Continue repair or replan only while the next attempt has a credible path to new evidence or progress and remains within budget. When repeated attempts stop producing evidence gain, no materially different safe approach remains, or the budget is exhausted, exit with truthful `BLOCK` or `ESCALATE` rather than looping ceremonially.

After execution starts, ordinary test failure, command drift, local architecture choice, retry, task decomposition, necessary implementation expansion, or remaining-plan revision are not by themselves HITL.

A local checkpoint judges a bounded result. The **Global Gate** judges the complete Goal. Do not add generic review stages merely because the task is large.

**Complete when:** ordinary uncertainty has a non-Human next action, material disagreement is exposed before sunk cost where possible, the Human boundary is explicit, stalled loops terminate truthfully, and local PASS cannot bypass complete-Goal acceptance.

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
- no blocker prevents a safe first action or truthful continued progress;
- material pre-run preconditions or disagreements are verified or assigned to Task 0 with explicit outcome routing;
- delegated defaults are explicit and safe for the handoff mode;
- ordinary execution uncertainty has a non-Human route;
- required continuity and acceptance can be bound before they are needed;
- the handoff mode is known and compile-and-run has explicit caller authority.

If a required non-intent prerequisite is unavailable and prevents all safe progress, emit `Status: Blocked` instead. A branch-local blocker may remain in an executable carrier when it is parked and independent safe work can continue.

This bar reduces ordinary post-compile HITL. It does not require all unknowns to be eliminated and does not pretend new evidence can never expose a real Human boundary.

## Research and decision work

Use the same direct-loop default. Gather sources, test hypotheses, compare options, and synthesize evidence. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness. A well-supported dead end can be a completed result. Respect explicit budgets; otherwise stop when further work no longer changes the decision materially enough to justify its cost.

## Carrier quality

A fresh runtime should be able to determine, without replaying the conversation:

- why the work exists and what final state is required;
- what is authoritative, verified, inferred, unknown, or visibly delegated;
- what remains Human-owned and what execution may adapt;
- whether Task 0 is required, what opening alignment it needs, and what each result means;
- the first safe action and real dependencies;
- how evidence changes the next action;
- what can continue when one branch blocks;
- when repair/replan should stop;
- what state must survive interruption;
- what evidence closes the complete Goal;
- whether execution starts immediately or the carrier is returned;
- what must be delivered.

Use less structure when these semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, handoff ambiguity, or loss of continuity.
