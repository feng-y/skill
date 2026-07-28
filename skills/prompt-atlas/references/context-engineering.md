# Context engineering filter

Apply these six shifts after intent is clear enough to hand off. They shape the final context; they are not six visible sections and do not extend intent intake into solution design.

## Six shifts

1. **Rules → judgment**
   - Keep explicit user decisions, real invariants, approval boundaries, and genuinely costly failure constraints.
   - Turn preferences and old universal prohibitions into contextual judgment, or omit them when a capable model can infer them.

2. **Examples → expressive intent**
   - Treat examples as evidence of direction, taste, vocabulary, or an important distinction.
   - State the underlying intent instead of making the model imitate the example. Leave tool-interface design to the owning tool or downstream capability.

3. **Upfront context → progressive disclosure**
   - Inline only the context needed to understand the intent and avoid the wrong problem.
   - Point to repo files, artifacts, or later discovery surfaces for task-specific depth rather than preloading everything.

4. **Repetition → one clear home**
   - Merge repeated hints into one authoritative statement and resolve contradictions before handoff.
   - Keep tool semantics beside the tool, repo truth in its owning source, and do not repeat them in the intent brief unless they change this request.

5. **Manual memory → distilled current intent**
   - Use conversation history and available memory as intake evidence, but do not replay the history in the final brief.
   - Carry forward only stable current intent. Do not assume auto-memory exists or treat memory as current repo truth; durable team truth still belongs in reviewable, version-controlled sources.
   - On ChatGPT surfaces, apply [chatgpt-memory.md](chatgpt-memory.md) when relevant memory or project context is already available.

6. **Simple prose specs → rich references**
   - Prefer high-fidelity references such as code, tests, mockups, artifacts, traces, and rubrics when they clarify meaning better than paraphrase.
   - Prompt Atlas stops before specification: references constrain the intended problem and evidence space, not the implementation solution.

## Guardrails

- Do not optimize for a deletion percentage or minimum character count.
- Do not remove safety, permission, business, or irreversible-action boundaries.
- Do not hide a route-changing ambiguity to make the brief look concise.
- Do not turn this filter into a repo-wide context audit.

Adapted from Thariq Shihipar, “The new rules of context engineering for Claude 5 generation models”: [accessible X article](https://x.com/trq212/status/2080710971228918066); publisher provenance: `https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models`.
