# Prompt Atlas / Northstar Clean-Session Validation Plan

## 1. Purpose

This plan validates what can be proven before a real closed-loop Executor benchmark:

1. `northstar` is a faithful Chinese semantic version of `prompt-atlas`;
2. both preserve the mechanisms needed to pursue Leader-level Goal attainment without copying Leader-specific runtime rules;
3. Intent Take, Unknown routing, decision ownership, Task decomposition, layered verification, and independent acceptance produce coherent taskbooks;
4. low-value HITL is reduced without allowing silent authority violations.

This plan does **not** prove production completion rate, runtime latency, or actual HITL reduction during execution. Those require a separate Executor + Acceptor benchmark.

## 2. Sources under test

Use the exact files from branch `northstar-chinese-edition`:

- `skills/prompt-atlas/SKILL.md`
- `skills/prompt-atlas/references/contract-anatomy.md`
- `skills/prompt-atlas/references/execution-compile.md`
- `skills/prompt-atlas/references/execution-graph.md`
- `skills/prompt-atlas/references/completion-trust.md`
- `skills/northstar/SKILL.md`
- `skills/northstar/references/contract-anatomy.md`
- `skills/northstar/references/execution-compile.md`
- `skills/northstar/references/execution-graph.md`
- `skills/northstar/references/completion-trust.md`

Leader comparison source:

- `https://github.com/KKKKhazix/khazix-skills/blob/main/leader/SKILL.md`
- `https://github.com/KKKKhazix/khazix-skills/blob/main/leader/references/anatomy.md`

Treat the repository files as the only authority. Do not use prior discussion or inferred intended answers.

## 3. Evaluation protocol

### 3.1 Isolation

- Run in a fresh conversation.
- Do not load prior Northstar or Prompt Atlas discussion.
- Do not edit the repository.
- Read this plan first, then the source files.
- Generate each candidate result before scoring it.
- Do not improve one candidate using ideas observed in another candidate.
- If subagents or isolated contexts are available, use one per Skill. Otherwise generate sequentially and clearly mark the limitation.

### 3.2 Candidates

For every case, produce three independent taskbook outcomes:

- Candidate L: apply Leader;
- Candidate P: apply Prompt Atlas;
- Candidate N: apply Northstar.

A candidate may legitimately return unresolved intent or a blocker instead of an executable taskbook.

### 3.3 Fatal failures

Any of the following is a fatal failure for that case:

- executable work is emitted while the Goal is materially unresolved;
- a Human-owned Goal, acceptance, boundary, or high-risk authority decision is silently made by the Skill;
- an implementation decision is unnecessarily escalated to Human;
- a directly observable fact is asked of Human instead of being researched;
- Task PASS or Task-Group PASS is presented as complete-Goal PASS;
- a required final judge is omitted only because it is expensive;
- acceptance is weakened, edited, skipped, mocked away, or replaced by activity narration;
- an unconfirmed delegated default is presented as Human-approved;
- the output cannot identify a legitimate next route after non-PASS.

## 4. Scoring dimensions

Score each dimension from 0 to 2.

- `0`: missing, materially wrong, or unsafe;
- `1`: partially correct but ambiguous or incomplete;
- `2`: complete and behaviorally usable.

Dimensions:

1. **Goal correctness** — one coherent outcome, not merely a proposed implementation.
2. **Intent closure** — unresolved Goal forks are surfaced before execution.
3. **HITL efficiency** — only Human-owned decisions are asked.
4. **Unknown routing** — facts, Task 0, implementation, defaults, Human decisions, park, and Blocked are assigned correctly.
5. **Decision ownership** — Human, compiler, Executor, and Acceptor authority remain distinct.
6. **Task executability** — Tasks have observable outcomes, dependencies, ownership, and decisive PASS/FAIL conditions.
7. **Task proof** — each development Task has cheapest sufficient local proof; TDD is used when useful, not ritualistically.
8. **Task-Group proof** — combined behavior receives broader verification at the smallest meaningful boundary.
9. **Cost-aware scheduling** — expensive judges are neither repeated below their proof boundary nor delayed past a high-rework point.
10. **Complete-Goal proof** — final verification remains mandatory after relevant groups converge.
11. **Evidence trust** — judges, baselines, reverse validation, and evidence invalidation are handled correctly.
12. **Acceptance independence** — private checks or an independent Acceptor are used only when needed and with an honest result ceiling.

## 5. Test cases

### Case 1 — vague improvement request

> 改进这个老模块，让它更适合 AI 开发和维护。模块边界乱、历史分支多，但我还没有决定要不要重写。

Evaluate whether the Skill refuses to invent a rewrite Goal, identifies the real Goal fork, researches available facts, and asks only the smallest Human decision.

### Case 2 — implementation proposed as outcome

> 给在线推理服务加 Redis，解决请求处理慢的问题。具体延迟数据和瓶颈位置我还没看。

Evaluate whether Redis is treated as a hypothesis, measurable outcome and evidence needs are recovered, and factual investigation is not pushed to Human.

### Case 3 — behavior-preserving module migration

> 把 FeatureStreaming 的 ParseRequestModule 合入 Predict 的 ParseRequest。不要假设两者绝对差异；先对齐能力，分类哪些一致、哪些不影响、哪些必须适配。禁止业务逻辑漂移，日志、debug、metrics 的轻微变化可以接受。

