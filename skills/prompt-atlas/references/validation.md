# Prompt Atlas Validation

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. This file freezes semantics that already exist in the current runtime; it adds no phase, state, node, workflow, or output schema.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is compiler ownership / proof chain, not an output template. Validation asks whether the Taskbook covers the Executor's real decisions with minimum-sufficient information, not whether it looks information-complete.

## Static smoke

1. **Goal fidelity**: Goal is a Human-owned outcome, not a model-selected patch shape. Directory disappearance, file moves, or namespace changes become success criteria only when Human/repo authority requires them or the shape itself is a Goal invariant.
2. **Decision priority**: when Goal properties may conflict, the Taskbook carries a precedence order so unlisted cases can be decided without enumerating every contingency.
3. **Bidirectional boundary**: both allowed territory and forbidden territory are clear; absence from a blacklist does not imply permission across the repo.
4. **Compile output filter**: Research findings do not automatically survive into the Taskbook. Details that can be cheaply and reliably recomputed from authoritative repo reality are omitted when their absence will not mislead judgment; traps whose omission can cause wrong scope/preserve/remove/Verification decisions must remain.
5. **Decision-complete, not information-complete**: necessary work/relations already established by current Evidence must not be hidden merely for progressive execution, but file/symbol/line/include inventories and patch plans do not gain output authority merely because Research knows them.
6. **Task abstraction / Executor judgment**: Tasks are outcome + judgment. An open same-shaped surface covered by one discriminator is scanned by the Executor; enumerate paths/files only when the set is closed, cannot be reliably inferred, and enumeration itself is the decision rule. Ordinary technical Unknowns stay with the Executor whenever Goal/priority/boundary/authority already support a safe decision; unresolved status alone does not make them Human decisions.
7. **Law vs intelligence**: `must/must not` comes only from Human, repo authority, or verified reality. High-confidence model implementation advice remains reversible intelligence.
8. **Graph discipline**: Graph expresses only real dependency / parallel / shared-write / join relations. It does not turn executable deltas, Verification, Evidence, or Completion Hook into nodes or create a Graph engine/scheduler. Necessary relations already known and stable are expressed once, without using “complete” as a reason to enumerate patch detail.
9. **Starting baseline**: keep only reproducible baseline signals that act as coverage or attribution anchors; never invent commands/targets. Any baseline used as a scope/coverage/attribution premise must be recomputed with the same authoritative probe before the first affected material work. A mismatch stales dependent assumptions/Evidence and pauses work that depends on that premise until affected state is repaired from current reality; unrelated work/Evidence remains reusable.
10. **Verification authority**: freeze what must be proven, not debugging workflow. Scope follows real reachability/effective binding/repo authority; cleanup/refactor/expected `0-diff` cannot downgrade triggered requirements.
11. **Evidence / provider validity**: Evidence must be reviewable and cover the judgment and completion claim; open surfaces do not default to per-file/per-symbol ledgers. test/build/replay/static providers are claims until shown to actually run, cover the claim, and propagate failure. Self-reported `PASS` is not Evidence.
12. **Judge integrity**: green created through `.skip`/todo, weakened assertions, deletion of live tests, mocking away the subject, threshold changes, swallowed errors, or `|| true` is invalid. Reverse/private/independent Evidence activates only when real false-green/gameability risk requires it.
13. **Completion success path**: `STOP` only when Goal / constraints + triggered required Verification + current valid Evidence close coverage. Empty Tasks/frontier is not completion by itself.
14. **Completion failure path**: after the same Verification fails three times with no new Evidence, stop pushing the same route; switch to an evidence-backed strategy/independent work or report accurate non-PASS. If a trusted baseline goes green→red, restore it or report the regression honestly.
15. **Durable state**: execution progress, new Unknowns, blockers, key decisions/Evidence, and resume point live in existing `implement-notes`; a new session restores it instead of using conversation as the only state.
16. **Taskbook size**: autonomous Taskbooks default to ≤4000 characters; compress judgment and remove duplication rather than splitting one Human Goal into artificial layers.
17. **Role boundary**: Taskbook delivery ends Prompt Atlas. It may inspect reality/run probes for compilation, but it does not perform material Goal work, mutate the target workspace toward the Goal, or launch an Executor.

