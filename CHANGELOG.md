# Semantic Changelog

This file records **breaking semantic migrations** in the Skill system: Skill removal/rename/merge, stable responsibility movement, and intentional retirement of a previously durable concept or workflow.

It is not the runtime contract and not a commit-by-commit release log. Current semantics live in `AGENTS.md`, each `SKILL.md`, and focused evals. This file answers one historical question: **when a surface disappeared, where did its responsibility go, or was it intentionally retired?**

## 2026-09-23 — Northstar plan becomes a file-backed primary artifact

Change: `fix/northstar-persisted-plan-artifact-20260923` (based on `c4de492bc3d2a8ea6433fbddf8564671dd5a8487`)

Northstar previously required a canonical Taskbook only for material / cross-session work. A design-only or otherwise reusable current Draft could still be returned only in the active conversation or host UI, which made the actual plan disappear with the session and blurred the difference between durable artifact and presentation surface.

- **Canonical plan artifact:** once a Northstar Draft is reusable for review, implementation, or handoff, it is persisted as one real Markdown plan file in the repo/workspace.
- **Taskbook relation:** material execution does not create a second plan. The same plan file takes on the Taskbook role by adding material task/status, decisive Evidence pointers, last Northstar judgment, and next owner.
- **UI boundary:** chat text, canvas/container/panel, or another host UI may summarize or render the plan but cannot be its only storage or authority.
- **Handoff boundary:** session handoff points to the persisted plan/Taskbook and carries resume delta only; it never serializes a copy of the plan.
- **Preserved:** current Draft semantics, Intent ownership, execution authorization boundary, worker autonomy, Northstar acceptance judgment, and Verify ownership of proof sufficiency.
- **Retired:** session/UI-only reusable Drafts and the interpretation of Taskbook as a separate plan-like artifact created only when work becomes material.
- **Evidence status:** the design-only Northstar eval now fails when an execution-ready reusable plan exists only in chat/UI without a persisted workspace/repo file.

## 2026-09-19 — Beacon returns to repo-grounded core prototypes

Change: `fix/beacon-core-prototype-20260919` (based on `4728ca5e1ffd04b434c58a9ba870297ede630f82`)

- **Old surface:** generalized local decision closure / concrete contrast, with a prototype treated as only an optional technique and materially different alternatives as an invocation prerequisite.
- **Current owner:** `beacon` builds one minimal, repo-grounded core prototype of a bounded feature intent or fault. A connected sketch, representative input/output, minimal implementation, or reproducer may express it; executable code is not mandatory.
- **Preserved:** caller-neutral/model-invoked routing, bounded scope, local artifact refinement, explicit return, non-authoritative output, and no production implementation. Known fault behavior can be represented while root cause remains unverified.
- **Responsibility boundaries:** selection/comparison/composition remain with the caller; factual closure with Unknowns First; Target judgment with AE; proof sufficiency with Verify. Evidence and questions support the prototype instead of replacing it.
- **Retired:** the generalized question/experiment-service interpretation and multi-candidate comparison as Beacon output; evidence-only or decision-only completion; requiring an invented ambiguity or complete root-cause closure before a useful core prototype. The stale `$prototype` route in Unknowns First's full-map reference now points to `$beacon`; the old invocation identity stays retired. No new Skill or protocol is added.
- **Evidence status:** focused eval specifications are updated, not a measured behavioral uplift.

## 2026-09-18 — Northstar persistent Taskbook + delta-only session handoff

Change: `fix/northstar-taskbook-handoff-20260918`

Northstar previously kept the current Draft continuous but treated Drafted Issue / durable handoff as the main transfer surface and explicitly avoided a default Taskbook. In material multi-task work this let session handoff absorb the full design, and the runtime wording also blurred “execution is authorized under Northstar context” with “Northstar itself continues implementation”.

