实现状态：`ready for independent acceptance`（尚无独立/隐藏测试结果，不宣称全局 `MET`）。

修改文件：

- `discount.py`：新增严格类型、有限性和范围校验；`[0,1]` 原样作为比例，`(1,100]` 除以 100。`final_price(price, discount)` 签名及原有价格转换、两位小数舍入框架保持不变。

验证证据：

- 有效归一化：`0→0.0`、`0.2→0.2`、`1→1.0`、`1.5→0.015`、`20→0.2`、`100→1.0`。
- 价格矩阵：折扣 `0/0.2/1/20/100` 分别得到 `100.0/80.0/0.0/80.0/0.0`。
- 20 个无效输入均抛出异常：布尔值、字符串、空字符串、`None`、容器、复数、`Decimal`、`Fraction`、NaN、正负无穷、负数及大于 100 的值。
- API：`inspect.signature(final_price)` 为 `(price, discount)`。
- `python -B -m unittest -v tests/test_discount.py`：2 项通过。
- `./check.sh`：退出码 0，输出 `checks passed`。
- 一次性边界矩阵：通过。
- `git diff --check`：通过。
- 最终仅 `discount.py` 被修改；`tests/test_discount.py` 与 `check.sh` 无差异，未新增依赖。
