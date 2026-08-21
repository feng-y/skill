# 当简单 Taskbook 不够

只在 Goal 已定准，且复杂度本身会改变 Execution 的 Graph 结构或 Verification 判断时读取。这里只帮助 Northstar 编译复杂 handoff，不重新定义 Goal，也不替 Executor 设计 patch、调试流程或 scheduler。

## Execution

复杂 Goal 的 Execution 按 fresh Executor 可以直接推进的 **best-known complete Graph** 编译：

- 不同 outcome、responsibility、binding boundary 或 real dependency 会改变执行判断时，分开表达对应 material work cut；
- 一个已由 Evidence 支持、且省略只会迫使 Executor 重新发现的 material cut / relation 应保留；
- 只有真实 prerequisite、共享 authoritative surface / conflict、或必须共同成立的 outcome 等关系真正改变 Executor 选择时，才表达 dependency；
- file/function/helper/caller、局部 edit 顺序、patch shape 和 local check 默认仍是 How。

Graph 的完整度跟随当前 **decision-relevant knowledge**：当前 Evidence 已能确定 `A → {B,C} → D` 时就一次表达，不为了 lazy / thin 故意只给 A；只有 B/C/D 的存在、scope 或 dependency 仍取决于 A 的未来 execution Evidence 时，才停在当前 frontier，等 Evidence 让后续 work 成为 reality 后再扩展。**best-known complete 不等于 research-complete**：不能为了补齐 Graph 扩大 inventory、验证候选 implementation、扫描只会改变 How 的 territory，或为未形成的未来工作创造占位 node、phase、taxonomy。

Taskbook prose order 不形成 dependency。没有真实 dependency 的 work 保持独立，不被强制串行或并行；一个 branch blocked 不冻结与它无关的 work；也不为了暴露并行度拆碎 cohesive work。简单/线性任务只是 Graph 的退化形式，不要求 diagram、Graph schema 或显式 node object。

## Unknown 与 baseline

若一个未关闭事实决定 material work 是否成立、是否越过 binding boundary、或能否安全开始，Northstar 前置关闭或保持为显式 Unknown / dependency。若不同答案只会改变实现选择，留给 Executor。

baseline 只有在它真的承担 scope、coverage、attribution 或“原来就坏 / 这次改坏”的判断时才值得进入 Taskbook。具体 command / target / parameter 只有在 repo authority 已确认且省略会误导时才保留；Research 找到命令本身不是固定它的理由。Executor 第一次真正依赖 baseline 时按当前 reality 重新取得；mismatch 只使依赖它的 work / Evidence stale。

## Verification / Evidence

Verification 不与 implementation work 或 Graph node 一一对应。先固定 completion claim，再判断需要什么 Evidence：

1. Evidence 先达到 claim 所需的置信度；
2. 满足该门槛的路径中，优先成本更低、对 claim 更直接的方式；
3. 已有 authoritative test/build/replay/integration/runtime Evidence 能直接证明 claim 时优先复用；
4. 新行为、稳定 regression risk 或现有 Evidence 覆盖不足时，再增加最小 focused test / check。

不要默认要求 failing-test-first，也不要因为 UT 贵就跳过真正需要的 regression Evidence。

当 current reality 已确认一组 test/build/replay/integration 路径直接覆盖关键 completion claim，而且只写抽象 obligation 容易让 fresh Executor 用便宜但不足的检查宣称完成时，Taskbook 保留它作为**当前 fallback verification path**。它是 proof backstop，不是 implementation plan 或永久 command checklist；implementation、binding 或 reality 使其失准时，Executor 必须从 repo authority 重推并取得等价或更强 Evidence。

一个 completion report / artifact 只有在最终 judgment 真正依赖它时才需要前置确认 producer、provenance、readiness、consumer、failure semantics 等 authority；如果它只是可替换 candidate verifier，不为了预选 verifier topology 扩大 Research。

执行结束后 Evidence 必须支持 Goal、binding constraints 和 completion claims，而不是活动说明、自报 PASS 或 task completion。存在具体“实现错了但仍可能 PASS”的风险时再读 [verification-trust.md](verification-trust.md)，只补能反证该风险的最小检查。

## Loop

Northstar 不拥有跨 session progress、retry、debugging 或 runtime scheduler，但 Taskbook 必须能在宿主执行 loop 中稳定演进：`Graph → Executor outcome / Evidence → Taskbook + current reality judgment → verified Evidence / new reality → affected Graph`。

Executor report、task checklist、test output 在核实前只提供 candidate Evidence / navigation，不能直接改变 reality 或 Graph。只有独立 judgment 核实的新 Evidence / reality 才重算真正受影响的 dependency cone：它让 contingent work 成为真实工作时扩展 Graph；证明某个 branch / dependency 不存在时删除；改变 scope、binding 或 material relation 时拆分、合并或重排剩余 work；影响 completion claim / coverage 时同步重算对应 Verification。无关 branch、仍有效 work 和 Evidence 保持有效，已完成 work 也不因 Graph 改写机械重开，除非它的 Evidence 前提或所证明行为已被影响。

Graph 是 Taskbook 中 Execution 的结构，不是额外 runtime object。不要新增 persistent Graph state、node taxonomy、scheduler、manager protocol 或第二本 taskbook；宿主已有 progress/state 就复用，没有也不要求 Northstar 发明一套。
