# Execution Graph: Static Compile and Runtime Evolution

Use only when a linear Task list would hide real dependency, parallelism, shared writes, or a meaningful Task-Group verification boundary. Graph carries **currently evidenced execution relationships** only; it does not define Goal, Verification, or Evidence.

## Static compile

At Handoff, the Graph is the best-known snapshot supported by current reality, not a frozen workflow:

- `depends on` — only when downstream work truly consumes an upstream result or the upstream result is a safe-execution prerequisite;
- `may run in parallel` — when there is no dependency or write conflict;
- `verify group at boundary` — when a coherent set of Tasks together establishes combined behavior or a shared contract that local verification cannot establish; place the broader judge before dependent work consumes it or at the join;
- `reverify at join` — when parallel work can continue but later changes may invalidate existing Evidence.

Omit transitive edges and do not turn mere sequence into dependency. Keep simple work linear; do not manufacture nodes, branches, or Task Groups just to have a Graph.

## Runtime Graph

The Executor runs the current ready frontier, not a frozen static order. When new Evidence changes execution reality, update only the **remaining Graph**:

- discover a real new prerequisite or consumer → add the Task/dependency before affected downstream work;
- prove an assumed dependency is false → remove the edge and unblock independent work;
- implementation reality changes → split, merge, or reorder remaining Tasks as needed;
- one branch is Blocked but another is independent → continue ready work; a join waits only for real dependencies;
- actual change surface, effective binding/config, or a shared contract changes → recompute affected Verification scope and join Evidence;
- completed work is not mechanically reopened when the Graph changes; reacquire Evidence only when its premises are affected or a new combined boundary requires broader Verification.

The static Graph is the starting execution structure; the runtime Graph is the Evidence-driven current execution state. What changes is the remaining execution relationship, not Goal, Human authority, or still-applicable required Verification.

A Task Group is only a combined Verification boundary over ordinary Tasks. Do not introduce a separate Graph object, schema, persistent state, scheduler, or fixed Agent topology. Reuse normal repo/runtime progress state when it exists; otherwise keep the current frontier in execution context rather than creating a Graph control plane. Write ownership and Evidence requirements remain in ordinary Task contracts. Every branch eventually rejoins or reaches an explicit terminal route; do not create multiple taskbooks.
