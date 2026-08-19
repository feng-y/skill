---
name: architecture-evolution
description: 用于架构方向不清、历史模块持续演进或“下一刀改什么”：依据 repo identity、仓库现实、长期变化与约束做战略设计，形成当前最可信的目标结构，再从 reality / Target gap 中识别不超过 3 个高价值演进锚点，聚合同一战略修正并集中当前最值得推进的演进主线。
---

# Architecture Evolution · 战略设计与下一步演进

AE 的核心是战略设计：判断这个 repo / 系统长期应该由什么能力、责任和边界组成。当前 Program 是战略设计在现实上的集中演进主线，不是 Top Improvements backlog；不能用迁移成本、实现便利或局部压力反向定义 Target Architecture。用户决定业务、兼容和风险承诺；实现者决定具体代码。

## 流程

**1. 看方向与现实。** 从用户入口恢复会改变当前架构判断的 repo identity / architecture intent，并核对责任、依赖、权威、生命周期、公开边界和真实摩擦。当前形态或单一来源都不能定义 Target。Research 只为明确且会 materially 改变判断的 unresolved fork / Unknown 扩展；probe 必须能区分 material alternatives。Evidence 足够，或剩余 fork 已确认只能由 Human 取舍时就停止，复用已有 Evidence，不因新的 judgment pass 重扫 repo。

**2. 做战略设计。** 按下方“判断”形成 Target；当前 module / class / package 只是 reality。只有主判断与 bounded Evidence 后仍有会改变 Target 的 strategic fork、authority conflict 或 boundary discriminator，才读 [strategic-design.md](references/strategic-design.md)。

只有长期责任、边界、依赖、抽象或权威应变化，或长期 binding 的业务 / 质量 / 运行约束会实质改变这些结构时，才升级为架构问题；smell、一次性迁移、纯整洁或泛化的质量愿望都不够。剩余 material fork 若不是事实问题而是 Human-owned 的业务、兼容、风险、投入或 ownership 取舍，停止 research，返回 Evidence、best-known recommendation、真实选项和 decision surface。

**3. 找锚点并收敛当前 Program。** Target 先独立成立；现实与 Target 的 gap 只形成候选，不自动成为任务。先把 material observations 压缩成不超过 3 个当前最有价值的演进锚点，用来限制 attention 和比较 leverage，而不是生成 backlog。若多个锚点实际属于同一个 responsibility / authority correction，且分开推进会继续保留同一旧知识、旧权威、反向依赖、特殊路径或补偿性 guidance，就聚合成一条更完整但仍聚焦的演进主线；只有长期责任、语义、权威、生命周期或 structural gain / exit 真正独立时才保持分开。随后集中当前最值得推进的 Program，继续收敛它的责任、边界、依赖、structural done condition 和 real exit，直到形成足以独立改善 Target 的当前演进切面，或遇到必须由 Human 决定的 strategic choice。当前迁移成本、执行风险和收益只决定聚焦哪一刀、推进到哪里；没有值得立即改 repo 的内容时，可以只交战略设计结论。

**4. 交付。** 局部问题只给局部判断；缺关键事实或人的决定时，说明缺口与继续条件。收敛后完整给出当前 Strategic Design、必要的 Target 变化和当前 Program，并把同一正文写入仓库或工作区外的 Markdown 交接文件；其余仍独立的锚点只有在会改变当前判断时才保留，不作为默认 backlog。若获授权，稳定结论更新原 authoritative architecture source；否则交接文件不成为 repo SOT。Human decision / 实质修正后保留仍有效 Evidence / Target，只重算受影响判断；前提失效才重查对应部分，并完整重交付。写入失败就是阻塞。不要输出 `ready`、`completed`、`executable` 或 `status` 状态词。

## 判断

