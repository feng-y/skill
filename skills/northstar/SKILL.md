---
name: northstar
description: 把用户的一句话想法或零散要求，整理成中文的 Agent 提示词、brief、Goal、执行合同或自主任务书。意图、证据、边界或成功标准还不稳定时尤其适用：补足完成当前判断所需的最小 context，用证据先消解 material Unknown，只路由剩余未决项，意图没定准就不进入执行。
---

# Northstar · 先定准目标，再写成能独立执行的任务书

Northstar 沿着一条固定 Flow 推进工作：

1. **Intent Take：定准 Human 真正要完成的 Goal；**
2. **编写任务书：把 Goal 写成可独立执行的合同；**
3. **Handoff：按用户授权交付或继续执行；**
4. **Acceptance：用完整证据判断是否真正完成。**

Skill 固化的不是大段上下文或冻结的执行细节，而是每个节点的 judgment：当前还缺什么 context、谁应该决定、什么时候已经足以继续、什么证据足以证明完成。Context 是动态的，只为完成当前 Intent Take、Goal/Task 描述或验收判断补足最小必要信息。

`Unknown` 是这套 judgment 中处理未决事项的机制，不是额外控制流。只有仍可能改变 Goal、验收要求、已确认边界、明确交付的可行性，或可信完成证明的不确定性，才是 Intent Take 需要处理的 material Unknown。事实 Unknown 优先用证据消解；只有剩余的未决项才进入责任路由。

所有进入执行的路径，最终都要形成一个类 Goal 合同：一个内部一致的 Goal、有现实依据的 Task 与依赖、清楚的授权，以及分层证明。开发工作使用成本最低且足够的 Task 局部验证，在组合行为成立的 Task Group 边界运行更大范围验证，相关工作收敛后再执行完整 Goal 验收。验证成本决定检查放在哪里和多久运行一次，但不能成为省略必要证明的理由。

四个角色：**Human** 决定 Goal、验收要求、已确认边界、明确提出的优先级和授权；**Northstar**（调研、写书和验收者）负责澄清、写任务书、交付并验收返回结果；**Executor**（执行者）独立执行任务书，负责稳定意图内的 implementation judgment，并可以根据证据调整实现范围和剩余工作；需要独立判断时，由未参与实现的 **Acceptor**（独立验收者）作最终验收。证据可以修正事实、可行性判断、实现工作和证明需要，但不能悄悄改变 Goal。Goal、验收要求或已确认边界重新变得不确定时，回到 Intent Take。

## 流程

### 0. 接住并定准意图（Intent Take）

先以 Human 最新且仍有效的请求、纠正和确认决定为准，再找回仍然成立的证据。始终分清四件事：Human 真正要什么、现实已经证明什么、模型推断了什么、还有哪些 Unknown。

Context 增强只服务于把 Intent Take 做完整：补足会改变 Goal、验收要求、已确认边界、明确交付可行性或可信证明路径的现实与证据；不要为了建立全面背景而大幅扩展无关上下游。

担忧、假设、比较、一组问题，或“改进”“清理”“做得更好”这类宽泛说法，都不自动等于 Goal。先查到足以看清真正选择为止，不替 Human 发明目标。

结果和手段要分开。用户点名的架构、工具或实现方式，默认只是对实现方式的一个假设；只有 Human 明确把它写进 Goal 或已确认边界时，它才是硬约束。

先用与后果相称的证据消解事实 Unknown，并用证据支撑 Human-owned 的选择。Human 持有 Goal、验收要求、已确认边界、明确提出的优先级和授权；稳定意图内的实现判断属于 Executor。优先使用成本最低且权威的来源：repo/config/test/runtime 观察、外部调研、probe/replay/prototype，或从其他人那里取得的信息。其他人的输入只是 evidence source，不产生第二个 Human authority。只路由仍未解决的部分：

- 当前可查事实 → 调研；
- 只有执行环境才能确认的事实 → Task 0（实质修改前的执行预检）；
- 怎么实现 → Executor；
- 不改变 Goal、验收要求或已确认边界，而且可以回退的选择 → Northstar 可以替 Human 做公开且未确认的 delegated default；
- 会改变 Goal、验收要求、已确认边界、Human 明确提出的优先级或授权的剩余选择 → Human；
- 前置条件暂时不可用，但还有独立工作可做 → 暂停受影响分支并记录；
- 前置条件不可用，而且没有安全工作可继续 → `Status: Blocked`。

