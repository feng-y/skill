# Skill improvement guidelines

Adapted from Warp Skill Doctor.

1. Cluster findings by root cause after attribution, across scorers and sessions.
2. Prioritize by frequency × severity.
3. Verify every finding against the current repo and current agent configuration before proposing edits. Drop findings that no longer reproduce or whose owner is elsewhere.
4. State the intended behavioral rule and owning surface in one sentence, then make the smallest change that expresses it.
5. Prefer replacing existing guidance over appending another paragraph.

Propose a Skill edit only when all are true:

- the failure is caused by a missing, wrong, or underspecified instruction on a concrete owning surface;
- the reusable rule and owner can be named;
- if that rule had been present and followed, the scored failure would have been prevented;
- the gap repeats across runs, or one occurrence is severe enough to prove a missing contract.

Do **not** edit when:

- the existing instruction already required the correct behavior and the model ignored it;
- the evidence is model variance rather than an instruction gap;
- the proposed fix merely restates, hedges, or copies examples from the observed runs;
- the real owner is product, infra, tool/runtime, scorer, or code outside instruction surfaces.

No change is a valid result. A speculative rule is worse than none.
