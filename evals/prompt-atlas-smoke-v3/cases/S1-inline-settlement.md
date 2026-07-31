# S1 — Clear local task uses inline settlement

## Input

The user directly requests completion in the available repository runtime:

> In `src/cache.py`, rename the private local variable `tmp` inside `lookup()` to `entry`. Preserve behavior and run `pytest tests/test_cache.py::test_lookup`.

Visible context:

- the repository and named file are available to the execution runtime;
- the target is local and reversible;
- the named focused test is the governing check;
- no other change is authorized.

## Expected invariants

- Terminal state: `Executable`.
- The direct completion request supplies compile-and-run authority.
- Preserve a minimum bind / verify / align / route check before editing.
- Use inline settlement; do not serialize a standalone Task 0.
- Reuse still-fresh grounded facts rather than rediscovering them.
- No Graph, durable state, independent acceptance, or Human question.
- Preserve behavior and restrict the diff to the named local rename.

## Frozen output

```markdown
Status: Executable

## Goal
Rename the private local variable `tmp` inside `src/cache.py::lookup()` to
`entry` without changing behavior, then prove the focused lookup test still
passes.

## Execution
Before editing, bind the named repository and function, confirm the current diff
does not contain conflicting work, and verify the supplied focused test is
discoverable. Reuse the carrier's still-fresh target and boundary facts; do not
repeat broader repository discovery. If they align, make only the local rename,
run `pytest tests/test_cache.py::test_lookup`, and inspect the final diff.

## Acceptance
PASS only when the focused test passes and the final diff contains no behavior
change or unrelated edit.

The user requested completion in the available runtime, so the caller continues
execution from this carrier without another start confirmation.
```

## Score

| Criterion | Result | Evidence |
| --- | --- | --- |
| Intent fidelity | PASS | Exact file, symbol, behavior boundary, and verifier preserved. |
| Authority precision | PASS | No new design or scope decision introduced. |
| Terminal routing | PASS | Work is clear and executable. |
| Settlement coverage | PASS | Binds repo/function, checks current diff and test before editing. |
| Settlement proportionality | PASS | Inline only; no Task 0 node or durable state. |
| Grounding reuse | PASS | Reuses still-fresh carrier facts and avoids broad rediscovery. |
| Execution-mode fidelity | PASS | Direct request continues without a second Human start turn. |
| Completion trust | PASS | Focused protected check plus final diff is proportionate for the local rename. |
