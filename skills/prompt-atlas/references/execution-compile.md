# Execution Compile

Use this reference when Stage 2 needs more detail on graph shape, branch closure, runtime behavior, AFK continuity, or Leader capability coverage. Execution Compile consumes Stable Intent IR and emits one executable control carrier; it does not reopen intent, execute the carrier, or own live state.

## Outcome

Produce the smallest truthful control structure that lets a capable executor keep making correct progress without using Human interaction as orchestration.

The carrier is not only an initial plan. It is an executable control program for a runtime: a graph plus the node-loop, routing, recovery, and acceptance semantics needed to interpret that graph correctly.

Preserve:

- the **Why / design intent** that guides unforeseen choices;
- the complete **Goal** and settled authority;
- grounded execution reality;
- real work dependencies and ownership;
- task-specific proof needed for trusted completion;
- material runtime routes and recovery semantics;
- the acceptance boundary that decides the complete Goal.

Graph complexity follows dependency, coordination, proof, isolation, runtime envelope, and recovery needs—not task size or a desire to plan everything up front.

## Lowering

Stable Intent is source semantics. Lower it into execution semantics rather than repeating it:

- Why → judgment anchor;
- Goal → global end condition;
- territory facts → State and node context;
- Human decisions / hard constraints → invariants;
- material execution decisions → closed branches with basis;
- work structure → nodes, edges, ownership, and joins;
- failure and uncertainty → runtime routes;
- success / proof semantics → local proof and Global Gate;
- interruption risk → recovery contract;
- output requirements → Delivery.

The carrier preserves one authoritative source for Goal and boundaries and makes the accepting authority for completion explicit; these authorities may be different.

## Executable control carrier

Compile four coupled semantics, using only the structure the task needs:

1. **Graph structure** — bounded outcome nodes, real dependency/evidence edges, ownership, joins, and the Global Gate.
2. **Runtime semantics** — how ready work progresses, how node-local loops close, and how verdicts route to repair, graph revision, blocking, Human decision, or intent repair.
3. **Recovery semantics** — what completed work, evidence, decisions, blockers, graph changes, and next-ready state must survive interruption.
4. **Acceptance semantics** — which proof closes local claims, who may judge the complete Goal, and when an independent boundary is required.

Prompt Atlas compiles this control contract. The execution runtime interprets it, schedules work, updates live state, and persists recovery data. Do not leave material routing or completion behavior implicit enough that the executor must reinvent it.

## Ground execution reality

Intent grounding establishes meaning; Stage 2 grounds the territory needed for orchestration.

Inspect the smallest authoritative surface that can determine the actual execution target, work boundaries, governing specs/tests/schemas, material baselines, real dependencies, and critical commands or verifiers. Prefer references to rich existing artifacts over restating them.

A command, baseline, gate, or environment is verified only when evidence supports that claim. If a prerequisite is unverified, make its check initial ready work when safe progress can continue; otherwise expose the true blocker.

Execution grounding may change graph shape, node boundaries, dependencies, proof topology, runtime routes, or execution decisions. It may not change Stable Intent.

If new evidence shows that the settled Goal cannot be preserved inside confirmed boundaries, or that progress requires a new Human-owned choice about outcome, accepted behavior, scope/priority, approval, or protected proof, stop lowering and return `Status: Unresolved Intent` with the conflict, evidence, and smallest decision surface. Re-enter Intent Take while preserving still-valid grounding. Do not disguise an intent repair as an execution branch.

## Close material branches

Close a branch before execution when different choices would materially change the control carrier—for example Task / Issue boundaries, dependency/order, verification ownership or acceptance path, scope, architecture responsibility, runtime envelope, recovery requirements, or the Global Gate—while all alternatives preserve Stable Intent.

Use Stable Intent, governing constraints, and authoritative evidence first. If materially different carriers remain equally compatible, use pre-execution HITL. Batch related decisions rather than turning Human turns into scheduling.

When another Human turn is explicitly unavailable, a visibly unconfirmed default may keep execution moving only if it preserves settled Goal and boundaries and is reversible or reliably mismatch-detectable. Record the assumption and consequence. Otherwise return `Status: Execution Decision`.

Local reversible How remains executor-owned. Keep binding invariants distinct from non-binding guidance.

## Build the graph

A **Task / Issue node** is a bounded outcome that can be started, observed, and locally judged. Give it only:

- **Outcome** — state it establishes;
- **Context** — facts or references needed for this work;
- **Dependencies** — upstream results it actually consumes;
- **Boundaries** — applicable invariants;
- **Verify** — task-specific evidence that makes the node locally done.

Use stable node identities when dependencies, recovery, parallel ownership, or evidence references need them. A one-node task is still a valid graph.

An **edge** represents real dependency, evidence flow, invalidation, or a required gate/routing relationship. Distinguish edge types only when the distinction changes readiness, proof, recovery, or control flow. Independent work should stay independent.

A **checkpoint** decides local completion and normally routes failure back to the node loop for repair. The **Global Gate** judges the complete Goal; a collection of local PASS results is not automatically global completion.

Do not unfold routine node-local work into a prose sequence of plan / implement / test / retry nodes. The node owns the simplest act / observe / evaluate / repair loop that can establish its Outcome. Split implementation, investigation, or verification only when they have different dependencies, owners, evidence products, or acceptance boundaries.

