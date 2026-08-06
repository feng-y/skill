# Verify One Architecture Design

只在 `Status: Design ready` 前读取。它验证设计假设，不验证实现正确性。

对每个适用维度写：

```text
Before / Expected after / How to verify
```

| Dimension | 核心问题 | 可用证据 |
| --- | --- | --- |
| Change locality | 同类变化是否需要更少的模块、判断和测试？ | 代表性 variant 的修改位置；调用者是否仍协调同一行为 |
| Ownership concentration | 一个责任、事实、状态或变化是否只有一个 authoritative owner？ | 重复解释/状态读取是否消失；projection 与 guard 是否明确 |
| Dependency stability | 稳定主流程是否只依赖稳定需要？ | 应删除的 import/include/call；core 中具体 provider/family 判断 |
| Caller knowledge | 调用者是否少知道步骤、状态、顺序、配置和实现类型？ | 方法/参数、调用序列、外部拼装和测试穿透的 before/after |
| Replacement | 什么现有负担变得不再需要？ | switch、重复判断、wrapper、旧入口、事实源、无效依赖；双轨退出条件 |

`Design ready` 必须同时满足：

1. 主要规则违反有直接证据；
2. target owner 与 seam 解决的是根因，不只是症状；
3. 至少一个可观察负担减少；
4. 复杂度没有转移到 helper、adapter 或调用者；
5. 真实业务差异与 `Protected behavior` 被保留；
6. replacement 是当前可描述的结果，不是假想未来灵活性。

否则修改设计，或返回 `No architecture change`、`Research required`、`Decision required`。

本文件只支持架构设计判断。实现阶段仍需单独证明行为、兼容、迁移完成和实际删除。
