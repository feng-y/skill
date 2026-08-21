---
name: architecture-evolution
description: 给定一个目标、几个关联目标或一个需要演进的模块，依据 repo identity、仓库现实和长期约束识别这些目标施加的真实架构压力，推导能更好吸收当前与同类未来变化的 AI-native Target Architecture，再从 reality / Target gap 中收敛当前最值得推进的结构演进。重点是让责任和知识更内聚、跨边界 coupling 更少，只在真实 variation 需要时隔离内部变化，长期依赖保持稳定且可解释的单向关系，并让主要变化可以在正确 owner 附近理解、修改和验证；不把高内聚低耦合当脱离目标的通用重构口号。
---

# Architecture Evolution · Goal 驱动的 AI-native 架构演进

AE 的核心是战略设计：**给定一个或多个相关 Goal，判断系统结构应该怎样演进，才能让这些 Goal 以及已经有 Evidence 支持的同类未来变化，在正确责任边界内更容易被理解、修改和验证。** 当前 Program 是这个 Target 在现实上的集中演进主线，不是 Top Improvements backlog，也不是 implementation plan。

AI-native 优化不是单独追求“模块更小”“层次更多”或 dependency 数更少。高内聚、低耦合、责任清晰、稳定契约、内部变化隔离、单向依赖和局部可验证，只有在它们真实缩小 Goal 所要求的长期 judgment / change / verification surface 时才有价值；不能吞并真实独立责任、复制 authority，或用新 facade / provider / layer 隐藏仍然存在的旧知识和旧路径。用户决定业务、兼容和风险承诺；实现者决定具体代码。

如果输入点名一个 module / package / subsystem，把它作为当前 scope 与 reality 入口，不默认它就是 Target boundary。若输入给出多个 Goal，只有它们共享 material architecture pressure，或它们涉及的 capability / boundary / dependency 必须协同设计才能正确满足 Goal 时才共同形成一个 Strategic Design；彼此没有共同结构前提的 Goal 不为了“统一架构”强行合并。

## 流程

**1. 看 Goal、变化压力与现实。** 从用户或上游已经成立的 Goal 开始，恢复会改变当前架构判断的 repo identity / architecture intent，并核对责任、依赖、权威、生命周期、公开边界和真实摩擦。AE 不重新做需求 shaping；如果不同 Goal 解释会 materially 改变业务结果、长期承诺或 owner，而 reality 无法决定，就返回 decision surface，不自行猜。

对每个 Goal 只追问架构上有决策价值的问题：它要求系统新增、替换、扩展或独立演进什么能力？同类变化现在需要哪些 owner 同时理解 / 修改 / 验证？哪些长期 binding 的兼容、性能、隔离、部署或 failure constraints 会改变责任或边界？把这些回答压成 **change pressure**，而不是把 Goal 翻译成 file / class / task list。当前形态或单一来源都不能定义 Target。Research 只为明确且会 materially 改变 Target / Program 的 unresolved fork / Unknown 扩展；probe 必须能区分 material alternatives。Evidence 足够，或剩余 fork 已确认只能由 Human 取舍时就停止，复用已有 Evidence，不因新的 judgment pass 重扫 repo。

**2. 做战略设计。** Target 从 Goal pressure + repo identity + verified reality 推导，不从当前 module shape、设计 pattern 或实现便利反推。以下关系是一个 judgment chain，不是新的 lifecycle / 固定模板：

- **Goal pressure → capability / responsibility。** 先判断为了吸收这些变化，哪个长期能力应该拥有决定和知识；不能直接从 Goal 跳到“新建模块”。
- **responsibility → module boundary / cohesion。** 一个长期 owner 应让同一变化原因所需的 knowledge、state、behavior、authority、lifecycle 和主要 verification 尽量闭合，并隐藏不该由 caller 重组的私有设计决定。多个相关 Goal 若持续要求同一组 owner 共同重建同一知识，这是 boundary 可能错误的 Evidence；真实独立语义 / authority / lifecycle 仍保持独立。
- **boundary → internal layering。** 只有 owner 内部存在稳定语义与可独立变化的实现、provider、storage/runtime adapter、lifecycle 或其他长期变化边界时才分层；分层的作用是让变化停在正确位置，不是形成 `interface/domain/provider/infrastructure` 的固定模板。没有稳定 variation 就不制造 layer / provider。
- **boundary → dependency direction。** 能力和 owner 先成立，再把长期 dependency 收敛到能由真实 semantic / authority / lifecycle / failure relationship 解释的少量稳定单向关系。caller 应依赖 owner 的稳定语义 / contract，而不是其具体实现或内部知识；单向依赖不能挽救错误的 capability decomposition。
- **Target → AI-native locality。** 用代表性 Goal / future change 挑战 Target：正确 owner 是否能在自身边界附近理解主要设计决定、完成 material change、取得关键 Verification Evidence？如果仍长期需要跨无关责任、authority、dependency 和 verification surface 重建同一私有知识，Target 还没有真正提高内聚或降低 coupling。

