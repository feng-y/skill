# Autonomous handoff guidance

只在简单 task definition 不足以支撑较长自主执行时读取。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是接口，不是流程模板。Taskbook 定义目标状态与完成证明，Executor materialize How。

## Goal

保留 Human-owned outcome，以及真正会约束执行选择的 priority / boundary / must-preserve。用户给出的实现手段默认是 hypothesis，除非 Human 或 repo authority 明确把它变成约束。

优先引用 repo 已有规格：tests、schema、ADR、Architecture Intent、验收脚本、可执行 reference。不要把它们重新翻译成一份更弱的散文规格。

## Execution

只拆 judgment 或 dependency 真正不同的 work。Graph 只表达真实依赖；不要把文件、函数、BUILD edit、调试顺序变成节点。

普通 factual / implementation Unknown 由 Executor 从当前 repo reality 处理。只有结论会改变上游 Goal / authority 时才重新打开上层决定。

已有且仍符合 Goal 的 work / Evidence 可以继续复用；新 Evidence 只让依赖它的结论 stale。Human 对当前 handoff 的 material correction 也是 Evidence：从最高受影响层重推，只替换依赖它的编译结果，然后继续完成本次 handoff，不能把修正留成 conversation-only patch。

## Verification / Evidence

写“完成需要证明什么”，不预写调试流程。优先使用 Human / repo 已有的 authoritative checks；需要引用 baseline 时只保留真正承担 coverage / attribution 的信号，并以当前 reality 为准。

Evidence 要能支撑实际 completion claim，而不是活动说明或自报 PASS。若验证失败，修实现或准确报告；不要削弱 judge 来制造成功。只有具体 false-green / gameability / independence 风险存在时再读 [verification-trust.md](verification-trust.md)。

## Handoff

保持 minimum-sufficient。Research 中 Executor 能可靠重建的细节不需要搬进 Taskbook；不写会导致错误目标、边界或验证判断的非显然事实才留下。

Autonomous handoff 必须 materialize 为 OS/runtime 临时目录中的 Markdown artifact，且路径位于当前 repo/workspace 外；不固定 `/tmp`、文件名或目录结构。artifact 是 authoritative Taskbook，成功写入才算交付并允许 `Status: Executable`。若 Human 后续 material correction 改变当前 contract，优先重写同一 artifact；旧 artifact 不可访问时写替代 artifact，并明确 supersede 关系。只在聊天里解释修正或追加 delta 不算完成 handoff；无法写入时准确 Blocked 并给恢复条件。

执行状态使用现有 `implement-notes`，保存 progress、关键 decision / Evidence、blocker 和 resume point。自主 Taskbook 默认保持短；如果内容不断增长，先删重复和 implementation intelligence，而不是增加更多规则。