A **Human Gate** exists only when new evidence exposes a material execution branch that preserves Stable Intent but current evidence cannot close. Park that node and continue independent ready work. If the new choice would change Goal or Human-owned intent, route back to Intent Take instead. The graph is truly blocked only when no safe ready work remains.

For parallel branches that touch shared mutable surfaces, make ownership explicit: prefer disjoint write domains, assign one owner per shared surface, make joins clear, and invalidate downstream proof when an upstream change makes it stale. This is orchestration semantics, not a fixed agent count.

Keep the initial graph small. The runtime may add, remove, split, merge, or reroute remaining nodes as evidence changes the current execution theory; trustworthy completed work stays complete unless new evidence invalidates it.

## Runtime and continuity

Each ready node uses the simplest evidence-driven loop that fits the task: act, observe the result, evaluate against its local outcome, then continue, repair, or revise How.

The carrier should make material verdict routes clear:

- a local mismatch normally returns to the current node loop for repair or a different local approach;
- evidence that invalidates the current execution theory may revise the remaining graph, dependencies, ownership, or proof topology;
- a newly exposed material branch that preserves Stable Intent may route to a Human Gate when evidence cannot close it;
- evidence that conflicts with Goal, accepted behavior, Human-owned scope, approval, or protected proof routes to `Status: Unresolved Intent`, not silent graph repair;
- complete local evidence routes to the Global Gate, not directly to final completion.

Do not add generic review or double-check stages merely because the task is non-trivial. Verification structure exists when the Goal or governing proof semantics require it; see [completion-trust.md](completion-trust.md).

Failure, difficulty, or an unexpected repo fact is not by itself HITL. The graph should keep advancing other ready work and revise remaining structure from evidence.

Compile runtime-envelope requirements only when material—for example whether Human interaction is available during execution, whether work may span contexts, where state can persist, whether multiple agents share mutable surfaces, and whether the executor may judge final completion.

When work may outlive one context, require recoverable semantic state:

- trustworthy completed nodes and their still-valid evidence;
- invalidated or stale evidence and why it no longer applies;
- still-valid graph changes;
- settled decisions and assumptions still in force;
- parked blockers/decisions and the exact missing input;
- next ready work and unresolved Goal conditions.

The storage mechanism is runtime-specific; resumability is the capability.

## Research and decision work

Use the same control model with different proof semantics. Nodes may gather sources, test hypotheses, compare options, reproduce claims, or synthesize evidence. Conclusions retain provenance, counterevidence, and material residual unknowns. A well-supported dead end can be a useful completed result. Respect explicit time/source budgets; otherwise stop when further work no longer changes the decision materially enough to justify the cost.

## Leader capability floor

Leader is a semantic coverage reference, not a serialization template.

| Leader capability | Prompt Atlas execution semantic |
| --- | --- |
| “这活为什么干” | Purpose / Why judgment anchor + Goal |
| 先实测仓库、命令、基线 | Execution grounding + verified/unverified State |
| “我替领导拍的板” | Material branch closure; unresolved branch → HITL or safe visibly-unconfirmed default |
| 白名单/禁区；法与情报分家 | Boundaries + binding-vs-guidance distinction |
| 任务 N + 依赖顺序 | Task / Issue nodes + real dependency edges |
| 每任务机器可判验收 | Local task-specific proof / checkpoint |
| 连败换路、结果变差回滚 | Failure-sensitive node routing + regression recovery |
| 防作弊、反向验证 | Protected proof semantics + failure sensitivity |
| 最终完成条件 | Trusted Global Gate; local done ≠ global completion |
| 中途无人可问 | Runtime envelope closes material branches before execution or records safe explicit defaults |
| 某项卡住继续别的 | Park blocked/Human-gated node; continue ready work |
| PROGRESS/BLOCKED 断点续跑 | Recoverable semantic state; storage left to runtime |
| 多 agent 地界/共享写点/接缝 | Parallel ownership + joins + stale-evidence invalidation |
| 探索型来源/死路/预算 | Evidence-bearing research graph + provenance/residual unknowns |
| 管理者暗卷/独立验收 | Independent accepting boundary outside executor-visible proof when required |

This is a capability floor, not an empirical parity claim. Behavioral parity still requires paired executions.

Leader mechanisms such as a fixed Task 0, mandatory progress filenames, exactly three failures before changing strategy, fixed agent topology, exact command order, or `/goal`'s carrier limit are runtime realizations. Preserve the underlying grounding, recovery, continuity, failure-sensitivity, ownership, or envelope requirement only when the actual task/runtime needs it.

## Carrier quality

A fresh executor should be able to recover, without replaying the conversation:

- why the work exists and what final state is required;
- what is known, unverified, already proven, or invalidated;
- which material branches and boundaries are settled;
- what work is ready and which real dependencies exist;
- how node-local failure, graph invalidation, Human decisions, and intent conflicts route;
- what task-specific evidence closes important nodes and the complete Goal;
- what can continue when one branch blocks and what state must survive interruption;
- who may judge final completion;
- what must be delivered.

Use less structure when those semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, or loss of AFK continuity.
