---
name: architecture-evolution
description: 用于架构方向模糊、只有历史模块或“应该改进什么”这类输入：从真实变化压力和代码现实中构造一个有证据、有边界、可继续设计的 Architecture Intent。目标设计或实现已经明确时不使用。
---

# Architecture Evolution · 从模糊方向构造架构 Intent

North Star：**把模糊的架构担忧、模块问题或改进方向，收敛成一个有证据、有边界、可继续设计或执行的 Architecture Intent。**

本 Skill 不负责完成目标架构、实现计划或代码改造。它解决的是更早的问题：

> 当前真正值得推进的架构意图是什么？

一次只构造一个 intent。

## Context loading

1. 先用本文件恢复变化压力并推进主流程；
2. 需要 architecture judgement 时读取 [rules.md](references/rules.md)；
3. 涉及历史 mode、compat、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时，按需读取 [legacy-lenses.md](references/legacy-lenses.md)；
4. intent 基本稳定后按需读取 [brooks-constraints.md](references/brooks-constraints.md) 做 challenge；
5. 最后读取 [intent-contract.md](references/intent-contract.md) 输出；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行不读。

`SKILL.md` 只拥有 Flow；`rules.md` 拥有 architecture judgement；`intent-contract.md` 只拥有输出形状。不要在多个文件重复同一规则。

## 何时使用

使用：架构方向仍模糊，需要从历史模块、重复症状、变化压力或代码现实中判断真正值得推进的方向。

跳过：局部 bug、机械迁移、明确 code review；目标架构和实现边界已经稳定；用户已经要求完整设计或直接实现；只有审美不满而没有真实压力。

## Flow

### 1. Ground

恢复最小现实：

- `Area`：本轮模块或能力范围；
- `Pressure`：重复变化、事故、维护摩擦、调用者知识或业务变化；
- `Evidence`：代码、调用、测试、配置、历史或运行事实；
- `Boundary`：最小上下游、明确不做什么。

始终分开 `Observed / Inferred / Unknown`。没有真实 pressure 时返回 `Status: No architecture intent`。

### 2. Discover

从 pressure 背后的结构原因找 intent，不从模式名出发。需要区分业务语义、ownership、consumer reassembly、dependency 或局部问题时使用 `rules.md`。

找一个最能解释主要压力、边界清楚、并能说明什么旧知识/路径/责任会退出的方向。必要时补足形成背景：当前结构原来依赖什么合理前提，哪个前提现在已经失效。

### 3. Shape

Architecture Intent 只需要说清：

- **What**：真正应该演化什么；
- **Why now**：为什么当前结构已经不再合适；
- **Desired end state**：完成后调用者、业务语义、ownership 或依赖关系有什么不同；
- **Boundary**：in scope / out of scope / must preserve；
- **Replacement / exit**：什么旧知识、路径、判断、责任或依赖应该消失。

如果确有少量不同的基本架构形态值得后续设计比较，可以简单点出 identity；只说明“是什么”，不展开具体设计。

Intent 到这里停止。具体 module/class/API、responsibility placement、调用流、迁移和实现属于后续 Target Design。

### 4. Challenge

只挑战会改变 intent 或 boundary 的问题：它是否其实是局部修复、是否错误统一不同 bounded context、是否只是转移复杂度、consumer reassembly 是否仍存在、ownership 是否越过 evidence 支持的 invariant、是否真的有 replacement / exit。

需要时使用 `rules.md` 和 `brooks-constraints.md`。它们是 judgement，不是最终输出章节。

仍存在会改变 intent 或 boundary 的 Material Unknown 时返回 `Status: Intent unresolved`；已关闭的 unknown 不保留为 active blocker。

## Output

只返回一个状态：

- **`Status: No architecture intent`** — 当前压力不足，或问题属于局部修改；
- **`Status: Intent unresolved`** — 一个关键 Unknown 或 Human 决定仍会改变方向；
- **`Status: Architecture intent ready`** — 输出一个有证据、有边界、足以继续目标设计的 Architecture Intent。

最终输出跟随用户主要语言；代码符号、文件名和稳定协议名称可以保留原文。
