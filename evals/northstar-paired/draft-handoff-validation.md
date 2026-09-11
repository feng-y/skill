# Primary core Prototype / Human interaction correction

Continuation base: `67b1f9dcf07e7cbfd7128c5076c410712313ca17`. Implementer self-review only; no independent model reviewer is claimed.

## Decision and scope

The user corrected the design: an Intent has one main, core Prototype, and Northstar must ask the Human for needed clarification and confirmation. The prior invariant covered a primary Draft but still allowed per-call surfaces/experiments to become the practical output. That framing is superseded, not merely supplemented with more experiments.

One intended change now has a corresponding primary Draft and one inspectable core Prototype. Local views, comparisons and measurements support that same whole, not separate Prototypes per optimization or specialist. Northstar actively presents its best-known interpretation, asks material questions, incorporates Human correction into the same core and records the corresponding meaning. This does not require two files, new approval stages or repeated questions about already confirmed/delegated choices.

Runtime edits remain in Northstar, Prototype and their invocation metadata. README, semantic migration history, plan and focused eval guidance are aligned. AE / Verify / Unknowns First runtime contracts and the 11 frozen cases/scorer/test code are unchanged. Independent AE/Verify or experimental requests do not acquire a synthetic Intent.

## Review rounds

1. Authority and main object: checked that one core Prototype means an actual connected intended path, not a renamed index of local artifacts. Multiple files/views/iterations do not become multiple semantic main objects; distinct Intents remain independent. Draft and Prototype must not become competing intended-change authorities.
2. Human interaction and counterexamples: needed clarification can precede complete technical investigation; confirmation may be based on an inspectable best-known core. Feasibility/performance observations cannot decide Human expectations. Existing responses and delegated decisions avoid repeated approval. The descriptor and return contract were checked and adjusted to preserve standalone callers without creating an Intent first.

No additional unresolved contradiction was identified in this bounded static review. This is not a measured behavioral improvement.

## Executed checks

`python3 -m unittest discover -s evals/northstar-paired -p 'test_draft_eval.py' -v` ran once: **26/26 passed**. Those are existing synthetic scorer/integrity tests; export still contains 11 prompts and empty observations remain INCONCLUSIVE. No new prose-matching tests or performance benchmark was added.

YAML/frontmatter, invocation metadata, UTF-8/whitespace, new relative links, unchanged frozen cases/scorer/tests, and patch hygiene were checked. The partial local snapshot came from the prior published bundle and connector content; source Git-blob identities were checked before edits. The recovered changelog initially differed by one word and was corrected to match the original blob before adding the migration entry. Logs and the incremental patch are retained in the review bundle.

## Behavioral evidence still missing

Actual clean-session actor / consumer / blinded-judge runs here: **0 / 0 / 0**. The staged H1 interaction and H0 already-confirmed countercheck are specified in `core-prototype-human-eval.md` but were not executed. They require observing the question, withholding the Human answer until its proper turn, and examining the integrated core after the reply. The existing scorer does not directly measure required-question omission or primary-Prototype cardinality; a green scorer result must not certify those behaviors.

The prior real-machine retrospective is user-reported failure evidence, not a version-identified paired run. Actual installed Skill resolution and Hermes performance remain unverified. No change was made to the user's machine or product code.

Merge posture: **HOLD / keep PR draft** for behavior-validated acceptance. The current patch implements the corrected semantic authority; it does not prove the agent has followed it in a real session.
