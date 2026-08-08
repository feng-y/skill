# Execution Graph: Static Compile and Runtime Evolution

Do not split Tasks just to expose a Graph. Use Graph only when the current Task granularity would hide a relationship that changes execution judgment: real dependency, parallelism, shared writes, a meaningful Task-Group boundary, or a join.

Graph carries **currently evidenced execution relationships** only. It is not a semantic SOT, future-work inventory, scheduler, or workflow model.

## Static compile

Compile the **minimum currently justified graph**:

- `depends on` only when downstream consumes an upstream result or requires it for safe execution;
- `may run in parallel` only when there is no dependency or write conflict;
- a Task-Group/join boundary only when combined Verification is materially different from local checks;
- re-verification only when later work may invalidate existing Evidence.

Omit transitive edges and mere sequence. Do not invent nodes to make a graph look complete.

Most importantly, do not materialize downstream Tasks whose existence depends on evidence not yet obtained. If A determines whether B/C/D are needed, compile A and the known decision boundary; let runtime Evidence materialize only the work that becomes real.

## Runtime evolution

Executor works the current ready frontier. New Evidence may change only the remaining graph:

- add a newly proven prerequisite, consumer, or affected surface before dependent work;
- remove a disproven dependency or unnecessary branch;
- split, merge, or reorder remaining Tasks when implementation reality changes;
- continue independent ready work when another branch is blocked;
- wait at a join only for real required upstream results;
- recompute affected Verification when change surface, binding/config, or combined behavior changes.

Completed work is not reopened mechanically. Reacquire Evidence only when its premise or the behavior it proved was affected.

A Task Group remains only a Verification boundary over ordinary Tasks. Do not create a Graph object/schema, persistent Graph state, scheduler, fixed Agent topology, or a second taskbook. Use normal repo/runtime progress records when they already exist; otherwise keep the current frontier in execution context.

The stable rule is:

> **Materialize what current Evidence makes executable; expand the graph when new Evidence makes more work real.**