# Intent convergence implementation review

Development/eval-only. This is implementer self-review, not an independent behavioral evaluation.

Continuation base: `f2e2e2bafd9a6596b29c227742337b7100d0e68d`.

## Verdict

The intended ownership model is implemented in Northstar runtime, invocation metadata and focused eval guidance:

- Northstar is the canonical Intent owner and convergence control;
- Prototype remains one caller-neutral construction tool and was not expanded;
- caller-side composition remains explicit;
- Human questions close expectation / scope / commitment gaps;
- factual / structural / proof owners remain unchanged;
- no new Skill, persistent state machine, ticket map or mandatory lifecycle was introduced.

No blocking contract contradiction was found in the bounded review below. This does **not** prove model behavior improvement. Real clean-session actor / consumer / blinded-judge runs in this continuation: **0 / 0 / 0**.

## Implementation review 1 — capability boundaries

Reviewed the Northstar descriptor, core rule, gap routing, Prototype boundary, Human interaction and handoff gate together.

Checks:

- Northstar decides *which gap matters* and integrates returned results; it does not decide Target Architecture, factual reality or proof sufficiency for the specialist.
- Prototype still builds only the commissioned problem artifact / draft / disposable experiment. It does not select and assemble problem-level outputs or declare overall Intent coverage.
- caller-side composition may expose another concrete construction gap; sending that bounded gap to Prototype does not transfer composition ownership.
- external orchestration can schedule calls but is not granted semantic ownership.

Result: pass for ownership consistency.

## Implementation review 2 — over-control / ceremony risks

Counterchecked failure modes introduced by an explicit convergence loop:

- **simple task:** may converge in one pass with no specialist or Human ceremony;
- **Human already authorized:** reuse the answer, do not ask again;
- **technical fact:** inspect territory instead of asking Human;
- **oversized Intent:** Human is asked only when narrowing changes accepted scope or commitment;
- **local PASS:** does not imply overall completion if integrated coverage is missing;
- **only implementation How remains:** hand off rather than keep Northstar as a progress manager;
- **Graph:** remains earned only for material dependencies that a fresh Executor would otherwise rediscover.

Result: no mandatory stage chain or approval loop introduced.

## Eval review

`evals/northstar/README.md` now checks the convergence trajectory rather than only artifact presence:

- requirement coverage;
- correct decision owner;
- caller-side composition quality;
- necessary/non-redundant Human interaction;
- fresh-consumer handoff quality.

These are explicitly eval lenses, not runtime schema fields. Existing paired scorer metrics remain useful but are insufficient by themselves to certify Intent convergence.

## Evidence boundary

This continuation changes text / invocation metadata / eval guidance only. No Hermes implementation, runtime installation, model session, Skill Doctor, benchmark or product Replay was executed here. Therefore do not infer improved routing, lower clarification rate, better handoff rate, performance gain or successful incident resolution from this review.

Merge posture for behavior-validated completion remains **HOLD / Draft** until clean-session evidence is available. Contract implementation itself has no blocking issue identified in these review rounds.
