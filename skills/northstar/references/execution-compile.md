# 自主任务书：把稳定 Goal 写成执行合同

只在 Goal 已定准后使用。最终产物是一份紧凑、权威的任务书，让 Executor 能安全启动，并依靠现场判断继续推进，而不是机械复述一份冗长计划。

语义 ownership 保持不变：

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

任务书的**物理展开保持稀疏**：只有会改变执行判断的 section / clause 才出现；同一事实只在自己的 semantic owner 下写一次，后续只消费，不重复解释。不要为了结构完整填空，不要把全局约束复制进每个 Task，也不要因为“未来可能发生”就提前展开工作。

任务书是可信的启动合同，不是对未来执行的完整模拟。只编译**当前证据支持的最小可执行结构**：足以启动、暴露真实依赖、守住 authority，并让 required Verification 可达。后续由运行时 Evidence 扩展或修正剩余工作。

## Goal

Goal 保持简洁：Human 要达到的结果、必须保持什么，以及本次明确交付。Why 只有在会改变取舍或执行判断时才写。

已确认边界、授权限制、受保护副作用，或 Northstar 替 Human 作出的未确认 delegated default，只有在确实约束执行时才写，并且只写一次；不要在每个 Task 里复述。Human 明确验证要求不属于 Goal，单独放到 Verification。

Goal 本身定义成功；不要增加 Completion Contract、completion properties、Acceptance layer 或其他 done taxonomy。

## Execution / Graph

Execution 只承载当前 Evidence 已经证明值得执行的工作。

一个 Task 是**可执行 delta**，不是缩小版 prompt。通常只需要：

- 完成后可观察到的结果；
- 只有不明显时才写的 starting point / 本 Task 独有硬约束；
- 只有确实控制后续推进时才附一次成本最低且足够的 local verification。

不要把 Goal、全局边界、共享 Reality、repo-wide rules 或 Goal-level Verification 复制进每个 Task。

简单工作保持线性。只有真实 dependency、并行、shared write、Task Group boundary 或 join 会改变执行判断时，才读取 [execution-graph.md](execution-graph.md)。Graph 只表达这些关系；省略传递依赖和单纯先后顺序。

不要为了让计划看起来完整而物化 speculative downstream Task / edge。如果当前 Evidence 只足以确定 Task A，而 B/C/D 取决于 A 的发现，就只编译 A 和已知 decision boundary；运行 A 后再让 Evidence 决定 B/C/D。

### Current Reality 与 Task 0

只记录会改变 Execution 或 Verification 的现实；大段支撑信息保留 source/reference，不复制进任务书。

只在某个 premise **编译时已经知道重要，但必须进入执行环境后、实质修改前才能确认**时使用 **Task 0**，例如真实 worktree/target binding、provider 是否可用、effective config，或 execution-only Verification trigger。Task 0 不是第二个 Research 阶段。

Task 0 或后续执行改变 implementation reality 时，只更新剩余 Execution / Graph 和受影响 Verification；前提仍成立的已完成工作与 Evidence 继续复用。

### Runtime progression

Executor 面对当前 ready frontier：

```text
ready work → execute / probe → Evidence → update remaining Graph → continue
```

新发现的事实只有在会改变当前执行判断时才 inline 解决。一个分支 Blocked，但独立工作仍 ready 时继续；join 只等待真实 dependency。已完成工作不机械重开，只有 Evidence 前提或 required combined Verification 被影响时才重新取证。

只有安全继续必须改变 Goal、已确认边界、Human 明确验证 authority、优先级或授权时，才回到 Human / Intent Take；其余变化在 Execution 内局部调整。

## Verification

Verification 在第一次真正需要的位置写一次，不在其他 section 重复。

- **Task 级**：当局部检查决定是否可以继续时，把成本最低且足够的检查附在该 Task 上一次；
- **Task Group 级**：只有局部检查无法证明组合行为时，在最小有意义组合边界 / join 写一次更大范围验证；
- **Goal 级**：只保留尚未被低层充分表达的最终 coverage obligation——Human 明确验证要求，以及 repo authority 仍要求的交付级验证。

Goal 级 Verification 是最终 **coverage boundary**，不是固定多跑一次 final command。仍有效的 Task / Task Group Evidence 直接复用，只补尚未覆盖或已失效的 required checks。

Required Verification 跟真实 impact/reachability、repo verification authority 和 Human 明确验证要求走。只有当 proof scope 会被改变时，才从 changed owner / shared responsibility / system contract 追到 effective binding/config 与真实 consumer/target。cleanup/refactor 标签和预期 `0-diff` 都不能降低已经触发的 Verification。

具体 test/build/replay/static/symbol provider 从 repo verification system 中选择，只能证明实际覆盖的行为；不要编译固定套餐。文档中的 provider 先当声明；Handoff 前能实测就实测，只有执行环境才能确认时交给 Task 0。

普通受保护 repo Verification 可能假绿、可被针对性优化、静默失效或确实需要独立 Evidence 时，才读取 [verification-trust.md](verification-trust.md)。

## Evidence

任务书只规定必须保留什么 Evidence，不把 Verification plan 再改写成一段重复 prose。

用于最终判断的关键 Evidence 要能复核 material claim：跑了什么 provider/probe、针对什么 target/revision 和关键 binding/config、verdict/exit 是什么、原始输出或稳定 artifact/reference 在哪里。保持与风险相称，不附加不会改变判断的仪式性 metadata。

Executor 的 `done`、`PASS`、实现说明和二手摘要只是输入，不是最终 Evidence。判断方能访问权威环境时，对最终结论关键且成本合理的 repo-authoritative Evidence 直接重新取证，不机械重跑全部 local check。缺失、stale、coverage 不足或 judge 被削弱的 Evidence 都不能支持 PASS。

最终报告只写：实际交付、决定性 Evidence、精确 residual/blocker（若有）、下一条合规路径。不要回放整个执行历史。

## Compile check

Handoff 前只确认：

- 一个稳定 Goal 和明确交付存在；
- material authority / boundary constraint 只表达一次；
- 至少一个 Task 或必要 Task 0 可以立即开始；
- 只物化当前 Evidence 已证明合理的 Task / relation；
- required Verification 放在最低有意义的 Task / Task Group / Goal 边界，且不重复；
- Goal-level coverage 仍可达到；
- 最终 Evidence 可以从权威环境或可复现结果中判卷；
- 没有新增 Completion/Acceptance layer、scheduler、manager、Graph engine、persistent Graph state 或固定 Agent topology。

任何内容如果不会改变执行判断，就省略，而不是为了 taskbook 的结构完整去填。