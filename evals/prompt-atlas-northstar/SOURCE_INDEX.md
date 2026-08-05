# Clean-Session Validation Source Index

This file makes source acquisition explicit and reproducible.

## Acquisition contract

Before generating any candidate output:

1. Open every source below.
2. Record a source-load table with `LOADED` or `FAILED` for each item.
3. Do not begin evaluation unless all 12 sources are loaded.
4. Prefer a GitHub repository connector. If unavailable, use web browsing with the blob URL or raw fallback URL.
5. Do not treat this index, the PR description, or prior discussion as a substitute for the source contents.
6. The Prompt Atlas and Northstar files are pinned to commit `5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77` so the evaluated text cannot move during the run.

## Prompt Atlas — pinned source

### P1 — SKILL.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/SKILL.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/SKILL.md

### P2 — contract-anatomy.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/contract-anatomy.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/contract-anatomy.md

### P3 — execution-compile.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/execution-compile.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/execution-compile.md

### P4 — execution-graph.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/execution-graph.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/execution-graph.md

### P5 — completion-trust.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/completion-trust.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/prompt-atlas/references/completion-trust.md

## Northstar — pinned source

### N1 — SKILL.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/SKILL.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/SKILL.md

### N2 — contract-anatomy.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/contract-anatomy.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/contract-anatomy.md

### N3 — execution-compile.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/execution-compile.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/execution-compile.md

### N4 — execution-graph.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/execution-graph.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/execution-graph.md

### N5 — completion-trust.md

- Blob: https://github.com/feng-y/skill/blob/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/completion-trust.md
- Raw: https://raw.githubusercontent.com/feng-y/skill/5d109e3dc32c30b400c8d1c349dfa6ecf49bdb77/skills/northstar/references/completion-trust.md

## Leader comparison source

### L1 — SKILL.md

- Blob: https://github.com/KKKKhazix/khazix-skills/blob/main/leader/SKILL.md
- Raw: https://raw.githubusercontent.com/KKKKhazix/khazix-skills/main/leader/SKILL.md

### L2 — anatomy.md

- Blob: https://github.com/KKKKhazix/khazix-skills/blob/main/leader/references/anatomy.md
- Raw: https://raw.githubusercontent.com/KKKKhazix/khazix-skills/main/leader/references/anatomy.md

## Required source-load report

Use this table before the candidate outputs:

| ID | Source | Status | Retrieval method | Evidence |
|---|---|---|---|---|
| P1 | Prompt Atlas SKILL |  |  | first heading or SHA |
| P2 | Prompt Atlas contract anatomy |  |  | first heading or SHA |
| P3 | Prompt Atlas execution compile |  |  | first heading or SHA |
| P4 | Prompt Atlas execution graph |  |  | first heading or SHA |
| P5 | Prompt Atlas completion trust |  |  | first heading or SHA |
| N1 | Northstar SKILL |  |  | first heading or SHA |
| N2 | Northstar contract anatomy |  |  | first heading or SHA |
| N3 | Northstar execution compile |  |  | first heading or SHA |
| N4 | Northstar execution graph |  |  | first heading or SHA |
| N5 | Northstar completion trust |  |  | first heading or SHA |
| L1 | Leader SKILL |  |  | first heading or SHA |
| L2 | Leader anatomy |  |  | first heading or SHA |

If any row is `FAILED`, stop and report only the failed URLs and access limitation. Do not fabricate an evaluation.