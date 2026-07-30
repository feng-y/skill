Status: Executable

**Goal**

在仓库 `/workspace/scratch/597e563ee8ac/eval/v3/runs/t1-atlas-a2` 中修复 checkout 折扣归一化，使 `0.2` 与 `20` 都表示 20%：`0 <= value <= 1` 按比例原样使用，`1 < value <= 100` 按百分数除以 100。仅接受 `int`、`float` 折扣且显式拒绝 `bool`；所有字符串、其他类型、NaN、正负无穷、负数和大于 100 的值均须抛出异常。保持 `final_price` 的公开 API 和折扣语义之外的既有价格计算行为，并使所有可信验收门通过。

**State**

- 执行目标：上述绝对路径；检查时 HEAD 为 `3f1d5cc80467a5a783798d399b3f0865bb421d8b`，工作树干净。本次编译仅检查，未修改仓库。
- `discount.py` 当前让 `normalize_discount(value)` 直接返回 `float(value)`；`final_price(price, discount)` 仍执行 `round(float(price) * (1.0 - normalize_discount(discount)), 2)`。
- 已验证当前行为：`0.2` 正确归一化并使 `final_price(100, 0.2) == 80.0`；但 `20` 被归一化为 `20.0`，价格成为 `-1900.0`。`bool`、数字字符串、负数、超过 100 的数、NaN 和无穷当前也会被错误接受。
- `python -m unittest -v tests/test_discount.py` 已验证通过 2 个现有测试；它们只覆盖 `0.2`。
- `./check.sh` 已验证返回成功，但脚本仅无条件打印 `checks passed` 并退出 0，因此它是必须保留并通过的门，却不能证明新语义。
- 未指定异常的具体类型或消息；只要所有无效折扣在正常调用路径中可靠抛出异常即可。具体异常类型属于执行者可决定的实现细节。
- 目标是代码状态变更，而不是仅给出分析。

**Decisions**

- 用户确认：闭区间 `[0, 1]` 是比例；区间 `(1, 100]` 是百分数。
- 用户确认：只接受 `int` 和 `float`；尽管 `bool` 是 `int` 的子类，也必须拒绝。
- 用户确认：所有字符串，包括 `"20"`，以及其他类型都必须拒绝；不得通过数值强制转换扩大输入集合。
- 用户确认：NaN、无穷、负数和大于 100 的折扣都必须拒绝。
- 用户确认：`final_price` 的公开 API 不变，不修改测试、`check.sh`，不新增依赖。

**Constraints**

- 保持 `final_price(price, discount)` 的名称、参数顺序、调用方式与返回计算框架；仅让其通过修正后的折扣归一化获得新语义，不借机改变 price 的转换或两位小数舍入行为。
- 类型检查必须使 `True`、`False` 失败，并拒绝字符串、`None`、容器、复数及 `Decimal`、`Fraction` 等所有非 `int`/`float` 输入。
- 有效边界必须精确：`0`、`1`、`100` 有效；小于 0 或大于 100 无效；所有非有限浮点数无效。
- 不修改 `tests/test_discount.py`、`check.sh` 或其 Judge/Population；不得通过跳过、弱化、替换测试或伪造命令成功来达成验收。
- 不新增第三方依赖；如需辅助，只能使用 Python 标准库。
- 将改动限制在实现该行为所需的最小生产代码范围，不做无关重构。

**Loop**

Act → Observe → Evaluate → Next

1. 从 `discount.py` 开始，实施最小的类型、有限性、范围校验和区间归一化；先拒绝 `bool` 和非 `int`/`float`，再做数值判断。
2. 观察精确输入输出和异常矩阵，并检查 `final_price` 是否继续复用 `normalize_discount`、保持原公开签名与舍入行为。
3. 运行现有单元测试与 `./check.sh`，再用不写入仓库的一次性 Python 断言覆盖现有测试缺失的有效边界、两种表示和所有拒绝类别。
4. 按 Evaluation 返回 `MET` 或带简短证据的 `UNMET`。若为 `UNMET`，把失败输入、实际结果和当前差距写回 State，修正实现 How 后重复；证据推翻实现方案时重规划，不改变用户已确认语义。

**Evaluation**

本地实现完成须同时满足：

- `normalize_discount(0) == 0`、`normalize_discount(0.2) == 0.2`、`normalize_discount(1) == 1`、`normalize_discount(1.5) == 0.015`、`normalize_discount(20) == 0.2`、`normalize_discount(100) == 1`。
- `final_price(100, 0.2) == 80.0` 且 `final_price(100, 20) == 80.0`；同时验证边界如折扣 `0` 得 `100.0`、折扣 `1` 和 `100` 均得 `0.0`。
- `True`、`False`、`"20"`、`"0.2"`、空字符串、`None`、容器、复数、其他数值类、NaN、`inf`、`-inf`、代表性负数以及略大于 100 的值均抛出异常。
- `python -m unittest -v tests/test_discount.py` 和 `./check.sh` 均成功。
- 最终 diff 未修改测试、`check.sh`，未新增依赖或无关改动，`final_price` 公开签名未变。

由于可见 `check.sh` 是无条件成功且现有测试未覆盖新增语义，执行者设计的一次性断言只能使状态达到 `ready for independent acceptance`。全局 `MET` 还要求仓库的独立评测/隐藏测试边界对上述完整语义验收通过；证明不足、测试被弱化或独立验收失败均为 `UNMET`。

**Output**

交付实现后的代码，并给出简洁完成回执：列出修改文件；将每项有效区间、拒绝类别、API 保持和受保护文件约束映射到实际命令或输入输出证据；记录 `./check.sh`、现有单元测试和一次性边界矩阵的结果；注明独立验收结果。若尚无独立验收结果，明确报告 `ready for independent acceptance`，不得宣称全局完成。若阻塞，列出未满足条件、已尝试的证据路径、准确阻塞项及解锁所需条件。

**Control**

采用单执行者直接循环：以 `discount.py` 的最小实现改动启动，每轮保留当前失败证据和下一动作。只要全局 Evaluation 为 `UNMET` 且仍有范围内、安全、能产生新证据的动作，就继续；重复动作不再减少不确定性时重规划。仅在出现真实的跨任务协调、恢复或隔离需求时升级执行结构。独立评测是此任务的风险触发验收边界，不要求预设多 Agent 拓扑。只有可信全局 `MET` 才完成；只有当继续工作需要新的用户决策、权限、范围扩张或不可获得的必需外部证据，且当前授权内已无安全下一步时才阻塞。
