# Prompt Foundation

Use these five foundations to clarify intent. They are not visible headings or a form, and they do not constitute a solution or spec.

## Intent intake

Start before wording. Determine:

- what change the user really wants in the world or system;
- why the task exists now and what current judgment led to it;
- which scattered facts, examples, preferences, rejections, and corrections reveal the same underlying intent;
- which facts are already established and which are discoverable;
- which semantic, scope, risk, or approval boundary the user is protecting;
- what the next interaction is actually for;
- where clarification should stop before solution design begins.

Do not ask the user for repo facts an agent can inspect. Ask only about human-held choices whose answer would change the goal, boundary, authority, or completion verdict. If the existing conversation already carries the answer, use it.

Treat hints according to their evidential role. Preserve explicit facts and corrections, use examples to infer direction rather than mandatory form, use rejections to sharpen boundaries, and ask about material contradictions. Do not expose this classification unless the user asks how the intent was reconstructed.

When the task depends on repo or runtime reality, use `unknowns-first` as a context-enhancement gate:

- identify Target / Territory / Unknown / Proof;
- probe only the first unknown that could materially change the contract;
- add verified facts to Current Context;
- leave unresolved intent-changing unknowns as the next user question or an explicit handoff boundary.

Do not expose the gate, a full unknown taxonomy, or the probe sequence in the final prompt unless the unknown map itself is the requested artifact.

## Five foundations

1. **Goal** — State the real problem and the change or result the user ultimately wants.
2. **Current Context** — State the current status and only the facts, evidence, or uncertainty that will affect judgment.
3. **Boundary** — State what must not change, drift, expand, or cross without approval. Distinguish genuine invariants from acceptable differences.
4. **Immediate Task** — State what the next engagement should clarify or accomplish without choosing the later solution path.
5. **Success / Stop Condition** — State when shared intent is clear enough to hand off and when further clarification would become design or specification.

Embed these five elements naturally. A good prompt normally reads as a few connected paragraphs, not as `Goal / Context / Boundary / Task / Done` fields.

## Intent brief, not solution or spec

Define the desired change, current reality, semantic and approval boundaries, next engagement, and clarification stopping point. Leave solution choice, investigation path, tool choice, implementation design, and acceptance specification to the capabilities that follow intent intake.

Do not expand a compact engineering request into:

- a recommended solution or architecture;
- a specification or acceptance checklist;
- an implementation plan or ticket breakdown;
- a full reasoning framework;
- a long audit checklist;
- several named prompting styles;
- fixed file or tool order;
- repeated analyze / reflect / review scaffolding.

The intent is ready when the user and agent agree on the problem, desired change, relevant context, protected boundary, and next engagement without needing to pretend the solution is already known.

## Revision method

1. Recover the intent behind the request or existing prompt.
2. Find the first missing foundation that could make the agent solve the wrong problem.
3. Close user-held ambiguities through one question at a time; close territory facts through minimal evidence.
4. Stop before solution selection, specification, planning, or execution.
5. Express the clarified intent as natural, human Markdown.

Source: `guides/prompt-foundation-structure.md` and `principles/transferable-principles.md` in [Prompt Atlas](https://github.com/feng-y/prompt-atlas), revision `5e9dd8f197827ec83be81790644db1f9667c6d65`.
