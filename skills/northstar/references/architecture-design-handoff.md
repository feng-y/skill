# Consume an Architecture Design Handoff

只在输入包含 `Architecture Design Contract` 且 `Handoff: Ready` 时读取。

## Preconditions

必须同时满足：

- Source 指向的合同为 `Status: Design ready`；
- Source 合同的 `Brooks verdict: PASS`；
- 用户已明确要求进入实现；
- handoff 的 `Source / Scope / Delta / Proof` 完整。

缺失时，不把它当作可执行架构输入；只补真正缺失的授权、事实或 Human 决定。

## Authority

`Source.Design` 指向的 Architecture Design Contract 是架构决定的唯一事实源。Northstar 不复制或重新裁决其中的业务判断、目标抽象、variation、模块责任、依赖方向与旧结构退出决定。

Northstar 只拥有：编译任务书、安排实现切片和迁移顺序、在稳定合同内调整实现方式，以及执行和完整 Goal 验收。

## Compile mapping

直接映射到现有六节任务书，不新增章节或 workflow：

- `Source` → Current Reality and Task 0；
- `Scope` → Contract Header 与 Boundaries and Authority；
- `Delta` → Execution；
- `Proof` → Task、Task Group 与完整 Goal 验收。

`Delta.Delete` 必须形成真实退出 Task 和验收证据，不能只实现新路径后保留永久双轨。

## Task 0

实质修改前只验证：

- Source 的 snapshot、关键路径和设计前提仍成立；
- Scope 仍足以完成 replacement；
- Proof 中依赖的 tests、schema、replay、CI 或其他判卷标准真实有效；
- 是否命中 `Proof.Return when`。

Task 0 不重新执行 Architecture Evolution，也不寻找“更优架构”。

## Routing on new evidence

- 只影响实现细节、任务拆分或验证调度 → Northstar 在合同内重新规划；
- Source 被误读但设计本身未变 → 纠正引用后继续；
- 命中 `Proof.Return when` → 停止受影响实现并返回 Architecture Evolution；
- 需要改变 Goal、验收要求或 Human 已确认边界 → 回到 Northstar Intent Take；
- 没有安全工作可继续 → `Status: Blocked`。

禁止 Northstar 在任务书中修改 Source 所指向的目标架构来绕过返回条件。

## Direct execution

用户已经要求“实现”“开始实现”或等价行动时，Northstar 达到 `Status: Executable` 后直接 compile-and-run，不再额外请求一次开始确认。
