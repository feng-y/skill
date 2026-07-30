# 进度
目标：让 batch 与 streaming consumer 共用 `app.parser.parse_request`，且既有输出不变。
顺序：先保存结构验收红灯，再合并解析行为并改 consumer，最后删除历史入口、更新 README、完整验收。
最大风险：默认 batch 误带 `trace_id` 或 `streaming`，改变既有输出形状。
状态：基线检查通过（HEAD `403c671`，工作树干净，2 tests passed，0 skipped）。
结构验收（改前，exit 1）：
```text
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
AssertionError
```

## 已完成

- 任务 1：canonical parser 已增加仅限关键字的 streaming 模式；stream consumer 已显式委托该模式。
- 任务 1 行为验收通过（exit 0，无输出）。
- 任务 2：已删除 `app/stream_parser.py`，README 已说明 streaming 走 canonical parser。
- 任务 2 结构验收通过（exit 0，无输出），完成红→绿。
- 最终测试通过：2 tests passed，0 skipped。
- 冻结测试 sha256 保持 `23644aace3249479b456ca39879244983251d82b2a3531de911ee81f98f9efbc`，冻结文件 diff 为空。
- 最终范围仅含允许的 4 个实现/文档路径及 `PROGRESS.md`、`BLOCKED.md`，无依赖文件。
