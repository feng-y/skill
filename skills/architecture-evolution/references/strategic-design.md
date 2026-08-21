# 战略设计

只在主 Skill + bounded Evidence 后仍有会改变 Target 的 strategic fork、authority conflict 或 boundary discriminator 时读取；这里只补判定，不加第二套流程。

战略设计回答系统长期应该是什么；当前 Program 只回答现实条件下值得先推进哪一刀。迁移成本、实现难度、局部 pressure 或已有 patch 可以改变 Program，不能把较便宜、较容易或已经存在的结构重新定义成 Target。只有新的 Goal、领域事实、长期约束、权威或已验证 reality 推翻战略前提时，才重算受影响的 Target。候选 Target 是当前最可信的 architecture judgment，不因描述完整或结构漂亮自动成立；material boundary / ownership 判断应能被后续 Evidence 证实或推翻。

## 从 Goal 到 Target

Goal 是架构变化的驱动力，不是模块设计指令。对于一个 Goal 或几个相关 Goal，先识别它们对系统施加的 **architecture change pressure**：哪些能力需要新增、替换、独立演进或吸收新的 variation；当前同类变化为何需要跨多个 owner / authority / dependency / verification surface；哪些长期 binding constraint 会让某种责任、生命周期、部署或 failure boundary 成为必需。只有这些会长期改变结构的部分进入 Target。

多个 Goal 只有在它们共享 material architecture pressure，或它们涉及的多个 capability / boundary / dependency 必须一起设计才能正确满足 Goal 时才共同塑造 Target。例如“增加第二种 storage backend”和“让 backend 切换不修改 caller”可能共同证明 provider variation；一个跨 pipeline Goal 也可能要求几个独立 owner 的 boundary / dependency 协同演进。反之，“降低登录延迟”和“拆分订单生命周期”如果没有共同结构前提，就不为了统一方案塞进一个 redesign。

从 Goal 到 Target 的关键关系是：

`Goal pressure → capability / responsibility → module boundary / cohesion → internal variation / layering → dependency direction → local understanding / change / verification`

这不是固定 reasoning pipeline，也不要求每一步都物化新对象。它只是防止几个常见错误：从 Goal 直接跳到 class/module、用局部高内聚掩盖错误 capability boundary、先整理 dependency 再合理化当前 owner、为了“分层”制造没有 stable variation 的 provider / adapter。

### Capability / module boundary

先判断什么长期能力应该拥有并隐藏为了满足 Goal 所需要的稳定设计知识 / 决定。一个候选 owner 应让同一变化原因所需的 knowledge、state、behavior、authority、lifecycle 和主要 verification 尽量闭合，使 caller 不再重组这些私有事实。

模块不是 capability taxonomy 的机械一一映射。几个细粒度 capability 若共享同一长期 owner / authority / lifecycle 和变化原因，可以在同一 module 内保持 cohesion；一个历史 module 若同时承担互不相关的长期变化原因，即使代码都“相关”，也可能需要重新划 boundary。用户点名 module 只定义 investigation scope，除非 authority 明确固定 representation，否则不能用当前名字证明 Target boundary。

### Internal variation / layering

boundary 成立后，再判断 owner 内部哪些变化需要隔离。只有 stable semantics 与可独立变化的 implementation / provider / storage/runtime adapter / lifecycle / deployment / performance architecture 等之间存在长期差异时，layer / provider 才成立。层次的价值是让一种变化停在正确 owner 内，而不是形成统一的 `interface → domain → provider → infrastructure` 模板。

如果两个实现只是当前代码不同但长期 contract / lifecycle / failure semantics 相同，应优先隐藏为 implementation；如果差异本身拥有独立 authority、生命周期或长期语义，则不能为了 module cohesion 强行内聚成 implementation detail。

### Dependency direction

能力和责任边界先成立，再设计 dependency direction、general / specific 与 information hiding。长期 dependency 必须能被真实 semantic / authority / lifecycle / failure relationship 解释，并尽量依赖 owner 的 stable contract / semantics，而不是具体实现或内部知识。

单向依赖是正确 boundary 的结果与约束，不是独立审美目标。若 `B → A` 只因为 helper/config 历史上在 A、调用方便或复用了 A implementation，应先重判 knowledge ownership；若 B 必须消费 A 的 authoritative semantic contract，则这个 dependency 可以合法存在并稳定单向。

### AI-native locality

高内聚低耦合最终要落到变化局部性。用一个代表性 Goal 或 Evidence 已确认的同类 future change 挑战候选 Target：

- **理解**：fresh implementer 是否能主要从正确 owner 附近恢复关键设计决定，而不是跨无关模块拼装隐含知识？
- **修改**：该变化是否主要落在应吸收它的 responsibility 内，还是仍迫使多个无关 owner 同时理解同一私有事实？
- **验证**：关键 completion / behavior Evidence 是否能从责任边界附近建立，而不是绕过 contract 穿透 implementation？

如果候选结构只是新增 facade / interface 后仍保留相同的跨 owner knowledge reconstruction，或通过复制 authoritative facts 让局部看起来独立，它不是真正的 AI-native improvement。

## 判断 Target

默认一个 best-known Target；只有 Evidence 同时支持 materially different 的长期结构且缺 decisive constraint，才保留多个候选。候选 Target 必须能回答这些问题；没有决策价值的问题不必机械展开。

