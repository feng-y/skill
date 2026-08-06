# Architecture Evolution Rules

These rules turn broad architecture slogans into evidence-backed diagnosis and design. Use the first four as primary architecture rules. Use the final rule as a design gate that rejects false improvement.

For every rule, move through:

```text
Signals → Diagnosis → Counterexample → Design move → Improvement proof
```

A signal is not a conclusion. Choose one primary violation per run.

## Rule 1 — One responsibility or variation has one owner

### Intent

A stable responsibility, business fact, or variation dimension should have one canonical place that interprets and owns it. Other modules consume its result instead of repeating the interpretation.

### Signals

- one feature repeatedly changes the same set of modules;
- provider/family/mode switches appear in several responsibilities;
- the same config, capability, state, or business rule is interpreted more than once;
- multiple modules each hold a partial view required to assemble one decision;
- a new implementation requires edits in factory, executor, parser, metrics, and callers;
- two paths can disagree about the same fact.

### Likely diagnosis

Responsibility or variation ownership is split. The system has several local interpreters instead of one canonical owner.

### Counterexamples

Do not merge merely because syntax is similar. Separate checks may express different responsibilities:

- parsing an external format versus choosing a runtime provider;
- validating an input versus enforcing an authoritative business rule;
- reporting a family label versus selecting family behavior;
- defensive fast-fail checks that deliberately mirror, but do not own, the rule.

State which layer is authoritative and why the other copies are projections or guards.

### Design move

- name the responsibility or variation precisely;
- assign one owner of the decision, state, or truth;
- make other modules consume a stable result, capability, or metadata;
- remove duplicate interpretation rather than centralizing only the enum or helper function;
- keep projections clearly non-authoritative.

### Improvement proof

- number of interpretation sites decreases;
- a new variant changes one owner and bounded adapters, not the stable flow;
- conflicting truth sources disappear;
- callers no longer reconstruct the same decision.

## Rule 2 — Stable flow does not depend on volatile implementation detail

### Intent

Code that expresses the stable business or execution flow should depend on a stable contract. Provider, family, storage, transport, deployment, or optimization details depend toward that contract, not the reverse.

### Signals

- core flow imports or switches on concrete implementation types;
- public contracts expose provider-specific config or runtime objects;
- a stable module constructs, initializes, or orders concrete implementations;
- common code depends on a scenario-specific module;
- both sides include or call each other;
- an abstraction is defined by the provider in a way that forces the consumer to depend on provider details;
- tests require the real implementation because no meaningful stable seam exists.

### Likely diagnosis

The dependency direction follows current code layout or construction order rather than stability and responsibility. Volatile detail leaks into the stable decision path.

### Counterexamples

Do not invert every dependency mechanically:

- a concrete type may itself be the durable domain contract;
- a single internal implementation may not justify a public seam;
- an implementation detail that never varies and is fully hidden may remain internal;
- performance-critical paths may deliberately use concrete representation, but the tradeoff must be explicit and local.

### Design move

- define the contract from the stable consumer's needs;
- keep provider-specific construction and selection behind an owner surface;
- pass capability or result, not implementation internals;
- keep implementation-specific configuration on the implementation side;
- add a seam only when real production/test adapters or current variation prove it is useful.

### Improvement proof

- adding or replacing an implementation does not modify stable flow;
- concrete type knowledge disappears from core decisions;
- dependency graph becomes directional without a new pass-through layer;
- public surface contains domain needs rather than provider mechanics.

## Rule 3 — A module hides complexity; callers do not reassemble capability

### Intent

A module earns its existence when callers can invoke a coherent capability through a small interface while behavior, state, order, error handling, and implementation choices remain inside.

### Signals

- wrappers mostly forward parameters and methods one-to-one;
- callers invoke several methods in a required but undocumented order;
- callers fetch config, runtime state, type, token, manager, and adapter separately, then assemble behavior;
- interface complexity approaches implementation complexity;
- many pure helpers were extracted for testability, while integration bugs remain in orchestration;
- tests pierce private state or duplicate internal call sequences;
- deleting a module would make complexity vanish rather than reappear in callers.

