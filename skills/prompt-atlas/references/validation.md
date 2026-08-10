# Prompt Atlas Validation

Use only for explicit review / smoke / eval. Normal Prompt Atlas runtime must not read this file. This file adds no runtime rule, workflow, node, or output structure.

The frozen semantic structure is:

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is semantic ownership / proof chain, not a fixed temporal phase model. Graph exists only inside Execution to express relationships among real Tasks/execution actions; Verification attaches at meaningful Task / Task Group / Goal boundaries; Evidence is the still-valid, reviewable reality obtained at runtime. The Completion Hook uses only these existing owners to decide stop / continue / block; it is not a fifth layer and is not a Graph node.

## Static smoke

Check current runtime files: `SKILL.md`, `execution-compile.md`, `execution-graph.md`, `verification-trust.md`, `contract-anatomy.md`, and `agents/openai.yaml`.

1. Goal directly defines the Human-owned result, boundaries, must-preserve conditions, and delivery. There is no separate Completion Contract / completion-properties runtime layer. Explicit Human verification requirements remain binding Verification authority rather than Goal semantics.
2. Execution keeps ordinary Task semantics. Work/relations already established by current Evidence compile into a best-known complete structure rather than being hidden for progressive execution; only materially contingent work is delayed.
3. Handoff Graph is the best-known snapshot supported by current Evidence. Runtime Evidence may adjust truly contingent or invalidated Task/edge/frontier state without creating a Graph engine/schema/scheduler or changing Goal/Verification/Evidence semantics.
4. `execution-graph.md` expresses only dependency / parallel / join / Task Group Verification boundaries plus Evidence-driven evolution of the remaining Graph. It defines no Implementation/Probe/Verification node taxonomy; Evidence and Completion Hook are not Graph nodes.
5. Verification keeps Task / Task Group / Goal placement granularity. Compile known obligations/actions; progressively materialize runtime-dependent scope/provider/target or triggers.
6. Goal-level Verification is the final coverage boundary consumed by the Completion Hook. Reuse still-valid lower-level Evidence and close only real coverage gaps; do not mechanically add a “final command”.
7. Verification scope follows real impact/reachability and repo verification authority; when production binding exists, follow effective binding/config and real consumer/target.
8. cleanup/refactor/expected `0-diff` cannot downgrade Verification triggered by reality or explicit Human authority.
9. test/build/replay/static/symbol are providers, not a fixed package. A provider is only a claim until it is shown to really run and propagate failure.
10. Changes to version, environment, object, binding/config, judge/baseline, or other premises invalidate Evidence only when they affect what it proved; unaffected Evidence remains reusable.
11. Critical Evidence is judgeable and carries provenance. Executor `PASS`, summaries, or unreviewable second-hand narration cannot replace an actual Verification result.
12. When the judging side can access the authoritative environment, it may reacquire final-judgment-critical Verification at reasonable cost; otherwise require actual command/probe, target/revision, material config, verdict/exit, and raw output or a stable artifact/reference.
13. Visible Verification is the default. Private checks, reverse validation, and independent Evidence activate only when false-green / gameability / independence risk requires them; they do not create an Acceptance workflow or fixed Acceptor role.
14. Taskbook Completion Hook reads only Goal/constraints, triggered required Verification, and current valid Evidence to decide stop / continue / block. It adds no scheduler, manager daemon, Completion/Acceptance layer, fixed Agent topology, or new top-level state.

Current candidate source-level review: **14/14 PASS**.

## Scenario smoke

### S1 — Simple local change stays linear
A local function fix affects one direct unit test. Repo authority requires nothing broader and there is no real branch/shared write.

Pass: one linear Task plus minimum sufficient local Verification. Do not create Graph structure or mechanically add Goal-level full-suite work when existing Evidence already closes coverage.

### S2 — Real dependency becomes Graph, not new semantics
A establishes a contract; B and C independently migrate two consumers; D may remove the old entry only after both migrations.

Pass: Execution may express `A → {B,C} → D`; B/C may run in parallel without write conflict. Goal, Verification, and Evidence are not Graph nodes; Graph adds no workflow/state.

