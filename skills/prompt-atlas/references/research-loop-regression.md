# Research Loop Regression

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. It records one real execution case that exposed a general loop gap; it adds no runtime phase, state, budget, node, or FS-specific rule.

## R1 — Stable Goal exits Research and starts the bounded executable frontier

The Human gives a clear executable cleanup Goal: an old subsystem is being retired and its implementation should continue to be removed within a declared directory boundary. Initial repo Evidence is already enough to identify currently safe removable leaves and clearly live shared code, while some consumer / dependency / external-usage Unknowns remain unexhausted.

Pass:

- Goal / authority is stable and ordinary implementation Unknown does not reopen Intent Take;
- Research closes only Compile blockers that truly prevent the first material action;
- when current Evidence already supports a safe bounded ready frontier, Compile/Run starts directly instead of turning non-blocking Unknown into Task 0 or a discovery backlog;
- the Graph contains only currently established work that directly advances the Goal, and Goal / confirmed boundaries define the stop boundary; adjacent residue discovered during execution does not automatically expand scope;
- when new Evidence truly blocks a ready leaf, disproves a dependency judgment, or triggers required Verification, only that affected node/branch changes;
- runtime Evidence adjusts only affected contingent / invalidated Execution / Verification.

Fail:

- every observation creates another “key question / real blocker / need to verify”;
- complete reachability inventory for candidate residue becomes a unified prerequisite before any deletion starts;
- already-safe leaf work is withheld because repo-external consumers, the full dependency graph, or historical paths have not been exhausted;
- an unsupported possibility such as “an external consumer might still exist” becomes a global blocker;
- the Goal already has a clear stop boundary but execution expands into every adjacent residue anyway.

## Captured FS cleanup shape

This example exists only to reproduce the regression and must not become a runtime prior. For this case, expected execution judgment should be close to:

```text
Goal: make the FS implementation fully exit within this bounded effort; handle other residue separately later.

ready frontier:
1. directly remove FS-only implementation that is already a leaf;
2. directly remove comparison logic that existed only for FS / Hermes coexistence;
3. keep peeling newly exposed FS-only leaves as deletions progress;
4. continue until the FS implementation can be removed completely;
5. STOP without expanding into residue unrelated to this bounded exit.
```

Shared pieces in `fea_lib` / `fea_util` that are still used by Hermes/model_server stay. Questions such as “does an external Flink UDF still consume libfs.so?” need Evidence only when they actually block the concrete leaf/branch being removed; they are not a unified Research/Task-0 prerequisite before the cleanup can begin.

## Claim boundary

This regression proves only that the candidate text expresses the intended Research-closure and bounded-frontier judgment. Without a clean-session Skill runner / isolated model session, do not claim behavioral uplift; real behavioral A/B remains `NOT RUN`.