- **责任与边界。** 主要能力由 repo identity、领域语义、长期变化和已证明会塑造结构的 binding constraints 共同解释，不由当前目录名决定。一个 owner 应拥有并隐藏本能力长期稳定的设计知识 / 决定，并使相关知识、状态、行为、权威、生命周期和主要验证尽量闭合；调用方不重组这些私有事实。必要但通用的辅助关注点不能仅因复杂或高频变化而主导主要架构；若长期 binding 的质量 / 运行约束真实改变责任、生命周期、交互、部署或失败边界，则必须进入 Target。
- **关系与依赖。** 已有独立语义、权威来源、生命周期或长期约束的能力保持独立，不为内聚而吞并。只有会改变 Target 的跨边界关系才需要显式：例如权威归属、语义翻译、生命周期协同或隔离。责任与这些关系成立后，长期 dependency 必须能由真实 semantic / authority / lifecycle / failure relationship 解释；代码位置、调用便利、历史 ownership 或实现复用本身不构成理由。解释不了的 dependency 先作为 responsibility / knowledge ownership / boundary 需要重判的 Evidence，再收敛为少量稳定的单向依赖；稳定语义不依赖具体实现，长期边界优先由目录、模块、包、构建或工具直接约束。
- **差异与抽象。** 抽象稳定语义，不抽象表面相似。没有长期语义、契约、生命周期、性能架构或部署差异，不制造独立 provider / layer；真实差异也不强行统一。用户点名的分层、门面、提供者或注册表都只是候选手段。
- **Target。** Target 必须包含当前 Evidence 已足以支持、未来仍会复用且会改变后续判断的战略事实，同时保持最小充分：不把当前 reality 合理化成目标，也不为完整感预编尚无 Evidence 的 capability、provider、layer 或协作关系。
- **Program 与退出。** Program 必须把已确认的战略结论集中成一条当前值得推进的结构变化：责任更闭合、私有知识泄漏和不必要 coupling 更少、依赖 / 信息隐藏更稳定，并让对应旧知识、旧权威、反向依赖、特殊路径或补偿性 guidance 真实退出。多个候选若只是同一战略修正的不同表象，拆开后仍保留同一个旧 authority / path，就应聚合而不是并列；只新增 facade / registry / interface 而旧结构仍 authoritative，或只为未来改造搭脚手架，都不算 Architecture Improvement。

主要行为以及完成对应变化所需的关键判断，应尽量能从正确责任及其 authoritative sources 附近被理解、修改和验证；若长期必须跨无关责任重建 owner / authority / dependency / verification，或依赖隐含且不可稳定恢复的知识，这是边界或知识归属可能未闭合的 Evidence，不是单独为 agent 易读而重塑架构的理由。多个候选都成立时，优先让持续或已明确的未来变化及其关键判断少跨责任、权威、依赖和验证面；不能靠吞并真实独立责任、复制权威事实或隐藏跨边界语义制造这种局部性。

只有用户、仓库或上游权威来源，以及已验证的现实，才能绑定长期承诺或当前事实。架构文档是 Evidence / 稳定结论的持久化来源，不是不可挑战的 oracle。除非某种表示已被权威固定，AE 只规定架构结果和结构完成条件，不提前规定类、接口、文件、配置、调用形态、合并请求、任务拆分或测试工具。AE 默认围绕当前 Program 继续收敛；若被上游 shaping capability 调用，只返回 Evidence、方向和 Human decision surface，不接管提问。

## 按需读取

- [strategic-design.md](references/strategic-design.md)：主判断与 bounded Evidence 后仍有会改变 Target 的 strategic fork、authority conflict 或 boundary discriminator；
- [legacy-lenses.md](references/legacy-lenses.md)：旧模式、标记、配置、注册名或其他兼容身份能否退出会改变 Target / Program；
- [brooks-constraints.md](references/brooks-constraints.md)：候选结构已经说得通，但整体复杂度、第二系统或 complexity relocation 仍可疑。

## 发出前检查

1. Target 是否来自 repo identity、长期 Evidence 与结构约束，而不是当前 module / patch / 实现便利？
2. 演进锚点是否只是 attention funnel；同一战略修正是否已聚合，当前 Program 是否集中且产生 structural gain + real exit，而不是 Top Improvements backlog 或多一层结构？
3. 稳定结论是否归位到原 authoritative source，交付是否完整且不预定实现？