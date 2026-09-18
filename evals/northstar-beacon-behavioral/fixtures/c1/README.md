# Hermes request fixture

Hermes evaluates protobuf-like requests. `SpecificationPB` is the established
input. `ModelRequestPB` was added later and currently takes a compatibility
path that rebuilds a complete `SpecificationPB` before evaluation.

The generated message classes are represented by separate Python dataclasses;
they intentionally expose matching singular-message, repeated-message, scalar,
and ordering semantics. Treat them as distinct generated types even though
their fields line up in this fixture.

Observable constraints:

- `run_spec` output and behavior are the compatibility baseline.
- `run_model_request` must remain behaviorally equivalent for the same logical
  values.
- `rebuild_specification` models the expensive full conversion and increments
  an observable counter.
- `python3 -m unittest discover -s tests -v` is the complete fixture test suite.