只有剩余选择会改变 Goal 或验收要求、跨越或放宽已确认边界、改变 Human 明确提出的优先级、超出高风险操作的已有授权，或者必须在证据无法裁决的多个实质不同 Goal 之间选择时，才询问 Human。

意图已定准，意味着这些事情已经清楚：唯一、内部一致且由 Human 决定的 Goal、为什么做、已确认边界、重要证据现状、怎样才算真正且可信地完成，以及最终交付什么。否则返回 `Status: Unresolved Intent`，写清当前理解和最小有效问题或探针。**意图未解决，绝不输出可执行工作。**

仅在这条边界仍不清楚时阅读 [contract-anatomy.md](references/contract-anatomy.md)。

### 1. 调研（Research）

自己能查的一律先查，不拿事实问题问 Human。只补足会改变当前判断或任务书的 context；证据已经足以继续时就停止扩展。核对真实工作区、具有约束力的规格和测试、关键命令、基线、依赖以及受保护的判卷标准（测试、schema、验收脚本、CI、基线等）。文档和命令名都先当作待验证声明：README 里的命令可能已经不存在，lint 可能只是 `echo` 出一个假绿灯，文件也可能因为无人 import 而从覆盖率报告里消失。只有执行环境才能回答的内容，放进 Task 0。

Handoff 前先识别本次 verification focus：由 Goal、completion properties、change impact/reachability 和主要 failure risk 决定哪些属性最需要重点证明；再读取相关 repo verification authority。已知事实触发的 mandatory gate 必须编译进任务书，执行期才能确认的 trigger 放进 Task 0，预期 `0-diff` 不得降级已触发 gate。

重要结论必须能回到它的证据。摘要可以携带 claim 和 source pointer，但不会因为被总结或写进交接而自动变成 proof；后续决定或判卷依赖某个属性时，保留对应的权威来源、reference 或可复现观察。

### 2. 提问（Ask）

只问 Human 必须决定且尚未解决的事。优先一轮问完，最多五个决定；每个给出选项和推荐。事实、任务拆分、架构如何实现、命令顺序和普通执行选择，不问 Human。

Northstar 替 Human 作出的决定必须标明仍未由 Human 确认，摆到明面上，并写清依据、猜错的代价、如何发现以及如何回滚。它只能处理可逆的执行选择，不能改变 Goal、已确认边界、验收要求、Human 明确提出的优先级或授权。不公开就等于越权；摆到明面才保留了 Human 的决定权。

### 3. 编写任务书

按 [execution-compile.md](references/execution-compile.md) 的固定合同顺序写任务书。各节职责不能混，细节多少随任务而变；替 Human 作出的决定必须放在执行之前，让 Human 在 Handoff 前看见 Northstar 代为选择了什么。

Context 增强只为了把 Goal 和 Task 描述到 Executor 能独立判断、执行和验收的程度。只写当前起点、边界、授权、关键依赖和证明需要；大段背景通过引用保留，不把任务书扩展成全局知识库。

编译 Execution 前，先把 Goal 收敛成有限、互不替代的 completion properties，形成 Completion Contract；只保留当前 Goal 必要的完成条件，不固定类别，也不能用一个属性的证据替代另一个。

任务书先写 completion properties，再用 verification focus 编译 mandatory gates 和 evidence provider；verification focus 只是判断，不新增任务书章节或固定字段。具体检查从 repo verification system 中选择，仅在入口本身是受保护判卷标准、权威基线或能显著消除歧义时点名。

一本任务书只承载一个 Goal，并在一次执行工作中完成并证明一个明确交付。如果做不到，就回到 Intent Take 缩小 Human 本次要的交付，不拆成多本任务书，也不编译无边界 Graph。

意图定准后，已确认边界和不可削弱的证明要求仍然具有约束力。证据变化时，Executor 可以调整实现方式和剩余工作。

开发任务要在不增加额外流程阶段的前提下编译三种证明粒度：每个 Task 使用成本最低且足够的局部证明；一组 Task 共同形成模块能力、共享合同或汇合结果时，在最小 Task Group 边界运行 repo verification system 中覆盖组合属性的更大范围验证；所有相关 Task Group 收敛后运行完整 Goal 验收。昂贵检查按证明范围、已有实测或可靠成本，以及延迟发现失败的恢复代价安排执行位置。

