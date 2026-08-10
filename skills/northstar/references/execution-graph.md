# 执行图：静态编排与运行时演化

不要为了画 Graph 先拆 Task。只有当前 Task 粒度会掩盖**会改变执行判断的关系**时才使用 Graph：真实 dependency、并行、shared write、有意义的 Task Group boundary 或 join。

Graph 只承载**当前 Evidence 已经支持的执行关系**。它不是 semantic SOT、未来工作清单、scheduler 或 workflow model。

## 静态编排

编译当前 Evidence 支持的 **decision-complete Graph**：把当前已知、会改变 execution judgment、且边界足够稳定的必要 work / relation 一次表达清楚；不为了 lazy 故意隐藏，也不因为“完整”枚举 file/symbol/patch detail。仍实质依赖未来 Evidence 的 contingent work 不提前猜。

- `depends on`：只有下游确实消费上游结果，或上游是安全执行前提时才写；
- `may run in parallel`：没有 dependency 和 write conflict 时才写；
- Task Group / join：只有组合 Verification 与局部检查实质不同且关系已经成立时才写；
- re-verification：只有后续工作已知可能让已有 Evidence 失效时才写。

省略传递依赖和单纯先后顺序，不为了让 Graph 看起来完整制造 node；但当前 Evidence 已经能确定 `A → {B,C} → D` 时，就直接编译这个结构，不故意退化成只给 A。

只有 B/C/D **是否存在、影响范围或必要关系**仍取决于 A 的未来 Evidence 时，才只编译当前已知结构与 decision boundary；等运行时 Evidence 到来后，只把真正成立的后续工作加入同一本 Graph。

## 运行时演化

Executor 面对当前 ready frontier。新 Evidence 只调整剩余 Graph：

- 新的真实 prerequisite、consumer 或 affected surface 被证明存在 → 在受影响下游前增加必要 work；
- 原 dependency 或 branch 被证明不存在 → 删除，让 ready work 继续；
- implementation reality 改变 → 拆分、合并或重排剩余 Task；
- 一个分支 Blocked，但其他分支独立 → 继续 ready work；
- join 只等待真实 required upstream result；
- actual change surface、binding/config、provider validity 或组合行为使新的 Verification obligation/action 真实适用 → 把该 verification/probe 作为当前 execution action 放在最低有意义边界；
- 已编译 Verification 的 scope/placement 被新 Evidence 推翻 → 只修正受影响部分。

这里不创建 ImplementationNode / ProbeNode / VerificationNode 等 taxonomy：实现、probe、verification 都只是当前需要执行的 action，Graph 只表达它们之间真实存在的关系。**Evidence 是 action 的 reality output，Completion Hook 是 Taskbook 的 judgment；两者都不是 Graph node。**

已完成工作不因 Graph 改写机械重开；只有它的 Evidence 前提或所证明行为被影响时才重新取证。

Task Group 仍然只是普通 Task 之上的 Verification boundary。不要增加 Graph object/schema、persistent Graph state、scheduler、固定 Agent topology 或第二本 taskbook。Graph 不定义第二套 progress/state 协议：复用 Compile/Handoff 已选定的唯一 durable execution-state carrier，并让 frontier 变化只更新同一载体中的必要 progress / Unknown / blocker / resume state。

稳定规则只有一句：

> **当前 Evidence 已经使其成为必要且稳定的 execution relation 一次编译；真正 contingent 的 work / Verification 由 Evidence 使其成为现实时再扩展 Graph。**