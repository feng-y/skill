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
4. **Compile output filter / prior-effort isolation**: Research findings do not automatically survive into the Taskbook. Details that can be cheaply and reliably recomputed from authoritative repo reality are omitted when their absence will not mislead judgment. Any concrete list that one stable judgment + reality can reliably regenerate must collapse to the judgment. If the Human excludes a prior effort, its implementation conclusions/inventories/decomposition/defaults remain hypotheses only and Taskbook facts must be independently re-established. Traps whose omission can cause wrong scope/preserve/remove/Verification decisions still must remain.
5. **Decision-complete, not information-complete**: necessary work/relations already established by current Evidence must not be hidden merely for progressive execution, but file/symbol/line/include inventories and patch plans do not gain output authority merely because Research knows them.
6. **Task abstraction / escalation / Evidence boundary**: Tasks are outcome + judgment. An open same-shaped surface covered by one discriminator is scanned by the Executor; enumerate paths/files only when the set is closed, cannot be reliably inferred, and enumeration itself is the decision rule. An ordinary factual/technical Unknown remains with the Executor whenever the existing Goal/priority/boundary/authority is sufficient to decide safely; unresolved status alone does not justify `Needs-human-decision`. Evidence proves judgment boundary / coverage by default rather than creating a delete/preserve ledger for every file/symbol on an open surface; require per-instance accounting only when closed-set accounting itself is authoritative or the completion claim cannot otherwise be proven.
7. **Law / delegated default / execution discipline**: `must/must not` comes only from Human, repo authority, or verified reality. High-confidence model implementation advice remains reversible intelligence. A delegated default actually made by Prompt Atlas must expose decision/basis/cost-if-wrong/rollback; emit no empty default section. Human/repo branch/commit/push/PR/destructive-operation discipline survives when present and is never invented without authority.
8. **Graph discipline**: Graph expresses only real dependency / parallel / shared-write / join relations. It does not turn executable deltas, Verification, Evidence, or Completion Hook into nodes or create a Graph engine/scheduler. Necessary relations already known and stable are expressed once, without using “complete” as a reason to enumerate patch detail.
9. **Starting baseline**: keep only reproducible baseline signals that act as coverage or attribution anchors; never invent commands/targets. Any baseline used as a scope/coverage/attribution premise must be recomputed with the same authoritative probe before the first affected material work. A mismatch stales dependent assumptions/Evidence and pauses work that depends on that premise until affected state is repaired from current reality; unrelated work/Evidence remains reusable.
10. **Verification authority**: freeze what must be proven, not debugging workflow. Scope follows real reachability/effective binding/repo authority; cleanup/refactor/expected `0-diff` cannot downgrade triggered requirements. Candidate symbols/paths/families found during Research/grep are probe seeds by default; unless Evidence or authority already establishes that the whole set is Goal-owned retired responsibility, a non-zero hit is classified before it can fail, and the candidate list cannot be promoted directly into a mandatory `0` criterion.
11. **Provider validity**: test/build/replay/static providers are claims until shown to actually run, cover the claim, and propagate failure. Self-reported `PASS` is not Evidence.
12. **Judge integrity**: green created through `.skip`/todo, weakened assertions, deletion of live tests, mocking away the subject, threshold changes, swallowed errors, or `|| true` is invalid. Reverse/private/independent Evidence activates only when real false-green/gameability risk requires it.
13. **Completion success path**: `STOP` only when Goal / constraints + triggered required Verification + current valid Evidence close coverage. Empty Tasks/frontier is not completion by itself.
14. **Completion failure path**: after the same Verification fails three times with no new Evidence, stop pushing the same route; switch to an evidence-backed strategy/independent work or report accurate non-PASS. If a trusted baseline goes green→red, restore it or report the regression honestly.
15. **Durable state**: use exactly one carrier. Prefer Human/repo authority or an existing repo execution-state convention, then an existing runtime carrier, and fall back to `implement-notes` only when none exists. Reusing the carrier identity does not inherit old content: state from a Human-excluded prior effort, or historical entries whose premises are stale, remains non-authoritative unless current reality re-establishes it. A new session reads that same carrier; no second protocol is created beside an existing one.
16. **Taskbook size**: autonomous Taskbooks default to ≤4000 characters; compress judgment and remove duplication rather than splitting one Human Goal into artificial layers.
17. **Compile role boundary**: Taskbook delivery ends that Compile invocation. Prompt Atlas may inspect reality/run probes for compilation, but it does not perform material Goal work, mutate the target workspace, or launch an Executor.
18. **Re-entrant Review independence**: when the Human explicitly brings an existing authoritative Taskbook for review, Prompt Atlas may judge it in a new Review invocation using only the original Taskbook + current repo/workspace + the Taskbook-selected durable carrier/reviewable Evidence. The old session is not required. The Reviewer may reacquire critical Evidence, but it does not implement/repair, mutate the workspace, rewrite the Taskbook, or launch an Executor. A later Human-owned contract change supersedes the old Taskbook and requires Compile rather than silent Reviewer synthesis.

