Status: Executable

**Goal**

在 `/workspace/scratch/597e563ee8ac/eval/v3/runs/t2-atlas` 完成一次最小化 parser 迁移：让 canonical `app.parser.parse_request` 成为唯一请求解析实现；所有 consumer 均使用它；删除 `app/stream_parser.py`。迁移后同时保持两条现有可观察契约：

- batch/default canonical 调用仍只返回标准字段，不因输入含 `trace_id` 或 `streaming` 而改变现有输出形状；
- streaming 调用仍保留历史 `trace_id` 与 `streaming` 语义，以及共有的 `user_id`、`features` 规范化行为。

**State**

- 执行目标：`/workspace/scratch/597e563ee8ac/eval/v3/runs/t2-atlas`，当前 `HEAD 403c671`（`master`）， intake 时工作树干净。
- 已核实结构：
  - `app/parser.py` 是 README 声明的 canonical parser，目前输出 `user_id = str(payload["user_id"])` 与 `features = list(payload.get("features", []))`。
  - `app/batch_consumer.py` 已导入 `app.parser.parse_request`。
  - `app/stream_consumer.py` 仍导入 `app.stream_parser.parse_request`。
  - `app/stream_parser.py` 重复共有解析逻辑，并额外执行：
    - 仅当输入中存在 `trace_id` 键时，输出 `trace_id = str(payload["trace_id"])`；
    - 始终输出 `streaming = bool(payload.get("streaming", True))`。
  - `README.md` 仍明确声称 streaming path 使用历史 parser，迁移后若不更新将失真。
- 已核实基线：
  - `python -m unittest discover -s tests -v` 通过，2 个测试；现有测试只覆盖 canonical/batch，不覆盖 streaming。
  - 直接基线探针确认：
    - batch/canonical 对 `{"user_id": 7, "trace_id": 42}` 输出 `{"user_id": "7", "features": []}`；
    - streaming 对无 streaming 专用字段的输入额外输出 `"streaming": True`；
    - `trace_id: 42` 输出 `"trace_id": "42"`；
    - 存在 `trace_id: None` 时输出 `"trace_id": "None"`；
    - `streaming: False` 或 `0` 输出 `False`。
- 架构内核已确定：解析能力只有 `app.parser.parse_request` 一个所有者，consumer 不再依赖或复制历史 parser。
- 证据可修订的目标假设：canonical API 需要一种显式、局部的 streaming 调用上下文/opt-in，默认调用保持 batch 行为，stream consumer 选择 streaming 行为。具体参数名和最小 API 形式属于执行 How；不能简单地让 canonical 默认无条件增加 `"streaming": True`，否则会破坏已核实的 batch 契约。
- 证明缺口：现有权威测试路径不覆盖 streaming，且用户禁止改测试；因此执行者自身证据最多达到 `ready for independent acceptance`，全局 `MET` 还需要独立验收边界确认 streaming 回归未被当前测试漏掉。

**Decisions**

- canonical `app.parser.parse_request` 是迁移后的唯一 parser。
- 所有 consumer 统一使用 canonical parser。
- 删除历史 `app/stream_parser.py`，不保留兼容 shim。
- batch 当前行为保持不变。
- streaming 的 `trace_id`、`streaming` 语义保持不变。
- 只实施本次迁移；不顺手重构、不修改测试、不新增依赖。

**Constraints**

- 允许的写入范围限于：
  - `app/parser.py`；
  - `app/stream_consumer.py`；
  - 删除 `app/stream_parser.py`；
  - 仅为移除迁移后失真的描述而最小更新 `README.md`。
  `app/batch_consumer.py` 已符合目标，除非执行证据证明迁移必需，否则不要改动；不得改测试、添加文件或修改依赖/工具配置。
- 保持 batch/default canonical 的完整当前契约：`user_id` 字符串化、`features` 列表化且缺省为 `[]`，输出不因输入含 `trace_id`/`streaming` 而自动增加 streaming 字段。
- 保持 streaming 的完整当前契约：共有字段与 batch 一致；`trace_id` 按“键是否存在”判断，存在即对值调用 `str`；`streaming` 始终存在，缺省 `True`，显式值经 `bool` 转换。
- 不得把 streaming 专用解析逻辑复制进 consumer；consumer 只负责选择 canonical parser 的适当调用上下文。
- Judge 不得通过修改/删除/跳过现有测试、弱化断言或用更窄输入集合制造通过。
- Population 至少包含：无 streaming 专用字段、存在普通及 `None` 的 `trace_id`、缺省/假值/真值 `streaming`，以及带 streaming 专用字段的 batch 输入。
- Object 必须是实际 `app.batch_consumer.consume`、`app.stream_consumer.consume` 和 canonical parser，不得以 mock 或仅测试复制出来的辅助逻辑替代。
- 不引入依赖，不做命名、模块布局、类型系统或无关风格重构。

