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
npx skills@latest add feng-y/skill --skill prototype
npx skills@latest add feng-y/skill --skill architecture-evolution
npx skills@latest add feng-y/skill --skill verify
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `northstar` — canonical engineering-intent skill. 把 conversation / request / incident 收敛成 durable Intent；需要跨 session / agent / Human 或执行环境流转时 materialize 为 Drafted Issue。Issue 是 Intent carrier，不是独立 Skill。
- `prototype` — caller-neutral、主要由 model 按需调用的 concrete-shaping specialist. 当前 caller 已理解自己的语义，但具体 path / usage / interface / interaction 仍可能 materially different 时，用最便宜的 Core Path / Usage / disposable Prototype 暴露差异，再把 correction / Evidence 返回原 caller。
- `architecture-evolution` — long-term Target Architecture judgment + Current → Target structural Evolution Program。Target 与 Program 是两层不同 judgment，但由一个外部 Skill 承担。
- `verify` — engineering verification skill. 从 authoritative completion/safety claim 出发定义 proof obligation，选择并驱动最直接的 real-artifact verification backend，收集 Evidence 并判断 proven / false / unproven。
- `unknowns-first` — factual map-versus-territory specialist. 只关闭会改变下一步判断的 repo/runtime/data/source fact，不接管 Intent、Prototype、Architecture 或 proof judgment。

## Invocation model

主要 Human-facing / direct capabilities：

- `northstar` — “我们到底要什么？”
- `architecture-evolution` — “长期结构应该怎么归位？”
- `verify` — “结果是否真的符合 claim？”

主要 model-invoked specialists：

- `prototype` — 当前 caller 已理解语义，但需要把 concrete shape 变得可观察；Human 很少需要主动调度。
- `unknowns-first` — 当前判断依赖未核实事实时自动/按需关闭 factual gap；Human 也可以直接要求先查事实。

`prototype` **不属于 Northstar 私有流程**。Northstar、Architecture Evolution、Verify、Unknowns First 或其他 semantic caller 都可以在遇到 material concrete-shape ambiguity 时调用它；Prototype 返回后，原 caller 继续拥有自己的 judgment。

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
prototype  architecture-evolution  unknowns-first
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
              ├── concrete observable shape unclear → prototype
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
```

Northstar owns **meaning**. Prototype owns **concrete reaction surfaces only** and returns them to its caller. Architecture Evolution owns **structural judgment**. Unknowns First owns **factual uncertainty**. Verify owns **verification / proof judgment**; Evidence is its proof artifact and basis.

Verify is not a mandatory post-PR stage. It may be invoked before implementation to make a material proof route explicit, during implementation when verification premises change, or after implementation to judge realized results. Clear local changes can rely on an already-authoritative focused check without extra ceremony.

Verification backends are orthogonal to this capability map. A project may use tests, build, integration harnesses, runtime probes, data checks, profiles, or project-specific systems. **DaVinci harness Replay is one such executable verification backend; it is not a Skill or semantic owner in this repo.** If a backend already owns Launch / Doctor / Drive / Capture / Cleanup, Verify follows that contract rather than recreating a second harness lifecycle.

Execution orchestration / control plane is also orthogonal. It may start, route, pause, resume, or retry work, but it does not own or transform Intent, architecture, verification semantics, material Graph, or artifact authority.

There is no independent `Goal` layer. Durable intent is expressed directly as Problem / Draft / Constraints / Acceptance / Decisions / Evidence when needed.

Breaking semantic migrations are recorded in [`CHANGELOG.md`](CHANGELOG.md), including removed surfaces, successor owners, and intentionally retired semantics. The changelog is historical context; runtime truth remains in `AGENTS.md`, each `SKILL.md`, and focused evals.

## Artifacts

- **Drafted Issue** — durable carrier for Northstar Intent / intended change.
- **PR** — realized Change / Delivery; implementation How、diff、implementation-local validation 与 review 默认留在这里。
- **Prototype artifact** — reaction surface, normally disposable; correction / Evidence returns to the caller, which decides whether anything durable should be persisted.
- **Architecture handoff** — only when a durable structural handoff is independently useful; otherwise structural decisions fold back to the caller / Issue.
- **Verify result** — Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing. It normally stays with the PR/review/verification surface unless it changes durable Intent or Architecture.

## Verification model

Verify follows a simple rule: define the finish/safety claim first, then prove the real artifact rather than a proxy. Existing project harnesses are preferred over inventing new verifier workflows. If required proof cannot run or source identity is not trustworthy, the correct result is `unproven`, not a confident PASS.

For behavior-preserving migration/refactoring, pin an authoritative baseline/oracle and compare the same inputs/config against the candidate. For replacement, also prove adoption and legacy residue. For performance, compare aligned workloads. For architecture, AE defines the Target and Verify checks already-adopted structural claims using direct owner/dependency/authority facts.

## Loop

Research、execution、review 和 Verify 都可能产生 new verified Evidence。Evidence 只重开真正受影响的 owner：Intent premise 回 Northstar，长期结构 fork 回 Architecture Evolution，factual uncertainty 回 Unknowns First；当任一 caller 已理解语义但 concrete shape 又变得 materially ambiguous 时，可 model-invoke Prototype 并只重开对应 shape surface；复杂 material work/dependency 变化但 Intent 仍成立时，只重算 Northstar material graph 的 affected cone。

## Architecture Evolution usage

Use `architecture-evolution` directly when an engineering request or existing Intent creates structural pressure, or when a named subsystem must evolve toward clearer long-term responsibility. A prior Northstar invocation is not required; when a canonical Northstar Intent / Drafted Issue exists, AE treats it as the accepted boundary.

Architecture Evolution first reuses or re-establishes the Target Architecture from current intent + authority + verified reality, then compares Current → Target and converges a focused Program with real exits. Program convenience cannot redefine Target. When structural completion itself is an accepted claim, Verify may check realized owner/dependency/authority facts against the already-adopted Target without redesigning it.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.
