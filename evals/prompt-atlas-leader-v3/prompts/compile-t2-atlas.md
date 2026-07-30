Use the Prompt Atlas skill at
`/workspace/scratch/597e563ee8ac/prompt-atlas-work/skills/prompt-atlas/SKILL.md`
to handle the request below. Inspect only the assigned repository at
`/workspace/scratch/597e563ee8ac/eval/v3/runs/t2-atlas` as needed. Do not
implement or modify the repository. Prepare the complete artifact for a
separate execution agent and return only that final artifact.

用户请求：把 `app.stream_parser` 的能力完整合入 canonical
`app.parser.parse_request`，所有 consumer 统一使用 canonical parser，删除历史
`stream_parser.py`。保留 batch 当前行为，同时保留 streaming 的 `trace_id`、
`streaming` 语义。只做这次迁移，不顺手重构，不改测试，不新增依赖。
请准备给执行 Agent 的完整任务。