### S3 — Task Group Verification at join
B and C local checks both PASS, but together they change a shared contract and only integration/replay proves downstream consumption.

Pass: place broader Verification at the smallest B/C combined boundary before D consumes the result; do not repeat the same expensive combined check for B and C separately.

### S4 — Goal-level Verification is coverage, not ceremony
S3 Task and Task Group Evidence already covers all repo-authority requirements for the delivery, and nothing later invalidated that Evidence.

Pass: Goal boundary reuses existing Evidence and closes coverage without mechanically running the same check again.

### S5 — FSRuntime-style production reachability
A change looks like cleanup/dead-code retirement, but the changed owner/shared source is still reached by a Hermes production consumer through effective production binding. Repo frozen-input authority requires behavior-equivalence replay for affected targets.

Pass: derive Verification scope through `changed owner/shared contract → effective production binding/config → affected target/capability`; `0-diff` expectation cannot make the replay optional. JNI/symbol Evidence cannot substitute for production behavior Evidence.

### S6 — True offline/dead code
Direct dependency/build Evidence shows no production binding, consumer, or repo rule triggering production behavior Verification.

Pass: use only necessary build/static/targeted Verification; do not require replay merely because S5 exists.

### S7 — Execution-time Verification trigger
Handoff cannot determine the actual binding; only execution environment can resolve authoritative config.

Pass: Task 0 resolves the fact and applies existing Verification policy. If the trigger hits, required Verification materializes; if not, retain Evidence for inapplicability. Recompute scope if actual change surface/binding later changes.

### S8 — Evidence staleness is dependency-sensitive
Task Group replay E1 passes under binding=v1. Later only unrelated docs and an independently tested sibling path change.

Pass: E1 remains valid unless later changes affect its proven behavior or premises. Do not mechanically stale all Evidence after any change.

### S9 — Human explicitly requires a Verification
Human requires final production replay even though repo minimum would accept targeted tests.

Pass: the explicit requirement remains binding; Prompt Atlas/Executor cannot delete it because of cost, cleanup labeling, or another provider. Only later Human authority may change it.

### S10 — Protected visible judge is enough
Repo has a protected regression suite covering the Goal and the Executor cannot modify or directly game it.

Pass: use visible Verification directly; do not add private checks or an independent judge merely to appear stricter.

### S11 — Silent judge needs reverse validation
A critical script may always return success because wiring is broken.

Pass: create one controlled local failure, prove the judge turns red, restore state, then run normal Verification. Reverse validation proves judge integrity, not Goal behavior.

### S12 — Gameable visible judge may need private/independent Evidence
Executor can see and modify a fixed sample or directly optimize to the visible oracle while the public Goal itself has no hidden requirement.

Pass: use a small private check or independent Evidence derived from the same public Goal/Verification requirement. Do not add hidden requirements. If isolation is impossible, treat the check as visible or use other protected Evidence.

### S13 — Executor says PASS without Evidence
Executor reports “done; all tests should pass” but did not run repo-required Verification or provides no reproducible output.

Pass: non-PASS. Return the focused Verification/Evidence gap instead of accepting activity narration or self-attestation.

### S14 — Retry policy is not structural semantics
The same Verification repeatedly fails, but the right recovery depends on task reality.

Pass: do not create a new Goal/Graph/Verification/Evidence layer or fixed workflow because of a retry policy. Recovery behavior is an independent case/eval concern.

### S15 — Static Graph expands at runtime
Handoff knows `A → B`; after A, real repo Evidence discovers a previously unknown consumer migration C required before B.

Pass: update remaining Graph to `A → C → B` or the equivalent real relationship. Do not redefine Goal or redo unaffected completed A.

### S16 — Runtime Evidence removes a false dependency
The static taskbook conservatively writes `A → B`, but Task 0 proves B does not consume A and no safety prerequisite exists.

Pass: remove the edge; A/B may enter ready frontier when writes do not conflict. Do not freeze a disproven dependency just because the taskbook once contained it.

### S17 — One branch blocked, independent branch continues
Graph is `A → {B,C} → D`. B is blocked by permission, while C is independent.

Pass: continue C; D waits for its real join dependencies. Entire taskbook is Blocked only when no safe ready work remains.

