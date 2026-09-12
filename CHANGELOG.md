# Semantic Changelog

This file records **breaking semantic migrations** in the Skill system: Skill removal/rename/merge, stable responsibility movement, and intentional retirement of a previously durable concept or workflow.

It is not the runtime contract and not a commit-by-commit release log. Current semantics live in `AGENTS.md`, each `SKILL.md`, and focused evals. This file answers one historical question: **when a surface disappeared, where did its responsibility go, or was it intentionally retired?**

## PR #95 — Composition moves entirely to the caller

Supersedes the unreleased `6b03114` permission for Prototype to perform delegated composition. Prototype remains one caller-neutral tool constructing the commissioned problem’s prototype/draft, small or complex. Northstar or another authorized caller now owns both selecting and assembling problem-level outputs, organizing calls, and aligning the integrated result with its accepted scope. Do not keep assembly inside Prototype while moving only final approval outside it.

Preserved: coherent internal construction, necessary runnable experiments, original-caller return, one overall intended-change authority, Human clarification/authorized scope change, AE/Verify/Unknowns ownership. Retired: delegated assembly, global composition plans or Prototype-call orchestration inside Prototype. No new Skill, size-specific mode, singleton-artifact rule or composition framework. If caller-side assembly reveals a concrete gap, Prototype may construct that missing behavior under a bounded commission; the caller resumes assembly.

## PR #95 — Historical composable-output interpretation (composition delegation superseded)

Supersedes the unreleased `e978a7f` single-core-Prototype constraint below. Prototype is a caller-neutral tool producing a prototype and draft for a concrete problem; multiple such outputs may be composed. Northstar owns integration into the primary Draft and a complete prototype when useful, aligned with the original Intent or a Human-confirmed scope adjustment. Oversized scope prompts a concrete narrowing/composition discussion, not silent reduction or a new mandatory approval stage.

Preserved: one current intended-change authority, necessary Human clarification/confirmation, real experiment Evidence and existing owner boundaries. Retired: limiting an Intent to one prototype, or forbidding local prototypes merely because an overall Intent exists. Local drafts are allowed but cannot independently redefine that Intent. No new Skill, artifact schema or composition framework.

## PR #95 — Historical single-core interpretation (superseded)

The following describes `e978a7f` only, not the current contract.

Supersedes the earlier #95 per-call cohesive-surface framing: an Intent has one main, core Prototype, not a collection of local prototypes. Views, comparisons and experiments now support that same core; Northstar keeps its primary Draft aligned and actively asks the Human to clarify expectations and confirm material interpretations or requested choices. Technical feasibility does not imply Human acceptance.

Preserved: one intended-change authority, caller-neutral Prototype, independent AE/Verify callers, proportional representations, factual Evidence, and no repeated confirmation for already answered or delegated choices. Retired: treating a set of locally complete experiments as the main Prototype, or treating Northstar as an automatic compiler with Human interaction only for technical blockers. No new Skill, two-file requirement or universal approval stage is introduced.

## 2026-09-11 — Recenter capability ownership around Northstar / Prototype / AE / Verify / Unknowns First

PR: #93 (`refactor/northstar-intent-replay`)

### Top-level Skill migration

| Previous surface | Status | Current owner | Preserved responsibility |
| --- | --- | --- | --- |
| `issue-shape` | **Moved / removed as Skill** | `northstar` | conversation/request → durable engineering Intent; Drafted Issue body/comments contract; tracker materialization; cohesive Issue granularity; durable correction fold-back |
| `intent-shape` | **Renamed / narrowed** | `prototype` | Core Path / Usage / Interface / disposable Prototype as the cheapest concrete reaction surface for already-understood Intent |
| `architecture-shape` | **Merged / removed as Skill** | `architecture-evolution` Target judgment | long-term responsibility / knowledge ownership, justified variation/layering, dependency direction, Target reuse/reopen conditions |
| old `northstar` difficult-intent + compile + outcome-judge surface | **Recentered / split** | `northstar` + `verify` + `architecture-evolution` | Northstar now owns canonical Intent; verification/proof judgment moves to Verify; structural forks move to AE; only earned material compile remains in Northstar |

### Replay clarification

Before PR #93, this skill repo did **not** contain a top-level `replay` Skill. DaVinci already had Replay in its harness as an executable verification system.

An intermediate version of PR #93 incorrectly materialized `replay` as a Skill and assigned it proof semantics. That structure is intentionally withdrawn before merge.

Final responsibility boundary:

- **Verify Skill** owns `claim → proof obligation → backend → Evidence → proven/false/unproven`.
- **Evidence** is the proof basis/artifact produced or consumed by Verify, not the top-level invocation surface.
- **DaVinci harness Replay** remains an execution backend that can produce behavior/equivalence observations/artifacts.
- tests/build/integration/runtime/data/profile and other project-local verification systems are peer backends.
- backend presence never defines the semantic claim or proof sufficiency by itself.

Do not reintroduce a Replay Skill merely because DaVinci exposes Replay execution capability.

### Why `verify`, not `evidence`

pstack exposes verification as an action/skill surface: `prove-it-works` establishes the engineering principle, and project-local `verify-<app>` skills drive the real application and capture Evidence. The useful invocation intent is **verify this**, while Evidence is the output/basis of that verification.

PR #93 briefly used `evidence` as the Skill name while correcting Replay ownership. The final surface is renamed to `verify` without changing the underlying proof contract.

Verify is a **capability, not a mandatory lifecycle stage**. It may be called before implementation to establish a material proof route, during implementation when proof premises change, or after implementation to judge realized results. Existing project-local verifier lifecycle contracts (for example Launch / Doctor / Drive / Capture / Cleanup) remain owned by those backends; Verify follows them instead of creating a second harness workflow.

