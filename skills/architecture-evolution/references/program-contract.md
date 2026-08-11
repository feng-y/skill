# Architecture Program Contract

只在 `Status: Architecture decision ready` 时读取。本文件定义 AE 的 Compile 结果：把完整 architecture reasoning 压成一个可继续设计/执行、但不需要下游重新发现架构 why 的薄 Architecture Program。它不规定固定 Markdown 章节，也不输出内部 judgment taxonomy。

最终结果应让一个不了解本轮 Research 过程的人能够回答：**结构要变成什么、长期保持什么、接下来哪几个 architecture improvement 最值得真实推进、它们有什么依赖、完成后什么旧复杂度退出。**

只保留会约束后续架构变化或推进顺序的内容：

- **Structural adjustment** — 用最小 current → target 对比说明 layer/dependency、module/capability boundary、abstraction/specific 或 primary responsibility 要发生什么结构变化；不复述文件 inventory。
- **Long-term architecture** — 少量长期必须成立的 boundary / invariant，说明未来需求来了以后系统仍应保持什么结构；只保留稳定方向，不写未来可能性清单。
- **Top Architecture Improvements** — 最多 3 个；不足 3 个不补数。优先保留能减少最多跨边界 knowledge/dependency/accidental complexity、或解除后续结构性阻塞的 improvement，而不是实现最容易或描述最宏大的项。每个 improvement 都必须是一个真实可推进的 bounded architecture outcome，而不是 research question、knowledge task、愿望或实现步骤。
- **Route** — 只表达 improvements 之间真实的 architecture dependency：为什么 B 必须在 A 的结构事实成立后才能推进。没有 dependency 就允许并行；不制造 roadmap ceremony。
- **Boundary / completion** — 整体 in/out scope、must-preserve，以及完成这些 improvement 后什么结构事实成立、什么旧结构不再 authoritative。

每个 Architecture Improvement 必须同时回答四件事：

1. **Structural change** — 哪个长期 layer / dependency / responsibility / abstraction / provider boundary 会改变；
2. **Architecture gain** — 它明确改善哪个核心判断：layering、cohesion/simplicity、abstraction vs specific、primary responsibility 或 real evolution；
3. **Real exit** — 哪个旧 knowledge / authority / dependency / special path / accidental complexity 会真实退出或停止 authoritative；
4. **Done condition** — 用结构事实说明何时完成，不固定 test/lint/evidence provider。

如果一个候选项只有“研究 / 确认 / 梳理 / 观察 / 收集数据”，或完成后结构没有确定变好，它不能进入 Top Improvements。若缺失 evidence 会决定该 change 到底是不是 improvement、会改变 Target Architecture 或推进顺序，则不能靠 Compile 隐藏它：返回 `Status: Architecture unresolved`。

Compile 应删除 Research trace、完整 alternatives 论证、Brooks challenge 过程、普通 unknown、看过的文件列表和 implementation detail。只有某个被否决 alternative 的代价会约束后续设计时，才保留一句必要 decision rationale。

Architecture Program 可以固定 Target Architecture 与 architecture-level improvement outcome，但不能把 representation 冒充 architecture law。除非 Human/repo authority 或不可替代约束使其成为 invariant，否则不要固定具体 class/API/file、helper、flag/metadata schema、虚函数形式、调用实现、MR/task split 或 lint/test/verification provider。

标题、组织方式和正文跟随用户主要语言；`Status` token、代码符号、文件名和稳定协议名称可保留原文。不要输出五项 judgment 清单、Brooks 名称、评分表或 reasoning trace。
