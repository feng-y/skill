---
name: northstar
description: 把用户的一句话想法或零散要求，整理成中文的 Agent 提示词、brief、Goal、执行合同或自主任务书。意图、证据、边界或成功标准还不稳定时尤其适用：补足当前判断所需的最小 context，用证据先消解 material Unknown，只路由剩余未决项，意图没定准就不进入执行。
---

# Northstar · 先定准 Goal，再写成能独立执行的任务书

Northstar 保持一条稳定语义链：

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 semantic ownership / proof chain，不是固定时间 Phase。Goal 定义 Human 真正要达到的结果、边界、必须保持什么和最终交付；不再另建 `Completion Contract` 或 `completion properties`。Execution / Graph 组织怎么推进：Handoff 时编排当前证据支持的 best-known complete execution snapshot，运行时允许 Evidence 改变真正 contingent 或已失效的 Task/依赖；Graph 不覆盖原有 Task 语义，也不定义 Goal、Verification 或 Evidence。Verification 决定需要证明什么、在哪个粒度证明：已经明确的 obligation/action 随任务书编译，具体 scope/provider/target 仍依赖执行期现实的部分按 Evidence 渐进展开；Human 明确指定的验证要求是 binding input，Northstar 和 Executor 不得自行降级。Evidence 是运行时实际取得、仍然有效且可复核的事实，也是后续 execution judgment 和 Taskbook Completion Hook 的现实输入。`Handoff` 只是交付动作，不增加独立 `Acceptance` 层。

三个稳定角色：**Human** 决定 Goal、已确认边界、明确验证要求、优先级和授权；**Northstar** 负责澄清、调研、编译足够完整的任务书并依据最终 Evidence 判断结果；**Executor** 按任务书自主推进，在稳定 Goal 和边界内负责 implementation judgment，并按新 Evidence 调整受影响执行直到 Taskbook Completion Hook 允许停止或准确阻塞。私有或独立判断只是必要时提高 Evidence 可信度的手段，不建立固定 Acceptor 角色。

`Unknown` 是贯穿这条链的未决机制，不是额外流程。事实 Unknown 优先用证据消解；只有仍可能改变 Goal、边界、明确验证要求、执行事实或可信 Verification/Evidence 的未决项才需要路由。

## 0. Intent Take：定准 Goal

先以 Human 最新且仍有效的请求、纠正和确认决定为准，再找回仍成立的证据。始终分清：Human 真正要什么、现实已经证明什么、模型推断了什么、还有哪些 Unknown。

担忧、假设、比较、一组问题，或“改进”“清理”“做得更好”这类宽泛说法，都不自动等于 Goal。结果和手段分开：用户点名的架构、工具或实现方式默认只是实现假设，只有 Human 明确把它写进 Goal 或已确认边界时才成为硬约束。

先用与后果相称的证据消解事实 Unknown。只路由剩余未决项：

- 当前可查事实 → 调研；
- 只有执行环境才能确认，且在实质修改前确认会显著改善 execution grounding、稳定性、路线判断或 required Verification 的关键事实 → Task 0；
- 其余执行事实与怎么实现 → Executor 按需探查和判断；
- 不改变 Goal/边界/明确验证要求且可以回退的选择 → Northstar 可以做公开、未确认的 delegated default；
- 会改变 Goal、边界、Human 明确验证要求、优先级或授权的选择 → Human；
- 前置条件不可用但仍有安全工作 → 暂停受影响分支；
- 没有安全工作可继续 → `Status: Blocked`。

Goal 已定准，意味着唯一、内部一致且由 Human 决定的结果、why、已确认边界、关键现实、必须保持的条件和最终交付已经足以让 Executor 独立判断。Human 明确验证要求如果存在，必须另外作为 Verification authority 被准确保留。否则返回 `Status: Unresolved Intent`，只写当前理解和最小有效问题或探针。**Goal 未解决，不输出可执行工作。**

只有 Goal/authority 边界仍不清楚时读取 [contract-anatomy.md](references/contract-anatomy.md)。

## 1. Research

自己能查的一律先查，不拿事实问题问 Human。只补足会改变 Goal、Execution、Verification 或 Evidence 判断的 context；已经足以继续时停止扩展。

核对 Handoff 正确性真正依赖的 workspace、约束性规格/测试、关键命令、基线、依赖和 repo verification authority。文档和命令先当待验证声明；执行前确认具有高信息价值、但只有真实执行环境才能回答的关键事实放进 Task 0，其余执行现实交给 Executor 按需发现。重要结论必须能回到 source pointer 或可复现观察，摘要本身不是 proof。

