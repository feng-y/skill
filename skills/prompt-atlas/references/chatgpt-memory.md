# ChatGPT Memory extraction and fold-back

Use this adapter only when ChatGPT has already made relevant memory, project context, files, or connected-app context available to the current response. It has two jobs:

1. compile task-relevant meaning into the current requested intent brief or prompt;
2. when the user explicitly asks to preserve stable intent-taking lessons, fold them back into the skill's canonical files.

It does not store raw memory or provide a Memory API.

## Capability boundary

- Do not claim to have read memory that is not present in the current context.
- Do not require Memory for Prompt Atlas to work. Fall back to the current conversation and other context suppliers.
- Do not copy personal memory into the skill, repo, prompt, or final brief merely to preserve it.
- Do not ask the user to export memory unless the missing history itself materially blocks intent clarification.
- Assume Claude Code, Codex sub-agents, and other receiving agents cannot access ChatGPT Memory.

## Map memory into the five foundations

- **Goal**: use stable goals and repeated motivations as candidate intent; the current request or correction wins.
- **Current Context**: use prior decisions and project history as leads, then verify current repo, document, or runtime facts.
- **Boundary**: reuse stable preferences, rejected directions, approval limits, and known invariants only when relevant now.
- **Immediate Task**: derive it primarily from the current request; do not resurrect an old task from memory.
- **Success / Stop Condition**: reuse stable expectations about what fulfills the requested work, what evidence matters, and where scope should stop, but do not invent a full acceptance specification.

Memory adds evidence to these foundations; it does not create a sixth field.

## Cross-agent handoff

Treat Memory as a private source and the intent brief as its portable compilation target:

1. select only memory-derived meaning that changes this task;
2. rewrite it as current Goal, Current Context, Boundary, Immediate Task, or Success / Stop context;
3. omit personal history, source mechanics, and unrelated preferences;
4. hand off a self-contained brief that does not say “check my memory” or require ChatGPT access.

For a single task, the intent brief is the portable artifact; do not create a second context block. When the same context must persist across tasks or tools, propose a user-approved, repo-scoped, reviewable context file that follows the target repo's existing convention. Never write private Memory into a repository automatically.

## Durable intent-take fold-back

When Memory and repeated conversation reveal a stable preference about how intent intake should work, extract the rule rather than the conversation that produced it. Persist it only when the user asks, or when the current task explicitly includes updating this skill.

Route each lesson to one authoritative home:

- core role, invariant, or workflow → `SKILL.md`;
- five-foundation meaning and intake criteria → `references/foundation.md`;
- ChatGPT-specific Memory consumption → this file;
- context compression and reference use → `references/context-engineering.md`;
- directly usable execution-prompt defaults → `references/conditional-execution-hints.md`.

Before writing, distinguish:

- stable intent-taking preference from one-task context;
- explicit correction from a passing reaction;
- reusable judgment from an example to imitate;
- user intent from repo or runtime fact.

Update or replace the owning rule instead of appending a history log. Reconcile duplicated or superseded wording so another agent gets one current contract. Do not create a generic “memory dump” reference: Claude Code and other agents need the distilled skill behavior, not ChatGPT's private source history.

## Relevance and conflict filter

Keep a memory item only when it changes the interpretation, boundary, or stopping point of the current request. Prefer:

1. the user's current explicit statement for desired intent;
2. current project or repo evidence for territory;
3. relevant recent project context;
4. broader memory as a candidate hint.

If memory conflicts with the current request, follow the current request without asking. If two still-relevant memories imply materially different directions and the current request does not resolve them, ask one focused question.

Do not surface unrelated, sensitive, or surprising personal details. Use memory silently unless attribution is necessary to resolve a conflict or the user asks how the intent was reconstructed.

## Product boundary

ChatGPT Memory may synthesize context from chats, files, and connected apps. Projects can provide project-scoped chats, files, and instructions. The exact availability depends on the user's product surface and settings, so keep this adapter capability-based rather than plan- or UI-specific. This capability is used only on the producing ChatGPT side; receiving agents consume the compiled brief and their own available evidence.

Official product references:

- [Memory FAQ](https://help.openai.com/en/articles/8590148)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in)
