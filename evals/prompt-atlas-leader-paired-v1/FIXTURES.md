# Prompt Atlas × Leader paired EVA v1 — preregistered fixture index

These four synthetic fixtures are frozen before any paired run. Each file contains the exact task input, repository generator, protected surfaces, forced conditions, budget, public oracle manifest, and manifest SHA-256.

- [F1 — False-green discount normalization](fixtures/F1-false-green.md)
- [F2 — Behavior-preserving parser migration](fixtures/F2-parser-migration.md)
- [F3 — Branch-local blocker with independent safe work](fixtures/F3-branch-blocker.md)
- [F4 — Forced cross-context parser migration](fixtures/F4-cross-context.md)

## Freeze rule

Do not alter a fixture after either arm begins. A necessary correction creates a new fixture version and invalidates prior runs for that fixture.

The public oracle manifest freezes judged properties without exposing private cases. Before execution, record the private oracle implementation SHA-256. It may test only the properties in the registered manifest.

Each setup script creates a fresh local Git repository. Generate separate but byte-identical starting repositories for Prompt Atlas and Leader arms and record their initial commit SHAs.

See [`PLAN.md`](PLAN.md) for isolation, forced-event, run-record, and capability-floor rules.
