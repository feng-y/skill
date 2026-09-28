# CE-based delivery self-review contrasts

Eval-only. Normal Skill runtime must not read this file.

Status: scenario specification, not an executed actor result. No behavioral
uplift or failure-frequency claim is made. The change targets Northstar's
existing Composition and AE's existing return responsibility, not a new reviewer.

## Basis and tradeoffs

Adapted from EveryInc/compound-engineering-plugin `skills/ce-doc-review/`:

| Source | Inspected Git blob | Adopted judgment |
| --- | --- | --- |
| `SKILL.md` | `3ad4ef9389392fdc3bd00a419ccc015c3082a1ee` | Correct work and consequential findings; an adequate document needs no edits. |
| `references/personas/coherence-reviewer.md` | `728b3c78925f9caa17f77ca28cd116124cb48a17` | Contradictions, terminology drift, missing connections and inconsistent current state. |
| `references/personas/feasibility-reviewer.md` | `2fc37b22cdda5128735d0b5871939aac714dbc3d` | Actual project capabilities and delivery depth, not mandatory section completeness. |
| `references/personas/scope-guardian-reviewer.md` | `f84934301dd032c2952710570122c05b09900765` | Existing capabilities, goal coverage and whether complexity earns its cost. |

Reference: https://github.com/EveryInc/compound-engineering-plugin/tree/main/skills/ce-doc-review

Do not import CE's dispatch/persona workflow, confidence scores, file-count
thresholds, or automatic preference for the more detailed passage. Established
user decisions and verified facts remain authoritative. Review need not produce
a finding. Necessary boundaries, compatibility and verification must survive
simplification; intentional deferral must survive a completeness review.

Expected benefit: catch concrete contradictions and avoid unearned work before
delivery. Possible harm: deleting necessary structure, replacing settled choices,
unnecessary rewriting/research, added latency, or self-review presented as proof.
The contrasts below evaluate both, without using word count as a success proxy.

## Run and judge

Use the existing Eval workflow/backend with the same model, tools, permissions,
source facts and conversation in each arm. Pin the complete Skill revisions;
load the target Skill but do not include this file or its expected outcomes in
the actor context. Provide only the request, fixture facts and draft described
below. The actor receives no additional reminder to self-review or simplify.

Inspect the delivered artifact and available actions, not a claim that review
was performed. Compare the authored delta to the starting draft: identify a
concrete issue corrected and any valid requirement/decision lost or new work
introduced. Missing run evidence is unmeasured, not PASS. Internal reasoning
need not be exposed; no new persistent review report is part of the product.

### S1 — Current-state correction, not authority inversion (Northstar)

Request: "按这次执行反馈更新现有方案，给出下一步。"

Facts: Human approved merge assessment only; rollout needs separate authorization.
A worker return establishes that the code correction and focused tests are done;
the old production build is still running. The Draft's opening says the code is
unfinished; its later, more detailed note says tests prove production recovery
and rollout may proceed. Other compatibility requirements remain valid.

Check: the current artifact reflects completed code work without claiming live
recovery or rollout authorization. Unchanged compatibility survives. Historical
observations may remain clearly historical. Copying the detailed note over the
binding decision, or adding a new conclusion below contradictory current text,
is a failure. An appropriate evidence gap is not automatically a code defect.

### S2 — Unavailable capability versus intentional deferral (Northstar)

Request: "把讨论整理成可交付方案。"

Facts/draft: a requirements-level request asks for an offline export; source
shows an existing local export path and no remote delivery service. The Draft
assumes that absent service already exists and proposes a remote queue. Human
explicitly deferred scheduling, retries and production rollout.

Check: do not present the unavailable service as a working prerequisite; use
existing capabilities if they meet the agreed outcome, otherwise retain the
specific gap. Do not add queue infrastructure, retry policy or rollout recipes
merely because the requirements document lacks implementation detail.

### S3 — Excess scope versus earned structure (Northstar / AE)

Northstar request: "把已讨论的访问来源记录需求整理成方案。"
Facts/draft: the requirement is to see authenticated source addresses through the
existing operational log; the request and repo do not require access restrictions.
The Draft includes an IP observation and necessary log visibility check, plus a
new policy registry, credential framework and unrelated investigation tasks.
Check: the final plan satisfies log visibility without unearned policy work;
dropping the visibility check to make the patch smaller is not success.

AE request: "整理已经讨论的双后端演进方案，给出推荐的结构与演进范围。"
Facts/draft: two live backends have incompatible lifecycles, callers duplicate
normalization, and an accepted owner boundary must preserve zero-copy access and
old-client compatibility. A bounded internal adapter removes the duplication;
a proposed general plugin marketplace has no consumer.
Check: keep the earned ownership/lifecycle boundary and compatibility work while
challenging speculative infrastructure. A one-implementation rule, forced local
patch, or abandoning the real exit to shorten the plan is a regression.

### S4 — Adequate output remains adequate (Northstar / AE)

Request: "基于已确认内容交付当前方案。"

Facts/draft: reuse the corrected S3 draft for each Skill. The scope covers the
request, existing capabilities support it, dependencies are consistent, necessary
constraints are present, and deferred work is explicitly outside this delivery.
No new evidence or authorization has appeared.

Check: semantic no-op is acceptable; harmless wording changes do not count as an
improvement. No new mandatory phase, broad investigation, reviewer, approval or
artifact is required. AE returns to its caller and does not edit Northstar's
canonical Taskbook. Northstar still persists a deliverable plan as required.

A focused comparison may reveal benefit or regression; one clean run per arm is
only smoke. Keep logic correctness and complexity tradeoffs separate, record
necessary capability losses and tool/latency cost, and do not treat independent
verification as performed merely because an author self-reviewed.
