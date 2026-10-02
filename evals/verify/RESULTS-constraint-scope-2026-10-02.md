# Binding constraints in verification scope

Base: `0949e15495ca0c97ba5907a6a27f75e7c932bae2` (merged PR #122).
This is focused behavioral evidence for a one-sentence Verify clarification, not a new evaluation platform.

## Finding and source repair

The historical Northstar L07 case retained in
[`loading-outcomes-2026-10-01.json.gz`](../northstar/loading-outcomes-2026-10-01.json.gz)
contains a real acceptance failure. Its Taskbook explicitly excludes non-string
input changes, and its contract requests no other behavior change. The initial
implementation changes a missing bytes lookup from `KeyError` to `None`. The
caller notices that delta but treats non-string semantics being “outside this
contract” as permission to waive it, then declares H1 complete.

The constraint did not disappear from the file. The acceptance judgment treated
the four enumerated positive outcomes as exhaustive and reinterpreted an explicit
behavior-change exclusion as absence of a compatibility commitment. The original
archive does not export the implementation/verifier authored handoffs or complete
returns, so it cannot attribute that historical failure to a particular Verify
invocation. Its subsequent repair is reviewer-driven recovery, not an initially
successful unassisted run.

Current-base frozen-return probes below reproduced this scope-waiver behavior in
two fresh, explicitly selected Verify actors. The existing invariant already
belongs to Verify; the repair replaces its vague Claim-first lead with a precise
scope discriminator:

> 先读取 authoritative contract，由适用的 Acceptance 与 binding Constraint / Decision 共同限定当前 claim；局部验收范围不能豁免已约定不改变的行为，未承诺的行为也不自动成为新 claim：

This replaces one sentence. It adds no section, checklist, field, owner, workflow,
backend, or rule specific to bytes/non-string inputs. Legitimate subclaim proof
remains possible: a local `proven` verdict must not erase a known binding
contradiction or become whole-task completion. Uncommitted behavior is not
silently upgraded into a preservation requirement. All other runtime sources
remain unchanged.

## Measurement

The experiment isolates **current return/claim judgment**, not the original full
implementation loop. Fresh native actors receive isolated snapshots and selected
current Skill sources. The task asks for assessment only, without implementation
or dispatch. Two original-scope repeats, an explicitly authorized-change control,
and corrected/uncommitted guards were fixed before candidate execution.

The returned report is reconstructed from the historical caller's retained
Decisive Evidence, including its incorrect scope waiver. It is supplied as a
claimed implementation return, not authoritative scope. Original worker messages
are unavailable; the reconstruction is not presented as an original transcript.
No actor-visible prompt contains a failure label, condition identity, recovery
feedback, expected verdict, or rubric. The two configurations use the same
organic task text apart from fixture/source paths, same available source set,
same tools/permissions and xhigh reasoning setting. They have no separately
imposed token/time quota; costs were not measured.

For the original and authorized conditions, candidate/base work inputs are
byte-identical. In the authorized control, only authoritative Taskbook/contract
scope changes: it explicitly permits the absent non-string-key delta. The
corrected guard retains the original contract with reviewed corrected code,
checks and returned report. It is a positive acceptance guard, not a
single-variable causal comparison. The uncommitted guard removes all residual
non-string preservation promises from authoritative scope and explicitly states
that there is no compatibility commitment for those inputs.

### Observations

| Selected Skill/configuration | Case IDs | Observed judgment | Interpretation |
| --- | --- | --- | --- |
| Unchanged Northstar, original contract / original code | amber | Reject H1; retain proven string outcomes | Correct caller judgment on this frozen return |
| Unchanged Northstar, explicitly authorized change | birch | Accept | Correct authority discrimination |
| Unchanged Northstar, corrected code / original contract | cedar | Accept | Correct positive acceptance guard |
| Base Verify, original contract / original code | dune, elm | Both say H1 proven with no remaining proof gap; waive known non-string delta | Two retained false passes |
| Base Verify, explicitly authorized change | fir | Proven | Correct authorized-change control |
| Candidate Verify, original contract / original code | glen, kelp | Both say whole H1 false; retain proven positive subclaims | Known binding contradiction no longer waived in these runs |
| Candidate Verify, explicitly authorized change | hazel | Proven | Does not reject an authorized delta |
| Candidate Verify, corrected code / original contract | iris | Proven | Does not reject restored compatibility |
| Candidate Verify, genuinely uncommitted behavior | jade | Proven for string-only contract | Does not invent preservation of unspecified behavior |

All 11 fresh actors completed. The three unchanged Northstar runs are diagnostic
controls, not candidate Verify trials. The direct Verify comparison comprises
three base runs and five candidate runs. Dune independently characterized the
bytes counterexample; Elm acknowledges the reported delta and waives it, but its
exported result does not establish that it independently executed that bytes
probe. Both nevertheless give the erroneous whole-H1 conclusion. Candidate
Glen/Kelp preserve the distinction between proven positive subclaims and a false
whole completion claim.

## Independent checks and limits

- Directly reconstructed original, initial and corrected source from the retained
  L07 archive. On the same 30 non-string input/environment comparisons, initial
  code differs from baseline 12 times and corrected code differs 0 times. Both
  satisfy the four requested string outcomes. These are product-code observations,
  not 30 agent behavior trials.
- Before/after hashes show that Verify actors added only `answer.md`; Northstar
  actors changed only their canonical Taskbook and added `answer.md`. No Skill,
  contract, code, check, baseline or supplied return was modified. Final snapshots
  cannot exclude a transient edit/revert.
- Independent review audited task/source identity, the genuine-uncommitted guard,
  authority changes, verdict interpretation and immutable inputs. Review does not
  convert a reported command into a complete tool-trajectory audit.
- Existing instrument regressions: 51 tests passed (27 controller-worker, 11
  behavioral-loop scorer, 13 Northstar/Beacon scorer). These validate the
  instrument only; neither those tests nor actors' counts of local Python probes
  are evidence of improved agent reliability.
- `git diff --check` and archive content/hash validation passed. No source
  migration or new runtime responsibility is introduced, so no breaking-semantic
  migration entry is needed.

The observed base false passes and corrected candidate judgments support this
narrow semantic clarification. They do not establish general behavioral uplift,
a production failure rate, automatic Skill routing, original handoff fidelity,
full-loop autonomous acceptance, or cost/latency improvement. Corrected and
uncommitted controls have candidate smoke observations, not paired base/candidate
estimates. No additional runtime rule is inferred from the historical case alone.

## Reproduction and retained evidence

[`constraint-scope-outcomes-2026-10-02.json.gz`](constraint-scope-outcomes-2026-10-02.json.gz)
retains the source case, exact task clauses, per-case initial/final content and
hashes, native actor identities, selected source snapshots (deduplicated by
SHA-256), comparison oracle,
adjudications, direct reproduction code/results, and instrument output. The
identical non-task reporting/authorization suffix and inherited host instructions
are not exported. Native actors inherit the host model; the exact model identifier
was not exposed by this backend, and complete native tool transcripts were not
available. Do not infer observed Skill reads merely from the selected prompt.

To repeat, materialize a case's `initial_files` into a fresh isolated directory
(resolving Skill content from `source_contents_by_sha256` by its recorded hash),
remap only its absolute paths in the retained prompt, use its pinned Skill source,
and assess the final verdict against the stated authority discriminator. Preserve
all failed attempts. The recorded Python reproduction source only checks the
archived product artifacts; it is not an agent runner or scorer.

Pinned Verify source SHA-256:

- Base: `dc6943040c91b4f3c5863f91dbb733f866a5267bcdea7bbc41a746ebaef494d3`
- Candidate: `e6cbd1cdeefda6d5feef89c1fabd0d8e10aff1314b262bd4faac355d3b6036a8`
