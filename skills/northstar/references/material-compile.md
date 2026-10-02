# Material execution / compile

本 reference 适用于 Northstar 已承接完整 Intent 的工作；受委托的局部 Intent 问题按 SKILL.md 返回实际 caller，不因此启动 Taskbook execution / learning flow。

按当前边界读取，不把下列内容当作固定阶段：

- return 关联不清或 binding premise 实质变化 → [返回关联与当前前提](#返回关联与当前前提)；
- 跨 session / agent / execution-environment 恢复 → [Session handoff 只记录 delta](#session-handoff-只记录-delta)；
- 当前 Intent / canonical Taskbook 已成立，但复杂 work / dependency 仍迫使 fresh consumer 重做高层判断 → 下列 compile 内容。简单线性 task 不展开 Graph。

Compile 的目标不是建立完整 work graph，而是把已成立 Intent 编译成 canonical Taskbook 中**最小充分的 task / dependency contract**：让后续执行者知道必须兑现哪些 cohesive outcomes、哪些真实 dependency 不能打乱，以及哪些 Acceptance / Constraint 必须保持。简单线性 work 只需要 compact task，不为了 planning ceremony 构建 Graph；session handoff 是另一件事，只记录 resume delta。

Compile 不重新定义 Intent，不产生或扩大 Human execution authorization，不设计 implementation How，不拥有 verification judgment。它展开的是兑现完整方案所需的 task / dependency 结构；Northstar 消费 material return 后维护 status / judgment / next owner，不以重编结构为前提。低层 execution progress / scheduler state 仍属于执行系统。

## 从 Intended delta 出发

先从 canonical Intent 恢复已经成立的 `Current → Intended` material delta。只保留为了让 Draft / Constraint / Acceptance 成立而真正需要兑现的差异，例如 responsibility / authority 归位、核心路径改变、binding boundary 建立、明确要求退出的 legacy path，以及必须保持的 invariant。

不要从文件结构、当前 module、候选 patch 或已有 task list 反推 Intended state；不要把仍会改变 Intent 的 unresolved alternative 编译成 implementation branch。

## 最小 task / dependency handoff

只 materialize fresh implementer 若不知道就会重新做高层判断的 work：

- 一个 task 对应一个 cohesive material outcome / responsibility / binding boundary，不按文件、helper、agent session 或 verifier 拆分；
- 只有 prerequisite、共享 authoritative surface / conflict、或必须共同成立的 outcome 才记录 dependency；
- 文本顺序不形成 dependency，能够独立推进的 work 保持独立；
- 省略某个 task / relation 会迫使 fresh implementer重新恢复 material Intent 时才保留；
- 仍取决于未来 execution Evidence 的 contingent work 不提前创建 placeholder task；
- verification claim 不因为可独立验证就自动成为 execution task。

简单或线性的 material work 不需要 Graph，只在 canonical Taskbook 中保留一个或少量 cohesive task。多个 task 也不自动等于多个 Issue；Taskbook 按一个 engineering Intent 持久化，Issue / external orchestration 只有真实协作边界时才按最小必要范围 materialize。不要为了“完整规划”把探索过程展开成 issue graph。

## Verify boundary

Compile 只携带 Northstar 已定义的 Acceptance / completion claim identity 与 material dependency，不选择具体 test / Replay / runtime command，也不把 verification step 编成 execution phase。

需要 proof obligation、backend selection、Evidence sufficiency 或 verdict 时交 `$verify`。一个 task 完成不代表整体 Acceptance 自动成立；一个 verification claim 也不自动成为 task。

## Evidence feedback

Research、execution、review 或 `$verify` 的 verified Evidence 只有在它使**现有 task / dependency 不再成立**时才重编这部分任务结构；普通 completion / blocker / acceptance 仍按 SKILL.md 的返回边界更新同一 Taskbook 的状态与 judgment：

- 新 reality 证明某个已记录 task 不需要或边界错误 → 删除 / 合并 / 修正对应 task；
- prerequisite 或 conflict 改变 → 只修订受影响 dependency；
- 只影响 implementation How → task / dependency 结构不变，不阻止 material return 后的状态与 judgment 更新；
- Evidence 推翻 Intent / Acceptance → Northstar 重开受影响的完整方案判断；修订成立后只调整因此变化的 task / dependency，保留无关方案、任务与有效 Evidence；
- Evidence 暴露新的长期 architecture fork → 返回 `$architecture-evolution`。

不要维护“持续演进的完整 Graph”，也不要因为局部 Evidence 变化重算无关 work。

## 交付与停止

默认把必要 task / dependency relation fold 回 canonical Taskbook；Taskbook 与 current Draft 是同一 Northstar work 的 durable surface，不再额外生成一份 session handoff 作为方案副本。需要跨 session 时另写短 handoff，只指向 Taskbook 并记录 resume delta。

当 fresh implementer / worker 已能在 binding boundary 内继续、剩余未知只影响 implementation How 时停止 compile。已有 Human execution authorization 时由 Northstar 选择并 handoff next material task / owner；真正启动执行由宿主 / worker / orchestration 负责。没有授权时 Taskbook 停在 execution-ready。worker 返回 material result / Evidence 后回到 Northstar judgment，再决定是否推进 task state；implementation-local substeps 不逐项回流 Northstar。

## 返回关联与当前前提

return 关联不清时，从已有 Taskbook / dispatch / artifact / 运行记录恢复对应 task、执行时的 binding context 与实际 result / Evidence。先查可得事实，只保留仍影响判断的 blocker；不要求新增字段、receipt 或让 Human 猜技术事实。关联成立只说明这是哪次工作的结果，不证明当前 Intent / Acceptance 已满足。

dispatch 后若 binding Decision / Constraint / Acceptance 已实质变化，按当前 canonical Taskbook 只重判受影响的 claim：旧结果不能沿旧解释关闭当前 task，仍有效 work / Evidence 保留。若只是版本、文字或无关 task 状态变化，不重做成立的工作。把实际差异与 judgment 回写同一方案文件，再按 SKILL.md 的已授权续接 / 停止边界处理。

## Session handoff 只记录 delta

跨 session 时，先确保 canonical 方案文件已经落盘；material execution 时它同时就是 Taskbook。跨环境只提供 pointer 不等于恢复成功：接收方须实际读到该 canonical 文件，才能继续依赖它的工作。若路径不可达或文件缺失，保留恢复 blocker，通过已有可用方式解决访问，不复制方案来冒充恢复；真实启动事件可如实报告为已启动但恢复受阻。生成的**短 handoff**只保留恢复所需 delta。handoff 只回答“从哪里恢复”：canonical plan/Taskbook pointer、baseline / working context 中 fresh session 必须知道的最小状态、last completed / current task、仍 live 的 decision / blocker、next task / owner，以及哪个结果需要返回 Northstar 判卷。

handoff **不得重新复制** Taskbook 中已经存在的 architecture、方案、完整 path mapping、改动面、Acceptance 或 out-of-scope。若这些内容在 handoff 中需要长篇重述，说明 durable 信息没有正确 fold back，应先更新 Taskbook。handoff 是 session delta，不是第二份缩略 Taskbook。

下一 session 的启动 prompt 也只应指向 repo rules + canonical 方案文件/Taskbook + handoff，并要求恢复 Northstar context 后继续 next task；不要把完整方案再次嵌入 prompt。fresh session 先读落盘的 canonical 方案文件，再消费 handoff delta。
