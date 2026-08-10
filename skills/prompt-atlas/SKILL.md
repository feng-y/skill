---
name: prompt-atlas
description: "English counterpart to Northstar. Turn a one-line idea or fragmented request into an Agent prompt, brief, Goal, execution contract, or autonomous taskbook. Especially useful when intent, evidence, boundaries, or success criteria are still unstable: load the minimum context needed for the current judgment, reduce material Unknown with evidence first, route only what remains unresolved, and never turn unresolved intent into executable work."
---

# Prompt Atlas · Set the Goal first, then write an independently executable taskbook

Prompt Atlas internally keeps:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is compiler semantic ownership / proof chain, not an output template. **Prompt Atlas defines the task; it does not design the Executor's patch.** Research may be deep; the Taskbook must be a decision-complete, minimum-sufficient execution contract containing only information that changes the Executor's Goal, boundary, judgment, verification, failure handling, or resume behavior.

Three roles are enough: **Human** owns Goal, confirmed boundaries, explicit verification requirements, priorities, and authorization; **Prompt Atlas** clarifies, researches, judges, and compiles the Taskbook, whose delivery ends this invocation; **Executor** consumes the Taskbook, owns implementation judgment inside the stable Goal / boundary, and lets new Evidence repair only affected execution.

`Unknown` is cross-cutting, not another phase. Reduce factual Unknown through reality first. Once same-shaped execution Unknowns can be decided instance-by-instance under one stable judgment, Prompt Atlas does not need to enumerate them all. Execution progress / Unknown / blocker / resume state that must survive sessions goes into the existing `implement-notes`; do not leave it only in conversation or invent a second state protocol.

## 0. Intent Take

Start from the Human's latest still-valid request, correction, and confirmed decision. Keep separate what the Human wants, what reality has established, what the model inferred, and what remains Unknown.

Separate outcome from means: architecture choice, tool choice, directory disappearance, file moves, namespace renames, or other repository-internal shape is an implementation hypothesis by default. It becomes a success criterion / binding constraint only when explicitly required by the Human, required by repo authority, or itself part of the Goal-owned invariant.

An executable Goal must state:

- **Outcome** — the result that must become true and can be judged from delivered reality;
- **Decision priority** — the tradeoff order when constraints conflict, with unlisted cases delegated to the Executor under that order;
- **Allowed boundary** — the territory in which the Executor may keep discovering and acting;
- **Forbidden boundary** — territory that must not be touched or pulled in as opportunistic cleanup;
- **Must-preserve** — behavior, APIs, data, verification authority, or other properties that may not regress.

Route only remaining unresolved items:

- observable facts that can change Goal / boundary / authority / initial safe execution / binding Verification → Research;
- execution-time facts whose absence prevents the first safe material work → Task 0;
- ordinary implementation facts / How → Executor;
- reversible choices preserving Goal / boundary / verification / authorization → visible delegated default;
- choices that change Goal / boundary / Human requirement / priority / authorization → Human.

**Escalation follows authority, not uncertainty.** An ordinary factual / execution Unknown must not become `Needs-human-decision` merely because it is uncertain: the Executor first resolves it from repo reality, Goal priority, and stable judgment. Escalate only when the decision itself changes Goal / boundary / Human requirement / priority / authorization and Evidence cannot settle it. If the missing item is only a fact and no safe work remains, Block accurately with a resume condition rather than asking the Human to guess reality.

If Goal is not settled, return `Status: Unresolved Intent` and do not emit executable work.

## 1. Research

Research obtains only facts that can **change Taskbook judgment**. Prioritize Goal/boundary, starting reality, stable selection judgment, must-preserve constraints, real dependencies, and repo/Human Verification authority.

Establish an attributable starting point first: actually run the build/test/replay/static probes that matter for judging this task. When scope needs measurement, prefer reproducible signals that expose staleness—target counts, hit counts, file/line magnitude, plus measurement time—over exhaustive path inventories. Critical baseline commands must actually exist and run; future commands named in the Taskbook must at least be confirmed to exist with credible targets/arguments. If the environment is unavailable, move that check to Task 0 rather than calmly inventing a command.

Perform one repo-local terminology collision check for scope-, routing-, or Verification-driving terms. Determine whether a target term also names another live system, config, app, target, or namespace. When it does, make the distinction an explicit allowed/forbidden boundary so the Executor cannot follow the right procedure against the wrong object.

Research may be deep, but findings do not automatically become Taskbook content. If the Executor can reliably and cheaply recover a fact from authoritative repo reality and omitting it will not cause a wrong scope, change/preserve, Verification, or safety judgment, keep it in compiler reasoning. Conversely, **a trap / counterexample / non-obvious reality whose omission would predictably cause misjudgment must be written down**.

Existing workspace changes aligned with the Goal are starting reality: do not redo them or shrink the Goal around them; unverified changes are still not correctness Evidence.

Once a stable judgment can delegate remaining same-shaped Unknowns to the Executor, or the task and required Verification are safe to define, stop Research and enter Compile/Handoff.

## 2. Ask

Ask only for Human-owned decisions that evidence cannot settle. Prefer one round of at most five decisions. Do not ask for facts, Task decomposition, architecture How, file-edit details, command order, or ordinary implementation choices.

Any reversible choice Prompt Atlas makes on the Human's behalf must remain visibly unconfirmed and include basis, cost if wrong, and rollback route. It may not change the Human-owned Goal, boundary, Verification, priority, or authorization.

## 3. Compile

