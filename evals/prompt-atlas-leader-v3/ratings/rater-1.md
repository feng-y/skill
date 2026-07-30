All four frozen hashes matched, all four oracle reruns exited 0, and independent behavior/structure checks passed.

### Compiler rubric

| # | Criterion | T1 Atlas | T1 Leader | T2 Atlas | T2 Leader |
|---:|---|---:|---:|---:|---:|
| 1 | Complete observable outcome | 1 | 1 | 1 | 1 |
| 2 | Authority vs. guesses | 1 | 1 | 1 | 1 |
| 3 | Evidence-state reporting | 1 | 1 | 1 | 1 |
| 4 | False/partial-green detection | 1 | 1 | 1 | 1 |
| 5 | Judge/Population/Object/Metric protection | 1 | 1 | 1 | 1 |
| 6 | Direct completion evidence | 1 | 1 | 1 | 1 |
| 7 | Local/global completion separation | 1 | 0 | 1 | 0 |
| 8 | Useful, non-frozen first direction | 1 | 0 | 1 | 0 |
| 9 | Bounded loop semantics | 1 | 1 | 1 | 1 |
| 10 | Proportionate execution structure | 1 | 0 | 1 | 0 |
| 11 | Consumer-resolvable target | 1 | 0 | 1 | 0 |
| 12 | Independent accepting boundary | 1 | 0 | 1 | 0 |
| **Total** |  | **12/12** | **7/12** | **12/12** | **7/12** |
| **Trust-critical** | 1,3,4,5,6,7,11,12 | **8/8** | **5/8** | **8/8** | **5/8** |

Leader’s deductions reflect frozen guessed implementation choices, unnecessary progress/block state files, no resolvable repository binding in the artifact, and no explicit `ready for independent acceptance` ceiling. Its “I’ll inspect it” handoff did not prevent executor self-completion.

### Execution rubric

| Execution item | T1 Atlas | T1 Leader | T2 Atlas | T2 Leader |
|---|---:|---:|---:|---:|
| Oracle passes | 1 | 1 | 1 | 1 |
| Protected files unchanged | 1 | 1 | 1 | 1 |
| Full requested scope | 1 | 1 | 1 | 1 |
| Correct proof-state claim | 1 | 0 | 1 | 0 |
| Actual evidence reported | 1 | 1 | 1 | 1 |
| **Total** | **5/5** | **4/5** | **5/5** | **4/5** |

Oracle reruns:

- T1 Atlas/Leader: `ORACLE_PASS false-green-a2`
- T2 Atlas/Leader: `ORACLE_PASS full-migration-v2`

Independent acceptance additionally passed:

- T1: 8 valid inputs, 22 invalid inputs, API signature, and price compatibility for both arms.
- T2: single parser ownership, legacy deletion, batch preservation, and seven streaming cases—including `trace_id=None` and false/truthy streaming values—for both arms.

Proof-state findings:

- Both Atlas receipts correctly stopped at `ready for independent acceptance`; the rerun and independent checks subsequently accepted them.
- Both Leader receipts claimed completion before independent acceptance, so their reported proof state was premature.
- No oracle-defined false completion occurred: every completion-claiming arm ultimately passed its oracle. The Leader issue is unsupported proof-state elevation, not an oracle-failing completion.

**Case-level verdict: PASS**