**Loop**

`Act → Observe → Evaluate → Next`

1. 从已核实的行为差异出发，选择能让 default 保持 batch、stream consumer 显式选择 streaming 语义的最小 canonical API；将历史 parser 的能力合入 `app.parser.parse_request`，切换 stream consumer，删除历史模块，并仅修正直接失真的 README 描述。
2. 观察代码差异、导入关系和实际 consumer 输出；使用 `rg` 确认不存在遗留 `app.stream_parser` 引用或第二份解析实现。
3. 运行未修改的 README 指定测试命令，并用独立于测试文件的直接运行探针覆盖 Constraints 中的 batch/streaming 行为矩阵。必要时用迁移前已记录基线作逐项对照。
4. 对完整 Goal 返回 `MET` 或 `UNMET` 及简短证据理由。若任一输出、导入、删除或范围条件未满足，将原因写回当前 State，调整实现 How 后继续；不要通过改变 Goal、测试或保护边界消除失败。

**Evaluation**

局部完成证据包括代码可导入、单个 consumer 输出正确、单个搜索或测试命令通过；这些都不能单独构成全局 `MET`。

全局 Gate 必须同时满足：

- `app/stream_parser.py` 不存在；`app/stream_consumer.py` 与 `app/batch_consumer.py` 均从 `app.parser` 使用 canonical parser；仓库中不存在失真的历史 parser 引用或重复解析实现。
- 未修改的 `tests/test_parser.py` 保持原样，`python -m unittest discover -s tests -v` 通过。
- default canonical 与 batch consumer 对标准输入保持原结果；对含 `trace_id`/`streaming` 的 batch 输入也保持仅有 `user_id`、`features` 的现有输出形状。
- stream consumer 的直接证据覆盖并通过：
  - 无 `trace_id`、无 `streaming` 时，输出共有字段及 `"streaming": True`；
  - 存在 `trace_id: 42` 时输出 `"trace_id": "42"`；
  - 存在 `trace_id: None` 时输出 `"trace_id": "None"`；
  - `streaming` 缺省为 `True`，显式假值经 `bool` 得到 `False`，真值经 `bool` 得到 `True`；
  - 共有的 `user_id`、`features` 规范化与迁移前一致。
- `git diff --check` 通过，实际 diff 仅落在允许写入范围，且无新依赖、测试改动或无关重构。
- 证明未通过弱化 Judge、收窄 Population 或替换 Object 获得；受损、缺失或假绿的证据均为 `UNMET`。
- 因现有 suite 不覆盖 streaming，本任务需要独立接受边界：由执行者之外的 fresh-context verifier 或上层 governing evaluation 针对上述行为矩阵和结构目标复核。执行者自证通过只能标记 `ready for independent acceptance`；该边界通过后才能宣告全局 `MET`。

**Output**

提交完成后的仓库状态，并附简洁 completion receipt，逐项映射：

- canonical 单一所有权与历史模块删除 → 文件/导入搜索证据；
- batch 行为保持 → 未修改测试结果及 batch/default 直接探针；
- streaming 语义保持 → streaming 行为矩阵的实际输入/输出；
- 范围与质量约束 → `git diff --check`、diff 文件清单、无测试/依赖改动；
- 独立验收状态 → `ready for independent acceptance` 或接受边界的实际结果。

若阻塞，block receipt 必须列出未满足条件、已尝试的证据路径、缺少的具体权限/证据/决定，以及可解除阻塞的动作；不得用笼统失败总结代替。

**Control**

- 使用 direct loop：一名执行者、一个当前动作、对应局部检查和一个全局 Gate 足以完成这次小范围迁移；仅在发现真实协调、隔离或恢复需求时升级复杂度。
- 开始时以最小 canonical 调用上下文设计推进，不预先冻结参数名等实现细节。
- 全局 Evaluation 为 `UNMET` 且仍有安全、能产生新证据的动作时继续；观察结果否定当前 How 或重复动作不再减少缺口时重规划。
- 每轮保留已完成证据、当前缺口与下一动作；不得因局部测试通过提前完成。
- 完成实现与执行者证据后进入 `ready for independent acceptance`；只有独立接受边界通过全部全局 Gate 才能完成为 `MET`。
- 仅当 settled authority 内已无安全下一步，且继续需要新的人类决定、权限扩张或不可获得的必要外部证据时阻塞。
