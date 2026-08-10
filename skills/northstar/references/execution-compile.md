# 自主任务书：把稳定 Goal 写成执行合同

只在 Goal 已定准后使用。产物是一份**当前证据下足够完整、又不猜未来**的任务书，让 fresh Executor 看见已知全局结构并独立推进。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 semantic ownership / proof chain，不是固定时间阶段。保持 **one fact, one owner**：当前 Evidence 已能确定的 Task、关系和 Verification obligation 一次编译清楚；只有存在、范围或具体动作仍实质依赖未来 Evidence 的部分才延迟展开。

## Goal

只写一个 Human-owned Goal：目标结果、必须保持什么、最终交付；Why 只有会改变取舍时才写。已确认边界、授权限制、受保护副作用或未确认 delegated default 只有确实约束执行时才表达，并且只写一次。Human 明确验证要求属于 Verification，不写回 Goal。

不要新增 Completion/Acceptance 语义。

## Execution / Graph

编译**当前证据支持的 best-known complete execution structure**，不是只给下一步，也不是模拟未知未来。

一个 Task 是 executable delta，通常只包含：

- 可观察结果；
- 不明显时才写的 starting point / Task-local hard constraint；
- 已经明确适用、且决定能否继续时的一次 local check。

不要把 Goal、全局边界、共享 Reality、repo rules 或 Goal-level Verification 复制进每个 Task。当前 Evidence 已证明必然存在、边界足够稳定且关系真实的工作应一次编译；简单工作保持线性，真实 dependency、并行、shared write、Task Group boundary 或 join 会改变判断时才读取 [execution-graph.md](execution-graph.md)。只有 work 的**存在、影响范围或必要关系**仍取决于未来 Evidence 时才延迟物化。

Human 已确认的执行策略、scope boundary 或 must-preserve constraint 属于当前合同输入，不因模型重新分层而被替换。当前 Evidence 已支持安全、bounded 的 ready frontier 时直接表达它；尚未阻塞当前 frontier 的 execution Unknown 不先物化成 prerequisite Task。**ready frontier 只表示现在可以执行什么，不改变 Human-owned Goal；当前只暴露一部分工作，不得把 Goal 改写成更窄的 phase 或局部 subgoal。** Graph 的 stop boundary 来自 Goal / confirmed boundaries；执行中发现相邻 residual 不自动扩 scope。

**Task 0** 是可选、bounded 的 execution warmup，只在缺少某个执行期事实会阻止第一项安全 material action，或 required Verification 明确要求在第一项 material action 前关闭 trigger 时使用。它不是第二个 Research 阶段、默认 checklist 或普通 execution Unknown 的收集区。当前 ready work 可以安全开始时，其他事实交给 Executor 在真正影响该 work 时按需取得。

运行时保持：

```text
ready work → execute / probe / applicable Verification → Evidence → update affected Execution / Graph / Verification → Completion Hook → continue / expand / stop / block
```

仍有效的已编译工作直接复用；新 Evidence 只修正 contingent / invalidated 部分。多个新 probe / task 都能缩小同一 material gap 时，优先成本更低且更可能改变 Execution / Verification 判断的那个。Goal、已确认边界、Human authority 和 required Verification 仍稳定时继续同一本 taskbook；越过稳定边界才按 [SKILL.md](../SKILL.md) 路由。

## Verification

Task / Task Group / Goal 是 **placement granularity**，不是要求 Compile 时填满三层 verification roadmap：

- **Task**：已明确、决定能否继续的局部检查随 Task 编译；runtime 才触发的 obligation 到适用时再加入；
- **Task Group**：已知组合行为需要独立证明时，在最小组合边界编译一次；contingent join 等 Evidence 证明后再加入；
- **Goal**：保留 repo authority 或 Human 明确要求的 delivery-level coverage，不预设额外“最终验证命令”。

已知 Verification obligation 和可靠的具体 action/scope 直接编译；provider、target、scope 或 obligation 是否触发仍依赖 change surface、binding/config、provider validity 等执行期事实时，只保留稳定 trigger/authority，事实成立后再 materialize 对应 action。

Goal-level Verification 是 Completion Hook 消费的 **coverage boundary**：复用仍有效的低层 Evidence，只补真实 coverage gap 或已失效 check。Required scope 跟真实 impact/reachability 和 repo authority 走；`0-diff`、cleanup、refactor 不能降级已经触发的要求。provider 在证明真实运行、覆盖 claim 并传播失败前只是声明；同等可信和覆盖时优先成本更低、失败信号更能缩小问题空间的选择。

普通 repo Verification 可能假绿、可被针对性优化、静默失效或确实需要 independent Evidence 时，才读取 [verification-trust.md](verification-trust.md)。

## Evidence

Compile 的是 proof / trust requirement，不是未来结果。运行时 Evidence 只保留足够判卷和支持下一判断的 material facts：provider/probe、target/revision、关键 binding/config、verdict/exit，以及原始输出或稳定 artifact/reference。

Executor 的活动说明或自报 `PASS` 不是 Evidence。判断方能以合理成本访问权威环境时，对最终结论关键的 repo-authoritative Evidence 直接重新取证；否则要求可复现 provenance。缺失、stale、coverage 不足或 judge 被削弱都不能支持 PASS。

Evidence 只让受影响结论失效：相关前提没变就复用；新 Evidence 推翻旧 claim 时，在原 semantic owner 处替换或失效旧状态，不保留冲突的有效副本。

## Completion Hook

Taskbook 自带 completion judgment，但不新增 Completion layer/schema/state/Acceptor。它只读取 **Goal / constraints + 已触发 required Verification + current valid Evidence**，在 material Evidence 更新后的 decision boundary 判断：

- Goal material outcome 是否已有最低充分 Evidence；
- must-preserve、confirmed boundaries、Human authority 和 repo hard constraints 是否仍成立；
- 已触发 required Verification 是否都有可信且有效的 Evidence。

全部满足就 `STOP`，不制造 Final Verification Task；仍有 material gap 就继续已有 work 或只扩展能关闭 gap 的 contingent work / Verification；没有安全路径就准确 `BLOCKED` / non-PASS。Task 做完或 frontier 为空本身都不是完成条件。

最终报告只保留实际交付、决定性 Evidence、精确 residual/blocker（若有）和下一条合规路径。

## Handoff check

Handoff 前只确认：

- Goal / material authority 各自只有一个 owner；
- 当前 Evidence 已确定的 required Tasks / relations / Verification obligations 已充分编译，没有为了 lazy 隐藏已知工作；
- ready frontier 没有反向缩小 Human Goal，Human 已确认的执行策略和 stop boundary 没有被模型重写；
- contingent work 没有 speculative materialize，且至少一个 Task 或真正必要的 Task 0 可立即开始；
- required Verification 不重复，Completion Hook 能基于现有 owner 判断 stop / continue / block；
- 没有重取前提未变化的 discovery / Evidence，也没有新增 Completion/Acceptance、scheduler、Graph engine 或固定 Agent topology。

不会改变执行判断的内容，直接省略。