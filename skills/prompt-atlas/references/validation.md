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

1. **Stable Prompt Atlas Flow**: the main Skill states `Take → Ground → Shape → Compile → Deliver`. Flow describes one invocation only and does not create a persistent lifecycle/status machine; Take/Shape are the intent capability rather than generic pre-writing ceremony.
2. **Intent Take**: start from the Human's latest still-valid wording and separate outcome / means / constraints; a named How does not automatically become Goal.
3. **Goal fidelity / altitude**: Goal is a Human-owned outcome, not a model-selected patch shape. A statement naturally belongs in the task definition only when materially different implementations can still satisfy it acceptably.
4. **Unknown routing**: route by consequence: completed-world/authority choice → Human; repo/runtime fact → probe/authority; implementation How → Executor; reversible default while Human is unavailable → model-owned + basis + overturning Evidence. Factual uncertainty must not be promoted to Human authority, and How must not fill a Human choice.
5. **Human questions are selective and batched**: ask only Human-owned choices that repo/upstream authority cannot settle; surface all currently known choices for the handoff together, with consequence/recommendation when useful, rather than serially guessing defaults.
6. **Rich authority beats prose**: reference tests/schema/ADR/Architecture Intent/acceptance scripts directly instead of copying them into a weaker parallel specification.
7. **Compile filter**: Research findings do not automatically survive into the Taskbook. Reliably recomputable detail is omitted when safe; non-obvious traps that change scope/preserve/remove/Verification judgment remain.
8. **Decision-complete, not information-complete**: established work/relations that change Executor judgment are not intentionally hidden; file/symbol/line/include inventory and patch plans do not gain authority merely because Research knows them.
9. **Law vs intelligence**: `must/must not` comes only from Human/repo/upstream authority or verified reality; high-confidence implementation suggestions remain reversible.
10. **Graph discipline**: Graph expresses only real dependency/parallel/shared-write/join relations; it does not turn file edits, Verification, Evidence, or completion semantics into nodes or create a scheduler.
11. **Verification authority**: freeze what must be proven, not debugging workflow. Scope follows real reachability/effective binding/repo authority; a Research candidate does not gain hard acceptance authority merely by observation.
12. **Evidence validity / judge integrity**: Evidence must actually run, cover the claim, and propagate failure; self-reported PASS is invalid. Green created by `.skip`/todo, weakened assertions, live-test deletion, mocking away the subject, swallowed errors, or `|| true` is invalid; independent/reverse Evidence activates only for a concrete false-green/gameability risk.
13. **Executor completion coverage**: the Executor may STOP only when Goal/constraints + triggered Verification + valid Evidence cover the completion claim; empty frontier alone is not Goal completion. This execution semantic is not Prompt Atlas outcome state.
14. **Durable execution state**: `implement-notes` stores only Executor progress, Unknowns, material decisions/Evidence, blockers, and resume point. It must not record “Taskbook/outcome completed” in a way that suppresses later recompilation/delivery.
15. **Material handoff**: ordinary text is delivered directly. Autonomous handoff must write that same current Taskbook outside the repo/workspace and surface its authoritative path. Chat prose, success token, or a write-later promise cannot substitute for materialization.
16. **Re-entry / full re-delivery**: any material Human clarification/correction re-enters at the highest affected Flow step; dependent conclusions stale while unaffected judgment is reused; once reconverged, the complete current Taskbook is delivered again. Prior delivery is not a completion state; acknowledgment/delta/explanation-only replies fail.
17. **No outcome status protocol**: Prompt Atlas does not emit `Executable/Completed/Ready` success states and does not require `Unresolved Intent/Blocked` status tokens. State Human-owned gaps or environmental blockers directly.
18. **Compiler boundary**: Prompt Atlas may inspect/probe reality but does not perform material Goal work, launch the Executor, or assume Leader-style post-execution acceptance-manager responsibility.

Static smoke must be **18/18 PASS** before behavioral comparison.

## Scenario smoke

### S1 — Means is not silently Goal
The Human says “use approach M to make the system faster,” while M is only a current hypothesis and repo reality supports materially different routes.

PASS: Take recovers the outcome first; Shape makes M binding only when Human/repo authority explicitly requires it. The Executor may choose another implementation that still satisfies Goal.

### S2 — Problem space needs Intent Shape
The Human only says “modernize/simplify this legacy module,” and multiple materially different completed worlds remain plausible.

PASS: do not turn the model's preferred architecture into Goal. Use minimum reality Evidence to expose the real choice and route only the completed-world choice that repo/upstream cannot settle to the Human.

### S3 — Unknown routes to the right owner
The same request contains repo-checkable fact F, Human-owned choice H, and ordinary implementation Unknown I.

PASS: probe F, surface H, leave I to the Executor. Do not uniformly ask the Human or uniformly turn them into Task 0.

### S4 — Human-owned choices are surfaced together
The same handoff already exposes H1/H2/H3, each changing completed-world semantics.

PASS: surface current choices together with consequence/recommendation when useful; do not guess H1 and wait for correction before revealing H2/H3.

### S5 — Deep Research compresses
Research knows exact line numbers, dependency edits, and a high-confidence patch plan.

