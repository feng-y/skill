# 当简单 Taskbook 不够

只在 Goal 已经定准，但任务很长、需要几种不同判断、明确先后关系、较强验收或跨会话继续时读取。这里只处理复杂 Taskbook 怎样保持可执行，不重新定义 Goal 或 Human / Executor 的责任。

## 开发工作怎么拆

一批对象如果都能用同一个结果和判断处理，就作为一项工作，让 Executor 在约定范围内扫全；不要按文件、函数或当前发现的实例拆。只有局部要达到的结果、判断规则、真实依赖或 binding constraint 不同，才值得拆开。

每项工作描述“完成后什么成立、按什么判断、与其他工作的真实关系”，不是 predicted patch。不要把 `edit file A → add helper B → update caller C → run test D` 当作默认任务粒度。

如果缺一个事实就连第一项安全 material work 都不能开始，把这个事实放在最前面查清；不要因此再开一轮大 Research。

## 当前只能做一部分时

**当前可安全推进的范围不能替换完整 Goal。**

如果 reality 只支持先做一部分，就只推进这一部分；Human 的完整 Goal 仍保留。执行中新的 Evidence 让后续工作变得可判断时，再把它加入当前工作；相邻 residue 也不能因为被发现就自动扩进 Goal。

通常不需要画执行图。只有关系会改变下一步选择时才写，例如：B 必须等 A 的结果、两项可以并行、几项会改同一个 authoritative surface、或者几项必须合起来验收。只写当前 reality 已经证明的关系；必须等执行后才知道的后续工作，等它真的出现再加入。一个分支 blocked，不应冻结与它无关的工作。

## 起点与 baseline

当前 workspace 中已经与 Goal 对齐的修改就是执行起点：不要求重做，也不能因为已有 diff 就缩小 Goal；“已经改了”本身也不是正确性 Evidence。

baseline 只有在它真的帮助判断有没有漏项，或区分“原来就坏”与“这次改坏”时才值得写。具体 command / target / parameter 是否能被 Taskbook 固定，遵守主 Skill 的 Verification evidence 规则；没有 reality Evidence 证明其存在且语义正确，就只保留 verification obligation，不编造命令。

如果 Taskbook 把某个 baseline 当作后续判断前提，Executor 在第一次依赖它之前重新取得；结果不一致时，只重算依赖这个前提的工作和 Evidence，其他仍有效部分继续复用。

## Verification 怎么拆

Verification 不跟开发工作一一配对。先列 completion claim，再判断每个 claim 需要什么 authoritative Evidence；相同 Evidence 能覆盖多个开发工作就合并，一个开发工作涉及多个独立 claim 就分别验证。

验证粒度由**要证明的行为、边界、风险和 authority**决定，而不是由 commit、文件或 task 数量决定。优先验证最终可观察行为和长期约束；局部 unit/build check 可以作为证据，但不能因为它贴近开发步骤就自动代表 Goal 已完成。

Taskbook 只冻结“Goal 完成必须证明什么”，不规定 Executor 怎样定位问题。Research 中发现一个候选对象，不等于它必须 `0-hit / 0-count`；只有已经证明它必须消失，而且归零本身就是 Goal 的一部分时，才这样验收。

如果存在具体“实现其实错了但仍可能显示 PASS”的风险，再读 [verification-trust.md](verification-trust.md)。否则不要增加额外判卷机制。

失败也要诚实：可信 baseline 从绿变红时先恢复或准确报告；同一路线反复失败且没有新 Evidence 时，换有依据的策略、先做独立工作或报告 blocker。禁止通过 skip/todo、放松断言、删活体测试、mock 掉目标、吞失败或 `|| true` 制造成功。

## 跨会话继续

较长 run 使用现有 `implement-notes` 记录 progress、关键 decision/Evidence、blocker 和 resume point。新 session 先读它，只重做前提已经变化或 Evidence 已失效的部分；不要另造第二份 Taskbook、持久 Graph 或 manager state。
