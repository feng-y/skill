# Objective trigger for the independent judge — J1 smoke (2026-10-11)

Backend: `evals/harness/claude_cli.py` with headless sonnet actors, fresh context and the Agent tool available. Fixture `notify` 2.2.0 includes the platform-owned durable job queue. The request asks for a concrete comparison between building deferred delivery on the shared queue and a notification-owned outbox. In **J1** the caller marks it high-risk ("billing receipts are legally required"). **J0** removes that sentence. Rubrics were locked by sha256 before each launch.

| Run | Arm | Parallel independent candidates | Independent judge | Notes |
| --- | --- | --- | --- | --- |
| round 4 | main `69beac7` ×2 | 2/2 | **0/2** | Both wrote "I did not run an independent judge" and offered a second opinion only if asked. The stated reason was that the Evidence was observed, not taste. |
| round 4b | main `69beac7` ×1 | 1/1 | **0/1** | Reproduces the gap (0/3 overall). |
| round 4b | fix ×2 | 2/2 | **2/2** | The judge ran after the candidates returned. One actor rejected the judge's hybrid (outbox plus queue as a wake-up) with an Evidence reason: the two stores cannot be written atomically. |
| round 4b | fix, J0 ×1 | 1/1 | 0/1 | The judge remains AE's call without high-risk marking. No over-use cost. |

All workspaces had zero product-file changes. Costs ran $0.39–0.55 per actor. Two actors took about 21 minutes of wall time while waiting on background candidates.

**Fix.** The rule used to trigger on "比较风险高或 AE 自评偏差 material", which left room for self-exemption. It now triggers objectively when the caller or Human marks the comparison high-risk, or when its result directly supports merge, ship, rollout or another irreversible decision. Observed Evidence or a clear-looking conclusion is explicitly not a reason to skip. Other comparisons keep the judge at AE's discretion, and the no-context degradation path is unchanged.

**Side observation, not addressed here.** In J0 the actor drafted its recommendation while one candidate was still running, then said the late notification changed nothing. Whether synthesis waited for all candidates cannot be confirmed from the transcript, so this is a possible premature-synthesis risk to watch.

**Limits.** n = 2–3 per arm, unblinded parent review, synthetic fixture. This shows the trigger now fires; it does not show that judged comparisons choose better.
