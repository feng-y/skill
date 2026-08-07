# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取和输出。

```markdown
# Architecture Intent

Status: Architecture intent ready

## Direction
- Intent:
- Why now:
- Desired end state:

## Reality
- Area:
- Observed pressure:
- Structural consequence:
- Why architectural rather than local:
- Key evidence:

## Boundary
- In scope:
- Out of scope:
- Must preserve:

## Design obligations
- Business semantics to unify or keep distinct:
- Essential variations to preserve:
- Capability / ownership question to resolve:
- Dependency direction to establish:
- Old path, knowledge or dependency that must exit:

## Unknown and guard
- Key Unknown:
- How it was closed or why it does not block intent:
- Counterexample checked:
- Applicable guard:

## Success evidence
- Evidence that the intent was implemented correctly:
- Evidence that replacement actually happened:
```

## Discipline

- 一个 intent，不输出候选清单；
- 描述 outcome，不提前指定实现模式；
- `Observed / Inferred / Unknown` 不混写；
- 必须说明为什么不是局部修改；
- 必须保留真实业务差异和 Protected behavior；
- 必须提出至少一个具体退出目标；
- Brooks 只用于风险校准，不输出全量风险表或 Health Score；
- 目标设计、任务拆分、迁移步骤和实现属于后续工作。
