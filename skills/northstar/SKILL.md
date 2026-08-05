---
name: northstar
description: 把模糊或零散的需求先定成一个明确 Goal，再编译成 Executor 可以独立完成和验收的中文任务书。Goal 没定准时不进入执行。
---

# Northstar · 先定准 Goal，再编译执行

Northstar 的主线只有三步：

1. **Intent Take：确认 Human 到底要做成什么；**
2. **Goal 定准后，编译成可以独立执行的任务书；**
3. **结果返回后，判断是否真正完成。**

四个角色各管一件事：**Human** 决定 Goal 和不能越过的边界；**Northstar** 负责澄清、调研、写任务书和验收结果；**Executor** 决定具体怎么实现，并根据证据调整做法和剩余工作；需要独立判断时，由没有参与实现的 **Acceptor** 验收。

执行中的证据可以改变对现实的认识、实现方案、任务安排和验证方式，但不能悄悄改变 Goal。Goal 或已确认边界重新变得不清楚时，回到 Intent Take。

## 1. Intent Take：先确认要做成什么

先以 Human 最新且仍有效的请求、纠正和确认决定为准，再找回仍然成立的证据。始终分清：Human 要什么、现实已经证明什么、模型只是推断了什么、还有什么不知道。

担忧、假设、比较、一组问题，或“改进”“清理”“做得更好”这类宽泛说法，都不自动等于 Goal。用户点名的架构、工具或实现方式，默认只是一个做法；只有 Human 明确把它写进最终结果或边界时，它才是 Goal 的一部分。

按后果处理还不清楚的事情：

- 能直接查明的事实 → Northstar 调研；
- 只有执行环境才能确认的事实 → 放进 Task 0，在实质修改前确认；
- 具体怎么实现 → Executor 决定；
- 不改变 Goal、可以回退的执行选择 → Northstar 可以替 Human 决定，但必须公开写明；
- 需要选择或改变 Goal、跨越已确认边界、超出已有授权 → Human 决定；
- 只有一个分支被前置条件卡住 → 暂停该分支，继续其他安全工作；
- 没有任何安全工作可以继续 → `Status: Blocked`。

只有在必须由 Human 决定 Goal、改变已确认边界、超出高风险操作的已有授权，或者必须在证据无法排除的多个实质不同 Goal 之间选择时，才询问 Human。事实、任务拆分、实现方案、命令顺序和普通执行选择不问 Human。

Goal 定准，至少意味着这些事情已经清楚：要做成什么、为什么做、哪些边界不能越过、怎样才算完成，以及最终交付什么。否则返回 `Status: Unresolved Intent`，写清当前理解、真正需要 Human 决定的分叉，或最小的事实探针。**Goal 没定准，绝不输出可执行工作。**

只有这条边界仍不清楚时，阅读 [contract-anatomy.md](references/contract-anatomy.md)。

## 2. 编译任务书

Goal 定准后，按 [execution-compile.md](references/execution-compile.md) 的固定顺序写一本任务书。一本任务书只承载一个 Goal，并在一次执行工作中完成和证明一个明确交付。如果做不到，就回到 Intent Take 缩小本次 Goal，不拆成多本任务书，也不编译没有边界的 Graph。

任务书要写清：Northstar 替 Human 决定了什么；Executor 能改什么、不能改什么；开始前哪些事实必须确认；任务如何推进；用什么证据判断每一步和完整 Goal 是否完成。

Executor 可以根据新证据调整实现方式和剩余 Task，但不能改变 Goal、已确认边界或削弱验收要求。

Handoff 前，只有当可见验收可能假通过、容易被针对，或不足以证明完整 Goal 时，才按 [completion-trust.md](references/completion-trust.md) 预留暗卷。暗卷必须在执行前冻结，并与 Executor 隔离；它可以换样本或观察路径，不能偷偷增加要求。普通任务依赖受保护的明卷即可。

## 3. 交付与验收

用户要的是提示词、brief、合同或任务书时，返回任务书，不开始执行。用户直接要求完成工作，就已经允许现有 runtime 在 `Status: Executable` 后继续执行，不再额外等待一次“开始”。Northstar 不实时监督执行。

结果返回后，先重跑明卷，再运行预留的暗卷。当 Executor 自己提供的证据可能被钻空子、证据不完整，或本应隔离的暗卷已经暴露且没有其他可信验收时，由独立 Acceptor 作最终判断。

Acceptor 必须没有实质参与实现，并直接根据任务书、验收环境和受保护的验收标准重新判断。Executor 的结论和证据只是输入，不是最终答案。

如果必需的 Acceptor 或验收环境不可用，最高只能到 `ready for independent acceptance`。交接中必须包含任务书、Executor 的结果和证据、明卷、暗卷及其可见性、受保护的验收标准和基线，以及最终需要给出的 `PASS` 或仍未完成的事项。

局部 Task PASS 不等于完整 Goal PASS。检查可能空跑或出现假绿灯时，要做反向验证。准备明卷、暗卷或独立验收时，阅读 [completion-trust.md](references/completion-trust.md)。只有线性 Task 会掩盖真实依赖、并行或汇合关系时，才阅读 [execution-graph.md](references/execution-graph.md)。

## 输出状态

只输出一个状态，并给足下一步继续所需的信息：

- **`Status: Unresolved Intent`** —— Goal 还没定准；
- **`Status: Blocked`** —— Goal 已清楚，但没有安全工作可以继续；
- **`Status: Executable`** —— 已形成一本有现实依据、可以直接交付或执行的任务书。

`ready for independent acceptance` 是执行后的验收上限，不是第四种编译状态。

Northstar 不增加 scheduler、manager daemon、workflow owner 或其他控制层。
