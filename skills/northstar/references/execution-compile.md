# 当简单 Taskbook 不够

只在 Goal 已定准，且复杂度本身会改变 Execution 或 Verification 判断时读取。这里只帮助 Northstar 编译复杂 handoff，不重新定义 Goal，也不替 Executor 设计 patch、调试流程或 scheduler。

## Execution

Taskbook 把复杂 Goal 编译到 fresh Executor 可以直接推进的 material 粒度：

- 不同 outcome、responsibility、binding boundary 或 real dependency 会改变执行判断时，分开表达对应 material work cut；
- 一个已由 Evidence 支持的 material cut 若省略只会迫使 Executor 重新发现，也保留；
- file/function/helper/caller、局部 edit 顺序、patch shape 和 local check 默认仍是 How。

Taskbook prose order 不形成 dependency。只有真实 prerequisite、共享 authoritative surface / 冲突、必须共同验收的结果等关系会改变 Executor 选择时才写；没有这种关系的 work 不被强制串行或并行，也不为了暴露并行度拆碎 cohesive work。

当前 reality 只能支持先做一部分时，保留完整 Goal，只缩当前 safe frontier。必须等 execution Evidence 才能知道的后续 work 等它变成真实问题后再加入；一个分支 blocked 不冻结与它无关的 work。

## Unknown 与 baseline

若一个未关闭事实决定 material work 是否成立、是否越过 binding boundary、或能否安全开始，Northstar 前置关闭或保持为显式 Unknown / dependency。若不同答案只会改变实现选择，留给 Executor。

baseline 只有在它真的承担 scope、coverage、attribution 或“原来就坏 / 这次改坏”的判断时才值得进入 Taskbook。具体 command / target / parameter 只有在 repo authority 已确认且省略会误导时才保留；Research 找到命令本身不是固定它的理由。Executor 第一次真正依赖 baseline 时按当前 reality 重新取得；mismatch 只使依赖它的 work / Evidence stale。

## Verification / Evidence

Verification 不与 implementation work 一一对应。先固定 completion claim，再判断需要什么 Evidence：

1. Evidence 先达到 claim 所需的置信度；
2. 满足该门槛的路径中，优先成本更低、对 claim 更直接的方式；
3. 已有 authoritative test/build/replay/integration/runtime Evidence 能直接证明 claim 时优先复用；
4. 新行为、稳定 regression risk 或现有 Evidence 覆盖不足时，再增加最小 focused test / check。

不要默认要求 failing-test-first，也不要因为 UT 贵就跳过真正需要的 regression Evidence。

当 current reality 已确认一组 test/build/replay/integration 路径直接覆盖关键 completion claim，而且只写抽象 obligation 容易让 fresh Executor 用便宜但不足的检查宣称完成时，Taskbook 保留它作为**当前 fallback verification path**。它是 proof backstop，不是 implementation plan 或永久 command checklist；implementation、binding 或 reality 使其失准时，Executor 必须从 repo authority 重推并取得等价或更强 Evidence。

一个 completion report / artifact 只有在最终 judgment 真正依赖它时才需要前置确认 producer、provenance、readiness、consumer、failure semantics 等 authority；如果它只是可替换 candidate verifier，不为了预选 verifier topology 扩大 Research。

执行结束后 Evidence 必须支持 Goal、binding constraints 和 completion claims，而不是活动说明、自报 PASS 或 task completion。存在具体“实现错了但仍可能 PASS”的风险时再读 [verification-trust.md](verification-trust.md)，只补能反证该风险的最小检查。

## Continuation

跨 session progress、resume state、retry 或调试 loop 属于 Executor / runtime，不进入 Northstar Taskbook protocol。新的 Evidence 推翻 premise 时只重算它的 dependency cone；仍有效的 Goal、work 和 Evidence 继续复用。