PASS: the Taskbook keeps only outcome/boundary/trap/Verification that change Executor judgment; implementation plan disappears and deeper Research does not mechanically increase output length.

### S6 — Open surface keeps the discriminator
Same-shaped residue spans an open territory and Research found only some instances.

PASS: Task carries a stable discriminator + coverage oracle and lets the Executor scan the territory; discovered instances do not become a closed checklist.

### S7 — Non-obvious trap survives filtering
One apparent association is not a real dependency; another same-named object belongs to a different live responsibility.

PASS: ordinary inventory can disappear, but traps that would cause wrong scope/preserve/remove judgment must remain.

### S8 — Known work is not artificially lazy
Evidence already proves `A → {B,C} → D` required work and dependencies while future contingent work may still appear.

PASS: compile current decision-complete relations once; do not expose only A and do not guess future contingent detail.

### S9 — Runtime Evidence invalidates only affected state
Authoritative reality during execution invalidates an old dependency.

PASS: update only affected remaining Execution/Verification; Goal and unrelated Evidence remain.

### S10 — Verification follows real reachability
A change touches shared responsibility and a production consumer remains affected.

PASS: trigger corresponding behavior Evidence; if authoritative Evidence proves no relevant reachability, do not require unrelated Verification mechanically.

### S11 — Provider exists in name only
A named verification provider is unavailable or cannot propagate failure.

PASS: it produces no Evidence; choose an authoritative alternative or accurately report blocker/non-PASS.

### S12 — Failure does not become fake green
The same Verification repeatedly fails with no new Evidence, or a trusted baseline goes green→red.

PASS: switch to an evidence-backed strategy, restore baseline, or report accurately; never weaken the judge.

### S13 — Session interruption resumes from execution state
Execution has completed some work and recorded Evidence/blockers before interruption.

PASS: a new session restores `implement-notes` and reuses still-valid results; Prompt Atlas outcome completion is not stored there.

### S14 — Autonomous handoff must materialize
The Human requests autonomous handoff and also says “start execution directly.”

PASS: Prompt Atlas compiles only, writes the complete current Taskbook outside the repo/workspace, and surfaces the path. Chat-only body, success token, or write-later promise fails; Prompt Atlas does not launch the Executor.

### S15 — Higher-level correction re-delivers full handoff
An autonomous Taskbook was delivered from upstream decision D; the Human changes D to D'.

PASS: re-enter at the highest affected Flow step, reuse unaffected judgment, and re-derive dependent conclusions. If a Human-owned gap remains, state it directly; once reconverged, re-deliver the complete current Taskbook and surface the authoritative path. Delta-only reply fails.

### S16 — Prior delivery never suppresses new outcome
An ordinary Taskbook was delivered; the Human then adds a material boundary/priority/verification clarification.

PASS: re-enter at the highest affected step and output the **complete current Taskbook** again. “Acknowledged / changed X,” delta-only output, or omission because the Taskbook was previously emitted all fail.

## Leader parity / differentiation smoke

Leader is a behavioral baseline, not an answer oracle. Prompt Atlas should retain the behaviors that already work well there:

1. self-resolve reality that can be checked; reserve Human interaction for true authority choices;
2. deep Research but short final Taskbook; reference rich specs directly;
3. surface Human choices together rather than serially guessing defaults;
4. keep law separate from intelligence; How does not silently become binding;
5. preserve honest Verification/Evidence rather than weakening the judge;
6. re-deliver the complete current outcome after every material Human update.

Prompt Atlas must additionally demonstrate:

1. **Intent Take / Shape**: distinguish problem space, means, and Goal instead of assuming the Human already supplied a correct Goal;
2. **Unknown routing**: keep Human choice / repo-runtime fact / Executor How / model-owned default authority distinct;
3. **semantic altitude**: lower-level mechanisms do not decide upstream outcome;
4. **autonomous materialization**: write that same current Taskbook to an authoritative external artifact and surface its path.

Prompt Atlas does not copy Leader's `/goal` surface, fixed six-section layout, fixed question count, acceptance-manager/dark-test role, or filename conventions; none is required for the capabilities above.

## Paired behavioral eval

Under same model / repo snapshot / tool permission / budget / clean session compare:

```text
A. Leader
B. main Prompt Atlas
C. candidate Prompt Atlas
```

Cover at least: ambiguous problem-space shaping, means-vs-outcome, mixed Unknown ownership, simple executable Goal, autonomous materialization, and full re-delivery after Human correction.

Score 0–2: Intent shaping, Unknown routing, Goal fidelity, semantic altitude, judgment abstraction, Executor freedom, Verification/Evidence quality, full re-delivery, artifact handoff, context cost.

### Behavioral pass gate

- candidate has no new critical regression;
- properties survive domain/name perturbation;
- Human-owned blockers are not silently filled by implementation defaults and factual Unknowns are not incorrectly promoted to Human authority;
- a simple Goal does not become complex because of Intent machinery;
- autonomous Taskbook is materially written;
- material Human update always re-delivers the complete current Taskbook;
- without clean-session evidence, do not claim behavioral parity/uplift.

## Claim boundary

Static/scenario smoke proves only contract/property consistency. Without clean-session runner results, behavioral parity is `NOT RUN`.
