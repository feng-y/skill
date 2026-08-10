# 可重入 Review：用原 Taskbook 独立判卷

仅在 Human 明确要求“review / 验收 / 判卷”一份**已经存在的 authoritative Taskbook** 时使用。它是一次新的 Northstar invocation，不是 Compile 的延长，也不新增 Acceptance layer、manager 生命周期或常驻 session。

## Authority

Review 只依赖可重建输入，不依赖旧 conversation 继续活着：

1. **authoritative Taskbook**：原 Goal、decision priority、allowed/forbidden boundary、must-preserve、required Verification、Evidence 要求、Completion Hook，以及 Compile 选定的 durable execution-state carrier；
2. **current repo/workspace reality**：当前 revision、diff、binding/config、可运行 provider；
3. **durable execution state**：Taskbook 指向的唯一 carrier，以及 Executor 留下的原始/稳定 Evidence artifact；若旧 Taskbook 未声明 carrier，则先按 Human/repo authority / existing repo convention / runtime existing carrier / `implement-notes` fallback 的顺序解析一处，不新造第二套；
4. 旧 session memory 只能帮助定位，不能替代上述 SOT。

如果 Human 在 Taskbook 之后明确改了 Goal / boundary / Verification / priority / authorization，不要静默拼出一个新合同；准确指出原 Taskbook 已被 supersede，需要重新 Compile 后再 Review。

## Review judgment

- 先读 Taskbook，不从 conversation 重建任务；
- 只按 **Goal / constraints + triggered required Verification + current valid Evidence** 应用原 Completion Hook；
- Executor narration、`PASS` 自报、durable carrier 中的结论都不是天然 Evidence；
- 能访问 authoritative environment 时，对最终结论关键且成本合理的 Evidence 直接重新取得；无法访问时要求可复核 provenance / artifact，而不是猜；
- premise 变化只让受影响 Evidence stale，不机械推翻无关 Evidence；
- judge 被 skip/todo、放松断言、删活体测试、mock 被测对象、改阈值、吞失败、`|| true` 等削弱后产生的绿灯无效；
- **Review 只判卷，不实现/修复**：不修改目标 workspace、不替 Executor 补 patch、不重写 Taskbook、不启动 Executor。发现失败只输出最小、可执行的 gap，让后续 Executor invocation 继续。

## Verdict

- **`Verdict: PASS`**：原 Completion Hook 已被可信 Evidence 满足；
- **`Verdict: NON-PASS`**：存在明确、仍可执行的 completion gap；列出最小 gap 与支撑它的 Evidence，不设计修复 patch；
- **`Verdict: BLOCKED`**：缺少判卷所需 authority / environment / Evidence，或原 Taskbook 已被 Human-owned contract change supersede；写清恢复条件。

Review 输出保持短：Verdict、最关键 Evidence、必要 gap / resume condition。不要复述整本 Taskbook。

## Fresh-session Review Prompt

下面是可复制到任意 fresh Northstar session 的薄 launcher；`<TASKBOOK_PATH>` 可替换成 repo/workspace 外的 Taskbook 文件路径，也可以直接附上 Taskbook 正文：

```text
Read <TASKBOOK_PATH> as the authoritative execution contract. Review the current workspace and still-valid Evidence against its Goal, decision priority, boundaries, must-preserve constraints, triggered required Verification, and Completion Hook.

Use current authoritative repo/runtime reality and the Taskbook-selected durable execution-state carrier only as evidence/provenance inputs; if the Taskbook predates carrier selection, resolve one existing carrier from Human/repo authority or repo/runtime convention before falling back to implement-notes. Do not reconstruct the task from conversation and do not create a second state protocol. Re-acquire final-judgment-critical Evidence directly when the authoritative environment is accessible. Reuse Evidence whose premises remain valid and stale only affected Evidence when premises changed. Executor narration or self-declared PASS is not proof, and any green obtained by weakening the judge is invalid.

Do not implement or repair the Goal, modify the target workspace, rewrite the Taskbook, or launch an Executor during review. Return Verdict: PASS only when the original Completion Hook is satisfied. Otherwise return Verdict: NON-PASS or BLOCKED with the smallest concrete gap, the Evidence supporting that judgment, and the exact resume condition for a separate Executor invocation.
```

Same-session review is allowed as a convenience, but correctness must be identical when the same Taskbook + repo reality + durable Evidence are supplied in a fresh session.