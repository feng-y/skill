# 执行图：静态编排与运行时演化

只有线性 Task 列表会掩盖真实依赖、并行关系或有意义的 Task Group 验证边界时，才使用执行图。Graph 只表达**当前有证据支持的执行关系**，不定义 Goal、Verification 或 Evidence。

## 静态编排

Handoff 时的 Graph 是基于当前 Reality 编译出的 best-known snapshot，不是冻结的执行脚本：

- `depends on`：只有下游确实要消费上游结果，或上游是安全执行前提时才写；
- `may run in parallel`：没有依赖，也没有写入冲突时才写；
- `verify group at boundary`：一组 Task 共同形成组合行为或共享合同，而局部证明不足时写；把更大范围检查放在下游消费之前或分支汇合处；
- `reverify at join`：并行可以继续，但后续修改可能让已有 evidence 失效时写。

省略传递依赖，不把单纯先后顺序伪装成依赖边。简单工作保持线性；不要为了“有 Graph”制造节点、分支或 Task Group。

## 运行时 Graph

Executor 面对的是当前可执行 frontier，而不是必须照抄静态 Task 顺序。新 Evidence 改变执行事实时，只调整**剩余 Graph**：

- 发现新的真实前提或 consumer → 在受影响下游前补 Task / dependency；
- 证明原依赖不存在 → 删除对应 edge，让原本被错误阻塞的工作继续；
- implementation reality 改变 → 可以拆分、合并或重排剩余 Task；
- 一个分支 Blocked，但其他分支不依赖它 → 继续 ready work；join 只等待真实依赖；
- actual change surface、effective binding/config 或共享合同变化 → 同步重算受影响 Verification scope 和 join evidence；
- 已完成工作不因 Graph 变化机械重做；只有它的 Evidence 前提被影响，或新的组合边界需要更高粒度验证时才重新取证。

静态 Graph 是启动时的编排，运行时 Graph 是 Evidence 驱动的当前执行状态。变化的是执行关系，不是 Goal、Human authority 或已经触发且仍适用的 Verification requirement。

Task Group 只是普通 Task 之上的组合验证边界；不要增加独立 Graph 对象、schema、持久状态、scheduler 或固定 Agent 拓扑。repo/runtime 已有进度记录时可记录剩余 Task 与依赖变化，没有就直接在当前执行上下文维护；不要为了 Graph 新造控制面。写入所有权和 evidence requirement 仍放在普通 Task 合同里。每个分支最终要汇合或走向明确终止路径，不要拆成多本任务书。
