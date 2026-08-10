---
name: architecture-evolution
description: 用于架构方向模糊、只有历史模块或“应该改进什么”这类输入：把真实变化压力放回仍有效的上位架构目标，构造一个推进 AI-native 的 Architecture Intent。目标设计或实现已经明确时不使用。
---

# Architecture Evolution · 从模糊方向构造架构 Intent

本 Skill 只决定当前真正值得推进的 architecture intent；不完成 target design、实现计划或代码改造。一次只构造一个 intent。

## Flow

### 1. Ground

先读 repo entry，再进入目标代码和最近层 evidence。记录 `Pressure`、`Reality`、`North-star`、`Boundary`，并分开 Observed、Inferred 与会改变 intent 的 Unknown。

当输入问的是广义“下一步架构方向”，近处 evidence 只完成 pressure grounding。进入 Judge 前，以 area 名检索 repo 当前的 architecture / evolution source，记录全部明确将该 area 放入上位目标的命中；检索结果未记录时，Ground 未完成。

只展开会改变判断的 semantics、ownership/lifecycle、consumer knowledge、dependency 或 runtime control。涉及历史 mode、compat、registration、loader/provider identity 或 residual state 时，按需读取 [legacy-lenses.md](references/legacy-lenses.md)。

**完成：**能说明 pressure 的结构后果、area 与 North-star 的关系及最小边界；没有真实 pressure 时返回 `No architecture intent`。

### 2. Judge

读取 [rules.md](references/rules.md)，依次判断 architecture or local、outcome、primary lever 与 Real Evolution exit。

只保留一个 intent，不评分、不并列项目。Material Unknown 只做足以裁决它的最小 probe，并明确 judgment changed / retained。

**完成：**能够选择 `No architecture intent`、`Intent unresolved`，或一个 outcome 已稳定的 `Architecture intent ready`。

### 3. Shape

ready 时读取 [brooks-constraints.md](references/brooks-constraints.md)，只吸收当前方向命中的 constraints；再按 [intent-contract.md](references/intent-contract.md) 成文。

Intent 写 outcome，不提前完成 target design。Success evidence 证明稳定结果与真实 exit；动态 app/config/target 只作 snapshot。

**完成：**下游无需重新发现 why，仍能自主设计；intent 足以判断方向有没有兑现。

### 4. Challenge

用 `rules.md` 中最强的适用 guard 挑战当前 intent。反证成立就替换、缩小或转为 unresolved；不成立只保留最重要的 guard。

**完成：**方向与边界经得起关键反例；不把 challenge 扩成第二轮完整分析。

## Output

- **`Status: No architecture intent`** — pressure 不足或只需局部修改；给出证据与局部边界。
- **`Status: Intent unresolved`** — 一个 Material Unknown 或 Human decision 仍会改变方向；给出最小关闭方式。
- **`Status: Architecture intent ready`** — 按 intent contract 输出一个有证据、有边界、可继续设计且可验证的 intent。

本 Skill 不调用固定下游 Skill。目标设计、任务书、实现与完整验收属于后续工作。
