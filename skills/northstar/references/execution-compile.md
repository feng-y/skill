# 自主任务书：把稳定 Goal 写成执行合同

只在 Goal 已定准后使用。最终产物是一份**当前证据下足够完整、又不猜未来**的任务书，让 fresh Executor 能独立启动、看见已知全局结构，并依靠现场 Evidence 调整真正不确定的部分。

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

这是一条 semantic ownership / proof chain，不是固定时间阶段。物理结构保持稀疏：**one fact, one owner**。当前 Evidence 已经足以确定的 Task、关系和 Verification obligation 应一次编译清楚；只有存在、范围或具体动作仍实质依赖未来 Evidence 的部分才延迟展开。空 section、重复 context 和 speculative future work 都省略。

## Goal

只写一个简洁的 Human-owned Goal：目标结果、必须保持什么、最终交付。Why 只有在会改变取舍时才写。

已确认边界、授权限制、受保护副作用，或 Northstar 替 Human 作出的未确认 delegated default，只有在确实约束执行时才表达，并且只写一次。Human 明确验证要求属于 Verification，不写回 Goal。

不要新增 Completion/Acceptance 语义。

## Execution / Graph

编译**当前证据支持的 best-known complete execution structure**，不是只给下一步，也不是模拟未知未来。

一个 Task 是 executable delta，不是 miniature prompt。通常只包含：

- 可观察结果；
- 只有不明显时才写的 starting point / Task-local hard constraint；
- 已经明确适用、且确实决定是否可以继续推进时的一次 local check。

不要把 Goal、全局边界、共享 Reality、repo rules 或 Goal-level Verification 复制进每个 Task。

当前 Evidence 已经证明必然存在、边界足够稳定且关系真实的工作，应一次编译出来；简单工作保持一个粗粒度 Task 或最短线性结构，真实 dependency、并行、shared write、Task Group boundary 或 join 会改变执行判断时才读取 [execution-graph.md](execution-graph.md)。只有某项工作**是否存在、影响范围或必要关系**仍取决于未来 Evidence 时，才不提前物化；运行时 Evidence 使它成为现实后再加入同一本 taskbook。

**Task 0** 是可选、bounded 的 execution warmup。只有在主要执行前关闭少量 Unknown 能显著改善 grounding、路线判断、稳定性或 required Verification 时才使用：例如绑定真实 repo/worktree/target、核对 material premise 或 baseline、证明关键 judge/provider 会真实运行并传播失败、确认会改变执行路线或验证范围的 runtime fact。当前 Evidence 已足以安全开始时立即停止 warmup；普通 execution fact 留给 Executor 按需发现。Task 0 不是第二个 Research 阶段，也不是固定 checklist。

运行时推进保持一条闭环：

```text
ready work → execute / probe / applicable Verification → Evidence → update affected Execution / Graph / Verification → Completion Hook → continue / expand / stop / block
```

已编译且前提仍成立的工作继续复用，不因新一轮判断重新规划整本 taskbook。新 Evidence 只增加、删除、拆分、合并或重排真正受影响的 contingent / invalidated 部分。多个新 probe / task 都能缩小同一个 material gap 时，优先成本更低且更可能改变 Execution / Verification 判断的那个。只要 Goal、已确认边界、Human authority 和 required Verification 仍稳定，就继续同一本 taskbook；真正越过稳定边界时按 [SKILL.md](../SKILL.md) 路由。

## Verification

Verification 的 Task / Task Group / Goal 粒度是**placement rule**，不是要求 Compile 时预先填满三层 verification roadmap。

- **Task**：已经明确的局部检查如果决定能否继续，应随 Task 一起编译；执行后才暴露的局部 obligation 到真实适用时再物化；
- **Task Group**：已知组合行为需要独立证明时，在最小组合边界编译一次；组合关系本身仍 contingent 时，等 Evidence 证明 join/coverage 真实存在再加入；
- **Goal**：保留 repo authority 或 Human 明确验证要求要求的最终 delivery-level coverage，不预设额外“最终验证命令”。