- **战略锚点。** 这个 repo / 系统为什么存在，在更大系统中承担什么核心职责？当前 Goal / Goal set 要求什么能力发生长期变化，什么明确属于其他 owner？哪些长期能力或 binding constraints 真正塑造主要架构，哪些只是必要支撑？
- **责任边界。** 一个候选 owner 应独占并隐藏什么长期设计知识 / 决定？哪类当前与未来变化应该在这里被吸收，而不要求 caller 或其他能力同步重建这些知识？由此判断哪些 knowledge、state、behavior、authority、lifecycle 和 verification 应共同闭合。按候选 boundary 完成代表性 slice 后，若 consumer 仍必须穿透旧 owner 或重组其私有事实，这才是 boundary 的反证；migration 过渡期同时修改 old / new owner 本身不构成反证。
- **分开还是吸收。** 哪些差异只是能力内部 implementation / config variation，哪些因为独立语义、契约、权威、生命周期、性能架构、部署或其他长期约束必须保持独立？没有稳定差异，不制造 provider / layer。
- **边界关系。** 只有当跨边界的 authority、语义共享 / 翻译、生命周期协同 / 隔离或失败传播会改变 Target 时，才把这种关系显式出来。没有这类事实时，一个稳定依赖方向已经足够，不为完整图谱枚举关系 taxonomy。
- **依赖与抽象。** 能力和责任边界先成立，再设计 dependency direction、general / specific 与 information hiding。稳定语义不依赖具体实现；单向依赖不能挽救错误的 capability decomposition。
- **最小充分。** Target 必须包含当前 Evidence 已足以支持、未来仍会复用且会改变后续判断的能力、边界、关系和约束；没有 Evidence 的未来 capability / provider / layer / hook 保持开放。既不补成终局蓝图，也不为了极简遗漏已知战略事实。

高内聚低耦合是这些判断成立后的结构结果，不是独立评分。若模块表面集中，但 caller 仍理解本应由 owner 隐藏的设计决定；或一个典型 Goal 仍需要跨多个 owner 重组同一份私有知识 / authority / verification，则 boundary 还没有成立。

## Evidence 怎么用

不默认文件名，也没有单一 oracle。按材料实际 authority 和当前前提使用：

- current code / config / test / runtime 证明当前 reality；
- repo contract、仍有效的 architecture source、domain source、ADR 等约束 intended semantics / responsibility / boundary；
- 真实 consumer、workflow 与外部契约帮助确认系统实际角色、authority 和 lifecycle；
- approved Goal / roadmap 与工程摩擦帮助发现 durable change pressure，但一次性需求或 hotspot 不能单独证明 Architecture Improvement；
- 外部文章、项目和通用 pattern 只用于挑战候选，不替代当前 repo 的 Evidence。

业务、质量或运行约束只有在 authority / Evidence 证明它长期 binding，并会实质改变责任、生命周期、交互、部署或 failure boundary 时，才参与塑造 Target。一般性的“更快、更可靠、更解耦、更 AI-native”愿望不能凭空制造结构。

Research 只为会改变 Target 的 unresolved fork / Unknown 扩展；probe 必须区分 material alternatives。两个长期结构都说得通、继续文字推理不能提高判断质量，而一个廉价且可丢弃的 structural probe 能明显区分它们时，做最小 probe，例如迁一个代表性 consumer、切一条真实 dependency、跑能区分性能架构的 benchmark 或观察一次真实 lifecycle。probe 只回答当前 architecture hypothesis，不自动成为 Program、长期 abstraction 或 production path；结果只把受影响的 Target judgment 收紧、推翻或保留。Evidence 足够，或剩余 fork 已确认只能由 Human 取舍，就停止。已有 Evidence 跨 judgment 复用；只有前提失效才重查，不为新的 judgment pass 或“更完整理解”重扫 repo。

## 挑战候选 Target

至少从四种真实工程压力挑战候选，不把它们当固定 reasoning order：

1. **Goal absorption**：当前 / 已知未来同类 Goal 是否主要由预期 capability / owner 吸收，还是仍穿过不应参与的 responsibility？
2. **理解与修改**：理解 / 修改一个主要能力，是否必须跨很多不相干责任重建知识或设计决定？
3. **切分与依赖**：合理范围的需求能否主要沿责任边界拆开，dependency 是否能由稳定 semantic / authority / lifecycle relationship 解释，而不是按文件或技术层硬切？
4. **验证**：主要行为能否从对应责任附近获得可靠 Evidence，而不是绕过边界拼装内部细节？先区分架构问题与测试基础设施 / 外部环境成本。

真实独立的 authority、lifecycle 和 domain semantics 可以合理跨边界。只有 real fork 才保留多个候选；多个候选都成立时，再比较后续变化传播：优先让持续或已明确的未来变化少跨 responsibility / authority / dependency / verification surface，但不能吞并真实独立 owner、复制事实或隐藏跨边界语义。

## 持久化

只有跨变化仍会复用、未来会继续改变判断的稳定结论，才更新 repo 已有的 authoritative architecture source。记录责任、边界、依赖、通用 / 特化、重要约束和仍未决的结构问题；不要记录目录清单、实现步骤、一次性 migration、probe artifact 或当前代码说明。

已有权威来源优先原位更新，不建平行 SOT。repo 没有架构来源时，也不要因为一次 AE run 自动创建全量 `ARCHITECTURE.md`；只有结论已经稳定、未来确实会复用且用户授权时，才建立最小来源。
