# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills:

```bash
npx skills@latest add feng-y/skill --all
```

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill beacon
npx skills@latest add feng-y/skill --skill architecture-evolution
npx skills@latest add feng-y/skill --skill verify
npx skills@latest add feng-y/skill --skill eval
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `northstar` — canonical engineering-intent skill. 把 conversation / request / incident 收敛成 durable Intent；需要跨 session / agent / Human 或执行环境流转时 materialize 为 Drafted Issue。Issue 是 Intent carrier，不是独立 Skill。
- `beacon` — caller-neutral、主要由 model 按需调用的核心原型 specialist。基于真实 repo，把一个 bounded 功能 Intent 或故障具体化为最小、可检查的核心原型；可以是接口/调用草图、代表性输入输出、最小实现或故障复现，不要求可执行代码。原型是主体，问题和 Evidence 服务于原型；结果返回原 caller。
- `architecture-evolution` — long-term Target Architecture judgment + Current → Target structural Evolution Program。Target 与 Program 是两层不同 judgment，但由一个外部 Skill 承担。
- `verify` — engineering verification skill. 从 authoritative completion/safety claim 出发定义 proof obligation，选择并驱动最直接的 real-artifact verification backend，收集 Evidence 并判断 proven / false / unproven。
- `eval` — agent behavioral evaluation engineering skill. 从 repo / agent surface / traces 中选择 material capability 或 failure，构建 Task + Environment + Verifier，运行并检查 agent/verifier trajectory，形成可重复 behavioral measurement。
- `unknowns-first` — factual map-versus-territory specialist. 只关闭会改变下一步判断的 repo/runtime/data/source fact，不接管 Intent、Beacon、Architecture、engineering proof 或 agent behavioral eval judgment。

## Invocation model

主要 Human-facing / direct capabilities：

- `northstar` — “我们到底要什么？”
- `architecture-evolution` — “长期结构应该怎么归位？”
- `verify` — “产品/工程结果是否真的符合 claim？”
- `eval` — “这个 Agent / Skill / prompt / harness 行为是否真的变好，怎么稳定测？”

主要 model-invoked specialists：

- `beacon` — 一个局部功能 Intent 或故障需要基于 repo 的核心原型，或已有原型需要局部修订；Human 很少需要主动调度。
- `unknowns-first` — 当前判断依赖未核实事实时自动/按需关闭 factual gap；Human 也可以直接要求先查事实。

`beacon` **不属于 Northstar 私有流程**。Northstar、Architecture Evolution、Verify、Unknowns First 或其他 caller 都可以按需调用；不必先制造设计歧义或查清全部故障根因。Beacon 返回一个局部核心原型，原 caller 负责采用、比较与组合；Northstar 持续拥有完整 Intent。

`eval` 与产品 engineering flow 正交。它可以由 Human 直接调用，也可以在 Skill/prompt/tool/harness 变更需要 behavioral Evidence 时由 model 按需调用；它观察 agent behavior，不取得被测 Skill 的 semantic ownership。

## Capability map

```text
conversation / request / incident
              ↓
          northstar
      canonical Intent
              │
   ┌──────────┼──────────────────┐
   │          │                  │
   ▼          ▼                  ▼
 beacon   architecture-evolution  unknowns-first
   ▲          │                  │
   └──── model-invoked by any semantic caller ────┘
              ↓
         Drafted Issue
              ↓
          execution
              ↓
              PR

accepted completion / safety / structural claim
              ↓
            verify        # optional before / during / after execution
              │
              ├── bounded behavior / fault needs core prototype → beacon
              ↓
      proof obligation
              ↓
   verification backend(s)
 test / build / DaVinci Replay / runtime / data / profile
              ↓
            verify
   Evidence + proven / false / unproven
              ↓
  affected semantic owner / Executor

agent / Skill / prompt / tool / harness behavior
              ↓
             eval
       repo + traces + Human priority
              ↓
  Task + Environment + Verifier
              ↓
       eval backend(s)
 Harbor / clean-session runner / trajectory recorder / project harness
              ↓
             eval
  Run Evidence / trajectories + trustworthy measurement
              ↓
 Skill / prompt / tool / harness improvement → rerun
```

Northstar owns **meaning and composition**. Beacon owns **repo-grounded core prototypes of bounded feature intents or faults** and returns them to its caller. Architecture Evolution owns **structural judgment**. Unknowns First owns **factual uncertainty**. Verify owns **product/engineering verification and proof judgment**. Eval owns **agent behavioral measurement design and judgment**. Verify Evidence 和 Eval Run Evidence 都不是新的 semantic owner。

Verify is not a mandatory post-PR stage. It may be invoked before implementation to make a material proof route explicit, during implementation when verification premises change, or after implementation to judge realized results. Clear local changes can rely on an already-authoritative focused check without extra ceremony.

Verification backends are orthogonal to this capability map. A project may use tests, build, integration harnesses, runtime probes, data checks, profiles, or project-specific systems. **DaVinci harness Replay is one such executable verification backend; it is not a Skill or semantic owner in this repo.** If a backend already owns Launch / Doctor / Drive / Capture / Cleanup, Verify follows that contract rather than recreating a second harness lifecycle.

