# Execution Graph

Use only when a linear Task list would hide true dependency, parallelism, or a meaningful Task-Group verification boundary.

- `depends on`: only for result consumption or safe-execution prerequisites.
- `may run in parallel`: when no dependency or write conflict exists.
- `verify group at boundary`: when a coherent set of Tasks together establishes a combined behavior or shared contract that local proof cannot establish; place the broader judge before dependent work consumes it or at the join.
- `reverify at join`: when later change may invalidate evidence without blocking parallel work.

A Task Group is only a semantic verification boundary over ordinary Tasks; do not introduce a separate graph object, schema, persistent state, or fixed Agent topology. Every branch must rejoin or end in an explicit terminal route. Omit transitive and merely sequential edges. Ownership and evidence rules stay in the ordinary Task contract. Do not introduce multiple taskbooks.
