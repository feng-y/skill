Status: `ready for independent acceptance`

Implemented the parser migration in `/workspace/scratch/597e563ee8ac/eval/v3/runs/t2-atlas`.

- Canonical ownership:
  - `app/parser.py` now handles default and explicitly opted-in streaming parsing.
  - Both consumers import `app.parser.parse_request`.
  - Deleted `app/stream_parser.py`.
  - Search found one `parse_request` definition and no `stream_parser` references.

- Batch/default compatibility:
  - Unchanged suite: 2 tests passed.
  - Canonical and batch input containing `trace_id: 42` and `streaming: False` still returned only:
    `{"user_id": "7", "features": ["a"]}`.

- Streaming compatibility:
  - Default → `streaming: true`.
  - `trace_id: 42` → `"trace_id": "42"`.
  - `trace_id: None` → `"trace_id": "None"`.
  - `streaming: 0` → `false`.
  - `streaming: "yes"` → `true`.
  - `user_id` stringification and tuple-to-list feature normalization passed.

- Scope and quality:
  - `git diff --check` passed.
  - Only `README.md`, `app/parser.py`, `app/stream_consumer.py`, and deletion of `app/stream_parser.py` are changed.
  - No test, dependency, or batch-consumer changes.
  - Worktree has no generated cache files.

An independent verifier must still confirm the global gate before marking `MET`.
