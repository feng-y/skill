# 当简单 Taskbook 不够

只在 Goal 已经定准，且复杂度本身会改变执行或 Verification 判断时读取，例如存在不同 outcome / boundary、真实依赖、执行 Evidence 才能显现的后续工作、验证成本 / Evidence 选择会改变完成证明，或跨会话 continuation。这里只处理这些差异怎样进入 Taskbook，不重新定义 Goal，也不替 Executor 预编译逐文件、逐函数的 implementation plan。

## Execution 写到什么粒度

Taskbook 仍要把复杂 Goal 编译到 fresh Executor 可以直接推进的粒度。只有不同 outcome / responsibility、binding boundary 或真实依赖会改变执行判断时，才分开形成 work；如果不分开会迫使 fresh Executor 重新发现一个已经有充分 Evidence 的 material cut，也应保留这个 cut。反过来，文件、函数、helper、调用顺序和局部检查仍由 Executor 从当前 repo 决定；不要为了“更可执行”把这些 How 展开成 predicted-patch checklist。

Research 已经发现具体 edit point、helper、caller 或 test，不会自动提高它们的 authority。除非 representation 本身被 Human / repo authority 固定，或遗漏该细节会让 fresh Executor 判断错、越界或无法证明完成，否则不写进 Taskbook。

若一个尚未关闭的事实决定某项 material work 是否安全，把它保留为 Unknown / dependency，并说明它会改变什么；不要把“先查 X、再改 Y”展开成执行步骤。

## 当前只能做一部分时

**当前可安全推进的范围不能替换完整 Goal。**

如果 reality 只支持先做一部分，就保留完整 Goal，并只标出当前已证明的安全 frontier。执行中新的 Evidence 让后续工作变得可判断时，再更新受影响部分；相邻 residue 也不能因为被发现就自动扩进 Goal。

通常不需要执行图。只有关系会改变 Executor 选择时才写，例如真实 prerequisite、可独立并行的 work、并行冲突、共享 authoritative surface 或必须共同验收的结果。只写当前 reality 已经证明的关系；必须等执行后才知道的后续工作，等 Evidence 使它成为真实问题后再加入。一个分支 blocked，不应冻结与它无关的工作。

## 起点与 baseline

当前 workspace 中已经与 Goal 对齐的修改就是执行起点：不要求重做，也不能因为已有 diff 就缩小 Goal；“已经改了”本身也不是正确性 Evidence。

baseline 只有在它真的改变后续判断，或区分“原来就坏”与“这次改坏”时才值得写。具体 command / target / parameter 若已由 reality Evidence 证明存在、语义正确，并且它直接覆盖 completion claim 或关键风险、删掉会明显提高 under-verification 风险，可以作为**当前 fallback verification path** 写入 Taskbook；它不是永久 authority，也不把对应实现方式固定下来。

如果后续判断依赖某个 baseline，Executor 在第一次真正依赖它时重新取得；结果不一致时，只重算依赖这个前提的工作和 Evidence，其他仍有效部分继续复用。

## Verification 与最终判卷

Verification 不跟 implementation work 一一配对。先列 completion claim，再判断每个 claim 需要什么 authoritative Evidence；相同 Evidence 能覆盖多个改动就合并，一个改动涉及多个独立 claim 就分别验证。

先要求 Evidence 对 completion claim 提供足够置信度；在满足这个条件的验证方式中，优先选择成本更低、对 claim 更直接的路径，而不默认要求先构造失败测试再实现。已有 authoritative test / build / replay / integration / runtime Evidence 能直接证明 claim 时优先复用；新行为、稳定 regression risk 或现有 Evidence 无法可靠覆盖的 claim，再增加最小 focused test / check。为复杂 legacy / infrastructure 边界强造大量 mock、fixture 或高成本 UT，但它们只重复实现细节而没有增加 material confidence，不是默认义务。

当 current reality 已确认一组 test / build / replay / integration 路径能直接覆盖关键 completion claim，而且只写抽象 obligation 容易让 fresh Executor 用更便宜但不足的检查宣称完成时，Taskbook 应保留这组**当前 fallback verification path**。这是 verification 兜底，不是 implementation plan：Executor 仍负责具体 verifier composition；若 implementation、binding 或 reality 改变使当前 path 不再准确，必须从 repo authority 重新推导并取得等价或更强 Evidence，不能机械执行 stale command，也不能因为路径变化而少验证。

验证粒度由**要证明的行为、边界、风险和 authority**决定，而不是 commit、文件、task 或局部测试数量。优先最终可观察行为和长期约束；unit/build check 可以贡献 Evidence，但不能因为它靠近改动就自动代表 Goal 已完成。

执行结束时重新用 Goal、binding constraint、completion claim 和当前 Evidence 判卷。patch 已落、任务已做或 tests 全绿都不能替代这个判断；Evidence 只覆盖局部实现时，就保留 material gap，而不是把局部 PASS 升成 Goal completion。

Taskbook 只冻结“Goal 完成必须证明什么”，不规定 Executor 怎样定位问题。Research 中发现一个候选对象，不等于它必须 `0-hit / 0-count`；只有已经证明它必须消失，而且归零本身就是 Goal 的一部分时，才这样验收。

如果存在具体“实现其实错了但仍可能显示 PASS”的风险，再读 [verification-trust.md](verification-trust.md)。否则不要增加额外判卷机制。禁止通过 skip/todo、放松断言、删活体测试、mock 掉目标、吞失败或 `|| true` 制造成功。

## 跨会话继续

跨会话 progress 机制属于 Executor / runtime，不进入 Taskbook 协议。继续时仍以同一 Taskbook、当前 reality 和仍有效 Evidence 为准，只重做前提变化或 Evidence 失效的部分；不要为 Northstar 另造持久 Graph、manager state 或第二份 Taskbook。
