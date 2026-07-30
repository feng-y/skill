# Execution Compile

Use this reference when Stage 2 graph shape, branch closure, AFK continuity, or HITL placement is not obvious. Execution Compile consumes Stable Intent IR and emits one executable carrier. It does not reopen intent and does not execute the graph.

## Objective

Compile the smallest truthful structure that lets a capable executor keep making correct progress without using Human interaction as orchestration.

Optimize for:

- longer autonomous execution span;
- real parallelism where independence exists;
- local verification and local recovery;
- recoverability across context interruption when needed;
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

## Ground execution reality

Intent grounding establishes meaning; Stage 2 must separately ground enough execution reality to avoid compiling fiction.

Before fixing the first graph, inspect the smallest authoritative surface that can determine:

- the actual repo/workspace or carrier binding;
- real work surfaces and ownership boundaries;
- governing specifications, tests, schemas, traces, or acceptance paths;
- baselines whose values matter to success;
- whether critical commands/verifiers actually exist and behave as assumed;
- dependencies that are real rather than inferred from prose order.

Run or inspect critical checks when accessible. If the environment is unavailable, keep that fact explicit. Compile verification of an unverified prerequisite as initial ready work when safe execution can continue; otherwise expose the true blocker. Never state a command, baseline, or gate as verified because it is plausible.

Prefer rich references over copying their content. Execution grounding may change graph shape, node boundaries, dependencies, proof topology, or execution decisions, but it may not reinterpret Stable Intent.

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

Use pre-execution HITL only when materially different graphs remain compatible with the stable intent and available evidence does not select among them. This is not limited to choices with obvious risk or a universally better answer; the point is to remove a branch that would otherwise interrupt AFK execution. When several such branches exist, batch the useful decision surface rather than using Human turns as a scheduler.

Do not escalate local How: helper naming, small code organization, exact patch order, reversible implementation details, or another choice whose alternatives do not materially change the graph remain executor-owned.

Keep law and guidance distinct. Human-confirmed decisions, governing constraints, and evidence-grounded invariants are binding; recommendations, promising starting points, or implementation hints remain non-binding unless their semantics are required for correctness.

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

When parallel branches can mutate shared surfaces, compile enough ownership to keep AFK execution safe:

- keep write domains disjoint where possible;
- assign one owner to each shared mutable surface;
- make joins and handoff evidence explicit;
- re-run or invalidate downstream evidence when upstream changes make it stale.

This defines orchestration semantics, not agent count. Runtime topology remains executor-owned unless the user fixed it.

### Checkpoint

A local checkpoint decides whether a node is done or routes it back for repair. Local PASS unlocks downstream work; local FAIL should normally stay inside the node loop.

### Global Gate

The Global Gate evaluates the complete Goal, not task count. Every required node being locally done is not sufficient when the overall behavioral, structural, or proof obligation is still unmet.

### Human Gate

A Human Gate exists only when new evidence exposes a material branch that cannot be closed from settled intent, governing constraints, or authoritative evidence. Do not put a Human Gate between ordinary tasks.

A Human-gated or externally blocked node does not stop independent ready work. Park it, preserve its evidence and missing decision, and continue elsewhere. The whole graph is blocked only when no safe ready work remains.

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
4. parks blocked/Human-gated nodes while other work remains ready;
5. updates the remaining graph when evidence invalidates current assumptions;
6. evaluates whether the Global Gate is satisfied.

Continue while the Goal is not proven and safe evidence-producing work remains inside settled boundaries. Complete only on trusted global completion. Block only when no safe next action remains or required evidence/authority is genuinely unavailable.

## Continuity

AFK execution may outlive one context even when the graph is small. When interruption or handoff is plausible, the carrier should require recoverable execution state at the semantic level:

- trustworthy completed nodes and their evidence;
- current graph changes that remain valid;
- parked blockers or Human decisions with exact missing input;
- next ready work and unresolved Goal conditions.