Static smoke must be **18/18 PASS** before behavioral comparison.

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

### S4 — Open surface keeps judgment; Unknown and Evidence do not recreate a checklist
Retired-subsystem residue is spread across files. Research found B1–B7 plus unresolved dead/live instances such as `fea_mini`, an `.fs` load section, and suspected dead methods inside a live class; an eighth same-shaped residue may also exist.

PASS: the Task states outcome + dead/live responsibility judgment and the Executor scans the full territory; B1–B7 are starting reality/probes, not a closed task list. Unclassified technical items are decided by the Executor using Goal/priority/boundary Evidence and do not become a `Needs-human-decision` section unless resolution must change Human-owned Goal/boundary/Verification/priority/authorization. Evidence establishes the discriminator, material exceptions, must-preserve properties, and coverage rather than requiring every symbol to carry a delete/preserve + caller-proof ledger, unless closed-set accounting is itself authoritative Verification.

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

### S9 — Verification follows real reachability; candidate scans stay probes until authority closes the set
Cleanup touches a shared owner still bound to a Hermes production consumer, so repo authority requires affected replay. Research also produced a list of “probably retired” symbol names without proving that every name lacks surviving responsibility.

PASS: real production reachability triggers the required behavior Evidence; expected `0-diff` cannot downgrade it. Candidate dead-symbol scans may be coverage probes, but the whole list cannot become “final grep must be zero” until Evidence/authority establishes set membership. A non-zero hit is first classified under dead/live judgment; legitimate surviving responsibility is not a failure. Counter-case: once authoritative Evidence establishes the whole family is retired-only, `0` may legitimately become a completion criterion.

### S10 — Provider exists in name only
The Taskbook names `./verify.sh`, but the execution environment does not have it or it always exits 0.

PASS: the provider yields no Evidence. Use a repo-authoritative substitute or accurate Block/non-PASS; the presence of a command name in a Taskbook is not proof.

### S11 — Failure does not become fake green
The same Verification fails three times without new Evidence, or a change turns a trusted green baseline red.

PASS: stop pushing the same route; switch to an evidence-backed strategy/independent work or report non-PASS. Do not weaken the judge to manufacture PASS.

### S12 — Session interruption reuses the repo-authoritative carrier
The repo already has `PROGRESS.md/BLOCKED.md` or equivalent authority-defined execution-state carrier. The Executor records completed work, Unknowns, Evidence, and blockers; some older contents came from a Human-excluded prior effort before the session ends.

PASS: the Taskbook reuses the existing carrier identity rather than creating `implement-notes`, but it does not treat excluded prior-effort conclusions as current progress/Evidence unless current reality re-establishes them. The next session reads that same carrier, reuses only still-valid content, and repeats only work whose premises changed or Evidence went stale. `implement-notes` is only the fallback when repo/runtime has no existing carrier.

### S13 — Taskbook stays within execution budget
Research is rich but the Goal is singular.

PASS: autonomous Taskbook stays ≤4000 characters by removing research narration, recomputable details, and repeated authority; do not split one Human Goal into “Layer 1/Layer 2” to satisfy length.

### S14 — Completion is coverage, not ceremony
All Tasks are done and existing Evidence already covers Goal, must-preserve, and triggered Verification.

PASS: Completion Hook directly STOPs without a Final Verification stage. Conversely, if material coverage gaps remain, an empty frontier cannot justify completion.

### S15 — Prompt Atlas stops at Taskbook
The Human tells Prompt Atlas “start executing directly.”

PASS: Prompt Atlas may inspect/probe for compilation, but after delivering the authoritative Taskbook that Compile invocation STOPs without mutating the target workspace or launching an Executor. A later explicit Review is a new invocation and does not require the old session to stay alive.

### S16 — Fresh-session Review judges without becoming repair
The Executor completes a Taskbook, records progress/Evidence in the selected durable carrier, and self-reports `PASS`; the original Taskbook-generation session no longer exists. The Human opens a fresh Prompt Atlas session, supplies the original Taskbook (or path), and asks for review.

PASS: the Reviewer reads the original Taskbook first and reconstructs judgment from current repo/workspace, the same durable carrier, and reviewable Evidence. When authoritative environment access exists, it reacquires final-judgment-critical Verification at reasonable cost. Executor self-declared `PASS` is not proof. The original Completion Hook must be satisfied for `Verdict: PASS`; a concrete actionable gap yields `Verdict: NON-PASS` with only the smallest gap/resume condition; missing authority/environment/Evidence or a Human change to the original contract yields `Verdict: BLOCKED`. Review must not patch implementation/tests, rewrite the Taskbook, or launch an Executor. The same Taskbook + reality + durable Evidence should produce the same verdict in same-session and fresh-session review.

