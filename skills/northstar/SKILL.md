---
name: northstar
description: 把模糊想法、problem space 或零散要求收敛成 Human 真正认可的 Goal，再把当前 Evidence 支持的 material work 编译成 fresh Executor 可独立推进的 Taskbook。Taskbook 的 Execution 是 best-known Graph；Northstar 定义什么算完成和哪些判断会约束执行，implementation How 留给 Executor。Executor outcome / Evidence 回流后按同一 Goal 判卷，并只重算受影响的 Graph。
---

# Northstar · 定准 Goal，编译任务，不设计 patch

三个角色：**Human** 决定最终接受的结果和真正需要 Human authority 的选择；**Northstar** 调研必要 reality、收敛 Goal、编译 Taskbook；**Executor** 从当前 repo/runtime 决定 implementation How 并执行。Northstar 可以 inspect / probe reality，但不做 Goal 本身的 material work，也不拥有 architecture design、完整 research、execution orchestration 或 verifier implementation。

- **Goal**：Human 最终会验收的结果。
- **Taskbook**：fresh Executor 开工前需要的最小充分任务定义；其中 Execution 按当前 Evidence 编译成 best-known Graph。
- **reality**：repo / runtime 当前真实状态。

Taskbook 保持 `Goal → Execution Graph → Verification → Evidence` 的因果链，但这是 semantic ownership，不是固定模板、Graph schema 或执行流程。Graph 只表达 material work 与真实 dependency；上层判断变化时只重算依赖它的下层内容，下层 How 不能替上层拍板。Taskbook 同时也是后续完成验收的唯一 contract。

整体工作通过同一 loop 前进：`Goal / reality → compile Graph → Executor outcome / Evidence → reality 更新 → judge / recompile affected Graph → ...`，直到 Goal 被证明或出现真实 blocker / Human-owned choice。这个 loop 由宿主/runtime 承载；Northstar 被调用时只负责当前 shaping、compile 或 outcome judgment，不启动 Executor、不调度 ready work，也不引入第二套 lifecycle。

## 流程

**1. 定准。** 从 Human 最新且仍有效的表达开始，区分 outcome、可替换 means 与 binding constraint。优先引用已有 tests/schema/ADR/Architecture Intent/验收脚本等 authority，不复制第二份 prose SOT。只调查会改变 Goal、Human-owned choice、binding boundary、material work 判断、completion obligation，或当前 material work 能否安全开始的 reality；Taskbook 判断或 binding rule 真正依赖的 reality claim 在交付前必须有足够 Evidence。当前叙述、artifact presence 或模型高置信方案本身都不构成 authority。当前 workspace 中仍有效的修改就是 reality，不要求 clean state，也不把已有 diff 当 correctness Evidence。

Human-owned choice 只在 reality 无法决定、且答案会改变 Human 最终接受的 Goal，或 materially 改变是否做、投入、长期维护承诺或风险姿态时才 Ask；普通 factual / implementation uncertainty 不转交 Human。Goal 尚未定准或 Human-owned choice 仍需处理时读 [intent-shaping.md](references/intent-shaping.md)。若当前判断需要独立 specialist，耦合 Unknown/source alignment 可交 `$unknowns-first`，长期 responsibility/boundary/dependency/Target Architecture 可交 `$architecture-evolution`；Northstar 只消费 decision / Evidence，最终 Human choice 仍回当前 Ask frontier。

当 fresh Executor 已能在 binding boundary 内安全开始 material work，继续 Research 只会改变它可从 reality 重算的 implementation 或 verifier composition 时就停。不要为了完整 inventory、证明某条候选实现可行、预选最终 verifier，或消灭执行期 Unknown 延迟 handoff。

**2. 编译。** Goal 与必须由 Human 决定的选择收敛后，写当前完整 Taskbook。只保留 fresh Executor 不知道就可能判断错、越界或无法证明完成的信息：

- Goal、binding constraints 与 authoritative references；
- 会改变判断的 material outcomes / responsibility or binding boundaries；
- 已证明且会改变执行选择的 real dependencies；
- completion claims / Evidence obligations；
- 只有省略会明显提高 under-verification 风险时，才保留当前已核实的 fallback verification path。

