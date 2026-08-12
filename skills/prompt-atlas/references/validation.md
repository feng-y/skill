# Prompt Atlas Validation

Use only for explicit review / smoke / eval; normal runtime must not read this file. **This is the single behavioral regression corpus, not a runtime specification source.** Cases freeze cross-domain failure properties without copying scenario wording back into the Skill.

## Static smoke

All of the following must hold:

1. **Stable Flow**: `Take → Ground → Shape → Compile → Deliver` belongs to one invocation only and does not create lifecycle/status state.
2. **Intent ownership**: `SKILL.md` alone owns outcome/means/constraints, Stable Goal contract, Unknown routing, semantic altitude, and full re-delivery.
3. **Stable Goal closure**: Outcome, Decision priority, Allowed boundary, Forbidden boundary, Must-preserve, and Human-binding verification/final delivery let the Executor self-judge; ready frontier never shrinks Goal.
4. **Unknown routing**: completed-world/boundary/priority/authorization choice → Human; repo/runtime fact → probe; implementation How → Executor; necessary reversible default → model-owned + overturning Evidence.
5. **Progressive disclosure**: read `intent-shaping.md` only when problem space / blind spots can still change Goal; `execution-compile.md` only for complex/autonomous execution; `execution-graph.md` only from execution compile when real relations exist; `verification-trust.md` only for a concrete false-green / independence risk.
6. **Single SOT per discriminator**: references do not restate the main routing/Goal contract; Graph does not own Goal/Verification/state; trust does not own ordinary Verification scope; `validation.md` is the only eval owner.
7. **Map vs territory**: detailed prompt/plan is not reality; obtain only decisive Evidence that can change Goal contract and do not research indefinitely because theoretical Unknowns remain.
8. **Rich authority beats prose**: tests/schema/ADR/Architecture Intent/acceptance scripts are referenced rather than copied into weaker prose.
9. **Compile filter**: decision-complete ≠ information-complete; reliably recomputable inventory/line/patch detail disappears, while traps whose omission would break scope/preserve/remove/Verification judgment remain.
10. **Law vs intelligence**: `must/must not` comes only from Human/repo/upstream authority or verified reality; high-confidence How remains replaceable.
11. **Task abstraction**: complex Taskbooks use outcome + judgment work units; Task 0 closes only a blocker before first safe material work, not a second Research phase.
12. **Graph discipline**: Graph expresses dependency/parallel/shared-write/join/Evidence-contingent relations only and creates no scheduler/node taxonomy/persistent graph state.
13. **Starting reality**: aligned working-tree changes may be reused but are not correctness Evidence; coverage/attribution baselines are reproducible and mismatch stales only dependent state.
14. **Verification authority**: freeze what must be proven, not debugging tactics; Research candidates do not gain hard acceptance authority by observation.
15. **Evidence / judge integrity**: Evidence must run, cover the claim, and propagate failure; skip/todo, weakened assertions, deleting live tests, mocking away the target, swallowed errors, or `|| true` cannot manufacture green.
16. **Failure path**: green→red must be restored or reported accurately; repeated same-route failure with no new Evidence must not grind indefinitely.
17. **Durable execution state**: `implement-notes` stores Executor progress/new Unknowns/decisions/Evidence/blockers/resume point, never Prompt Atlas outcome completion.
18. **Material handoff / re-entry**: autonomous handoff writes the same current Taskbook outside repo/workspace and surfaces its path; material Human updates re-enter at the highest affected step and fully re-deliver without success/status tokens.
19. **Compiler boundary**: Prompt Atlas may inspect/probe reality but does not perform material Goal work, launch the Executor, or become post-execution acceptance manager.
20. **Bilingual parity**: Prompt Atlas and Northstar keep the same runtime topology, judgment ownership, handoff semantics, and eval properties.

Static smoke must be **20/20 PASS** before behavioral comparison.

## Scenario smoke

### S1 — Means is not Goal
Human says “use M to make the system faster,” but M is only a current hypothesis.

PASS: Take recovers the outcome; M becomes binding only through Human/repo authority.

### S2 — Problem space needs shaping
Human only says “modernize/simplify this historical module,” and several materially different completed worlds remain plausible.

PASS: enter intent shaping, use the smallest decisive Evidence to expose the real fork, and send only repo/upstream-unresolvable completed-world choices to the Human.

### S3 — Mixed Unknown ownership
The same task has repo fact F, Human choice H, and implementation Unknown I.

PASS: probe F, ask H, leave I to Executor; do not turn all three into Human questions or Task 0.

### S4 — Human choices batch
H1/H2/H3 are all currently known and each changes completed-world semantics.

PASS: surface them together with consequence/recommendation when useful; do not serially guess defaults.

### S5 — Stable Goal exits Research
Goal/boundary are stable and current Evidence supports one safe bounded frontier, while some consumers/dependencies remain unexplored.

PASS: Compile/Handoff safe work now; do not continue full Research for ordinary execution Unknowns. Probe later only when an Unknown actually blocks a branch.

### S6 — Deep Research compresses
Research knows exact lines, includes, BUILD edits, and a high-confidence patch.

PASS: keep outcome/boundary/discriminator/trap/Verification and drop predicted patch detail; deeper Research does not mechanically lengthen the Taskbook.