只有长期责任、边界、依赖、抽象或权威应变化，或长期 binding 的业务 / 质量 / 运行约束会实质改变这些结构时，才升级为架构问题；smell、一次性 migration、纯整洁或泛化的“高内聚低耦合”愿望都不够。只有主判断与 bounded Evidence 后仍有会改变 Target 的 strategic fork、authority conflict 或 boundary discriminator，才读 [strategic-design.md](references/strategic-design.md)。

剩余 material fork 若不是事实问题而是 Human-owned 的业务、兼容、风险、投入或 ownership 取舍，停止 research，返回 Evidence、best-known recommendation、真实选项和 decision surface。

**3. 找锚点并收敛当前 Program。** Target 先独立成立；现实与 Target 的 gap 只形成候选，不自动成为任务。先把 material observations 压缩成不超过 3 个当前最有价值的演进锚点，用来限制 attention 和比较 leverage，而不是生成 backlog。

若多个锚点实际属于同一个 responsibility / authority correction，且分开推进会继续保留同一旧知识、旧权威、反向依赖、特殊路径或补偿性 guidance，就聚合成一条更完整但仍聚焦的演进主线；只有长期责任、语义、权威、生命周期或 structural gain / exit 真正独立时才保持分开。

当前 Program 应描述**结构迁移**而不是 implementation steps：哪些 responsibility / knowledge / authority 要归位，哪个 boundary 要建立或退出，哪个 dependency 要改向，哪些内部 variation 应被 owner 吸收，哪些旧 authority / special path / reverse dependency 必须真正消失，以及用什么 architecture / behavior Evidence 证明目标结构成立。它可以有多个有真实 dependency 的 structural cuts，但不预定 file、class、API、patch 顺序或 test provider。当前迁移成本、执行风险和收益只决定聚焦哪一刀、推进到哪里；没有值得立即改 repo 的内容时，可以只交战略设计结论。

**4. 交付。** 局部问题只给局部判断；缺关键事实或人的决定时，说明缺口与继续条件。收敛后完整给出：

- 当前 Goal / Goal set 产生的 architecture change pressure；
- 与 Goal 直接相关的 current architecture constraint，而不是完整 repo inventory；
- 当前最可信的 Target Architecture，包括必要的 capability / module boundary、cohesion、internal variation / layering 与 dependency direction；
- 当前 Program 的 structural moves、real exit 与 migration boundary；
- 用来证明 AI-native 改善成立的 architecture / behavior Evidence，例如 responsibility 是否闭合、旧 dependency 是否退出、代表性变化是否减少跨无关 owner 的 judgment / change / verification surface。

把同一正文写入仓库或工作区外的 Markdown 交接文件；若获授权，稳定结论更新原 authoritative architecture source，否则交接文件不成为 repo SOT。Human decision / 实质修正后保留仍有效 Evidence / Target，只重算受影响判断；前提失效才重查对应部分，并完整重交付。写入失败就是阻塞。不要输出 `ready`、`completed`、`executable` 或 `status` 状态词。

## 判断

