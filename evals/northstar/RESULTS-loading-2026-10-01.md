# Conditional loading / learning: Phase 3 and composed review

Base: `d74e3ab6946f6ec7056395509e4c833fe882b1f2` (Phase 2).
This is the third staged change in the same Draft PR.

## Runtime delta

Ordinary dispatch/return uses the existing main ownership, current-Taskbook
judgment, real-event, authorization, acceptance, continuation and stopping rules.
The material reference retains distinct complex-dependency, ambiguous-identity,
changed-binding-context and cross-session/environment recovery details. Removed
ordinary-return duplication is covered in main; harmless version/text changes
still do not force rework.

Workers normally report reusable signals in their return. Feedback details are
loaded when that signal merits durable retention or an independent record was
explicitly requested. Ordinary dispatch does not preallocate a log path. Important
learning retains its source; an explicit no-signal record is still honored.
Canonical access is a receiver-side recovery precondition: a genuine process
launch may be reported while restoration remains blocked, but a pointer alone
never proves successful restoration or enables canonical-dependent work.

Exact UTF-8 sizes relative to Phase 2:

| Source | Before | After | Delta |
| --- | ---: | ---: | ---: |
| AGENTS.md | 18,605 | 18,677 | +72 |
| Northstar SKILL.md | 26,529 | 26,775 | +246 |
| material-compile.md | 8,926 | 7,809 | -1,117 |
| feedback-log.md | 4,661 | 4,961 | +300 |
| Total | 58,721 | 58,222 | -499 |

This is a source-size measurement, not a token, latency or performance claim.
Earlier phases add ownership/plan clarity; this table is not a claim that the
whole PR shrinks every source or the full prompt.

## Observed loading and behavior

Seven fresh native actors explicitly loaded isolated, byte-identical copies of
the final Northstar source. A temporary OS inotify observer watched SKILL.md and
both references throughout each case. Calibration read the main source and
confirmed an access event without inventing reference accesses. All observers
were stopped before source-hash inspection. No persistent harness or runtime
component was added.

| Case | Observed reference access | Artifact outcome |
| --- | --- | --- |
| L01 ordinary return | neither | current Taskbook accepts H1; no feedback artifact |
| L02 reusable signal | feedback-log only | sourced cross-session observation retained after Taskbook judgment |
| L03 changed binding Acceptance | material-compile only | old green return does not close the new missing-key clause; prior valid work retained |
| L04 receiving environment lacks canonical file | material-compile only | explicit restore blocker; no invented plan or execution success |
| L05 explicit independent note, no reusable surprise | feedback-log only | requested note appended with existing history preserved |
| L06 final scoped AE → Northstar recheck | neither | bounded explanation returns to AE; no architecture takeover or parallel Taskbook |
| L07 ordinary implementation/return loop | neither in the initial run | four string-header checks passed, but independent review found an unapproved non-string compatibility change; initial full acceptance failed |

L07's initial independently rerun check passes the four string-header outcomes,
but this is **not** an unqualified acceptance PASS. Its pre-run scope also
excluded non-string changes. Missing bytes keys changed from KeyError to None;
independent review correctly identified that unsupported/new-API disclaimers do
not authorize changing existing behavior. The initial caller and verifier missed
that original constraint. The failed initial outcome is retained rather than
counted away or attributed to autonomous caller detection.

The same task was corrected under its unchanged original contract after reviewer
feedback. The corrected code restores missing-bytes KeyError, passes the original
four string-header requirements, and independently matches 30 non-string baseline
comparisons across string-key, bytes-key and empty collections. The revised caller
records its initial acceptance as superseded. This proves bounded review-driven
recovery; it cannot establish that initial unassisted acceptance was sound. No case-specific runtime rule is added:
the existing scope/constraint invariant already covers the issue, and this one
observation does not justify extra runtime instructions. Native inventory
observed the initial verification child running and completed. Implementation
dispatch is recorded in the actor's work artifact; this is not a complete tool
trajectory audit. The main-only loading observation remains valid for the
initial interval, not an assertion about later recovery reads.

## Evidence, review and limits

[Outcome archive](loading-outcomes-2026-10-01.json.gz) retains before/after artifacts,
source-copy hashes, exact authored task clauses, raw access events, observer code/calibration, exact size
measurements and independent L07 check output. It records limitations explicitly.
The temporary observer is measurement support, not a new Skill, router, loader or
production system. Authored task clauses are retained verbatim; an identical
non-task reporting/permission coordination suffix and inherited host instructions
are not exported. The independent reviewer inspected the full authored prompts;
no task clause specifies expected reference reads or skips.

Access events establish which watched files were accessed. They do not measure
exact bytes/tokens consumed, PID-level attribution, every host read, or semantic
comprehension; event counts are not invocation counts. One trial per case and no
paired base measurement cannot establish statistical cost or behavioral uplift.
Final snapshots cannot exclude transient edits or prove every reported command.
Automatic Skill selection and production transport remain unmeasured.

Independent review covers the final composed source against the verified main
snapshot, prior phase evidence, and these final affected-boundary checks. The 51
existing synthetic/infrastructure regressions pass again; they validate the
instruments, not candidate agent behavior. JSON/source identity checks and
`git diff --check` pass. The five other Skills' runtime sources remain identical
to their Phase 1-tested versions. Publication remains Draft and does not imply
merge readiness or new merge/deployment authority.
