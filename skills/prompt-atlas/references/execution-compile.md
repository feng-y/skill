# Autonomous Taskbook: compile a stable Goal into a decision-complete execution contract

Use only after Goal is settled. The Taskbook must let a fresh Executor complete the Goal independently **without pre-writing its patch**.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is compiler ownership / proof chain, not an output template. **Decision-complete does not mean information-complete.** Research may be deep; the Taskbook keeps only information that changes Executor judgment.

## Goal

Write one Human-owned Goal and make explicit:

- **Outcome** — the result property that must become true;
- **Decision priority** — the tradeoff order for conflicts, with unlisted cases delegated to the Executor under that order;
- **Allowed boundary** — territory where the Executor may keep discovering and acting;
- **Forbidden boundary** — territory that must not be touched or pulled in opportunistically;
- **Must-preserve** — behavior, APIs, data, verification authority, or other non-regression properties;
- final delivery.

Do not make a model-selected repository shape a success criterion by default. Directory disappearance, file moves, namespace renames, or a particular patch shape belong in Goal only when explicitly required by the Human, required by repo authority, or themselves part of the Goal invariant.

## Compile output filter

Compile is an output filter, not a Research transcription step. Every fact proposed for the Taskbook passes two questions:

1. Can the Executor reliably and cheaply recover it from authoritative repo reality? If yes, prefer the judgment/criterion over line numbers, inventories, and detail.
2. Would omitting it materially increase the chance of wrong scope, wrong change/preserve judgment, wrong Verification, or unsafe implementation? If yes, preserve that trap / counterexample / non-obvious reality.

Therefore:

- ordinary line numbers, include details, symbol counts, candidate patches, and recomputable inventories are omitted by default;
- terminology collisions, false dependencies, non-obvious surviving consumers, hard boundaries, and facts that change Verification triggers must be preserved;
- reproducible baseline counts may be preserved because they act as coverage / attribution anchors rather than background detail;
- **a candidate remains intelligence**: a Research name marked “probably dead / should reach zero” does not gain acceptance authority merely because it was discovered.

More Evidence should compress into fewer, more reliable judgments—not more instructions.

## Execution / Graph

The Taskbook normally keeps only a small number of **outcome + judgment work units**.

A Task should let the Executor scan and handle the full same-shaped surface under one stable judgment. Normally it needs only:

- the local outcome;
- applicability territory / starting reality only when omission would cause misjudgment;
- a stable judgment that repeatedly decides change / preserve / skip / block;
- hard constraints that truly reduce the choice space;
- already-binding Verification obligations that determine whether the work is valid.

**A Task is not an executable delta, file-path checklist, or predicted patch.** Enumerate paths/files only when the set is closed, cannot be reliably derived from the repo, and enumeration itself is the decision rule. For open surfaces, state the discriminator and let the Executor scan the full set; otherwise the N+1th same-shaped residual outside the checklist will be missed.

**Applying a judgment instance-by-instance does not mean compiling an instance-by-instance Evidence ledger.** The Executor gathers enough Evidence for the instances it changes; the Taskbook normally asks for a coverage oracle, machine-judgeable outcome, and material exceptions that prove the judgment covers the work surface. Require per-file/per-symbol keep-delete accounting only when closed-set reconciliation is itself acceptance, repo/Human authority requires it, or an instance has distinct safety / authority / Verification risk.

Research finding a high-confidence implementation does not make exact file decomposition, symbol destinations, extraction line ranges, include/BUILD rewrites, command order, or failure-localization tactics binding. Freeze How only when required by the Human, repo authority, real dependency/risk, or a uniquely safe route.

**Law and intelligence stay separate**: `must/must not` comes only from the Human, repo authority, or verified reality. A model-recommended route remains intelligence even at high confidence. The Executor may take a smaller, safer compliant path and records why in `implement-notes`.

**Escalate by authority, not uncertainty.** Ordinary factual / execution Unknowns stay with the Executor and are resolved through reality + judgment; do not create a `Needs-human-decision` list for them. Escalate only when resolving the item requires changing Goal / boundary / Human requirement / priority / authorization. If only a fact is unavailable and no safe work remains, Block accurately with a resume condition.

Group instances covered by one judgment. Split only when outcome, judgment, dependency, authority, risk, or required Verification genuinely differs. Graph expresses only real dependency / parallel / join relations that change execution judgment; do not fragment work merely to make Graph precise.

Preserve Human-confirmed strategy / scope boundary / must-preserve constraints. The ready frontier says what can execute now and does not redefine the Human Goal. Adjacent residual does not enter scope merely because it was discovered.

Still-valid workspace changes aligned with the Goal are starting reality. Reuse them; do not redo them or shrink the Goal around them. “Already changed” is not correctness Evidence.

**Task 0** exists only when a missing execution-time fact blocks the first safe material work, or required Verification explicitly requires a trigger before material work. It is not continued Research, an inventory, or a default checklist.

## Starting baseline

Establish an attributable starting point when the environment is available. Actually run build/test/replay/static probes that matter for judging the task. When scope needs measurement, prefer reproducible signals—target count, grep hit count, file/line magnitude, measurement time—over full path inventories.

Keep only baselines that let the Executor recompute scope, detect omissions, or distinguish pre-existing breakage from regressions introduced by this work. If a command was not actually run, a number cannot be confirmed, or the environment is unavailable, do not fabricate it. Future commands named in the Taskbook must at least be confirmed to exist with credible targets/arguments; use Task 0 when the check must happen before material work.

