# S4 — Artifact request stops at handoff

## Input

The user asks:

> Write a prompt/task brief for another coding agent to consolidate the two parser modules. Do not modify the repository.

The current runtime has repository access, but the user explicitly requests only a reusable handoff artifact.

## Expected invariants

- Terminal state: `Executable` when intent and carrier are complete.
- Mode: artifact-only.
- Do not modify the repository or begin execution.
- Delegated defaults remain visible for review.
- Preserve proportional pre-execution settlement for the downstream runtime.
- The downstream runtime reuses grounded carrier facts and checks only stale, disputed, or execution-only reality.

## Frozen output

```markdown
Status: Executable

## Goal
Consolidate the legacy parser into the canonical parser, migrate every consumer,
preserve confirmed behavior, and remove the legacy module after structural and
behavioral proof.

## Boundaries
Do not perform unrelated refactoring, weaken governing tests, or delete the
legacy module before all production consumers are migrated and verified.

## Execution carrier
The downstream runtime first binds the actual repository and reuses the
still-valid grounded facts in this carrier. It checks only execution-only,
stale, or disputed facts: current consumer inventory, governing verifier
behavior, relevant baselines, and material carrier/reality disagreement. Keep
that settlement inline when the remaining checks are clear; serialize Task 0
when named material uncertainty remains. Then use the smallest dependency path
through canonical behavior extension, consumer migration, no-reference proof,
legacy deletion, and complete-Goal acceptance.

## Delivery
Return the implementation diff, executed evidence, residuals, and truthful final
verdict.

Artifact-only: return this carrier for review or forwarding. Do not modify the
repository in this run.
```

## Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Produces a reusable task brief and respects no-modification. |
| Authority precision | PASS | Execution remains downstream-owned. |
| Terminal routing | PASS | The carrier itself is complete. |
| Settlement coverage | PASS | Downstream bind/verify/align route is preserved. |
| Settlement proportionality | PASS | Inline versus explicit form follows grounded risk. |
| Grounding reuse | PASS | Existing carrier facts are reused; only stale/disputed/runtime facts are checked. |
| Execution-mode fidelity | PASS | Stops at artifact handoff despite repository access. |
| Completion trust | PASS | Proof obligations survive the handoff boundary. |
