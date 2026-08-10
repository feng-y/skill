# 自主任务书：把稳定 Goal 编译成判断充分的执行合同

只在 Goal 已定准后使用。Taskbook 要让 fresh Executor 独立完成目标，但**不替 Executor 预写 patch**。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 compiler 内部 ownership / proof chain，不是输出模板。**decision-complete ≠ information-complete。** Research 可以很深，Taskbook 只保留会改变 Executor 判断的信息。

## Goal

只写一个 Human-owned Goal，并明确：

- **Outcome**：最终必须成立的结果属性；
- **Decision priority**：冲突时的让步顺序，未列情况按此自裁；
- **Allowed boundary**：允许持续发现和处理的 territory；
- **Forbidden boundary**：不能碰、不能顺手扩展的 territory；
- **Must-preserve**：行为、接口、数据、验证权威等不可退化属性；
- 最终交付。

不要把模型选择的内部代码形状默认写成 success criterion。目录消失、文件搬迁、namespace 改名、某个 patch shape 只有在 Human 明确要求、repo authority 要求或其本身就是 Goal invariant 时才属于 Goal。

## Compile output filter

Compile 是输出过滤器，不是 Research 转录器。每条准备写入 Taskbook 的事实都过两问：

1. Executor 能否从 authoritative repo reality 低成本、可靠地重新取得？若能，优先写判据，不写清单/行号/明细。
2. 省略它是否会显著增加错误 scope、错误删除/保留、错误 Verification 或不安全实现的概率？若会，这个 trap / counterexample / non-obvious reality 必须保留。

因此：

- 文件行号、普通 include 明细、symbol count、候选 patch、可重算 inventory 默认省略；
- 同名异义、假依赖、非显然 surviving consumer、真实 hard boundary、会改变验证触发的 binding 等必须保留；
- 可复算的 baseline/count 可以保留，因为它们是 coverage oracle / attribution anchor，而不只是背景信息。

更多 Evidence 应该压缩成更少、更可靠的 judgment，而不是更多 instruction。

## Execution / Graph

Taskbook 默认只保留少量 **outcome + judgment work unit**。

一个 Task 应该让 Executor 能在统一 judgment 下扫描并处理完整同类 surface，通常只需要：

- 要达到的局部 outcome；
- 适用 territory / starting reality，仅在不写会误判时给出；
- 会反复决定“改 / 保留 / 跳过 / block”的 stable judgment；
- 真正限制选择空间的 hard constraint；
- 已经 binding、决定该 work 是否成立的 Verification obligation。

**Task 不是 executable delta、文件路径清单或 predicted patch。** 路径/文件只有在集合封闭、不能从 repo 可靠推导、且枚举本身就是判据时才列。对于开放 surface，写判据让 Executor 自己扫全集；否则 checklist 外的第 N+1 个同类残留会永久漏掉。

不因为 Research 已知一个高置信实现方案，就把具体文件拆法、搬迁目的地、函数抽取行号、include/BUILD 改写、命令顺序或 failure-localization tactic 固化成合同。只有 Human / repo authority /真实 dependency / risk 或唯一安全路径要求时才固化 How。

**法与情报分开**：`必须/不许` 只来自 Human、repo authority 或已验证 reality；模型推荐的路线即使置信度高，也默认只是 intelligence。Executor 找到更小、更稳且满足 Goal/authority 的路径可以改走，并在 `implement-notes` 记录原因。

只要 Goal / decision priority / boundary / authority 已足以安全裁决，普通事实或技术 Unknown 由 Executor 在执行期取证后自行决定；只有裁决需要改变 Human-owned Goal、boundary、明确 Verification、priority 或 authorization 时才回到 Human。

当多个实例共享同一个 judgment 时合并成一个 Task；只有 outcome、judgment、dependency、authority、risk 或 required Verification 真不同才拆。Graph 只表达会改变 execution judgment 的真实 dependency / parallel / join，不为了“精确”把工作切成 patch nodes。

Human 已确认的 strategy / scope boundary / must-preserve 直接保留。ready frontier 只表示现在能做什么，不改变 Human Goal；adjacent residual 不自动扩 scope。

当前 workspace 中仍与 Goal 一致的修改作为 starting reality 复用；“已经改了”不是 correctness Evidence，不要求重做，也不据此缩 Goal。

**Task 0** 只在缺少某个执行期事实会阻止第一项安全 material work，或 required Verification 明确要求在 material work 前关闭 trigger 时使用。它不是 Research continuation、inventory 或默认 checklist。

## Starting baseline

交付前尽量建立可归因起点。对本任务真正有判卷价值的 build/test/replay/static probe 实测 baseline；范围需要度量时优先给可复算 signal，例如 target 数、grep 命中数、文件/行数量级和测量时间，而不是完整 path inventory。

Taskbook 只保留能让 Executor 复算 scope、判断漏项或区分“原本就坏”与“本次改坏”的 baseline。命令没实测、数字对不上或环境不可达时，不伪造；Taskbook 中未来要执行的命令至少确认真实存在、target/参数可信，必要时把核验放入 Task 0。

