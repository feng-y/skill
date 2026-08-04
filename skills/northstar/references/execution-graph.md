# 执行图（Execution Graph）

仅在线性 Task 列表会掩盖真实依赖或并行关系时使用。

- `depends on`：仅用于结果消费关系或安全执行前置条件；
- `may run in parallel`：不存在依赖或写冲突时使用；
- `reverify at join`：后续修改可能使证据失效，但不应阻止并行工作时使用。

每个分支都必须重新汇合，或结束于一个显式终止路由。省略传递依赖和仅仅表示先后顺序的边。所有权与证据规则仍写在普通 Task 合同中。不要引入 Graph schema、固定 Agent 拓扑或多本任务书。
