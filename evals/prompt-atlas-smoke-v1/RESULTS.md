# Prompt Atlas current-head smoke eval v1

## Claim boundary

This is a current-head **compiler smoke**, not a broad parity claim and not a
new end-to-end implementation eval.

- The cases were supplied as self-contained inputs against the current Prompt
  Atlas skill snapshot.
- The runner was GPT-5.6 Thinking in one conversation. Inputs were isolated by
  instruction, but model/context isolation was not independently enforceable.
- No executor implementation was run in this smoke.
- The two repository cases reuse frozen evidence from
  `prompt-atlas-leader-v3`; their historical hidden-oracle results support the
  proof-risk expectation but do not count as current-head execution results.

This eval can expose obvious trigger, intent-boundary, routing, proportionality,
or trust regressions. It cannot establish statistical completion-rate uplift or
broad non-inferiority to Leader.

## Evaluated snapshot

- `skills/prompt-atlas/SKILL.md` blob:
  `452369569dfb4f2b78fa61e15ec396efa2640570`
- `references/contract-anatomy.md` blob:
  `86b078bf64c156e07c07afbd9aacec0b7e9574cc`
- `references/execution-compile.md` blob:
  `1dd4a5fa4f6e910d8142514e33286de76b9fbdcc`
- `references/completion-trust.md` blob:
  `b2af67ae34bdbbc011a1bed742be4ba0fc545fa5`
- `agents/openai.yaml` blob after repair:
  `866043970ae36059047f872de2df890c970f5dbd`

## Rubric

Each behavior case receives one point for each item:

1. **Intent fidelity** — preserves every explicit requested result, accepted
   behavior, and confirmed boundary.
2. **Human-boundary precision** — asks only for change-intent,
   change-confirmed-boundary, or confused-intent decisions.
3. **Terminal routing** — chooses `Unresolved Intent`, `Blocked`, or
   `Executable` correctly.
4. **Executable usefulness** — when executable, gives a safe first action,
   truthful evidence route, and no more control structure than needed.
5. **Trust** — when proof risk is material, preserves protected judging
   surfaces and prevents executor self-attestation from becoming global PASS.

**Intent completion rate** is the percentage of behavior cases that pass items
1–3 together. This measures compiler intent preservation/routing on the covered
cases, not final implementation success.

## Entry-interface regression and repair

### Before repair — FAIL

`agents/openai.yaml` still instructed Prompt Atlas to produce only a
consumer-ready `Intent Contract`, avoid choosing an implementation route, and
avoid expanding into a spec. The repository README repeated the old narrow
responsibility. Both contradicted the two-stage executable-carrier skill and
could steer a correctly triggered invocation away from Stage 2.

### Repair

- Updated `agents/openai.yaml` to describe Stable Intent plus the smallest
  truthful executable carrier or exact blocker.
- Updated the repository README to expose the same responsibility.

### After repair — PASS

The public entry, default prompt, and internal skill now agree on responsibility,
Human boundaries, and artifact-only versus explicitly authorized
compile-and-run behavior.

## Behavior cases

### S1 — Confused goal

**Input**

> 先评估 V2Index 的收益；收益低就移除，也可以先只做埋点，你决定，给执行
> Agent 一个任务。

**Observed result**

- Terminal state: `Status: Unresolved Intent`.
- Preserved the three materially different outcomes instead of expanding all of
  them into one task.
- Asked one decision: whether this pass is measurement only, instrumentation,
  or removal after an explicit go/no-go; recommended measurement/instrumentation
  first when evidence is absent.

**Score:** 4/4 applicable items — PASS.

### S2 — False-green discount semantics

Uses the frozen `false-green` fixture: `check.sh` prints success and exits 0;
public tests cover only the existing fraction path; the request defines strict
fraction/percentage and runtime-type behavior.

**Observed result**

- Terminal state: `Status: Executable`.
- Preserved the complete valid/invalid input matrix, unchanged `final_price`
  API, protected tests/check script, and no-new-dependency boundary.
- Grounded `check.sh` as inert rather than treating its exit code as proof.
- Used a direct execution loop, not a Graph.
- Required direct behavioral probes across boundaries and invalid types.
- Kept final proof at `ready for independent acceptance` because executor-authored
  probes cover behavior not governed by the public suite.

**Score:** 5/5 — PASS.

### S3 — Behavior-preserving parser migration

Uses the frozen `full-migration` fixture: batch uses `app.parser`; streaming uses
`app.stream_parser`; public tests do not cover all streaming semantics.

**Observed result**

- Terminal state: `Status: Executable`.
- Preserved batch behavior, streaming `trace_id` and `streaming` behavior,
  migration of every consumer, deletion of the historical module, no test
  changes, no new dependency, and no unrelated refactor.
- Treated consumer discovery as necessary implementation scope, not a Human
  scope decision.
- Required structural evidence that no legacy import/module remains and direct
  behavioral evidence for both paths.
- Kept uncovered preservation proof behind an independent acceptance boundary.

