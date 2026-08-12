# When Goal is not settled yet

Read only after the main Skill has begun Ground / Shape but still cannot determine which Goal the Human will ultimately accept.

## Is this Goal or How?

Use one test:

> **Would the Human still accept it if a materially different implementation satisfied the same requirement?**

Yes usually means it is How and Prompt Atlas should not freeze it.

No means it expresses a result, boundary, risk commitment, or Verification requirement the Human actually cares about and belongs in Goal.

A concrete current implementation, class/provider, or detailed plan does not automatically elevate How into Goal. Conversely, when the Human explicitly requires a representation / compatibility / provider because that representation itself is a business or technical commitment, it may be part of Goal.

## Do not mistake the map for reality

The prompt, current plan, and Prompt Atlas itself are maps. The repo, runtime, historical constraints, and real consumers may expose facts the map omitted but that can still change Goal.

Prefer checking differences such as authoritative specs or precedents, real consumers, external contracts, serialized/config identity, deployment or authorization constraints, and the real relationship between current workspace work and Human Goal. These are lenses, not a checklist.

After finding a new fact, ask only: **would another value make the Human accept a different Goal?** If not, stop expanding.

## When requirements conflict

If Human requirements cannot all hold at once, Goal must make clear what wins. That priority can come only from the Human, existing authority, or an unavoidable reality constraint; Prompt Atlas must not reorder it merely because one implementation is easier.

If reality resolves the conflict, converge directly. Otherwise surface the Human-owned conflict together with the main consequences and a recommendation.

## When to stop

When every remaining question can change only How rather than the Goal the Human will accept, stop Intent Research and return to Compile. New Unknowns during implementation are normal; Prompt Atlas does not need to eliminate them before execution.
