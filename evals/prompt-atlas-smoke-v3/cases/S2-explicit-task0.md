# S2 — Execution-only verifier uncertainty uses explicit Task 0

## Input

The user asks for a behavior-preserving schema-v2 loader migration.

Visible compile context:

- repository documentation names `./check.sh` as the acceptance command;
- the compiler cannot execute the target build environment;
- the downstream runtime has repository and build access;
- whether `check.sh` exercises the loader, whether schema-v2 capability exists, and the current behavior baseline are unknown;
- changing public behavior or protected schema semantics is not authorized.

## Expected invariants

- Terminal state: `Executable`.
- Preserve the migration Goal and behavior/schema boundaries.
- Serialize explicit Task 0 because named material preconditions are execution-only and a wrong assumption would create false proof or rework.
- Reuse confirmed carrier facts; investigate only execution-sensitive or unverified facts.
- Verify command failure sensitivity, baseline, runtime capability, and carrier/reality agreement.
- Factual mismatch inside intent revises the route; intent/boundary conflict returns to Intent Take.
- No Human question for facts the runtime can inspect.

## Frozen output

```markdown
Status: Executable

## Goal
Migrate the configuration loader to schema v2 while preserving current public
behavior and protected schema semantics.

## Task 0 — settle execution-only preconditions
Reuse the carrier's confirmed Goal and boundaries. Before modification:
1. Bind the actual workspace, loader entrypoint, schema files, and protected
   judging surfaces.
2. Run `./check.sh` and prove it is failure-sensitive and actually exercises the
   loader rather than treating exit 0 as sufficient evidence.
3. Capture the current loader behavior baseline and governing verifier.
4. Confirm schema-v2 runtime capability and required dependencies.
5. Record only material disagreement or unverified assumptions together with the
   initial route and largest risk.

Routing:
- facts and understanding align → begin the migration;
- a clear carrier misread → correct it and continue;
- command, baseline, or route assumptions differ while intent and boundaries
  still hold → revise the route and continue;
- preserving behavior or protected schema semantics is impossible → return to
  Intent Take before affected modification;
- no safe work remains because required access/capability is missing → Blocked.

## Acceptance
Use the verified governing surface and direct behavior comparison. Do not weaken
or replace protected schema or proof semantics.
```

## Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Migration and preservation remain binding. |
| Authority precision | PASS | Runtime facts are investigated; boundary changes remain Human-owned. |
| Terminal routing | PASS | A finite safe first task exists. |
| Settlement coverage | PASS | Verifier, baseline, capability, alignment, and routing included. |
| Settlement proportionality | PASS | Explicit Task 0 is justified by named execution-only risks. |
| Grounding reuse | PASS | Confirmed Goal/boundaries are reused; only unverified execution facts are checked. |
| Completion trust | PASS | Requires failure sensitivity rather than nominal command success. |
