# 当简单 Taskbook 不够

只在 Goal 已经定准，但任务很长、需要几种不同判断、真实依赖、较强验收或跨会话继续时读取。这里只帮助复杂 Taskbook 保持**决策完整但实现开放**，不重新定义 Goal，也不替 Executor 预编译 patch。

## Execution 保持判断粒度

Taskbook 不是 task list。一批对象如果都受同一个结果、判断和 binding constraint 支配，就只表达这一层，让 Executor 在真实 repo 中自行找全。只有局部要达到的结果、判断规则、真实依赖或 binding constraint 不同，才值得分开表达。

每一项只需要说明“完成后什么成立、什么判断控制这个范围、与其他结果有什么真实依赖”。如果几步可以换顺序、换文件、换 helper/class、换局部实现而不改变 Goal、风险或完成证明，就不要把这些步骤写进 Taskbook。`edit A → add B → update C → run D`、file/symbol/line、候选类名和当前 patch idea 默认都是 implementation intelligence，不是 execution contract。

一个具体细节只有在**删掉它会允许 Executor 做出一个仍符合高层文字、却违反 authority / boundary / risk / completion contract 的实现**时才值得保留。仅仅“已查到”“很可能要改”“能帮助 fresh Executor 更快开始”都不够；能从当前 repo/runtime 廉价可靠重算的导航信息留给 Executor。

通常不画执行图。只有关系本身会改变正确执行选择时才写，例如一个结果真实依赖另一个结果的 Evidence、两项会争用同一 authoritative surface、或几项必须一起满足一个 completion claim。不要把普通施工顺序升级成 dependency。

## 当前只能推进一部分时

**当前可安全推进的范围不能替换完整 Goal。**

如果 reality 只支持先推进一部分，就保留完整 Goal，只说明当前 material boundary 与为什么其他部分尚不能决定。执行中新的 Evidence 让后续工作变得真实时再处理；相邻 residue 也不能因为被发现就自动扩进 Goal。

一个分支 blocked，不应冻结与它无关的 material work；但 Northstar 不需要提前把所有可能分支切成未来任务。只保留已经会改变当前执行选择的依赖。

## 起点与 baseline

当前 workspace 中已经与 Goal 对齐的修改就是执行起点：不要求重做，也不能因为已有 diff 就缩小 Goal；“已经改了”本身也不是正确性 Evidence。

Starting reality 只保留会改变 Goal、binding boundary、material dependency 或 completion proof 的事实。具体代码锚点、文件清单和当前 inventory 如果 Executor 能从 authoritative repo 可靠重建，就不复制进 Taskbook；需要时直接引用现有 authority。

baseline 只有在它真的帮助区分“原来就坏”与“这次改坏”、或会改变 completion judgment 时才值得写。发现一个现成 command / target / parameter 不代表 Taskbook 应固定它；只有它本身是 authoritative acceptance interface、不可替代的风险反证，或缺少它会让 completion claim 失去明确含义时才固定。否则只写 verification obligation，让 Executor 选择真实证据路径。

如果后续判断依赖某个 baseline，Executor 在第一次依赖它之前重新取得；结果不一致时，只重算依赖这个前提的工作和 Evidence，其他仍有效部分继续复用。

## Verification 按 claim，不按施工项

Verification 不跟 Execution 一一配对。先写 Goal completion claim，再判断每个 claim 需要什么 authoritative Evidence；相同 Evidence 能覆盖多个范围就合并，一个范围涉及多个独立 claim 就分别验证。

验证粒度由**要证明的行为、边界、风险和 authority**决定，而不是由 commit、文件、task 或已发现测试数量决定。优先验证最终可观察行为和长期约束；局部 unit/build check 可以作为证据，但不能因为它贴近代码改动就自动代表 Goal 已完成。

Taskbook 固定“什么必须被证明”，不固定 Executor 的 debugging flow。Research 发现的 case 默认是 Evidence / risk example，不自动成为逐项 checklist；只有 authority 直接固定该 case，或它是不可替代的反证边界时，才保留具体 case/target。一个候选对象也不因为被发现就自动升级成 `0-hit / 0-count`；只有已经证明它必须消失，而且归零本身属于 Goal 时才这样验收。

如果存在具体“实现其实错了但仍可能显示 PASS”的风险，再读 [verification-trust.md](verification-trust.md)。否则不要增加额外判卷机制。

失败也要诚实：可信 baseline 从绿变红时先恢复或准确报告；同一路线反复失败且没有新 Evidence 时，换有依据的策略、先做独立工作或报告 blocker。禁止通过 skip/todo、放松断言、删活体测试、mock 掉目标、吞失败或 `|| true` 制造成功。

## 跨会话继续

较长 run 使用现有 `implement-notes` 记录 progress、关键 decision/Evidence、blocker 和 resume point。新 session 先读它，只重做前提已经变化或 Evidence 已失效的部分；不要另造第二份 Taskbook、持久 Graph 或 manager state。
