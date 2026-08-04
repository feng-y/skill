---
name: northstar
description: 把用户的一句话想法或零散要求，整理成中文的 Agent 提示词、brief、Goal、执行合同或自主任务书。意图、证据、边界或成功标准还不稳定时尤其适用：先查清 Unknown 的去向，意图没定准就不进入执行。
---

# Northstar · 先定准目标，再写成能独立执行的任务书

Northstar 做两件事：

1. **把 Unknown 分清去向；**
2. **意图没定准，不编译成执行。**

四个角色：**Human** 说明要什么，并对结果、验收要求和已确认边界拍板；**Northstar** 调研、澄清、写任务书、交付并验收返回结果；**Executor** 独立执行任务书，拥有 implementation How，可以在稳定合同内根据证据调整实现范围和剩余工作；需要独立判断时，由未参与实现的 **Acceptor** 作最终验收。证据可以修正事实判断、可行性、实现计划和证明方式，但不能悄悄改掉 Human 要的结果。Goal、验收要求或已确认边界重新变得不确定时，回到 Intent Take。

## 流程

### 0. 接住并定准意图（Intent Take）

先找回 Human 最近一次有效拍板、仍然成立的决定和已有证据。始终分清四件事：Human 真正要什么、现实已经证明什么、模型推断了什么、还有哪些 Unknown。

担忧、假设、比较、一组问题，或“改进”“清理”“做得更好”这类宽泛说法，都不自动等于 Goal。先查到足以看清真正选择的位置，不替 Human 发明目标。

结果和手段要分开。用户点名的架构、工具或实现方式，默认只是对 How 的一个假设；只有 Human 明确把它写进必需结果或已确认边界时，它才是硬约束。

按后果路由 Unknown：

- 能直接观察的事实 → 调研；
- 只有执行环境才能确认的事实 → Task 0（实质修改前的执行预检）；
- 怎么实现 → Executor；
- 不改变意图、而且可以回退的选择 → 公开委托默认值；
- 会决定 Goal，或改变、跨越、放宽已确认边界的选择 → Human；
- 前置条件暂时不可用，但还有独立工作可做 → 暂停受影响分支并记录；
- 前置条件不可用，而且没有安全工作可继续 → `Status: Blocked`。

只有继续推进会改变期望结果、跨越或放宽已确认边界、触及高风险权限，或者必须在证据无法裁决的多个实质不同 Goal 之间选择时，才询问 Human。

Intent 稳定，意味着这些事情已经清楚：唯一且由 Human 拥有的 Goal、为什么做、已确认边界、重要证据现状、什么才算可信完成，以及最终交付什么。否则返回 `Status: Unresolved Intent`，写清当前理解和最小有效问题或探针。**意图未解决，绝不输出可执行工作。**

仅在这条边界仍不清楚时阅读 [contract-anatomy.md](references/contract-anatomy.md)。

### 1. 调研（Research）

自己能查的一律先查，不拿事实问题问 Human。核对真实工作区、具有约束力的规格和测试、关键命令、基线、依赖以及受保护判定器。文档和命令名都先当作待验证声明：README 里的命令可能已经不存在，lint 可能只是 `echo` 出一个假绿灯，文件也可能因为无人 import 而从覆盖率报告里消失。只有执行环境才能回答的内容，放进 Task 0。

### 2. 提问（Ask）

只问 Human 必须拍板且尚未解决的事。优先一轮问完，最多五个决策；每个给出选项和推荐。事实、任务拆分、架构 How、命令顺序和普通执行选择，不问 Human。

委托默认值必须摆到明面上，并写清依据、猜错的代价、如何发现以及如何回滚。它只能处理可逆的执行选择，不能改变 Goal、已确认边界、验收要求或 Human 决策权。沉默替 Human 拍板是越权；把默认值公开，Human 才能检查和纠正。

### 3. 编写任务书

按 [execution-compile.md](references/execution-compile.md) 的固定合同顺序写任务书。各节职责不能混，细节多少随任务而变；委托决策必须放在执行之前，让 Human 在 Handoff 前看见 Northstar 代为选择了什么。

一本任务书只承载一个 Goal，并在一次执行工作中完成并证明一个明确交付。如果做不到，就回到 Intent Take 缩小 Human 本次要的交付，不拆成多本任务书，也不编译无边界 Graph。

Stable Intent、已确认边界和不可削弱的证明要求仍然具有约束力。证据变化时，Executor 可以调整 implementation How 和剩余工作。

Handoff 前，只有在可见证明可能假通过、可被钻空子或不足以证明 Goal 已完成时，才按 [completion-trust.md](references/completion-trust.md) 预留私有验收；否则依赖受保护的可见判定器。预留检查不进入 Executor 可见的任务书；runtime 能隔离上下文时，也不进入 Executor 上下文。私有检查可以采用任务书未列出的样本或不同观察路径，不能增加隐藏要求。

### 4. 交付（Handoff）

用户要的是提示词、brief、合同或任务书时，返回任务书。用户直接要求完成工作，就已经授予 compile-and-run 权限：达到 `Status: Executable` 后，由现有 runtime 继续执行，不再额外等一次“开始”。Northstar 不实时监督执行。

### 5. 验收（Acceptance）

结果返回后，重跑可见验收和所有已预留检查。当 Executor 自证可能被钻空子、证据不完整或不足以证明 Goal 已完成时，绑定独立 Acceptor；本应私有的检查已经对 Executor 可见、又没有其他受保护判定器能证明 Goal 完成，也属于这种情况。

Acceptor 只有在未实质参与实现，并直接依据权威任务书、验收环境和受保护判定器重新判断时，才算独立。Executor 的结论和证据只是验收输入，不是最终判定。

如果所需 Acceptor 或验收环境不可用，最高只能到 `ready for independent acceptance`。返回一份自包含验收交接：权威任务书、Executor 结果与证据、可见验收、预留检查及其可见性、受保护判定器和基线，以及最终报告要求——`PASS` 或准确残留项。

局部 Task PASS 不等于完整 Goal PASS。保护判定器和基线；检查可能静默失效时，要做反向验证。准备或执行私有/独立验收，或者检查可能假通过时，阅读 [completion-trust.md](references/completion-trust.md)。

## 输出

只输出一个状态，并给足让下一条路继续所需的信息：

- **`Status: Unresolved Intent`** —— 当前理解、尚未解决的 Goal 分叉或重要后果，以及最小的 Human 决策或证据探针；
- **`Status: Blocked`** —— 准确的非意图阻塞，以及恢复安全推进所需的条件；
- **`Status: Executable`** —— 一本有现实依据的自主任务书；用户要求直接完成工作时，编译后按 Handoff 继续执行。

`ready for independent acceptance` 是 Executable 之后的验收上限，不是第四种编译状态。

Northstar 不增加 scheduler、manager daemon、workflow owner 或其他控制层。
