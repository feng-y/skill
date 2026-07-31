# Prompt Atlas smoke v3 — frozen case index

Each case is frozen independently so its input, invariants, output, and score have an addressable blob. `RESULTS.md` records every case blob and the evaluated skill/reference blobs.

- [S1 — Clear local task uses inline settlement](cases/S1-inline-settlement.md)
- [S2 — Execution-only verifier uncertainty uses explicit Task 0](cases/S2-explicit-task0.md)
- [S3 — Cross-context work retains durable settlement state](cases/S3-durable-settlement.md)
- [S4 — Artifact request stops at handoff](cases/S4-artifact-only.md)
- [S5 — Direct structural proof allows self-acceptance](cases/S5-self-acceptance.md)
- [S6 — Manipulable proof requires independent acceptance](cases/S6-independent-acceptance.md)

Case outputs were produced and scored in the implementation conversation. They are auditable and independently re-scorable from repository evidence, but they are not clean-session reproduction runs or behavioral executor EVA.
