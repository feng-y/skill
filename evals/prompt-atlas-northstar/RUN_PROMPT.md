# Clean-Session Run Prompt

Paste the block below into a new conversation.

```text
执行 Prompt Atlas / Northstar clean-session taskbook 验证。

必须先联网或使用 GitHub 工具，完整读取以下两个文件：

1. https://github.com/feng-y/skill/blob/northstar-chinese-edition/evals/prompt-atlas-northstar/VALIDATION_PLAN.md
2. https://github.com/feng-y/skill/blob/northstar-chinese-edition/evals/prompt-atlas-northstar/SOURCE_INDEX.md

先按 SOURCE_INDEX.md 加载 P1–P5、N1–N5、L1–L2 共 12 个权威源，并输出 source-load table。可以使用 GitHub connector、网页或 raw fallback；不要把相对路径当成已加载内容。

只有 12 个源全部 LOADED 后，才严格执行 VALIDATION_PLAN.md 的 8 个案例：分别生成 Leader、Prompt Atlas、Northstar 三个独立候选，再统一按 12 个维度评分。不要修改仓库或 PR，不使用其他对话背景，不预设结论。

最终输出计划规定的完整报告，并明确本轮能证明什么、不能证明什么。如果任何源无法加载，只报告失败的具体 URL 和工具限制，不得编造评测结果。
```
