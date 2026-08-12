# When the Human has not decided the outcome

Read only when `SKILL.md` has already checked reality but still cannot tell which final result the Human would accept.

The prompt, current plan, and Prompt Atlas itself are only maps. The repo, runtime, historical constraints, and real users can expose something the map omitted. The goal here is not to enumerate every Unknown; it is to find **the missing choice that can change what the Human calls done**.

## Find the choice, not more information

For every new fact ask:

> If this fact had a different value, could the Human accept a different completed outcome?

If not, it is not an intent-shaping problem; leave it to the Executor or ignore it. If yes, keep investigating.

Business or compatibility constraints, existing specs and prior decisions, real consumers, external contracts, and current workspace state can all reveal such a choice, but they are places to look rather than a mandatory checklist.

## Let reality answer first

If repo/runtime evidence can settle the fact, probe it instead of asking the Human to guess. Reality may invalidate a proposed means, but it cannot silently rewrite the Human's outcome.

If reality removes the fork, return to the main flow and Compile. Only when several materially different completed outcomes still remain plausible and reality cannot decide between them should Prompt Atlas surface those choices together, with consequences and a recommendation when useful.

## Stop when only How remains

Once the remaining uncertainty can change only how the work is implemented, stop Intent Research. Unknowns appearing during implementation are normal; Prompt Atlas does not need to eliminate them in advance.