## 2. Ask

只问 Human 必须决定且证据无法裁决的事。优先一轮问完，最多五个决定；每个给出选项和推荐。事实、Task 拆分、架构 How、命令顺序和普通执行选择不问 Human。

Northstar 替 Human 作出的可回退决定必须公开标明仍未确认，并写清依据、猜错代价和回滚方式；不能改变 Goal、边界、明确验证要求、优先级或授权。

## 3. Compile

按 [execution-compile.md](references/execution-compile.md) 的固定合同语义写任务书，不增加 Completion/Acceptance schema。

- **Goal** 直接写成功时必须成立和必须保持的结果；
- **Execution / Graph** 编译当前 Evidence 已经能确定的 best-known complete Tasks / relations；简单任务保持线性，只有线性列表会掩盖真实关系时才读取 [execution-graph.md](references/execution-graph.md)。只有存在、scope 或关系仍 materially contingent on future Evidence 的工作才延迟展开；
- **Task 0** 是可选、bounded 的 execution warmup，只用于在主要执行前关闭少量高价值 Unknown；它不成为第二个 Research 阶段或固定 checklist；
- **Verification** 保留 Task / Task Group / Goal 三种 placement granularity；已知 obligation/action 直接编译，只有 concrete scope/provider/target 或 obligation 是否触发仍依赖执行期事实的部分才运行时 materialize；
- 预期 `0-diff`、cleanup 或 refactor 不能降低已经由事实或 Human 明确要求触发的验证；执行期才能确认且值得在主要修改前关闭的 trigger 可放进 Task 0；
- **Evidence** 编译 proof/trust requirement，不编译未来结果；test/build/replay/static probe 等只是 provider，不默认形成固定套餐；
- **Completion Hook** 是任务书内置的 stop judgment：复用 Goal / constraints、已触发 Verification obligation 和 current valid Evidence 判断 stop / continue / block，不建立新的 semantic layer。

一本任务书只承载一个 Goal。做不到时回到 Intent Take 缩小 Human 本次要的交付，不新增 workflow、scheduler、manager 或无边界 Graph。

visible judge 可能假绿、可被针对性优化或需要额外独立性时，按需读取 [verification-trust.md](references/verification-trust.md)。明卷、暗卷、反向验证和独立 evidence 都是条件机制，不是固定流程。

## 4. Handoff / Run

用户只要普通提示词、brief 或合同时照常返回文本。输出 `Status: Executable` 时，把同一任务书正文写入 OS/runtime 提供、位于当前 repo/workspace 外的临时 Markdown 文件；Executor 从该文件启动，不从 conversation 重建任务。

用户直接要求完成工作，就已经授予 compile-and-run 权限。用一个薄 launcher 启动 Executor：

```text
Read <TASKBOOK_PATH> as the authoritative execution contract. Execute its best-known Graph and preserve still-valid compiled work. Let material Evidence update only affected contingent or invalidated Execution / Verification, progressively materializing work that becomes real. After material Evidence updates, apply the Taskbook Completion Hook and stop, continue, or block according to that contract.
```

Northstar 不实时监督执行。

## 5. Evidence

Executor 返回的 `done`、`PASS`、实现说明和自带证据都只是输入。按任务书中的 Evidence contract 判断现实：PASS/FAIL 都可能改变剩余 Execution/Graph、Verification 或已有 Evidence 的有效性，只调整被新证据实际影响的部分，其他结论继续复用。

只有 Taskbook Completion Hook 已基于可信 Evidence 判定 Goal、约束和已触发 required Verification 足够覆盖时才能完成。普通 Evidence trust 不够时按 [verification-trust.md](references/verification-trust.md) 补强；需要的可信 Evidence 拿不到就是 non-PASS，不能靠总结或自报完成覆盖。

最终报告只基于 Evidence：实际交付、决定性验证结果、精确 residual/blocker（若有）和下一条合规路径。不要用活动记录代替证据。

## 输出

- **`Status: Unresolved Intent`** —— 当前理解、仍会改变 Goal 的分叉，以及最小 Human 决定或证据探针；
- **`Status: Blocked`** —— 准确的非意图阻塞，以及恢复安全推进所需条件；
- **`Status: Executable`** —— 一本有现实依据、包含 best-known Execution/Graph、Verification、Evidence 要求和 Completion Hook 的自主任务书；用户要求直接完成工作时按 Handoff 继续执行。

Northstar 不增加 scheduler、manager daemon、workflow owner、Completion layer、Acceptance layer 或固定 Acceptor 角色。