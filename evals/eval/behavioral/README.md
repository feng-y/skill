# Eval actor paired diagnostic smoke

These are three **constructed, editor-exposed diagnostic tasks**, based on
E11–E13. They test real Eval actors doing audits/repairs/adoption decisions.
They do not establish held-out generalization or a working end-to-end automatic
hillclimber. The documentation-agent records *inside* the fixtures are synthetic,
frozen inputs; actual outer Codex actor runs must not be confused with them.

## Binding and reproduction

`run.py` adapts the existing `northstar-beacon-behavioral/run.py`: fresh session,
revision-specific Skill installation, execution, timeout, JSONL events, Codex
session rollouts, and before/after Git snapshots are reused. Only prompts,
fixtures, complete artifact capture and actual CLI version are replaced.
The shared runner's new optional `--repeats` preserves its prior default of 3;
this task uses 1, with targeted repeats only for a difference/failure/question.
No Northstar behavior or fixture is changed.

From the repo root, with the existing Codex login on the execution host:

```sh
python evals/eval/behavioral/run.py \
  --output-root /code/b/skill-eval-runs/eval-pr120-smoke \
  --max-workers 3 --repeats 1 \
  --base-sha 9a89fc02dd9ec5cc7e67b57e993976109dfbf8fa \
  --candidate-sha 40ffccb2f92727963dc443fb787eedc539e4a8a2
python evals/eval/behavioral/check.py /code/b/skill-eval-runs/eval-pr120-smoke
python evals/eval/behavioral/judge.py /code/b/skill-eval-runs/eval-pr120-smoke --max-workers 3
```

The output root must be new/empty. `--case E11` (or E12/E13) scopes repeats.
The backend uses `gpt-5.6-sol`, high reasoning, never approval,
`danger-full-access`, a 1,200-second actor timeout, and 600-second judge timeout.
These are disposable local fixtures; no real publication or deployment tools
are supplied. The runner reuses the host login through a symlink; **never publish
`codex-home/auth.json` or archive the whole output tree indiscriminately**.

## Task / Environment / Verifier

| Task | Environment and observable action | Independent check / semantic judgment |
| --- | --- | --- |
| E11: audit questionable quality scores | Visible answer/citation contract; undeclared file requirement; inconsistent regrades; failure-only corpus; two frozen configurations. Repair and execute offline grader. | Both groups rescore correctly; immutable records/prompt; wrong answers/citations still rejected. Diagnose sampling/noise/headroom, and don't infer model inferiority or live uplift. |
| E12: decide two optimization adoptions | Approved distinct quality/cost objectives, paired intervals, grouping and exposure/selection history. Write assessment only. | Reject unsupported quality gain, support cost saving within predeclared quality tolerance, preserve exposure/selection/final-test limits and action authority. |
| E13: diagnose stalled iterations | Three unsuccessful rounds; undeclared file check; stale reference state; repeated wrong answers in tool traces. Repair and execute offline grader. | Both groups get 6/9; remaining errors stay errors. Separate measurement recovery from behavior gain; preserve prompt/data; recommend one attributable next experiment without pretending it ran. |

`check.py` requires an observed successful read of the selected Eval Skill (a
measurement validity gate), independently verifies snapshots, and probes each repaired grader with
wrong-answer and wrong-citation records in fresh disposable copies. These probes
catch unconditional-pass repairs; they do not prove general verifier robustness.
`judge.py` supplies the frozen case rubric to a fresh, independent Codex judge,
reusing the existing judge executor and trajectory packaging. It consumes actual
commands/results, changes, artifacts and independent checks, not only final prose.
Skill-read outputs are omitted from the judge package to reduce treatment leakage;
the unmodified complete original trajectory is retained. Main-agent review must
also inspect those originals and confirm actual Skill loading and access scope.

## Exposure and claims

Prompts contain no expected route, rubric, PASS/FAIL answer or arm identity.
Actors see only a neutral UUID workspace, ordinary task materials and the selected
installed Skill. The host target Skill copies are disabled identically. Full
`skills/` trees are installed by the existing runner; for these revisions only
Eval runtime differs. Judges receive opaque IDs and no arm/SHA labels.

This backend has full filesystem access, not an enforced security boundary:
external manifests and sibling directories are physically accessible. Inspect
all trajectories for label/rubric/opposite-arm access; any such access invalidates
the comparison. Even without observed access, claim only diagnostic smoke,
**not independently isolated held-out evaluation**. Newly authored fixtures and
same-task repeats never become independent unseen tasks by relabeling.

Keep full run identity, tool/state evidence, failures and costs. Fix the measurement
before attributing a behavior failure; rerun both arms if the task/environment or
verifier repair changes what is measured. Don't patch runtime for a one-off miss,
and don't repeat passing ties merely to hunt for separation.
