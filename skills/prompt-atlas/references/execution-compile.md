# Execution Compile

Use this reference when Stage 2 graph shape, branch closure, AFK continuity, or HITL placement is not obvious. Execution Compile consumes Stable Intent IR and emits one executable carrier. It does not reopen intent and does not execute the graph.

## Objective

Compile the smallest structure that lets a capable executor keep making correct progress without using Human interaction as orchestration.

Optimize for:

- longer autonomous execution span;
- real parallelism where independence exists;
- local verification and local recovery;
- preservation of Goal, Why, authority, and proof integrity;
- HITL only where a material execution branch cannot be closed safely from settled intent or evidence.

Do not optimize for task count, field count, a visually rich DAG, or maximum up-front planning.

## Lowering, not append

Stable Intent IR is source semantics. The executable carrier is a lower-level representation.

Execution Compile should transform intent semantics into the places where they constrain runtime judgment:

- Why / design intent becomes a judgment anchor;
- Goal becomes the global end condition;
- grounded reality becomes execution State and node context;
- Human decisions and hard constraints become graph invariants;
- material execution decisions become closed branches with their basis;
- success and proof semantics become local checks and the Global Gate;
- output requirements become Delivery.

Do not print a complete Intent Contract and then add Tasks, Graph, or Loop below it. Avoid duplicate Goal, constraint, or success authorities.

## Decision closure

Before materializing the graph, look for choices that would otherwise make an executor stop mid-run because different answers produce materially different execution structures.

A branch is material when choosing differently changes one or more of:

- Task / Issue boundaries;
- real dependencies or ordering;
- verification ownership or the acceptance path;
- implementation scope;
- architecture direction or responsibility placement;
- the shape of the Global Gate.

Close such branches from settled intent, governing constraints, and authoritative evidence when possible. Record the basis so a later executor does not reopen a settled choice.

Use pre-execution HITL only when materially different graphs remain compatible with the stable intent and available evidence does not select among them. This is not limited to choices with obvious risk or a universally better answer; the point is to remove a branch that would otherwise interrupt AFK execution.

Do not escalate local How: helper naming, small code organization, exact patch order, reversible implementation details, or another choice whose alternatives do not materially change the graph remain executor-owned.

## Graph construction

A graph is orchestration, not a decorative task list.

### Node

A Task / Issue node is a bounded unit that can be started, progressed, observed, and locally judged. Give it only what it needs:

- **Outcome** — what state this node should establish;
- **Context** — only facts or references needed for this work;
- **Dependencies** — upstream results it actually consumes;
- **Boundaries** — applicable invariants or scope limits;
- **Verify** — evidence that makes this node locally done.

A node may be implementation, migration, research, probe, synthesis, cleanup, or another bounded work unit. Do not decompose into mechanical code-edit steps unless those steps have independent dependency or verification meaning.

### Edge

Create an edge only for real dependency, evidence flow, or a required gate. If B does not consume A's result, do not serialize B after A merely because prose would say “then.” Independent work may fan out.

### Checkpoint

A local checkpoint decides whether a node is done or routes it back for repair. Local PASS unlocks downstream work; local FAIL should normally stay inside the node loop.

### Global Gate

The Global Gate evaluates the complete Goal, not task count. Every required node being locally done is not sufficient when the overall behavioral, structural, or proof obligation is still unmet.

### Human Gate

A Human Gate exists only when new evidence exposes a material branch that cannot be closed from settled intent, governing constraints, or authoritative evidence. Do not put a Human Gate between ordinary tasks.

## Small and lazy graph

Compile only graph structure that is useful before execution starts. A simple task may be:

`Work → Verify → Global Gate`

A larger task may expose several independent nodes, joins, or a verification branch. Do not predict an entire implementation when later evidence can determine the remaining structure more accurately.

The runtime may add, remove, split, merge, or reroute remaining nodes when evidence changes the current execution theory. Preserve trustworthy completed work unless new evidence invalidates it.

Graph complexity should follow real dependency, coordination, proof, isolation, or recovery need—not task size or a generic “complex task” threshold.

## Loop semantics

Each ready node runs a local evidence-driven loop:

`Act → Observe → Evaluate → Next`

When local verification fails, first diagnose, change How, gather missing evidence, or locally replan. Failure, difficulty, or an unexpected repo fact is not by itself a reason for HITL.

The graph runtime repeatedly:

1. selects ready work;
2. executes the node loop;
3. records resulting evidence and state;
4. updates the remaining graph when evidence invalidates current assumptions;
5. evaluates whether the Global Gate is satisfied.

Continue while the Goal is not proven and safe evidence-producing work remains inside settled boundaries. Complete only on trusted global completion. Block only when no safe next action remains or required evidence/authority is genuinely unavailable.

## AFK and HITL

A useful execution graph reduces Human involvement through four mechanisms:

1. **Decision closure** — material branches are resolved before they interrupt execution.
2. **Graph completeness** — the executor can discover ready work and real dependencies without asking what to do next.
3. **Verification closure** — nodes and the Goal have explicit evidence-based completion semantics.
4. **Recovery closure** — local failure routes to repair or replan rather than immediately back to the Human.

Do not use HITL as scheduling. A good Human interaction should be explainable as: “this unresolved choice materially changes the graph, and current intent/evidence cannot close it.”

## Leader as a capability floor

Leader-style taskbooks are a useful execution-coverage reference, not a required serialization. Preserve the capabilities that make them AFK-capable:

- concise Why / Goal;
- material decisions closed before execution;
- work surface decomposed into bounded units;
- hard no-go boundaries;
- concrete local and global acceptance;
- continuation, failure, and blocker semantics.

Do not copy realization details merely for parity: fixed Task 0, fixed retry counts, mandatory progress files, exact patch-by-patch sequencing, fixed agent topology, or command order are justified only when the task itself requires them.

## Executable carrier quality

A fresh executor should be able to answer, without reconstructing prior conversation:

- Why are we doing this, and what direction should guide unforeseen choices?
- What final state must be true?
- What relevant state and proof already exist?
- Which material branches are already settled, and on what basis?
- What work is currently known, which nodes depend on which, and what is ready now?
- What may not drift?
- How is each important node verified, and what proves the complete Goal?
- How should failure, new evidence, graph revision, HITL, completion, and true blocking behave?
- What must be delivered at the end?

If the artifact answers these with less structure, keep it smaller. If omitting one would create drift, false completion, unnecessary HITL, or loss of AFK continuity, keep it explicit.