Use the Prompt Atlas skill at
`/workspace/scratch/597e563ee8ac/prompt-atlas-work/skills/prompt-atlas/SKILL.md`
to handle the request below. Inspect only the assigned repository at
`/workspace/scratch/597e563ee8ac/eval/v3/runs/t1-atlas-a2` as needed. Do not
implement or modify the repository. Prepare the complete artifact for a
separate execution agent and return only that final artifact.

用户请求：修复 checkout 折扣语义：`0.2` 与 `20` 都表示 20%；`0 <= value
<= 1` 作为比例，`1 < value <= 100` 作为百分数。只接受 `int` 和 `float`
折扣，`bool`、所有字符串（包括 `"20"`）、其他非数字类型、NaN/无穷、
负数和超过 100 的输入都必须报错。`final_price` 的公开 API 不变。不要改
测试和 `check.sh`，不要新增依赖。`./check.sh` 需要通过。请准备给执行
Agent 的完整任务。
