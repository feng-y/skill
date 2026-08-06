# Verify One Architecture Design

Use this during a normal Architecture Evolution run. It checks whether the proposed design improves the target structure. It does not evaluate the Skill itself and does not prove implementation correctness.

## Verification dimensions

For each applicable dimension, write `Before / Expected after / How to verify`.

### Change locality

Ask whether the same future change would require fewer modules, decisions, and tests.

Useful evidence:

- current and target interpretation sites;
- current and target files/modules touched by adding one representative variant;
- whether callers still coordinate the same behavior.

### Ownership concentration

Ask whether one responsibility, truth, state, or variation now has one authoritative owner.

Useful evidence:

- duplicate rules or state readers that disappear;
- authoritative owner and remaining projections/guards;
- whether two paths can still disagree about the same fact.

### Dependency stability

Ask whether stable flow depends only on stable needs rather than concrete implementation details.

Useful evidence:

- forbidden import/include/call edges removed;
- concrete provider/family checks removed from stable flow;
- implementation-specific config and lifecycle retained on the implementation side.

### Caller knowledge

Ask whether callers need to know fewer concepts, steps, states, ordering rules, special entry points, or implementation types.

Useful evidence:

- public methods/parameters before and after;
- required call sequence before and after;
- internal state/config no longer assembled by callers;
- tests no longer reproducing internal orchestration.

### Replacement

Ask what existing structure becomes unnecessary.

Useful evidence:

- switches, duplicate decisions, wrappers, legacy entries, fact sources, or old test surfaces that can be deleted;
- an invalid dependency or caller knowledge burden that disappears even when no file is deleted;
- for temporary coexistence, the authoritative path, migration evidence, and explicit deletion condition.

## Decision rule

A design is ready only when:

1. the primary rule violation has direct evidence;
2. the target owner and seam address the diagnosed root cause;
3. at least one observable burden decreases;
4. the design does not merely relocate complexity;
5. real business differences and protected behavior remain explicit;
6. replacement is concrete rather than promised as future flexibility.

If these cannot be shown, revise the design or return `No architecture change`, `Research required`, or `Decision required`.

## Claim boundary

This verifies the architecture design hypothesis only. A later implementation must separately prove behavior, compatibility, migration completion, and actual deletion with repository or runtime evidence.
