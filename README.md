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

- `prompt-atlas` — English counterpart to Northstar: shape vague or means-heavy input into the Goal the Human actually wants, resolve only the questions that must be settled before execution, then compile and materialize the current Taskbook for a fresh Executor.
- `northstar` — Chinese counterpart to Prompt Atlas: 先把模糊输入收敛成 Human 真正认可的 Goal，只关闭执行前必须关闭的问题，再把当前 Taskbook 交给 fresh Executor；implementation How 保持在 Executor。
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — start from a named module's repo reality, re-identify capability/boundary and stable variation, then converge a Target Architecture and a few concrete structural improvements before implementation design.

## Architecture Evolution usage

Use `architecture-evolution` when a module keeps accumulating structural pressure or its long-term architecture is still unclear. Give the relevant area and the pressure; the Skill grounds the decision in repo reality and returns either a local/no-evolution judgment, the decisive missing evidence/choice, or a compiled Architecture Program.

```text
Use $architecture-evolution on <module-or-capability>.
Given its current pressure and repo reality, decide the target architecture and the highest-value structural improvements worth advancing.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; this README does not duplicate them.