Static smoke must be **17/17 PASS** before behavioral comparison.

## Scenario smoke

### S1 — Simple local bugfix stays simple
A local bugfix has one outcome, one direct test, and no real Graph relationship.

PASS: one linear outcome+judgment Task plus minimum-sufficient Verification. The new contract must not force priority tables, Graph structure, full baselines, or cleanup-style checklists into a simple task.

### S2 — Deep Research compresses instead of expanding
Research knows exact line numbers, include/BUILD edits, and a high-confidence patch plan.

PASS: the Taskbook keeps only outcome, boundary, traps, judgment, and required Verification that change Executor decisions; implementation design stays with the Executor. Deeper Research must not mechanically make the Taskbook longer.

### S3 — Internal shape is not silently promoted to Goal
The Human asks to retire old FS implementation while preserving surviving behavior; target directories still contain live shared symbols.

PASS: “directory must disappear” is not silently promoted into success criteria and does not force live-symbol relocation. If the Human explicitly requires package removal or one-way dependency as an architecture invariant, that internal shape may legitimately be part of Goal.

### S4 — Open surface keeps the judgment
Retired-subsystem residue is spread across files. Research found B1–B7 and there are still same-shaped instances whose dead/live status is not yet classified.

PASS: the Task states outcome + dead/live responsibility judgment and the Executor scans the full territory. B1–B7 do not become a closed task list, and unclassified instances do not become Human decisions merely because their status is not known yet. Evidence proves the discriminator, material exceptions, and final coverage rather than requiring a delete/preserve ledger for every symbol.

### S5 — Non-obvious trap survives output filtering
A file includes an old FS header but actual symbol use is zero; another same-named `fs` object belongs to live feature streaming/replay.

PASS: ordinary include inventory can disappear, but “include is a false dependency” and “same-name live system is forbidden” must survive because omission would cause wrong preserve/delete decisions.

### S6 — Baseline recheck gates stale execution
The Taskbook carries reproducible build-green, target-count, and grep-hit baselines and uses them as scope/coverage/attribution premises. Reality changes after Handoff but before material work, so a material count/binding no longer matches.

PASS: before the first affected material work, the Executor reruns/recomputes the baseline with the same authoritative probe. A mismatch immediately stales dependent assumptions/Evidence, pauses work that depends on that premise, and repairs affected Execution / Verification from current reality. Unrelated work/Evidence continues; the gate must not mechanically turn every task into Task 0.

### S7 — Known work is not artificially lazy
Current Evidence already proves `A → {B,C} → D` work exists with real dependencies; future contingent work may still appear.

PASS: compile the currently known decision-complete work/relations once. Do not expose only A, and do not guess all contingent future or enumerate patch detail in the name of completeness.

### S8 — Runtime Evidence changes only affected state
After A, a new consumer C appears, or authoritative reality disproves an old dependency.

PASS: add/remove/reorder only affected remaining Execution / Verification. Goal and unaffected Evidence remain stable; do not recompile the whole project from scratch.

### S9 — Verification follows real production reachability
Cleanup touches a shared owner still bound to a Hermes production consumer; repo authority requires affected replay.

PASS: behavior Evidence is required; expected `0-diff` cannot downgrade it. Counter-case: when authoritative Evidence proves truly offline/dead code, replay must not be mechanically required.

### S10 — Provider exists in name only
The Taskbook names `./verify.sh`, but the execution environment does not have it or it always exits 0.

PASS: the provider yields no Evidence. Use a repo-authoritative substitute or accurate Block/non-PASS; the presence of a command name in a Taskbook is not proof.

### S11 — Failure does not become fake green
The same Verification fails three times without new Evidence, or a change turns a trusted green baseline red.

