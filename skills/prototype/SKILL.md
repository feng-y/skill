---
name: prototype
description: "A single caller-neutral engineering prototype tool: build or revise the prototype and draft for a commissioned problem, small or complex, and run the required disposable experiment. Return the artifact and observations; the caller owns composition, orchestration, and alignment with overall Intent."
---

# Prototype · 构建受托问题的原型与 draft

Prototype 是 **单一、caller-neutral、主要由 model 按需调用的工程原型工具**。调用方给定要解决的问题、相关上下文、边界和所需结果；Prototype 构建或修正该问题的原型与 draft，必要时执行可丢弃试验，再把产物与观察返回原 caller。任务可以小，也可以复杂，不按规模拆成不同 Skill，也不限定为一个字段或孤立 decision。

**组合不在 Prototype 内。** Northstar 或其他调用方选择和拼装不同问题的产物，组织调用顺序，维护整体 Draft，并判断与 Intent 的差距。Prototype 不选择或拼装不同问题的产物，不通过“受托组合”接管这项工作，也不调度新的 Prototype 调用。受托原型内部可以有多个必要部件；完成这一个问题的内部构建，不等于承担跨问题产物的组合。

Prototype 不拥有 canonical Intent / Issue，不决定长期 Target Architecture，不定义 proof obligation 或 verdict，不编译 execution Graph，也不进入生产实现。原型及 draft 可以是同一份产物，不强制两份文件；局部 draft 不成为整体 Intent 的另一份权威。

## 输入、调用与返回边界

从当前委托恢复：要解决什么问题、已确定的约束 / 接口、需要交回什么产物。复用已有上下文，不制造固定字段或新协议。普通构建可以使用调用方提供的代码、数据和已确认接口；这不授权 Prototype 选择或组合其他问题的方案。

- **Northstar** 可以委托某个具体问题的原型，或复杂原型中的缺失部分；它负责 Human 澄清、范围确认、组合和 Intent 对齐。
- **AE / Verify / Unknowns First / 其他 caller** 可以在各自问题已明确后调用相同工具。AE 保留结构判断，Verify 保留证明判断，Unknowns First 只关闭事实；返回原 caller，不自动经过 Northstar。
- **Human 直接委托**原型或实验时可直接执行，不要求先生成 Intent，也不把这项能力变成固定 Human-facing 阶段。

如果委托实际上是选择、拼装一组局部产物并匹配整体 Intent，说明该组合工作应由调用方完成；其中具体的构建缺口可以返回为下一项委托，不自行接管组合。不要因为原型较复杂就退出或替 caller 拆解全局任务。

长期 owner / boundary 本身未定时返回相应结构 owner；accepted outcome 或范围需要 Human 决定时返回 caller。现状 source / config / runtime 身份缺失可先作最小事实检查，必要时由 `$unknowns-first` 关闭；试验要测的可行性或成本未知不是拒绝试验的理由。

已有真实 artifact / backend、只需定义证明或判读 Evidence 时交 `$verify`。被 Verify 委托构建试验时，完成 artifact / observation 再交回，不能因它拥有 proof 判断就退回未完成的委托。既无形态缺口，也无待完成的明确试验委托，且只剩生产 implementation How 时不额外调用。

## 完成一个连贯的受托原型

共同决定当前问题的路径、dataflow、接口、boundary 或 lifecycle 应一起展开，直到产物能回答被委托的问题；不因一个局部演示完成就提前结束，也不为完整感穷尽实现细节。复用已有有效部分，correction 只重开受影响部分。

向 caller 交代产物解决什么、覆盖到哪里、依赖哪些条件，以及实际发现的接口冲突或缺口。这些是供调用方使用的边界信息，不是 Prototype 的组合方案、全局任务表或整体完成判断。问题超出当前边界时给出具体缺口，由 caller 决定补充委托、组合或 ask Human 收窄；不能自行丢弃原始要求。

## 按问题选择足够的表示或试验

**Core Path / Usage / Interface Draft**：形态、调用方式或交互理解是决定性问题时，用最便宜且足够的路径、状态、接口示例或 mock。静态表达已充分就不写可丢弃代码；不默认生成交互 HTML。

**Disposable Prototype**：选择依赖实际可行性、行为差异或成本，或当前明确要求实做时，构建并运行最小可丢弃代码 / timing probe，或复用已有可执行实验。图、计划和未运行代码不能替代明确实做。保持与被委托问题相符的语言、输入和环境，不用便于展示但无关的替代物冒充。

不为 production quality 补通用抽象、持久化、完整测试体系或 rollout；但回答当前问题必需的行为 / 等价性检查和匹配的 baseline/treatment 测量不能省略。Prototype 返回实际 observation；proof obligation、Evidence sufficiency 和 verdict 属于 Verify。试验观察不自动证明生产收益或整体 Acceptance。

候选对照只服务于当前受托问题，使用可比条件；明确委托的检查不因展示数量而静默丢弃。返回差异和局限，不替 caller 采用方案，也不把候选的选择 / 组合扩展成全局原型管理。

## 输出与停止

返回受托原型与 draft、适用边界、依赖 / 未决点，以及实际完成的观察。实做需保留可复现入口和输入 / 配置身份，区分已运行、未运行及不足以判断。结果不必是正收益；已完成但 inconclusive 的试验可返回，不授权无限追加。

受托工作完成或遇到真实 blocker 后交回原 caller。caller 负责后续组合、Human 交互和整体对齐；局部完成不能宣布 Intent 已完成。Prototype 不输出组合计划、Taskbook、issue graph、PR split、全局进度或第二份 Intent SOT。
