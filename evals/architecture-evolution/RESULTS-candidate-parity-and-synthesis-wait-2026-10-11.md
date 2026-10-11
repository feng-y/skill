# Candidate parity and synthesis wait — AE smoke (2026-10-11)

Backend: `evals/harness/claude_cli.py`, headless sonnet actors. Fixture and request are the J1 high-risk explicit comparison from [the judge-trigger results](RESULTS-objective-judge-trigger-2026-10-11.md).

## Does AE wait for every candidate before synthesizing?

The earlier J0 report raised this as a possible risk. It was ruled out by re-analyzing all 6 round-4/4b AE transcripts. A report has reached the model only when a turn-ending `result` event names that subagent in `origin.senderTaskId`; stream order of `task_notification` events is not enough, because result events are flushed in batches. The synthesis turn, matched by its result text, came after every candidate report in 6/6 runs, and after the judge report as well where a judge ran. In the flagged J0 run, the synthesis turn was itself triggered by the second candidate's report. Its low reuse of that candidate's identifiers reflects that it recommended the other option, not that it missed the report.

## Candidate parity

The same re-analysis found 1/6 runs where AE gave the parallel candidates unequal models: `sonnet` at low effort versus `haiku`, with an `opus` judge. The rule "可用时给每个候选不同的设计约束或模型" did not require comparable strength, so the comparison could reflect generation capacity instead of design. The rule now allows different design constraints or different models of comparable capability, with equal model strength and effort.

Regression run with the fix (WORKTREE ×3, rubric locked before launch):

| Check | Result |
| --- | --- |
| Parallel independent candidates | 3/3 |
| Candidate models / effort | 3/3 equal (inherit) |
| Independent judge after candidates | 3/3 (one judge on opus; the candidates themselves were equal) |
| Synthesis after every candidate and judge report | 3/3 |
| Product files changed | 0 |

Each run cost $0.51–0.68. Wall time was 149–1329s; one actor waited about 22 minutes on background reports.

**Limits.** With a 1/6 base rate, three clean runs are a regression check and do not prove the fix; the evidence is the wording invariant plus no regression. n is small, review was unblinded, and the fixture is synthetic.
