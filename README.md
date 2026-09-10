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
npx skills@latest add feng-y/skill --skill replay
npx skills@latest add feng-y/skill --skill unknowns-first
```

## Skills

- `northstar` — canonical engineering-intent skill. 把 conversation / request / incident 收敛成 durable Intent；需要跨 session / agent / MultiCA 流转时 materialize 为 Drafted Issue。Issue 是 Intent carrier，不是独立 Skill。
- `prototype` — concrete-shaping specialist. Intent 已理解但具体 Target 仍可能 materially different 时，用最便宜的 Core Path / Usage / disposable Prototype 暴露差异并返回 correction / Evidence。
- `architecture-evolution` — long-term Target Architecture judgment + Current → Target structural Evolution Program。Target 与 Program 是两层不同 judgment，但由一个外部 Skill 承担。
- `replay` — verification / outcome owner. 从 authoritative Acceptance / Constraints 出发，选择并核实 test/replay/runtime Evidence，判断 proven / false / unproven，并把问题路由给正确 owner。
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification-relevant Evidence step.

## Capability flow

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
       Human / Agent / MultiCA
              ↓
              PR
              ↓
            replay
       ┌──────┼────────────────┐
       │      │                │
       ▼      ▼                ▼
   Executor  northstar  architecture-evolution
     fix     intent fix   structural fork
```

Northstar owns **meaning**; Replay owns **verification**. Prototype makes understood Intent inspectable; Architecture Evolution resolves long-term structure and current structural evolution; Unknowns First resolves territory uncertainty.

There is no independent `Goal` layer. Durable intent is expressed directly as Problem / Draft / Constraints / Acceptance / Decisions / Evidence when needed.

## Artifacts

- **Drafted Issue** — durable carrier for Northstar Intent / intended change.
- **PR** — realized Change / Delivery; implementation How, diff and review stay here by default.
- **Prototype artifact** — reaction surface, normally disposable; durable correction returns to the caller.
- **Replay result** — claim judgment + Evidence basis + owner routing, not a repair planner or execution manager.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.

## Architecture Evolution usage

Use `architecture-evolution` when current Intent creates structural pressure or when a named subsystem must evolve toward clearer long-term responsibility. The named module is an investigation scope, not automatically the Target boundary.

Architecture Evolution first reuses or re-establishes the Target Architecture from Intent + authority + verified reality, then compares Current → Target and converges a focused Program with real exits. Program convenience cannot redefine Target, and Replay green cannot by itself prove architecture improvement.
