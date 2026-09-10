# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills (currently installs Issue Shape, Northstar, Unknowns First, Intent Shape, Architecture Evolution, and Architecture Shape):

```bash
npx skills@latest add feng-y/skill --all
```

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill issue-shape
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill intent-shape
npx skills@latest add feng-y/skill --skill architecture-evolution
npx skills@latest add feng-y/skill --skill architecture-shape
```

## Skills

- `issue-shape` — 把 current conversation / external request 编译成可独立流转的 Drafted Issue。Issue body 保存当前 canonical intended change；按需调用 specialist，并把 durable correction / Evidence / Decision fold back 到同一个 Issue。
- `northstar` — optional difficult-intent compiler / outcome judge；只在 Drafted Issue 仍存在 binding interpretation、Human-owned trade-off、复杂 material delta / dependency 等无法局部关闭的问题时介入，clear Issue 可以直接执行。
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `intent-shape` — caller-neutral concrete-shaping specialist that makes an already-understood but still materially ambiguous Target inspectable through the cheapest Core Path / Usage / Prototype, then returns correction and Evidence without owning the canonical Issue.
- `architecture-evolution` — use an existing Target Architecture, or model-invoke `architecture-shape` when it is missing/stale, then compare current reality with Target and converge the highest-leverage structural Evolution Program with real exits.
- `architecture-shape` — Architecture Evolution model-invoked specialist that derives the long-term Target Architecture from Goal pressure, verified reality, responsibility/knowledge ownership, justified variation and stable dependency direction; it does not choose the current evolution Program.

## Drafted Issue flow

`issue-shape` is the normal artifact entry when engineering intent needs to leave the current conversation:

```text
conversation / external intent
        ↓
    issue-shape
        ↓
   Drafted Issue
   ├─ direct agent
   ├─ MultiCA / coordinator
   └─ northstar only when difficult intent earns it
```

A Drafted Issue should stay useful without the original conversation, Northstar, or a specific execution platform. `intent-shape`, `unknowns-first`, and architecture skills are specialists; their durable results fold back into the same Issue instead of creating parallel intent/spec/plan SOTs. PR remains the realized Change / Delivery surface for implementation, validation, and review.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.

## Architecture Evolution usage

Use `architecture-evolution` when existing intent or related goals create structural pressure, or when a named module/subsystem needs to evolve toward a clearer long-term responsibility. A separate Goal document or prior Northstar invocation is not required. If a still-valid Target Architecture already exists, AE reuses it; if Target is missing or a material premise has changed, AE model-invokes `architecture-shape` to re-establish the Target before choosing the current Program. The named module remains an investigation scope, not automatically the Target boundary.

```text
Use $architecture-evolution for these goals: <goal-or-related-goals>.
Ground current reality, reuse or re-establish the Target Architecture, then converge the highest-value structural Evolution Program and real exits without designing implementation How.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md). Long-term Target judgment is owned by [`skills/architecture-shape/SKILL.md`](skills/architecture-shape/SKILL.md); Architecture Evolution consumes that result rather than maintaining a second Target-design contract.