### Northstar responsibility migration

| Previous responsibility/reference | Current owner / status | Notes |
| --- | --- | --- |
| `intent-shaping.md` — intent take, Human-owned choice, Goal/How framing | `northstar` **minus Goal layer** | Problem / Draft / Constraints / Acceptance / Decisions/Evidence remain; independent `Goal` is intentionally retired |
| `execution-compile.md` — material delta / Graph compile | `northstar/references/material-compile.md` | compressed to an earned path only when complex material dependency blocks a fresh Executor; no mandatory Taskbook/Graph |
| Graph → Evidence → affected dependency cone loop | `northstar` material compile | preserved; research/execution/review/verified Evidence only recompiles the affected cone, not the whole workflow |
| `outcome-judgment.md` — contract-first independent outcome judgment | `verify` | Verify starts from authoritative claims and judges proof as proven / false / unproven |
| `verification-trust.md` — false-pass / evidence sufficiency | `verify` | retained as real-artifact proof, source identity, cheap falsifier and sufficiency semantics |
| `material-decision-review.md` | **Split by owner** | contract/completion proof gap → Verify + Executor; new structural fork → AE; Human commitment → Northstar/Human; ordinary How → Executor |

### Pstack-aligned verification model

The verification responsibility is aligned to the same separation used by pstack:

1. state a checkable finish/safety condition before judging;
2. prove the real artifact instead of relying on proxies such as build green or agent self-report;
3. prefer an existing project verification harness; create new verifier machinery only when the project lacks a checkable path;
4. when proof cannot run or identity/oracle is not trustworthy, report `unproven` / inconclusive rather than rounding up;
5. skill/prompt behavior changes require blinded behavioral eval and are not proven by product Replay.

This repo exposes that responsibility as `verify`; project-specific backend execution stays outside the semantic owner map.

### Architecture migration

`architecture-shape` was removed as a top-level Skill, but its responsibility was **not deleted**. It is now the first internal judgment inside `architecture-evolution`:

```text
Target Architecture judgment
        ↓
Current → Target gap
        ↓
Evolution Program + real exits
```

The Target-vs-Program boundary remains mandatory: current implementation or Program convenience cannot define the long-term Target. Verify may check an already-adopted structural completion claim, but it cannot redesign the Target.

### Unknowns First scope reduction

The old Unknowns First full-map surface included several non-factual moves. Those responsibilities were deliberately redistributed:

| Old Unknowns behavior | Current owner / status |
| --- | --- |
| concrete sample / mock / prototype / "four directions" for reaction | `prototype` |
| intent interview / accepted-outcome or commitment decision | `northstar` / Human |
| long-term ownership / boundary / dependency options | `architecture-evolution` |
| proof plan / false-pass / whole-outcome judgment | `verify`; backend execution may use Replay/test/build/runtime as appropriate |
| implementation/build plan, reviewer checklist, buy-in doc, quiz | **No semantic Skill owner**; caller / Executor / PR may create these artifacts when useful |
| full-map handoff as a second SDLC | **Retired**; L3 now maps coupled factual unknowns / source alignment only |

`unknowns-first` now owns only factual map-versus-territory closure: repo/runtime/data/source facts, provenance, freshness, and source alignment.

### Intentionally retired semantics

The following were **not moved to another owner**. They were intentionally removed from the stable semantic model and should not be restored merely because old files contain them:

- independent `Goal` artifact / field / lifecycle;
- mandatory `Goal → Target → Taskbook → execution` chain;
- mandatory Taskbook or explicit Graph for clear Issues;
- mandatory independent verification ceremony after every PR;
- a second `intent.md → spec.md → plan.md` SOT chain;
- Unknowns First as a second end-to-end SDLC / handoff workflow;
- execution control plane / MultiCA as a semantic stage or reasoning owner;
- verifier/backend such as DaVinci Replay as a semantic Skill owner;
- top-level `architecture-shape` as a separate invocation surface;
- persistent Graph state / scheduler / manager protocol owned by Northstar;
- exhaustive decision ledger or mandatory material-decision review for ordinary implementation choices.

### Artifact ownership after migration

- **Drafted Issue** — durable carrier of Northstar Intent / intended change.
- **PR** — realized change, implementation How, implementation-local validation and review.
- **Prototype artifact** — disposable reaction surface; durable correction/Evidence returns to the caller.
- **Architecture handoff** — persisted only when independently useful; otherwise durable structural decisions fold back to the caller / Issue.
- **Verify result** — Claim + proof obligation + source/backend identity + material Evidence + proven/false/unproven verdict + owner routing. It stays with PR/review/verification by default; only durable contract/architecture corrections fold back to their semantic owner.
- **Replay/test/build/runtime artifacts** — backend outputs consumed as Evidence; they are not a second semantic SOT.

### Eval migration

Old eval directories tied to removed surfaces were replaced by owner-focused contracts:

- `evals/issue-shape` → `evals/northstar` + `evals/northstar-paired`
- `evals/intent-shape` → `evals/prototype`
- `evals/architecture-shape` + old goal-driven AE eval → `evals/architecture-evolution`
- old Northstar outcome/verification cases → `evals/verify`
- narrowed factual boundary → `evals/unknowns-first`

The paired Northstar scorer is retained, but now measures **Intent handoff quality** rather than verification. Changes to Verify/Skill behavior should use blinded clean-session behavioral eval; DaVinci Replay verifies product behavior, not whether this Skill design improves agent behavior.

### Reintroduction rule

A retired responsibility may be reintroduced only with new current Evidence that it has a stable semantic owner and an independent invocation reason. Historical presence or availability of an execution backend alone is not justification.
