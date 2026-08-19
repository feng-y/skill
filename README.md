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

- `prompt-atlas` — English counterpart to Northstar: shape Human intent into the right Goal, preserve Executor judgment, and compile a high-altitude Taskbook whose successful delivery is materialized to an authoritative external Markdown file.
- `northstar` — Chinese counterpart to Prompt Atlas. It probes reality before asking, resumes after Human clarification or interruption, keeps implementation How with the Executor, and separates how work is organized from how completion is proven.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — start from a named module's repo reality, re-identify capability/boundary and stable variation, then converge a Target Architecture, identify high-value evolution anchors, and concentrate the current structural move before implementation design.

## Runtime tools

- [`rdr`](rdr/) — Remote Diagnostic Runtime. A separate Python runtime, not an Agent Skill and not installed by `skills`. It gives development-side agents local-like remote shell, PTY, signal, and file-transfer access to a target runtime when SSH is unavailable; all AI reasoning remains on the development side.

## Architecture Evolution usage

Use `architecture-evolution` when a module keeps accumulating structural pressure or its long-term architecture is still unclear. Give the relevant area and the pressure; the Skill grounds the decision in repo reality and returns either a local/no-evolution judgment, the decisive missing evidence/choice, or a focused Architecture Program.

```text
Use $architecture-evolution on <module-or-capability>.
Given its current pressure and repo reality, decide the target architecture, identify the highest-value evolution anchors, and converge the current structural move worth advancing.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; this README does not duplicate them.
