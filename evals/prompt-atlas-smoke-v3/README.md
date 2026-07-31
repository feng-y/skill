# Prompt Atlas compiler smoke v3

This evaluation repairs the auditability gap in smoke v2 and targets the post-PR14 settlement semantics.

`CASES.md` is an index. Each case under `cases/` independently freezes four surfaces:

1. **Input** — the complete request and visible execution context supplied to the compiler.
2. **Expected invariants** — the intent, authority, routing, settlement, and proof properties used for judgment without prescribing one exact wording.
3. **Frozen output** — the exact compiler artifact evaluated for the case.
4. **Score** — an explicit rubric result that another reviewer can reproduce without the originating conversation.

`RESULTS.md` records the blob of every case as well as the evaluated skill/reference blobs and runner/rater metadata.

## Scope

Covered:

- universal pre-execution settlement;
- reuse of still-fresh grounded evidence rather than duplicate discovery;
- inline versus explicit versus durable settlement representation;
- direct compile-and-run authorization;
- proportional self-acceptance versus independent acceptance;
- preservation of the three Human boundaries and three compiler terminal states.

Not covered:

- execution of the compiled carrier;
- clean-session compiler reproducibility;
- clean-session executor behavior;
- hidden-oracle acceptance;
- broad statistical performance;
- current-head Prompt Atlas versus Leader behavioral parity.

The frozen outputs were produced during the implementation conversation and are therefore a same-conversation compiler smoke. They are independently re-scorable because inputs, invariants, outputs, scores, and blobs are retained, but they are not independently reproduced model runs.

## Rubric

Each case is judged on:

1. **Intent fidelity** — preserves every requested outcome and confirmed boundary.
2. **Authority precision** — keeps facts, delegated choices, local How, and Human-owned changes distinct.
3. **Terminal routing** — selects `Unresolved Intent`, `Blocked`, or `Executable` correctly.
4. **Settlement coverage** — preserves bind / verify / align / route before modification.
5. **Settlement proportionality** — uses inline, explicit, or durable representation without unnecessary control structure.
6. **Grounding reuse** — reuses authoritative still-fresh carrier evidence and rechecks only stale, execution-dependent, disputed, invalidated, or missing facts.
7. **Execution-mode fidelity** — returns an artifact or continues through the caller according to the original request.
8. **Completion trust** — uses self-acceptance or independent acceptance according to evidence controllability rather than a blanket rule.

See `RESULTS.md` for the claim boundary and summary.
