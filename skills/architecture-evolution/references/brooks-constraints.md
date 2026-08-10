# Brooks Architecture Constraints

只在 Architecture Intent 已基本稳定、需要 challenge 当前判断时读取。Brooks 是可选 judgement lens；具体 architecture judgement 以 `rules.md` 为准。

只使用与当前 pressure 和 boundary 有 evidence 关系的约束：

- **R6 Domain Model Distortion** — 不能按现有代码形状错误统一真实不同的业务语义。
- **R2 Change Propagation** — 共同规则和 variation 的变化应收敛到权威位置。
- **R3 Knowledge Duplication** — 同一业务决定、配置解释或路径选择应只有一个权威来源。
- **R4 Accidental Complexity** — 新 abstraction 必须吸收真实变化并替代旧结构，不能只增加新的间接层。
- **R5 Dependency Disorder** — policy / contract / implementation 的依赖与控制方向应稳定，不能由底层隐式反向控制 policy。
- **R1 Cognitive Overload** — capability 应让 caller 少知道步骤、状态、顺序和实现类型。

用相关约束 challenge `rules.md` 已形成的 best-known judgement；反证成立就推翻或缩小 intent，否则不新增另一套 guard。

Brooks 只改变 judgement；最终 Intent 不输出 R1–R6、评分、proof 或 challenge 过程。
