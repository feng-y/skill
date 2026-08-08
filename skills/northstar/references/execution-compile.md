# 自主任务书：把稳定 Goal 写成执行合同

只在 Goal 已定准后使用。最终产物是最小但可信的任务书，让 Executor 能安全启动，并依靠现场判断继续推进。

语义 ownership 保持固定：

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

物理结构保持稀疏：**one fact, one owner**。只物化会改变执行判断的信息；空 section、重复 context 和 speculative future work 都省略。任务书是启动合同，不是对未来执行的完整模拟。

## Goal

只写一个简洁的 Human-owned Goal：目标结果、必须保持什么、最终交付。Why 只有在会改变取舍时才写。

已确认边界、授权限制、受保护副作用，或 Northstar 替 Human 作出的未确认 delegated default，只有在确实约束执行时才表达，并且只写一次。Human 明确验证要求属于 Verification，不写回 Goal。

不要新增 Completion/Acceptance 语义。

## Execution / Graph

只编译**当前证据支持的最小可执行结构**。

一个 Task 是 executable delta，不是 miniature prompt。通常只包含：

- 可观察结果；
- 只有不明显时才写的 starting point / Task-local hard constraint；
- 只有确实决定是否可以继续推进时才附一次 local check。

不要把 Goal、全局边界、共享 Reality、repo rules 或 Goal-level Verification 复制进每个 Task。

简单工作保持线性。只有真实 dependency、并行、shared write、Task Group boundary 或 join 会改变调度时，才读取 [execution-graph.md](execution-graph.md)。不要提前物化那些存在与否仍取决于未来 Evidence 的 downstream Task：先执行当前 frontier，再只扩展新 Evidence 真正证明存在的工作。

只在某个 premise **编译时已知重要，但必须进入执行环境后、实质修改前才能确认**时使用 **Task 0**。Task 0 不是第二个 Research 阶段。

运行时推进只有一条：

```text
ready work → execute / probe → Evidence → update remaining Graph → continue
```

只要 Goal、已确认边界、Human authority 和 required Verification 仍稳定，Evidence 就可以增加、删除、拆分、合并或重排剩余工作；前提仍成立的已完成工作直接复用。真正越过这些稳定边界时，按 [SKILL.md](../SKILL.md) 路由，不在这里再编码第二套控制流。

## Verification

每个 Verification obligation 只写一次，并放在最低有意义边界：

- **Task**：只有局部检查决定是否可以继续时，附成本最低且足够的检查；
- **Task Group**：局部检查无法证明组合行为时，在最小组合边界写一次更大范围验证；
- **Goal**：只保留 repo authority 或 Human 明确验证要求仍要求的最终 delivery-level coverage。

Goal-level Verification 是最终 **coverage boundary**，不是固定额外命令。仍有效的低层 Evidence 直接复用，只补尚未覆盖或已失效的 required checks。

Required Verification 跟真实 impact/reachability 和 repo verification authority 走。预期 `0-diff`、cleanup 或 refactor 不能降低已经触发的要求。具体 provider 从 repo verification system 中选择，只能证明其真实覆盖范围；只有执行环境才能确认的 provider/binding trigger 放进 Task 0。

普通受保护 repo Verification 可能假绿、可被针对性优化、静默失效或确实需要 independent Evidence 时，才读取 [verification-trust.md](verification-trust.md)。

## Evidence

不要把 Verification plan 再改写成重复 prose。只保留足够判卷 material claim 的 Evidence：实际 provider/probe、相关 target/revision 和关键 binding/config、verdict/exit，以及原始输出或稳定 artifact/reference。

Executor 的活动说明或自报 `PASS` 只是输入，不是最终 Evidence。判断方能以合理成本访问权威环境时，对最终结论关键的 repo-authoritative Evidence 直接重新取证；否则要求可复现 provenance。缺失、stale、coverage 不足或 judge 被削弱的 Evidence 都不能支持 PASS。

最终报告保持很小：实际交付、决定性 Evidence、精确 residual/blocker（若有）、下一条合规路径。不要回放整个执行历史。

## Handoff check

Handoff 前只确认：

- 一个稳定 Goal 和 material authority constraint 已各自表达一次；
- 至少一个 Task 或必要 Task 0 可立即开始，并且只物化当前有证据支持的 Task / relation；
- required Verification 不重复，且 Goal-level coverage 仍可达到；
- 最终 Evidence 可判卷，并且没有新增 Completion/Acceptance、scheduler、Graph engine 或固定 Agent topology。

不会改变执行判断的内容，直接省略。