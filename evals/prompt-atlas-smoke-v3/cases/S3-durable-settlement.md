# S3 — Cross-context work retains durable settlement state

## Input

The user requests complete behavior-preserving migration from a legacy parser to the canonical parser across all production consumers, followed by legacy deletion.

Visible context:

- the work is expected to span multiple sessions;
- production consumers and tests are available only in the execution runtime;
- the runtime may be restarted or handed to another capable executor;
- batch and streaming behavior must remain unchanged;
- delete the legacy module only after every consumer is migrated;
- no unrelated refactor is authorized.

## Expected invariants

- Terminal state: `Executable`.
- Use explicit Task 0 for consumer/baseline/verifier settlement.
- Retain material settlement and progress durably because the run crosses contexts.
- Use one project-local continuity file, not a second Task-0 state system.
- Reuse still-valid carrier evidence and persist only material runtime deltas.
- Preserve branch parking, evidence invalidation, and complete-Goal acceptance.
- No fixed role topology or Graph beyond real dependencies.

## Frozen output

```markdown
Status: Executable

## Goal
Migrate every production consumer from the legacy parser to the canonical
parser, preserve batch and streaming behavior, and delete the legacy module only
after no consumer or runtime reference remains.

## Task 0 — bind the migration territory
Reuse confirmed intent and boundaries from the carrier. Before modification:
- inventory production consumers and imports unavailable during compile;
- capture batch and streaming behavior baselines;
- identify and validate governing tests/commands, including false-green checks;
- record material carrier/reality disagreement, initial dependency order, and
  largest migration risk.

Retain settlement results and subsequent run state in
`.scratch/parser-migration/IMPLEMENTATION_NOTES.md`: binding decisions,
execution-discovered consumer inventory, completed and invalidated evidence,
parked blockers, remaining Goal conditions, and next safe work. The runtime owns
this one continuity file; it is not repository source of truth and is not
committed automatically.

## Execution
Use a direct adaptive path. Migrate independent consumers when ready, keep shared
parser behavior under one owner, rerun affected evidence when upstream changes
invalidate it, and park only a blocked branch while independent safe work
remains. Delete the legacy module only after no-reference proof and both behavior
families pass.

## Acceptance
Judge the complete Goal: preserved batch and streaming behavior, all production
consumers migrated, no legacy reference remains, protected judging surfaces are
unchanged, and no residual blocker is hidden.
```

## Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Complete migration, preservation, deletion order, and scope retained. |
| Authority precision | PASS | Runtime adapts How while outcomes remain fixed. |
| Terminal routing | PASS | Safe settlement and execution route exist. |
| Settlement coverage | PASS | Consumer, baseline, verifier, disagreement, and route are settled first. |
| Settlement proportionality | PASS | Durable state is justified by cross-session risk. |
| Grounding reuse | PASS | Carrier authority is reused; only runtime-only facts and deltas are persisted. |
| Completion trust | PASS | Complete-Goal gate prevents partial migration from claiming completion. |
