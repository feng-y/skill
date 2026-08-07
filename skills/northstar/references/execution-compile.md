# 自主任务书：把稳定 Goal 写成执行合同

只在 Goal 已定准后使用。最终产物是一本紧凑、权威的任务书，Executor 拿到后无需 Human 日常指挥，也能独立推进。

任务书保持固定结构和职责边界。Context 只写会影响后续判断、执行动作或验证证据的信息；大段支撑材料保留引用入口；全局事实只写一次，Task 内只补局部差异。不要把 Goal、Execution/Graph、Verification 和 Evidence 再编译成 completion/acceptance schema。

## Verification granularity

开发工作保留三种验证粒度，不增加新的 workflow stage：

- **Task 级验证**：证明一个局部行为所需的成本最低且足够的验证；代码修改优先到达 repo verification system 中直接覆盖受影响行为的最近有效边界，通常是受影响单元测试、定向测试或更权威的 direct probe；
- **Task Group 级验证**：一组 Task 共同形成组合行为、共享合同、迁移切片或汇合结果，而局部验证不足以覆盖时，在最小有意义边界运行覆盖该组合行为的更大范围验证；
- **Goal 级验证**：相关工作收敛后，确认本次明确交付所需的 repo verification 已被足够 evidence 覆盖。它是最终验证边界，不要求机械新增一条“最终命令”；仍有效的 Task/Task Group evidence 可以复用，只补 repo authority 仍要求但尚未覆盖的检查。

低层 PASS 可以解锁后续工作，但不能代替更高层实际需要验证的行为。验证成本决定执行节奏，不决定是否需要验证；昂贵检查只在它会改变调度时记录成本，不编造耗时。

## Repo verification authority

Handoff 前读取与预期 change surface 相关的 repo verification authority。由 Goal、真实 impact/reachability、主要 failure risk 和 Human 明确验证要求（若有）决定哪些行为必须验证；Human 明确验证要求是 Verification 的 binding input，不属于 Goal 本体，也不能由 Northstar/Executor 自行降级。不增加 `verification focus` 等中间模型。

从 changed owner、共享责任面或系统合同追到 effective binding/config 与 affected target/capability；存在 production binding authority 时，以 effective production config 和真实 consumer 为准。已知事实触发 mandatory verification 时，把它写成不可削弱的验证要求；“只是删除/重构”或预期 `0-diff` 都不能降级。仅执行期可知的 trigger 交给 Task 0，并预先写明触发后必须运行什么验证。

具体 test/build/replay/static/symbol probe 等 provider 从 repo verification system 中选择，只能证明其实际覆盖的行为；不要默认编译固定套餐，也不要为了凑覆盖枚举检查。只有入口本身是受保护判卷标准、权威基线，或点名能显著消除歧义时，才在任务书里固定具体 provider。

调研、选型和决策类工作也使用同一结构，只是 Execution 中写会产出证据的调查或决策，而不是实现 Task。每个结论都必须有来源和日期或可复现 probe；伪造引用、没有实际运行的“测量”和凑数结论都算失败。对有明确边界的学习 Goal，一条证据充分的死路也可能是有效结果。

## 合同头（Contract Header）

开头简要说清六件事：

- 本任务书是本次执行的权威合同；
- 唯一、内部一致且由 Human 决定的 Goal，包括成功时必须观察到和必须保持的结果；
- 这活为什么干，以及成功时世界有什么不同；
- Human 明确验证要求（若有）以及 Goal 级需要覆盖的 verification；
- 要求冲突时按什么顺序取舍；
- 哪些是违反即不合格的硬规则，哪些只是可以结合现场调整的建议。

Goal 本身定义成功，不再另建 `Completion Contract`、`completion properties` 或其他完成 taxonomy。Verification requirement 独立约束怎么证明 Goal，不重新定义 Goal。只有确实存在执行停止预算时才写；普通工作不要凭空加时间盒或尝试次数。

## 1. 替 Human 作出的决定

Northstar 在 Human 尚未明确选择时替 Human 作出的可回退决定，全部放在这里，并且必须早于边界和执行。

每项按这个顺序写：要决定什么 → 尚未由 Human 确认的临时默认 → 依据 → 猜错的代价 → 如何发现或回滚。

