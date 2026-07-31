# Execution Compile

Use this reference when Stage 2 needs more detail on authority boundaries, graph shape, loop boundaries, branch closure, continuity, or proof topology. Execution Compile consumes Stable Intent IR and emits one executable carrier; it does not execute the carrier or own live run state.

## Outcome

Produce the smallest truthful carrier that lets a capable downstream runtime keep making correct progress without using Human interaction as ordinary orchestration.

Use two lenses throughout:

- **Authority** — who may decide or change Intent, material execution structure, node-local How, and final acceptance.
- **Control protocol** — how Graph, Loops, routes/gates, continuity, and acceptance govern execution.

These are design lenses, not a runtime framework. Express them through task-specific roles, boundaries, nodes, routes, and proof rather than an abstract control architecture.

## 1. Ground execution reality

Inspect the smallest authoritative surface that can determine:

- the actual target or workspace;
- governing specs, tests, schemas, and protected verifiers;
- material baselines and critical commands;
- real work dependencies and shared mutable surfaces;
- the execution envelope, including Human availability and continuity limits.

A fact, command, baseline, or verifier is confirmed only when evidence supports it. If a prerequisite is unverified, make its check initial ready work when safe progress can continue; otherwise expose the true blocker.

Grounding may change candidate node boundaries, dependencies, proof topology, or runtime requirements. It may not change Stable Intent.

**Complete when:** every carrier-shaping factual claim is verified, visibly unverified, or converted into an initial check or blocker.

## 2. Close authority and material branches

Keep four powers distinct when the task needs them:

- **Intent authority** — changes Goal, accepted behavior, Human-owned scope/priority, approval, or protected proof.
- **Control owner** — commits material changes to the remaining Graph, ownership, proof topology, or recovery/acceptance route while Stable Intent remains valid.
- **Executor** — chooses node-local How, performs actions, and produces evidence inside current boundaries.
- **Acceptor** — judges the Global Gate, independently when the proof requires it.

One runtime may carry several powers for low-risk work. Colocation does not grant extra authority: the Executor cannot silently weaken the Goal or proof, and a control owner cannot promote a non-PASS acceptance verdict into completion.

Close a branch before execution when different answers materially change node outcomes, dependencies, ownership, proof path, runtime envelope, recovery, or the Global Gate. Use Stable Intent, governing constraints, and evidence first. If materially different carriers remain equally acceptable, return `Status: Execution Decision` unless the caller explicitly permits a visible, reversible, reliably mismatch-detectable default.

If evidence exposes a new Human-owned choice or shows that the Goal cannot be preserved inside confirmed boundaries, return `Status: Unresolved Intent`.

**Complete when:** every material branch is closed, explicitly defaulted under the allowed rule, or surfaced in a terminal state; local reversible How remains executor-owned.

## 3. Build the Graph

A **Task / Issue node** is a bounded outcome that can be started, observed, and locally judged. Give it only:

- **Outcome** — the state it establishes;
- **Context** — facts or rich references needed for the work;
- **Dependencies** — upstream results it actually consumes;
- **Boundaries** — applicable authority and safety invariants;
- **Verify** — task-specific evidence that makes it locally done.

Edges represent real dependency, evidence, invalidation, or required routing flow—not prose order. Use stable identities only when dependencies, recovery, parallel ownership, or evidence references need them. A one-node task is a valid Graph.

For parallel branches, prefer disjoint write domains. Assign one owner per shared mutable surface, make joins explicit, and invalidate downstream proof when an upstream change makes it stale.

Keep the initial Graph small. Evidence may justify adding, removing, splitting, merging, or rerouting remaining work, but material changes require the control owner. Completed work remains trusted unless new evidence invalidates what it proved.

**Complete when:** every node has a locally judgeable Outcome, every edge changes readiness or proof, ownership is unambiguous where writes overlap, and the Global Gate is reachable from the remaining work.

## 4. Attach Loops, routes, and gates

Keep routine local convergence inside each node:

```text
act → observe → evaluate → continue / repair / exit
```

