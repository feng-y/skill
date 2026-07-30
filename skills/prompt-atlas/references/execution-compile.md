# Execution Compile

Use this reference when Stage 2 needs more detail on graph shape, branch closure, AFK continuity, or Leader capability coverage. Execution Compile consumes Stable Intent IR and emits one executable carrier; it does not reopen intent or run the graph.

## Outcome

Produce the smallest truthful structure that lets a capable executor keep making correct progress without using Human interaction as orchestration.

Preserve:

- the **Why / design intent** that guides unforeseen choices;
- the complete **Goal** and settled authority;
- grounded execution reality;
- real work dependencies and ownership;
- task-specific proof needed for trusted completion;
- enough recovery semantics for the work to continue through failure or interruption.

Graph complexity follows dependency, coordination, proof, isolation, and recovery needs—not task size or a desire to plan everything up front.

## Lowering

Stable Intent is source semantics. Lower it into execution semantics rather than repeating it:

- Why → judgment anchor;
- Goal → global end condition;
- territory facts → State and node context;
- Human decisions / hard constraints → invariants;
- material execution decisions → closed branches with basis;
- success / proof semantics → local proof and Global Gate;
- output requirements → Delivery.

The final carrier has one authority for Goal, boundaries, and completion.

## Ground execution reality

Intent grounding establishes meaning; Stage 2 grounds the territory needed for orchestration.

Inspect the smallest authoritative surface that can determine the actual execution target, work boundaries, governing specs/tests/schemas, material baselines, real dependencies, and critical commands or verifiers. Prefer references to rich existing artifacts over restating them.

A command, baseline, gate, or environment is verified only when evidence supports that claim. If a prerequisite is unverified, make its check initial ready work when safe progress can continue; otherwise expose the true blocker.

Execution grounding may change graph shape, node boundaries, dependencies, proof topology, or execution decisions. It may not change Stable Intent.

## Close material branches

Close a branch before execution when different choices would materially change the execution graph—for example Task / Issue boundaries, dependency/order, verification ownership or acceptance path, scope, architecture responsibility, or the Global Gate.

Use Stable Intent, governing constraints, and authoritative evidence first. If materially different graphs remain equally compatible, use pre-execution HITL. Batch related decisions rather than turning Human turns into scheduling.

When another Human turn is explicitly unavailable, a visibly unconfirmed default may keep execution moving only if it preserves settled Goal and boundaries and is reversible or reliably mismatch-detectable. Record the assumption and consequence. Otherwise return `Status: Execution Decision`.

Local reversible How remains executor-owned. Keep binding invariants distinct from non-binding guidance.

## Build the graph

A **Task / Issue node** is a bounded unit that can be started, observed, and locally judged. Give it only:

- **Outcome** — state it establishes;
- **Context** — facts or references needed for this work;
- **Dependencies** — upstream results it actually consumes;
- **Boundaries** — applicable invariants;
- **Verify** — task-specific evidence that makes the node locally done.

An **edge** represents real dependency, evidence flow, or a required gate. Independent work should stay independent.

A **checkpoint** decides local completion and normally routes failure back to the node for repair. The **Global Gate** judges the complete Goal; a collection of local PASS results is not automatically global completion.

A **Human Gate** exists only when new evidence exposes a material branch that current intent/evidence cannot close. Park that node and continue independent ready work. The graph is truly blocked only when no safe ready work remains.

For parallel branches that touch shared mutable surfaces, make ownership explicit: prefer disjoint write domains, assign one owner per shared surface, make joins clear, and invalidate downstream proof when an upstream change makes it stale. This is orchestration semantics, not a fixed agent count.

Keep the initial graph small. The runtime may add, remove, split, merge, or reroute remaining nodes as evidence changes the current execution theory; trustworthy completed work stays complete unless new evidence invalidates it.

## Runtime and continuity

Each ready node uses the simplest evidence-driven loop that fits the task: act, observe the result, evaluate against its local outcome, then continue, repair, or revise How.

Do not add generic review or double-check stages merely because the task is non-trivial. Verification structure exists when the Goal or governing proof semantics require it; see [completion-trust.md](completion-trust.md).

Failure, difficulty, or an unexpected repo fact is not by itself HITL. The graph should keep advancing other ready work and revise remaining structure from evidence.

When work may outlive one context, require recoverable semantic state:

- trustworthy completed nodes and evidence;
- still-valid graph changes;
- parked blockers/decisions and the exact missing input;
- next ready work and unresolved Goal conditions.

The storage mechanism is runtime-specific; resumability is the capability.

## Research and decision work

Use the same graph model with different proof semantics. Nodes may gather sources, test hypotheses, compare options, reproduce claims, or synthesize evidence. Conclusions retain provenance, counterevidence, and material residual unknowns. A well-supported dead end can be a useful completed result. Respect explicit time/source budgets; otherwise stop when further work no longer changes the decision materially enough to justify the cost.

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
| 防作弊、反向验证 | Protected proof semantics + failure sensitivity |
| 最终完成条件 | Trusted Global Gate; local done ≠ global completion |
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
- what is known, unverified, or already proven;
- which material branches and boundaries are settled;
- what work is ready and which real dependencies exist;
- what task-specific evidence closes important nodes and the complete Goal;
- what can continue when one branch blocks and what state must survive interruption;
- what must be delivered.

Use less structure when those semantics remain clear. Keep detail only when its absence would create drift, false completion, unnecessary HITL, or loss of AFK continuity.