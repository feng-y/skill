# Execution Graph Judgment

只由 [execution-compile.md](execution-compile.md) 在多个 work unit 之间确有真实 **dependency / parallel / shared write / join / Evidence-contingent relation** 时读取。Graph 只拥有 execution relation，不拥有 Goal、Task taxonomy、Verification authority、state machine 或 scheduler。

## Compile current relations

只表达当前 Evidence 已支持、会改变执行判断的关系：

- `depends on`：下游真实消费上游结果，或上游是安全执行前提；
- `may run in parallel`：没有 dependency，也没有 material write conflict；
- `shared write`：多个 work 会修改同一 authoritative surface，需要显式 ownership / ordering；
- `join`：组合 outcome / Verification 与各分支局部完成实质不同；
- `re-verify after`：后续 work 已知会使已有 Evidence 失效。

省略纯顺序偏好和传递依赖。当前 Evidence 已证明 `A → {B,C} → D` 就一次编译，不故意只给 A；真正依赖未来 Evidence 才知道是否存在的 work 不提前猜。

## Let Evidence evolve only affected relations

运行时新 Evidence 只修改受影响的 remaining Graph：真实 prerequisite / consumer 出现则增加必要 relation；旧 dependency 被证明不存在则删除；implementation reality 改变时可拆分、合并或重排剩余 work。已完成 work 只有其 Evidence premise 或所证明行为被影响时才重开。

一个 branch blocked 不应冻结独立 ready branch；join 只等待真实 required upstream result。**Ready frontier 只是现在能做什么，不能反向缩小 Human Goal，也不能把当前可见工作命名成新的 Layer/阶段 Goal。**

Graph 不创建 ImplementationNode / ProbeNode / VerificationNode 等 taxonomy；这些都只是 work/action。Evidence 是 reality output，不是 node。不要增加 persistent Graph object、第二本 taskbook、固定 Agent topology 或 manager/scheduler。
