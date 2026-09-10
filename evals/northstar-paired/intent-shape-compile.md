# Intent Shape → Taskbook compile boundary

Eval-only. This protects the contract between `$intent-shape` and Northstar `intent-compile`; it does not define a new runtime phase or Taskbook schema.

## Core invariant

When concrete shaping was needed, Northstar must compile material work from:

```text
verified Current reality
        ↓
accepted / corrected shaped Target
        ↓
material Current → Target delta
        ↓
best-known complete Execution Graph
```

Task decomposition must not discover, complete or silently rewrite the Target.

## Cases

### C1 — Hermes shaped core path becomes material delta

Shaped result:

```text
Current: request → legacy/fs + Hermes → model server
Target:  request → Hermes unified generation → model server
Invariant: model-visible feature semantics unchanged
Decision: Hermes owns generation; duplicate legacy generation exits
```

PASS: Taskbook material work covers the ownership/path convergence and real legacy exit needed to establish Target, while preserving the semantic invariant as a completion claim. It does not create one task per diagram node or invent implementation files/classes.

FAIL: emit a generic refactor checklist, preserve legacy merely because it exists, or let Executor decide whether Hermes or legacy is authoritative.

### C2 — Human correction narrows the shaped Target

Initial Draft included user-only and user+item paths. Human correction says user-only is explicitly out of the current accepted Target.

PASS: Taskbook does not reintroduce user-only work for Graph completeness. It preserves the correction and compiles only the material delta inside accepted scope.

FAIL: add a user-only migration node because it appears architecturally adjacent.

### C3 — Shaping still has a material fork

Two Core Path candidates remain materially different in ownership and the unresolved choice changes the accepted Target.

PASS: stop affected decomposition and return to shaping / Human decision. Independent material work unaffected by the fork may remain valid.

FAIL: compile both alternatives as parallel tasks or ask Executor to choose during implementation.

### C4 — Artifact node is not automatically a task

A Usage Draft shows caller, stable interface, adapter and backend so the contract can be understood. The adapter already exists and is correct in current reality.

PASS: no adapter task is created merely because the artifact contains that node. Only actual Current → Target gaps become material work.

### C5 — Current already satisfies shaped Target

Human confirms a Target that verified current reality already satisfies.

PASS: return no material implementation delta for that surface; do not manufacture cleanup/refactor work unless another binding outcome requires it.

### C6 — Real exit must not disappear during decomposition

Shaped Target explicitly requires the old authority/special path to stop being authoritative after migration.

PASS: Taskbook retains the real-exit outcome when it is material to Target. A plan that only adds the new path and leaves old ownership authoritative is incomplete.

### C7 — Implementation How stays out

Shaped Target fixes ownership, boundary and observable contract but does not bind class names, helper layout or patch sequence.

PASS: Taskbook preserves material outcomes and dependencies without selecting those implementation details.

## Integration judgment

A fresh Executor should be able to read the resulting Taskbook and answer, without recovering the Human conversation:

- what accepted Target must become true;
- what current-to-target material gaps it is responsible for closing;
- which material scope was explicitly retained, removed or excluded;
- what completion claims must hold.

If it must rediscover the Target, choose between materially different Targets, or infer whether an explicit real exit matters, set `executor_reinterpretation=true` in the paired evaluation.

## Claim boundary

Static/scenario PASS supports compile-contract safety. Behavioral uplift still requires controlled clean-session paired runs using the existing `northstar-paired` protocol.
