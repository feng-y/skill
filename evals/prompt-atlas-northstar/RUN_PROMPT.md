# Clean-Session Run Prompt

Paste the block below into a new conversation.

```text
执行 Prompt Atlas / Northstar clean-session taskbook 验证。

必须先完整读取：

1. https://github.com/feng-y/skill/blob/northstar-chinese-edition/evals/prompt-atlas-northstar/VALIDATION_PLAN.md
2. https://github.com/feng-y/skill/blob/northstar-chinese-edition/evals/prompt-atlas-northstar/OFFLINE_SOURCE_INDEX.md

读取计划和索引后，不要返回进度说明，也不要说“12 个源尚未加载”。必须在同一轮继续打开 OFFLINE_SOURCE_INDEX.md 中的三个固定 bundle：

- B-P：包含 P1–P5
- B-N：包含 N1–N5
- B-L：包含 L1–L2

三个 bundle 全部 LOADED，就等于 12 个权威源全部加载。先输出三行 bundle source-load table，然后立即继续执行 VALIDATION_PLAN.md 的全部 8 个案例；不要停下来等待确认。

对每个案例分别生成 Leader、Prompt Atlas、Northstar 三个独立候选，再统一按 12 个维度评分。不要修改仓库或 PR，不使用其他对话背景，不预设结论。候选生成前不得把 bundle 内容改写成摘要来代替原文。

最终输出计划规定的完整报告，并明确本轮能证明什么、不能证明什么。只有在实际尝试三个 bundle URL 后仍无法打开某一个时，才报告失败的 bundle URL 和工具限制；不得把 bundle 内的单个源直接标记为未加载，也不得编造评测结果。
```
