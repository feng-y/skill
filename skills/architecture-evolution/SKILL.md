---
name: architecture-evolution
description: 用于架构方向模糊、只有历史模块或“应该改进什么”这类输入：从真实变化压力和代码现实中构造一个有证据、有边界、可继续设计的 Architecture Intent。目标设计或实现已经明确时不使用。
---

# Architecture Evolution · 从模糊方向构造架构 Intent

North Star：**把模糊的架构担忧、模块问题或改进方向，收敛成一个有证据、有边界、可继续设计或执行的 Architecture Intent。**

本 Skill 不完成目标架构、实现计划或代码改造。一次只构造一个 intent。

## Context loading

1. 本文件只负责 Flow；
2. 需要 architecture judgement 时读 [rules.md](references/rules.md)；
3. 遇到历史 mode、compat、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时按需读 [legacy-lenses.md](references/legacy-lenses.md)；
4. intent 基本稳定后按需读 [brooks-constraints.md](references/brooks-constraints.md) challenge 判断；
5. 最后读 [intent-contract.md](references/intent-contract.md) 输出；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行不读。

同一规则只放一个 owner；不要在 Flow、judgement 和 output contract 之间重复维护。

## 何时使用

使用：架构方向仍模糊，需要从历史模块、重复症状、变化压力或代码现实中找出真正值得推进的方向。

跳过：局部 bug、机械迁移、明确 code review；目标架构和实现边界已稳定；用户已要求完整设计或直接实现；只有审美不满而没有真实 pressure。

## Flow

**1. Ground。**恢复最小现实：本轮 area、真实 pressure、决定性 evidence、最小 boundary。始终区分 `Observed / Inferred / Unknown`。没有真实 pressure 就返回 `Status: No architecture intent`。

**2. Discover。**从 pressure 背后的 structural cause 找 intent，不从模式名出发。需要 architecture judgement 时用 `rules.md`。找一个最能解释主要压力、边界清楚、并能说明什么旧知识/路径/责任会退出的方向；必要时解释当前结构原来依赖什么合理前提、哪个前提现在已经失效。

**3. Shape。**把 best-known judgement 收敛成一个 bounded Architecture Intent，结构见 `intent-contract.md`。如果确有少量基本架构形态值得后续设计比较，可以简单点出“是什么”；不物化具体 Target Design。

**4. Challenge。**用 `rules.md`，必要时加 `brooks-constraints.md`，只挑战会改变 intent 或 boundary 的判断。仍有这类 Material Unknown 就返回 `Status: Intent unresolved`；否则保留收敛后的 intent。

## Output

只返回一个状态：

- **`Status: No architecture intent`** — 当前压力不足，或问题属于局部修改；
- **`Status: Intent unresolved`** — 一个关键 Unknown 或 Human 决定仍会改变方向；
- **`Status: Architecture intent ready`** — 输出一个有证据、有边界、足以继续目标设计的 Architecture Intent。

具体 module/class/API、responsibility placement、调用流、迁移和实现属于后续 Target Design / execution。

最终输出跟随用户主要语言；代码符号、文件名和稳定协议名称可以保留原文。