Do not mandate `PROGRESS.md`, `BLOCKED.md`, a database, or another storage mechanism unless the runtime or task requires it. The capability requirement is resumability without redoing trusted work or inventing state after context loss.

## Research and decision work

Research/selection graphs use the same execution model but different completion semantics:

- nodes may gather sources, test a hypothesis, compare options, reproduce a claim, or synthesize evidence;
- conclusions carry provenance or reproducible evidence rather than arbitrary numeric hard goals;
- fabricated citations, unrun “measurements,” or unsupported certainty are invalid proof;
- material counterevidence and residual unknowns remain visible;
- evidence that a path is a dead end may be a valid completed node and useful final result;
- explicit time/source budgets are honored when supplied; otherwise stop on the best supported answer when further work no longer changes material uncertainty enough to justify cost.

## AFK and HITL

A useful execution graph reduces Human involvement through four mechanisms:

1. **Decision closure** — material branches are resolved before they interrupt execution.
2. **Graph completeness** — the executor can discover ready work and real dependencies without asking what to do next.
3. **Verification closure** — nodes and the Goal have explicit evidence-based completion semantics.
4. **Recovery closure** — local failure, partial blocking, and context interruption route to repair, other ready work, or recovery rather than immediately back to the Human.

Do not use HITL as scheduling. A good Human interaction should be explainable as: “this unresolved choice materially changes the graph, and current intent/evidence cannot close it.”

## Leader capability floor

Leader-style taskbooks are a useful execution-coverage reference, not a required serialization. Prompt Atlas should preserve the behavior that makes them AFK-capable while keeping realization runtime-selectable.

| Leader capability | Prompt Atlas execution semantic |
| --- | --- |
| “这活为什么干” | Purpose / Why judgment anchor + Goal |
| 先实测仓库、命令、基线 | Execution grounding + verified/unverified State |
| “我替领导拍的板” | Decision closure; unresolved material branch → pre-execution HITL |
| 白名单/禁区；法与情报分家 | Boundaries + explicit binding-vs-guidance distinction |
| 任务 N + 依赖顺序 | Task / Issue nodes + real dependency edges |
| 每任务机器可判验收 | Local Verify / checkpoint |
| 防作弊、反向验证 | Protected proof semantics + failure sensitivity |
| 最终完成条件 | Trusted Global Gate; local done ≠ global completion |
| 某项卡住继续别的 | Park blocked/Human-gated node; continue independent ready work |
| PROGRESS/BLOCKED 断点续跑 | Recoverable semantic state; storage mechanism left to runtime |
| 多 agent 地界/共享写点/接缝 | Parallel write ownership + explicit joins + stale-evidence invalidation |
| 探索型来源/死路/预算 | Evidence-bearing research graph + provenance/residual unknowns |
| 管理者暗卷/独立验收 | Independent accepting boundary outside executor-visible proof when required |

Do not copy realization details merely for parity: fixed Task 0, fixed retry counts, mandatory progress files, exact patch-by-patch sequencing, fixed agent topology, or command order are justified only when the task itself requires them.

## Executable carrier quality

A fresh executor should be able to answer, without reconstructing prior conversation:

- Why are we doing this, and what direction should guide unforeseen choices?
- What final state must be true?
- What relevant state and proof already exist, and what is still unverified?
- Which material branches are already settled, and on what basis?
- What work is currently known, which nodes depend on which, and what is ready now?
- What may not drift, and which guidance remains optional?
- How is each important node verified, and what proves the complete Goal?
- If one node blocks, what independent work can continue?
- What state must survive a context interruption?
- How should failure, new evidence, graph revision, HITL, completion, and true blocking behave?
- What must be delivered at the end?

If the artifact answers these with less structure, keep it smaller. If omitting one would create drift, false completion, unnecessary HITL, or loss of AFK continuity, keep it explicit.