The Loop may change local How, rerun proof, or try another local approach. It does not silently change the node Outcome, dependencies, protected proof, or accepting authority.

Make material routes explicit:

- local mismatch → remain in the node Loop and repair or change local approach;
- local PASS → complete the node and unlock authorized downstream work;
- blocked node → park the affected branch and continue independent ready work;
- evidence invalidates the execution theory → propose or commit a remaining-Graph revision through the control owner;
- evidence conflicts with Human-owned Intent → return to Intent Take;
- complete local evidence → Global Gate, not direct completion.

A **checkpoint** judges a node. The **Global Gate** judges the complete Goal. Do not add generic review stages merely because the task is large; add proof structure only when the Goal, mutable surface, or governing verifier requires it.

**Complete when:** every material failure or verdict has one truthful next route, Loop exits are locally observable, and local PASS cannot bypass the Global Gate.

## 5. Compile continuity only when needed

Continuity is required when work may outlive one context, pause on Human input, span independent actors, or invalidate earlier evidence.

Require enough semantic state to resume without replaying the conversation:

- Goal and still-binding decisions by reference;
- current Graph and ready/active/completed/parked work;
- completed evidence and what each item proves;
- stale or invalidated evidence and why;
- active blockers and exact missing input;
- accepted Graph changes or pending control decisions;
- remaining Global Gate conditions;
- next safe work.

For long-running or cross-context repository work, default to a project-specific workspace:

```text
.scratch/<project>/IMPLEMENTATION_NOTES.md
```

Use a stable project/effort slug. The downstream runtime initializes and maintains the file when execution begins; Prompt Atlas only compiles the continuity requirement. The file is case-local runtime material, not repository source of truth, and should not be committed or promoted automatically.

Use one concise file by default. Add per-agent or append-only receipts only when real concurrency, independent acceptance, or interruption risk makes a single writer unsafe. Keep private or hidden acceptance cases outside Executor-visible state.

A useful implementation-notes shape is:

```markdown
# Implementation Notes

## Goal and authority
## Current graph and progress
## Evidence and invalidation
## Decisions and blockers
## Remaining acceptance
## Next work
```

Use less structure when the same semantics remain clear.

**Complete when:** a fresh runtime can identify the current truthful state and next safe action without reconstructing the run from chat history.

## 6. Close acceptance and delivery

The Global Gate carries the proof obligations for the complete Goal. Make explicit:

- what evidence closes the Goal rather than merely showing activity;
- which surfaces are protected from modification;
- who may judge completion;
- when fresh context, hidden checks, or an independent Acceptor is required;
- what residuals or blockers must be reported rather than hidden.

Use the existing verdicts:

- `PASS`
- `RETRY`
- `BLOCK`
- `ESCALATE`

A non-PASS verdict routes to more evidence-producing work, a controlled Graph revision, a blocker, or the relevant authority boundary. It cannot be rewritten into completion by the Executor or control owner.

Define Delivery separately from proof: what artifacts, evidence summary, residuals, and next actions the caller receives.

**Complete when:** an authorized judge can distinguish PASS from false completion using the carrier alone, and the delivery preserves the evidence and residuals needed to trust that judgment.

## Research and decision work

Use the same process with evidence-bearing probe/source/synthesis nodes. Judge completion by provenance, counterevidence, residual unknowns, reproducibility, and decision usefulness. A well-supported dead end can be a completed result. Respect explicit time/source budgets; otherwise stop when further work no longer changes the decision materially enough to justify its cost.

## Carrier quality

A fresh downstream runtime should be able to determine, without replaying the conversation:

- why the work exists and what final state is required;
- what is authoritative, verified, inferred, or unknown;
- who controls Intent, local How, material Graph change, and acceptance;
- what work is ready and which dependencies are real;
- how each node converges and how material evidence routes control;
- what can continue when one branch blocks;
- what state must survive interruption;
- what evidence closes important nodes and the complete Goal;
- what must be delivered.

Use less structure when these semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, authority confusion, or loss of continuity.