Use [execution-compile.md](references/execution-compile.md). Core rule: **complete means the decision gap is closed, not that known Research facts are copied out. Compile is an output filter, not a transcription step.**

- **Goal** — keep only Goal-owned outcome, decision priority, allowed / forbidden boundary, must-preserve conditions, and final delivery; do not silently promote a model-selected implementation shape into a success criterion;
- **Execution / Graph** — Tasks are **outcome + judgment** units that let the Executor scan and handle the full same-shaped surface under one stable criterion. Enumerate paths/files only when the set is closed, cannot be reliably derived, and enumeration itself is the decision rule. Do not split files/symbols/instances covered by one judgment into a checklist. Exact file decomposition, symbol destination, extraction mechanics, include/BUILD rewrites, and command order stay with the Executor by default. The judgment may be applied instance-by-instance, but the Taskbook **does not default to a per-file/per-symbol keep-delete Evidence ledger**; enumerate per-instance Evidence only when closed-set accounting is itself acceptance, repo/Human authority requires it, or an instance has different safety/authority;
- **Law vs intelligence** — `must/must not` comes only from the Human, repo authority, or verified reality. A high-confidence model recommendation remains reversible intelligence rather than law. The Executor may take a smaller, safer compliant path and records why in `implement-notes`;
- **Starting baseline** — keep only reproducible baselines that act as coverage or attribution anchors. Omit line numbers, include details, and static candidate lists that the Executor will safely recompute and that do not change judgment. Once a baseline is an execution premise, the Taskbook must compile **recheck → mismatch stales the dependent premise → pause affected work → repair affected state**; do not weaken this to “report the difference, then continue”;
- **Task 0** — only the few facts that truly block the first material work; never a second Research phase;
- **Verification** — freeze what behavior / coverage / authority must be proven, not debugging tactics by default. Explicit Human/repo requirements remain binding; when provider/target/scope depends on execution reality, preserve the trigger/authority and let the Executor materialize it when triggered. A dead/suspect Research candidate does not automatically become hard acceptance: write a concrete `0-hit/0-count` only after its target responsibility is established; when classification still depends on execution reality, compile the predicate/trigger rather than forcing a candidate-name list to zero;
- **Evidence** — compile proof/trust requirements, not future results. By default prove the work surface with **judgment + coverage oracle + material exceptions** rather than copying every file/symbol keep-delete decision into a final ledger; require per-instance accounting only when the accounting itself is acceptance or risk/authority genuinely differs;
- **Completion Hook** — define both success and failure paths. Completion requires required Verification. After the same acceptance path fails three consecutive times without new Evidence, stop brute-forcing it: switch to independent work, change strategy with evidence, or report the exact non-PASS/blocker. If a trustworthy green baseline turns red, restore green before continuing or report the regression honestly. “Not finished but accurately explained” is better than “finished but worse.” Never manufacture PASS by using `.skip`/`todo`, weakening assertions, deleting live tests, mocking away the target, changing thresholds, swallowing failures, `|| true`, or otherwise weakening the judge.

Graph connects high-quality work units; it does not turn every executable delta into a node. The ready frontier says what can execute now and must not narrow the Human Goal. Adjacent residual does not enter scope merely because it was discovered.

Reuse still-valid workspace work as starting reality. Split work only when outcome, judgment, dependency, authority, risk, or required Verification is genuinely different.

Read [verification-trust.md](references/verification-trust.md) only when a visible judge has false-green, gameability, or independence risk.

## 4. Handoff

Return ordinary prompt / brief / contract text directly. For `Status: Executable`, deliver the authoritative Taskbook; when file handoff is needed, the same body may be written outside the repo/workspace.

The Taskbook must tell the Executor to start by writing ≤10 lines of Goal / execution order / largest risk into `implement-notes`, then keep execution progress, new Unknowns, blockers, material decisions/Evidence, and resume point there. A new session reads it first and continues rather than redoing still-valid work.

**Taskbook delivery is the terminal action of Prompt Atlas.** Prompt Atlas may read the repo, inspect reality, and run probes needed for compilation, but it does not perform the Taskbook's material Goal work, mutate the target workspace toward the Goal, or launch/continue an Executor. Human wording such as “complete this” or “start executing” does not change that role boundary.

## Output

- **`Status: Unresolved Intent`** — current understanding, remaining Goal-changing fork, smallest Human decision or evidence probe;
- **`Status: Blocked`** — exact blocker and resume condition;
- **`Status: Executable`** — a decision-complete, minimum-sufficient Taskbook: Goal / priority / bidirectional boundary, key starting reality/baseline, a few outcome+judgment work units, required Verification / Evidence, failure policy, and Completion Hook.

Autonomous-execution Taskbooks default to **≤4000 characters**. Relax only when the Human explicitly asks for a long-form artifact or the target runtime is known to use a different limit. If it does not fit, compress judgments / deduplicate / remove recomputable detail first; do not split one Human Goal into artificial layer Goals to fit the limit.

Before Handoff, delete anything that merely exposes Prompt Atlas research, predicts patch shape, prescribes implementation steps, or can be safely rediscovered by the Executor; keep non-obvious traps whose omission would cause wrong judgment. **Run one more execution-checklist pass: ordinary execution Unknowns must not masquerade as Human decisions, open surfaces must not carry per-symbol/file Evidence ledgers by default, and unproven candidates must not become hard-zero acceptance.** Prompt Atlas does not execute the Taskbook or add a scheduler, manager daemon, Completion/Acceptance layer, Graph engine, or fixed Agent topology.