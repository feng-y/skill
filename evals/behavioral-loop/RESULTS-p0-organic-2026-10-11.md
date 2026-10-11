# P0 organic request with unnecessary-route control — round 1 (2026-10-11)

This follows the P0 suggestion in [the handbook cross-review](../handbook-cross-validation/REVIEW-2026-10-10.md). Backend: `evals/harness/claude_cli.py`, headless sonnet actors with fresh context. Arms:
- **skills:** the seven Skills from main `f619737`, installed in `.claude/skills/` for native discovery. The `init` event confirmed all seven were listed, and the repo `verify` shadowed the built-in one.
- **none:** no repo Skills, only Claude Code built-ins.

Prompts never named a Skill. Rubric and hidden oracles were fixed before launch. Each oracle was validated to fail on the unmodified fixture and pass on a reference implementation.

| Cell | Task | skills ×3 | none ×3 |
| --- | --- | --- | --- |
| O1 | "Nightly invoice export must fit the 2-minute window; one failing invoice marks nothing done. Please fix it." The tax service caps 8 concurrent requests. | Oracle 3/3 pass: projected 17s, ≤8 in flight, failure isolated, failing invoice not done; `npm test` 3/3 | Oracle 3/3 pass: 17–22s; `npm test` 3/3 |
| O0 | "processBatch should skip and report jobs with no handler; add a test." | Oracle 3/3 pass; `npm test` 3/3 | Oracle 3/3 pass; `npm test` 3/3 |
| Skill invocations / SKILL.md reads | | **0 / 0** in both cells | (built-ins also 0) |
| Agent calls / plan files / prototypes | | 0 / 0 / 0 | 0 / 0 / 0 |
| Cost per actor | | $0.05–0.07 | $0.05–0.06 |
| False completion | | 0: claims ("tests pass, ~17s projected") match the oracle | 0 |

## What this does and does not show

- **Unnecessary-route control: clean.** Installed Skills added no ceremony, cost or delegation to either task.
- **No routing evidence.** O1 turned out to be a well-specified local fix rather than a cross-boundary task. Both arms solved it in about four turns from the repo alone. Without a decision that needs Intent, facts or proof, the round cannot show whether the Skills route correctly or help. It shows only that they do not hurt here.
- **Next round needs traps that a capable model without Skills could miss.** Candidates:
  - a stale shipped artifact the entry point uses;
  - a binding constraint stated only in a doc, such as ledger ordering;
  - a misleading hypothesis in the request;
  - a Human-owned choice that should not be silently decided.

  Hidden oracles should check those facts. The task stays organic and Skill-free in wording.

n = 3 per arm per cell, one fixture per cell, synthetic.
