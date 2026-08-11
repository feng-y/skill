# Brooks Challenge Lenses

只在一个 architecture proposal 已经 plausible、但仍需要挑战其 conceptual integrity、complexity 或克制性时读取。Brooks 只提供反证 lens；`rules.md` 仍是唯一 architecture judgement owner。

只展开与当前 decision 有真实关系的 challenge：

- **Conceptual Integrity** — 系统应由少量一致的 design ideas 解释。一个局部很好的 feature、优化或 abstraction，如果要求 caller / maintainer 同时记住第二套概念、特殊规则或例外路径，就可能破坏整体结构。优先 challenge Layering、Cohesion 和 Primary responsibility 是否仍由同一组概念解释。
- **Essential vs Accidental Complexity** — 稳定业务语义、真实 lifecycle / performance / deployment constraint 属于必须尊重的 essential complexity；由历史 representation、工具限制、重复解释、兼容残留或当前代码形状制造的 complexity 不应被永久 architecture 化。用它 challenge Abstraction vs specific 与 Real evolution：新 abstraction 若只是重新包装 accidental complexity，不算改进。
- **Second-System Effect** — 重设计最容易把过去没做的 flexibility、extension point、mode、hook、registry、通用框架和“顺便优化”一次补齐。除非当前 evidence 证明它们是长期 architecture requirement，否则优先克制：保留更少概念、更窄 public surface，让未来真实 pressure 再证明新的 abstraction / specific boundary。

Brooks challenge 的目的不是替 `rules.md` 再做一次完整 review，而是推翻“局部都合理、整体却更复杂”的方案。反证成立就缩小、替换或保持 unresolved；不要为保住 proposal 增加新的 guard。

最终 Architecture Decision 不输出 Brooks 名称、评分、challenge trace，也不要求逐项检查。