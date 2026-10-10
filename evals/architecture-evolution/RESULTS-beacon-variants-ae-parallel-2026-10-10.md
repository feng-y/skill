# Beacon variants + parallel independent AE candidates — smoke (2026-10-10)

Base: `d1ea3b3d548e1c42dc6323254627eea557d146f8` (main). Candidate: `feat/beacon-variants-ae-parallel-20261010`.
- **v1** is the first candidate wording.
- **v2** is the final wording. It adds two things: an explicit caller / Human request counts as a trigger, and once a comparison is triggered, independent parallel generation is mandatory whenever any delegation capability exists.

Actors were Claude Code `general-purpose` subagents with `model: sonnet`, fresh context, and the Agent tool available (probed beforehand). There were 27 actors in total. Rubrics were fixed before each launch and kept out of actor context. Tool calls were read from actor transcripts. Product files were checked by sha256 before and after: every workspace was unchanged.

## Purpose and limits

This checks whether the Human-decided behavior change happens and whether its guards hold. It is **not** evidence of outcome uplift. Each cell ran once or twice, and parent semantic review was unblinded. Fixtures are synthetic: `jobrunner` for Beacon, and `notify` for AE (three flows with duplicated quiet-hours/opt-out policy, a legacy email wrapper, and, in later cells, a durable platform-owned job queue). Two actors in the AF2/AF3 cells wrote prototypes to the same scratch directory names, so their artifacts may have interfered; their reported observations differ, which suggests they did not fully overwrite each other, but this was not verified.

## Beacon

| Cell | base | candidate |
| --- | --- | --- |
| BF: caller names a live fork (continue-and-report vs stop-at-first-failure) | 2/2 built both variants behind one switch on the repo's anchors, ran them, no verdict | 2/2 same, with each variant's premise labelled |
| BN: no fork (decided `maxAttempts`) | 1/1 single prototype | 1/1 single prototype, explicitly no variants |

With a direct, explicit request, base already produced variants. The old single-prototype wording did not prevent this. The change removes a contradiction between the contract and the observed behavior; no uplift was measured.

## Architecture Evolution

| Cell | base | v1 | v2 |
| --- | --- | --- | --- |
| AF: fork that is not live (SMS/push, policy owner obvious) | 2/2 prose, no comparison | 2/2 prose, no comparison, explicit trigger check | 1/1 prose, no comparison (judged the rest implementation How) |
| AC: ADR already settles ownership | 1/1 reused ADR | 1/1 reused ADR | 1/1 reused ADR |
| AF2: live fork (deferral home: shared queue vs notification outbox), organic request | 2/2 prose; the substrate choice was handed to platform team / Human | 2/2 prose; same deflection | **1/1 triggered on its own: 2 parallel independent Beacon prototypes, picked a base, absorbed coherent parts of the other, recorded rejections, said why no judge** |
| AF3: same fork, explicit request to compare concretely | 2/2 single-context comparison tables, no Beacon | 2/2 single-context tables, no Beacon; both used the "independence limited" escape clause although Agent was available | **2/2 parallel independent Beacon prototypes** (both Agent calls issued before either result) |

Observations:

- **v1 loophole.** Both v1 actors on AF3 wrote "independence limited" or "the repo is small" and compared everything in one context. v2 closes this. Any delegation capability now counts as available, and repo size, readable facts, or an existing leaning do not justify skipping independent generation.
- **What concrete candidates add.** The v2 prototypes produced runtime Evidence that no prose comparison found:
  - with concurrent enqueue, the shared queue lost 50 jobs and assigned duplicate ids;
  - overlapping ticks double-sent;
  - a missing handler made the failure permanent;
  - only the outbox candidate re-evaluated policy at release.
  The four single-context AF3 comparisons split 3:1 on the recommendation. The three v2 runs all chose the notification-owned outbox. That is not proof of correctness, but it is consistent with the comparison being driven by Evidence.
- **Guards.** v2 did not over-trigger on AF or AC. On the organic live fork, v2 triggered in 1/1 while base and v1 triggered in 0/4. With n=1 this may be variance, but no v2 text targets organic triggering beyond the explicit-request clause.
- **Reaction tells** (implementation-time deviations the Executor must return rather than absorb) appeared as an explicit section in 7/7 v1/v2 AE runs on AF/AF2/AC. In base it appeared in 0/7 as a section; 2/7 base runs stated a looser re-entry trigger.
- **Cost.** Each v2 run that triggered took roughly 3–5× the wall time of a prose run (about 175–315s versus 30–65s).

## Disposition

Adopt v2. The Human already decided the Beacon multi-variant semantics. v2 makes the AE parallel-independent mechanism actually run when a comparison is warranted or requested, and keeps settled and routine choices out of competition. Still unmeasured: whether organic triggering is reliable, and whether outcomes improve against a ground-truth structural result.
