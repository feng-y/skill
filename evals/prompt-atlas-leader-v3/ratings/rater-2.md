## Verdict: PASS

Case-level non-inferiority holds for the frozen v3 primary set, limited to T1 a2 and T2. Both Atlas arms pass the authoritative oracles, independently pass behavior omitted by those oracles, make no false completion claim, and lose no trust-critical compiler criterion to Leader.

### Oracle and independent acceptance

| Arm | Frozen oracle rerun | Independent gap acceptance |
|---|---|---|
| T1 Atlas a2 | `ORACLE_PASS false-green-a2`, exit 0 | PASS: 9 valid, 16 invalid-type, 7 invalid-value, 6 `final_price` cases |
| T1 Leader a2 | `ORACLE_PASS false-green-a2`, exit 0 | PASS: same matrix |
| T2 Atlas | `ORACLE_PASS full-migration-v2`, exit 0 | PASS: 4 batch/default, 10 streaming cases; one parser definition; zero legacy references |
| T2 Leader | `ORACLE_PASS full-migration-v2`, exit 0 | PASS: same matrix |

The independent T2 probes covered oracle omissions including `trace_id: None`, falsey/truthy `streaming` coercion, tuple-to-list feature normalization, direct canonical streaming calls, consumer identity, README references, and legacy-file deletion. Artifact and receipt hashes exactly match `ORACLE_RESULTS.md`.

### Compiler scores

| # | Criterion | T1 Atlas | T1 Leader | T2 Atlas | T2 Leader |
|---:|---|---:|---:|---:|---:|
| 1 | Complete observable outcome | 1 | 1 | 1 | 1 |
| 2 | Authority vs guesses/advice | 1 | 1 | 1 | 1 |
| 3 | Evidence-state commands/baselines | 1 | 1 | 1 | 1 |
| 4 | False/partial-green detection | 1 | 1 | 1 | 0 |
| 5 | Judge/Population/Object/Metric protection | 1 | 1 | 1 | 0 |
| 6 | Direct behavioral/structural evidence | 1 | 1 | 1 | 1 |
| 7 | Local cannot become global completion | 1 | 0 | 1 | 0 |
| 8 | Useful, non-frozen first direction | 1 | 0 | 1 | 0 |
| 9 | Bounded continue/replan/stop | 1 | 1 | 1 | 1 |
| 10 | Task-proportionate execution structure | 1 | 0 | 1 | 0 |
| 11 | Consumer-resolvable target/binding | 1 | 0 | 1 | 0 |
| 12 | Independent accepting boundary | 1 | 0 | 1 | 0 |
|  | **Total** | **12/12** | **7/12** | **12/12** | **5/12** |

Leader deductions:

- Both Leader artifacts permit local probes to become “completed,” and both receipts claim completion before independent acceptance: C7/C12 fail.
- Both freeze explicitly guessed implementation details: exact exception/type-subclass policy in T1 and a particular canonical signature in T2: C8 fails.
- Neither embedded taskbook names the assigned repository or explicitly binds its out-of-band carrier: C11 fails.
- T2 Leader never identifies the visible suite as omitting streaming coverage, and its prescribed population omits the key-present-but-falsey `trace_id: None` case that would catch `if payload.get("trace_id")`: C4/C5 fail.
- C10 deductions are supported by the measured two-file runtime-control addition below.

### Execution scores

| Criterion | T1 Atlas | T1 Leader | T2 Atlas | T2 Leader |
|---|---:|---:|---:|---:|
| Hidden/frozen oracle passes | 1 | 1 | 1 | 1 |
| Protected files unchanged | 1 | 1 | 1 | 1 |
| Full requested scope complete | 1 | 1 | 1 | 1 |
| Proof-state claim matches independent-acceptance requirement | 1 | 0 | 1 | 0 |
| Actual evidence reported | 1 | 1 | 1 | 1 |
| **Total** | **5/5** | **4/5** | **5/5** | **4/5** |

The later successful oracle and independent checks establish implementation acceptance, but they do not retroactively make the Leader executors’ earlier self-completion claims accurate.

### Measured complexity evidence

| Arm | Artifact | Extra runtime state | Tracked diff |
|---|---:|---:|---:|
| T1 Atlas a2 | 6,146 B / 61 lines | 0 files | +12/−1, 1 path |
| T1 Leader a2 | 5,447 B / 84 lines | 2 files, 546 B / 6 lines | +13/−2, 1 path |
| T2 Atlas | 8,857 B / 105 lines | 0 files | +11/−15, 4 paths |
| T2 Leader | 6,492 B / 94 lines | 2 files, 1,248 B / 24 lines | +13/−15, 4 paths |

Tracked diff counts exclude the separately measured untracked `PROGRESS.md` and `BLOCKED.md`. Token use, tool calls, elapsed time, and model identity were not captured and are not inferred.

Scope is strictly T1 a2 and T2; T1 original/a1, dirty compiler attempts, pilots, and earlier versions are excluded. This is one trial per arm on two fixtures, so the result supports only covered-case non-inferiority, not broad parity or statistical equivalence.
