# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取。本文件只拥有最终 Intent 的物理结构；judgment 与 ready 条件由 `rules.md` 拥有。

```markdown
# Architecture Intent

Status: Architecture intent ready

## Direction
- Intent:
- Why now:
- North-star source:
- North-star contribution:
- Desired end state:
- Primary architecture direction:

## Reality
- Area:
- Observed pressure:
- Structural consequence:
- Why architectural rather than local:
- Decisive evidence:

## Boundary
- In scope:
- Out of scope:
- Must preserve:

## Design obligations
- <only obligations supported by this intent>
- Replacement / exit:

## Progressive Brooks constraints

| Risk | Design constraint | Why applicable | Guard | Proof expected |
| --- | --- | --- | --- | --- |

## Challenge
- Counterexample checked:
- Applicable guard: <only when needed>

## Success evidence
- Stable acceptance rule:
- Replacement evidence:
```

只有真实存在 Material Unknown 时，才在 `Success evidence` 前追加：

```markdown
## Material unknown
- Claim at risk:
- Minimal probe:
- Evidence:
- Intent changed / retained:
```

只有 affected scope 会动态变化或 snapshot 有助于 grounding 时，才在末尾追加：

```markdown
## Current snapshot evidence
- Scope derivation:
- Current snapshot:
```