**凡被编译进 Taskbook 并作为 scope / coverage / attribution premise 的 baseline，Executor 在首次受影响 material work 前必须用同一 authoritative probe 复算。** 若结果不匹配，不得把旧值当 truth 继续：立即把依赖该 premise 的 assumption / Evidence 标 stale，暂停受影响 work，按当前 reality 修正 Execution / Verification；与该 mismatch 无关的 work / Evidence 继续复用。这个 recheck 是 baseline 的使用条件，不把所有任务机械变成 Task 0。

## Verification

Verification 冻结**必须证明什么**，不默认冻结**为了实现/调试应该怎么跑**。

- Task：只有 local check 已经 binding 且决定是否能继续时才写；
- Task Group / join：组合行为必须单独证明时才写；
- Goal：保留 repo authority 或 Human 明确要求的 delivery coverage。

Provider、target、scope 依赖 change surface / binding / runtime reality 时，编译稳定 trigger/authority，让 Executor 在触发后 materialize 具体 action。cleanup/refactor/expected `0-diff` 不能降低已经触发的 required Verification。

“每改一个文件都 build”“每搬一个类型都单独 test”这类 failure-localization tactic 默认属于 Executor，不进入 binding contract，除非 repo/Human authority 或特殊风险明确要求。

需要额外 judge trust 时按需读取 [verification-trust.md](verification-trust.md)。

## Evidence

Compile proof / trust requirement，不编译未来结果。最终 judgment 需要的 Evidence 应可复核并覆盖真实 claim；Executor 自报 `PASS` 或活动说明不是 Evidence。前提未变化的 Evidence 可复用，新 Evidence 只让受影响结论失效。

Evidence 证明 **judgment + completion claim**，不默认要求开放 surface 的每个文件/符号分别建立删除/保留账本。只有逐项对账本身就是权威验收，或缺少它就无法证明 completion claim 时，才要求 per-instance accounting。

## Completion Hook

Taskbook 自带 stop judgment，但不新增 Completion layer。Completion 同时定义成功路径和失败路径：

### Success

只读取 **Goal / constraints + triggered required Verification + current valid Evidence**：

- Goal material outcome 是否已有最低充分 Evidence；
- decision priority 下更高优先级属性是否没有被较低优先级目标破坏；
- must-preserve / allowed+forbidden boundaries / authority 是否仍成立；
- triggered required Verification 是否都有可信 Evidence。

全部满足才 `STOP`。

### Failure / stop-loss

- 同一验收连续失败 3 次且没有新增 Evidence 时，不继续同一路线硬顶；切换独立 work、改变有依据的策略，或准确报告 non-PASS/blocker；
- 可信 baseline 从绿变红时，优先恢复到绿再继续；恢复不了就如实报告，不把退化状态当完成；
- “没做成但说清了”优于“做了但更糟”；
- 禁止通过 `.skip` / `todo`、放松断言、删除活体测试、mock 掉被测对象、改阈值、吞错误、`|| true` 或其他削弱 judge 的方式制造 PASS。测试随被删主体一起删除时必须由 Goal / dead-code judgment 正当化并可对账。

## Durable execution state

开工先在现有 `implement-notes` 写 ≤10 行 Goal / 执行顺序 / 最大风险；之后持续记录 execution progress、new Unknown、blocker、关键 decision/Evidence 和 resume point。换 session 后先读它，只重做前提已变化或 Evidence 已失效的工作；conversation 不作为唯一状态存储。

## Handoff check

发出前只问：

- Goal 写的是 outcome，还是把模型选的 implementation shape 偷偷当成功标准？
- 冲突时是否有清楚 decision priority，未列情况能否据此自裁？
- allowed / forbidden boundary 是否双向清楚？
- Taskbook 是否定义了任务，而不是展示 Northstar 的调研过程？
- 每个 Task 是否是 outcome + judgment，而不是文件/函数/checklist/patch step？
- 同一个 judgment 能覆盖的开放 surface 是否由 Executor 扫全集，而不是静态枚举？
- 普通技术 Unknown 是否仍留给 Executor judgment，而不是因为未决就升级 Human？
- `必须/不许` 是否都有 authority，还是把模型建议误写成 law？
- Evidence 是否在证明 judgment / claim，而不是重新拆成逐实例账本？
- 是否保留了不写就会让 Executor 判错的 trap，同时删除了可安全重算的明细？
- baseline 是否可复算，并明确了 mismatch 时 stale / pause / repair affected state 的 gate？
- Verification 是否冻结 required proof，而没有把 debugging tactic 变成硬流程？
- Completion 是否同时有 success、stop-loss、rollback 和 judge-integrity 路径？
- execution Unknown 是否有 `implement-notes` resume carrier？

自主执行 Taskbook 默认 **≤4000 字符**；只有 Human 明确要 long-form artifact 或目标 runtime 已知使用不同限制时放宽。超长先压缩 judgment、删重复、删可重算明细，不通过把一个 Human Goal 拆成多个 layer Goal 来规避长度。

如果删除某段不会改变 Executor 的目标、边界、判断、验证、失败处理或恢复方式，就删除它。