Eval backends are likewise orthogonal. **Harbor is one possible task/eval execution backend, not the `eval` Skill identity.** Existing clean-session runners、trajectory recorders 或 project-local evaluation harnesses 都可以承载同一个 Task / Environment / Verifier contract；Eval 负责 measurement semantics 与可信度，而不是框架生命周期。

Execution orchestration / control plane is also orthogonal. It may start, route, pause, resume, or retry work, but it does not own or transform Intent, architecture, verification/eval semantics, material Graph, or artifact authority.

There is no independent `Goal` layer. Durable intent is expressed directly as Problem / Draft / Constraints / Acceptance / Decisions / Evidence when needed.

Breaking semantic migrations are recorded in [`CHANGELOG.md`](CHANGELOG.md), including removed surfaces, successor owners, and intentionally retired semantics. The changelog is historical context; runtime truth remains in `AGENTS.md`, each `SKILL.md`, and focused evals.

## Artifacts

- **Drafted Issue** — durable carrier for Northstar Intent / intended change.
- **PR** — realized Change / Delivery；implementation How、diff、implementation-local validation 与 review 默认留在这里。
- **Beacon artifact** — a minimal, repo-grounded core prototype of a bounded feature intent or fault, normally disposable. An interface/usage sketch, representative behavior, minimal implementation, or reproducer may express the core. The prototype and supporting correction / Evidence return to the caller; adoption, comparison, composition, and persistence remain there.
- **Architecture handoff** — only when a durable structural handoff is independently useful; otherwise structural decisions fold back to the caller / Issue.
- **Verify result** — Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing. It normally stays with the PR/review/verification surface unless it changes durable Intent or Architecture.
- **Eval artifact** — Capability/failure + Task + Environment + Verifier + backend binding + Run Evidence/Trajectory + measurement status. It belongs under `evals/` or the project's existing eval surface, not in canonical Intent or product verification state.

## Verification model

Verify follows a simple rule: define the finish/safety claim first, then prove the real artifact rather than a proxy. Existing project harnesses are preferred over inventing new verifier workflows. If required proof cannot run or source identity is not trustworthy, the correct result is `unproven`, not a confident PASS.

For behavior-preserving migration/refactoring, pin an authoritative baseline/oracle and compare the same inputs/config against the candidate. For replacement, also prove adoption and legacy residue. For performance, compare aligned workloads. For architecture, AE defines the Target and Verify checks already-adopted structural claims using direct owner/dependency/authority facts.

## Eval model

Eval measures **agent behavior**, not product correctness. It starts by mapping the actual agent surface—prompts/instructions, models, tools/permissions, Skills/hooks, repo/data/services—and mines available traces for recurring request shapes, tool failures, incorrect state changes, false claims, or other material behavior. Traces are observations, not automatic golden answers.

A stable executable eval is modeled as:

```text
Task
 + Environment
 + Verifier
 + Run Evidence / Trajectory
```

Task should be organic and not leak the rubric or expected Skill route. Environment should reproduce only the tool/data/permission/state semantics that drive the target behavior; expensive or destructive production dependencies may be simulated when their relevant contract is preserved. Verifier prefers deterministic state/artifact/tool-call checks and uses an independent semantic judge only where needed. Candidate self-report never proves an action occurred.

After each run, inspect **both** the agent trajectory and verifier Evidence/trajectory. If the measurement is broken or reward-hackable, fix the eval before changing the runtime Skill/prompt. One-shot PASS is smoke; stochastic behavior or behavior-uplift claims require repeated, preferably blinded comparisons with run identity pinned.

## Loop

Research、execution、review 和 Verify 都可能产生 new verified engineering Evidence。Evidence 只重开真正受影响的 owner：Intent premise 回 Northstar，长期结构 fork 回 Architecture Evolution，factual uncertainty 回 Unknowns First；当一个局部功能或故障需要核心原型、或已有原型需修订时，可 model-invoke Beacon 并只处理对应 local surface；复杂 material work/dependency 变化但 Intent 仍成立时，只重算 Northstar material graph 的 affected cone。

Agent improvement 走另一条反馈环：真实 task/trace → Eval → executable measurement → Skill/prompt/tool/harness 改进 → rerun。产品 Replay/test 结果不能替代这条 behavioral loop；Eval measurement 也不能替代产品 Verify。

## Architecture Evolution usage

Use `architecture-evolution` directly when an engineering request or existing Intent creates structural pressure, or when a named subsystem must evolve toward clearer long-term responsibility. A prior Northstar invocation is not required; when a canonical Northstar Intent / Drafted Issue exists, AE treats it as the accepted boundary.

Architecture Evolution first reuses or re-establishes the Target Architecture from current intent + authority + verified reality, then compares Current → Target and converges a focused Program with real exits. Program convenience cannot redefine Target. When structural completion itself is an accepted claim, Verify may check realized owner/dependency/authority facts against the already-adopted Target without redesigning it.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.
