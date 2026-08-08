# 执行图：静态编排与运行时演化

不要为了画 Graph 先拆 Task。只有当前 Task 粒度会掩盖**会改变执行判断的关系**时才使用 Graph：真实 dependency、并行、shared write、有意义的 Task Group boundary 或 join。

Graph 只承载**当前 Evidence 已经支持的执行关系**。它不是 semantic SOT、未来工作清单、scheduler 或 workflow model。

## 静态编排

只编译**当前证据支持的最小 Graph**：

- `depends on`：只有下游确实消费上游结果，或上游是安全执行前提时才写；
- `may run in parallel`：没有 dependency 和 write conflict 时才写；
- Task Group / join：只有组合 Verification 与局部检查实质不同才写；
- re-verification：只有后续工作可能让已有 Evidence 失效时才写。

省略传递依赖和单纯先后顺序，不为了让 Graph 看起来完整制造 node。

更重要的是：**不要提前物化那些存在与否仍取决于未来 Evidence 的 downstream Task。** 如果 A 的结果决定是否需要 B/C/D，就只编译 A 和已知 decision boundary；等运行时 Evidence 到来后，只把真正成立的后续工作物化出来。

## 运行时演化

Executor 面对当前 ready frontier。新 Evidence 只调整剩余 Graph：

- 新的真实 prerequisite、consumer 或 affected surface 被证明存在 → 在受影响下游前增加必要工作；
- 原 dependency 或 branch 被证明不存在 → 删除，让 ready work 继续；
- implementation reality 改变 → 拆分、合并或重排剩余 Task；
- 一个分支 Blocked，但其他分支独立 → 继续 ready work；
- join 只等待真实 required upstream result；
- actual change surface、binding/config 或组合行为变化 → 重算受影响 Verification。

已完成工作不因 Graph 改写机械重开；只有它的 Evidence 前提或所证明行为被影响时才重新取证。

Task Group 仍然只是普通 Task 之上的 Verification boundary。不要增加 Graph object/schema、persistent Graph state、scheduler、固定 Agent topology 或第二本 taskbook。repo/runtime 已有正常 progress record 就复用；没有就直接在当前执行上下文维护 frontier。

稳定规则只有一句：

> **当前 Evidence 让什么真正可执行，就物化什么；新的 Evidence 让更多工作成为现实后，再扩展 Graph。**