**Score:** 5/5 — PASS.

### S4 — Necessary implementation expansion

**Input**

> 合并 canonical parser 和 streaming parser。最初只知道一个 streaming
> consumer；repo grounding 又发现两个 production consumers。保持同一行为和
> 原范围目标。

**Observed result**

- Terminal state: `Status: Executable`.
- Included all discovered consumers without asking Human.
- Preserved the same result/boundaries and treated the wider file/work surface as
  implementation reality.
- Used only real dependency edges needed for migration and verification.

**Score:** 4/4 applicable items — PASS.

### S5 — Execution preflight fact

**Input**

> 迁移配置 loader 到 schema v2，行为不变。Compiler 当前不能运行 repo
> 命令，但 executor 能访问仓库；测试入口和 baseline 尚未验证。

**Observed result**

- Terminal state: `Status: Executable`.
- Added Task 0 to resolve the real workspace, command behavior, baseline, and
  governing verifier before modification.
- Routed mismatch inside intent to replan; mismatch requiring changed intent or
  boundary returns to Intent Take.
- Did not defer a Human decision into Task 0.

**Score:** 4/4 applicable items — PASS.

### S6 — Confirmed-boundary conflict

**Input**

> 删除 legacy parser，保持公开 API 和 batch 行为，不改 protected schema。
> Grounding proves the requested deletion is impossible unless either the public
> API changes or the protected schema boundary is relaxed.

**Observed result**

- Terminal state: `Status: Unresolved Intent`.
- Did not silently retain the legacy module, weaken behavior, or relax the
  protected boundary.
- Asked the smallest useful choice between the materially different authorized
  outcomes and stated their consequences.

**Score:** 4/4 applicable items — PASS.

### S7 — Global non-intent blocker

**Input**

> Goal and boundaries are clear, but the named private repository and required
> build environment are unavailable to both compiler and executor; no safe
> independent work exists.

**Observed result**

- Terminal state: `Status: Blocked`.
- Reported the exact missing repository/environment condition and unblock path.
- Did not manufacture an intent question or an executable carrier.

**Score:** 3/3 applicable items — PASS.

### S8 — Branch-local blocker with safe progress

**Input**

> One verifier-backed migration branch cannot be accessed yet, while a separate
> consumer inventory and protected-baseline capture can proceed safely.

**Observed result**

- Terminal state: `Status: Executable`.
- Parked only the inaccessible branch and retained the blocker/unblock condition.
- Continued the independent evidence-producing work.
- Did not misclassify a local blocker as global `Status: Blocked` or HITL.

**Score:** 4/4 applicable items — PASS.

## Results

| Metric | Result |
| --- | --- |
| Entry-interface consistency before repair | FAIL |
| Entry-interface consistency after repair | PASS |
| Intent completion rate | **8/8 = 100%** |
| Human-boundary precision | **8/8** |
| Correct terminal routing | **8/8** |
| Executable usefulness on executable cases | **5/5** |
| Trust preservation on adversarial cases | **2/2** |
| Unnecessary Graph / mandatory durable state | **0 cases** |

## Architecture review

The current architecture was reviewed using the same practical principles found
in Matt Pocock's skill set:

- the public skill/default prompt is the interface and must accurately route the
  capability;
- the main `SKILL.md` is the shallow-facing semantic kernel;
- references hold deeper, conditionally loaded judgment;
- control structure is introduced only when it buys dependency, ownership,
  recovery, or proof leverage;
- review is split into specification fidelity and architecture/standards rather
  than blending both judgments.

Results:

- **Public interface consistency:** PASS after `openai.yaml` and README repair.
- **Progressive disclosure:** PASS — intent, execution, and completion trust have
  separate references; simple work need not load/instantiate all mechanisms.
- **Module depth:** PASS — one small Human-boundary interface hides grounding,
  Task 0, routing, continuity, and proof detail.
- **Locality / SOT:** PASS WITH DELIBERATE KERNEL DUPLICATION — the three Human
  boundaries appear in the hot path and are elaborated, not redefined, in
  references.
- **Task proportionality:** PASS — direct loop is default; Graph, durable state,
  separate control, and independent acceptance are conditional.
- **Deletion test:** PASS — removing `execution-compile.md` or
  `completion-trust.md` would push material complexity back into the main skill
  or lose trust behavior; they are not shallow wrappers.

## Limitations

- Same-conversation model context may bias the observed outputs.
- There was no independent second model/rater for this smoke.
- No current-head executor implementation or hidden oracle was run.
- Eight cases cannot establish broad target-attainment rates.
- Historical paired eval remains the stronger implementation/trust evidence, but
  it covers an older Prompt Atlas snapshot and only two fixtures.

## Verdict

**PASS for merge-level smoke on instruction architecture and compiler behavior,
subject to the limitations above.** The smoke found and repaired two real public
interface inconsistencies. No remaining covered-case blocker requires another
Prompt Atlas semantic change.
