# Northstar / AE 改进方案

版本：v2（两轮方案评审后；本轮 runtime 修改尚未开始）
日期：2026-09-09
基线：`48c200f6c336ed1480f11dd67a1bbab2ccdbc605`；待修订候选：PR #88 / `cef07470eada1bde03e623ff5d0fc634c5b44c7c`。

## 目标与范围

Northstar 保证接住的是当前有效意图，澄清会改变选择的歧义，需要交接时不丢失问题、关键理由、承诺和验收边界。AE 在这些约束内承担战略技术判断，证明责任与知识应如何归位，以及什么 Evidence 会证实或推翻候选结构。它们不是一条强制流水线。

Goal 保留为 accepted outcome 的语义，不规定独立 Goal 文档、标题或阶段。Northstar 以 Intent take（含必要 shaping）为核心；Intent compile 与独立 outcome judgment 分别防止交接损失、虚假完成。AE 保留 Target 与 Program 的区别，不用当前迁移便利重定义长期目标。

本轮不新增 Skill、调度器、平台、持久化协议或语言副本；不改 RDR、Unknowns First、根 AGENTS.md、评分脚本与未合入 PR #82。不合并 PR，最终只给合入意见。

## 研究依据与取舍

外部材料提供设计依据，不构成模型行为改善的实验。以下一手资料于本轮重新读取；Google 的完整白皮书只沿用此前转录本理解，这里引用共同作者的原始说明，不声称核验了完整原 PDF。