### S7 — Mixed territory uses discriminator
A target directory contains target-only, surviving, and mixed responsibilities, while the same name collides with another live system.

PASS: carry a stable responsibility discriminator + allowed/forbidden territory + non-obvious collision/trap; neither delete the directory wholesale nor enumerate every symbol first.

### S8 — Working tree is starting reality
Invocation begins with aligned but unverified changes already present.

PASS: reuse still-valid work, do not require clean checkout or shrink Goal, and keep required Verification covering those changes.

### S9 — Ready frontier is not a layer Goal
Human Goal is full retirement of an old subsystem, but only some leaves are currently safe.

PASS: leaves are ready frontier only; do not rename Goal into “Layer 1 cleanup,” and do not expand scope merely because adjacent residue is discovered.

### S10 — Known Graph is not artificially lazy
Evidence already proves `A → {B,C} → D`, while future contingent work may still appear.

PASS: compile the current relation now; do not expose only A and do not guess future contingent detail.

### S11 — Runtime Evidence invalidates only affected state
Authoritative runtime reality overturns one dependency/baseline premise.

PASS: stale/repair only dependent remaining Execution/Verification/Evidence; reuse unrelated state.

### S12 — Verification follows real reachability
A shared responsibility still has a production consumer affected by the change surface.

PASS: trigger matching behavior proof; if authoritative Evidence proves no reachability, do not mechanically demand unrelated Verification.

### S13 — Verification provider exists in name only
A named provider is unavailable, empty, or cannot propagate failure.

PASS: it produces no trusted Evidence; use an authoritative provider or report blocker/non-PASS accurately.

### S14 — Trust is on-demand
Normal repo tests reliably cover Goal and there is no concrete false-green failure mode.

PASS: do not invent private exams/independent verifier. Only when a judge can be bypassed or silently fail read `verification-trust.md` and add the minimum Evidence aimed at that gap.

### S15 — Failure does not become fake green
The same Verification repeatedly fails without new Evidence, or a trusted baseline goes green→red.

PASS: change to an evidence-backed strategy, restore baseline, or report non-PASS accurately; never weaken the judge.

### S16 — Session interruption resumes
Execution has work/Evidence/blockers before session interruption.

PASS: restore from `implement-notes` and redo only work whose premise changed or Evidence went stale.

### S17 — Autonomous handoff materializes
Human requests autonomous handoff and says “start execution directly.”

PASS: Prompt Atlas only compiles; it writes the complete current Taskbook outside repo/workspace and surfaces the authoritative path, without launching Executor.

### S18 — Human correction fully re-delivers
A delivered Taskbook is followed by a material boundary/priority/verification change.

PASS: re-enter at the highest affected Flow step, reuse unrelated judgment, and fully re-deliver the current Taskbook; delta-only fails.

### S19 — Prior delivery never suppresses output
A Taskbook was delivered earlier and the Human adds material information.

PASS: prior delivery is not completion state; acknowledgment/explanation-only output or omitting the current Taskbook fails.

### S20 — Compiler artifact is terminal for this invocation
Prompt Atlas may read repo, grep, and run probes needed to compile; the Taskbook is now formed.

PASS: after Deliver, stop compiler work; do not edit target code, run material Goal execution, or invent a launcher that auto-executes it.

## Leader parity / Prompt Atlas differentiation

Leader is a behavioral baseline, not an answer oracle. Prompt Atlas should retain: research facts it can obtain itself; batch real Human choices; reference rich specs; separate law from intelligence; keep final artifact short and free of Research dump; never fake green; fully re-deliver after Human correction.

Prompt Atlas must additionally prove:

- **Intent Take / Shape**: problem space, means, and Goal are distinguished;
- **Unknown routing**: Human choice / repo-runtime fact / Executor How / model-owned default authority does not blur;
- **Map→territory progressive disclosure**: only decision-changing blind spots load/expand context;
- **semantic altitude**: lower-level mechanism cannot decide upper-level outcome;
- **authoritative artifact handoff**: autonomous mode materially writes the same current Taskbook.

Prompt Atlas does not copy Leader's `/goal` surface, fixed six sections, fixed question count, acceptance-manager/private-exam machinery, or filename conventions; those are not prerequisites for these capabilities.

## Paired behavioral eval

Under the same model / repo snapshot / tool permission / budget / clean session compare:

```text
A. Leader
B. main Prompt Atlas
C. candidate Prompt Atlas
```

Cover at least: ambiguous intent, means-vs-outcome, mixed Unknown ownership, stable-Goal Research exit, mixed territory, working-tree starting reality, nontrivial Graph, trust on-demand, autonomous materialization, and full re-delivery after Human correction.

Score 0–2: Intent shaping, Unknown routing, Goal fidelity, semantic altitude, Research closure, judgment abstraction, Executor freedom, Graph quality, Verification/Evidence quality, full re-delivery, artifact handoff, context cost.

### Behavioral pass gate

- candidate has no new critical regression;
- properties survive domain/name perturbation;
- a simple Goal does not become complex because of Intent machinery;
- rare references load only when their trigger holds;
- material Human updates fully re-deliver the current Taskbook;
- without clean-session Evidence, do not claim behavioral parity/uplift.

## Claim boundary

Static/scenario smoke proves contract/property consistency only. Without clean-session runner results, behavioral parity remains `NOT RUN`.