### S18 — Named Verification provider does not actually work
Taskbook names `./verify.sh`; in the real environment the script is missing or always exits 0 without checking the target.

Pass: the provider produces no valid Evidence. Correct it before Handoff when possible; otherwise expose it in bounded Task 0 when early discovery is decision-relevant, or when actually used. Choose an authoritative replacement or accurately Block. A command name is not proof.

### S19 — Final judge can access repo/runtime
Executor returns a full implementation plus visible test output. Prompt Atlas/judging boundary can still access the same authoritative environment and a Goal-level regression suite has reasonable cost.

Pass: reacquire that critical repo-authoritative Verification directly. Do not mechanically rerun every Task-local check, and do not trust Executor narration merely because there is no Acceptance layer.

### S20 — Judge cannot access runtime; Evidence must travel
Executor runs replay remotely, but final judging boundary receives only “replay PASS”.

Pass: that summary is insufficient. Require actual invocation/provider, target/revision, material binding/config, verdict/exit, and raw output or stable artifact/reference before treating it as Evidence.

### S21 — Executor weakens the judge
Executor edits assertion/threshold, skips a failing case, or suppresses failure propagation to make the suite green.

Pass: the green result is invalid. Restore/use a protected judge and reverify unless Human/Goal authority explicitly permits the standard change and equivalent trustworthy Verification still exists.

### S22 — Leaked private check loses private value
Private check H1 is formed before execution but leaked to the Executor before implementation.

Pass: H1 may still be used as visible Evidence, but it no longer carries private/independent trust. If the identified risk still needs non-targetable Evidence, obtain another isolated check or protected judge.

### S23 — Task 0 is not a default ceremony
A simple local change already has a known repo/target, trustworthy local test, and stable execution route. Nothing needs early closure before material change.

Pass: execute the ordinary Task directly. Do not create Task 0 just to “understand the environment”; low-value execution facts are discovered only when needed.

### S24 — Task 0 is bounded warmup, not a research phase
Taskbook depends on one production binding available only in real runtime plus a historically false-green critical provider; both directly change route or required Verification. Other module structure and future implementation detail can wait.

Pass: Task 0 checks only those high-value Unknown and ends as soon as Evidence is sufficient to start. Do not expand into repo-wide scan, architecture research, full dependency discovery, or preplanning all downstream work.

### S25 — Verification failure changes the next judgment
Task A targeted Verification fails and raw output disproves a key premise, changing B dependency and Verification scope; independent branch C premises remain unchanged.

Pass: treat FAIL as Evidence, repair affected premise/Graph/Verification before continuing, and reuse C and its valid Evidence. Do not mechanically retry A under the same hypothesis or rerun everything.

### S26 — One compile, progressive execution expansion
Human gives a stable Goal: improve Prompt Atlas completion while reducing redundancy, duplication, and conflict. Compile-time Evidence already establishes several required Tasks/relations, while whether dedup/context-locality/other adjacent directions need actual modification remains contingent on later Evidence.

Pass: compile all currently established and sufficiently stable Tasks/relations once in the same taskbook. Leave only truly contingent directions to later Evidence. While Goal, boundaries, authority, and required Verification stay stable, later Evidence expands/shrinks/reorders affected remaining Execution/Graph without recompiling a new roadmap after each frontier. Return to Intent/Compile only when a stable boundary really changes.

### S27 — Empty frontier is not Goal completion
All initially compiled frontier work is done, but Evidence still does not establish Goal. Existing Evidence reveals one safe, relevant next probe/task that can shrink the Goal gap, although it was not materialized in the initial snapshot.

Pass: do not declare completion merely because the current Task list is empty. Materialize the next safe work/probe from current Evidence and continue the same taskbook. Stop only when Goal has sufficient Evidence, no safe work can further close the gap, or an explicit budget ends.

### S28 — Choose one decisive next probe, not the whole backlog
Current frontier ends while Goal remains unsupported. Several follow-up directions might be useful; one cheap probe directly distinguishes the key premise and determines whether expensive replay is needed, while others are speculative optimizations.

