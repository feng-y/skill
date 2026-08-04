# Execution Graph

Use only when work has real branches, dependencies, shared writes, or a join that linear task order would hide.

Compile the minimum dependency structure:

- order Tasks by real dependency;
- mark only material prerequisites and parallel branches;
- give each shared mutable surface one owner;
- end with a Task or completion gate that rejoins the branches and verifies the whole Goal;
- require downstream re-verification when an upstream change invalidates its evidence.

Render the graph as ordinary Tasks. Use brief relationship phrases such as `depends on`, `may run in parallel`, and `after both pass`. Do not expose a node schema, graph terminology, fixed Agent topology, or multiple taskbooks unless the task itself requires them.
