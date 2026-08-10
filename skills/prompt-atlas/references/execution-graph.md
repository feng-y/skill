# Execution Graph: static compile and runtime evolution

Do not split Tasks just to draw a Graph. Use Graph only when the current Task granularity would hide a **relationship that changes execution judgment**: a real dependency, parallelism, shared write, meaningful Task Group boundary, or join.

Graph carries only **execution relationships already supported by current Evidence**. It is not a semantic SOT, future-work inventory, scheduler, or workflow model.

## Static compile

Compile the **decision-complete Graph supported by current Evidence**: express once the necessary work / relations that are already known, materially change execution judgment, and have sufficiently stable boundaries. Do not hide them for artificial laziness, and do not enumerate file/symbol/patch detail merely in the name of “complete.” Truly contingent work that still depends materially on future Evidence is not guessed early.

- `depends on` — only when downstream really consumes an upstream result or the upstream result is a safe-execution prerequisite;
- `may run in parallel` — only when there is no dependency or write conflict;
- Task Group / join — only when combined Verification is materially different from local checks and the relationship is already real;
- re-verification — only when later work is already known to be able to invalidate existing Evidence.

Omit transitive dependencies and mere sequence. Do not manufacture nodes to make the Graph look complete. But when current Evidence already establishes `A → {B,C} → D`, compile that structure directly rather than intentionally degrading it to only A.

Compile only the known structure and its decision boundary when whether B/C/D **exist, what they affect, or which relationship is necessary** still depends on future Evidence from A. When runtime Evidence arrives, add only the downstream work that becomes real to the same Graph.

## Runtime evolution

The Executor works the current ready frontier. New Evidence adjusts only the remaining Graph:

- a newly proven prerequisite, consumer, or affected surface → add necessary work before affected downstream work;
- a disproven dependency or branch → remove it and let ready work continue;
- changed implementation reality → split, merge, or reorder remaining Tasks;
- one branch Blocked while another is independent → continue ready work;
- a join waits only for real required upstream results;
- actual change surface, binding/config, provider validity, or combined behavior makes a new Verification obligation/action applicable → place that verification/probe as a current execution action at the lowest meaningful boundary;
- new Evidence disproves compiled Verification scope/placement → repair only the affected part.

Do not create ImplementationNode / ProbeNode / VerificationNode taxonomies here: implementation, probes, and verification are simply current executable actions, while Graph expresses only their real relationships. **Evidence is the reality output of an action; the Completion Hook is taskbook judgment. Neither is a Graph node.**

Completed work is not reopened mechanically when Graph changes; reacquire Evidence only when its premises or the behavior it proved were affected.

Task Group remains only a Verification boundary over ordinary Tasks. Do not add a Graph object/schema, persistent Graph state, scheduler, fixed Agent topology, or second taskbook. Reuse normal repo/runtime progress records when they exist; otherwise keep the frontier in current execution context.

The stable rule is:

> **Compile execution relations once when current Evidence already makes them necessary and stable; expand truly contingent work / Verification only when Evidence makes it real.**
