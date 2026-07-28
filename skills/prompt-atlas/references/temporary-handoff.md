# Temporary Intent Take carrier

Use this carrier only when the user asks to hand the completed Intent Take to a fresh agent or session, or explicitly asks for the final artifact in temporary storage. The file changes where the Intent Contract is delivered, not what Prompt Atlas produces. Do not turn it into a general conversation summary, spec, plan, task breakdown, implementation sequence, or checklist.

## Location and delivery

- Create one Markdown file in the operating system's temporary directory, never in the current workspace. On Unix, use a unique path under a validated `${TMPDIR:-/tmp}` rather than a stable filename.
- Treat the file as ephemeral and keep it out of version control.
- Return the absolute file path in the final response without repeating the document's contents.

## Document content

Compile the conversation into:

1. one minimum-sufficient Intent Contract containing Goal, Current Context, Boundary, Immediate Task, and Success / Stop semantics;
2. references to existing artifacts needed to interpret that contract;
3. a `## Suggested skills` section naming relevant available skills and why the next agent should invoke them.

Fold material blockers and bounded unknowns into Current Context or Success / Stop rather than creating a separate project-status report. When the user passes arguments with the handoff request, treat them as the next session's focus and use them to select and emphasize relevant intent. Do not reinterpret them as permission to expand scope.

## Deduplication and safety

- Reference existing specs, plans, ADRs, issues, commits, diffs, and other artifacts by absolute path or URL instead of restating them.
- Preserve conclusions needed to understand the requirement, but omit conversation replay, investigation transcripts, project narration, and completed detail already recoverable from those artifacts.
- Redact credentials, API keys, passwords, tokens, private Memory content, personally identifiable information, and other sensitive values. Use a clear placeholder such as `[REDACTED]` when the omission itself matters.
- Suggest only skills relevant to the next focus. Do not turn the section into a catalog or claim unavailable skills are installed.

Keep the entire file within the normal Intent Take output budget in routine cases. When more context exists, reference its owning artifact instead of expanding the handoff.
