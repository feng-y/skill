# Execution Graph

Use only when work has real branches, dependencies, shared writes, or a join that linear task order would hide.

Add a direct edge only when a downstream Task consumes an upstream result, requires its completion for safe execution, or must be reverified when that result changes. Do not add transitive or merely sequential edges.

Compile the minimum dependency structure:

- order Tasks by those direct dependencies;
- mark only material prerequisites and parallel branches;
- give each shared mutable surface one owner;
- end with a Task or completion gate that rejoins the branches and verifies the whole Goal;
- require downstream re-verification when an upstream change invalidates its evidence.

Render the graph as ordinary Tasks. Use brief relationship phrases such as `depends on`, `may run in parallel`, and `after both pass`. Do not expose a node schema or graph terminology unless the task itself requires them. Do not prescribe a fixed Agent topology or compile multiple taskbooks.