- **Goal 与变化压力。** Goal 本身不是 architecture instruction。AE 只把当前 Goal、approved roadmap、durable change pressure 和长期 binding constraints 中会改变 responsibility / boundary / dependency / lifecycle 的部分编入 Strategic Design。一次性 implementation inconvenience 不制造长期架构。
- **责任、模块与内聚。** 主要能力由 repo identity、领域语义、Goal pressure、长期变化和已证明会塑造结构的 binding constraints 共同解释，不由当前目录名决定。一个 owner 应拥有并隐藏本能力长期稳定的设计知识 / 决定，并使相关知识、状态、行为、权威、生命周期和主要验证尽量闭合。高内聚不是“所有相关代码放一起”，而是同一长期变化原因尽量不要求 caller 或其他 owner 重建本应私有的知识。
- **内部变化与分层。** layering / provider / adapter 只有在 owner 内部存在可独立变化且需要稳定隔离的语义或实现边界时成立。真实 variation 应被正确 owner 吸收；没有 stable variation 不增加层次，真实独立 capability 也不能被“内聚”吞进模块内部。
- **关系与依赖。** 已有独立语义、权威来源、生命周期或长期约束的能力保持独立。只有会改变 Target 的跨边界 authority、语义翻译、生命周期协同 / 隔离或 failure propagation 才显式建模。责任与关系成立后，长期 dependency 必须能由这些事实解释，并尽量依赖稳定 contract / semantics 而非 implementation detail。解释不了的 dependency 先作为 responsibility / knowledge ownership / boundary 需要重判的 Evidence，再收敛为少量稳定单向依赖。
- **差异与抽象。** 抽象稳定语义，不抽象表面相似。没有长期语义、契约、生命周期、性能架构或部署差异，不制造独立 provider / layer；真实差异也不强行统一。用户点名的分层、门面、提供者、注册表或“单向依赖”都只是候选手段，必须由 Goal pressure 和 reality 证明。
- **AI-native Target。** Target 的价值在于让主要 Goal 与已证明的同类变化拥有更小、更稳定的 reasoning / change / verification surface：正确 owner 更容易被独立理解，变化更少穿过无关责任，关键契约和依赖更显式，完成证明更接近责任边界。不能为了局部可读性吞并真实独立责任、复制 authoritative facts、隐藏真实跨边界关系，或把实现细节升级成 architecture law。
- **Target。** Target 必须包含当前 Evidence 已足以支持、未来仍会复用且会改变后续判断的战略事实，同时保持最小充分：不把当前 reality 合理化成目标，也不为完整感预编尚无 Evidence 的 capability、provider、layer 或协作关系。
- **Program 与退出。** Program 必须把已确认的战略结论集中成当前值得推进的结构变化：责任更闭合、私有知识泄漏和不必要 coupling 更少、内部 variation 被正确隔离、dependency / information hiding 更稳定，并让对应旧知识、旧权威、反向依赖、特殊路径或补偿性 guidance 真实退出。只新增 facade / registry / interface 而旧结构仍 authoritative，或只为未来改造搭脚手架，都不算 Architecture Improvement。
- **验证。** Behavior parity 只证明没有改坏，不证明 architecture improvement。Architecture Evidence 应直接对应 Target 的结构 claim：responsibility / authority 是否真正归位、旧 dependency / path 是否退出、caller 是否不再重组 owner 私有事实、代表性 Goal 是否主要沿预期 boundary 被理解 / 修改 / 验证。若这些 claim 无法被 reality 检查，Target 仍过于抽象。

只有用户、仓库或上游权威来源，以及已验证的现实，才能绑定长期承诺或当前事实。架构文档是 Evidence / 稳定结论的持久化来源，不是不可挑战的 oracle。除非某种表示已被权威固定，AE 只规定架构结果和 structural done condition，不提前规定类、接口、文件、配置、调用形态、合并请求、任务拆分或测试工具。AE 默认围绕当前 Program 继续收敛；若被上游 shaping capability 调用，只返回 Evidence、方向和 Human decision surface，不接管提问。

## 按需读取

- [strategic-design.md](references/strategic-design.md)：Goal pressure 与 bounded Evidence 仍支持 materially different 的 capability / module boundary、internal variation、dependency 或 Target；
- [delivery-examples.md](references/delivery-examples.md)：Strategic Design 已成立，但交付形状容易漂移，或候选 Target 疑似只是平台化、加层 / facade 化、complexity relocation；示例只帮助表达和挑战候选，不定义第二套 contract；
- [legacy-lenses.md](references/legacy-lenses.md)：旧模式、标记、配置、注册名或其他兼容身份能否退出会改变 Target / Program；
- [brooks-constraints.md](references/brooks-constraints.md)：候选结构已经说得通，但整体复杂度、第二系统或 complexity relocation 仍可疑。

## 发出前检查

1. 是否从 Goal / Goal set 恢复了真实 architecture change pressure，而不是把用户点名的 module / layer / provider 或当前 patch 当 Target？
2. Target 是否让 capability / module responsibility 更闭合，并只在真实 variation 需要时分层，长期 dependency 依赖稳定语义并保持可解释的单向关系？
3. 对代表性 Goal，Target 是否减少了跨无关 owner 的 judgment / change / verification surface，而没有通过吞并独立责任、复制 authority 或新增无退出的 abstraction 制造“假内聚低耦合”？
4. 演进锚点是否只是 attention funnel；同一战略修正是否已聚合，当前 Program 是否产生 structural gain + real exit，并保持 architecture altitude 而没有变成 implementation plan？
5. 稳定结论是否归位到原 authoritative source，交付是否完整且能被 architecture / behavior Evidence 证实或推翻？
