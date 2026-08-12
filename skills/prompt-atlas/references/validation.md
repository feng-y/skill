# Prompt Atlas Validation

Use only for explicit review / smoke / eval. Normal runtime must not read this file. It tests behavior; it does not redefine Prompt Atlas.

## Static smoke

1. The main Skill has a clear `Take → Ground → Shape → Compile → Deliver` flow without a lifecycle/status machine.
2. A means named by the Human does not automatically become Goal; when a materially different implementation would still satisfy the Human, How remains with the Executor.
3. Research closes only facts that can change what counts as done or prevent safe material work from starting; rich repo authority is referenced directly, and the current workspace is treated as reality rather than an error state.
4. Facts repo/runtime can settle are investigated first. Only choices reality cannot make and that genuinely change the Human's accepted outcome are returned to the Human, surfaced together rather than serially.
5. The Taskbook filters content by whether omission would make the Executor judge incorrectly. Open surfaces carry a stable judgment rather than a closed checklist, and the currently safe frontier never shrinks the full Goal.
6. Verification states what must be proven rather than prescribing debugging order. The judge cannot be weakened to manufacture PASS, and extra trust checks appear only for a concrete false-green risk.
7. Normal tasks return the complete current text; autonomous handoff actually writes the same Taskbook to an artifact outside repo/workspace. After material Human correction, the complete current Taskbook is delivered again; prior delivery is not completion state.

Static smoke requires 7/7 PASS.

## Scenario smoke

### S1 — The Human names a How
The Human says “use Redis to make it faster,” while repo reality still supports other plausible approaches.

PASS: Prompt Atlas recovers the performance outcome first. Redis becomes binding only when Human/repo authority actually requires it.

### S2 — The Human only gives a problem space
The Human says “modernize this historical module,” and reality supports several materially different end states.

PASS: Prompt Atlas does not choose its favorite architecture for the Human. It investigates facts that can remove forks, then surfaces only the remaining real choices.

### S3 — Three kinds of uncertainty appear together
One question is answerable from the repo, one changes final product behavior, and one is only about code shape.

PASS: investigate the first, ask the Human about the second, leave the third to the Executor. Do not turn all three into Human questions or a Research backlog.

### S4 — Research is already sufficient
A cleanup still has many unenumerated instances, but one stable rule is enough for the Executor to decide what should be removed or kept.

PASS: stop enumerating, write the rule and its territory, and hand off. A complete inventory is not a prerequisite.

### S5 — A directory is not the boundary
The target directory contains both legacy-only code and shared code still used in production.

PASS: the Taskbook carries the responsibility rule and behavior that must survive. It does not require the directory to disappear or list every currently found symbol as the answer.

### S6 — The workspace already contains useful work
Prompt Atlas starts with a set of changes aligned with the Human Goal but not yet verified.

PASS: continue from that reality. Do not require a clean checkout, treat the diff as correctness Evidence, or shrink Goal to “finish this diff.”

### S7 — Known relations and future unknowns coexist
Current Evidence proves `A → {B,C} → D`, while execution may still reveal contingent work later.

PASS: compile the established relations because they change execution choices; do not intentionally hide them behind A, and do not predict future contingent work.

### S8 — Reality changes during execution
A baseline or dependency assumed by the Taskbook is contradicted by authoritative runtime evidence.

PASS: invalidate only dependent work and verification; preserve the Goal and still-valid Evidence.

### S9 — PASS may be false green
The acceptance check can be bypassed by skip, mock, threshold changes, or it never observes the real behavior.

PASS: never weaken the judge. Add only the smallest check that counters this specific failure mode. Without a concrete risk, do not mechanically add hidden or independent review machinery.

### S10 — A simple Goal stays simple
The Human already gave a clear outcome, boundaries, and proof, and repo reality exposes no upstream fork.

PASS: Ground briefly, then Compile/Deliver. Do not create questions, terminology, or phases merely to demonstrate the intent machinery.

### S11 — Autonomous handoff is corrected later
Prompt Atlas has already written the Taskbook to an external artifact; the Human then changes a requirement that materially affects the outcome.

PASS: re-enter at the affected step, update or rewrite the complete current Taskbook, and surface the authoritative path. A delta-only reply fails. Prompt Atlas must not execute the Taskbook itself.

## Compare with Leader

Leader is a behavioral baseline, not an answer oracle. Prompt Atlas must at least preserve these useful behaviors: investigate facts before asking the Human; batch real Human choices; reference existing specs directly; keep the final Taskbook shorter than the Research behind it; and prevent the Executor from manufacturing success by changing the judge.

Prompt Atlas must additionally show two capabilities: **when the Human has not yet supplied the right Goal, it can settle what outcome the Human actually wants; and for autonomous work it can materially hand the complete current Taskbook to a fresh Executor instead of stopping at chat prose.**

## Behavioral eval

Under the same model / repo snapshot / tool permission / clean session, cover at least: ambiguous problem space, named means, mixed fact/Human/How, a simple executable Goal, open-surface cleanup, autonomous materialization, and full re-delivery after Human correction.

Without clean-session results, only static/scenario contract review may be claimed; behavioral parity/uplift remains `NOT RUN`.
