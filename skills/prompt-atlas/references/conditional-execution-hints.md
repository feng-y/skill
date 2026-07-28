# Execution-quality profile

Apply this profile when the Intent Contract may be executed directly. Select only the protections that materially improve completion quality for this task and blend portable semantics into the contract. Carrier mechanics such as named progress files belong only in a selected autonomous or long-running carrier.

## Establish reality

- Inspect the actual repo, target ref, worktree, commands, tests, configs, runtime, and existing rich specifications needed to understand the work.
- Record a measured baseline when regression, migration, cleanup, performance, coverage, or count-based completion depends on it.
- Embed an exact command only after it has been verified in the current environment. When access is unavailable, make the missing baseline or command a precise execution precondition rather than an invented fact.
- Keep laws and intelligence distinct: a verified invariant or user decision is binding; a likely approach remains an evidence-tagged hypothesis.

## Protect the work

- State the achieved result, not “analyze,” “try,” or another activity, as the execution objective.
- Name the allowed scope and protected neighboring behavior when drift would be costly. Preserve existing user changes and repo invariants unless the intent explicitly changes them.
- Give routine implementation judgment to the executor. Reserve escalation for contradictions, missing authority, or ambiguity that changes the intended result or crosses an approval boundary.
- For exploration, close on a decision or bounded finding with evidence and remaining uncertainty, not fake implementation metrics.

## Prove completion

- Use proportional evidence that exercises the requested behavior: relevant tests, build or lint checks, config/reference searches, replay or trace comparison, runtime observation, or a richer existing specification.
- When the repo owns a verification policy, map the change to its complete gate set. Account for every applicable minimum gate, upgrade gate, block condition, and no-evidence state; do not replace a mandatory replay, build, route, or contract gate with a merely similar check.
- Freeze a meaningful baseline when the evaluator could otherwise pass by weakening the target. State positive preservation criteria first; add narrow anti-shortcut constraints only for plausible reward-hacking paths such as skipping tests, loosening assertions, mocking the subject under test, deleting coverage, or retaining a hidden duplicate.
- Add a negative or fault-path check when a silent failure, false-green check, or disabled signal is a material risk.
- Treat evidence limits honestly. A passing build does not prove semantic equivalence when replay, trace, or behavior evidence is the real proof.

## Sustain autonomous work

- For work likely to outlive one context window, include a small durable progress record containing the current objective, completed evidence, next action, and unresolved blocker. Require a resumed executor to read it before repeating work.
- Use a separate blocker record only when work can continue safely around an unresolved dependency; a contradiction that invalidates the intended result stops the affected work.
- Set evidence-based retry or rollback limits when repeated failure could waste substantial time or degrade a known baseline.
- Omit continuity machinery for work that comfortably fits one run.

## Coordinate parallel work

Apply only when the user authorizes parallel execution:

- give every executor the same global intent and completion semantics;
- assign non-overlapping write boundaries and a single owner for shared files or generated artifacts;
- define the integration seam and require evidence to be rerun after shared-state changes;
- keep discovery evidence from silently authorizing edits in another executor's area.

## Selection

- Pure clarification: no execution profile.
- Research, diagnosis, or review: reality, proportional evidence, honest uncertainty, and the relevant escalation boundary.
- Repo implementation: reality, scope, invariants, evidence, autonomy, and plausible anti-shortcut protections.
- Long autonomous work: add progress, blocker, retry, and resume semantics.
- Parallel work: add coordination only after user authorization.
- Explicit behavior change: preserve unaffected invariants; do not impose generic behavior equivalence on the behavior being changed.
