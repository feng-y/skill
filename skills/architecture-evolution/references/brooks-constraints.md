# Brooks Architecture Constraints

只在 Architecture Intent 已基本稳定、需要 challenge 当前判断时读取。Brooks 是 judgement lens，不是输出模板、评分器或独立报告。

只使用与当前 pressure 和 boundary 有 evidence 关系的约束：

- **R6 Domain Model Distortion** — 不能按现有代码形状错误统一真实不同的业务语义。
- **R2 Change Propagation** — 共同规则和 variation 的变化应收敛到权威位置。
- **R3 Knowledge Duplication** — 同一业务决定、配置解释或路径选择应只有一个权威来源。
- **R4 Accidental Complexity** — 新 abstraction 必须吸收真实变化并替代旧结构，不能只增加 facade/manager/registry/mode flag。
- **R5 Dependency Disorder** — policy / contract / implementation 的依赖与控制方向应稳定，不能由底层隐式反向控制 policy。
- **R1 Cognitive Overload** — capability 应让 caller 少知道步骤、状态、顺序和实现类型。

## Challenge

用相关约束问当前 intent：

- 复杂度是真的减少，还是搬到了 helper、adapter、registry、config 或 caller？
- caller / consumer knowledge 是否真的下降？
- 是否错误统一了不同 bounded context？
- ownership 是否扩大到 evidence 不支持的 execution / orchestration 或相邻 subsystem？
- 新 abstraction 是否有真实 replacement / exit？
- dependency direction 是否更稳定，而不是更隐蔽？

反证成立就 reject 或缩小 intent；否则只保留真正影响 direction / boundary 的 guard。

## Guards

- 相似规则不自动属于同一 bounded context；
- vendor adapter 可以合法吸收外部 churn；
- composition root 可以知道 implementation，但不能承载业务 policy 或 runtime usage knowledge；
- capability ownership 不自动包含 request execution / orchestration；
- 相邻 subsystem 已有正确 owner 时优先稳定 relation/contract；
- 简单 DTO、record、线性实现不因“简单”成为问题；
- 深模块内部可以复杂，关键是复杂度不要泄漏给 caller；
- 迁移期双轨可以暂时存在，但必须有 authoritative path 和退出条件。

## Boundary

Brooks 只改变 Architecture Evolution 的 judgement；最终 Intent 不输出 R1–R6、Risk/Guard/Proof 表、PASS/RETRY、Health Score 或 challenge 过程。
