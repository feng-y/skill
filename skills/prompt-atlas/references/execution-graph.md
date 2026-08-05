# Execution Graph

Use when a linear Task list would hide true dependency, parallelism, or a meaningful Task-Group verification boundary, or when Stable Intent and the declared delivery are bounded but some downstream work cannot yet be stated truthfully.

Express only real graph relations:

- `depends on`: only for result consumption or safe-execution prerequisites.
- `may run in parallel`: when no dependency or write conflict exists.
- `verify group at boundary`: when a coherent set of Tasks together establishes a combined behavior or shared contract that local proof cannot establish; place the broader judge before dependent work consumes it or at the join.
- `reverify at join`: when later change may invalidate evidence without blocking parallel work.

The **current frontier** is the work whose real dependencies are satisfied, required context and authority are available, local closure evidence is defined, and no write conflict prevents execution. It is an execution judgment, not a graph edge, scheduler, or persistent queue.

## Progressive compilation

Compile a Task only when current evidence is enough to state its observable result, real dependencies, authority boundary, and sufficient proof. Do not invent placeholder Tasks to make the graph appear complete. Keep in-scope work that is not yet precise enough as an unresolved area until frontier results make it truthfully compilable. An unresolved area may remain in execution only while its current consequence does not require choosing or changing the Goal, acceptance requirements, or a confirmed boundary; return to Intent Take as soon as that changes. Stable Intent, one bounded delivery, confirmed boundaries, and complete-Goal proof remain binding throughout.

When an unresolved area blocks progress, use the smallest closure operation needed for the next judgment: `Research` reads existing reality; `Prototype` makes an abstract question concrete enough to judge; `Grilling` obtains the decision of the Human who owns it after available evidence is gathered; closure `Task` means a necessary enabling action when observation or discussion cannot proceed. These operations may chain. They are not fixed Task types, workflow stages, or substitutes for authority judgment.

After any result that can change remaining work, refresh the graph: record the result and evidence; check which assumptions or proofs remain valid; add, remove, split, merge, or rewrite remaining Tasks; update only real dependency and evidence-invalidating relations; and recompute the current frontier. Park only affected branches while independent frontier work remains. Return to Intent Take only when the Goal, acceptance requirements, or a confirmed boundary becomes unsettled; use `Status: Blocked` only when no safe frontier remains.

## Low-resolution view

When the graph is non-trivial, keep its shared view low-resolution: Goal, material decisions, current frontier, unresolved areas, out-of-scope work, proof state, and pointers to detail. A decision or evidence body lives in one authoritative taskbook section, Task, repository/runtime record, or existing issue; the shared view summarizes and points to it instead of copying it. Load the Goal and protected boundaries, the current work item, its direct dependencies, and relevant decisions and evidence; do not load every branch by default.

This view does not require a new Map file, issue tracker, persistent graph object, fixed schema, or Agent topology. Reuse the taskbook and the repository or runtime's normal implementation record.

A Task Group is only a semantic verification boundary over ordinary Tasks. Every compiled branch must rejoin or end in an explicit terminal route. Omit transitive and merely sequential edges. Ownership and evidence rules stay in the ordinary Task contract. Do not introduce multiple taskbooks.
