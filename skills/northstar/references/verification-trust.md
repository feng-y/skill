# Verification / Evidence Trust

只在 Evidence trust / independence 会改变 completion judgment 时读取。provider 可执行性、claim coverage、Evidence freshness / provenance / reuse 等正常语义仍由 [execution-compile.md](execution-compile.md) 负责。

默认使用 repo 已有、受保护且足以覆盖 Goal 的 visible verification；Human 或 repo verification authority 明确要求独立验证时，该要求保持 binding。

## Trust judgment

没有 binding independence requirement 时，只问一个问题：**是否存在一个具体且 material 的 failure mode，使 Executor 在 Goal 或 required Verification 没有真正成立时，仍可能得到 visible PASS？**

没有就停止增加判卷机制；有就先说清 failure mode，再只补能反证它的最小 trust Evidence。典型原因是 judge 没有真实观察目标、Executor 可以修改或针对 oracle / 固定样本优化、关键 coverage/scope 只依赖实现者自己的推导，或决定性 Evidence 只能由实现者自报。一般 uncertainty 不是 trust gap；coverage / scope 本身仍归 execution compile 判断。

## Judge integrity

除非 Goal/Human authority 明确允许且仍保留等价可信验证，否则不得通过削弱断言或 coverage、skip、mock 绕过真实对象、降低阈值、吞掉失败传播或修改验收脚本制造 PASS。已有权威 baseline 被破坏就是回归；测试数、coverage、schema、replay baseline 等只有 repo 本身把它们当 judge 时才冻结。

关键 judge 可能空跑、假绿或静默失效时，制造一次受控局部失败确认失败信号，恢复后再运行正常 verification。反向验证只证明 judge 有效，不代替 Goal 行为验证。

## 明卷 / 暗卷

**明卷**是 Executor 可见的 verification，也是默认路径。只有 Trust judgment 已指出可由隔离观察反证的 failure mode，或 binding authority 本身要求私有检查时，才使用少量**暗卷**。

暗卷必须从同一个公开 Goal / Verification requirement 推导，不增加隐藏要求；要获得 private-evidence 价值，就应在执行前形成并与 Executor 隔离。可以换样本、scope derivation 或观察路径，但必须针对那个具体 gap；数量本身不增加 trust。无法隔离或提前泄露后，只能按明卷计算。

## 独立 Evidence

当 Executor 自证不足、visible/private judge 仍可被操纵、关键 coverage / claim 只由实现者自己的推导支撑，或 binding authority 明确要求独立取证时，可以由未参与实现的主体在权威环境中重新取得 Evidence。独立性来自未参与实现并重新面对 Goal、repo authority、baseline 和真实环境；是否使用相同模型或 provider 本身不能证明或否定独立性。

独立主体不是固定角色，也不形成 Acceptance workflow。必要的独立 Evidence 暂时拿不到时准确报告 evidence gap，不能降级成 `PASS`。

## 非 PASS

Evidence 伪造、跳过、过期、coverage 不足、judge 被削弱、存在未解释的 material contradiction、只有不可复核总结、暗卷失去隔离却被当作私有 Evidence，或必要独立 Evidence 缺失时，都不能 PASS。

下一步只能取得新的有效 Evidence、调整 Execution/Graph 后重新验证、如实阻塞，或回到 Human-owned Goal/authority 决策边界；不要靠补写结论、降低标准或新增 completion/acceptance 术语覆盖缺口。
