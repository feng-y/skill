# Execution Graph Judgment

Read only from [execution-compile.md](execution-compile.md) when multiple work units have real **dependency / parallel / shared-write / join / Evidence-contingent relations**. Graph owns execution relations only; it does not own Goal, Task taxonomy, Verification authority, state machine, or scheduling.

## Compile current relations

Express only relations already supported by Evidence and capable of changing execution judgment:

- `depends on`: downstream genuinely consumes upstream output, or upstream is a safety prerequisite;
- `may run in parallel`: no dependency and no material write conflict;
- `shared write`: multiple work units touch the same authoritative surface and need explicit ownership / ordering;
- `join`: combined outcome / Verification differs materially from branch-local completion;
- `re-verify after`: later work is already known to invalidate existing Evidence.

Omit preference-only ordering and transitive edges. If Evidence already proves `A → {B,C} → D`, compile it now rather than exposing only A. Do not guess work whose existence truly depends on future Evidence.

## Let Evidence evolve only affected relations

Runtime Evidence changes only the affected remaining Graph: add a prerequisite/consumer when proven real, remove a dependency when disproven, and split/merge/reorder remaining work when implementation reality changes. Reopen completed work only when its Evidence premise or proven behavior is affected.

One blocked branch must not freeze independent ready branches; a join waits only for genuinely required upstream results. Graph must respect the Goal / ready-frontier boundary already owned by `SKILL.md`; it does not redefine scope or phase Goals here.

Graph does not create ImplementationNode / ProbeNode / VerificationNode taxonomies; those are work/actions. Evidence is reality output, not a node. Do not add a persistent Graph object, second taskbook, fixed Agent topology, manager, or scheduler.
