# Complex Execution Compile

只在 Goal 已稳定、但 fresh Executor 需要多个 work unit、execution-time discovery、baseline / resume state 或非平凡 Verification 才能独立完成时读取。Goal semantics、Unknown ownership 与最终 artifact transport 仍由 `SKILL.md` 拥有。

## Output filter

Compile 是输出过滤器，不是 Research 转录器。准备写入 Taskbook 的事实过两问：

1. Executor 能否从 authoritative reality 低成本、可靠重算？能则优先写判据，不写 inventory / 行号 / patch 明细。
2. 省略它是否会显著增加错误 scope、错误保留/删除、错误 Verification 或不安全执行？会则保留这个 trap / counterexample / non-obvious reality。

更多 Evidence 应压成更少、更稳定的 judgment，而不是更多 instruction。

## Work units

Task 默认是 **outcome + judgment**，让 Executor 在一个稳定判据下处理完整同类 surface；不是 executable delta、文件清单或 predicted patch。只有 outcome、judgment、dependency、authority、risk 或 required Verification 真不同才拆 Task。

开放 surface 写 discriminator + territory，让 Executor 扫全集；不要把 Research 已发现的实例变成封闭 checklist。直接沿用 `SKILL.md` 已收敛的 Goal contract，本文件只在其边界内组织 work。

当前 workspace 中仍与 Goal 对齐的修改作为 starting reality 复用；“已经改了”不是 correctness Evidence，也不要求 clean checkout 后重做。

**Task 0** 只关闭第一项安全 material work 前真正阻塞执行的少量事实，或 material work 前必须确认的 binding Verification trigger。它不是第二轮 Research、完整 inventory 或默认 preflight。

## Starting baseline

只有承担 coverage / attribution / stale detection 的 baseline 才进入 Taskbook。命令、target、参数必须来自真实 authority；环境不可达就要求 Executor 先核实，不能编造。

作为 execution premise 的 baseline 在首次受影响 material work 前复算。mismatch 只让依赖该 premise 的 work / Evidence stale；修正受影响 Execution / Verification，其他 still-valid state 继续复用。

## Graph

没有真实 relation 就保持线性。只有多个 work unit 之间存在会改变 execution judgment 的 **dependency、parallel、shared write、join 或 Evidence-contingent relation** 时，读 [execution-graph.md](execution-graph.md)。Graph 不因为任务“很大”自动出现。

## Verification / Evidence

沿用 `SKILL.md` 的 Verification contract；复杂 Taskbook 只额外 materialize provider / target / scope 的稳定 trigger 与 authority，让 Executor 按实际 change surface / binding / runtime reality 触发具体 action。

Research candidate 不自动获得 hard acceptance authority。`0-hit / 0-count` 只有在对象已被证明属于 target responsibility、且归零本身承担 completion claim 时才 binding；否则写 discriminator + coverage oracle。

前提仍有效的 Evidence 可复用，新 Evidence 只让依赖它的结论 stale。具体 false-green / gameability / independence 风险存在时再读 [verification-trust.md](verification-trust.md)。

## Success and failure judgment

Executor 只有在 Goal contract + triggered required Verification + current valid Evidence 覆盖 completion claim 时才能停止；frontier 为空不是完成证明。

失败路径同样要可执行：可信 baseline green→red 时先恢复或准确报告；同一路线反复失败且没有新增 Evidence 时不要无限硬顶，改用有依据的新策略、切换独立 work 或报告 blocker/non-PASS。不得通过 skip/todo、放松断言、删活体测试、mock 掉目标、吞失败、`|| true` 等削弱 judge 来制造 PASS。

## Durable execution state

对于复杂/autonomous run，把 `SKILL.md` 已定义的 execution state 写入现有 `implement-notes`：progress、new Unknown、关键 decision/Evidence、blocker 和 resume point。新 session 先恢复它，只重做前提变化或 Evidence stale 的部分；不要形成第二本 Taskbook。
