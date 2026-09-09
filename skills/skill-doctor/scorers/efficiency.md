---
name: Efficiency
description: Whether the agent worked directly toward its result, or wasted effort on redundant steps, avoidable rework, or unnecessary back-and-forth.
labels:
  - value: highly_efficient
    score: 1
  - value: mostly_efficient
    score: 0.8
  - value: mostly_inefficient
    score: 0.4
  - value: highly_inefficient
    score: 0.2
---

Score the full cost of reaching the result against what a competent engineer with the same tools should have needed.

Look for:

- rework caused by an earlier mistake or missing check;
- repeated Human correction or steering;
- re-reading, re-running, or re-searching already known information;
- broad operations when a targeted standard step was available;
- independent reads/searches/workstreams serialized without reason;
- retrying an unchanged failing approach or guessing instead of checking reality;
- verification that happened too late, or the same verification repeated without new evidence.

A single small slip with no downstream cost can still be `mostly_efficient`. Repeated waste or one avoidable rework cycle is normally `mostly_inefficient`; sustained looping or repeated Human correction is `highly_inefficient`.

Reason: 1–3 sentences naming the dominant waste, rough count, and likely fixable owner. Name an existing Skill when it should have prevented the waste.