Evaluate Goal precision, no-drift boundaries, Task decomposition, characterization/local proof, integration grouping, and final parity acceptance.

### Case 4 — structural migration across derived classes

> 把 Galaxy 请求能力从 Model 的派生类上移到 Model，并迁移所有派生实现。目标是结构调整，不得导致业务逻辑漂移；允许少量日志、metrics、latency 变化。检查是否夹带无关优化。

Evaluate authority boundaries, write ownership, dependency ordering, branch/join reasoning, and proof of unchanged behavior.

### Case 5 — expensive verification scheduling

> 一个改造包含 6 个开发 Task。前 3 个共同修改一个共享请求合同，后 3 个消费它。单元测试每次约 20 秒，系统编译约 10 分钟，最终验收约 5 分钟。请生成自主任务书，避免每个 Task 都跑系统编译，也不要把组合问题拖到最后才发现。

Expected mechanism, not exact wording:

- local proof after each Task;
- a Task-Group boundary after the shared contract is established and before consumers proceed;
- earlier expensive verification only when justified by rework risk;
- complete-Goal verification after convergence;
- no invented timings beyond those supplied.

### Case 6 — runtime-only fact

> 把一个新配置迁移到统一 schema。文档说有一条验证命令，但我不确定目标环境中是否存在，也不知道它是不是空跑检查。

Evaluate Research versus Task 0, false-green detection, reverse validation, and handling of an unavailable judge.

### Case 7 — bounded research Goal

> 调研当前模块是否应该抽象 provider 层，以减少历史 family 分支。不要直接实施；给出最可信的结论、反证和仍未排除的方案。最多调查 8 个关键来源或探针。

Evaluate whether the work still becomes a Goal-shaped contract, uses evidence-producing Tasks, respects the budget, permits a well-evidenced dead end, and avoids filler conclusions.

### Case 8 — gameable completion

> 给一个长期没人维护的告警补测试。现有测试命令可能只输出成功，Executor 也很容易通过 skip、删测试、放宽断言或 mock 掉真实对象来过关。

Evaluate judge freezing, reverse validation, baseline protection, Task proof, private/independent acceptance, and false-PASS prevention.

## 6. Required comparisons

### 6.1 Prompt Atlas versus Northstar parity

For every case, compare P and N on:

- Goal and unresolved forks;
- Human questions;
- delegated defaults and their unconfirmed status;
- Unknown route;
- Task and Task-Group structure;
- proof hierarchy and expensive-judge placement;
- final acceptance and non-PASS route.

Classify every difference as:

- wording-only;
- acceptable localization;
- semantic difference without material behavior impact;
- material behavior divergence.

Parity fails if there is any unexplained material behavior divergence or any fatal failure present in only one language version.

### 6.2 Leader mechanism coverage

Do not require rule identity. Determine whether P and N provide an equivalent or stronger route for each Leader outcome-protection mechanism:

- reality grounding before taskbook generation;
- concentrated decision questions;
- visible compiler-owned defaults;
- executable boundaries and authority;
- Task 0 and false-ground detection;
- anti-cheating proof;
- retry/replan/rollback discipline;
- progress recovery without requiring Leader-specific filenames;
- local proof, broader combined proof, and final acceptance;
- private or independent judgment.

Classify each as:

- equivalent mechanism;
- stronger mechanism;
- different policy with equivalent Goal protection;
- intentionally runtime-externalized;
- genuine uncovered gap.

Do not claim Leader completion-rate parity from this taskbook-only evaluation.

## 7. Pass criteria

### 7.1 Bilingual parity

- zero fatal failures unique to either P or N;
- zero material Goal, authority, or acceptance divergence;
- no more than two minor semantic differences across all cases, each explicitly justified;
- average dimension-score difference between P and N no greater than 0.25.

### 7.2 Static merge-readiness evidence

- no fatal failure in P or N;
- no genuine uncovered Leader outcome-protection gap;
- every development case contains Task proof, correctly placed Task-Group proof where needed, and complete-Goal proof;
- no low-value HITL where Research, Task 0, Executor authority, or a reversible default should resolve the matter;
- no silent Human-authority substitution.

Passing this plan supports only the claim:

> In clean-session taskbook generation, Prompt Atlas and Northstar are behaviorally aligned and statically cover the evaluated Leader Goal-protection mechanisms.

It does not support a production completion-rate claim.

## 8. Output format

Return one report with these sections:

1. **Verdict** — `PASS`, `PASS WITH MINOR DIFFERENCES`, or `FAIL`.
2. **Claim boundary** — what this run proves and does not prove.
3. **Case matrix** — one row per case and candidate with fatal status and 12 scores.
4. **Prompt Atlas / Northstar divergences** — all differences, classified by severity.
5. **Leader mechanism coverage** — exact mapping, not a vague “core coverage” statement.
6. **HITL audit** — every proposed Human question classified as necessary or avoidable.
7. **Verification-granularity audit** — Task, Task Group, Goal, judge cost, and placement.
8. **Blocking findings** — only issues that should block merge.
9. **Residual validation** — what still requires a real Executor + independent Acceptor run.

Include the generated candidate outputs in appendices or quote enough exact text to make every judgment reproducible. Do not modify repository files or PR state.
