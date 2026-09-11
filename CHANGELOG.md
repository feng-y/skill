# Semantic Changelog

This file records **breaking semantic migrations** in the Skill system: Skill removal/rename/merge, stable responsibility movement, and intentional retirement of a previously durable concept or workflow.

It is not the runtime contract and not a commit-by-commit release log. Current semantics live in `AGENTS.md`, each `SKILL.md`, and focused evals. This file answers one historical question: **when a surface disappeared, where did its responsibility go, or was it intentionally retired?**

## 2026-09-11 — Recenter capability ownership around Northstar / Prototype / AE / Replay / Unknowns First

PR: #93 (`refactor/northstar-intent-replay`)

### Top-level Skill migration

| Previous surface | Status | Current owner | Preserved responsibility |
| --- | --- | --- | --- |
| `issue-shape` | **Moved / removed as Skill** | `northstar` | conversation/request → durable engineering Intent; Drafted Issue body/comments contract; tracker materialization; cohesive Issue granularity; durable correction fold-back |
| `intent-shape` | **Renamed / narrowed** | `prototype` | Core Path / Usage / Interface / disposable Prototype as the cheapest concrete reaction surface for already-understood Intent |
| `architecture-shape` | **Merged / removed as Skill** | `architecture-evolution` Target judgment | long-term responsibility / knowledge ownership, justified variation/layering, dependency direction, Target reuse/reopen conditions |
| old `northstar` difficult-intent + compile + outcome-judge surface | **Recentered / split** | `northstar` + `replay` + `architecture-evolution` | Northstar now owns canonical Intent; independent verification moved to Replay; structural forks move to AE; only earned material compile remains in Northstar |

### Northstar responsibility migration

| Previous responsibility/reference | Current owner / status | Notes |
| --- | --- | --- |
| `intent-shaping.md` — intent take, Human-owned choice, Goal/How framing | `northstar` **minus Goal layer** | Problem / Draft / Constraints / Acceptance / Decisions/Evidence remain; independent `Goal` is intentionally retired |
| `execution-compile.md` — material delta / Graph compile | `northstar/references/material-compile.md` | compressed to an earned path only when complex material dependency blocks a fresh Executor; no mandatory Taskbook/Graph |
| Graph → Evidence → affected dependency cone loop | `northstar` material compile | preserved; research/execution/review/Replay Evidence only recompiles the affected cone, not the whole workflow |
| `outcome-judgment.md` — contract-first independent outcome judgment | `replay` | Replay judges material completion claims as proven / false / unproven when independent verification is earned |
| `verification-trust.md` — false-pass / evidence sufficiency | `replay` | retained as Replay's claim-relevant proof and cheap counter-check semantics, not as a separate reference |
| `material-decision-review.md` | **Split by owner** | contract violation / completion gap → Replay + Executor; new structural fork → AE; Human commitment → Northstar/Human; ordinary How → Executor |

### Architecture migration

`architecture-shape` was removed as a top-level Skill, but its responsibility was **not deleted**. It is now the first internal judgment inside `architecture-evolution`:

```text
Target Architecture judgment
        ↓
Current → Target gap
        ↓
Evolution Program + real exits
```

The Target-vs-Program boundary remains mandatory: current implementation or Program convenience cannot define the long-term Target. Replay may verify an already-adopted structural completion claim, but it cannot redesign the Target.

### Unknowns First scope reduction

The old Unknowns First full-map surface included several non-factual moves. Those responsibilities were deliberately redistributed:

| Old Unknowns behavior | Current owner / status |
| --- | --- |
| concrete sample / mock / prototype / "four directions" for reaction | `prototype` |
| intent interview / accepted-outcome or commitment decision | `northstar` / Human |
| long-term ownership / boundary / dependency options | `architecture-evolution` |
| proof plan / false-pass / whole-outcome judgment | `replay` when independent verification is earned; implementation-local checks stay with Executor |
| implementation/build plan, reviewer checklist, buy-in doc, quiz | **No semantic Skill owner**; caller / Executor / PR may create these artifacts when useful |
| full-map handoff as a second SDLC | **Retired**; L3 now maps coupled factual unknowns / source alignment only |

`unknowns-first` now owns only factual map-versus-territory closure: repo/runtime/data/source facts, provenance, freshness, and source alignment.

### Intentionally retired semantics

The following were **not moved to another owner**. They were intentionally removed from the stable semantic model and should not be restored merely because old files contain them:

- independent `Goal` artifact / field / lifecycle;
- mandatory `Goal → Target → Taskbook → execution` chain;
- mandatory Taskbook or explicit Graph for clear Issues;
- mandatory Replay after every PR;
- a second `intent.md → spec.md → plan.md` SOT chain;
- Unknowns First as a second end-to-end SDLC / handoff workflow;
- execution control plane / MultiCA as a semantic stage or reasoning owner;
- top-level `architecture-shape` as a separate invocation surface;
- persistent Graph state / scheduler / manager protocol owned by Northstar;
- exhaustive decision ledger or mandatory material-decision review for ordinary implementation choices.

### Artifact ownership after migration

- **Drafted Issue** — durable carrier of Northstar Intent / intended change.
- **PR** — realized change, implementation How, implementation-local validation and review.
- **Prototype artifact** — disposable reaction surface; durable correction/Evidence returns to the caller.
- **Architecture handoff** — persisted only when independently useful; otherwise durable structural decisions fold back to the caller / Issue.
- **Replay result** — independent claim judgment + Evidence basis + owner routing; not a repair plan or progress manager.

### Eval migration

Old eval directories tied to removed surfaces were replaced by owner-focused contracts:

- `evals/issue-shape` → `evals/northstar` + `evals/northstar-paired`
- `evals/intent-shape` → `evals/prototype`
- `evals/architecture-shape` + old goal-driven AE eval → `evals/architecture-evolution`
- old Northstar outcome/verification cases → `evals/replay`
- narrowed factual boundary → `evals/unknowns-first`

The paired Northstar scorer is retained, but now measures **Intent handoff quality** rather than Northstar-owned verification.

### Reintroduction rule

A retired responsibility may be reintroduced only with new current Evidence that it has a stable semantic owner and an independent invocation reason. Historical presence alone is not justification.
