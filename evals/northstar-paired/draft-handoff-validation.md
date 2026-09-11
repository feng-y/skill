# Primary-Draft change validation

Development/eval evidence only. This is implementer self-review, not an independent model review.

## Current continuation verdict

Continuation base: `e76021a1c265a3580fbcd30c95e91f231de70eef`; original PR base: `acc09e5040b808b46cc8f9aea17bbac988d639ab`.

**Known contract contradictions corrected; HOLD for behavior-validated merge.** Actual clean-session actor / consumer / blinded-judge runs performed in this continuation: **0 / 0 / 0**. The user's real-machine retrospective remains useful failure evidence, not an identified paired run against this revision.

## Findings and repairs

1. **Invocation entry contradicted runtime.** `skills/prototype/agents/openai.yaml` still demanded one isolated decision and broadly excluded implementation. Align Prototype frontmatter/body/default prompt and README with cohesive shaping or explicitly delegated disposable execution. Align Northstar's entry with the one-primary-Draft integration responsibility.
2. **Explicit experiments could hit a premature bypass.** The body still said to stop when no shape gap remained, even though later paragraphs required explicitly commissioned experiments. Known shape now cancels only unnecessary shaping, not the experiment assignment. A Verify caller retains proof ownership without receiving its unfinished artifact assignment back.
3. **The comparison cap could silently reduce scope.** Remove the fixed two-to-three-candidate rule. Compare only decision-relevant candidates; preserve explicitly delegated work and report genuinely unfinished items instead of dropping them.
4. **Empirical uncertainty could masquerade as a setup blocker or cause an endless loop.** Distinguish unknown current source/config identity from the quantity the experiment is intended to measure. Return an inconclusive completed experiment to the caller instead of forcing a win or inventing unbounded follow-up work.
5. **Consumer probes could be given missing semantics.** Clarify that the independent consumer gets the handoff and target/territory snapshot, not the original request or specialist conversation. The judge retains the original request to detect omissions. Supplying it to the consumer would hide an incomplete Draft.

No new Skill, readiness schema, permanent execution manager or prototype category is introduced. AE, Verify and Unknowns First runtime contracts remain unchanged. This does not repair the user's machine installation or establish the cause of the reported HTML-only Skill resolution.

## Review rounds

**Round 1 — entry/body consistency:** inspect the Prototype descriptor, default invocation prompt, positive routes, bypasses and stopping conditions together. Replace contradictory clauses rather than append another exception layer. Retain cheap static shaping where sufficient, disposable rather than production implementation, and original-caller ownership.

**Round 2 — counterexamples and evidence:** challenge explicit runnable work with an already-known shape; How-only local change; Verify-delegated trial; unknown setup facts; inconclusive observations; and a delegated candidate set larger than a display cap. Verify that one primary Draft can still contain multiple related changes. Review the consumer-probe input boundary separately from the candidate prompt.

Disposition: no additional blocking runtime contradiction found in this bounded review. It is not proof of agent improvement.

## Executed checks

```bash
python3 -m unittest discover -s evals/northstar-paired -p 'test_draft_eval.py' -v
git diff --check
```

**26/26 existing scorer/integrity tests passed** in this continuation. The same suite exported all 11 organic prompts and kept empty observations `INCONCLUSIVE`. These synthetic tests validate the scoring/packaging path, not Skill behavior. No new prose-matching unit tests or extra case inventory were added just to increase a test count.

Packaging checks cover UTF-8/whitespace, YAML frontmatter and invocation metadata, unchanged Skill names, absence of runtime references to private eval files, and unchanged scorer/case/example bytes. Source files were recovered from the earlier published bundle and connector reads; original Git-blob identities were checked before editing. This is a partial local snapshot, not a clone or remote execution environment. Test output and the incremental patch are retained in the companion bundle.

## What remains unproven

The frozen 11-case manifest, `draft_eval.py`, original `score.py`, example and scorer tests are unchanged. Use the existing D10 / D4 / D6 / D11 cases as a focused check of explicit execution, bypass, owner return and honest blocking. Inspect actual loaded instructions, including invocation metadata, and keep the entry mode equal within each pair. No fresh model sessions were available or launched here; no routing, owner-transfer, performance or efficiency uplift is claimed.

Earlier D10 local Python measurements are historical fixture evidence at `e76021a`, not rerun results from this continuation and not Hermes production evidence. Earlier review and experiment records remain in the preceding commits and published bundles. Do not replace clean-session evidence with another synthetic benchmark.

Skill Doctor was explicitly removed by `c13842d` before #93; it is not restored by this PR, and no Skill Doctor grades were fabricated.