Handoff 前，只有在明卷可能假通过、可被钻空子或不足以证明 Goal 已完成时，才按 [completion-trust.md](references/completion-trust.md) 预留私有验收（暗卷）；否则依赖受保护的明卷和判卷标准。暗卷不进入 Executor 可见的任务书；runtime 能隔离上下文时，也不进入 Executor 上下文。暗卷可以采用任务书未列出的样本或不同观察路径，不能增加隐藏要求。

### 4. 交付（Handoff）

用户只要普通提示词、brief 或合同时照常返回文本。输出 `Status: Executable` 时，把同一份任务书正文写入 OS/runtime 提供的临时目录中的一个 Markdown 文件；路径必须在当前 repo/workspace 之外且不能硬编码 `/tmp`。TUI 可以同时显示正文、摘要和路径，但 Executor 只从该文件启动，不从 conversation 重建；写入失败时可以返回文本，但不得声称已进入执行。

用户直接要求完成工作，就已经授予 compile-and-run 权限：文件写好后，用一个薄 launcher 启动 Executor，不再额外等一次“开始”：

```text
Read <TASKBOOK_PATH> as the authoritative contract. Execute toward its Goal; Tasks are the current dependency graph, not the completion condition. Loop: observe → run ready work → verify with the repo's applicable verification system → update evidence/graph. Replan as evidence changes without changing Goal, boundaries, authority, or mandatory gates. Stop only when Goal is proven, no safe work remains, or an explicit budget ends.
```

launcher 只负责驱动任务书；Northstar 不实时监督执行。Executor 返回后继续进入同一条 Acceptance，由 Northstar 保留 Goal-level 判卷权。

### 5. 验收（Acceptance）

Northstar 对照同一份权威任务书的 Goal、Completion Contract、已确认边界和 mandatory gates 判卷；Executor 的 `done`、`PASS` 和自带证据都只是验收输入，不是最终 verdict。若 Goal 与边界仍稳定但仍有未满足 property、缺失或 stale evidence、未完成 mandatory gate，就把这些 focused gaps 返回给 Executor，继续同一本任务书而不是重编；只有继续推进必须改变 Goal、验收要求、已确认边界、Human 明确优先级或授权时，才回到 Intent Take/Human。

结果返回后，重跑明卷（可见验收）和所有预留暗卷（私有检查）。当 Executor 自证可能被钻空子、证据不完整或不足以证明 Goal 已完成时，绑定独立 Acceptor；本应是暗卷的检查已经对 Executor 可见、又没有其他受保护的判卷标准能证明 Goal 完成，也属于这种情况。

Acceptor 只有在未实质参与实现，并直接对照权威任务书、验收环境和受保护的判卷标准重新判断时，才算独立。Executor 的结论和证据只是验收输入，不是最终判断。

如果所需 Acceptor 或验收环境不可用，最高只能到 `ready for independent acceptance`。返回一份自包含验收交接：权威任务书、Executor 结果与证据、明卷、暗卷及其可见性、受保护的判卷标准和基线，以及最终报告要求——`PASS`，或准确列出仍未满足的事项。

局部 Task PASS 和 Task Group PASS 可以解锁后续工作，但都不等于完整 Goal PASS。保护判卷标准和基线；检查可能静默失效时，要做反向验证。准备或执行私有/独立验收，或者检查可能假通过时，阅读 [completion-trust.md](references/completion-trust.md)。

## 输出

只输出一个状态，并给足让下一条路继续所需的信息：

- **`Status: Unresolved Intent`** —— 当前理解、尚未解决的 Goal 分叉或重要后果，以及最小的 Human 决定或证据探针；
- **`Status: Blocked`** —— 准确的非意图阻塞，以及恢复安全推进所需的条件；
- **`Status: Executable`** —— 一本有现实依据的自主任务书；用户要求直接完成工作时，编译后按 Handoff 继续执行。

`ready for independent acceptance` 是 Executable 之后的验收上限，不是第四种编译状态。

Northstar 不增加 scheduler、manager daemon、workflow owner 或其他控制层。
