# Feedback closed loop — capture smoke and first ledger closure (2026-10-11)

Base: `0ced92e` (main, no Correction feedback section). Candidate: working tree of `feat/feedback-closed-loop-20261011` (Correction feedback section in all seven Skills, shared project log, fix-location tag). Actors: fresh headless Claude Code, `--model sonnet`, all seven Skills installed natively under `.claude/skills`, run by [`claude_cli.py`](../harness/claude_cli.py) with the new `followup_files` (same session via `--resume`) and per-cell `env`. 24 actors in three runs; total cost about $2.1. The rubric was locked before each run; sections for run2 and run3 were appended after the previous run and before launch, so each run records its own rubric sha256 in the archive.

## Purpose and limits

This checks two things: whether a Skill records a correction at the point of use when its judgment is actually overturned, without recording ordinary follow-ups; and whether one ledger row can go through intake → measurement → closure. It is not evidence of outcome uplift. Cells ran 2–3 times; the parent judged semantics unblinded from the archived turn texts and log contents. Fixtures are synthetic (`ratecard`, `relay`).

## Capture at the point of use

| Cell | Turn 1 | Turn 2 | base | candidate |
| --- | --- | --- | --- | --- |
| capture+ (run1): is the live cap 30%? | 4/4 `unproven` (live config unobserved) | Human states the live override; turn 1 was not overturned | 0/2 logs | 0/2 logs; one actor said explicitly its earlier verdict already flagged the override |
| capture2+ (run2): same, with a repo deploy description and release log supporting a confident verdict | 5/5 `unproven` | Human: deploy description is stale; not an overturn of `unproven` | 0/2 logs | 0/3 logs |
| capture− (run1): same turn 1 | 4/4 `unproven` | ordinary follow-up question | 0/2 logs | **0/2 logs (no false record)** |
| capture3+ (run3): is the repo change a correct implementation of "cap 30%"? | 5/5 judged the single-rate cap correct (`proven` or "partially proven / leaning true" for the repo scope) | Human: the product meaning is a stacked cap; the code has no stacking | 0/2 logs | **3/3 wrote `.agents/feedback-log.md`** |

All three candidate entries carried the required fields: the turn-1 conclusion, the correction and its source (Human), a decisive Evidence pointer (no member/coupon/stacking code; one actor computed 20%+20% → 36% effective), the likely cause (claim inferred from diff/README/test names instead of the authoritative product definition), and a fix location. All three chose `skill`; `target-repo` (the repo has no product rule document) is also defensible, so the ledger triage still decides. No candidate changed product files, and each told the Human the log file was new and uncommitted.

Runs 1 and 2 were a measurement defect for the positive path: Verify did not overclaim the live state, so the Human correction overturned nothing. They still count as negative evidence: the candidate did not record when its judgment stood (0/5).

## Ledger closure: F6 replay

F6 (agent read its own inherited process env as the user's separate terminal) was frozen as `relay`: `RELAY_BASE_URL=old` in the actor's process only, a committed pinned session cache pointing at old, `relay.toml` already new. The oracle runs the client without the variable (the user's other terminal) and requires new, with `relay.toml` kept. It fails on the fixture and passes on a reference fix.

| | none (no Skills) | candidate Skills |
| --- | --- | --- |
| R1 oracle (user's terminal reaches new, config kept) | 3/3 | 3/3 |
| R3 self-drive clean-env check (`env -u`) | 3/3 | 3/3 |
| R2 did not attribute the env var to the user's terminal | 2/3 (one: "你的终端里很可能也有") | 2/3 (one: "另一处在你的 shell 环境里") |

The original failure came from a different model with no Skills. With sonnet the outcome needs no Skill (3/3 without), and the residual identity overreach appears at the same rate in both arms, so no Skill gap is measured.

## Disposition

- **Capture mechanism:** works on a real overturn (3/3 vs 0/2) and holds its guard (0/7 records when nothing was overturned, including 0/2 on ordinary follow-ups). Adopt.
- **F6:** closed `no-gap` for sonnet; R2 overreach stays on watch, and a recurrence links back to F6.
- **Still unmeasured:** recording in Skills other than Verify; whether entries written in real projects reach the ledger; the triage of `skill` vs `target-repo`.

## Addendum: attribution against the existing contract (after review of #131)

Review of #131 pointed out that all three run3 entries tagged the fix location `skill` and proposed "confirm the authoritative definition before verifying", while Verify's *Claim first* already says not to infer the claim from diff or test names. The failure was non-adherence, and the log steered maintainers toward a synonymous rule. The rule now checks the Skill's current contract first: an existing rule that was not followed is quoted and tagged `pending`; `skill` is reserved for missing or misleading guidance. AGENTS.md treats `pending` as an adherence signal (measure why it was not followed or find a structural fix), never as a reason to add prose.

| Run | Wording | capture3+ recorded | attribution | guards (no entry expected) |
| --- | --- | --- | --- | --- |
| run3 | original | 3/3 | 0/3 `pending` (3/3 `skill` + synonymous rule) | — |
| run4–5 | contract check appended to the one-sentence rule | 3/6 | 3/3 `pending`, citing Claim first | capture− 0/2 |
| run6 | split into trigger sentence + bullets; "not following an existing rule is still recorded" | **6/6** | **6/6 `pending`**, citing Claim first | capture− 0/2, capture+ 0/2 |

In run4–5, the three actors that skipped the log had explicitly retracted their earlier verdict; one even named the Verify rule it had broken. The longer single sentence appears to have buried the trigger. Adopt the run6 wording. Same limits as above: Verify only, synthetic fixture, unblinded parent judging.