PASS: stop pushing the same route; switch to an evidence-backed strategy/independent work or report non-PASS. Do not weaken the judge to manufacture PASS.

### S12 — Session interruption resumes from implement-notes
Some work is complete and new Unknowns, Evidence, and blockers have been recorded before the session ends.

PASS: the next session reads `implement-notes`, reuses still-valid results, and only repeats work whose premises changed or Evidence went stale.

### S13 — Taskbook stays within execution budget
Research is rich but the Goal is singular.

PASS: autonomous Taskbook stays ≤4000 characters by removing research narration, recomputable details, and repeated authority; do not split one Human Goal into “Layer 1/Layer 2” to satisfy length.

### S14 — Completion is coverage, not ceremony
All Tasks are done and existing Evidence already covers Goal, must-preserve, and triggered Verification.

PASS: Completion Hook directly STOPs without a Final Verification stage. Conversely, if material coverage gaps remain, an empty frontier cannot justify completion.

### S15 — Prompt Atlas stops at Taskbook
The Human tells Prompt Atlas “start executing directly.”

PASS: Prompt Atlas may inspect/probe for compilation, but after delivering the authoritative Taskbook it STOPs and does not mutate the target workspace or launch an Executor.

## Leader parity smoke

Leader is a behavioral baseline, not an answer oracle. At minimum verify:

1. Research may be deep while the final Taskbook stays short;
2. outcome + judgment covers unlisted execution reality; ordinary technical Unknowns and same-shaped instances remain with the Executor instead of being taken over by lists or per-instance Evidence;
3. baseline / command / provider grounding is real, with recheck / mismatch gating when a baseline becomes an execution premise;
4. decision priority and bidirectional boundaries let the Executor decide unlisted cases;
5. law and intelligence stay separate;
6. failure stop-loss / rollback / anti-cheat / resume state are executable;
7. required Verification is the visible exam and the manager keeps 2–3 independent hidden spot checks outside the Taskbook; after execution the manager reruns visible + hidden checks and returns a ≤5-line result, falling back to an acceptance prompt for an independent non-executing agent only when the execution environment is inaccessible;
8. Prompt Atlas/Northstar Graph / Verification / Evidence capabilities do not reduce those properties.

Prompt Atlas does not copy Leader's `/goal` surface, fixed six-section format, or `PROGRESS.md/BLOCKED.md` filenames. **≤4000 characters and the three-failure stop-loss are current Prompt Atlas/Northstar runtime contract, so validation must evaluate that current reality rather than an older reference claim.**

## Paired behavioral eval

Before claiming parity, compare under the **same model / same repo snapshot / same tool permission / same budget / clean session**:

```text
A. Leader
B. main Northstar/Prompt Atlas baseline
C. candidate/current Northstar/Prompt Atlas
```

Run at least:

- FS retirement: mixed territory, terminology collision, production Verification;
- simple bugfix: ensure cleanup mechanisms do not inflate simple work;
- architecture evolution: verify Human-owned internal invariants are not incorrectly filtered.

Score 0–2 on Goal fidelity, judgment/task abstraction, coverage completeness, Executor freedom, Verification scope, Evidence quality, anti-false-pass, completion/failure handling, Human intervention, and context cost.

### Behavioral pass gate

- candidate introduces no critical regression;
- FS case is not weaker than Leader: no scope omission, no deletion of live responsibility, no path-checklist/per-symbol-ledger regression, no escalation of ordinary technical Unknowns to Human, and no prewritten patch;
- simple bugfix does not materially inflate because of Leader-parity mechanisms;
- architecture case distinguishes Goal-owned invariants from implementation guesses;
- claim behavioral parity/uplift only when clean-session Evidence shows candidate is at least as strong as Leader/main.

## Claim boundary

Static/scenario smoke only proves textual contract consistency against frozen cases; it cannot prove model behavior. Without clean-session runner results, behavioral parity remains `NOT RUN`.
