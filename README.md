# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills (currently installs Northstar, Unknowns First, and Architecture Evolution):

```bash
npx skills@latest add feng-y/skill --all
```

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `northstar` — 接住与整形工程 Intent，澄清问题、预期结果、边界与取舍；需要执行交接时编译 Taskbook，执行结果回流时独立判卷。Goal 是被接受的结果，不是必交的独立文件；Graph 只组织 Execution，implementation How 留给 Executor。
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — consume engineering intent or a named scope to judge long-lived responsibilities, boundaries, variation, and dependencies; derive an AI-native Target and, when warranted, a focused Program with structural gain and real exits. No separate Goal document or mandatory Northstar pass is required.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.

## Architecture Evolution usage

Use `architecture-evolution` when engineering intent creates structural pressure, or when a named module/subsystem needs to evolve toward a clearer long-term responsibility. Supply the intended outcome, constraints, and scope in their existing form; a separate Goal artifact is not required. The named module is an investigation scope, not automatically the Target boundary. The Skill grounds the intent in repo reality, derives the capability/module boundary and justified layering/dependency direction, then returns either a local/no-evolution judgment, the decisive missing evidence/choice, or a focused Architecture Program.

```text
Use $architecture-evolution for this intent or related goals: <intent-or-goals>.
Ground them in current repo reality, identify the architecture change pressure, derive the AI-native Target Architecture, and converge the highest-value structural evolution Program without designing implementation How.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; optional examples under `skills/architecture-evolution/references/` illustrate delivery and anti-patterns but do not define a second contract.
