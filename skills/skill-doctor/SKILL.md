---
name: skill-doctor
description: Grade installed agent skills from recent local Codex or Claude Code conversations, attribute recurring waste or defects to the owning instruction surface, and propose only evidence-backed minimal skill edits. Use when evaluating whether Northstar, Architecture Evolution, or other skills are actually helping in real runs.
---

# Skill Doctor

Adapted from Warp's `skill-doctor` at `warpdotdev/common-skills`. Keep conversation data local. Never upload transcripts, session files, or excerpts to external services. Only the final report or user-approved excerpts may leave the machine.

The core loop is:

`Collect real conversations → Score → Attribute failures → Verify current instructions → Propose the smallest owning edit`

This Skill evaluates behavior, not prose aesthetics. A shorter or more elegant Skill is not an improvement unless real conversations support the claim.

## Start

Identify the executing harness from runtime context. Supported harnesses and local sources are in [supported-harnesses.md](references/supported-harnesses.md). If the harness is unsupported or cannot be identified confidently, stop before reading conversation history.

Choose the narrowest useful conversation scope. If the user already named a repo or skills to evaluate, do not ask again. Otherwise prefer conversations in the current repo; broaden only when the user wants cross-project or global-skill evidence.

Create a scratch report directory outside the repo:

```bash
REPORT_DIR="$(mktemp -d "${TMPDIR:-/tmp}/skill-doctor-XXXXXXXX")"
```

Never write generated reports or proposed edits into the target repo until the user explicitly asks to apply them.

## Collect

Use the local collector:

```bash
python3 "$SKILL_ROOT/scripts/collect_sessions.py" \
  --out "$REPORT_DIR" \
  --repo "$REPO" \
  --skills-dir "$REPO/skills"
```

Useful options:

- `--harness codex|claude|auto`
- repeat `--repo PATH` for multiple projects
- `--all-conversations`
- `--include-global-skills`
- `--days N` (default 45)
- `--max-sessions N` (default 12)
- repeat `--skills-dir PATH` for nonstandard skill roots

Read `inventory.json`. If `sessions_sampled == 0`, do not fabricate a score. State that no qualifying local conversations were available and give the exact collection command needed in the user's real development environment.

## Score

For every sampled transcript, score:

- [Efficiency](scorers/efficiency.md)
- [Code Quality](scorers/code-quality.md) when the transcript contains enough evidence of code changes; otherwise mark `insufficient_evidence`.

For each score record the label, numeric value, and a short reason tied to concrete transcript evidence.

Aggregate using Warp's original weighting:

- `raw_efficiency` = mean efficiency score
- `raw_code_quality` = mean applicable code-quality score; if none applies, report it as insufficient rather than pretending code quality was measured
- report curve for each measured quality score: `curve(x) = 0.5 + 0.5 * x`
- `skill_coverage` = sampled sessions in which at least one installed skill was detected / sampled sessions
- when both quality dimensions are measurable: `overall = 0.5 * efficiency + 0.35 * code_quality + 0.15 * skill_coverage`

Do not hide failed sessions behind averages. A conversation is a `failed_conversation` when any applicable raw efficiency or code-quality score is below `0.5`.

## Attribute before editing

Only `failed_conversations` may justify a Skill change. For each failure:

1. identify the concrete waste or defect;
2. name the likely owning surface: skill trigger, skill runtime instruction, project rule, tool/runtime, model variance, or product/infra;
3. read the current owning instruction before proposing a fix;
4. apply [skill-improvements.md](references/skill-improvements.md).

A failure is not automatically a Skill defect. If the existing instruction already required the correct behavior, or the real fix belongs to runtime/tooling/model variance, do not add another rule.

## Propose improvements

Prioritize root-cause clusters by frequency × severity. Prefer replacing an existing instruction over appending another paragraph. Keep edits small and general; do not encode one transcript's answer as a permanent rule.

For every proposed edit include:

- skill / owning file;
- observed failure pattern and source sessions;
- one reusable behavioral rule the edit would establish;
- why the current instruction is missing/wrong/underspecified;
- unified diff or complete proposed file;
- expected observable metric that should improve on a rerun.

Do not modify real Skill files during grading. Apply edits only after the user asks.

## Report

Write `REPORT_DIR/report.md` and `REPORT_DIR/report.json` with:

- scope, harness, session count, window;
- efficiency / code-quality / skill-coverage measurements;
- three highest-impact findings;
- failed-conversation evidence;
- proposed edits, if any;
- explicit `no_change` findings when evidence does not justify an edit.

Finish with the absolute report path and a short statement of what is measured versus still unproven.
