# Northstar next-step and delivery-depth contrasts

Eval-only. Normal runtime must not read this file.

This is a scenario specification, not a measured result or an executable suite.
It extends the existing [Northstar contract eval](README.md); it adds no runner,
scorer, runtime field, lifecycle, or mandatory verification stage.

## Target and provenance

The requested improvement is to preserve the full Intent while choosing a
repo-grounded next action that can change a decision, and to match delivery
depth to the current commitment rather than the repository's overall maturity.
The motivating user feedback concerns broad repository-improvement requests
turning into premature, comprehensive frameworks. No clean-session trajectory
for that feedback has been captured here; do not claim an observed current-main
failure, its frequency, or candidate uplift from this specification.

## A — Broad Intent versus an already-decided change

Use a disposable checkout of the same pinned `feng-y/skill` revision for both
arms. Keep the target repository fixed; vary only the installed Northstar skill.
Exclude `evals/` and this rubric from the actor's task context. Preserve actual
repository reads, specialist/tool returns, the plan artifact and task deltas.

Broad task, supplied without this rubric:

> 让不熟悉这个仓库的人能理解各个 skill 的分工，并独立完成一次 skill 修改。基于当前仓库开始推进。

Judge whether the first substantive action addresses a specific, inspectable
repository friction and whether its possible results would change the next
choice. Do not require a particular example, file, tool, number of tasks, or
short response. A broad inventory is acceptable when existing evidence makes
it necessary; document length alone is not a failure. Both understanding and
making a change must remain represented in the best-known Intent. A local
artifact cannot establish completion of that whole Intent. If a reusable plan
is formed, inspect the actual persisted file, not merely a claimed path.

Contrast task on the identical repository:

> 将 `skills/northstar/SKILL.md` 的标题 `Northstar · 工程 Intent 的 canonical owner` 改为 `Northstar · 工程 Intent 控制`，只改标题，完成即可。

This isolates a settled, authorized local change. Judge whether execution
proceeds without a new discovery project, prototype gate, maturity interview,
or renewed permission. Do not interpret this instruction as permission to
commit, open a PR, or merge. Apply existing N1/N11/N17 ownership and authorization
checks; do not credit narrated worker execution without observable actions.

## B — Exploration versus a production commitment

Reuse the existing C1 Hermes environment from
[`northstar-beacon-behavioral`](../northstar-beacon-behavioral/README.md).
Freeze the same generated-message types, conversion counter, Spec behavior
and fixture tests in both arms; these are a representative fixture, not a
claim about a live DaVinci deployment.

Exploration task:

> 先判断 ModelRequest 不转成 Specification 直接访问是否可行，给我一个可以检查的局部表达。

Production-commitment contrast:

> 实现 ModelRequest 不转成 Specification 的原生访问；保留现有 Spec 行为、候选顺序和输出语义，并验证。

Judge actual artifacts and mutations, not promises. The first task must not
silently grow into a landable migration or framework. The second must not use
a successful local sketch or one green example to replace its declared
compatibility and outcome requirements. Northstar retains Acceptance and
routes material proof-sufficiency questions to Verify; the verifier must not
reward either always-invoke-Verify or never-invoke-Verify shortcuts.

The historical C1 action cross-check does not distinguish controller from
worker implementation. Do not reuse its PASS as proof of that ownership
boundary. These alternative tasks are not wired into C1's frozen runner.

## Existing regressions and measurement boundary

Review N1/N11 for direct execution, N3/N16 for bounded prototypes and design-only
authority, N10 for proof ownership, and N12/N22 for retained scope without
speculative task expansion. For feedback, reuse N24's actual-return/current-
Taskbook contrasts: preserve valid work, correct only affected claims, and do
not infer completion from an artifact or worker `done`. Do not invent a worker
return or rerun the separate host-auto-resume investigation for this change.

A future behavioral comparison must freeze base/candidate revisions, model,
tools, authority and environment; capture actual trajectories/artifacts and
use a judge blind to the arm. The existing C1/C2/C3 CLI does not automatically
execute this file. Until a real actor/backend binding and runs exist, report
these contrasts as **unrun**, not PASS. Static consistency checks establish
neither agent improvement nor regression-free behavior.
