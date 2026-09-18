# Accepted surrounding context

- The SDK exposes protobuf message fields through generated field references.
- Singular message and repeated message fields must share one caller-facing
  access abstraction.
- Callers must not branch on which protobuf container supplied a value.
- Scalar, map, mutation, serialization, error, and code-generation behavior is
  outside this local interface-shape decision and remains unchanged.
- The wider product Intent, architecture choice, and verification judgment are
  owned outside this local draft.
