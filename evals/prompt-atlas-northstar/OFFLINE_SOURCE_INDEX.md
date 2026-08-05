# Bundle-First Offline Source Index

This index replaces the 12-link acquisition path for clean-session evaluation.

## Acquisition contract

Before generating candidates:

1. Read `VALIDATION_PLAN.md` completely.
2. Open all three bundles below in the same turn/session.
3. Do not return an intermediate status such as “the 12 sources are not loaded.” The purpose of the bundles is to load all 12 sources through three files.
4. Verify the bundle heading, included source IDs, and bundle blob SHA.
5. Treat the fenced source sections inside each bundle as the exact authority. Do not summarize them before candidate generation.
6. Begin the 8-case evaluation only after all three bundles are loaded.

## Bundles

### B-P — Prompt Atlas, P1–P5

- URL: https://github.com/feng-y/skill/blob/898a35f85cfe6c53ee9c6fe7fb3332b2ec71c314/evals/prompt-atlas-northstar/PROMPT_ATLAS_BUNDLE.md
- Expected heading: `# Prompt Atlas Source Bundle`
- Expected blob SHA: `b7b80fe19e78b55020eb054f4c42cac5c0a4b0b0`
- Embedded source IDs: P1, P2, P3, P4, P5

### B-N — Northstar, N1–N5

- URL: https://github.com/feng-y/skill/blob/898a35f85cfe6c53ee9c6fe7fb3332b2ec71c314/evals/prompt-atlas-northstar/NORTHSTAR_BUNDLE.md
- Expected heading: `# Northstar Source Bundle`
- Expected blob SHA: `55b28ee185d10c9f0fc2ad6935e455a0fe682060`
- Embedded source IDs: N1, N2, N3, N4, N5

### B-L — Leader, L1–L2

- URL: https://github.com/feng-y/skill/blob/898a35f85cfe6c53ee9c6fe7fb3332b2ec71c314/evals/prompt-atlas-northstar/LEADER_BUNDLE.md
- Expected heading: `# Leader Source Bundle`
- Expected blob SHA: `ba6a46287172fa4bb60f12eb4aa4f1d8109a04ab`
- Embedded source IDs: L1, L2

## Required source-load table

Use this table before candidate outputs:

| Bundle | Embedded sources | Status | Retrieval method | Evidence |
|---|---|---|---|---|
| B-P | P1–P5 |  |  | heading + blob SHA |
| B-N | N1–N5 |  |  | heading + blob SHA |
| B-L | L1–L2 |  |  | heading + blob SHA |

When all three rows are `LOADED`, all 12 sources are loaded and evaluation must continue in the same response/workflow.

If a bundle genuinely cannot be opened, report the exact failed bundle URL and the attempted retrieval method. Do not report the individual embedded sources as unloaded without first attempting the bundle URL.
