# 稳定意图：先确认到底要做什么

只有在“这个请求是否已经包含一个可执行 Goal”仍不清楚时，才读本文件。

## 问题空间不是 Goal

担忧、假设、比较、混合问题、彼此冲突的结果，以及“改进”“简化”“优化”“清理”“现代化”这类宽泛动词，通常只是在描述问题空间。先补足证据，把真正需要选择的地方显露出来；不要因为模型有一个看似合理的建议，就把它当成 Human 已经决定的 Goal。

结果和手段要分开。被点名的架构、工具、迁移或实现方式，可能只是 Human 当前对实现方式的猜想。只有 Human 明确把它写进 Goal 或已确认边界时，它才是必需项。

## 谁决定什么：Human、现实和推断不要混

- **Human** —— 决定 Goal、哪些结果/行为可以接受、明确提出的优先级、验证要求、批准事项和边界；
- **现实** —— 已有证据；它可以修正事实判断、可行性、实现工作和 Verification 需要；
- **推断** —— 模型的理解、建议或推荐；
- **Unknown** —— 后果还没有定下来的事项。

证据可以证明某条建议路线走不通，但不能替 Human 改变 Goal。Human 明确验证要求保持 binding，但属于 Verification authority，不写回 Goal 本体。

这里的 Unknown 只指仍可能改变 Stable Intent、Human verification authority 或关键执行事实的不确定性。普通 implementation How 属于 Executor，可以在 Stable Intent 关闭后继续保持未决。

## Context 与 Unknown

Intent Take 只补足形成 Goal 所需的最小 context：最新且仍有效的 Human 表达、会改变选择的现实证据和已确认边界。Human 明确验证要求如果存在，单独保留给 Verification；不要为了建立全面背景而把无关上下游带进来。Context 已经足以区分不同 Goal 时就停止扩展。

Unknown 的具体 evidence reduction、责任路由和 delegated default 合同统一定义在 [SKILL.md](../SKILL.md)。本文件只保留 authority model 和 Stable Intent closure，不再重复另一套路由表。

## 什么时候才算目标定准

Goal 定准至少要清楚这些事情：唯一、内部一致且由 Human 决定的结果、为什么做、本次工作要达到什么状态、必须保持什么、已确认边界、存在时 Human 明确提出的优先级、重要现实证据，以及最终交付什么。

Human 明确验证要求不决定 Goal 是什么，但必须在进入执行前被准确保留为 Verification 的 binding input。

如果仍有多个实质不同的 Goal 都说得通，返回 `Status: Unresolved Intent`：写清当前理解、不同选择的后果、必要时给出推荐，并提出最小问题或探针。不要输出可执行工作。