**Any baseline compiled into the Taskbook as a scope / coverage / attribution premise must be recomputed by the Executor with the same authoritative probe before the first affected material work.** On mismatch, do not keep using the old value as truth: immediately mark dependent assumptions / Evidence stale, pause work that depends on that premise, and repair affected Execution / Verification from current reality. Unrelated work / Evidence remains reusable. The Taskbook must not weaken this gate to “report the difference, then continue,” and the gate does not mechanically turn every task into Task 0.

## Verification

Verification freezes **what must be proven**, not **how implementation/debugging should proceed** by default.

- Task — include a local check only when it is already binding and controls progression;
- Task Group / join — include separate proof only when combined behavior genuinely needs it;
- Goal — preserve delivery coverage required by repo authority or explicit Human requirements.

When provider, target, or scope depends on change surface / binding / runtime reality, compile the stable trigger/authority and let the Executor materialize the concrete action after it triggers. cleanup/refactor/expected `0-diff` cannot downgrade already-triggered required Verification.

**Do not turn Research candidates into a hard-zero list.** A concrete symbol/file/config may become a `0-hit / 0-count` acceptance item only after it is established to belong to the target responsibility and its disappearance is part of the Goal/Verification claim. If “dead vs live/mixed” is still execution-time judgment, compile the predicate and coverage oracle instead: every instance proven target-only must disappear, while surviving/mixed exceptions remain. Do not pre-name candidates and force them to zero.

Tactics such as “build after every moved type” or “test after every edited file” belong to the Executor by default. They become binding only when repo/Human authority or a specific risk requires them.

Read [verification-trust.md](verification-trust.md) only when judge trust genuinely needs strengthening.

## Evidence

Compile proof / trust requirements, not future results. Evidence needed for final judgment must be reviewable and cover the real claim. Executor narration or self-declared `PASS` is not Evidence. Reuse Evidence while its premises remain valid; new Evidence invalidates only affected conclusions.

The default Evidence shape is **judgment + coverage oracle + material exceptions + Verification result**. Do not demand a final “delete/keep + grep output” ledger for every symbol/file on an open surface merely to look rigorous; that turns judgment back into a checklist. Require per-instance accounting only for closed-set reconciliation, audit authority, or genuinely different instance risk.

## Completion Hook

The Taskbook carries a stop judgment without adding a Completion layer. Completion defines both success and failure paths.

### Success

Read only **Goal / constraints + triggered required Verification + current valid Evidence**:

- whether the Goal's material outcome has minimum sufficient Evidence;
- whether higher-priority properties in the decision order were not sacrificed to lower-priority goals;
- whether must-preserve / allowed+forbidden boundaries / authority still hold;
- whether every triggered required Verification obligation has trustworthy Evidence.

Only then `STOP`.

### Failure / stop-loss

- After the same acceptance path fails three consecutive times without new Evidence, stop brute-forcing it: switch to independent work, change strategy with evidence, or report the exact non-PASS/blocker;
- if a trustworthy green baseline turns red, restore green before continuing where possible; if restoration fails, report the regression honestly rather than declaring completion;
- “not finished but accurately explained” is better than “finished but worse”;
- never manufacture PASS via `.skip` / `todo`, weakened assertions, deleting live tests, mocking away the target, changing thresholds, swallowing failures, `|| true`, or any other judge weakening. Tests may be deleted with their dead subject only when the Goal / dead-code judgment justifies it and the count can be reconciled.

## Durable execution state

Start by writing ≤10 lines of Goal / execution order / largest risk into the existing `implement-notes`, then keep execution progress, new Unknowns, blockers, material decisions/Evidence, and resume point there. A new session reads it first and redoes only work whose premises changed or whose Evidence became invalid. Conversation is not the sole state store.

## Handoff check

Before delivery, ask only:

- Does Goal describe an outcome, or did a model-selected implementation shape get smuggled in as success?
- Is the decision priority clear enough to adjudicate unlisted cases?
- Are allowed and forbidden boundaries both explicit?
- Does the Taskbook define the task instead of exposing Prompt Atlas research?
- Is each Task an outcome + judgment rather than a file/function/checklist/patch step?
- Does an open same-shaped surface get scanned by criterion instead of static inventory?
- Did “instance-by-instance judgment” accidentally become an instance-by-instance Evidence ledger?
- Did an ordinary factual/execution Unknown get mislabeled as a Human decision?
- Does every `must/must not` have authority, or did model intelligence get promoted into law?
- Are traps that would cause wrong judgment preserved while safely recomputable detail is removed?
- Are baselines reproducible with a mismatch gate that stales / pauses / repairs affected state rather than “report then continue”?
- Is every concrete object in a hard-zero / zero-hit acceptance check already proven to belong to the target responsibility rather than being a Research candidate?
- Does Verification freeze required proof without turning debugging tactics into hard workflow?
- Does Completion include success, stop-loss, rollback, and judge-integrity paths?
- Do execution Unknowns have an `implement-notes` resume carrier?

Autonomous-execution Taskbooks default to **≤4000 characters**. Relax only when the Human explicitly asks for a long-form artifact or the target runtime is known to use a different limit. If it does not fit, compress judgments / deduplicate / remove recomputable detail first; do not split one Human Goal into artificial layer Goals to fit the limit.

If deleting a passage does not change the Executor's Goal, boundary, judgment, verification, failure handling, or resume behavior, delete it.