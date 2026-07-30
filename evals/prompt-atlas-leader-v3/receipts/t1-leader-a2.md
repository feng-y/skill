已完成折扣归一化，改动仅涉及白名单文件：`discount.py`、`PROGRESS.md`、`BLOCKED.md`；无新增依赖，`BLOCKED.md` 内容为“无”。

基线：

```text
$ git status --short
[无输出，exit 0]

$ ./check.sh
checks passed

$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
test_fraction_is_preserved ... ok
test_fraction_price ... ok
Ran 2 tests in 0.000s
OK
```

合约及红→绿：

```text
$ [完整合约命令]
contract passed
exit 0

$ [旧行为模拟命令]
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
AssertionError
exit 1

$ [再次运行完整合约]
contract passed
exit 0
```

最终验收：

```text
$ PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s tests -v
test_fraction_is_preserved ... ok
test_fraction_price ... ok
Ran 2 tests in 0.000s
OK

$ ./check.sh
checks passed

$ git diff --check
[无输出，exit 0]

$ git diff --exit-code -- README.md check.sh tests/test_discount.py
[无输出，exit 0]

$ git status --short
 M discount.py
?? BLOCKED.md
?? PROGRESS.md
```

`PROGRESS.md` 共 5 行，满足不超过 10 行要求。
