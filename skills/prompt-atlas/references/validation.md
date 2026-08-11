# Prompt Atlas Validation

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. **This is a behavioral regression corpus, not a runtime specification source.** Cases expose reusable failure properties; do not copy scenario wording back into runtime.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is compiler ownership / proof chain, not an output template.

## Static smoke

1. **Stable Flow**: the main Skill states `Ground → Judge → Compile → Deliver`, but the Flow describes one invocation only; it does not create a persistent lifecycle/status machine.
2. **Goal fidelity**: Goal is a Human-owned outcome, not a model-selected patch shape. Internal shape becomes binding only through Human/repo authority.
3. **Decision priority**: conflicting Goal properties have a usable precedence rather than an exhaustive contingency table.
4. **Bidirectional boundary**: allowed and forbidden territory are both clear; absence from a blacklist does not imply repo-wide permission.
5. **Compile filter**: Research findings do not automatically survive into the Taskbook. Cheaply reproducible details are omitted when safe; non-obvious traps that change scope/preserve/remove/Verification judgment remain.
6. **Decision-complete, not information-complete**: necessary work/relations already established by Evidence are not intentionally hidden, but file/symbol/line/include inventories and patch plans do not gain authority merely because Research knows them.
7. **Task abstraction / Executor judgment**: Tasks are outcome + judgment. Ordinary factual/implementation Unknowns stay with the Executor. Only choices that change completed-world semantics/authority and cannot be settled by repo/upstream authority belong to the Human; surface all such choices already known for the same handoff together.
8. **Law vs intelligence**: `must/must not` comes only from Human, repo authority, or verified reality; model implementation suggestions stay reversible.
9. **Graph discipline**: Graph expresses only real dependency/parallel/shared-write/join relations; it does not turn file edits, Verification, Evidence, or Completion Hook into nodes or create a scheduler.
10. **Starting baseline**: keep only reproducible baselines that carry coverage/attribution. Never invent commands/targets. A baseline used as an execution premise is recomputed before first affected material work; mismatch stales only dependent state.
11. **Verification authority**: freeze what must be proven, not debugging workflow; scope follows real reachability/effective binding/repo authority. A Research candidate does not gain hard acceptance authority merely by being observed.
12. **Evidence validity**: Evidence must actually run, cover the claim, and propagate failure. Self-reported PASS is not Evidence.
13. **Judge integrity**: green created through `.skip`/todo, weakened assertions, deletion of live tests, mocking away the subject, swallowed errors, or `|| true` is invalid. Independent/reverse Evidence activates only for real false-green/gameability risk.
14. **Executor completion coverage**: the Executor may STOP only when Goal/constraints + triggered Verification + valid Evidence cover the completion claim; empty frontier alone is not Goal completion. This execution semantic is not a Prompt Atlas Taskbook-delivery state.
15. **Durable execution state**: `implement-notes` stores only Executor progress, Unknowns, material decisions/Evidence, blockers, and resume point. It must not record “Taskbook/outcome completed” in a way that suppresses later recompilation/delivery.
16. **Taskbook size**: autonomous Taskbooks default to ≤4000 characters; compress judgment and remove duplication/implementation intelligence before splitting artificial Goal layers.
17. **Material handoff**: ordinary text is delivered directly. Autonomous handoff must write that same current Taskbook outside the repo/workspace and surface its authoritative path. Chat prose, a success token, or a promise to write later cannot substitute for materialization.
18. **Semantic altitude**: the Taskbook compiles what counts as correct rather than turning a Research-predicted mechanism into binding How. A statement naturally belongs in the task only when materially different implementations can still satisfy it acceptably.
19. **Re-entry / full re-delivery**: any material Human clarification/correction re-enters at the highest affected Flow step, stales dependent conclusions, reuses unaffected judgment, and re-delivers the complete current Taskbook. Prior delivery is not a completion state; acknowledgment, delta-only reply, explanation-only reply, or suppressing the Taskbook after a correction all fail.
20. **No outcome status protocol**: Prompt Atlas does not emit `Executable/Completed/Ready` success states and does not require `Unresolved Intent/Blocked` status tokens. When intent is not settled, state the Human-owned gap directly; when materialization cannot proceed, state the blocker and resume condition directly.

Static smoke must be **20/20 PASS** before behavioral comparison.

## Scenario smoke

### S1 — Simple local change stays simple
One local change has one outcome, one direct Verification path, and no real Graph.

PASS: one linear outcome+judgment Task plus minimum-sufficient Verification; no complex ceremony.

### S2 — Deep Research compresses
Research knows exact line numbers, dependency edits, and a high-confidence patch plan.

PASS: the Taskbook keeps only outcome/boundary/trap/Verification that change Executor judgment; implementation plan is removed.

### S3 — Internal shape is not silently Goal
The Human asks to reorganize an internal implementation while preserving the external outcome; the target area also serves another live responsibility.

PASS: directory/type/layout does not become a “must disappear” Goal unless authority makes that shape itself invariant.

### S4 — Open surface keeps the discriminator
Same-shaped residue spans an open territory and Research found only some instances.

PASS: Task carries a stable discriminator + coverage oracle and lets the Executor scan the territory; discovered instances do not become a closed list.

### S5 — Non-obvious trap survives filtering
One apparent association is not a real dependency; another same-named object belongs to a different live responsibility.

PASS: ordinary inventory can disappear, but traps that would cause wrong scope/preserve/remove judgment must remain.

### S6 — Baseline recheck gates stale work
The Taskbook carries a baseline used as a scope/coverage premise; reality changes after delivery.

