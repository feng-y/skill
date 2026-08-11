# Brooks Architecture Constraints

只在当前 architecture trade-off、complexity relocation 或 conceptual integrity 难以判断时读取。Brooks 是按需 judgement lens；具体 architecture decision 以 `rules.md` 为准。

只使用与当前 forces 和 boundary 有 evidence 关系的约束：

- **R6 Domain Model Distortion** — 不能按现有代码形状错误统一真实不同的业务语义。
- **R2 Change Propagation** — 共同规则和 variation 的变化应收敛到权威位置，而不是跨多个 owner 传播。
- **R3 Knowledge Duplication** — 同一业务决定、配置解释或路径选择应只有一个权威来源。
- **R4 Accidental Complexity** — 新 abstraction 必须吸收真实变化并替代旧结构；比较方案时要说明复杂度去了哪里。
- **R5 Dependency Disorder** — policy / contract / implementation 的依赖与控制方向应稳定，不能由底层隐式反向控制 policy。
- **R1 Cognitive Overload** — capability 应让 caller 少知道步骤、状态、顺序和实现类型。

这些约束用于区分 materially different architecture 的真实 trade-off，或推翻一个只是搬移 complexity 的方案；不要求逐项检查，也不形成独立阶段、评分或最终 section。

Brooks 只改变 judgement；最终 Architecture Decision 不输出 R1–R6、评分、proof 或 challenge 过程。
