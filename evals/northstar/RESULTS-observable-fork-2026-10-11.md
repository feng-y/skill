# Northstar observable fork vs Human preference — N1 smoke (2026-10-11)

This checks the #128 Northstar sentence: a fork whose answer can be observed by running goes to Beacon variants rather than to the Human, while experience or preference stays with the Human.

Fixture: a job runner whose nightly invoice export must fit a 2-minute window. A sequential run projects to about 138s, and the tax service caps concurrency at 8. One failing invoice currently aborts all marking. The request was organic and design-only ("work out the plan with me; don't implement it yet"). Backend: `evals/harness/claude_cli.py`, sonnet, base `d1ea3b3` (pre-#128) ×2 versus main `69beac7` ×2.

| Check | base | main |
| --- | --- | --- |
| Observable fork settled from territory, not asked | 2/2 ran `export:sample`, then derived the bounded-concurrency timing arithmetically | 2/2 same |
| Beacon variants used | 0/2 | 0/2 |
| Human-owned policy kept as an explicit Human choice (failed invoice pending vs failed status, alerting, retries) | 2/2 | 2/2 |
| Plan persisted to `.northstar/*.md`, no product edits, no implementation | 2/2 | 2/2 |

Result: no difference. Base already measures technical facts itself and asks only the policy questions. Arithmetic was a reliable discriminator here, so no prototype was needed. The sentence is neither shown useful nor harmful. Revisit only if a trace shows Northstar asking the Human an observable question.
