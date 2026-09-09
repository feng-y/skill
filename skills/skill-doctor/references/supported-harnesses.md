# Supported harnesses

This adapted Skill Doctor currently reads local **Codex** and **Claude Code** history. The Warp upstream also supports additional harnesses; they are intentionally not claimed here until the local collector implements them.

| Harness | Collector ID | Local source |
| --- | --- | --- |
| Codex | `codex` | `~/.codex/sessions/**/rollout-*.jsonl` and `~/.codex/archived_sessions/**/rollout-*.jsonl` |
| Claude Code | `claude` | `~/.claude/projects/*/*.jsonl`; optional subagents under `subagents/` |

At startup, identify the harness from runtime context, not by guessing from files that happen to exist. If the current harness is neither Codex nor Claude Code, do not read conversation history.

Project skills are discovered from `skills/`, `.agents/skills/`, `.codex/skills/`, and `.claude/skills/`. Global skills are included only when explicitly requested.
