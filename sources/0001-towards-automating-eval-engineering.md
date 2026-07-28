---
title: Towards Automating Eval Engineering
author: Viv (@Vtrivedy10)
published: 2026-07-23
source: https://x.com/Vtrivedy10/article/2079976006644072796
kind: learning-source
---

# Towards Automating Eval Engineering

Structured learning notes derived from Viv's article about the LangChain Eval Engineering Skill. Read the [original article](https://x.com/Vtrivedy10/article/2079976006644072796) for the source narrative.

## Core idea

Eval engineering can be partially automated without pretending that an agent can infer the right business judgment in one shot. A coding agent can inspect a repository and production traces, propose capabilities worth evaluating, and build executable evals. The user remains in the loop to choose the valuable directions, decide what should run live or be simulated, and iteratively approve tasks and verifiers.

The resulting division of labor is:

- repository and traces supply observable agent behavior;
- the skill proposes eval directions and constructs the environment;
- the user contributes domain judgment and approves what is worth measuring;
- Harbor provides a reproducible task, environment, verifier, and execution record.

## Workflow

1. Inspect the agent surface: prompts, models, tools, skills, hooks, backing data, services, and API calls.
2. Mine traces when available to observe real tool arguments, results, errors, recurring requests, and failure modes.
3. Propose agent abilities and eval directions instead of generating a final suite in one shot.
4. Interview the user about business value, live dependencies, simulations, cost, permissions, and production-write boundaries.
5. Build and run a task, then inspect both the agent trajectory and verifier trajectory.
6. Revise the instruction, environment, or verifier when the eval measures the wrong proxy or permits shortcuts.
7. Keep the task environment stable while comparing models, prompts, tools, and agent versions.

## Harbor task model

Each eval is represented as:

```text
evals/<task-id>/
├── task.toml
├── instruction.md
├── environment/
└── tests/
```

The three semantic components are:

- **Instruction** — the task presented to the agent.
- **Environment** — a Docker-based reproduction of relevant tools, data, permissions, state, and dependencies.
- **Verifier** — executable judgment of whether the intended capability was demonstrated.

Harbor records trajectories, artifacts, rewards, and errors so the same eval can be replayed against different agent configurations.

## Why iteration matters

The first verifier is rarely trustworthy enough. Inspecting the agent and verifier trajectories can reveal:

- irrelevant citations used to satisfy a citation-count proxy;
- claims that an action occurred when it did not;
- answer material accidentally exposed in the environment;
- completion of a measurable proxy without completion of the real task;
- unrealistic mocks or missing production failure modes.

These failures are evidence that the task, environment, or verifier needs revision, not merely that the agent needs another prompt.

## Continual improvement loop

```text
mine traces
  → identify a recurring capability or failure
  → build an eval
  → improve the agent or harness
  → rerun against the stable eval
```

In this framing, production traces are a continuing data source, and evals become reusable targets for prompt, tool, harness, model, or fine-tuning changes.

## Relevance to this repository

This source supports a broader agent-engineering model:

- **Prompt Atlas** clarifies the intended change and protected boundary without prematurely selecting a solution.
- **Unknowns First** identifies missing territory and proof, then selects the smallest useful repo, trace, runtime, or user probe.
- **Eval Engineering** converts business judgment into executable tasks, environments, and verifiers.
- **An orchestration layer** can then execute and iterate while eval gates prevent unsupported completion claims.

The important human contribution is not merely approving generated test cases. It is deciding which capabilities matter, what production behavior must be represented, which shortcuts invalidate the result, and when an evaluator is trustworthy enough to gate autonomous work.

## Questions worth carrying forward

- How can tacit project experience be turned into candidate abilities without flattening it into generic evaluators?
- How should evaluator quality be calibrated against human judgment?
- How can trace failures be converted into versioned regression evals with low friction?
- How should the system distinguish agent failure, environment failure, and verifier failure?
- Which dependencies must remain live, and which should be simulated for cost, safety, privacy, or reproducibility?
- How can eval suites detect reward hacking and drift as the product changes?
