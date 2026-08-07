# Verification / Evidence Trust

只在普通 repo verification 可能假通过、可被针对性优化、静默失效，或结果确实需要额外独立性时读取。默认优先使用 repo 已有、受保护且足以覆盖 Goal 的 verification；不要为了“更严格”机械增加暗卷或独立 judge。

## Evidence 必须能直接支持 Goal

- **覆盖真实 claim。** build、lint、coverage、活动记录或局部测试只有在确实覆盖当前要判断的行为时才有证明力；provider 不能证明它覆盖范围之外的事实。
- **跟真实 affected surface 走。** 验证范围根据实际 change surface、effective binding/config 和真实 consumer/target 决定，不根据“只是 cleanup/refactor”或预期 `0-diff` 主观降级。
- **前提必须仍成立。** 版本、环境、对象、binding/config 或上游行为变化可能影响原证据时，该 evidence 失效；不受影响的 evidence 可以继续复用。
- **判卷标准不能偷改。** 除非 Goal 明确要求且仍保留等价可信验证，否则不得削弱断言、缩小 coverage、跳过测试、用 mock 绕开真实对象、降低阈值、吞掉失败传播或修改验收脚本来制造 PASS。
- **基线不能无授权倒退。** 已有权威 baseline 被破坏就是回归，不因为实现更简单或成本更低而自动可接受。

## 反向验证：检查坏了必须会响

关键检查存在空跑、假绿或静默失效风险时，制造一次受控且局部的失败，确认失败信号真实出现；恢复后再运行正常验证。

只有“这里坏了会有人知道”已经由 repo 机制本身可靠保证时，才不需要额外反向 probe。反向验证只验证 judge 的有效性，不代替 Goal 行为本身的正常验证。

## 明卷与暗卷

**明卷**是 Executor 可见的 verification。它是默认路径；如果 repo 的受保护测试、replay、CI、schema 或其他 judge 已经足以证明 Goal，就直接使用，不额外增加私有检查。

只有 visible judge 可以被针对性优化、实现者可以轻易迎合样本、或公开验证无法单独形成可信判断时，才预留少量**暗卷**：

- 暗卷必须从同一个公开 Goal、边界和验证要求推导，不能增加隐藏要求；
- 可以换样本、输入或观察路径，但验证的仍是同一行为；
- 必须在执行前冻结，并在 runtime 能隔离时与 Executor 隔离；
- runtime 无法隔离时，不得声称它是暗卷；把它当明卷，或改用其他受保护 evidence。

暗卷失败表示现有 Goal 仍有未满足事实，不是执行结束后新增要求。

## 独立 evidence

当 Executor 自证无法形成可信判断、visible/private judge 仍可被操纵，或任务风险确实要求独立性时，可以让未参与实现的主体在权威环境中重新取得 evidence。

“独立”指没有实质参与实现，并重新面对 Goal、repo verification authority、基线和真实环境取得证据；是否使用相同模型或 provider 本身不能单独证明或否定独立性。

独立主体不是 Northstar 的固定角色，也不形成独立 Acceptance workflow。它只是一个条件性的 evidence source。需要的独立 evidence 暂时无法取得时，就准确报告 evidence gap，不能降级成 `PASS`。

## Verification granularity 仍然有效

可信度机制不改变正常验证粒度：

- Task 级 verification 证明局部行为；
- Task Group 级 verification 覆盖局部检查无法覆盖的组合行为、共享合同、迁移切片或汇合结果；
- Goal 级 verification 在相关工作收敛后证明本次明确交付。

低层 PASS 不能替代更高层实际需要验证的行为；验证成本只影响运行位置和频率，不影响是否需要验证。

## 非 PASS

Evidence 伪造、跳过、过期、coverage 不足、judge 被削弱、暗卷无法隔离却被当作私有证据，或独立 evidence 缺失时，都不能写成 PASS。

下一步只能是：取得新的有效 evidence、调整 Execution/Graph 后重新验证、如实阻塞，或回到 Human-owned 的 Goal/authority 决策边界。不要通过补写结论、降低标准或新增 completion/acceptance 术语把缺口覆盖掉。