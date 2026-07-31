# Execution Compile

Use this reference only for Stage 2 edge cases. The main skill is the source of truth for the six-section taskbook and execution rules.

## Task 0

Task 0 is fixed; its weight is not. A clear local task may need only one compact opening item. Riskier work may add baseline capture, dependency checks, or verifier failure-sensitivity.

Task 0 binds the actual execution object and validates the taskbook before material change. Reuse evidence only when it is authoritative, fresh, and applicable to the same repo, worktree, target, and environment. Recheck missing, stale, disputed, environment-dependent, or invalidated facts.

If reality differs:

- revise the remaining graph when Goal and confirmed boundaries still hold;
- return to Intent Take when progress would change intent or a confirmed boundary;
- park only the blocked branch when independent safe work remains;
- otherwise emit `Status: Blocked` with the exact resolving condition.

A Human decision visible during compile may not be deferred to Task 0.

## Graph and ownership

Every taskbook has a graph, but not every graph is elaborate.

```text
Task 0 → Execute with local proof → Global Gate
```

Add nodes and edges only when they change readiness, write ownership, evidence, invalidation, joins, or branch routing. Use one owner for a shared mutable surface. Upstream changes invalidate downstream evidence only when they affect what it proved.

The compiler freezes Goal, Human authority, confirmed boundaries, protected proof surfaces, completion obligations, and handoff mode. The Executor may revise, split, merge, reorder, or park remaining work inside that envelope and records material changes in `PROGRESS.md`.

## State and stopping

For repository execution, `PROGRESS.md` preserves completed/current/next work, evidence, stale evidence, parked branches, and remaining Goal conditions. `BLOCKED.md` exists only for a real blocker and records attempts, the exact missing condition, its resolving condition, and safe work that can continue. Both stay under `.scratch/<project>/` and are not committed.

A retry must change the hypothesis or approach. A known-bad path stops immediately. Three consecutive failures against the same acceptance condition in the same route force replan, branch switch, rollback, `BLOCK`, or `ESCALATE`.

Local proof unlocks dependent work; only the Global Gate closes the Goal. If required independent acceptance is unavailable, completion stops at `ready for independent acceptance`.

Keep the taskbook small enough to close as one execution effort. If it cannot, split it into independently completable taskbooks rather than growing the graph without bound.