- **Canonical durable surface:** material or cross-session Northstar work now persists as one Taskbook containing the current Draft, binding Decisions / Constraints / Acceptance, minimal material tasks / status, decisive Evidence pointers, last Northstar judgment, and next owner.
- **Session handoff:** reduced to a resume delta that points to the Taskbook. Architecture, full plan, Acceptance, out-of-scope and other durable content belong in the Taskbook and must not be duplicated into handoff or the next-session prompt.
- **Execution boundary:** Northstar owns semantic control, task dispatch and task acceptance, but does not execute implementation or low-level orchestration mechanics. Workers own implementation How and return result / Evidence.
- **Judgment boundary:** worker `done`, patch, test green or PR existence are submissions, not canonical acceptance. Northstar decides whether the material task satisfies Intent / Acceptance and updates the Taskbook; Verify still owns proof obligation and Evidence sufficiency.
- **Issue boundary:** Drafted Issue remains a tracker / external carrier. When a repo-local Taskbook exists it points to that canonical source instead of becoming a parallel plan.
- **Preserved behavior:** execution-ready remains separate from Human execution authorization; existing scoped authorization is reused without approval loops; later material clarification and Evidence only reopen affected semantics.
- **Retired semantics:** long-form handoff as a duplicate plan, session prompt as a copied execution spec, Northstar wording that implies it personally implements the authorized change, and worker self-report as sufficient task closure.

## 2026-09-16 — Northstar execution-ready ≠ execution authorization

PR: #99 (`fix-northstar-execution-authorization`)

Northstar previously used `executable handoff` for both semantic readiness and permission/transition to execution. That overloaded one term and could either start durable implementation after a design-only request or force a second approval after the Human had already requested implementation.

- **Current semantic:** `execution-ready` means the current canonical Draft is specific enough that an implementer need not invent material Intent. It is not semantic finality and does not grant execution authorization.
- **Authorization source:** recover scoped execution authorization from the Human request's meaning. Existing or later requests to implement/fix/change are reused without a redundant confirmation; analysis/design/review/evaluation wording does not authorize the named action merely because it contains an action word. Authorization stays bound to the requested object and action rather than expanding implementation into commit/merge/rollout.
- **Preserved behavior:** Northstar keeps Intent continuity through implementation and Evidence feedback; ordinary implementation How remains autonomous; material clarification reopens only the affected semantic owner.
- **Durable handoff:** retained only for real transfer across session/agent/environment or explicit requested handoff. A handoff carries the current Intent but does not invent authorization.
- **Retired semantics:** readiness as implicit execution permission, readiness as an automatic handoff to a synthetic Executor lifecycle, and repeated approval after authorization already exists.
- **Control-plane boundary:** Northstar does not start/pause/resume/retry execution or own progress. Compile can make material work execution-ready but cannot create authorization.

## 2026-09-14 — Prototype → Beacon

PR: #96 (`refactor/beacon-intent-shaping`)

`prototype` as a top-level Skill identity is replaced by `beacon` because the responsibility is broader and more neutral than the prototype technique itself.

- **Canonical owner:** `beacon` — caller-neutral, primarily model-invoked local intent concretization. It takes one bounded part of an already-understood semantic question and makes the material concrete difference inspectable.
- **Preserved behavior:** cheapest sufficient Core Path / Usage / Interface / concrete artifact; correction / Evidence returns to the original caller; the caller keeps semantic ownership.
- **Prototype after migration:** prototype/mock/minimal implementation remains one optional implementation technique inside Beacon. It no longer defines the top-level Skill identity.
- **Northstar boundary:** Northstar still owns complete Intent, composition, and final compilation. Multiple local Beacon artifacts do not compose themselves.
- **Caller migration:** Northstar, Architecture Evolution, Verify, and Unknowns First now invoke `$beacon` directly.
- **Removed surfaces:** `skills/prototype` and `evals/prototype` are removed after caller migration; there is no `$prototype` runtime route.
- **Invocation:** Beacon is model-invoked. Its `SKILL.md` does not disable model invocation, and `agents/openai.yaml` does not disable implicit invocation; model-facing trigger semantics live in `description`.

Focused behavioral contract lives in `evals/beacon`.

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
