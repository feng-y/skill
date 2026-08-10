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

## R6 — Deep research compresses into task definition, not implementation design

Prompt Atlas has researched deeply: it knows which surviving types must remain, which dead chain can be removed, which includes/BUILD/registrations may be affected, and can propose a complete relocation plan. Research quality is high, but the Human only asked to retire the old subsystem implementation within a confirmed boundary while preserving surviving behavior.

Pass:

- the final Taskbook keeps only a few work units, for example coexistence-comparison cleanup, old implementation retirement, and direct residual cleanup;
- mixed code uses one stable judgment: retired-only remove, surviving responsibility preserve, mixed remove only the retired part, insufficient evidence preserve or accurately block;
- “surviving responsibility must remain” is binding, but exact destination files, extracted line ranges, and include rewrites are implementation hypotheses and are not mandatory by default;
- Graph keeps only real work-unit dependencies rather than expanding into an A1–A5/B1–B7 patch schedule;
- Verification freezes required build/test/replay/dead-reference coverage, not failure-localization tactics such as building after every moved type;
- line numbers, symbol counts, and include inventories from Research enter the Taskbook only when they truly change judgment.

Fail:

- the Taskbook prescribes exact destination files for surviving types, precise line extraction, and include edit lists even though neither Human nor repo authority requires that patch shape;
- one high-confidence viable plan becomes the authoritative execution path and the Executor is forced to prove the predicted patch;
- every file move, function extraction, BUILD edit, and scan becomes a separate Graph node;
- debugging-friendly intermediate build/test order is promoted into required Verification;
- deeper Research produces a longer Taskbook with more instructions instead of compressing into fewer, more reliable judgments.

Expected abstraction level is close to:

```text
Goal: retire old implementation inside the confirmed boundary while preserving surviving behavior.

Work 1: remove old/new coexistence comparison.
Work 2: inside the implementation territory, repeatedly apply responsibility judgment to remove retired-only code; preserve surviving/mixed responsibility and let the Executor choose the minimum safe implementation.
Work 3: clean direct init/startup/tools/tests/build-registration residual under the same dead/live judgment without expanding into unrelated residue.

Verification: repo-required build/tests + affected behavior replay/equivalent evidence + dead-reference closure.
```

## R7 — Leader-parity contract covers unlisted execution reality without a checklist

In the same FS cleanup case, Research has measured starting build/test/hit counts, found a terminology collision with another live system / same-named replay app, and observed that target directories contain both dead FS-only code and surviving shared code, including some false dependencies where files are included but none of their symbols are actually used.

Pass:

- Goal is “retire FS-only implementation while preserving surviving behavior,” not “make two directories disappear”;
- Goal includes a clear tradeoff order such as `behavior preservation > correct deletion boundary > amount removed`, and the Executor adjudicates unlisted cases with it;
- allowed and forbidden territory are both explicit, and same-named objects belonging to feature streaming / another live runtime are placed outside the cleanup boundary;
- Tasks use outcome + dead/live responsibility judgment to drive a full-surface scan instead of treating the currently known B1–B7 paths as a closed checklist;
- reproducible baselines (green build, target count, grep hit count, directory magnitude) anchor starting-state confirmation and omission detection; ordinary line numbers/include inventories stay out;
- non-obvious traps remain when omission would cause a wrong decision, e.g. an include that is a false dependency with zero actual symbol use;
- Completion includes both success and failure routes: required proof, three-failure stop-loss, green→red rollback / honest non-PASS, and anti-cheat against `.skip`, weakened assertions, live-test deletion, mocking away the target, or `|| true`;
- runtime Unknown / progress / blocker / resume point is persisted in the **single durable carrier selected by Compile/Handoff**. Prefer Human/repo authority or an established repo/runtime convention, and fall back to `implement-notes` only when no existing carrier exists. A new session resumes from that same carrier rather than creating a second protocol.

Fail:

- deeper Research produces a larger fact dump instead of a smaller judgment contract;
- “directory disappearance” still forces unnecessary relocation of live symbols;
- only forbidden scope is given and the Executor must infer what territory it may keep scanning;
- current path inventory is treated as the whole job, so same-shaped residual outside the checklist is not discovered;
- the taskbook says only “non-PASS cannot stop” and gives no stop-loss / rollback / honest failure path;
- terminology collisions are not isolated and the Executor can operate on the wrong live `fs` object;
- execution Unknown exists only in conversation and is rediscovered after interruption.

## Captured FS cleanup shape

This example exists only to reproduce the regression and must not become a runtime prior. Shared pieces in `fea_lib` / `fea_util` that are still used by Hermes/model_server stay; FS-only leaves and FS/Hermes comparison are peeled according to the Human-confirmed strategy. A question such as “does an external Flink UDF still consume libfs.so?” needs Evidence only when it actually blocks the concrete leaf/branch being removed; it is not a unified Research/Task-0 prerequisite before cleanup can begin. Same-named runtime config under `model_server/production/ops/script/*.py` remains deferred when it belongs to other residual outside the Goal boundary. Existing comparison/fixture deletions on the current branch are starting reality but must still be covered by the Taskbook's required Verification.

## Claim boundary

These regressions prove only that the candidate runtime text expresses Research closure, compiler/Executor boundary, Goal preservation, bounded-frontier judgment, judgment compression, starting-reality reuse, taskbook compression, and Leader-parity failure/resume judgment. Without a clean-session Skill runner / isolated model session, do not claim behavioral uplift; real behavioral A/B remains `NOT RUN`.