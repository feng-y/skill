# Verification / Evidence Trust

只在 Evidence trust / independence 可能改变 completion judgment 时读取。provider 是否真实运行、coverage 是否覆盖 claim、Evidence freshness / provenance / selective reuse 等正常语义由 [execution-compile.md](execution-compile.md) 负责；这里不再复制。

默认优先使用 repo 已有、受保护且足以覆盖 Goal 的 visible verification；不要为了“更严格”机械增加暗卷或独立 judge。

## Trust judgment

增加额外 trust mechanism 前先判断：**即使 visible verification 全部 PASS，Goal 或已触发 required Verification 是否仍可能 materially false 或未被覆盖？**

- 如果不能，visible Evidence 已足够；停止增加判卷机制。
- 如果仍可能，先指出使绿灯不足以判卷的具体原因，例如 judge 可能没有真实观察目标、Executor 可以控制或针对 oracle / 固定样本优化、由 Executor 自己推导的 coverage/scope 仍需要独立反证，或关键 Evidence 只能由实现者自报。然后只补足能反证该风险的最小 trust Evidence。

反向验证、暗卷和独立 Evidence 都只是修补这个 trust gap 的手段，不是新的 Goal、Acceptance 层或固定流程。

## 保护 judge 与 baseline

除非 Goal/Human authority 明确允许且仍保留等价可信验证，否则不得通过削弱断言、缩小 coverage、跳过测试、用 mock 绕开真实对象、降低阈值、吞掉失败传播或修改验收脚本来制造 PASS。

已有权威 baseline 被破坏就是回归，不因为实现更简单或成本更低而自动可接受。测试数、skip/todo、coverage、schema 或 replay baseline 只有在 repo 本身把它们当判卷标准时才冻结，不机械制造新指标。

## 反向验证

关键检查存在空跑、假绿或静默失效风险时，制造一次受控且局部的失败，确认失败信号真实出现；恢复后再运行正常 verification。反向验证只证明 judge 会正确发信号，不代替 Goal 行为本身的验证。

## 明卷 / 暗卷

**明卷**是 Executor 可见的 verification，也是默认路径。repo 的受保护测试、replay、CI、schema 或其他 judge 已足够时，不增加私有检查。

只有 Trust judgment 证明可见绿灯仍留下 material falsifiability gap，且隔离观察能实际缩小该 gap 时，才使用少量**暗卷**。它必须从同一个公开 Goal 和 Verification requirement 推导，可以换样本、scope derivation 或观察路径，但不能增加隐藏要求；如果要称为暗卷，就应在执行前形成并与 Executor 隔离。runtime 无法隔离时，把它当明卷或改用其他受保护 Evidence。

暗卷的价值来自对同一 claim 的独立反证能力，不来自数量。优先检查 visible path 可能遗漏的 coverage、material contradiction 或 shortcut，不为“多一层保险”重复明卷。

暗卷一旦在执行前泄露给 Executor，就不再提供 private-evidence 价值；可以继续作为明卷使用，但不能重复计算其独立性。

## 独立 Evidence

当 Executor 自证无法形成可信判断、visible/private judge 仍可被操纵，或关键 coverage / claim 只能由实现者自己的推导支撑时，可以让未参与实现的主体在权威环境中重新取得 Evidence。

“独立”指没有实质参与实现，并重新面对 Goal、repo verification authority、基线和真实环境取得证据；是否使用相同模型或 provider 本身不能单独证明或否定独立性。

独立主体不是 Northstar 的固定角色，也不形成独立 Acceptance workflow。需要的独立 Evidence 暂时无法取得时，准确报告 evidence gap，不能降级成 `PASS`。

## 非 PASS

Evidence 伪造、跳过、过期、coverage 不足、judge 被削弱、存在未解释的 material contradiction、只有不可复核总结、暗卷无法隔离却被当作私有 Evidence，或必要的独立 Evidence 缺失时，都不能写成 PASS。

下一步只能是取得新的有效 Evidence、调整 Execution/Graph 后重新验证、如实阻塞，或回到 Human-owned 的 Goal/authority 决策边界。不要通过补写结论、降低标准或新增 completion/acceptance 术语把缺口覆盖掉。
