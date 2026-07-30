Use the Leader skill at
`/workspace/scratch/597e563ee8ac/leader-source/leader/SKILL.md` to handle the
request below. Inspect only the assigned repository at
`/workspace/scratch/597e563ee8ac/eval/v3/runs/t2-leader` as needed. Do not
implement or modify the repository. Prepare the complete taskbook for a
separate execution agent and return only the final deliverable required by the
skill.

用户请求：把 `app.stream_parser` 的能力完整合入 canonical
`app.parser.parse_request`，所有 consumer 统一使用 canonical parser，删除历史
`stream_parser.py`。保留 batch 当前行为，同时保留 streaming 的 `trace_id`、
`streaming` 语义。只做这次迁移，不顺手重构，不改测试，不新增依赖。
请准备给执行 Agent 的完整任务。
