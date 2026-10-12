# Claude Code CLI eval backend

Eval-only backend for paired behavioral smokes. It is not a Skill and does not define what a case measures; cases, rubrics and judging stay with the owning eval.

`claude_cli.py SPEC --out DIR` does the following:
- builds one sanitized workspace per actor from a fixture, installs each arm's Skill sources (a git ref, `WORKTREE` for the working tree, or `NONE` for a no-Skill control) under `skills_dir`, and excludes that directory from git. `skills_dir` defaults to `.agents/skills`; use `.claude/skills` to test native Skill discovery and routing without naming Skills in the prompt;
- locks the rubric by recording its sha256 and a timestamp before launch, and refuses to start without one;
- runs fresh headless `claude -p` actors in parallel, each with its own `TMPDIR`, pre-approved tools, an optional `--disallowedTools` list (for example `Agent` to model no delegation), a budget cap and a timeout;
- keeps the full stream-json transcript per actor;
- separates the main actor from nested subagents (`parent_tool_use_id`), and records the main actor's ordered tool calls (with Read and Skill targets), its synthesis (the longest own text when the final result event is empty), cost, wall time, and product files changed against the pre-run digest;
- for Agent calls, records the parallel batch versus later sequential calls, each subagent's hand-back report, and `synthesis_after_all_candidates`. That field is true only if every batch report reached the model, meaning a turn's `result.origin.senderTaskId` names it, at or before the turn that produced the synthesis. Stream order alone is not used, because result events are flushed in batches.

`--reanalyze --out DIR` recomputes these facts from saved transcripts without running actors.

Spec shape:

```json
{ "model": "sonnet", "skills": ["architecture-evolution", "beacon"],
  "arms": {"base": "<git ref>", "cand": "WORKTREE"},
  "rubric": "path/to/rubric.md", "max_budget_usd": 5, "timeout_s": 1500, "seed": 1,
  "cells": [{"id": "J1", "fixture": "path/to/fixture", "prompt_file": "path/to/prompt.txt",
             "arms": {"base": 2, "cand": 2}, "disallowed_tools": []}] }
```

`{ws}` in a prompt file is replaced by the actor's workspace path. The rubric is never shown to actors. Host-installed Skills with the same names would contaminate arms, so check `~/.claude/skills` first.

Known limits:
- nested subagent events are inside the main transcript, not separate files;
- judging is not automated;
- actors share the host account and network.

`skills` (top level or per cell) may be a map from arm to Skill list, and a cell may set `prompt_files` (arm → prompt file) instead of `prompt_file`, so one arm can get a slash command and another a plain request. A cell may set `env` (extra environment variables for that cell's actors; never `ANTHROPIC_*`, which the actor itself uses) and `followup_files` (later Human turns, each sent with `--resume` into the same session and appended to one transcript).

## Transcript turns

The transcript reader moved into the `retro` Skill, which uses it at runtime: [`skills/retro/scripts/session_turns.py`](../../skills/retro/scripts/session_turns.py). Evals can call it the same way to trace a ledger row to a specific moment; keep raw output local.
