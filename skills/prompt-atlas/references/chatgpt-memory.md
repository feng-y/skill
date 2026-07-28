# ChatGPT Memory adapter

Use this only when ChatGPT has already supplied relevant Memory, project context, files, or connected-app context. It compiles task-relevant meaning into the current Intent Contract; it does not provide a Memory API or store raw memory.

## Consume safely

- The current request owns intent; current repo, config, tests, and runtime evidence own territory. Treat Memory as a candidate hint beneath both.
- Map relevant Memory into Goal, Current Context, Boundary, Immediate Task, or Success / Stop; do not create a sixth field.
- Reuse stable motivations, decisions, rejected directions, preferences, and completion expectations only when they change this task.
- Derive Immediate Task primarily from the current request. Verify remembered repo facts before relying on them.
- If Memory conflicts with the current request, follow the current request. Ask one question only when two still-relevant hints imply different directions.

## Make it portable

- Carry forward task meaning, not chat history, personal details, or Memory mechanics.
- Produce a self-contained contract that never tells another agent to “check my memory.”
- Never copy private Memory into a repo automatically. When cross-task persistence is needed, propose a user-approved, repo-scoped, reviewable home.
- When the user explicitly asks to update this skill, fold back only stable Intent Take behavior and replace the owning rule instead of appending a memory log.

Do not claim access to unavailable Memory, require an export unless missing history blocks intent, or surface unrelated sensitive context.
