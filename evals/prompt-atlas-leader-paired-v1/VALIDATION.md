# Prompt Atlas × Leader paired EVA v1 — fixture validation

## Status

**FIXTURE INFRASTRUCTURE: PASS**

**REFERENCE-SOLUTION FEASIBILITY: PASS**

**PROMPT ATLAS × LEADER BEHAVIORAL ARMS: NOT RUN**

Validation date: `2026-07-31`

## Environment

- GNU Bash `5.2.37`
- Python `3.13.5`
- pytest `9.0.2`
- Git `2.47.3`
- ripgrep `14.1.1`
- Linux x86_64, kernel `6.12.13`

This environment is evidence for fixture validation only. The final paired run must separately freeze its own environment image and tool versions.

## Infrastructure validation

The four repository generators and their registered public commands were executed in fresh temporary directories.

| Fixture | Generator | Registered initial behavior | Worktree after checks |
| --- | --- | --- | --- |
| F1 false-green | PASS | `check.sh` exits 0; visible pytest passes | clean |
| F2 parser migration | PASS | visible batch pytest passes; legacy references remain | clean |
| F3 branch blocker | PASS | discount percentage test fails; private verifier absent | clean |
| F4 cross-context | PASS | visible batch/export pytest passes; legacy references remain | clean |

All four registered oracle-manifest SHA-256 values were recomputed from the manifest text and matched.

Python bytecode and pytest cache noise was removed by:

- adding only `__pycache__/`, `.pytest_cache/`, and `*.py[cod]` to each generated repository's `.gitignore`;
- running public pytest commands with `PYTHONDONTWRITEBYTECODE=1` and `-p no:cacheprovider`.

`.scratch` is intentionally not ignored so F4 can still detect continuity state that is accidentally committed or hidden.

The repository includes `validate-fixtures.py` to repeat the generator, manifest, public-command, and cleanliness checks before either paired arm starts.

## Corrections found during validation

### Runtime-noise contamination

Initial pytest execution could create `__pycache__` and `.pytest_cache`, polluting worktree-state and unrelated-change judgments. The generators and public commands now prevent that noise.

### Discount boundary ambiguity

The original F1/F3 wording overlapped at numeric value `1`:

- `0..1` as fraction;
- `1..100` as percentage.

The fixture is now explicit:

- `0 <= value <= 1` remains a fraction;
- `1 < value <= 100` is divided by 100;
- numeric `1` therefore normalizes to `1.0`, not `0.01`.

F1 and F3 manifests were versioned to v2 and rehashed.

## Reference-solution feasibility

Independent reference implementations were applied in temporary generated repositories to verify that the fixtures and judged properties do not conflict.

| Fixture | Reference result |
| --- | --- |
| F1 | complete PASS; valid/invalid boundaries and public API verified; `1 -> 1.0` |
| F2 | complete PASS; batch behavior preserved, streaming default/trace behavior preserved, all consumers migrated, legacy module removed |
| F3 | Branch A PASS; Branch B remains genuinely unavailable; truthful final BLOCK is feasible without changing tax source |
| F4 | complete PASS across a simulated clean-context restart; continuity state preserved; no legacy reference remains; `.scratch` is not committed |

This validation proves fixture satisfiability and expected terminal feasibility. It does not measure either skill's behavior.

## Claim boundary

This file does **not** establish:

- clean-session Prompt Atlas compiler output;
- clean-session Leader taskbook output;
- executor behavior for either arm;
- private-oracle results for either arm;
- behavioral parity or superiority.

Those claims remain gated by the isolated paired protocol in `PLAN.md`.
