---
name: architecture-evolution
description: 用于架构方向模糊、只有历史模块或“应该改进什么”这类输入：从真实变化压力和代码现实中构造一个可讨论、可继续设计的 Architecture Intent，说明真正的架构问题、形成背景、目标方向、边界以及必要时少量可能的目标架构 identity。目标设计或实现已经明确时不使用。
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
4. intent 基本稳定后读取 [brooks-constraints.md](references/brooks-constraints.md)，用相关约束挑战、缩小或保护当前判断；Brooks 是内部 reasoning lens，不是最终输出 section；
5. 最后读取 [intent-contract.md](references/intent-contract.md) 输出稳定 intent；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行禁止读取。

语义归位保持简单：本文件拥有运行主线；`rules.md` 拥有 architecture judgment / discriminator；`brooks-constraints.md` 只拥有内部 architecture challenge 约束；`intent-contract.md` 只拥有输出形状；`validation.md` 只拥有 regression/eval。不要在多个位置维护同一套 authoritative 判断。

本 Skill 吸收 opportunity finding、improve 和 design grilling 的判断，并直接保留 Brooks 架构约束；不调用或编排外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill。

## Language

最终输出跟随用户当前主要语言。内部 taxonomy、reference 或英文源码不改变输出语言；代码符号、类型名、文件名和必须保持稳定的协议名称可以保留原文。

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
- `Unknown`：会改变 intent、boundary 或目标 architecture identity 的未决事实。

Architecture reality / judgment 遵循 `rules.md` 的 lifetime：相关前提未变就复用；authoritative Evidence 改变前提时只 reopen 并替换受影响判断，不保留冲突的 active snapshot。

没有真实压力时返回 `Status: No architecture intent`。

### 2. Discover the intent

从压力背后的结构原因寻找方向，而不是从模式名出发。先形成能解释主要 pressure 的 **architecture problem identity**：哪项业务语义、ownership、consumer knowledge、dependency 或 replacement 关系真正失配，以及它为什么不是局部 cleanup。

常见信号包括：

- 同一业务存在多套语义或事实解释；
- 共同语义存在，但实现差异泄漏给调用者；
- 完整能力没有内聚 owner；
- 稳定 policy 被易变 implementation 或场景反向牵引；
- 新抽象持续增加，但旧路径和旧知识没有退出。

同时恢复形成背景：当前结构原来依赖什么合理前提、variation 或历史阶段；哪个前提现在已经失效，导致原 boundary 与现实错位。

需要比较时只保留少量有证据方向，不评分。选择一个最能解释当前压力、边界最清楚、且能说明什么将消失的 intent。已知热点也必须证明它值得升级为架构 intent。

### 3. Shape the intent

Architecture Intent 只回答：

- **Problem**：真正的架构问题是什么，为什么它不是局部修改；
- **Background / Why now**：当前变化压力，以及使现有结构失去合理性的历史前提或现实变化；
- **Direction**：哪项能力或结构应该发生什么方向性变化；
- **Desired end state**：完成后业务、调用者、ownership 或依赖关系有什么不同；
- **Possible target identities**：仅在一个 intent 下确有多个值得后续设计比较的基本形态时，给出 1–3 个 architecture identity；只描述核心 ownership / semantic / dependency identity 与主要取舍，不规定具体落法；
- **Boundary**：in scope / out of scope / must preserve；
- **Replacement / exit**：至少说明一种当前旧知识、路径、判断、责任或依赖应当退出；
- **Unknown**：如果存在会改变 intent、boundary 或目标 identity 的 material unknown，说明其风险和最小关闭方式；没有则不制造。

Intent 描述结果和基本架构形态，不提前规定 class、interface、API、factory、strategy、registry、adapter、对象组合、调用流程、迁移步骤、实现任务或 verification plan。用于解释现实的 role、provider、support、variation 或 ownership distinction，不自动成为新的架构 artifact。

涉及 ownership 时，必须区分“当前 capability 要闭合什么”与 request/execution/orchestration、相邻 subsystem 的 ownership relation；只有 evidence 支持时才扩大 owner scope。Possible target identities 可以指出“ownership 更可能落在哪类稳定边界”，但不能替后续目标设计做具体 responsibility placement。

### 4. Challenge and constrain the intent

从当前仍有效的 best-known intent 出发找反证，不重新执行已经有有效 Evidence 支撑的 architecture analysis。重点只挑战会改变方向、边界或目标 identity 的问题：它是否其实只是局部修复，是否 false-unify 不同 bounded context，是否把历史差异或 current partition 固化成长期 contract，是否只转移复杂度或 consumer reassembly，ownership 是否越过 evidence 支持的 invariant，replacement / exit 是否真实，以及是否存在 Human-owned 业务或兼容决定。需要更细 discriminator 时读取并复用 `rules.md`，不在这里维护第二套 checklist。

如果存在 Material Unknown，必须通过 `claim at risk → minimal probe → evidence → intent changed / retained` 影响判断；只命名 unknown 而不改变下一步，不算关闭。已经关闭且前提未变化的 Unknown 不重新打开。

方向稳定后按需读取 `brooks-constraints.md`。Brooks R1–R6 只作为内部 challenge lens：用于拒绝、缩小或保护会造成 cognitive overload、change propagation、knowledge duplication、accidental complexity、dependency disorder 或 domain distortion 的 intent / target identity。不要把 Brooks 编号、风险表、proof expectation 或 challenge 过程直接输出给用户；只有实际改变 Architecture Intent 的结果，才以普通架构语言沉淀到 Direction、Boundary、Must preserve 或 Replacement / exit。

反证改变方向时替换或缩小受影响 intent；约束不适用时只在 reasoning 中保留必要 guard。

### Stop line

当 architecture problem、形成背景、目标方向、边界以及必要时少量 possible target identities 已经足够让后续目标设计继续时停止。

如果输出开始回答下面问题，说明已经越过 Architecture Evolution 的边界，应停止并交给后续目标设计：

- 具体 class / interface / API / adapter 应该是什么；
- 具体 responsibility 应落在哪个对象或函数；
- 具体执行、调用、构造或数据流如何编排；
- 具体 migration、implementation slice、任务拆分或 verification 如何完成。

## Output

只返回一个状态：

- **`Status: No architecture intent`** — 当前压力不足，或问题属于局部修改；输出决定性证据和局部边界。
- **`Status: Intent unresolved`** — 输出当前理解、一个关键 Unknown、最小探针或 Human 决定，以及它会改变什么。
- **`Status: Architecture intent ready`** — 读取 `intent-contract.md`，输出一个有证据、有边界、足以继续目标设计且不越界到具体设计的 Architecture Intent。

本 Skill 的终点是稳定 intent。目标设计负责把 architecture identity 物化成具体架构决定；任务书、实现和完整验收属于后续工作。
