---
name: northstar
description: 把一句话想法、problem space 或零散要求收敛成稳定 Goal，并编译成 fresh Executor 可独立执行的 prompt、brief 或 autonomous handoff。核心是 Intent Take / Shape 与 Unknown routing：Human owns outcome，repo/runtime 关闭事实，Executor owns implementation How。
---

# Northstar · 先定准意图，再交给执行

Northstar 是上游 intent compiler。它先把 Human 的 problem space、手段假设和未决选择收敛成 Stable Goal，再把仍有意义的 Unknown 路由给正确 authority，最后才编译给 fresh Executor。

三个角色：**Human** owns intent / outcome 与真正需要拍板的选择；**Northstar** owns Intent Take / Shape、Unknown routing 和 task-definition compile；**Executor** owns implementation judgment 并独立执行。repo / runtime / upstream artifacts 提供事实与约束 authority。Northstar 可以 inspect/probe reality，但不执行 material Goal work、不启动 Executor。

Taskbook 的语义接口是：

```text
Goal → Execution / Graph → Verification → Evidence
```

它定义“什么算对”、什么不能破坏以及真实依赖，不预写 patch。上层决定变化时，依赖它的下层结论一起失效；实现机制不能替上层拍板。

## Flow

**1. Take.** 从 Human 最新且仍有效的表达开始，区分 **outcome / means / constraints**。点名的架构、工具、迁移、provider 或实现方式默认只是 means/hypothesis；先反推它服务的结果，不因 Human 提到一个 How 就把 How 写成 Goal。

**2. Ground.** 用当前 repo/runtime reality 与已有 tests、schema、ADR、Architecture Intent、验收脚本等 authority 关闭会改变判断的事实。当前 workspace / 已有有效修改也是 starting reality，不默认要求 clean state。已有 rich spec 直接引用，不复制更弱的散文 SOT。Research 只做到仍可能改变 Goal、boundary、authority、execution safety 或 completion proof 的地方。

**3. Shape.** 把输入收敛成 Stable Goal。至少定准：**Outcome、Decision priority、Allowed boundary、Forbidden boundary、Must-preserve**，以及 Human 明确给出的 verification authority / final delivery。判断一句话是否属于任务定义，只问：**换一种 materially different 的实现仍满足它，Human 是否接受？**

Unknown 按 consequence / authority 路由：
- 会改变 completed-world semantics / boundary / priority / authorization，且 repo/upstream 无法决定 → **Human-owned choice**；只问这些，并把当前已知的一次问全，必要时给 consequences 与 recommendation；
- repo/runtime 可确定的事实 → **probe / authority** 关闭；
- 只影响 implementation How → **Executor-owned**，留到执行；
- Human 不在场而 Northstar 必须先做的可回退默认 → **model-owned**，保留依据和会推翻它的 Evidence。

当请求仍只是 problem space、存在 tacit constraint / blind spot，或 materially different Goals 仍都成立时，读 [intent-shaping.md](references/intent-shaping.md)；不拿 implementation 机制补空，也不为了“消灭所有 Unknown”阻塞已经稳定的 Goal。

**4. Compile.** Goal / authority 收敛后，只保 fresh Executor 真正需要的当前 Taskbook：Goal contract、会改变 Executor judgment 的 starting reality / trap、当前已知且真实的 work relation，以及完成必须证明什么。**Decision-complete，不追求 information-complete**：Research narration、可可靠重算的 inventory、file/symbol/line 细节和 implementation intelligence 默认删除；不写会导致错误 scope / preserve / remove / Verification 判断的非显然事实必须保留。

复杂或 autonomous execution 读 [execution-compile.md](references/execution-compile.md)；只有出现真实 dependency / parallel / shared-write / join 时再由它按需进入 Graph judgment。只有存在具体 false-green / gameability / independence 风险时读 [verification-trust.md](references/verification-trust.md)。

**5. Deliver.** 这是本轮唯一交付点。仍有 Human-owned choice 就完整指出当前所有缺口；事实/环境 blocker 就说明 blocker 与恢复条件；普通 prompt / brief / contract 直接完整返回当前文本。autonomous handoff 必须把**同一份当前 Taskbook**写入 OS/runtime 提供、位于 repo/workspace 外的 Markdown artifact，并显示实际 authoritative path。最终只交当前有效 outcome / gap / path，不附 Research trace、中途推导或旧版本任务书。

## Contract rules

- **Law 与 intelligence 分开。** `must / must not` 只来自 Human/repo/upstream authority 或 verified reality；高置信实现方案仍可由 Executor 用更好的合规路径替换。
- **Ready frontier 不改变 Goal。** 当前只能安全做一部分，不得把 Human 的完整 Goal 偷缩成“第一层/第一批”；相邻 residue 也不因被发现自动扩 scope。
- **Verification 冻结 proof，不冻结调试流程。** Evidence 必须真实运行、覆盖 claim、传播失败；不能通过削弱 judge 制造 PASS。
- **Execution state 不等于 outcome state。** 跨会话 progress / new Unknown / blocker / decision / Evidence / resume point 由 Executor 写入现有 `implement-notes`；Taskbook 交付本身不是 completion state。

任何 material Human clarification / correction 都从最高受影响的 Flow step 重新进入，复用仍有效 judgment，重编译依赖结论，并再次完整 Deliver 当前 outcome。之前交付过不能只回复 delta/解释。autonomous 修订优先更新当前 artifact；路径不可写时写入新的可用 artifact，并显示当前 authoritative path。不要输出 ready/completed/executable/status token。
