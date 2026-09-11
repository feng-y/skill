# Primary-Draft change validation — 2026-09-11

Development/eval evidence only. Not a runtime instruction or a behavioral-uplift claim.

## Verdict

- Runtime/contract review: no remaining blocking issue found in the reviewed patch.
- Local executable checks: **26/26 scorer/integrity tests passed**, CLI export/empty-input checks passed, existing paired-scorer example smoke passed, changed frontmatter/whitespace checks passed.
- Actual clean-session candidate runs: **0**. Actual blinded consumer probes: **0**. Measured routing/Draft/owner/over-trigger uplift: **INCONCLUSIVE**.
- Merge recommendation for the requested behavior-validated completion: **HOLD / keep PR draft until real paired evidence is available**. The implemented semantic correction is reviewable; synthetic scorer fixtures do not discharge the behavioral gate.

## Scope and provenance

Base: `acc09e5040b808b46cc8f9aea17bbac988d639ab`.

Changed runtime: Northstar and Prototype only. AE, Verify, Unknowns First, material-compile, RDR and orchestration remain unchanged. No new Skill/semantic owner. Existing `score.py` and `results.example.jsonl` are byte-identical to base.

The local workspace is a connector-sourced partial snapshot, not a successful git clone. Original blobs used for modifications and the existing scorer were verified against GitHub Git-blob SHA values before editing/running. No original Hermes execution trace or production source was obtained. User-reported failure plus the user's explicit one-primary-Draft authority justified the targeted contract correction; transcript-level causal attribution remains unverified.

## Review trail

All rounds below are self-review by the implementing assistant. No independent model/reviewer session is claimed.

### Plan round 1 — owner boundary

Rejected the overly broad formulation that all specialists must refine an Intent Draft. Independent AE/Verify callers keep their own authority and need no Northstar artifact. Distinguished one semantic authority per Intent from one physical file or one global Draft. Did not adopt prior illustrative Hermes request-scope/immutability choices as production facts.

### Plan round 2 — depth without ceremony

Checked coupled sharing, already-concrete local work, missing facts, adopted correction, direct architecture/verification and independent-Intent counterexamples. Kept completeness relative to material intended change, not exhaustive implementation design. Approved the narrowed two-runtime-file plan before implementation.

### Implementation round 1 — consistent activation and stopping

Found that replacing the atomic-decision heading alone left the description/activation phrased only as competing interpretations. Updated the description and entry discriminator to a material concrete-shape gap, without requiring manufactured alternatives. Replaced residual atomic wording in the disposable-prototype paragraph. Preserved fact/architecture/proof owner boundaries.

Split an executable implementation handoff from a truthful blocked Draft: exposing a blocker is not proof that the blocked implementation can proceed. Updated the owner-focused eval contracts to match the cohesive-surface rule.

### Implementation round 2 — scorer false-positive review

Initial 22-test suite passed. Additional review identified measurement risks and corrected them:

- a forbidden Prototype call could hide behind a green human-entered grade;
- a blocked handoff could be labelled executable;
- paired settings could change between repeats;
- unclean/mixed real records should remain inconclusive, not be mislabeled as synthetic success;
- case-specific handoff expectations belong in the private case manifest, not in the scorer logic.

Added focused tests for these changes. Final suite: 26 tests passed. No later scoring/runtime edits were made before packaging.

## Executed checks

```bash
cd evals/northstar-paired
python3 -m unittest -v test_draft_eval.py
python3 score.py results.example.jsonl
```

The tests include prompt-only export, stale-output-directory rejection, empty-run inconclusive exit, fake/missing artifact and forged-line rejection, pair/configuration/session-isolation checks, unknown-grade handling, and negative grading fixtures for missing Draft, fragments, competing authority, caller takeover, over-trigger and premature executable handoff.

These tests feed **synthetic graded observations** to the scorer. They prove that the scorer rejects those recorded conditions; they do not prove that an actual model follows the Skills or that the original Hermes failure is reproduced/fixed.

The existing scorer's example remains schema smoke only. It returns sample-insufficient `INCONCLUSIVE` for behavioral interpretation. Its illustrative latency/token changes are not measurements from this work.

Additional packaging checks: modified Skill YAML frontmatter parsed; Skill names retained; runtime contains no new eval/rubric references; UTF-8 text, whitespace and Markdown fences checked. Four modified-file `git diff --no-index --check` checks produced no diagnostics. The initial shell wrapper treated the expected no-index difference exit code 1 as a command failure; rerun with a noninteractive Git environment confirmed no whitespace errors.

## Unexecuted behavioral work

The frozen focused set contains 8 reconstructed/constructed cases, requiring 48 actual base/candidate sessions for three repeats plus fresh consumer probes for Intent cases. These runs were **not launched**. No agent runtime is callable in this environment: Codex/Claude executables and model API credentials are absent; the connector-directory check found no connected execution service. This is an execution-access limitation, not a measured model failure.

Do not infer improved routing, owner retention, primary-Draft completion, Prototype precision, token use, latency or Hermes CPU behavior from this report. The next actual evaluation must use the frozen inputs, current base and pinned candidate with a blinded judge. Broader uplift still requires real task cases under the existing paired-eval contract.

## Skill Doctor correction

Repository history records `c13842d53c718ad0a3b068b0e1ed96ed7f147a10`, 2026-09-09, `cleanup: remove unused skill-doctor files`. The earlier conversational attribution to accidental removal by #93 was wrong. This patch does not restore the removed Skill or fabricate a Skill Doctor score.
