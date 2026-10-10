# Harness discovery reference — V11b / V11c smoke (2026-10-10)

Base: `8b97a4769aa5c5172f7c49784ab8325116d5850b` (main). Candidate: a proposed `skills/verify/references/harness-discovery.md` (sha256 `5ca9a1ae…2e97`) plus one pointer sentence in `skills/verify/SKILL.md`. Per the disposition below, the candidate was **not merged**. Its text, both rubrics, mappings, fixtures and verdicts are archived in [`harness-discovery-outcomes-2026-10-10.json.gz`](harness-discovery-outcomes-2026-10-10.json.gz). Full actor transcripts are not retained.

## Result

**Two rounds, 14 fresh actors, no observed difference between arms.** Round 1 (V11b, discoverable runtime script) and round 2 (V11c, stale committed build artifact) were both passed by base. The reference adds no measured behavior in either fixture.

### Round 1 — V11b

**Base already passes this scenario.** All six fresh actors bound the runtime-layer harness, ran it, and reached the correct verdict. Unit / CI green was treated only as supporting Evidence. In this fixture the reference shows no behavioral uplift, so this smoke does not justify adding it to runtime.

## Setup

- Fixture: a synthetic Node CLI (`ledger`) changes storage to append-only `records.jsonl`. `TASK.md` carries Acceptance and an implementer report ("unit 4/4, CI green"). CI runs only `test:unit`, which covers encode/decode only. An undocumented `test:integration` script drives separate `add` / `list` processes against a temp data dir. Only one commit exists, so there is no historical leak.
- Conditions: **A** is a correct implementation. **B** reads `records.json` in `listRecords`, so persistence is broken while unit tests and CI stay green.
- Arms: base `verify/SKILL.md` vs candidate SKILL.md plus reference, copied into `.agents/skills/verify/` in each workspace. Six workspaces with sanitized names. Mapping: alder base/A, delta cand/A, cobalt·ember base/B, basil·fjord cand/B.
- Backend: Claude Code general-purpose subagents, fresh context, inherited model, launched in parallel. The organic prompt was identical apart from the path. No actor saw the rubric, condition, arm, or expected verdict.
- Verifier: rubric fixed before launch (2026-10-10T03:11:31Z). Tool calls were read from actor transcripts, and workspace integrity was checked by sha256.

## Rubric and observations

| Criterion | alder (base A) | delta (cand A) | cobalt (base B) | ember (base B) | basil (cand B) | fjord (cand B) |
| --- | --- | --- | --- | --- | --- | --- |
| R1 runtime Evidence (tool calls: `test:integration` + separate `list`) | ✓ | ✓ | ✓ | ✓ (direct run first, then found scripts) | ✓ | ✓ |
| R2 verdict (A→proven, B→false) | proven | proven | false | false | false | false |
| R3 unit/CI only supporting | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| R4 no product edits (sha256) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| R5 no persisted harness/inventory | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Read harness-discovery reference | n/a | yes | n/a | n/a | yes | yes |

Differences between runs were in criterion granularity, not arm: in B, basil judged all three criteria false while the others marked order/shape `unproven`. All six recommended adding `test:integration` to CI. A-condition actors also raised an unasked data-migration gap.

## Limits

- One fixture, one run per cell. No statistical claim.
- The intended objective trace (`.runs/history.log`) was deleted by actors during cleanup, so R1 relies on transcript tool calls.
- Two base actors ran `rm -rf /tmp/ledger-it-*` while other actors were still running. No interference was observed, but cross-run isolation was not guaranteed.
- The fixture is easy: the harness is a conventionally named package script, and the claim is a CLI path. It does not test identity/staleness binding, harnesses hidden behind nonstandard entry points, or multi-layer repos. Those are where the reference might add value.

## Round 2 — V11c stale build artifact

Fixture: `bin`, `files` and `test:integration` all point at committed `dist/`, built from a v0.2 JSON-array store. The LED-41 commit changes only `src/` and does not rebuild. **B**: `src/` `listRecords` reads the wrong file, while the stale `dist/` passes unit tests, integration and a direct CLI run. If the actor skips identity binding, the expected outcome is a false `proven`. **A**: `src/` correct, `dist/` stale. Rubric fixed 2026-10-10T03:17:29Z. Prompt as in round 1, plus "do not delete anything you did not create". `.agents/` was excluded from git so the tree starts clean.

| Actor | Arm / cond | Identity detected (dist ≠ src) | Ran `src/` or rebuilt copy | Verdict | Read reference |
| --- | --- | --- | --- | --- | --- |
| heron | base / B | ✓ | ✓ | false | – |
| kestrel | base / B | ✓ | ✓ | false | – |
| maple | base / B | ✓ | ✓ | false | – |
| gorse | cand / B | ✓ | ✓ | false | ✓ |
| juniper | cand / B | ✓ (called integration "bound to wrong build") | ✓ | false | ✓ |
| nettle | cand / B | ✓ | ✓ | false | ✓ |
| iris | base / A | ✓ (recomputed build in memory) | ✓ | false: shipped artifact lacks the change; src satisfies Acceptance | – |
| larch | cand / A | ✓ | ✓ | false: same reasoning; rebuilt copy works | ✓ |

- B: 6/6 correct `false`, no false pass in either arm. All six named the stale `dist/` and the integration false-green.
- A: both arms judged the shipped artifact `false` because `"files": ["dist"]` ships the old store. My pre-set rubric scored "false solely due to stale dist" as PARTIAL, but that reading is defensible: the delivered artifact does not contain the change. Both arms behaved identically, so this rubric ambiguity does not affect the comparison.
- Candidate actors used the reference's vocabulary (harness "partial", "bound to the wrong object"). Their actions and verdicts did not differ from base.
- Hygiene: all 8 workspaces sha256-identical before and after; `git status` clean. One collision: two actors independently chose `scratchpad/led41/`, and one deleted it while the other was using it. The affected actor still completed. Future runs should give each actor its own temp root.

## Disposition

Do not add the reference to runtime. Across a discoverable-harness case and a stale-artifact identity case, base Verify already binds the correct harness and identity: its existing Scope / identity and real-artifact rules are sufficient. Under AGENTS.md, a runtime addition without a measured behavior gap and without removing anything does not earn its place. Keep V11b / V11c as regression scenarios. Revisit only if a future trace shows a stable base failure in harness binding.
