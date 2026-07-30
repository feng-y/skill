已完成 canonical parser 合并；`BLOCKED.md` 为“无”。

行为验收：

```text
exit_code=0
```

结构验收红→绿：

```text
改前 exit_code=1
Traceback (most recent call last):
  File "<stdin>", line 5, in <module>
AssertionError

改后 exit_code=0
```

最终测试：

```text
test_batch_consumer (test_parser.ParserTests.test_batch_consumer) ... ok
test_canonical_shape (test_parser.ParserTests.test_canonical_shape) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

冻结文件与范围检查：

```text
23644aace3249479b456ca39879244983251d82b2a3531de911ee81f98f9efbc  tests/test_parser.py
git diff --exit-code -- tests/test_parser.py app/batch_consumer.py app/__init__.py
exit_code=0

 M README.md
 M app/parser.py
 M app/stream_consumer.py
 D app/stream_parser.py
?? BLOCKED.md
?? PROGRESS.md
```

`git diff --check` 通过；无测试、依赖或越界文件改动。
