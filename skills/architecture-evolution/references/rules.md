# Architecture Intent Rules

只在方向仍模糊、需要区分架构 intent 与局部修改时读取。

## Start from pressure

有效 intent 必须能追溯到真实压力：

- 同一业务规则或配置解释反复在多处修改；
- 新需求持续增加特殊入口、mode flag 或 provider/family switch；
- 事故、回归或测试脆弱性集中在同一结构边界；
- 调用者必须知道内部步骤、状态、生命周期或实现类型；
- 一个模块同时承受多个不相关变化；
- 新抽象增加，但旧路径、旧事实源和旧判断仍存在；
- common/core/Harness/Runtime 被具体场景或 provider 牵引。

文件大、函数长、目录不整齐、模式不优雅或单次局部修改，不单独构成架构 intent。

## Architecture or local

只有同时满足以下大部分条件，才形成 architecture intent：

- 压力会重复出现或恢复成本高；
- 一个结构原因造成多个可观察后果；
- 影响跨越单个局部实现，但仍能限定边界；
- 需要重新确定业务语义、责任 owner、稳定 contract 或依赖方向；
- 可以说明完成后什么旧知识、路径、判断或依赖会退出。

否则给出局部修改边界，不升级。

## Four intent lenses

这些是构造 intent 的提问，不是要求立即给出目标设计。

1. **Business Semantic Integrity**
   - 是否存在同一业务的多套语义或事实解释？
   - 是否可能错误合并不同 bounded context？

2. **Stable Abstraction with Explicit Variation**
   - 调用者是否依赖实现差异而不是业务能力？
   - 哪些差异可能是 essential，哪些只是历史残留？

3. **Cohesive Capability Ownership**
   - 完整 capability、invariant、状态和生命周期是否有 owner？
   - 是否由 caller、helper 和全局对象共同拼装？

4. **Unidirectional Policy Dependency**
   - 稳定 policy 是否被 provider、场景或 implementation 反向定义或控制？
   - 是否存在 `common→scenario`、`policy→provider` 或隐式控制反转？

## Real Evolution gate

Intent 必须指向真实减少，而不是新增一层。至少能提出一个后续需要证明的退出目标：

- 平行业务语义；
- 重复事实解释；
- 调用者内部知识；
- 无效抽象或特殊入口；
- 反向或循环依赖；
- 永久兼容分支。

如果只能说“增加 facade/interface/manager/registry”，intent 尚未成立。

## Brooks risk prompts

Brooks 只作为 intent challenge 的风险词汇，不生成全量报告：

- `R6 Domain Model Distortion` — intent 是否表达真实业务，而不是代码形状？
- `R2 Change Propagation` — 它是否针对真实变化扩散？
- `R3 Knowledge Duplication` — 是否存在重复业务决定或事实解释？
- `R4 Accidental Complexity` — intent 是否会制造 speculative abstraction？
- `R5 Dependency Disorder` — 是否指向正确的 policy/contract/implementation 边界？
- `R1 Cognitive Overload` — 完成后 caller/module 是否会少知道关键步骤和隐含状态？

合理的 bounded context、vendor adapter、composition root、简单 DTO 和深模块内部复杂度都需要应用 guard，不能机械报错。

## Intent quality gate

`Architecture intent ready` 必须满足：

1. 一个明确方向，不是候选列表；
2. 有真实 pressure 和代码证据；
3. 说明为什么是架构问题而不是局部修复；
4. desired end state 描述结果，不锁死实现模式；
5. in scope、out of scope 和 must preserve 清楚；
6. 后续设计 obligations 明确；
7. 至少一个可观察的 replacement/exit 目标；
8. 一个关键 Unknown 已关闭，或明确不会阻止 intent；
9. success evidence 可验证；
10. 已检查最重要反例和 guard。
