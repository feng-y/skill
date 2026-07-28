# Prompt Foundation

Use these five foundations as the result of intent intake. They are not visible headings or a form.

## Intent intake

Start before wording. Determine:

- what change the user really wants in the world or system;
- why the task exists now and what current judgment led to it;
- which facts are already established and which are discoverable;
- which semantic, scope, risk, or approval boundary the user is protecting;
- where this turn should stop rather than silently expanding into later work.

Do not ask the user for repo facts an agent can inspect. Ask only about human-held choices whose answer would change the goal, boundary, authority, or completion verdict. If the existing conversation already carries the answer, use it.

When the task depends on repo or runtime reality, use `unknowns-first` as a context-enhancement gate:

- identify Target / Territory / Unknown / Proof;
- probe only the first unknown that could materially change the contract;
- add verified facts to Current Context;
- leave unresolved route-changing unknowns as an explicit stopping or escalation boundary.

Do not expose the gate, a full unknown taxonomy, or the probe sequence in the final prompt unless the unknown map itself is the requested artifact.

## Five foundations

1. **Goal** — State the real problem and the change or result the user ultimately wants.
2. **Current Context** — State the current status and only the facts, evidence, or uncertainty that will affect judgment.
3. **Boundary** — State what must not change, drift, expand, or cross without approval. Distinguish genuine invariants from acceptable differences.
4. **Immediate Task** — State what this turn must accomplish without silently requiring every later stage.
5. **Success / Stop Condition** — State what verdict or observable evidence constitutes completion and when further expansion should stop.

Embed these five elements naturally. A good prompt normally reads as a few connected paragraphs, not as `Goal / Context / Boundary / Task / Done` fields.

## Contract, not execution script

Define the destination, current reality, semantic and approval boundaries, this turn's frontier, and the completion verdict. Leave investigation path, tool choice, and most intermediate checks to the model.

Do not expand a compact engineering request into:

- a full reasoning framework;
- a long audit checklist;
- several named prompting styles;
- fixed file or tool order;
- repeated analyze / reflect / review scaffolding.

Add a structured result list only when it makes the final verdict easier to review.

## Revision method

1. Recover the intent behind the request or existing prompt.
2. Find the one missing foundation that most affects model behavior.
3. Delete repetition, model-expanded process, and fake invariants.
4. Add the smallest useful context or boundary.
5. Express the intent as natural, human Markdown.
6. Check that the model still owns judgment while remaining inside the task boundary.

Source: `guides/prompt-foundation-structure.md` and `principles/transferable-principles.md` in [Prompt Atlas](https://github.com/feng-y/prompt-atlas), revision `5e9dd8f197827ec83be81790644db1f9667c6d65`.
