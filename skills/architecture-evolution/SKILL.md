---
name: architecture-evolution
description: 用于架构方向模糊、只有历史模块或“应该改进什么”这类输入：从真实变化压力和代码现实中构造一个可讨论、可验证的 Architecture Intent，说明应该演化什么、为什么、边界、渐进设计约束和成功证据。目标设计或实现已经明确时不使用。
---

# Architecture Evolution · 从模糊方向构造架构 Intent

North Star：**把模糊的架构担忧、模块问题或改进方向，收敛成一个有证据、有边界、可继续设计或执行的 Architecture Intent。**

本 Skill 不负责完成目标架构、实现计划或代码改造。它解决的是更早的问题：

> 当前真正值得推进的架构意图是什么？

输入可以是仓库局部、历史模块、业务能力、反复出现的问题，或一个尚未说清楚的方向。一次只构造一个 intent。

## Context loading

1. 先只用本文件恢复变化压力并判断是否存在架构 intent；
2. 需要区分候选方向、业务边界或架构性质时读取 [rules.md](references/rules.md)；
3. 涉及历史 mode、compat、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时，按需读取 [legacy-lenses.md](references/legacy-lenses.md)；
4. intent 方向稳定后读取 [brooks-constraints.md](references/brooks-constraints.md)，只吸收与当前方向相关的设计约束；
5. 最后读取 [intent-contract.md](references/intent-contract.md) 输出稳定 intent；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行禁止读取。

本 Skill 吸收 opportunity finding、improve 和 design grilling 的判断，并直接保留 Brooks 架构约束；不调用或编排外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill。

## 何时使用

使用：

- “这个历史模块应该往哪个方向改”；
- “下一步最值得做的架构演化是什么”；
- 用户给出多个症状，但尚未形成明确目标；
- 已知热点存在，但还不清楚它是局部修复、结构调整还是业务统一问题；
- 需要把代码现实转成可确认的架构方向。

跳过：

- 普通局部 bug、机械迁移或明确 code review；
- 目标架构、实现边界和成功标准已经稳定；
- 用户要求完整设计、任务书或直接实现；
- 没有真实变化、维护、理解或业务压力，只有审美不满。

## Flow

### 1. Ground the direction

恢复最小现实：

- `Area`：模块、能力或局部代码范围；
- `Prompt`：用户当前模糊表达、担忧或方向；
- `Pressure`：需求、重复修改、事故、维护阻塞、调用者知识或理解摩擦；
- `Evidence`：代码、调用、测试、配置、变更历史、运行事实或仍有效文档；
- `Boundary`：本轮最小上下游与明确不做什么。

需要判断结构原因时，分开观察业务语义、ownership/lifecycle、consumer reassembly、source dependency 和 runtime control/consumption；一个观察面整洁不能证明另一个观察面正确。

始终分开：

- `Observed`：证据直接证明；
- `Inferred`：证据支持的解释；
- `Unknown`：会改变 intent、boundary 或 design obligation 的未决事实。

没有真实压力时返回 `Status: No architecture intent`。

### 2. Discover the intent

从压力背后的结构原因寻找方向，而不是从模式名出发。常见方向包括：

- 同一业务存在多套语义或事实解释；
- 共同语义存在，但实现差异泄漏给调用者；
- 完整能力没有内聚 owner；
- 稳定 policy 被易变 implementation 或场景反向牵引；
- 新抽象持续增加，但旧路径和旧知识没有退出。

需要比较时只保留少量有证据方向，不评分。选择一个最能解释当前压力、边界最清楚、且能说明什么将消失的 intent。已知热点也必须证明它值得升级为架构 intent。

### 3. Shape the intent

Architecture Intent 只回答：

- **What**：哪项能力或结构应该发生什么方向性变化；
- **Why now**：当前变化压力和后果；
- **Desired end state**：完成后业务、调用者或依赖关系有什么不同；
- **Boundary**：in scope / out of scope / must preserve；
- **Obligations**：只写与当前 intent 相关、后续设计必须回答的业务语义、variation、ownership、consumer knowledge、dependency 或 replacement 问题；
- **Progressive constraints**：当前方向需要下游逐步吸收的 Brooks 架构设计约束；
- **Unknown**：如果存在会改变 intent 的 material unknown，说明其风险和最小关闭方式；没有则不制造；
- **Evidence of success**：描述稳定验收规则和 proof；会随 production config、deployment binding 或 changed ownership 变化的当前对象，只作为 snapshot evidence，不冻结为长期 contract。

Intent 描述结果，不提前规定 class、factory、strategy、registry 或迁移步骤。用于解释现实的 role、provider、support、variation 或 ownership distinction，不自动成为新的架构 artifact。涉及 ownership 时，必须区分“当前 capability 要闭合什么”与“request/orchestration 或相邻 subsystem 仍由谁拥有”。

### 4. Challenge and constrain the intent

先用代码现实挑战方向：

- 它是否只是局部修复或审美清理；
- 是否错误合并不同 bounded context；
- 是否把历史差异误当作长期业务差异；
- 是否会诱导 union interface、额外 wrapper 或 speculative seam；
- 是否只是转移复杂度；
- consumer 是否仍需重组 configuration、implementation、lifecycle、ordering、identity 或 access facts；
- 是否把 capability ownership 错扩成 request execution / orchestration ownership；
- 是否为了闭合当前 capability，吞并了相邻 subsystem 原本正确的 ownership；
- success evidence 是否把当前动态 app/target/config snapshot 错冻结成长期验收集合；
- 是否能指出旧路径、重复知识、调用者知识或反向依赖将退出；
- 是否存在 Human-owned 业务或兼容决定。

如果存在 Material Unknown，必须通过 `claim at risk → minimal probe → evidence → intent changed / retained` 影响判断；只命名 unknown 而不改变下一步，不算关闭。

方向稳定后按需读取 `brooks-constraints.md`。Brooks R1–R6 是后续架构设计需要逐步吸收的约束：intent 阶段只携带与当前 pressure 和 desired end state 直接相关的约束，不做全量扫描、评分、PASS/RETRY 或独立报告。

反证改变方向时修改或撤销 intent；约束不适用时写明关键 guard；约束是否真正满足由后续目标设计、实现和验收证明。

## Output

只返回一个状态：

- **`Status: No architecture intent`** — 当前压力不足，或问题属于局部修改；输出证据和局部边界。
- **`Status: Intent unresolved`** — 输出当前理解、一个关键 Unknown、最小探针或 Human 决定，以及它会改变什么。
- **`Status: Architecture intent ready`** — 读取 `brooks-constraints.md` 与 `intent-contract.md`，输出一个有证据、有边界、携带渐进设计约束且可验证的 Architecture Intent。

本 Skill 的终点是稳定 intent。目标设计负责吸收约束并形成架构决定；任务书、实现和完整验收属于后续工作。
