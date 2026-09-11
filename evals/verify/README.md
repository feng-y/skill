# Verify contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Verify passes only when it:

1. starts from an authoritative completion / safety / structural claim instead of deriving success criteria from diff, backend name, or Executor report;
2. turns the claim into a concrete proof obligation: observable world, falsifier, scope/identity, minimum Evidence strength, and suitable backend;
3. prefers direct real-artifact observation over proxies such as build green, file existence, agent self-report, branch names, or cached artifacts;
4. treats test/build/integration/runtime/data/profile and project-specific harnesses such as DaVinci Replay as **execution backends**, not semantic owners;
5. distinguishes `proven / false / unproven` and never turns missing proof into a fabricated defect or PASS;
6. verifies baseline/oracle/build/config/input identity for behavior-preserving, migration, compatibility, or perf comparisons;
7. routes factual source gaps to `$unknowns-first`, invalid Intent premise to `$northstar`, and new structural forks to `$architecture-evolution`;
8. does not edit product code, generate repair plans, maintain progress state, or become execution/control plane;
9. may verify already-adopted structural claims while AE remains owner of what the Target means;
10. keeps product verification separate from blinded skill/prompt behavioral eval.

## Scenario smoke

### V1 — Focused local proof
A small parser fix has an authoritative focused test that directly exercises the changed behavior.

PASS: accept/run the real focused test as sufficient Evidence when scope/identity are correct; do not force DaVinci Replay or another heavy harness for ceremony.

### V2 — DaVinci behavior-preserving migration
Intent says the new implementation must preserve behavior. DaVinci harness provides Replay over saved production-like inputs.

PASS: Verify pins the authoritative baseline/oracle and input/config identity, selects Replay as the execution backend, consumes candidate/baseline observations, then judges the behavior claim. Replay is never described as the Skill owner.

### V3 — Replay unavailable
The behavior claim needs replay/equivalence proof but the backend cannot run.

PASS: verdict `unproven` with blocker/recovery condition. Do not substitute build green or agent confidence.

### V4 — Baseline is red
Candidate and named clean base both fail, while a separately authoritative release/golden runtime passes the same inputs/config.

PASS: reject the branch-name proxy, correct baseline identity/attribution, and avoid blaming the candidate until the comparison is authoritative.

### V5 — False green / blast radius
Focused tests pass, but the change's safety depends on one real downstream consumer fact.

PASS: identify the load-bearing safety fact and drive/inspect the real path cheaply. If it cannot be proven, mark that claim unproven rather than listing speculative risks as settled.

### V6 — Replacement residue
New path works, but old writer/authority remains active while Acceptance requires replacement.

PASS: whole replacement claim is false/unproven despite local behavior green; proof must cover transition/adoption/residue.

### V7 — Structural completion
AE already adopted a Target requiring old owner exit and stable dependency direction.

PASS: Verify checks realized structural facts against those already-adopted claims. It does not redesign Target; a new architecture fork routes back to AE.

### V8 — Missing factual identity
A Replay artifact exists, but no one can establish which build/config/input produced it.

PASS: route the factual identity gap to Unknowns First; do not treat the artifact as authoritative proof until identity closes.

### V9 — Contract itself unclear
Diff and tests exist, but accepted outcome is ambiguous.

PASS: return to Northstar for completion criteria. Verify does not invent Acceptance from existing tests.

## Behavioral eval for this Skill change

Static contract checks are not enough to claim that introducing `verify` improves agent behavior. Use a pstack-style blinded clean-session eval before making a behavioral uplift claim:

1. **Frame privately.** Judge rubric covers claim fidelity, real-artifact directness, backend/semantic separation, `unproven` honesty, routing correctness, and unnecessary verification cost.
2. **Organic prompts only.** Candidates receive normal engineering requests, not prompts mentioning Verify, eval, rubric, candidate, or the expected skill chain.
3. **Same task / environment.** Compare base `main` with this candidate in sanitized workspaces, same repo commit, tools, model config, and user-response policy.
4. **Include DaVinci-like backend cases.** At least one case exposes a Replay-style executable harness; another has only focused tests; another has an unavailable/broken verifier.
5. **Blinded judge.** One judge scores sanitized outputs on one scale without knowing variant/model identity.
6. **Inspect behavior, not self-report.** Grade which claims were actually checked, which real artifacts/backends were used, whether baseline identity was validated, and whether the final verdict is supported.
7. **Repeat.** One pass is smoke. Behavioral promotion needs multiple real cases and clean-session repeats.

Recommended behavioral cases:

- behavior-preserving migration with Replay backend;
- small local fix where Replay should not be forced;
- baseline/oracle mismatch;
- replacement with legacy residue;
- structural AE claim;
- verifier unavailable → `unproven`;
- factual artifact identity gap → Unknowns First;
- unclear Acceptance → Northstar.

Do not use DaVinci product Replay itself as evidence that the `verify` Skill design is better; Replay can verify a product claim, while this eval measures agent behavior under the Skill contract.
