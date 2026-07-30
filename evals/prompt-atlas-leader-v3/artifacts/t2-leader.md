在执行 agent 那边输 `/goal `，粘贴下面整段，发出去。没有目标模式就直接粘贴发送。领导只看三处：开头「这活为什么干」、`我替领导拍的板`、末尾两条「完成条件」。

```text
你是执行者，这份文档是唯一任务来源；中途没人可问，拿不准的写入 `BLOCKED.md`，跳过并继续可做项，最终一并提交。
断线或换会话先读 `PROGRESS.md` 接着做；每完成一项立即更新，禁止重做已完成项。
这次要消灭两套请求解析逻辑：所有 consumer 都走 canonical `app.parser.parse_request`，同时 batch 与 streaming 的既有输出都不变。
冲突时按「既有行为不变 > 单一解析入口 > 改动最小」让步。
“只允许／不许”违反即失败；“建议”可换更好做法，但须在 `PROGRESS.md` 记明原因。

## 我替领导拍的板
- canonical 接口采用 `parse_request(payload, *, streaming=False)`（猜的）：默认保持 batch；stream consumer 显式传 `streaming=True`。猜错会导致无法同时区分无标记的 batch 与 stream 请求。
- batch 即使收到 `trace_id`、`streaming` 字段也继续忽略它们（猜的）；否则现有 batch 输出形状会变化。
- README 删除历史 parser 的过时描述并说明 streaming 也走 canonical（猜的）；不扩写其他文档。
- `stream_consumer` 只负责选择 streaming 模式并委托；字段默认值、转换和组装全部放在 `app/parser.py`，否则不算完整合入。

## 界限
只允许修改 `app/parser.py`、`app/stream_consumer.py`、`README.md`，删除 `app/stream_parser.py`，新建/更新 `PROGRESS.md`、`BLOCKED.md`；其余路径只读。
`tests/test_parser.py`、`app/batch_consumer.py`、`app/__init__.py` 是冻结判卷面，不许改。测试文件基线 sha256 为 `23644aace3249479b456ca39879244983251d82b2a3531de911ee81f98f9efbc`。
不许改测试、顺手重构、修旁支问题、新增依赖或工具、改变公共字段名；发现需要时只记 `BLOCKED.md`。
禁止删除数据、改权限或进行其他不可恢复操作。

## 现状与任务 0
2026-07-29 实测：HEAD `403c671`、工作树干净；`python -m unittest discover -s tests -v` 共 2 项通过、skipped 0。batch 已从 `app.parser` 导入，stream 仍从 `app.stream_parser` 导入；历史 parser 对 stream 默认输出 `streaming=True`，按 `bool(...)` 转换显式值，存在 `trace_id` 时转为字符串。
先运行：
`git status --short`
`git rev-parse --short HEAD`
`python -B -m unittest discover -s tests -v`
数字或状态不符就把原始输出置于 `BLOCKED.md` 顶部，停止受影响部分。核对后把“目标／顺序／最大风险”控制在 10 行内写入 `PROGRESS.md`。
改代码前运行任务 2 的结构验收，保存其因 `app/stream_parser.py` 仍存在而变红的输出；这是红→绿证据。

## 任务 1：把两种行为收进 canonical parser
在 `app/parser.py` 增加仅限关键字的 streaming 模式，默认 batch 行为逐字段不变。streaming 模式必须保留：
- `user_id` 转字符串，`features` 转新 list、缺省 `[]`；
- `trace_id` 仅在输入存在时加入并转字符串；
- 输出始终含 `streaming`，值为 `bool(payload.get("streaming", True))`。
`app/stream_consumer.py` 改为导入 canonical parser，并用 streaming 模式调用；不在 consumer 重复解析逻辑。
验收：
python -B - <<'PY'
from app.parser import parse_request
from app.batch_consumer import consume as batch
from app.stream_consumer import consume as stream
p = {"user_id": 7, "features": ["a"], "trace_id": 42, "streaming": False}
assert parse_request(p) == {"user_id": "7", "features": ["a"]}
assert batch(p) == {"user_id": "7", "features": ["a"]}
assert parse_request({"user_id": 7}, streaming=True) == {
    "user_id": "7", "features": [], "streaming": True}
assert parse_request(p, streaming=True) == {
    "user_id": "7", "features": ["a"], "trace_id": "42", "streaming": False}
assert stream({"user_id": 7}) == {
    "user_id": "7", "features": [], "streaming": True}
assert stream(p) == {
    "user_id": "7", "features": ["a"], "trace_id": "42", "streaming": False}
PY

## 任务 2：清除历史入口和过时说明
删除 `app/stream_parser.py`；更新 README 的对应事实，不做其他文案整理。确保两个 consumer 运行时引用的是同一个 canonical 函数，仓库实现和 README 均无历史模块引用。
结构验收：
python -B - <<'PY'
from pathlib import Path
import app.batch_consumer as batch
import app.parser as parser
import app.stream_consumer as stream
assert not Path("app/stream_parser.py").exists()
assert batch.parse_request is parser.parse_request
assert stream.parse_request is parser.parse_request
targets = [*Path("app").glob("*.py"), Path("README.md")]
bad = [str(p) for p in targets if p.exists() and "app.stream_parser" in p.read_text()]
assert not bad, bad
PY
改前此命令必须红，改后必须绿；两次原始输出都保留。

## 规矩
跳过测试（skip/todo）、放宽断言、mock 被测 parser、删除测试、改验收命令、用 `|| true` 掩盖失败均算作弊。测试数不得低于 2，skipped 必须为 0。
同一验收连续失败 3 次就转做下一项并记录；结果比基线差，只撤销本次白名单内改动并如实报告，禁止留下更差状态。
交付前运行：
python -B - <<'PY'
import unittest
r = unittest.TextTestRunner(verbosity=2).run(unittest.TestLoader().discover("tests"))
assert r.wasSuccessful()
assert r.testsRun >= 2, r.testsRun
assert len(r.skipped) == 0, r.skipped
PY
`sha256sum tests/test_parser.py`
`git diff --exit-code -- tests/test_parser.py app/batch_consumer.py app/__init__.py`
`git status --short`
检查 diff 只含白名单且没有依赖文件。

## 完成条件
1. 行为验收与结构验收全部通过：batch 输出零变化，stream 的 `trace_id`、默认/显式 `streaming` 全保留，两个 consumer 共用 canonical，历史文件及引用为 0。
2. 原有测试至少 2 项通过、skipped 0，冻结文件指纹和内容不变，无测试改动、依赖、重构或越界文件。
每条都须在对话中贴实际命令输出，包含结构验收红→绿证据；只说“完成”不算。`BLOCKED.md` 随交付提交，没问题也写“无”。全部完成，或任一验收跑满 3 次仍失败即停，汇报卡点和剩余工作。
```

跑完回来说一声，我来验收，给你 5 行内的人话报告。
