# Consume an Architecture Design Handoff

只在输入包含 `Architecture Design Contract` 且 `Handoff: Ready` 时读取。

## Preconditions

必须同时满足：

- `Status: Design ready`；
- `Brooks verdict: PASS`；
- 用户已明确要求进入实现；
- handoff 包含 `Design source`、`Goal seed`、`Target`、`Architecture decisions`、`Design delta`、`Implementation boundary`、`Protected behavior`、`Verification obligations` 和 `Design invalidation triggers`。

缺失时，不把它当作可执行架构合同；按 Northstar 的 Intent Take 补齐真正缺失的授权、事实或 Human 决定。

## Authority

Architecture Evolution 已拥有并完成：

- 同一业务/不同业务判断；
- canonical capability；
- stable abstraction 与 variation points；
- cohesive module ownership；
- dependency direction；
- 必须退出的旧结构。

Northstar 不重新裁决这些架构决定，也不把它们降级成可选建议。Northstar 只拥有：

- 把 Goal seed 编译成一本可执行任务书；
- 安排实现切片、迁移顺序和验证节奏；
- 在稳定设计合同内根据代码证据调整实现方式；
- 完成执行与完整 Goal 验收。

## Compile mapping

把 handoff 映射到现有六节任务书，不新增章节或 workflow：

- `Goal seed` 与 `Target` → Contract Header；
- `Architecture decisions`、`Do not change`、`Protected behavior` → Boundaries and Authority；
- `Design source`、repo snapshot、`Design invalidation triggers` → Current Reality and Task 0；
- `Keep / Move / Merge / Delete` 与 `Implementation boundary` → Execution；
- `Verification obligations` → Task、Task Group 和完整 Goal 证明；
- Brooks residual Warning → Acceptance 中的残留风险、owner 与验证边界。

`Delete` 必须形成真实退出 Task 和验收证据，不能只实现新路径后保留永久双轨。

## Task 0

实质修改前，只验证 handoff 仍适用于当前现实：

- `Design source` 对应的 repo snapshot、关键路径和依赖是否仍成立；
- protected tests、schema、replay、CI 或其他判卷标准是否真实有效；
- implementation boundary 是否仍足以完成 replacement；
- 是否出现任一 `Design invalidation trigger`。

Task 0 不重新执行 Architecture Evolution，也不重新寻找更优架构。

## Routing on new evidence

- 只影响实现细节、任务拆分或验证调度 → Northstar 在合同内重新规划并继续；
- 证明 handoff 被明确误读，但不改变架构决定 → 纠正引用后继续；
- 推翻同一业务判断、essential difference、canonical contract、module ownership、dependency direction 或 Protected behavior → 停止受影响实现，返回 Architecture Evolution；
- 需要改变 Goal、验收要求或已确认边界 → 回到 Northstar Intent Take 交给 Human；
- 没有安全工作可继续 → `Status: Blocked`。

禁止 Northstar 在任务书中悄悄修订目标架构来绕过 invalidation。

## Direct execution

用户已经要求“实现”“开始实现”或等价行动时，`Handoff: Ready` 即提供架构输入，Northstar 达到 `Status: Executable` 后直接 compile-and-run，不再额外请求一次开始确认。