没有就写 `None`，不要为了填满章节虚构决定。

## 2. 地界与授权（Boundaries and Authority）

先写清预期写入地界，再写明确禁区。证据证明要达到 Goal 并取得足够验证就必须扩大实现范围时，Executor 可以在已确认边界和授权内调整范围，并在执行证据中写清原因和影响；不能悄悄改变 Goal 或 Human authority。

依赖新增或升级、权限变更、外部系统写入、破坏性操作及其他不可逆副作用要明确约束。列出不能被削弱的 repo 判卷标准：测试、schema、验收脚本、CI、基线及其他验收依据。点名看起来顺手、实际不属于本次 Goal 的顺手活和不可逆操作。

写清 Executor 在 Goal、已确认边界、授权和不可削弱验证要求内可以自行决定或调整什么。超出授权的操作记为阻塞；Goal 或已确认边界重新不稳定时回到 Intent Take。只有没有任何安全工作可继续时，才返回 `Status: Blocked`。

## 3. 当前现实与 Task 0（Current Reality and Task 0）

记录已经有证据支持的事实和基线；没有验证的声明明确标出来。仓库或 runtime 已有正常实现记录就直接复用；Northstar 不要求新建固定文件名或专用进度产物。

需要 Task 0 时，它在实质修改前执行，绑定真实 repo、worktree 和 target，实测关键命令和判卷标准是否有效，识别空跑检查和假绿灯，并暴露任务书假设与执行现实之间的重要差异。证据可以修正事实、可行性、实现范围、剩余 Task 和验证需要，但不能重新定义 Goal。

Task 0 如果承担 verification trigger 推导，解析当前可知的 changed owner / shared contract → effective binding/config → affected target/capability；触发就把既定 mandatory verification 纳入执行，未触发要保留其不适用的事实依据。执行过程中实际 change surface 或 binding 变化时，必须重新按 repo authority 计算受影响验证范围。

现实与任务书假设不一致时：

- 只是明确误读且纠正不改变 Goal/边界 → 纠正后继续；
- Goal 和边界仍成立 → 调整剩余 Execution/Graph；
- 还有安全工作 → 暂停受影响分支；
- 没有安全工作 → `Status: Blocked`，写清解除条件；
- 继续推进必须改变 Goal、边界或授权 → 回到 Intent Take/Human。

## 4. 执行（Execution / Graph）

按真实依赖排列 Task。每个 Task 至少写清：完成后能观察到什么、成本最低且足够的局部验证是什么、局部 PASS/FAIL 如何判定。

代码修改的局部验证必须到达 repo verification system 中能直接覆盖受影响行为的最近有效边界；通常使用受影响单元测试或定向测试，其他 direct probe 更真实或权威时就用它。TDD 的红→绿是定义行为或锁住回归最直接、低成本的方法时使用，不机械强制。正常局部边界不可用时，说明原因并使用最接近的 direct probe。

**Task Group** 是一组共同形成组合行为、共享合同、迁移切片或依赖图汇合结果的 Task。它只是 Verification 的组合粒度边界，不是新 workflow、持久对象或 Agent 拓扑。当 Task 级验证不足以覆盖组合行为时，写清组合结果、覆盖它的更大范围验证，以及验证运行的位置。

更大范围验证放在能证明组合行为的最小 Task Group 边界：一组连贯 Task 之后、下游消费结果之前，或并行分支重新汇合时。不要给每个 Task 重跑昂贵的全系统验证。已有实测或可靠成本时，用检查成本和延迟失败的恢复成本决定运行时机；成本只能减少无意义重复，不能削弱必要验证。

简单任务保持线性。真实分支、依赖、共享写入、Task Group 或汇合点会被线性列表掩盖时，读取 [execution-graph.md](execution-graph.md)，只把最小真实依赖写进普通 Task。

## 5. 执行规则（Execution Rules）