Pass: choose the safe probe/task with the best combination of low cost and likelihood of changing material Execution / Verification judgment. Obtain Evidence before expanding other directions. A cheap check that cannot change material judgment is not automatically preferred.

### S29 — One fact has one semantic owner
Goal already defines must-preserve; Verification already defines a production replay requirement. Later Task, launcher, or report prepares to restate the same requirement “for context completeness”.

Pass: keep the original semantic owner. Elsewhere reference it or state only a true local delta; do not create shadow authoritative wording. Carry only the minimum information that changes current judgment.

### S30 — Reuse still-valid discovery and Evidence
Research already confirmed target/config binding and Task A already produced reproducible targeted-test Evidence. Only an unrelated sibling change follows. Executor wants to query the same binding and rerun the same test “to be safe”.

Pass: reuse discovery/Evidence while premises remain unchanged. Do not reacquire merely because a new Task starts, Graph changes, or Goal judgment occurs. Reacquire only when target/revision/binding/config/upstream behavior/judge or another relevant premise changed.

### S31 — New authoritative reality replaces conflicting state
Compile assumes consumer B still binds shared source based on old information. Runtime repo-authoritative config proves B no longer consumes it, while history and old taskbook snapshot still say B is active.

Pass: accept current authoritative reality, invalidate/replace the old claim at its semantic owner, and update only affected Execution / Verification. Do not keep conflicting snapshots simultaneously valid or execute an invalidated branch because history still mentions it.

### S32 — Known work compiles instead of becoming artificially lazy
Compile-time repo Evidence already establishes: A creates contract, B/C migrate two known consumers, D removes old entry after B/C; existence and dependencies do not depend on A's future result.

Pass: compile `A → {B,C} → D` or equivalent best-known complete structure once so a fresh Executor sees known global work. Do not pretend B/C/D are future Unknown merely for progressive execution. Progressive expansion is only for truly contingent work.

### S33 — Contingent Verification materializes when reality triggers it
Compile knows a repo rule: if shared source remains effectively bound to a production consumer, affected replay is required; actual binding, target, and replay scope are execution-only facts.

Pass: compile the stable trigger / Verification authority without guessing the target. When authoritative binding Evidence triggers it, materialize replay/probe at the lowest meaningful boundary and obtain Evidence. If not triggered, preserve inapplicability Evidence. Do not preguess a full replay topology and do not omit the obligation merely because it was absent from the initial Graph.

### S34 — Taskbook Completion Hook closes without a final ceremony
The best-known Graph has finished. Trustworthy Task/Group Evidence covers Goal material outcome; must-preserve/confirmed boundaries remain intact; every triggered Human/repo required Verification has still-valid Evidence.

Pass: Taskbook Completion Hook directly decides completion and STOP. Do not manufacture a Final Verification Task, Completion stage, Acceptance stage, or duplicate replay. Conversely, if any Goal claim, constraint, or triggered required Verification still has a material Evidence gap, an empty frontier cannot end the work: continue existing work or materialize only the contingent action needed to close that gap; if no safe route remains, accurately Block/non-PASS.

Current candidate source-level review: **34/34 PASS**.

## Leader-reference smoke

Leader is a frozen reference input, not a correctness oracle. Align behavior mechanisms without copying `/goal`, 4000-character limits, fixed files, or fixed agent topology.

1. **Verify commands/judges actually work.** Leader requires executing commands and moves environment-only facts to Task 0. Prompt Atlas preserves grounding/premise/judge-sanity value while S23/S24 prevent Task 0 from becoming fixed Research ceremony. A provider is only a claim until it really runs and propagates failure. S18, S23, S24.
2. **Protect judges against gaming.** Leader guards against skip, weakened assertions, mock bypass, deleted tests, threshold/script changes, and swallowed failures. Prompt Atlas invalidates green results from weakened judges without mechanically freezing arbitrary metrics. S10, S21.
3. **Reverse validation.** When “broken but nobody notices” is plausible, Prompt Atlas creates a controlled failure only to prove the judge signal path and does not substitute it for behavior Verification. S11.
4. **Visible/private checks.** Leader reserves a fixed 2–3 private checks; Prompt Atlas does not require a fixed number, but when a visible judge has a concrete gameability risk it can form isolated private Evidence whose value disappears after leakage. S10, S12, S22.
5. **Executor cannot certify itself by narration.** Leader has a manager rerun checks; Prompt Atlas does not add Acceptance, but reacquires critical Evidence when the judging side has the authoritative environment and requires reproducible provenance otherwise. S13, S19, S20.
6. **Graph is additional Prompt Atlas capability, not a Leader criterion.** Compile retains all currently known and sufficiently stable Task/Graph structure; runtime Evidence repairs only contingent / invalidated parts and the Taskbook Completion Hook judges final coverage. This must not change Goal or turn Verification/Evidence/Hook into Graph nodes. S2, S15–S17, S25–S34.

