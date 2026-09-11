# Primary-Draft change validation

Development/eval evidence only. Not a runtime instruction or a behavioral-uplift claim.

## Current verdict — follow-up to the real-machine retrospective

- The supplied Codex retrospective is real-machine failure evidence **reported by the user**, not a raw independently audited transcript and not an identified run against PR #95.
- The first #95 candidate (`c7e5987`) still had an untested selection/empirical-closure gap. Its D1 already supplied the adopted sharing design; it did not test whether the model completed experiments before selecting the main Draft.
- Targeted runtime corrections and the v2 eval additions have been implemented and self-reviewed. No new Skill, state machine, mandatory prototype stage, or semantic owner was added.
- **26/26 scorer/integrity tests passed** on the updated 11-case inventory; prompt-only export and empty-input `INCONCLUSIVE` checks passed within that suite.
- D10's self-contained experiment fixture was actually smoke-run locally: **24 equality comparisons passed**, with repeated matched CPU timing at **1 / 4 / 16 models**. Source and raw output are retained in the companion review bundle. This is a constructed Python fixture, NOT Hermes code, a model session or production performance evidence.
- Actual clean-session agent runs / independent consumer probes / blinded behavioral judgments executed here: **0 / 0 / 0**. Behavioral uplift remains **INCONCLUSIVE**.
- Merge posture: **HOLD / keep PR draft**. Do not call this incident fixed until real runs show selected-Draft closure, adequate actual experiments and correct ownership. Do not keep expanding runtime rules merely to compensate for the absent runner.

## Scope and evidence attribution

Original base: `acc09e5040b808b46cc8f9aea17bbac988d639ab`.
First candidate: `c7e5987b582ec4e51facdd81ff3352396ff4f3d5`.

Runtime changes remain confined to Northstar and Prototype. AE, Verify, Unknowns First, material-compile, RDR and orchestration are unchanged. The original `score.py`, `results.example.jsonl`, and the new `draft_eval.py` scoring implementation were not changed by this follow-up. Only a hard-coded test inventory count was generalized for appended cases.

The local snapshot comes from the prior published review bundle; both runtime base blobs were verified against the current PR's immutable GitHub content hashes before editing. It is a partial snapshot, not a checkout of the user's development machine. No original Hermes code, raw trace, candidate J implementation or production profile was obtained.

The retrospective reports three distinct conditions: a candidate ledger passed off as the intended change; uncompleted delegated code/performance experiments; and an HTML-only/no-tests Prototype contract. The last differs from the repository's engineering Prototype, which already allowed throwaway code and timing probes. Actual loaded version/overrides are unverified: wrong installation or resolution is plausible, not established. Identity must be checked in real eval traces rather than presumed from a desired revision.

## Review trail

All rounds are implementer self-review, not independent reviewer/model sessions.

### Initial candidate (c7e5987)

Two plan rounds narrowed ownership and granularity: one primary Draft per Intent, not per file/session; direct AE/Verify callers need no synthetic Northstar artifact; facts must not be invented to complete a Draft. Two implementation rounds aligned activation/stopping and corrected scorer false-green risks (over-trigger, blocked readiness, repeat settings and unclean records). Historical result: 26 scorer tests passed, no agent runs. The original report is preserved at c7e5987.

### Follow-up plan review — what the retrospective changes

The earlier statement that only measurement remained is superseded. D1 was a preselected-design integration control. The revised plan adds selection from Evidence, an actual disposable experiment and an unavailable-backend counterexample. Existing D1–D8 are preserved rather than rewritten to look like an original failure reproduction.

### Follow-up counterreview — reject excessive fixes

Rejected three new prototype Skills, a mandatory Reaction → Feasibility → Performance chain, and a new readiness state schema. The discriminator is what observation the current decision requires. Prototype provides a disposable artifact/observation; Verify retains proof strength; Northstar adopts/rejects/revises into the same primary Draft. Explicit current experiments cannot be silently deferred, but genuine blockers and research-only scope still permit an honestly partial handoff.

### Follow-up implementation review

Distinguished prioritizing a candidate from adopting it, and Draft implementability from completing the user's current assignment. Kept one primary Draft compatible with multiple connected changes. Revised Prototype's "no complete tests" language so necessary equality/behavior checks and matched measurements are not excluded. Removed the residual stopping loophole that could classify selection-changing empirical work as later verification mechanics. No concrete Hermes lifecycle or optimization answer was put into runtime instructions.

## Executed checks

```bash
python3 -m unittest discover -s evals/northstar-paired -p 'test_draft_eval.py' -v
```

The 26 tests exercise the scorer, identity/line-span validation, paired settings, prompt export, missing/unknown evidence and recorded negative conditions. They are synthetic observations, not model behavior tests. Test output is retained in `followup-tests.log` in the companion bundle.

Additional checks: D1–D8 manifest entries identical to v1; D9–D11 append-only in v2; runtime YAML frontmatter/name checks; no runtime-to-eval reference; unchanged scorer/example bytes; UTF-8 and whitespace checks. The fixture smoke preserves source/hash, input hash/size, equality outcomes, and raw timing samples; no timing number is interpreted as a Skill improvement.

## Unexecuted behavioral work

The new targeted smoke is D9–D11 × 2 arms = 6 actual actor sessions, plus consumer probes for D9/D11. The full repeated v2 set is 11 × 2 × 3 = 66 actual actor sessions plus applicable consumer probes. Neither has been launched here. The current environment lacks a callable independent agent runner. The original real-task/repeat requirements still apply to broad uplift claims; repeating constructed cases does not make them real corpus.

Before a behavioral conclusion, verify actual loaded Skill identity and inspect real trace/result/probe evidence. A finished HTML or a self-reported benchmark is not a substitute. No fixed speedup or mandatory positive optimization result is required: a correctly supported rejection can be the right outcome.

## Skill Doctor correction retained

Commit `c13842d53c718ad0a3b068b0e1ed96ed7f147a10` on 2026-09-09 explicitly removed Skill Doctor (`cleanup: remove unused skill-doctor files`), before #93. It is not restored by this change, and no Skill Doctor score is fabricated.
