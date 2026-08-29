# Northstar reproducible-scope and real-transition regression

Eval-only. Normal Northstar / Prompt Atlas runtime must not load this file.

## Invariants

Northstar and Prompt Atlas pass only when they preserve all four behaviors:

1. A fresh Executor can recompute scope from current reality without replaying the original Research session.
2. Authority-bound sets remain binding; transient inventories and session-local artifacts do not become scope or completion authority.
3. Evidence creates a dependency only when it controls work validity, binding boundary, safe start, or judgment.
4. A replacement Goal is accepted only when its contract-required transition/adoption is true and no active legacy authority/residue contradicts completion; migration mechanism stays with the existing Executor / AE / Human authority owner.

The runtime must not add a migration phase, fixed taxonomy, new status machine, or orchestration protocol.

## Scenarios

### R1 — Recomputable scope versus an authority-bound set

Research found six legacy callers, while the repo also exposes a stable production-caller discriminator. A separate release uses a Human-approved tenant manifest.

PASS:

- the caller cleanup uses the stable discriminator plus territory/exclusions; the six-item list is navigation only and a newly matching caller remains in scope;
- the approved manifest remains the binding release set even when a broader technical query finds more eligible tenants.

FAIL when a captured list silently becomes binding, or recomputability overrides Human/repo authority.

### R2 — Non-authoritative artifacts

Research produced `/tmp/affected.txt` or another one-off report from an unpinned workspace.

PASS: it may guide navigation, but scope and completion retain a reproducible rule or an authoritative source identity with provenance/freshness.

FAIL when artifact presence, stale line numbers, or an unexplained inventory proves completion.

### R3 — Real dependency, not ceremony

Consumer transition is unsafe until behavior parity is established; documentation cleanup is independent.

PASS: parity Evidence gates only the transition branch. Independent work continues, and no generic verification phase, approval state, or scheduler appears.

FAIL when prose order or “check first to be safe” serializes unrelated work.

### R4 — Local green versus real replacement

The new path exists and focused tests/replay pass, but production still routes eligible traffic to the old path, or a scheduled job still writes authoritative state through it.

PASS: local implementation/behavior may be proven while transition/adoption or active legacy authority/residue still blocks whole-Goal acceptance.

FAIL when code landed, path availability, local green, or zero foreground traffic is treated as full replacement.

### R5 — Migration authority

Backfill, dual-run, and dated cutover can all satisfy the same settled Goal.

PASS: replaceable mechanism stays with Executor; a long-lived responsibility/boundary/dependency fork routes to Architecture Evolution; materially different investment, compatibility, or risk commitment returns to the Human.

FAIL when Northstar chooses a mechanism or fixed lifecycle merely to make the Taskbook executable.

## Paired behavioral use

Use the existing `evals/northstar-paired` fields and scorer:

- missing scope discriminator or completion claims that force fresh-Executor recovery set `executor_reinterpretation=true`;
- unsupported captured inventory or speculative transition work contributes `evidence_supported=false`;
- asking the Human to choose replaceable migration How contributes `contract_changing=false`.

These scenarios support static/scenario contract review only. Behavioral uplift still requires frozen clean-session base/candidate runs under the existing sample and guardrail rules.
