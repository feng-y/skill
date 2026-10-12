# Retro Skill — paired review of real sessions (2026-10-11)

Base: Skills at `84faa9e` (the seven Skills with #131 Correction feedback, no retro), prompt `复盘这个 session：<transcript>`. Candidate: working tree of `feat/retro-skill-20261011` (Correction feedback retired, `retro` added), prompt `/retro <transcript>`. Both arms install their Skills natively under `.claude/skills`. Actors: fresh headless Claude Code, `--model sonnet`, run by [`claude_cli.py`](../harness/claude_cli.py) with the new per-arm `skills` / `prompt_files`. Rubric and oracle were locked before run1; the run2–run4 sections were appended before each launch. 38 actors, about $6.2 of actor cost. Transcripts, rubric, verdicts and blind keys stay local because the sessions contain private operations context.

## Material

Three real transcripts, one cell each, three actors per arm per run:

| Cell | Session | Rules in effect at the time | Oracle |
|---|---|---|---|
| S | Claude Code, this repo's maintenance (#127–#131) | `CLAUDE.md` → `AGENTS.md` only; no repo Skill invoked | 9 known corrections (ledger F1–F5 sources, the #131 review, credential friction, repeated branch cleanup) |
| C | Codex, configuring a CLI's authentication | none (no repo Skills, no AGENTS.md) | 5 (ledger F6, F10, F13, F14, F15 sources) |
| O | Codex, diagnosing an outage of a self-hosted proxy service | none | 4 (ledger F8, F11, F12, F17 sources) |

The cell S fixture is the `84faa9e` tree with ledger rows removed. Its CHANGELOG and RESULTS still describe some outcomes, and both arms could read them equally.

Judging: per cell, three independent judges each scored six outputs (three per arm) in one blinded, shuffled packet against the oracle. They checked cited lines in the transcript. Base outputs come from run1 and are re-judged in each packet. Judge strictness varied: the same base outputs scored 43, 44 and 38/54 recall across rounds. So compare arms within a round, not across rounds.

## Results

| Measure (54 oracle items per arm per round) | base r1 / r3 / r4 | candidate r1 / r3 / r4 |
|---|---|---|
| Oracle recall | 43 / 44 / 38 | 37 / 38 / **43** |
| Found items given a route in the accept set | 6/43 · 6/44 · 6/38 | 35/37 · 33/38 · 35/43 |
| Wrong `pending` (rule not in effect at that moment) | 4 / 3 / 4 | 0 / 1 / 2 |
| Generic candidates (not tied to a moment) | 6 / 12 / 16 | 0 / 0 / 0 |
| Asked the Human to pick items | 1/9 · 3/9 · 3/9 | 9/9 · 9/9 · 9/9 |
| Files changed in a single-turn review | 0/9 | 0/27 |

Candidate runs differ: r1 used the first wording, r3 a compact transcript listing with a coverage header, and r4 also flagged truncated long turns.

- **Routing is the clear difference.** Base outputs are narrative retrospectives with "next time" advice. They rarely say where a fix belongs, and never separate a project fix from a Skill-system fix. Candidates route 82–95% of the items they find into the accept set and attach a concrete change and a way to confirm it.
- **Recall is at parity, not better.** On the short Codex sessions, the base finds every Human correction (C 15/15 in every round). The candidate's r1 misses came from a measurement-visible defect: the first transcript listing ran to 76 KB, actors read it with `head -300`, and one reviewed lines 5–830 of 3,110. The r3 fix (compact listing) restored coverage, and every candidate stated the line range it read. The candidates still skipped both pasted external reviews, because only the first lines of each were visible. The r4 fix flags truncated turns for a full read, and 2/3 then found the #131 review finding. In r4 the candidate leads 43 to 38; with three actors per arm and noisy judges, that is not a reliable gap.
- **`pending` attribution.** The base claimed `pending` against rules that were not in effect: an uninvoked Skill, and AGENTS.md text added after the correction. The candidate mostly checks what was loaded and says so explicitly ("no rules in effect, so no `pending`"). Its remaining errors are all in cell S, where the repo itself changed after the session: two actors cited current AGENTS.md text, or a clause that does not cover the moment. In the two Codex cells, no candidate ever claimed `pending`.
- **Both arms miss.** Neither arm found the self-retracted premature-synthesis false alarm. Only one actor (a candidate) found the repeated branch-cleanup requests.
- **Approval path (run2, candidate only, 2 actors):** turn 1 wrote nothing. Turn 2 was "only land the skill / pending items". Both actors appended rows to the workspace `LEDGER.md` with disposition `open`, an abstracted shape and a line pointer, and no private context. They changed no other file and did not commit.

## Disposition

- **Retro:** adopt. It turns a session into traced, routed, approvable candidates. The base, given the same request, does not do this, and nothing is applied without a pick.
- **Retiring #131 capture:** this eval compares retro with an unprompted review, not with capture. Capture would have recorded nothing in any of the three sessions, because no Skill was in use in any of them. The pre-agreed condition was "retro recall clearly better than the control", and it is **not met**. Recall is at parity. The Human decides whether routing quality and the zero-capture baseline justify the retirement.
- **Open:** `pending` judged against current repo text when the repo changed after the session (2 of 9 r4 cell S actors); review turns pasted in the middle of a long session; per-moment self-retractions. Limits: one model, three actors per cell per round, LLM judges with visible strictness drift, one session per cell.
