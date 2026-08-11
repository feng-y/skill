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

Prompt Atlas and Northstar are two language surfaces of the same Skill semantics: **Prompt Atlas is the English version and Northstar is the Chinese version**. Their runtime model, decision boundaries, taskbook semantics, Verification/Evidence behavior, and eval cases should remain behaviorally aligned; changes to one should be synchronized to the other unless the difference is purely language-specific. Because their invocation territory overlaps, install the language surface you want to use unless you are explicitly comparing the two.

Install one skill:

```bash
npx skills@latest add feng-y/skill --skill prompt-atlas
npx skills@latest add feng-y/skill --skill northstar
npx skills@latest add feng-y/skill --skill unknowns-first
npx skills@latest add feng-y/skill --skill architecture-evolution
```

## Skills

- `prompt-atlas` — English surface of the shared Northstar semantics: shape a problem space into a stable Goal, route Unknowns to the right authority, then compile a minimum-sufficient task definition or autonomous handoff.
- `northstar` — Chinese surface of the same Intent Take / Shape + Unknown-routing semantics; Human owns outcome, repo/runtime closes facts, and implementation How stays with the Executor.
- `unknowns-first` — expose the first map-versus-territory gap and close it with the smallest useful probe, question, or verification step.
- `architecture-evolution` — start from a named module's repo reality, re-identify capability/boundary and stable variation, then converge a Target Architecture and a few concrete structural improvements before implementation design.

## Architecture Evolution usage

Use `architecture-evolution` when a module keeps accumulating structural pressure or its long-term architecture is still unclear. Give the relevant area and the pressure; the Skill grounds the decision in repo reality and returns either a local/no-evolution judgment, the decisive missing evidence/choice, or a compiled Architecture Program.

```text
Use $architecture-evolution on <module-or-capability>.
Given its current pressure and repo reality, decide the target architecture and the highest-value structural improvements worth advancing.
```

The authoritative runtime semantics live in [`skills/architecture-evolution/SKILL.md`](skills/architecture-evolution/SKILL.md) and its routed references; this README does not duplicate them.
