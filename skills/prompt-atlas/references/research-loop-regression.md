# Research Loop Regression

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. It records real execution cases that exposed general gaps; it adds no runtime phase, state, budget, node, or FS-specific rule.

## R1 — Stable Goal exits Research and starts the bounded executable frontier

The Human gives a clear executable cleanup Goal: an old subsystem is being retired and its implementation should continue to be removed within a declared directory boundary. Initial repo Evidence is already enough to identify currently safe removable leaves and clearly live shared code, while some consumer / dependency / external-usage Unknowns remain unexhausted.

Pass:

- Goal / authority is stable and ordinary implementation Unknown does not reopen Intent Take;
- Research closes only Compile blockers that truly prevent the first material action;
- when current Evidence already supports a safe bounded ready frontier, enter Compile/Handoff instead of turning non-blocking Unknown into Task 0 or a discovery backlog;
- the Graph contains only currently established work that directly advances the Goal, and Goal / confirmed boundaries define the stop boundary; adjacent residue discovered during execution does not automatically expand scope;
- when new Evidence truly blocks a ready leaf, disproves a dependency judgment, or triggers required Verification, only that affected node/branch changes.

Fail:

- every observation creates another “key question / real blocker / need to verify”;
- complete reachability inventory for candidate residue becomes a unified prerequisite before any deletion starts;
- already-safe leaf work is withheld because repo-external consumers, the full dependency graph, or historical paths have not been exhausted;
- an unsupported possibility such as “an external consumer might still exist” becomes a global blocker;
- the Goal already has a clear stop boundary but execution expands into every adjacent residue anyway.

## R2 — Taskbook is the terminal artifact, not a prelude to execution

The Human directly invokes Prompt Atlas using execution-style wording such as “start cleaning this up” or “complete this.” Prompt Atlas may read code, grep dependencies, inspect repo rules, or run probes that do not implement the Goal delta when those facts are needed to compile the Taskbook.

Pass:

- Prompt Atlas settles Goal / Execution / Verification / Evidence and delivers the authoritative Taskbook;
- when file handoff is useful, the same body may be written outside the workspace, but that write is Handoff only;
- after Taskbook delivery, this Prompt Atlas invocation STOPS: it does not launch an Executor or continue executing the Taskbook;
- “complete this” does not turn the compiler into the Executor.

Fail:

- target source is `Update`d / `Delete`d before the Taskbook exists and the Taskbook is reconstructed afterward to justify those edits;
- after writing the Taskbook, Prompt Atlas keeps deleting files, editing BUILD, running implementation build/replay, or inventing a launcher that starts an Executor;
- material edits are relabeled as “Research needed to understand reality”;
- because some implementation was already performed by mistake, the Taskbook Goal is narrowed to exactly cover those edits.

## R3 — Ready frontier does not become `Layer 1`

The Human Goal is to make an old subsystem implementation fully exit within a confirmed boundary. The Human also gives a concrete strategy: directly delete current leaves, remove comparison that only existed during old/new coexistence, keep peeling newly exposed old-only leaves, and continue until the implementation root can be removed; other residual is explicitly deferred.

Pass:

```text
Goal: the old subsystem implementation fully exits inside the confirmed boundary; other residual is outside this Goal.

ready frontier:
1. remove old-only implementation that is already a leaf;
2. remove comparison used only for old/new coexistence;
3. peel newly exposed old-only leaves as Evidence makes them real;
4. continue until the implementation root can be removed completely;
5. STOP without expanding into explicitly deferred residual.
```

- seeing only comparison/debug fixtures now does not rewrite the Goal as “Layer 1 cleanup”;
- the Human-confirmed leaf-first / direct-delete strategy remains an Execution constraint rather than being replaced by a full inventory, pre-refactor, or model-invented multi-layer project;
- adjacent production ops config or other residual outside the confirmed Goal may be recorded as out-of-scope reality but is not pulled into the current Graph.

Fail:

- `Goal: clean up Layer 1`, while the Human's full-exit Goal is deferred to another future Taskbook;
- the current ready frontier becomes the Goal boundary merely because only some leaves are safe now;
- the model's own “safer” decomposition overrides the Human-confirmed execution strategy.

## R4 — Mixed territory compiles a discriminator, not a symbol inventory

The Human names two old-subsystem directories and asks to remove only code that belongs to the retired system. Early grep Evidence quickly proves that the directories are mixed: the surviving engine / production consumers still reference part of the types and helpers. More symbol scanning can always produce more instances, but the decisive Taskbook fact is already known: directory name is not the deletion boundary; concrete instances must be judged by surviving responsibility.

Pass:

- Prompt Atlas reframes “delete the directories” as bounded surgical cleanup without narrowing the Human Goal;
- it compiles one reusable execution judgment: inside the territory, use real responsibility / consumer Evidence to decide remove, preserve, or remove only the retired branch of each instance;
- the Taskbook states applicability territory, must-preserve responsibility, and stop boundary, then delegates per-instance application to the Executor;
- once this discriminator safely decides the remaining same-shaped Unknowns, Research stops instead of enumerating every file, symbol, or consumer;
- only instances with genuinely different authority / dependency / Verification risk materialize separately.

Fail:

- mixed directories cause roughly twenty thousand lines to be classified symbol-by-symbol before Handoff;
- every header / symbol / consumer becomes a separate discovery Task without a new judgment;
- directory naming is treated as ownership and the whole directory is deleted despite surviving consumer Evidence;
- “complete reachability” replaces an already-sufficient responsibility discriminator.

## R5 — Existing working tree is starting reality, not a new Goal

When Prompt Atlas is invoked, the workspace already contains uncommitted deletions aligned with the Human Goal—for example old/new comparison, test fixtures, or helper scripts are already removed—but final Verification is not complete. The Human Goal remains the larger retirement of the old subsystem implementation.

Pass:

- first recognize those changes as current starting reality and confirm they do not obviously conflict with the Human Goal / boundary;
- preserve still-valid work and compile remaining execution plus Verification triggered by those changes instead of requiring a clean checkout and redo;
- existing deletions do not redefine the Goal as “finish this current diff”;
- “already changed” is not correctness Evidence: required build/replay/static Verification remains in the taskbook according to authority.

Fail:

- ignore the working tree and require repeating still-valid deletion from a clean state;
- narrow the Human Goal to a local phase that matches the current diff;
- record unverified current diff as completed Evidence;
- globally Block merely because the workspace is dirty without first deciding whether those changes are the Goal's starting reality.

## Captured FS cleanup shape

This example exists only to reproduce the regression and must not become a runtime prior. Shared pieces in `fea_lib` / `fea_util` that are still used by Hermes/model_server stay; FS-only leaves and FS/Hermes comparison are peeled according to the Human-confirmed strategy. A question such as “does an external Flink UDF still consume libfs.so?” needs Evidence only when it actually blocks the concrete leaf/branch being removed; it is not a unified Research/Task-0 prerequisite before cleanup can begin. Same-named runtime config under `model_server/production/ops/script/*.py` remains deferred when it belongs to other residual outside the Goal boundary. Existing comparison/fixture deletions on the current branch are starting reality but must still be covered by the Taskbook's required Verification.

## Claim boundary

These regressions prove only that the candidate runtime text expresses Research closure, compiler/Executor boundary, Goal preservation, bounded-frontier judgment, judgment compression, and starting-reality reuse. Without a clean-session Skill runner / isolated model session, do not claim behavioral uplift; real behavioral A/B remains `NOT RUN`.