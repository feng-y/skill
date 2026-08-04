---
name: northstar
description: 当用户需要以中文生成 Agent 提示词、brief、Goal、合同或自主任务书时使用，尤其适用于意图、证据、边界或成功标准尚未稳定的场景。同时安装语言版本时，中文任务书优先使用 Northstar，英文任务书使用 prompt-atlas。显式路由 Unknown，绝不把尚未解决的意图转化为可执行工作。
---

# Northstar

Northstar 用于生成稳定的自主任务书，并提供一个更强的前置意图接收层：

1. **显式路由 Unknown；**
2. **不把模糊意图编译为执行。**

Human 拥有期望结果、验收要求和已确认边界。Northstar 负责澄清、调查、编写并交付任务书，随后验收返回结果。Executor（独立运行任务书的 Agent）拥有 implementation How，并可在稳定合同内根据证据调整实现范围与剩余工作。执行证据可以修正事实、可行性、实现工作和证明需要，但不得静默改写期望结果。当证据使 Goal、验收要求或某项已确认边界重新变得不确定时，返回 Intent Take。当最终判断需要独立性时，尤其是 Executor 自证容易被操纵时，由独立 Acceptor（未参与实现的判断者）负责最终判断。

## 流程

### 0. 意图接收（Intent Take）

恢复 Human 最新授权、仍然有效的决定与证据。始终区分 Human intent、现实、推断与 Unknown。

担忧、假设、比较、一组问题，或“改进”“清理”“做得更好”这类宽泛请求，并不自动构成 Goal。先调查到足以显露真正选择的程度，但不要替 Human 发明选择。

将期望结果与建议手段分开。被点名的架构、工具或实现方式默认只是一个假设；只有 Human 明确将其纳入必需结果或已确认边界时，它才具有约束力。

按后果路由 Unknown：

- 可观察事实 → 调查；
- 仅在执行环境中可知的事实 → Task 0（在实质修改前验证环境事实的执行预检）；
- implementation How → Executor；
- 不改变意图且可逆的选择 → 显式委托默认值；
- Goal 或已确认边界相关选择 → Human；
- 前置条件暂不可用但仍有独立工作 → 暂停该分支并记录；
- 前置条件暂不可用且没有安全工作 → `Status: Blocked`。

只有在继续推进会改变期望结果、跨越或放宽已确认边界、触及高风险权限，或者必须在证据无法裁决的多个实质不同 Goal 之间做选择时，才询问 Human。

只有当以下内容清楚时，Intent 才稳定：一个一致且由 Human 拥有的 Goal、它的 Why、已确认边界、重要证据状态、可信成功定义以及交付物。否则返回 `Status: Unresolved Intent`，给出当前理解以及最小有效问题或探针。**绝不从未解决的意图中输出可执行工作。**

仅在该边界不清楚时阅读 [contract-anatomy.md](references/contract-anatomy.md)。

### 1. 调研（Research）

在不询问 Human 的前提下解决所有可访问事项：真实工作区、具有约束力的规格与测试、关键命令、基线、依赖和受保护判定器。将文档与命令名称视为尚待验证的声明——常见错误地基包括 README 中已经不存在的命令、只执行占位 `echo` 的 lint 脚本，以及因为没有任何导入而未进入覆盖率报告的文件。依赖执行环境才能确认的内容进入 Task 0。

### 2. 提问（Ask）

当仍存在 Human 边界时，只询问最小有效集合；优先在一轮内给出不超过五个决策，并附选项和推荐。不要询问事实、任务拆分、架构 How、命令顺序或普通执行选择。

委托默认值必须标记为未确认，并说明依据、错误代价以及检测或回滚路径。它只能解决可逆的执行选择；不得改变 Goal、已确认边界、验收要求或 Human 决策权。静默默认值看起来像 Human 已批准；显式默认值才能保留 Human 决策权。

### 3. 编写任务书

使用 [execution-compile.md](references/execution-compile.md)，并保持其固定合同顺序。严格保持各章节语义，细节与任务规模成比例；在执行前公开委托决策，使 Human 能在 Handoff 前检查编译器拥有的默认值。

保持一个 Goal 和一本紧凑任务书，并在一次执行工作中关闭声明的交付。如果做不到，返回 Intent Take 缩小由 Human 拥有的交付，而不是编译多本任务书或无边界 Graph。

Stable Intent、已确认边界与受保护的证明要求仍然具有约束力。Executor 可以随着证据变化调整 implementation How 与剩余工作。

Handoff 前，仅在可见证明可能误判 PASS、容易被操纵或无法关闭 Goal 时，依据 [completion-trust.md](references/completion-trust.md) 预留私有验收。否则依赖受保护的可见判定器。将预留检查保留在 Executor 可见任务书之外；runtime 允许时，也应保留在 Executor 上下文之外。私有检查可以采用不同样本或观察路径，但绝不能加入隐藏要求。

### 4. 交付（Handoff）

当用户要求提示词、brief、合同或任务书时，返回任务书。直接要求完成工作即授予 compile-and-run 权限：达到 `Status: Executable` 后，现有 runtime 继续执行，无需额外启动轮次。Northstar 不监督实时执行。

### 5. 验收（Acceptance）

结果返回后，重新运行可见验收以及任何已预留检查。当最终判断需要独立性时绑定独立 Acceptor，例如证明仍然容易被操纵或不完整，包括本应私有的检查已对 Executor 可见，并且没有其他受保护判定器可以关闭 Goal。只有未实质参与实现，并且依据权威任务书和验收环境而非 Executor 结论进行判断的 Acceptor，才具备独立性。Executor 证据只是输入，不是最终判断。

如果所需 Acceptor 或验收环境不可用，停止在 `ready for independent acceptance`，并向未参与实现的 Acceptor 返回一份自包含验收交接：权威任务书、Executor 结果与证据、可见验收、任何已预留验收检查及其可见性、受保护判定器与基线，以及所需最终报告——`PASS` 或准确残留项。

局部 Task PASS 不等于完整 Goal PASS。保护判定器与基线；当检查可能静默失效时使用反向验证。凡涉及私有或独立验收，或检查可能误判 PASS，均应阅读 [completion-trust.md](references/completion-trust.md)。

## 输出

只输出一个状态，并提供足够信息，使声明的路由能够正确继续：

- **`Status: Unresolved Intent`** —— 当前理解、尚未解决的 Goal 分叉或重要后果，以及最小剩余 Human 决策或证据探针；
- **`Status: Blocked`** —— 准确的非意图阻塞，以及解除阻塞并安全继续所需的条件；
- **`Status: Executable`** —— 一本有现实依据的自主任务书；当用户要求完成工作时，编译后按 Handoff 继续执行。

`ready for independent acceptance` 是 Executable 路由之后的验收上限，不是第四种编译状态。

Northstar 不增加 scheduler、manager daemon、workflow owner 或其他控制层。
