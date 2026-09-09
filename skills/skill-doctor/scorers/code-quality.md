---
name: Code Quality
description: Whether code, tests, and comments produced by the agent are well-designed and consistent with the target repo.
labels:
  - value: approve
    score: 1
  - value: block
    score: 0.2
  - value: insufficient_evidence
    score: 0.5
---

Apply this scorer only when the transcript exposes enough of the produced code change to review it. Judge the artifact as a careful senior reviewer would, using the target repo's own conventions.

`approve` means mergeable as-is except trivial nits. `block` means at least one defect requires a fix before merge. Use `insufficient_evidence` when the transcript does not expose enough code/diff; exclude that result from code-quality aggregation and failed-conversation filtering.

Assess:

- design fit and absence of speculative abstraction/scope creep;
- correctness, edge cases, error and concurrency behavior;
- unnecessary complexity or indirection;
- repo-local conventions and naming;
- code smells and diff hygiene;
- tests that would fail for a broken implementation and cover material risks;
- comments that explain why rather than narrate edits;
- required docs updated with the behavior/tooling change;
- Human corrections: a real defect requiring external correction is a negative signal even if later fixed.

Reason: 1–3 sentences citing the specific defect or convention that drove the grade and what check, convention, test, or Skill should have caught it.
