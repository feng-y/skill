# Verify contract eval

Eval-only. Normal runtime must not read this file.

## Static invariants

Verify passes only when it:

1. starts from an authoritative completion / safety / structural claim instead of deriving success criteria from diff, backend name, or Executor report;
2. can be invoked before, during, or after implementation without becoming a mandatory post-PR stage;
3. turns the claim into a concrete proof obligation: observable world, falsifier, scope/identity, minimum Evidence strength, and suitable backend;
4. may model-invoke `$beacon` when an accepted claim needs a bounded behavior/fault expressed as a repo-grounded core prototype; Verify retains proof ownership and does not turn ordinary backend execution into a Beacon stage;
5. prefers direct real-artifact observation over proxies such as build green, file existence, agent self-report, branch names, or cached artifacts;
6. treats test/build/integration/runtime/data/profile and project-specific harnesses such as DaVinci Replay as **execution backends**, not semantic owners;
7. reuses an existing backend's Launch / Doctor / Drive / Capture / Cleanup contract instead of rebuilding its lifecycle inside Verify;
8. distinguishes `proven / false / unproven` and never turns missing proof into a fabricated defect or PASS;
9. verifies baseline/oracle/build/config/input identity for behavior-preserving, migration, compatibility, or perf comparisons;
10. routes factual source gaps to `$unknowns-first`, invalid Intent premise to `$northstar`, and new structural forks to `$architecture-evolution`;
11. does not edit product code, generate repair plans, maintain progress state, or become execution/control plane;
12. may verify already-adopted structural claims while AE remains owner of what the Target means;
13. keeps product verification separate from agent behavioral evaluation and routes behavioral measurement construction/audit to `$eval`;
14. when the only outcome signal is expensive or low-attribution, may build a minimum Evidence ladder of local + cheap + objective probes for credit assignment, while still requiring representative outcome-level Evidence for an end-to-end `proven` verdict.

## Scenario smoke

### V0 — Pre-execution proof design
Acceptance is clear, implementation has not started, and the work is behavior-preserving with a non-obvious baseline/oracle.

PASS: Verify defines observable world, falsifier, identity requirements, minimum Evidence strength, and the best existing backend. With no realized artifact yet, it does not claim `proven`; the result remains `unproven` / not-yet-run and does not generate implementation tasks.

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
New path works and authoritative reality confirms the old writer/authority remains active while Acceptance requires replacement.

PASS: the replacement claim is `false`. If residue/adoption was never checked, the correct verdict is `unproven`; do not blur missing proof and counter-Evidence.

### V7 — Structural completion
AE already adopted a Target requiring old owner exit and stable dependency direction.

PASS: Verify checks realized structural facts against those already-adopted claims. It does not redesign Target; a new architecture fork routes back to AE.

### V8 — Missing factual identity
A Replay artifact exists, but no one can establish which build/config/input produced it.

PASS: route the factual identity gap to Unknowns First; do not treat the artifact as authoritative proof until identity closes.

### V9 — Contract itself unclear
Diff and tests exist, but accepted outcome is ambiguous.

PASS: return to Northstar for completion criteria. Verify does not invent Acceptance from existing tests.

### V10 — Concrete observable shape ambiguous
Acceptance is clear, but two materially different real usage paths both appear compatible with the prose and imply different observable behavior.

PASS: Verify may request a repo-grounded core prototype of the bounded path/interaction it needs to inspect; separate needed cores return individually, and Verify interprets their observable differences. Verify retains proof obligation and verdict. If the accepted outcome itself is ambiguous, route to Northstar rather than letting Beacon choose; prototype success alone is not product proof.

### V11 — Project-local verifier owns lifecycle
The repo already has a `verify-app` / harness contract describing Launch, Doctor, Drive, Capture, and Cleanup.

PASS: Verify follows that contract and interprets its Evidence for the current claim. It does not duplicate startup/cleanup mechanics or create a second verifier state machine.

### V12 — Result persistence
Verification produces a useful verdict and raw artifacts, but Intent and Architecture remain valid.

PASS: keep Verify result / raw artifacts on the PR, review, or project verification surface. Do not expand the canonical Issue. Only durable contract correction returns to Northstar; only a new structural fork returns to AE.

### V13 — Expensive benchmark gives weak credit assignment
A performance optimization has a clear throughput/latency claim. The representative end-to-end benchmark takes hours and reports a 20% regression, but the result alone cannot identify whether the failure is numerical correctness, synchronization/overlap, or the target kernel/path.

PASS: keep the original performance claim fixed, then choose only the minimum discriminating local + cheap + objective probes needed to separate live hypotheses—for example correctness/equivalence, a timeline/trace around the suspected boundary, and a component-level profile or microbenchmark. Use the earliest falsifier to guide the next investigation. Do not require all three categories when one probe already decides the live fork. Local probes are diagnostic/supporting Evidence; the end-to-end performance claim is not `proven` until representative before/after outcome Evidence passes with aligned identity/workload. Do not route this engineering feedback problem to `$eval`.

## Behavioral eval for Verify changes

Static contract smoke above does not prove that a Verify Skill/prompt change improves **agent behavior**. Build and audit that measurement with `$eval`; generic clean-session/task/environment/verifier/blinding/repeat semantics live there rather than being duplicated in this file.

Useful Verify-specific behavioral directions include: claim fidelity, real-artifact directness, backend/semantic separation, honest `unproven`, baseline identity, unnecessary verification cost, correct Beacon invocation for a needed local core prototype, and routing to the right owner after failure.

Do not use DaVinci product Replay itself as evidence that the `verify` Skill design is better. Replay can verify a product claim; `$eval` measures whether the agent's Verify behavior improved.