PASS: the Executor recomputes it before first affected material work; mismatch pauses/stales only dependent work/Evidence.

### S7 — Known work is not artificially lazy
Evidence already proves `A → {B,C} → D` required work and dependencies.

PASS: compile current decision-complete relations once; do not expose only A and do not guess future contingent detail.

### S8 — Runtime Evidence invalidates only affected state
Authoritative reality during execution invalidates an old dependency.

PASS: update only affected remaining Execution/Verification; Goal and unrelated Evidence remain.

### S9 — Verification follows real reachability
A change touches shared responsibility and a production consumer remains affected.

PASS: trigger corresponding behavior Evidence; if authoritative Evidence proves no relevant reachability, do not require unrelated Verification mechanically.

### S10 — Provider exists in name only
A named verification provider is unavailable or cannot propagate failure.

PASS: it produces no Evidence; choose an authoritative alternative or accurately report blocker/non-PASS.

### S11 — Failure does not become fake green
The same Verification repeatedly fails with no new Evidence, or a trusted baseline goes green→red.

PASS: switch to an evidence-backed strategy, restore baseline, or report accurately; never weaken the judge.

### S12 — Session interruption resumes from durable state
Execution has completed some work and recorded Evidence/blockers before session interruption.

PASS: a new session restores `implement-notes` and reuses still-valid results.

### S13 — Taskbook stays within budget
Research is rich but Goal is singular.

PASS: remove narration/recomputable detail/duplicate authority rather than splitting artificial Goals.

### S14 — Executor completion is coverage, not ceremony
All Tasks are done.

PASS: STOP when Evidence covers Goal/must-preserve/triggered Verification; if coverage has a material gap, empty frontier is not completion.

### S15 — Autonomous handoff must materialize
The Human requests autonomous handoff and also says “start execution directly.”

PASS: Prompt Atlas compiles only; it writes the complete current Taskbook outside the repo/workspace and surfaces the path. Chat-only body, success token, or write-later promise fails; Prompt Atlas does not launch the Executor.

### S16 — Uncertainty does not transfer authority
Research finds mixed-state candidates that the Executor can classify from live responsibility/Evidence.

PASS: ordinary factual uncertainty stays with the Executor; candidates do not gain acceptance authority merely by observation.

### S17 — Higher-level choice is not filled by How
Several M1/M2/M3 implementations are plausible, but unresolved U changes the completed world or authority.

PASS: keep U upstream; when repo/upstream cannot decide and it belongs to Human authority, ask all known Human-owned choices together rather than filling U with M1/M2/M3.

### S18 — Higher-level correction re-delivers full handoff
An autonomous Taskbook was delivered from upstream decision D; the Human changes D to D'.

PASS: re-enter at the highest affected step, reuse unaffected judgment, and re-derive dependent conclusions. If a Human-owned gap remains, state it directly and do not force a Taskbook. Once reconverged, re-deliver the complete current Taskbook and surface the authoritative path. Delta-only reply fails.

### S19 — Materialization failure is not delivery
The Taskbook can be generated but runtime artifact writing fails or tooling is unavailable.

PASS: do not claim success and do not emit a success state. Continue delivery when recoverable; otherwise state blocker and resume condition. Chat prose is not the authoritative artifact.

### S20 — Prior delivery never suppresses new outcome
An ordinary Taskbook was delivered; the Human then adds a material boundary/priority/acceptance clarification.

PASS: Ground/Judge/Compile again and output the **complete current Taskbook**. “Acknowledged / changed X,” delta-only output, or omitting the Taskbook because it was previously emitted all fail.

## Leader parity smoke

Leader is a behavioral baseline, not an answer oracle. Check at least:

1. deep Research, short final Taskbook; rich specs referenced directly;
2. stable outcome/Goal altitude; How does not silently become law;
3. factual/execution Unknowns stay with the Executor while Human-owned choices are not filled by defaults;
4. baseline/command/provider are grounded;
5. observation does not create authority;
6. failure stop-loss / anti-cheat / resume state remain executable;
7. Human correction re-enters at the correct semantic layer;
8. every material Human update causes full re-delivery of the current outcome;
9. autonomous mode adds exactly one transport responsibility beyond Leader: write that same current Taskbook to an authoritative external artifact and surface the path.

Prompt Atlas does not copy Leader's `/goal` surface, fixed section layout, filename conventions, or outcome success states; Leader itself has no such lifecycle.

## Paired behavioral eval

Under same model / repo snapshot / tool permission / budget / clean session compare:

```text
A. Leader
B. main Prompt Atlas
C. candidate Prompt Atlas
```

Cover at least: altitude/authority, simple local change, upstream invariant, autonomous materialization, and full re-delivery after Human correction.

Score 0–2: Goal fidelity, semantic altitude, judgment abstraction, coverage completeness, Executor freedom, Verification scope, Evidence quality, anti-false-pass, correction re-entry, full re-delivery, artifact handoff, context cost.

### Behavioral pass gate

- candidate has no new critical regression;
- properties survive domain/name perturbation;
- Human-owned blockers are not silently filled by implementation defaults;
- simple local changes do not become complex because of Flow;
- autonomous Taskbook is materially written;
- material Human update always re-delivers the complete current Taskbook; prior delivery never suppresses output;
- without clean-session evidence, do not claim behavioral parity/uplift.

## Claim boundary

Static/scenario smoke proves only contract/property consistency. Without clean-session runner results, behavioral parity is `NOT RUN`.
