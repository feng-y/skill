# Execution Graph

Use only when a linear Task list would hide real branches, dependencies, shared writes, or a join.

Add a direct edge only when a downstream Task consumes an upstream result, requires its completion for safe execution, or must be reverified when that result changes. Do not add transitive or merely sequential edges.

Expose only material prerequisites, parallel branches, and an explicit join or terminal route. The ordinary Task contract remains authoritative for write ownership and evidence validity.

Render the graph as ordinary Tasks. Use brief relationship phrases such as `depends on`, `may run in parallel`, and `after both pass`. Do not expose a node schema or graph terminology unless the task itself requires them. Do not prescribe a fixed Agent topology or compile multiple taskbooks.
