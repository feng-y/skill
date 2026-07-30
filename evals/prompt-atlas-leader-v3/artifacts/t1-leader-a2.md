在执行 agent 那边输 `/goal `，粘贴下面整段，发出去。领导只看三处：开头「这活为什么干」两行、「我替领导拍的板」、末尾「完成条件」两条硬指标。

```text
你是执行者，这份文档是唯一任务来源；中途没人可问，拿不准的写进 `BLOCKED.md`，跳过并继续可做项，最后一并交付。
断线或换会话先读 `PROGRESS.md` 接着做；每完成一项立刻更新，不要重做。
这活要统一 checkout 的折扣语义：比例和百分数输入得到同一结果，所有危险或含糊输入明确报错。
冲突时按“折扣正确性 > 输入拒绝完整性 > 公开 API 兼容 > 改动小”让步。
“只允许／不许”违反即失败；“建议”可换更好做法，但须在 `PROGRESS.md` 记原因。

## 我替领导拍的板
- 错误类型（猜的）：类型不对报 `TypeError`，数值非法报 `ValueError`｜猜错只影响异常分类，不影响必须报错。
- “只接受 int 和 float”（猜的）：仅内建 `int`、`float`，其子类及 Decimal、Fraction 等也拒绝；`bool` 必须先于整数判断拒绝｜猜错可能影响冷门调用方。
- `final_price` API 不变：名称、`(price, discount)` 签名、价格转 float、保留两位小数行为不动；仅折扣归一化语义改变。
- 不补测试文件：用户已明确不许改测试；用一次性 Python 合约命令验收。

## 界限
只允许改 `discount.py`，并新建或更新 `PROGRESS.md`、`BLOCKED.md`。其他路径只读。
`tests/test_discount.py`、`check.sh` 是冻结判卷标准，禁止修改、删除、改权限或绕过；README 也不得顺手改。
不重构价格逻辑、不新增依赖、配置、流程或工具；确有必要写入 `BLOCKED.md`，不得擅自扩大范围。
不可恢复的操作立即停下记录，继续其他安全工作。

## 现状与任务 0
2026-07-29 实测：`./check.sh` 退出 0，但只固定打印 `checks passed`，是假绿灯；真实命令
`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`
运行 2 个测试、0 跳过、全绿。现实现把折扣直接 `float(value)`；合约在 `1.1`、`20` 等百分数输入处失败。工作树开工时为空。
先运行：
`git status --short`
`./check.sh`
`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`
若工作树不空、脚本非 0、测试不是恰好 2 个或有跳过，停止受影响部分，把原始输出置于 `BLOCKED.md` 顶部。核对后在 `PROGRESS.md` 用不超过 10 行写目标、顺序、最大风险，再动工。

## 任务 1：修正折扣归一化
只改 `discount.py`：`0 <= value <= 1` 原样作为比例；`1 < value <= 100` 除以 100。边界 0、1、100 必须合法。拒绝 bool、所有字符串、非内建 int/float、NaN、正负无穷、负数和大于 100。
建议使用标准库有限数检查；不得靠字符串转换放行输入。
运行以下合约，必须退出 0 并打印 `contract passed`：

PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
import inspect, math
from decimal import Decimal
from fractions import Fraction
from discount import normalize_discount, final_price
valid=[(0,0.0),(-0.0,-0.0),(0.2,0.2),(1,1.0),(1.1,0.011),(20,0.2),(20.0,0.2),(100,1.0)]
for value, expected in valid:
    got=normalize_discount(value)
    assert math.isclose(got, expected, rel_tol=0, abs_tol=1e-12),(value,got)
for value in [True,False,"20","0.2","",b"20",None,[],{},Decimal("20"),Fraction(1,5),20j]:
    try: normalize_discount(value)
    except TypeError: pass
    else: raise AssertionError(f"expected TypeError: {value!r}")
for value in [float("nan"),float("inf"),float("-inf"),-0.01,100.01,101]:
    try: normalize_discount(value)
    except ValueError: pass
    else: raise AssertionError(f"expected ValueError: {value!r}")
assert str(inspect.signature(final_price)) == "(price, discount)"
assert final_price(100,0.2) == final_price(100,20) == 80.0
assert final_price("12.345",0) == 12.35
print("contract passed")
PY

反向验证：运行下列旧行为模拟，必须非 0 并出现 `AssertionError`；它只改内存，不改文件。随后重跑上面合约恢复全绿，并粘贴红→绿输出。

PYTHONDONTWRITEBYTECODE=1 python - <<'PY'
import discount
discount.normalize_discount=lambda value: float(value)
assert discount.normalize_discount(20) == 0.2
PY

最后运行：
`PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v`
`./check.sh`
`git diff --check`
`git diff --exit-code -- README.md check.sh tests/test_discount.py`

## 规矩
禁止 skip/todo、删测试、放宽断言、mock 被测对象、改验收脚本、`|| true` 或吞掉异常；测试数不得少于 2，跳过必须为 0。
同一验收连败 3 次即停止重复试错，记录每次失败与下一步；结果比基线差就回滚该尝试并如实报告。

## 完成条件
1. 合约覆盖的 8 个合法输入、18 个非法输入及 3 项 `final_price` 兼容检查全绿，现有 2 个测试全绿且 0 跳过，`./check.sh` 退出 0。
2. 冻结文件 diff 为空、无新增依赖，改动仅落在白名单。
每条都要在对话中贴实际命令输出，含反向验证红→绿；只说完成不算。`BLOCKED.md` 必须随交付提交，没问题也写“无”。完成上述条件，或同一验收已跑满 3 轮即停并如实说明卡点和缺口。
```

跑完回来说一声，我来验收，给你 5 行内的人话报告。
