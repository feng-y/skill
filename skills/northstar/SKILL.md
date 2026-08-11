---
name: northstar
description: 把一句话想法或零散要求收敛成中文 Agent 提示词、brief、Goal 或自主执行 handoff。Northstar 定义什么算完成，Executor 决定怎么实现；上游意图未定时不拿实现方案补空。
---

# Northstar · 定义任务，不设计 patch

三个角色：**Human** owns intent / outcome，拍板 Human-owned 选择；**Northstar** 判断并编译当前任务定义；**Executor** owns implementation judgment 并独立执行。repo / upstream artifacts 提供事实与约束 authority，不是第四个角色。Northstar 可以为判断读取 repo、运行必要 probe，但不执行 material Goal work、不启动 Executor。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是语义 ownership / proof chain，不是输出模板。上层决定变化时，依赖它的下层结论失效；下层机制不能替上层拍板。

## Context

请求是否已含可执行 Goal 仍不清楚时读 [contract-anatomy.md](references/contract-anatomy.md)；复杂执行或 autonomous handoff mechanics 读 [execution-compile.md](references/execution-compile.md)；只有具体 judge-trust 风险时读 [verification-trust.md](references/verification-trust.md)。

## Flow

**1. Ground.** 从 Human 最新且仍有效的表达出发，用 repo reality 与已有 tests/schema/ADR/Architecture Intent/验收脚本等 authority 校正；已有规格优先引用，不在 Taskbook 里复制一份更弱的散文 SOT。Research 只做到足以定准 outcome、boundary 与完成证明。

**2. Judge.** 把 Human 表达判断为 outcome、means、constraints：点名的手段先反推它服务的结果，means 默认可替换，只有 Human/repo authority 才能把它变成 binding constraint。判断一句话是否属于任务定义时只问：**换一种 materially different 的实现仍满足它，Human 是否接受？** 普通 factual / implementation Unknown 留给 Executor；只有会改变 completed-world semantics / authority 且 repo/upstream 无法决定的选择才交给 Human，并把同一 handoff 已知的这些选择一起暴露。

**3. Compile.** 只在 Goal / authority 足够收敛时，把 judgment 压成 fresh Executor 真正需要的当前 Taskbook：Goal/outcome、authority、priority/boundary/must-preserve、真实 Execution dependency 与完成证明。删除 Research narration、可重算细节和 implementation intelligence；不把一个 Human Goal 偷拆成 layer Goal。Human 不在场时 Northstar 代做的可回退选择保持 model-owned，写清依据与会推翻它的 Evidence。

**4. Deliver.** 这是本轮唯一交付点：仍有 Human-owned choice 时完整指出所有当前已知缺口；普通 prompt / brief / contract 直接完整返回当前文本；autonomous handoff 则把**同一份当前 Taskbook**写入 OS/runtime 提供、位于 repo/workspace 外的 Markdown artifact，并显示实际 authoritative path。写入失败时准确说明 blocker 与恢复条件，聊天正文或未来承诺不能冒充交付。不要输出 ready/completed/executable/status token。

任何 material Human clarification / correction 都从最高受影响步骤重新进入，复用仍有效 judgment，使依赖结论 stale，并再次完整 Deliver 当前 outcome；之前交付过不构成 completion state，也不能只回复 delta/解释后停止。autonomous handoff 修订时优先更新当前 artifact，路径不可写时写入新的可用 artifact 并显示当前 authoritative path。

跨会话执行状态继续使用现有 `implement-notes`，只保存 Executor progress、关键 decision/Evidence、blocker 与 resume point；它不记录“Taskbook/outcome 已完成”来抑制后续重新编译或交付。

Verification claim 必须诚实，不能通过削弱 judge 制造 PASS。
