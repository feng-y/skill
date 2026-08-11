# Architecture Decision Contract

只在 `Status: Architecture decision ready` 时读取。本文件只定义最终 Architecture Decision 的语义义务，不规定固定 Markdown 章节，也不要求输出内部 judgment taxonomy。

最终结果应让一个不了解本轮 Research 过程的人能够回答：**现在的结构为什么不再合适、目标架构为什么更好、若有真实 fork 为什么选它、旧架构如何真正退出。**

只保留 decision-relevant 内容：

- **Problem / Evidence** — 真实 pressure 与足以支撑判断的 decisive evidence；
- **Current structural issue** — 当前 layering/dependency、module cohesion、abstraction/specific 或 primary responsibility 中真正失衡的部分；`knowledge / SOT / control / lifecycle / variation` 仅在它们能解释结构问题时出现；
- **Alternatives** — 只在存在 materially different architecture fork 时出现。比较真正不同的长期结构与最重要 architecture cost，不为了格式制造多个方案；
- **Decision / Target Architecture** — 目标 layer / dependency、module responsibility、abstraction / specific boundary 与必要的长期 invariant；说明为什么它比仍可行 alternative 更符合当前 reality；
- **Evolution / Exit** — 先建立什么结构性 boundary / authority，哪些旧 knowledge / dependency / path 随后退出，temporary complexity 的 purpose / exit 是什么；不展开 implementation task list；
- **Boundary / Acceptance** — in/out scope、must-preserve，以及什么结构事实成立时可以认为 architecture evolution 完成。

Architecture Decision 可以选择 Target Architecture，但不能把 representation 冒充 architecture law。除非 Human/repo authority 或不可替代约束使其成为 invariant，否则不要固定具体 class/API/file、helper、flag/metadata schema、虚函数形式、调用实现、migration task 或 lint/test/verification provider。

若存在 materially different architecture 且当前 evidence 不足以裁决，不输出 ready decision；返回 `Status: Architecture unresolved` 并指出真正会改变选择的缺口。

标题、组织方式和正文跟随用户主要语言；`Status` token、代码符号、文件名和稳定协议名称可保留原文。不要输出五项 judgment 清单、Brooks 名称、评分表或 reasoning trace。
