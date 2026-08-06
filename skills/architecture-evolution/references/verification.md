# Verify One Architecture Design

只在 `Status: Design ready` 前读取。它验证设计假设，不验证实现正确性。

对每个维度写：

```text
Before / Expected after / How to verify
```

| Dimension | 核心问题 | 可用证据 |
| --- | --- | --- |
| Business semantic integrity | 同一业务是否只有一套 canonical semantics，不同业务是否仍清楚区分？ | 代表性输入/输出/错误场景；配置与事实解释位置；平行主流程数量 |
| Variation containment | 本质差异是否只存在于明确 variation point，稳定 contract 是否不含实现并集？ | 新增一个代表性 provider/family 的修改面；公共参数与外部 switch；专属配置归属 |
| Capability cohesion | 一项完整能力、invariant、状态和生命周期是否由一个内聚模块拥有？ | 主责任描述；状态读写位置；调用顺序；private collaborator；调用者与测试的外部拼装 |
| Unidirectional dependency | policy 是否只依赖稳定 capability，detail 是否不能反向控制 policy？ | import/include/call graph；callback/global state/registry；contract owner；composition root |
| Real replacement | 哪些旧业务路径、抽象、知识或反向依赖变得不再需要？ | Delete 清单；authoritative path；双轨退出条件；旧测试和入口的删除证据 |

再用一个代表性真实变化检查整体结果：

- 修改一条共同业务规则；
- 增加或替换一个 variation；
- 调整一个模块内部辅助实现。

每种变化都应集中在其业务、variation 或模块 owner 附近，不要求无关模块和调用者同步修改。

`Design ready` 必须同时满足：

1. 已有证据支持“同一业务/不同业务”的判断；
2. essential 与 accidental differences 被明确区分；
3. canonical capability、stable abstraction、cohesive module 和 dependency direction 相互一致；
4. 至少一个可观察负担减少；
5. 复杂度没有转移到 union interface、helper、adapter 或调用者；
6. 真实业务差异和 `Protected behavior` 被保留；
7. replacement 是当前可描述的结果，不是假想未来灵活性。

否则修改设计，或返回 `No architecture change`、`Research required`、`Decision required`。

本文件只支持架构设计判断。实现阶段仍需单独证明行为、兼容、迁移完成和实际删除。