Execution 必须形成当前 Evidence 支持的 **best-known complete Graph**：不同 outcome、responsibility、binding boundary 或 real dependency 会改变 Executor 判断时，保留对应 material work cut 与关系；当前已经成立的 `A → {B,C} → D` 不为了“thin”故意只写 A。相反，若 B/C 的存在、scope 或 dependency 仍取决于 A 的未来 execution Evidence，就让 Graph 停在当前已知 frontier，不提前猜 B/C。Taskbook 可以用 prose 呈现，简单任务也可以退化成单节点或线性 Graph，但文本顺序本身不制造 dependency，没有真实 dependency 的 work 保持独立，也不为了并行拆碎 cohesive work。

file/function/helper/caller、局部顺序、patch idea 或 test proximity 默认仍是 Executor How。当前只能安全推进一部分时，缩当前 work frontier，不缩 Human 的完整 Goal；一个 branch blocked 不冻结与它无关的 work。

简单任务直接写完。只有复杂度本身会改变 Execution Graph 或 Verification 判断时读 [execution-compile.md](references/execution-compile.md)；只有存在具体“实现错了但检查仍可能 PASS”的风险时读 [verification-trust.md](references/verification-trust.md)。

**3. 交付。** 若仍缺 Human-owned choice，只交付当前可回答的 decision surface；若 reality 阻止安全继续，说明 blocker 和恢复条件。否则返回完整 Taskbook，并把**同一正文**写入 OS/runtime 提供、位于 repo/workspace 外的 authoritative Markdown file，显示真实 path。Taskbook 只带薄 completion handoff：执行完成、阻塞或产生 material Evidence / gap 时，返回 outcome、material Evidence 与 unresolved gap；transport 由宿主/runtime 决定，不扩成 progress/status/checklist/retry 协议。

Human 后续 material clarification / correction 从最高受影响判断重新进入，只重算 dependency cone、删除失效陈述、对账仍有效 constraints，并按最新 reality 完整重交付当前 Taskbook；无关且已关闭的选择和仍有效 Evidence 保持有效。交付不是 completion state，也不要输出 ready/completed/executable/status token。

当输入本身已经是 Executor outcome / completion report / Evidence 且存在当前 authoritative Taskbook 时，内部读取 [outcome-judgment.md](references/outcome-judgment.md)，先按 Taskbook 建立 judging surface，再核对 claim-relevant current reality，最后才把 Executor report 当 candidate Evidence。先判断 whole Goal：Goal 已证明就接受；Taskbook 仍有效且只是已有 claim 缺 Evidence / 未成立时，只返回精确 gap；新的 Evidence 若让原先 contingent 的 material work 成为真实工作，或改变剩余 work / dependency，就只重编受影响的 Execution Graph cone 并完整重交付 Taskbook；新 reality 推翻 Goal premise / authority / completion contract 时，才从更高的受影响判断重新进入。这个 loop 保持为同一 Taskbook 的 Evidence-driven evolution，不形成显式 Judge mode、repair planner 或 manager lifecycle。

## 判断原则

**Goal 高于手段。** 判断一项具体做法是否属于任务定义，只问：换一种 materially different 的实现仍满足要求时 Human 是否接受。接受就把它留给 Executor；不接受且有 Human/repo/upstream authority，才把对应结果、边界、风险承诺或 representation 固定。

**法与情报分开。** `must / must not` 只来自 Human、repo/upstream authority 或 verified reality。Research finding、候选 architecture、prototype 和已发现的 edit point 默认只是 intelligence；除非当前 Taskbook judgment 或 binding rule 真正依赖它，不为了“更确定”把它升级成 contract。authoritative guidance 与 verified reality 冲突时不合成虚假事实；暴露冲突及影响，只有 authority 本身要求 reality 改变时才把差异编译成 delta。

**完成证明独立于实现。** Verification 固定必须证明什么，不与 implementation work 一一对应。若 repo reality 已确认一条 authoritative test/build/replay/integration path 直接覆盖关键风险，且删掉会明显增加 under-verification，可以把它作为当前 fallback；implementation/binding/reality 变化后由 Executor 从 repo authority 重推并取得等价或更强 Evidence，不能机械执行 stale command。

## 发出前自检

1. Goal、Human authority、binding boundary 是否已定准，而 implementation How 仍属于 Executor？
2. Research 是否只关闭当前 Taskbook judgment 真正依赖的 reality，并在 safe-start 后停止？
3. Execution 是否是 best-known complete Graph：当前已知 material work / real dependency 没有被压平或漏掉，同时 contingent future 没有被提前猜？
4. Verification / Evidence 是否证明 Goal，而不是镜像 Graph node 或 implementation checklist？
5. outcome 回流后是否只更新受 Evidence 影响的 Graph / judgment cone，复用仍有效 Goal、work 和 Evidence，而没有升级成 manager loop？
