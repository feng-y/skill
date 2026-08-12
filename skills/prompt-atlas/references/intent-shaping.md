# When the Human has not decided Goal

Read only when `SKILL.md` has already checked reality but still cannot tell which Goal the Human would accept.

The prompt, current plan, and Prompt Atlas itself are only maps. The repo, runtime, historical constraints, and real users can expose something the map omitted. The aim is not to enumerate every uncertainty; it is to find **the choice that can change Goal**.

## Find the choice, not more information

For every new fact ask:

> If this fact had a different value, could the Human accept a different Goal?

If not, leave it to the Executor or ignore it. If yes, keep investigating.

Business or compatibility constraints, existing specs and prior decisions, real consumers, external contracts, and current workspace state can all hide such a choice, but they are places to inspect on demand rather than a checklist.

## Let reality answer first

If reality can settle the fact, probe it instead of asking the Human to guess. Reality may invalidate a proposed means, but it cannot silently rewrite Goal.

If reality removes the fork, return to the main flow and Compile. Only when several materially different Goals still remain plausible and reality cannot decide between them should Prompt Atlas surface those choices together, with consequences and a recommendation when useful.

## Stop when only How remains

Once the remaining uncertainty can change only How rather than Goal, stop Research. New questions during implementation are normal; Prompt Atlas does not need to eliminate them in advance.
