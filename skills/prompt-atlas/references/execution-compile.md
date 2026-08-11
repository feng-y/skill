# Autonomous handoff guidance

Read only when a simple task definition is not enough for longer autonomous execution.

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

This is an interface, not a process template. The Taskbook defines target state and proof of completion; the Executor materializes How.

## Goal

Keep the Human-owned outcome plus only the priority / boundary / must-preserve constraints that genuinely limit execution choices. A proposed implementation from the Human is a hypothesis by default unless Human or repo authority explicitly makes it binding.

Prefer existing repo specifications: tests, schemas, ADRs, Architecture Intents, acceptance scripts, and executable references. Do not translate them into a weaker prose copy.

## Execution

Split work only when judgment or dependency genuinely differs. Graph expresses real dependencies; it does not turn files, functions, BUILD edits, or debugging order into nodes.

Ordinary factual / implementation Unknowns stay with the Executor to resolve from current repo reality. Reopen an upstream decision only when the conclusion would change Goal / authority.

Still-valid work / Evidence aligned with the Goal can be reused. New Evidence stales only conclusions that depend on it.

## Verification / Evidence

State what must be proven for completion, not the debugging workflow. Prefer authoritative Human / repo checks. If a baseline matters, keep only signals that genuinely carry coverage / attribution and ground them in current reality.

Evidence must support the real completion claim rather than activity narration or self-declared PASS. If verification fails, fix the implementation or report accurately; do not weaken the judge to manufacture success. Read [verification-trust.md](verification-trust.md) only for a concrete false-green / gameability / independence risk.

## Handoff

Stay minimum-sufficient. Research details the Executor can reliably reconstruct do not belong in the Taskbook; keep only non-obvious facts whose omission would cause a wrong Goal, boundary, or verification decision.

Write the complete current Taskbook to an OS/runtime-provided Markdown artifact outside the current repo/workspace. The artifact carries the task definition only; do not add ready/completed/executable metadata. For a revision, update the current Taskbook when possible; if that path is not writable, write the revision to an available runtime artifact and surface the actual authoritative path.

`implement-notes` stores only Executor progress, material decisions / Evidence, blockers, and resume point.

Keep autonomous Taskbooks short; when content grows, remove duplication and implementation intelligence before adding more guidance.