已知 Verification obligation 和已知、可靠的具体 action/scope 应直接编译；如果 concrete provider、target、scope 或 obligation 是否触发仍依赖执行期 change surface、binding/config、provider validity 等事实，则把稳定 trigger/authority 保留下来，等运行时事实成立后再 materialize 对应 Verification action。

Goal-level Verification 是最终 **coverage boundary**，由 Taskbook 的 Completion Hook 消费；仍有效的低层 Evidence 直接复用，只补真实 coverage gap 或已失效的 required checks。

Required Verification 跟真实 impact/reachability 和 repo verification authority 走。预期 `0-diff`、cleanup 或 refactor 不能降低已经触发的要求。具体 provider 只能证明其真实覆盖范围；provider 在实际证明可运行并传播失败前只是声明。只有执行环境才能确认且值得在主要修改前关闭的 provider/binding trigger 才放进 Task 0，其余在真正使用时验证。

当 repo authority 允许多个同等可信、同等覆盖的 provider 或 boundary 时，优先选择成本更低且失败信号更能缩小问题空间的那个；信息量不能替代必要 coverage。

普通受保护 repo Verification 可能假绿、可被针对性优化、静默失效或确实需要 independent Evidence 时，才读取 [verification-trust.md](verification-trust.md)。

## Evidence

Compile 的是 proof / trust requirement，不是未来 Evidence 结果。运行时只保留足够判卷 material claim、支持下一步判断或最终停止的实际 Evidence：provider/probe、相关 target/revision 和关键 binding/config、verdict/exit，以及原始输出或稳定 artifact/reference。

Executor 的活动说明或自报 `PASS` 只是输入，不是最终 Evidence。判断方能以合理成本访问权威环境时，对最终结论关键的 repo-authoritative Evidence 直接重新取证；否则要求可复现 provenance。缺失、stale、coverage 不足或 judge 被削弱的 Evidence 都不能支持 PASS。

Evidence 只让受影响的结论失效：版本、环境、对象、binding/config、上游行为或 judge 前提没有改变时直接复用，不因为 Graph 变化或进入更高层 Verification 就机械重取。新 Evidence 推翻旧 claim 时，在原 semantic owner 处替换或失效旧状态，不保留相互冲突的有效副本。

## Completion Hook

Taskbook 自带一个 completion judgment，但不新增 Completion layer、schema、state object 或 Acceptor。它只读取已有 owner：**Goal / constraints + 已触发的 required Verification + current valid Evidence**。

在 material Evidence 更新后的 decision boundary 判断：

- Goal 的 material outcome 是否已有最低充分 Evidence 覆盖；
- must-preserve、confirmed boundaries、Human authority 和 repo hard constraints 是否仍成立；
- 所有已经真实触发的 required Verification 是否已有可信且仍有效的 Evidence。

三者都满足就直接 `STOP`，不为了仪式再制造 Final Verification Task；仍有 material gap 就继续已有 work 或只扩展能关闭该 gap 的 contingent work / Verification；没有安全路径能缩小 gap 时准确 `BLOCKED` / non-PASS。初始 Task 做完或 frontier 为空本身都不是完成条件。

最终报告保持很小：实际交付、决定性 Evidence、精确 residual/blocker（若有）、下一条合规路径。不要回放整个执行历史。

## Handoff check

Handoff 前只确认：

- 一个稳定 Goal 和 material authority constraint 已各自表达一次；
- 当前 Evidence 已能确定的 required Tasks / relations / Verification obligations 已充分编译，而不是为了 lazy 故意隐藏已知工作；
- contingent work 没有被 speculative materialize，且至少一个 Task 或必要 Task 0 可立即开始；
- required Verification 不重复，Goal-level coverage 仍可达到，Completion Hook 能基于现有 owner 做 stop / continue / block 判断；
- 当前 execution state 没有同一事实的多份 authoritative copy，也没有重取前提未变化的 discovery / Evidence；
- 最终 Evidence 可判卷，并且没有新增 Completion/Acceptance、scheduler、Graph engine 或固定 Agent topology。

不会改变执行判断的内容，直接省略。