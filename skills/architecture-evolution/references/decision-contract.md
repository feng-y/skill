# Architecture Decision Contract

只在 `Status: Architecture decision ready` 时读取。本文件只定义最终 Architecture Decision 的语义义务，不规定固定 Markdown 章节。

最终结果应让一个不了解本轮 Research 过程的人能够回答：为什么这是 architecture problem、当前 architecture 的关键力量和关系是什么、有哪些 materially different 的选择、为什么选当前方向、目标 architecture 长期固定什么、系统如何在 architecture 层面演进过去。

只保留 decision-relevant 内容：

- **Problem / Forces** — 真实 change pressure、决定性 evidence，以及哪些 stable constraints 真正驱动 architecture decision；
- **Current architecture model** — 与判断有关的 responsibility、authority/SOT、knowledge、control/lifecycle、dependency、variation 与 change-pressure 关系；不输出无关 inventory；
- **Alternatives** — 只在存在真实 design-space fork 时出现。说明 materially different 的 architecture axis、各自最重要的收益与 architecture cost；不为了格式制造多个方案；
- **Decision / Target Architecture** — primary direction、长期 boundary/invariant、authority/knowledge/control/lifecycle/dependency/essential variation 归属，以及为什么它比仍可行的 alternative 更符合当前 forces；
- **Evolution** — architecture-level transition：需要先建立什么 authority/boundary，什么旧 knowledge/control/path 随后退出，temporary complexity 的 purpose/exit，以及关键 reversibility/lock-in；不展开 implementation task list；
- **Boundary / Acceptance** — in/out scope、must-preserve、真正 replacement/exit，以及 outcome-level architecture acceptance。

Architecture Decision 可以选择 Target Architecture，但不能把 representation 冒充 architecture law。除非 Human/repo authority 或不可替代约束使其成为 invariant，否则不要固定具体 class/API/file、helper、flag/metadata schema、虚函数形式、调用实现、migration task 或 lint/test/verification provider。

若存在 materially different architecture 且当前 forces 不足以裁决，不输出 ready decision；返回 `Status: Architecture unresolved` 并指出真正会改变选择的缺口。

标题、组织方式和正文跟随用户主要语言；`Status` token、代码符号、文件名和稳定协议名称可保留原文。不要输出 taxonomy、Brooks 名称、评分表或 reasoning trace。
