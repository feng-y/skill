# Execution Graph

Use only when a linear Task list would hide real branches, dependencies, shared writes, or a join.

Add a direct dependency only when a downstream Task consumes an upstream result or requires its completion for safe execution. Do not add transitive or merely sequential dependencies. When a later upstream change could invalidate downstream evidence without blocking parallel work, mark the required re-verification at the join instead of creating a dependency.

Expose only material prerequisites, parallel branches, re-verification at joins, and an explicit join or terminal route. The ordinary Task contract remains authoritative for write ownership and evidence validity.

Render the graph as ordinary Tasks. Use brief relationship phrases such as `depends on`, `may run in parallel`, `reverify at join`, and `after both pass`. Do not expose a node schema or graph terminology unless the task itself requires them. Do not prescribe a fixed Agent topology or compile multiple taskbooks.