### Likely diagnosis

The seam is placed around files or classes, not around a coherent capability. Complexity is exposed or relocated instead of hidden.

### Counterexamples

- small pure functions can be valuable when their contract is complete and composition is genuinely the caller's responsibility;
- a thin adapter may be correct at an external transport seam;
- orchestration may belong to a higher-level owner when lower-level modules intentionally expose primitives;
- line count is not depth.

Apply the deletion test: if deleting the module merely removes indirection, it is likely shallow; if required knowledge spreads back across callers, it may be earning its keep.

### Design move

- identify the complete capability callers actually need;
- move ordering, state transitions, validation, and error translation behind one seam;
- reduce methods, parameters, special cases, and required external knowledge;
- keep test-only seams internal;
- merge shallow modules when their separation creates caller reconstruction;
- delete middle layers that add no leverage.

### Improvement proof

- callers use fewer steps and concepts;
- public interface shrinks while behavior remains available;
- tests verify observable capability through the same seam callers use;
- complexity becomes local rather than reappearing in helpers or callers.

## Rule 4 — Independent change reasons have independent responsibility boundaries

### Intent

Responsibilities that change for independent reasons should not share one owner, lifecycle, or mutable state merely because they currently execute together.

### Signals

One module mixes several of:

- business semantics;
- input adaptation or serialization;
- provider selection and object construction;
- metrics, tracing, logging, debug dump;
- caching, batching, memory layout, latency optimization;
- compatibility fallback or migration state;
- runtime lifecycle and resource ownership.

Different changes edit disjoint parts of the same module or require unrelated reviewers and tests.

### Likely diagnosis

The module boundary follows current execution order or file history rather than one coherent reason to change. Primary and auxiliary responsibilities are falsely bound.

### Counterexamples

Do not split every concern into a public module:

- observation may remain a private internal collaborator;
- a performance optimization may belong inside the capability because callers must not see it;
- code that changes together to preserve one invariant may be cohesive even if it has several steps;
- physical file size is not evidence by itself.

### Design move

- state the primary responsibility in one sentence;
- classify other concerns as intrinsic behavior, internal implementation, adapter, observer, policy, compatibility boundary, or removable history;
- separate only when the change boundary, ownership, or verification surface is genuinely independent;
- prefer private composition before creating public layers.

### Improvement proof

- the primary owner can be described without “and also” chains;
- auxiliary concerns no longer influence business decisions;
- unrelated changes stop modifying the same responsibility surface;
- state and lifecycle are owned where they are actually needed.

## Design Gate — Replace, do not layer

### Intent

An architecture design is an improvement only when it reduces knowledge, duplication, invalid dependency, or historical structure. A new layer is not progress by itself.

### Rejection signals

- the old path remains canonical while a new wrapper sits beside it;
- a new interface has one adapter and no current test or variation need;
- a registry centralizes names but decisions still remain scattered;
- code moved, but old facts, state, and special entry points remain live;
- the target file shrinks while helpers and callers inherit the same complexity;
- both old and new tests remain because the new seam cannot express the real behavior;
- the design promises future flexibility but removes nothing today.

### Counterexamples

Temporary coexistence can be legitimate during a migration, but the design must state:

- which path is authoritative now;
- what evidence allows traffic/consumers to move;
- the deletion condition;
- the maximum residual boundary.

### Design move

Every `Design ready` result must specify:

- `Keep` — current responsibilities and contracts that remain;
- `Move` — responsibility or state moving to a new owner;
- `Merge` — duplicate interpretation or shallow modules becoming one capability;
- `Delete` — old switches, paths, wrappers, facts, tests, or entry points that should disappear;
- `Do not change` — protected scope preventing redesign drift.

### Improvement proof

- at least one concrete knowledge burden, duplicate decision, invalid edge, or obsolete path is removed;
- the new seam replaces rather than shadows the old one;
- temporary migration residue has an explicit exit condition;
- no improvement claim relies only on cleaner naming, new types, or a tidier diagram.
