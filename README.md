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
npx skills@latest add feng-y/skill --skill evidence
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `northstar` — canonical engineering-intent skill. 把 conversation / request / incident 收敛成 durable Intent；需要跨 session / agent / Human 或执行环境流转时 materialize 为 Drafted Issue。Issue 是 Intent carrier，不是独立 Skill。
- `prototype` — concrete-shaping specialist. Intent 已理解但具体 Target 仍可能 materially different 时，用最便宜的 Core Path / Usage / disposable Prototype 暴露差异并返回 correction / Evidence。
- `architecture-evolution` — long-term Target Architecture judgment + Current → Target structural Evolution Program。Target 与 Program 是两层不同 judgment，但由一个外部 Skill 承担。
- `evidence` — engineering proof specialist. 从 authoritative completion/safety claim 出发定义 proof obligation，选择最直接的 real-artifact Evidence 与合适 verifier/backend，并判断 proven / false / unproven。
- `unknowns-first` — factual map-versus-territory specialist. 只关闭会改变下一步判断的 repo/runtime/data/source fact，不接管 Intent、Prototype、Architecture 或 proof judgment。

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
   │          │                  │
   └──────────┴──────────────────┘
              ↓
         Drafted Issue
              ↓
          execution
              ↓
              PR

Northstar / AE accepted claims
              ↓
           evidence
      proof obligation
              ↓
   verification backend(s)
 test / build / project harness / runtime / data
              ↓
           evidence
    proven / false / unproven
              ↓
  affected semantic owner / Executor
```

Northstar owns **meaning**. Prototype owns **concrete reaction surfaces**. Architecture Evolution owns **structural judgment**. Unknowns First owns **factual uncertainty**. Evidence owns **proof semantics and sufficiency judgment**.

Verification executors are orthogonal to this capability map. A project may use tests, build, integration harnesses, runtime probes, data checks, profiles, or project-specific systems. **DaVinci harness Replay is one such executable verification backend; it is not a Skill or semantic owner in this repo.**

Execution orchestration / control plane is also orthogonal. It may start, route, pause, resume, or retry work, but it does not own or transform Intent, architecture, Evidence semantics, material Graph, or artifact authority.

There is no independent `Goal` layer. Durable intent is expressed directly as Problem / Draft / Constraints / Acceptance / Decisions / Evidence when needed.

Breaking semantic migrations are recorded in [`CHANGELOG.md`](CHANGELOG.md), including removed surfaces, successor owners, and intentionally retired semantics. The changelog is historical context; runtime truth remains in `AGENTS.md`, each `SKILL.md`, and focused evals.

## Artifacts

- **Drafted Issue** — durable carrier for Northstar Intent / intended change.
- **PR** — realized Change / Delivery; implementation How、diff、implementation-local validation 与 review 默认留在这里。
- **Prototype artifact** — reaction surface, normally disposable; durable correction returns to the caller.
- **Architecture handoff** — only when a durable structural handoff is independently useful; otherwise structural decisions fold back to the caller / Issue.
- **Evidence result** — Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing. It is not a repair planner or execution manager.

## Proof model

Evidence follows a simple rule: define the finish/safety claim first, then prove the real artifact rather than a proxy. Existing project harnesses are preferred over inventing new verifier workflows. If required proof cannot run or source identity is not trustworthy, the correct result is `unproven`, not a confident PASS.

For behavior-preserving migration/refactoring, pin an authoritative baseline/oracle and compare the same inputs/config against the candidate. For replacement, also prove adoption and legacy residue. For performance, compare aligned workloads. For architecture, AE defines the Target and Evidence proves already-adopted structural claims using direct owner/dependency/authority facts.

## Loop

Research、execution、review 和 Evidence verification 都可能产生新 verified Evidence。Evidence 只重开真正受影响的 owner：Intent premise 回 Northstar，concrete-shape ambiguity 回 Prototype，长期结构 fork 回 Architecture Evolution，factual uncertainty 回 Unknowns First；复杂 material work/dependency 变化但 Intent 仍成立时，只重算 Northstar material graph 的 affected cone。

## Architecture Evolution usage

Use `architecture-evolution` directly when an engineering request or existing Intent creates structural pressure, or when a named subsystem must evolve toward clearer long-term responsibility. A prior Northstar invocation is not required; when a canonical Northstar Intent / Drafted Issue exists, AE treats it as the accepted boundary.

Architecture Evolution first reuses or re-establishes the Target Architecture from current intent + authority + verified reality, then compares Current → Target and converges a focused Program with real exits. Program convenience cannot redefine Target. When structural completion itself is an accepted claim, Evidence may verify realized owner/dependency/authority facts against the already-adopted Target without redesigning it.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.
