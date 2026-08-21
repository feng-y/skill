# skill

Personal agent skills following the [Agent Skills](https://agentskills.io/) directory convention.

## Install

Discover and select skills interactively:

```bash
npx skills@latest add feng-y/skill
```

Install all skills (currently installs Prompt Atlas, Northstar, Unknowns First, and Architecture Evolution):

```bash
npx skills@latest add feng-y/skill --all
```

Prompt Atlas is the English version of Northstar; Northstar is the Chinese version of Prompt Atlas. They should behave the same, so changes to one should be mirrored to the other unless the difference is purely language-specific. Since they cover the same tasks, install the language surface you want unless you are explicitly comparing them.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — English counterpart to Northstar: take Human intent, close only ambiguity that can change the executable contract, then compile that contract for a fresh Executor while leaving implementation How open; Graph structures the Execution portion only.
- `northstar` — Chinese counterpart to Prompt Atlas: 接住 Human intent，只关闭会改变 executable contract 的歧义，再编译成 fresh Executor 可直接推进并证明完成的 executable Taskbook；Graph 只组织 Execution，implementation How 仍由 Executor 决定。
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — take one goal, several related goals, or a named scope; recover their real architecture change pressure from repo reality, then design an AI-native Target with cohesive responsibility, justified internal variation/layering, stable one-way dependencies, smaller cross-boundary change/verification surfaces, and a focused structural evolution Program with real exits.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.

## Architecture Evolution usage

Use `architecture-evolution` when one or more goals create structural pressure, or when a named module/subsystem needs to evolve toward a clearer long-term responsibility. The named module is an investigation scope, not automatically the Target boundary. The Skill grounds the goals in repo reality, derives the capability/module boundary and justified layering/dependency direction, then returns either a local/no-evolution judgment, the decisive missing evidence/choice, or a focused Architecture Program.

```text
Use $architecture-evolution for these goals: <goal-or-related-goals>.
Ground them in current repo reality, identify the architecture change pressure, derive the AI-native Target Architecture, and converge the highest-value structural evolution Program without designing implementation How.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; optional examples under `skills/architecture-evolution/references/` illustrate delivery and anti-patterns but do not define a second contract.
