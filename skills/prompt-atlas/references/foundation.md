# Prompt Foundation

Use these five foundations as the minimum completeness contract and skeleton for intent intake. They are not the only source of context, optional fields, visible headings, or a form, and they do not constitute a solution or spec.

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

Use available context in this closing order:

1. synthesize the current conversation, relevant project context, and memory into candidate intent;
2. verify discoverable territory facts through the repo, runtime, documents, or connected sources;
3. ask the user only for a human-owned decision or a contradiction that evidence cannot resolve.

Authority is typed rather than global. The user's latest explicit correction is authoritative about desired intent. Current repo, config, tests, and runtime evidence are authoritative about territory. Memory and prior descriptions are useful hints but cannot override either.

When the task depends on repo or runtime reality, use `unknowns-first` as the default context supplement:

- identify Target / Territory / Unknown / Proof;
- close one material territory unknown at a time, then re-evaluate the five foundations;
- add verified facts to Current Context, Boundary, or Success / Stop Condition as appropriate;
- leave unresolved intent-changing unknowns as the next user question or an explicit handoff boundary.

Use another relevant skill or tool when it can supply missing domain or artifact context. In every case, fold back only the facts that change the intent contract. Do not expose the supplement's framework, a full unknown taxonomy, or the probe sequence in the final prompt unless that map itself is the requested artifact.

## Five foundations

1. **Goal** — State the real problem and the change or result the user ultimately wants.
2. **Current Context** — State the current status and only the facts, evidence, or uncertainty that will affect judgment.
3. **Boundary** — State what must not change, drift, expand, or cross without approval. Distinguish genuine invariants from acceptable differences.
4. **Immediate Task** — State what the next engagement should clarify or accomplish without choosing the later solution path.
5. **Success / Stop Condition** — State when shared intent is clear enough to hand off and when further clarification would become design or specification.

Embed these five elements naturally. A good prompt normally reads as a few connected paragraphs, not as `Goal / Context / Boundary / Task / Done` fields.

Do not hand off while a missing foundation would force the receiving agent to guess the user's direction. A foundation may remain concise or contain an explicit unknown, but its effect on intent must be understood.

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
3. Close user-held ambiguities through one question at a time; close territory or domain facts through `unknowns-first` or another relevant context supplement.
4. Stop before solution selection, specification, planning, or execution.
5. Express the clarified intent as natural, human Markdown.

Source: `guides/prompt-foundation-structure.md` and `principles/transferable-principles.md` in [Prompt Atlas](https://github.com/feng-y/prompt-atlas), revision `5e9dd8f197827ec83be81790644db1f9667c6d65`.