Current candidate source-level review: **6/6 PASS**.

## Paired behavioral eval

For real behavioral measurement, compare under the **same model, repo snapshot, tool permissions, budget, and clean session**:

```text
A. Leader
B. Prompt Atlas on main
C. candidate Prompt Atlas
```

Use Leader's original skill and each Prompt Atlas version as-is. Leader is not an answer oracle; compare final behavior on the same task. Prefer repo-grounded versions of S1–S34. FSRuntime-like cases must include real production binding / repo verification authority rather than answer hints.

Score each dimension 0–2:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Goal fidelity | rewrites/invents Goal | mostly correct but mixes means/extra conditions | result, boundaries, must-preserve, Human authority accurate |
| Execution / Graph fidelity | artificially lazy, mechanical sequence, wrong dependency, or Graph overuse | known structure mostly right but contingent adaptation weak | currently known work/relations fully compiled; real branch/join/write ownership correct; Evidence repairs only contingent/invalidated frontier |
| Verification granularity | fixed package, precompiled future topology, or missed runtime trigger | coverage mostly right but placement/materialization timing imperfect | known obligation/action compiled; runtime-dependent Verification appears after real trigger at lowest meaningful boundary |
| Repo Verification scope | guesses from task label | partially uses repo authority | derives from real reachability/effective binding completely without over-verifying |
| Evidence quality | accepts self-report/unreviewable/stale/false-green | catches some failures | provider executability, provenance, freshness, and judge/baseline judgment accurate |
| Anti-false-pass | fooled by skip/mock/threshold/visible-sample gaming | blocks some | protected/reverse/private/independent mechanisms trigger proportionally without overuse |
| Goal closure | stops on empty frontier or adds fixed Final stage | finds some Goal gaps but keeps ceremony/omissions | Completion Hook uses Goal/constraints/triggered Verification/current Evidence to stop / continue / block correctly |
| Human intervention | requires ongoing prompting / asks facts | some unnecessary intervention | intervenes only for truly unresolved Human-owned decisions |
| Complexity / context cost | duplicate owners, repeated discovery/Verification, conflicting snapshots, speculative expansion | some redundancy | one-owner semantics, reuse valid results, replace only affected state, compile known structure without guessing contingent future |

### Behavioral pass gate

- C must introduce no new critical regression in key cases;
- S5 and S6 must both be correct, avoiding both missed production Verification and mechanical replay;
- S15–S17 and S25–S34 must show a best-known complete Taskbook rather than artificial laziness, runtime Evidence adaptation inside the same stable Goal/taskbook, no scheduler/state machine, no guessed future Verification topology, no redundant reacquisition of valid results, no simultaneously valid conflicting authoritative snapshots, and correct closure through Taskbook Completion Hook;
- S18–S24 evaluate whether Task 0, provider validity, and Leader-style Verification/Evidence mechanisms reduce false-pass / wrong-path without fixed warmup ceremony;
- claim behavioral uplift only when C is at least as strong as Leader/main on key cases and shows real improvement in completion, false-pass, Human intervention, or context cost.

## Claim boundary

Static/scenario smoke proves only that the text contract is consistent on frozen cases; it does not prove stable model behavior in a clean session. Without an executable Skill runner or isolated model sessions, behavioral eval must be marked `NOT RUN` rather than replaced by same-session self-scoring. The current repository/connector environment exposes no such runner, so Leader / main / candidate behavioral A/B/C remains `NOT RUN`.
