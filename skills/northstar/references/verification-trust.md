# Verification / Evidence Trust

只在普通 repo verification 可能假通过、可被针对性优化、静默失效，或结果确实需要额外独立性时读取。默认优先使用 repo 已有、受保护且足以覆盖 Goal 的 verification；不要为了“更严格”机械增加暗卷或独立 judge。

## Evidence trust

- **先证明 judge/provider 真能工作。** 文档里的命令、脚本名和 CI 入口都只是声明；Handoff 正确性依赖且能提前实测时就实测，必须进入执行环境后才能确认、并且在主要修改前确认能显著降低 false-green 或错误路线风险时才放进 Task 0，其余在真正使用时验证。不存在、空跑或不会传播失败的检查不能产生有效 Evidence。
- **覆盖真实 claim。** build、lint、coverage、活动记录或局部测试只有在确实覆盖当前要判断的行为时才有证明力；provider 不能证明覆盖范围之外的事实。
- **跟真实 affected surface 走。** verification scope 根据实际 change surface、effective binding/config 和真实 consumer/target 决定，不因 cleanup/refactor 或预期 `0-diff` 主观降级。
- **前提仍然成立。** 版本、环境、对象、binding/config 或上游行为变化可能影响原证据时，该 Evidence 失效；未被影响的 Evidence 可以复用。
- **判卷标准不能偷改。** 除非 Goal 明确要求且仍保留等价可信验证，否则不得削弱断言、缩小 coverage、跳过测试、用 mock 绕开真实对象、降低阈值、吞掉失败传播或修改验收脚本来制造 PASS。
- **基线不能无授权倒退。** 已有权威 baseline 被破坏就是回归，不因为实现更简单或成本更低而自动可接受。测试数、skip/todo、coverage、schema 或 replay baseline 只有在 repo 本身把它们当判卷标准时才冻结，不机械制造新指标。

## Evidence 要可判卷

Executor 的 `PASS`、总结、截图式描述或“应该通过”不是 Evidence。关键 Evidence 至少要能回答：**跑了什么、对什么对象/版本/配置跑、结果是什么、原始输出或可复现入口在哪里。**

判断方能访问真实 repo/runtime 时，对最终结论关键且成本合理的 repo-authoritative verification 应直接重新取证，而不是只信 Executor 的摘要；不要求机械重跑每个已经充分且仍有效的 Task-local check。

判断方摸不到执行环境时，Evidence 必须随交付携带足够 provenance：实际 command/probe、target/revision、关键 config/binding、exit/verdict，以及机器可判的原始输出或稳定 artifact/reference。只有无法复核的二手总结时，准确标为 evidence gap，不把它提升成 PASS。

## 反向验证

关键检查存在空跑、假绿或静默失效风险时，制造一次受控且局部的失败，确认失败信号真实出现；恢复后再运行正常 verification。反向验证只证明 judge 会正确发信号，不代替 Goal 行为本身的验证。

## 明卷 / 暗卷

**明卷**是 Executor 可见的 verification，也是默认路径。repo 的受保护测试、replay、CI、schema 或其他 judge 已足够时，不增加私有检查。

只有 visible judge 可以被针对性优化、实现者能轻易迎合固定样本，或公开验证不足以形成可信判断时，才使用少量**暗卷**：它必须从同一个公开 Goal 和 Verification requirement 推导，可以换样本或观察路径但不能增加隐藏要求；如果要称为暗卷，就应在执行前形成并与 Executor 隔离。runtime 无法隔离时，把它当明卷或改用其他受保护 Evidence。

暗卷一旦在执行前泄露给 Executor，就不再提供 private-evidence 价值；可以继续作为明卷使用，但不能重复计算其独立性。

## 独立 Evidence

当 Executor 自证无法形成可信判断、visible/private judge 仍可被操纵，或任务风险确实要求独立性时，可以让未参与实现的主体在权威环境中重新取得 Evidence。

“独立”指没有实质参与实现，并重新面对 Goal、repo verification authority、基线和真实环境取得证据；是否使用相同模型或 provider 本身不能单独证明或否定独立性。

独立主体不是 Northstar 的固定角色，也不形成独立 Acceptance workflow。需要的独立 Evidence 暂时无法取得时，准确报告 evidence gap，不能降级成 `PASS`。

## 非 PASS

Evidence 伪造、跳过、过期、coverage 不足、judge 被削弱、只有不可复核总结、暗卷无法隔离却被当作私有 Evidence，或必要的独立 Evidence 缺失时，都不能写成 PASS。

下一步只能是取得新的有效 Evidence、调整 Execution/Graph 后重新验证、如实阻塞，或回到 Human-owned 的 Goal/authority 决策边界。不要通过补写结论、降低标准或新增 completion/acceptance 术语把缺口覆盖掉。
