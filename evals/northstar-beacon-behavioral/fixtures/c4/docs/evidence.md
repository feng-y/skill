# Current evidence

- An old production instance has collection enabled and object target 20, but
  31 rounds produced no accepted event; the drop reason is `zero_items`.
- The patch has passed a clean build, 22 focused tests covering zero/nonzero
  events and failure paths, and 200/200 replay on the available corpus.
- Replay compares existing responses. Its corpus has no valid zero-sized event.
- There is no corrected-version production object. Production instances still
  run the old build; capacity and upload confirmation have not been measured.
