# 自主任务书：把稳定 Goal 编译成最小充分执行合同

只在 Goal 已定准后使用。Taskbook 要让 fresh Executor 独立完成目标，但**不替 Executor 预写实现方案**。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 compiler 内部 ownership / proof chain，不是输出模板。**完整的是 decision coverage，不是 information coverage 或 patch coverage。** Research 可以很深，Taskbook 必须压缩。

## Goal

只写一个 Human-owned Goal：目标结果、confirmed boundary、must-preserve、最终交付。Why 只有会改变取舍时才写。Human 明确 Verification requirement 归 Verification，不复制回 Goal。

## Execution / Graph

Taskbook 默认只保留少量 **bounded work unit**。

一个 Task 应该让 Executor 能在一组统一 judgment 下独立推进到可观察结果，通常只需要：

- 要达到的局部 outcome；
- 适用 territory / starting reality 仅在不写会误判时给出；
- 一个会反复决定“做 / 保留 / 停 / 分支”的 stable judgment；
- 真正限制选择空间的 hard constraint；
- 已经 binding、且决定该 work 是否成立的 Verification obligation。

**Task 不是 executable delta，也不是 predicted patch。** 不因为 Research 已经知道某个可行方案，就把以下细节自动写成执行合同：具体文件怎么拆、符号搬到哪个新文件、函数抽哪几行、include/BUILD 怎么改、命令先后、每个 leaf 的删除顺序、用于定位失败的中间 build/test。只有 Human 明确要求、repo authority 要求、真实 dependency/风险要求，或 Evidence 证明这是唯一安全路线时，才把这类 How 固化。

当一批文件/符号/实例共享同一个 judgment 时，合并成一个 Task；不要为每个实例建立节点。只有 outcome、dependency、authority、risk 或 required Verification 真不同才拆。

Graph 只表达会改变 execution judgment 的真实关系，例如 dependency、可并行 work unit、shared write 或必须组合验证的 join。不要为了 Graph 精确把工作切碎。

Human 已确认的 strategy / scope boundary / must-preserve 直接保留。ready frontier 只表示现在能做什么，不改变 Human Goal；adjacent residual 不自动扩 scope。

当前 workspace 中仍与 Goal 一致的修改作为 starting reality 复用；“已经改了”不是 correctness Evidence，不要求重做，也不据此缩 Goal。

**Task 0** 只在缺少某个执行期事实会阻止第一项安全 material work，或 required Verification 明确要求在 material work 前关闭 trigger 时使用。它不是 Research continuation、inventory 或默认 checklist。

## Information compression

Research finding 不自动进入 Taskbook。只有它至少改变以下一项才值得保留：

- Goal / boundary / must-preserve；
- Executor 反复应用的 judgment；
- work unit 的真实 dependency / risk / authority；
- required Verification / Completion judgment；
- 无法安全从 repo 重新取得、且丢失会导致执行偏离的 starting reality。

Executor 打开 repo 就能安全重新取得的文件行号、symbol count、include 明细、候选清单、已知 patch 方案，默认省略。**更多 Evidence 应该压缩成更少、更可靠的判断，而不是更多 instruction。**

## Verification

Verification 冻结**必须证明什么**，不默认冻结**为了实现/调试应该怎么跑**。

- Task：只有 local check 已经 binding 且决定是否能继续时才写；
- Task Group / join：组合行为必须单独证明时才写；
- Goal：保留 repo authority 或 Human 明确要求的 delivery coverage。

Provider、target、scope 依赖 change surface / binding / runtime reality 时，编译稳定 trigger/authority，让 Executor 在触发后 materialize 具体 action。cleanup/refactor/expected `0-diff` 不能降低已经触发的 required Verification。

“每改一个文件都 build”“每搬一个类型都单独 test”这类失败定位策略默认属于 Executor tactic，不进入 binding contract，除非 repo/Human authority 或特殊风险明确要求。

需要额外 judge trust 时按需读取 [verification-trust.md](verification-trust.md)。

## Evidence

Compile proof / trust requirement，不编译未来结果。最终 judgment 需要的 Evidence 应可复核并覆盖真实 claim；Executor 自报 `PASS` 或活动说明不是 Evidence。前提未变化的 Evidence 可复用，新 Evidence 只让受影响结论失效。

## Completion Hook

Taskbook 自带 stop judgment，但不新增 Completion layer。只读取 **Goal / constraints + triggered required Verification + current valid Evidence**：

- Goal material outcome 是否已被最低充分 Evidence 覆盖；
- must-preserve / confirmed boundaries / authority 是否仍成立；
- triggered required Verification 是否都有可信 Evidence。

全部满足就 `STOP`；有 gap 就继续现有 work 或只 materialize 能关闭 gap 的 contingent work；没有安全路径就准确 `BLOCKED`。frontier 为空或 Task 做完本身都不等于完成。

## Handoff check

发出前只问：

- Taskbook 是否定义了任务，而不是展示 Northstar 的调研过程？
- 每个 Task 是否是 bounded work unit，而不是文件/函数/patch step？
- 是否把“一个可行实现”误写成了“必须这样实现”？
- 同一个 judgment 能覆盖的实例是否已经合并？
- Graph 是否只保留真实 execution relationship？
- Verification 是否只冻结 required proof，而没有把 debugging tactic 变成硬流程？
- Executor 可安全自行取得、且不改变 judgment 的细节是否已经删除？

如果删除某段不会改变 Executor 的目标、边界、判断或完成条件，就删除它。