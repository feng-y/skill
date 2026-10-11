# Claude Code CLI eval backend

Eval-only backend for paired behavioral smokes. It is not a Skill and does not define what a case measures; cases, rubrics and judging stay with the owning eval.

`claude_cli.py SPEC --out DIR` does the following:
- builds one sanitized workspace per actor from a fixture, installs each arm's Skill sources under `.agents/skills/` (a git ref, or `WORKTREE` for the working tree), and excludes `.agents/` from git;
- locks the rubric by recording its sha256 and a timestamp before launch, and refuses to start without one;
- runs fresh headless `claude -p` actors in parallel, each with its own `TMPDIR`, pre-approved tools, an optional `--disallowedTools` list (for example `Agent` to model no delegation), a budget cap and a timeout;
- keeps the full stream-json transcript per actor;
- records the result (falling back to the last assistant text when a background-woken session ends with an empty result event), cost, wall time, the ordered tool-call sequence, Agent calls split into the parallel batch versus later sequential calls, and product files changed against the pre-run digest.

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
- nested subagent transcripts are not captured separately;
- judging is not automated;
- actors share the host account and network.