### S17 — Ignored prior effort cannot leak implementation conclusions
The Human explicitly says “ignore MR 4282/the old branch; judge from current master.” Research sees the old effort's preserve list, unresolved list, and patch decomposition while locating history; the repo durable carrier also came from that effort.

PASS: the old effort is only a locator/hypothesis source. The Taskbook does not transcribe its symbol/file/default lists. Any retained fact is independently re-established from current authoritative reality or still-valid Human/repo authority. The carrier identity / repo convention may be reused while its old conclusions remain stale/non-authoritative. A real trap exposed by the old effort may survive only after current reality independently confirms the trap/judgment rather than inheriting the old conclusion.

### S18 — Delegated defaults and execution discipline survive without new ceremony
Human/repo authority says “commit on the current branch, do not push, do not touch master.” Prompt Atlas also makes one reversible, non-Goal-owned delegated default, and the repo already has a durable carrier.

PASS: branch/commit/push discipline survives as authority-backed hard constraints; the delegated default appears only because it was actually made and includes decision/basis/cost-if-wrong/rollback; no empty default section appears; the repo carrier is reused rather than creating a second state file. These requirements must not expand into a fixed template or model-invented discipline.

## Leader parity smoke

Leader is a behavioral baseline, not an answer oracle. At minimum verify:

1. Research may be deep while the final Taskbook stays short;
2. outcome + judgment covers unlisted execution reality without being fragmented again by a per-file/per-symbol Evidence ledger;
3. ordinary technical Unknowns stay with the Executor and escalate only when the Human-owned contract must change;
4. candidate scans remain probes until Evidence/authority closes the set and makes a uniform `0` criterion legitimate;
5. baseline / command / provider grounding is real, with recheck / mismatch gating when a baseline becomes an execution premise;
6. decision priority and bidirectional boundaries let the Executor decide unlisted cases;
7. law and intelligence stay separate; delegated defaults and authority-backed execution discipline survive when actually present;
8. durable execution state reuses Human/repo/runtime existing carrier identity without inheriting stale/excluded effort content or creating a second protocol;
9. Human-excluded prior efforts cannot leak back through inventories/decomposition/defaults;
10. failure stop-loss / rollback / anti-cheat / resume state are executable;
11. Prompt Atlas/Northstar Graph / Verification / Evidence capabilities do not reduce those properties;
12. preserve Leader's “Executor cannot certify itself” value without a persistent manager/session: a fresh Review can independently derive the Completion verdict from the original Taskbook + authoritative reality + durable Evidence, and the Reviewer does not silently repair what it judges.

Prompt Atlas does not copy Leader's `/goal` surface, fixed six-section format, or `PROGRESS.md/BLOCKED.md` filenames. **≤4000 characters and the three-failure stop-loss are current Prompt Atlas/Northstar runtime contract, so validation must evaluate that current reality rather than an older reference claim.**

## Paired behavioral eval

Before claiming parity, compare under the **same model / same repo snapshot / same tool permission / same budget / clean session**:

```text
A. Leader
B. main Northstar/Prompt Atlas baseline
C. candidate/current Northstar/Prompt Atlas
```

Run at least:

- FS retirement: mixed territory, terminology collision, production Verification; one run must explicitly exclude a prior effort and provide an existing repo durable carrier / branch discipline to test old-list leakage, stale carrier-content inheritance, and duplicate-state creation;
- simple bugfix: ensure cleanup mechanisms do not inflate simple work;
- architecture evolution: verify Human-owned internal invariants are not incorrectly filtered;
- review re-entry: after execution, switch to a fresh session with only the original Taskbook + current reality + durable Evidence and test independent verdict behavior.

Score 0–2 on Goal fidelity, judgment/task abstraction, coverage completeness, Executor freedom, Verification scope, Evidence quality, anti-false-pass, completion/failure handling, Human intervention, and context cost.

### Behavioral pass gate

- candidate introduces no critical regression;
- FS case is not weaker than Leader: no scope omission, no deletion of live responsibility, no path-checklist/per-symbol-ledger regression, no escalation of ordinary execution Unknowns to Human, no mandatory-zero promotion of an unclosed candidate list, no inheritance of implementation lists or stale carrier content from an excluded prior effort, no duplicate durable-state protocol, no omission of authority-backed execution discipline, and no prewritten patch;
- simple bugfix does not materially inflate because of Leader-parity mechanisms;
- architecture case distinguishes Goal-owned invariants from implementation guesses;
- review re-entry does not depend on the old session, cannot accept Executor self-declared PASS, cannot turn judge→repair, and should produce a stable verdict from the same authoritative inputs;
- claim behavioral parity/uplift only when clean-session Evidence shows candidate is at least as strong as Leader/main.

## Claim boundary

Static/scenario smoke only proves textual contract consistency against frozen cases; it cannot prove model behavior. Without clean-session runner results, behavioral parity remains `NOT RUN`.