- 执行中遇到新的 Unknown，先判断它影响 Goal、边界、事实、实现方式、Verification 还是 Evidence，再按 [SKILL.md](../SKILL.md) 处理；
- Task 是当前执行计划，不是冻结范围。证据变化时，可以在 Goal、边界、授权和不可削弱验证要求内增加、删除、拆分、合并或重排剩余 Task；
- 保持验证粒度：Task PASS 可以解锁依赖工作，Task Group PASS 可以解锁消费组合结果的下游工作，但二者都不能替代本次 Goal 实际要求的最终验证；
- 已触发的 mandatory verification 不可降级；只能在 repo authority 允许时更换等价或更权威的 provider、调整运行位置；
- 验证调度同时考虑证明范围、检查成本和延迟失败恢复成本；缺失验证不能写成 PASS；
- 重要决策、会改变证据的偏离、重新规划、范围扩大、验证节奏变化和 blocker，优先保存在 repo/runtime 正常实现记录中；
- 恢复执行时，只复用前提仍然成立的决定和 evidence；后续变化没有影响其覆盖行为时不要重复工作；
- 不得跳过测试、削弱断言、缩小验收覆盖、用 mock 绕开真实对象、吞掉失败、偷改判卷标准或接受更低基线，除非 Goal 明确要求且仍有等价可信的 repo evidence；
- 关键检查可能静默失效时需要反向验证；visible judge 可被针对性优化时按 [verification-trust.md](verification-trust.md) 增加受保护、私有或独立 evidence；
- 每次重试都必须改变假设或方法；已知错误路线立即停。同一路线对同一验证条件失败三次，必须重新规划、换分支、回滚、`BLOCK` 或 `ESCALATE`；
- 未授权回归必须回滚并如实报告；
- 遵守仓库已有的分支、PR 和提交前规则。

## 6. 验证与证据（Verification and Evidence）

相关 Task 和 Task Group 收敛后，在 Goal 级确认本次交付的 repo verification coverage：复用仍有效的 Task/Task Group evidence，只运行 repo authority 仍要求且尚未被覆盖的检查。Goal 级验证是最终判断边界，不是固定的一条额外命令。

最终验证范围必须根据**实际** change surface、effective binding/config 和真实 consumer/target 确认；不要沿用已经被执行变化推翻的早期 snapshot，也不要因为预期 `0-diff`、cleanup 或 refactor 就缩小已触发的验证。

Evidence 只有在下列条件仍成立时可以支持判断：

- verification 实际运行，而不是计划或口头声明；
- provider 确实覆盖当前 claim；
- 产生 evidence 时的版本、环境、对象、binding/config 和关键前提仍然成立；
- 后续变化没有影响 evidence 原本证明的行为；
- judge、断言、coverage、baseline 和失败传播没有被削弱；
- 重要输出真实存在或可以复现。

若关键 judge 可能假绿、visible verification 可被钻空子，或需要额外独立性，按 [verification-trust.md](verification-trust.md) 使用反向、私有或独立 evidence。它们只提高 Evidence 的可信度，不形成独立 Acceptance 阶段或固定 Acceptor 角色。

最终报告必须给出 `PASS` 或准确的非 PASS 路径，并说明：干成了什么、哪些 Task/Task Group/Goal 级 verification 及其 evidence 支持判断、还有哪些真实 residual/blocker、下一条合规推进路径是什么。Executor 的 `done`、`PASS` 和 activity narration 都不能代替 evidence。

Handoff 前再检查：只有一个 Goal 和明确交付；至少一个 Task 或必需 Task 0 能立即开始；真实依赖有依据；共享写入有唯一归属；相关 repo verification authority 已读取；已知 mandatory verification 已编译，执行期 trigger 已进入 Task 0；Task / Task Group / Goal 三种验证粒度放置合理；昂贵验证没有机械下沉到每个 Task；授权边界清楚；Goal 级所需验证可由现有/计划 evidence 完整覆盖。不要编译 scheduler、lease、固定 Agent topology、Completion Contract 或 Acceptance workflow。

一本任务书必须在一次执行工作中形成本次明确交付。runtime 支持时，Executor 可以委托、并行或使用依赖 Graph，但必须保持一个 Goal、清楚写入所有权、正确放置验证粒度，并最终取得足以支持 Goal 的 Evidence。做不到时回到 Intent Take 缩小 Human 本次要的交付；不要把一个 Goal 拆成多本任务书。