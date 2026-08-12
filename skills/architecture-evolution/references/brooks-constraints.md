# Brooks Challenge Lenses

只在一个 architecture proposal 已经 plausible、但仍需要挑战 conceptual integrity、complexity 或克制性时读取。`SKILL.md` owns stable architecture judgment；本文件只提供反证 lens。

- **Conceptual Integrity** — 系统应由少量一致 design ideas 解释。一个局部合理的 feature、优化或 abstraction，如果要求 caller / maintainer 同时记住第二套概念、特殊规则或例外路径，就可能破坏整体结构。Conceptual integrity 不等于统一 implementation：stable specific variation 能被同一架构自然解释时应保留。
- **Essential vs Accidental Complexity** — 只有来自问题本身或当前必须满足的外部约束、无法通过改变 representation / organization 消除的复杂度才是 essential。历史 representation、重复解释、兼容残留或当前 provider/class/deployment 形状制造的 complexity 仍要被挑战；新 abstraction 只是包装 accidental complexity 时不算改进。
- **Second-System Effect** — 重设计容易把过去没做的 flexibility、extension point、mode、hook、registry、generic framework 一次补齐。没有当前长期 Evidence 就不物化，让未来真实 pressure 再证明新的 boundary。

Brooks challenge 只用于推翻“局部都合理、整体却更复杂”的 proposal；反证成立就缩小、替换或保持 unresolved，不为保住 proposal 增加新的 guard。最终 Program 不输出 Brooks 名称、评分或 challenge trace。
