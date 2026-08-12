# Verification Trust

只在 visible Verification 可能产生**具体且 material 的 false-green / gameability / independence 风险**时读取。正常 Verification scope、provider trigger、Evidence freshness/reuse 由 [execution-compile.md](execution-compile.md) 拥有；本文件只判断“这个 PASS 能不能信”。

## Trust question

没有 binding independence requirement 时只问：

> 是否存在一个具体 failure mode，使 Goal / required Verification 没有真正成立时，Executor 仍可能得到 visible PASS？

没有就停止增加 trust mechanism。一般 uncertainty、coverage 未完全展开或“多验一次更放心”都不是 trust gap。

常见 material gap 是：judge 没有真实观察目标；Executor 可以修改/绕过 oracle；固定样本可被针对优化；关键失败不能传播；决定性 Evidence 只能由实现者自报。

## Judge integrity

除非 Human/repo authority 明确允许且仍有等价可信证明，否则不得通过 skip/todo、放松断言或 coverage、删活体测试、mock 绕过真实对象、改阈值、吞失败传播或修改验收脚本制造 PASS。

关键 judge 可能空跑、假绿或静默失效时，可以制造一次受控局部失败确认失败信号，再恢复并运行正常 Verification。这个 reverse check 只证明 judge 能报错，不代替 Goal behavior Evidence。

## Additional trust Evidence

只有前面的具体 gap 能被额外观察反证时，才增加最小 trust Evidence：

- **isolated/private check**：从同一个公开 Goal / Verification requirement 推导，不增加隐藏要求；必须在执行前形成并保持隔离，否则按 visible check 计算；
- **independent Evidence**：关键 claim 不能由参与实现的同一推导链可信证明时，由未参与实现的主体在 authoritative environment 重新取证。是否使用相同模型/provider 本身不决定独立性。

这些不是固定 Acceptance workflow，也不要求每个任务都存在。必要 trust Evidence 拿不到时准确报告 evidence gap，不能降级成 PASS。
