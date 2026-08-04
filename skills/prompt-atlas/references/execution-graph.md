# Execution Graph

Use only when a linear Task list would hide true dependency or parallelism.

- `depends on`: only for result consumption or safe-execution prerequisites.
- `may run in parallel`: when no dependency or write conflict exists.
- `reverify at join`: when later change may invalidate evidence without blocking parallel work.

Every branch must rejoin or end in an explicit terminal route. Omit transitive and merely sequential edges. Ownership and evidence rules stay in the ordinary Task contract. Do not introduce a graph schema, fixed Agent topology, or multiple taskbooks.
