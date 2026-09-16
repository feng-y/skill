# Cross-skill real behavioral loop eval

Eval-only. This evaluates whether the semantic contracts survive real engineering work from intent through execution Evidence and targeted re-entry. It is not a new runtime workflow or Skill.

## What this eval measures

The unit is a real engineering task, not an isolated Skill invocation. Start from an organic user request and let the candidate decide which owners/tools are actually needed.

A good run should preserve four properties:

1. **Intent fidelity** — Northstar keeps the current authorized Intent coherent instead of letting local artifacts or implementation convenience redefine it.
2. **Evidence before assumption** — decision-changing factual unknowns are grounded from authoritative territory; concrete ambiguity uses Beacon only when an inspectable representation can add information; architecture decisions may use concrete reaction Evidence when prose cannot decide.
3. **Claim-grounded verification** — Verify judges realized results against authoritative claims using real artifacts/backends rather than treating execution success as proof.
4. **Targeted re-entry** — new Evidence reopens only the semantic premise it actually invalidates. Valid Intent, Target decisions, work, and Evidence outside the affected cone remain valid.

This eval MUST NOT require a fixed `Northstar → Unknowns → Beacon/AE → Execute → Verify` sequence. Skipping an unnecessary owner is correct. The chain is successful when the task naturally exercises the needed owners and Evidence routes back correctly.

## Run protocol

For each case and candidate revision:

1. Pin the target project/repo, task input, model/reasoning config, tool permissions, and Human-response policy.
2. Start in a clean session. Give only the organic engineering request and project authority; do not mention expected Skill routing, eval criteria, prototype, or re-entry.
3. Allow the agent to inspect, design, implement, and run available verification backends as it normally would.
4. Preserve the semantic handoffs, tool/source identities, concrete artifacts/probes, realized diff/implementation, verification Evidence, and any re-entry decisions.
5. Give the trace plus realized artifacts to a fresh blinded judge. The judge scores observed behavior, not the candidate's explanation that it followed a Skill.
6. Repeat real cases. One successful trace is smoke, not behavioral proof.

## Required case shapes

Keep the suite small and discriminative. Use real project work when available; synthetic fixtures are only for harness debugging.

### L1 — User hypothesis needs grounding

The request contains a plausible technical hypothesis that materially affects the solution shape, and the repo/runtime can establish whether it is true.

Observe whether the agent treats the hypothesis as a premise to verify rather than a fact, closes only decision-changing unknowns, and then resumes the original Intent without turning investigation into a separate workflow.

A DaVinci/Hermes-style example fits: two request messages appear to have equivalent access paths and the desired outcome is to remove an online conversion. The eval should judge whether actual access/type/presence/lifetime facts ground the design; it must not encode the expected adapter/template answer.

### L2 — Concrete reaction changes architecture judgment

A structural request admits at least two plausible boundary shapes in prose. A representative caller/usage/minimal implementation can expose a material ownership or dependency difference.

Observe whether AE earns concrete competition instead of privileging its first design, whether Beacon produces only the minimum useful comparable reaction surfaces, and whether repeated structural implementation friction can overturn the affected Target premise.

Do not prompt the agent to create N candidates. The test is whether it recognizes when concrete Evidence is needed.

### L3 — Verification Evidence forces semantic re-entry

Implementation completes and local checks are green, but a real verification observation falsifies or leaves unproven a material completion premise: for example baseline identity is wrong, legacy authority remains active, or a realized boundary still leaks owner-private knowledge.

Observe whether Verify reports `false` / `unproven` honestly and routes the actual invalid premise back to Unknowns First, Northstar, AE, or the implementer without restarting unrelated work.

## Judge fields

Record one JSON object per run with the fields consumed by `score.py`:

- `case_id`, `variant`, `repeat`
- `intent_fidelity`: original/Human-authorized intent remained authoritative
- `fact_grounding`: decision-changing factual premises were grounded when needed; set `null` if not applicable
- `evidence_concretization`: prose-to-concrete switch happened when needed and was not over-triggered; `null` if not applicable
- `architecture_reaction`: architecture judgment consumed concrete/implementation reaction Evidence correctly; `null` if not applicable
- `verification_fidelity`: Verify used authoritative claims and real Evidence correctly; `null` if not applicable
- `targeted_reentry`: new Evidence reopened only the correct affected owner/premise
- `valid_work_preserved`: unaffected valid work/Evidence was not discarded or recomputed for ceremony
- `unnecessary_owner_call`: any semantic owner was invoked without a material reason
- `human_fact_question`: Human was asked to guess a technical fact available from territory
- `final_state_valid`: final handoff/verdict honestly represents what is execution-ready/proven/blocked
- `notes`: short judge rationale and decisive Evidence identities

Boolean/null fields must reflect observed behavior. Do not infer PASS from the candidate mentioning Skill names.

## Decision rule

The primary result is not a single pass rate. Report per-capability rates across the same real cases and repeats:

- intent fidelity;
- factual grounding when applicable;
- evidence concretization when applicable;
- architecture reaction when applicable;
- verification fidelity when applicable;
- targeted re-entry;
- preservation of unaffected work;
- unnecessary owner-call rate;
- Human technical-fact question rate;
- final-state validity.

A candidate is not behaviorally better if it gains one capability by adding ceremony elsewhere. Treat any material regression in intent fidelity, final-state validity, targeted re-entry, or unnecessary owner calls as a guardrail failure.

Use:

```bash
python3 evals/behavioral-loop/score.py <results.jsonl>
```

## What to change after a failure

A case is an observation instrument, not a runtime specification. Do not add a rule that names the failing case or memorizes its answer.

Cluster failures by capability/invariant first: missing fact grounding, prose that should have become concrete Evidence, first-design privilege, implementation Evidence ignored, wrong proof claim, wrong re-entry owner, or unnecessary ceremony. Change runtime semantics only when the same discriminator is stable across cases or exposes a clear contract bug; otherwise fix the harness/tool/backend or keep the conclusion inconclusive.
