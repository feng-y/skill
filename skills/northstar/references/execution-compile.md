# 当简单任务书不够

只在 Goal 已经定准，但任务较长、需要多个不同判断、真实依赖、较强验证或跨会话继续执行时读取。

这里仍然只服务一个问题：

> **什么信息如果不写，fresh Executor 会做错选择，或无法证明完成？**

## 写判断，不写调研

能从 repo/runtime 可靠重算的事实默认不写；不写会让 Executor 误删、误留、越界或漏验证的非显然事实才写。更多 Research 应压成更少、更稳定的判断，而不是更多 instruction。

当前 workspace 中已经与 Goal 对齐的修改就是执行起点：不要求重做，也不能因为已有 diff 就缩小 Goal；“已经改了”本身也不是正确性证据。

baseline 只有在它真的帮助判断覆盖是否完整，或区分“原来就坏”与“这次改坏”时才值得进任务书。命令、target、参数必须来自真实环境，不能编造。

## 只在判断不同的地方拆工作

一批实例如果都能用同一个判断处理，就保持一个 work unit，让 Executor 自己扫完整 surface；不要按文件、函数或当前已发现的实例拆成 checklist。只有 outcome、判断、真实依赖或验证要求不同，才值得拆开。

如果缺一个事实就连第一项安全 material work 都不能开始，把关闭这个事实放在最前面；不要因此开启第二轮大 Research。

通常不需要 Graph。只有关系本身会改变执行选择时才写，例如：B 必须消费 A 的结果、两项可安全并行、多个工作会写同一 authoritative surface、或者组合结果必须一起验证。只写当前 Evidence 已经证明的关系；真正要等未来 Evidence 才知道的后续工作，等它变成现实时再加入。一个分支 blocked 不应冻结与它无关的工作。

## 写清怎么证明，而不是怎么调试

Verification 只冻结“完成必须证明什么”。具体 build/test/replay 的执行顺序、每改一步就测一次等 failure-localization 技巧默认交给 Executor。

如果一个 baseline 被任务书当作后续判断前提，Executor 在第一次依赖它之前重新取得；不匹配时，只让依赖这个前提的工作和 Evidence 失效，其他仍有效部分继续复用。

不要把 Research 中发现的候选对象自动升级成 `0-hit / 0-count` 验收；只有它已经被证明必须消失，而且归零本身就是完成条件时才这样写。

如果存在具体“实现其实错了但仍可能显示 PASS”的风险，再读 [verification-trust.md](verification-trust.md)。否则不要增加额外判卷机制。

失败路径也要诚实：可信 baseline 从绿变红时先恢复或准确报告；同一路线反复失败且没有新增 Evidence 时换有依据的策略、切换独立工作或报告 blocker。禁止通过 skip/todo、放松断言、删活体测试、mock 掉目标、吞失败或 `|| true` 制造成功。

## 让长任务能继续

较长 autonomous run 使用现有 `implement-notes` 记录 progress、关键 decision/Evidence、blocker 和 resume point。新 session 先从这里恢复，只重做前提已经变化或 Evidence 已失效的部分；不要另造第二本 Taskbook、持久 Graph 或 manager state。