| 来源 | 吸收 | 不照搬 |
| --- | --- | --- |
| [Anthropic SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook)，Plan / Design / Build / Legacy SOT | 保留问题、理由和约束；下游对照上游；一个事实使用一个权威来源。 | 不把原文的 intent/spec/plan 文件链、plan approval 改成所有任务的固定流程；原文确实主张 accepted plan，不能说它取消计划或审批。 |
| [OpenAI engineering-team guide](https://cdn.openai.com/business-guides-and-resources/building-an-ai-native-engineering-team.pdf)，印刷页 5、13、15（已看页面图） | 可委派分析不等于转移承诺责任；验收对应功能意图；多轮 review 修复具体缺陷。 | 不把人的最终责任解释成 AE 不能作技术判断；不把 Design 中的 UI 原型全部映射成战略架构。 |
| [Addy Osmani / Google 白皮书共同作者](https://addyosmani.com/blog/new-sdlc-vibe-coding/)，Context / Verification / Phases | 按需上下文；产物与执行轨迹分开评价；原型可用来澄清意图。 | 不引用模型/harness 百分比或效率倍率作为本项目证据；不把字数减少当质量收益。 |
| [LangChain ADLC](https://www.langchain.com/blog/the-agent-development-lifecycle)，Test / Monitor / Iterate | 同一输入比较版本，记录实际行为与修正，按责任归因。 | 不为此引入评分平台；规则已有而模型没遵守，不再追加同义规则。 |

## 基线判断

Northstar 已有 means/outcome 判定、Human choices、Grill、条件性 specialist / prototype、bounded research、真实 Graph 和独立验收。本轮不把它们宣称为新增能力。实际契约缺口是：root 以可执行交接作为通用停止点，shaping-only 的完整交付不够清楚；交接只强调 Goal/constraints，未明确保留会改变选择的问题与理由。

AE 已有 material alternatives、决定性证据、重开条件、representative-change challenge 和 real exit。改进不是增加架构原则，而是让已形成的技术决定可被下游消费；避免“未定业务承诺”阻止可独立回答的条件性技术分析，避免正式 Goal 文件成为入口要求。

当前对话中的过度建设是可见助手错误，但不能据此宣称 Northstar 被实际加载并导致了该错误。它只为 eval 提供输入区别；runtime 更改依据用户本次职责要求、仓库既有契约和上述公开方法。

## 拟定改动

### N — 意图与交接

1. 从原始表达中保留 problem / why / obligation、预期结果和当前委托范围，事实、假设与 Human 承诺不混写；只保留能改变判断的内容，不加必填模板。
2. shaping-only 返回当前意图或真实 decision surface；当前委托需要执行时直接形成可用约定，不要求用户额外说“交接”。Northstar 不接管实现，但宿主不能把该职责边界当作中止已授权端到端工作的理由。无新承诺不额外询问，不以初稿完成为停止点。
3. 交接前检查两类真实缺口：严格完成合同仍未解决原问题，或合同偷偷增加范围/承诺。用已有 Intent compile / Verification 语义承接，不创建新阶段。
4. cross-session 交接要让下一位读者恢复关键意图；引用原 authority，下游无法访问原上下文时在同一 Taskbook 保留最小必要信息及出处。必要 authority 本身无法核实时显式保留缺口，不伪造批准。保留的是决定性意图，不是完整聊天、设计推理或第二份 decision SOT。

### A — 架构判断与协作

1. 接受已有 intent、issue、Goal 或 scope；只需足以回答当前结构问题的内容。未决承诺下可回答带显式假设的技术问题，不能借此自动承诺投入。
2. 已有结构判断成立后，保留会被下游复用的决定性 Evidence 与必要重开条件；不要求凑备选、写 ADR 或重复战略设计。
3. 保留 no-evolution 判断、Target/Program 区分、真实独立责任、稳定 variation/依赖、structural gain/real exit 和 authority-bound representation。
4. 基于 main 做聚焦修改，替换旧 #88 的大范围 root 重写；AE 只调整入口、条件咨询和决定性证据的交付连接，保留原有战略判断主体。YAML 回到薄调用入口；不设字节数目标，也不为压缩删除真实 discriminator。

### E — 验证

冻结六类对照（用具体 prompt 和固定事实卡，不只列抽象标题）：评估 vs 实施；无 Goal 标题的清楚意图；实验 vs 已有义务；局部 bug vs 长期知识泄漏；局部 green vs real exit；实现/结构/意图/环境的反馈区别。每类明确输入、oracle、可观察的拒绝条件。

保留原 Northstar / AE 回归要求。原有“两项连续能力/直接 handoff”等检查仅适用于执行请求，明确 shaping-only 交付不构成未完成，避免 runtime 与 eval 相互矛盾。包装检查包括 YAML、链接、normal-runtime 不引用 eval、路径范围和远端 blob 一致性。场景契约 review 与 clean-session 行为评估分开记录；不存在实际运行就不产生分数、transcript 或成功率。

## 顺序与完成条件

本方案先经过两轮 review：第一轮检查职责/范围/authority，第二轮挑战上下游契约与验证设计。修正方案后才实施。实现第一轮审查实际 diff 与引用的一致性，第二轮用正反场景挑战边界；出现新修复再定向复核，不机械全量重跑。

最终产物：更新同一个 PR #88；提供方案、各轮问题及处理结果、验证依据和合入意见。能够合入表示当前审查未发现阻塞缺陷，不表示已证明跨任务的行为提升。


## 方案评审记录（实施前）

两轮均由当前主 Agent 进行不同角度的审查；不是独立模型实验或外部 reviewer 批准。

| 轮次 | 发现 | 处理与结论 |
| --- | --- | --- |
| Plan R1：职责/授权 | “需要交接时才 compile”可能变成等待用户另说交接，或让宿主在任务书后提前停止。 | 以当前委托所需的产出判定；明确 Northstar 不执行不等于宿主不推进。保留本次只给合入意见的边界。 |
| Plan R1：最小改动 | 旧 #88 重写 AE 全文，但 alternatives/reopen/real exit 已在 main，不能当新增能力。 | 选 main-based 聚焦补丁，不把全文压缩当履职改善；原战略主体与独立判卷保留。 |
| Plan R1：权威 | “原始问题溯源”可能扩大为每次重读所有聊天、复制架构理由。 | 只保留会改变判断的意图和出处；有具体冲突才回查；不新增 decision SOT。 |
| Plan R2：验证口径 | 六个场景标题还不能复现；静态检查容易被写成模型通过。 | 交付固定事实与 exact prompt 的正反探针；人工契约 review、包装检查、真实行为结果分栏，未运行保持 not run。 |
| Plan R2：全链一致 | 原有 root/reference/eval 默认围绕 executable Taskbook，shaping-only 可能被旧回归误判。 | 实现 review 必查停止条件、reference routing、outcome context 和对应 validation，而不只改 description。 |
| Plan R2：合入标准 | “能合入”与“提高成功率”容易被混为一谈。 | 合入意见依据实际 diff/契约和包装证据；无 clean-session 证据不宣称运行收益，不制造质量分数。 |

结论：上述修正后方案可进入实施；未授权的新平台、自动合并、独立 Goal 产物和全量 AE 重写均排除。
