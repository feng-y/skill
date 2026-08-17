# 战略设计

只在主 Skill 的判断与 bounded Evidence 之后，仍存在会 materially 改变 Target 的 strategic fork、authority conflict 或 boundary discriminator 时读取。本文件只提供会改变 Target 的判定问题，不增加第二套流程。

战略设计回答系统长期应该是什么；当前 Program 只回答现实条件下值得先推进哪一刀。迁移成本、实现难度、局部 pressure 或已有 patch 可以改变 Program，不能把较便宜、较容易或已经存在的结构重新定义成 Target。只有新的领域事实、长期约束、权威或已验证 reality 推翻战略前提时，才重算受影响的 Target。

## 判断 Target

默认形成一个 best-known Target；只有 Evidence 同时支持 materially different 的长期结构、且仍缺 decisive constraint 时，才保留多个候选。候选 Target 必须能回答这些问题；没有决策价值的问题不必机械展开。

- **战略锚点。** 这个 repo / 系统为什么存在，在更大系统中承担什么核心职责？当前范围预期负责什么，什么明确属于其他 owner？哪些长期能力或 binding constraints 真正塑造主要架构，哪些只是必要支撑？
- **责任边界。** 一个候选 owner 应独占并隐藏什么长期设计知识 / 决定？哪类未来变化应该在这里被吸收，而不要求 caller 或其他能力同步重建这些知识？由此判断哪些 knowledge、state、behavior、authority、lifecycle 和 verification 应共同闭合。
- **分开还是吸收。** 哪些差异只是能力内部 implementation / config variation，哪些因为独立语义、契约、权威、生命周期、性能架构、部署或其他长期约束必须保持独立？没有稳定差异，不制造 provider / layer。
- **边界关系。** 只有当跨边界的 authority、语义共享 / 翻译、生命周期协同 / 隔离或失败传播会改变 Target 时，才把这种关系显式出来。没有这类事实时，一个稳定依赖方向已经足够，不为完整图谱枚举关系 taxonomy。
- **依赖与抽象。** 能力和责任边界先成立，再设计 dependency direction、general / specific 与 information hiding。稳定语义不依赖具体实现；单向依赖不能挽救错误的 capability decomposition。
- **最小充分。** Target 必须包含当前 Evidence 已足以支持、未来仍会复用且会改变后续判断的能力、边界、关系和约束；没有 Evidence 的未来 capability / provider / layer / hook 保持开放。既不补成终局蓝图，也不为了极简遗漏已知战略事实。

高内聚低耦合是这些判断成立后的结构结果，不是独立评分。若模块表面集中，但 caller 仍理解本应由 owner 隐藏的设计决定；或长期变化仍需要跨多个 owner 重组同一份私有知识，则 boundary 还没有成立。

## Evidence 怎么用

不默认文件名，也没有单一 oracle。按材料实际 authority 和当前前提使用：

- current code / config / test / runtime 证明当前 reality；
- repo contract、仍有效的 architecture source、domain source、ADR 等约束 intended semantics / responsibility / boundary；
- 真实 consumer、workflow 与外部契约帮助确认系统实际角色、authority 和 lifecycle；
- history 与工程摩擦帮助发现 durable change pressure，但 hotspot / 一次性困难不能单独证明 Architecture Improvement；
- 外部文章、项目和通用 pattern 只用于挑战候选，不替代当前 repo 的 Evidence。

业务、质量或运行约束只有在 authority / Evidence 证明它长期 binding，并会实质改变责任、生命周期、交互、部署或 failure boundary 时，才参与塑造 Target。一般性的“更快、更可靠、更解耦”愿望不能凭空制造结构。

Research 只围绕一个明确、仍未解决且会改变 Target 的 fork / Unknown 扩展；每个新增 probe 都应能区分 material alternatives。若现有 Evidence 已足以判断，就停止扩搜；若剩余 fork 本质是 Human-owned commitment / trade-off，而不是可继续调查的事实问题，也停止 autonomous research。已获得的 Evidence 默认跨 responsibility / boundary / dependency 等 judgment 复用；只有新 Evidence 或 Human decision 推翻其前提时，才重查对应部分。不要为了新的 judgment pass 或“更完整理解”重新扫描 repo。

## 挑战候选 Target

至少从四种真实工程压力挑战候选，不把它们当固定 reasoning order：

1. **理解**：理解一个主要能力，是否必须跨很多不相干责任重建知识或设计决定？
2. **修改**：同类变化是否会穿过本不该参与的 owner，或迫使别人理解本应被隐藏的决定？
3. **切分**：合理范围的需求能否主要沿责任边界拆开，而不是按文件或技术层硬切？先排除需求本身混合多个业务结果或 ownership 尚未决定。
4. **验证**：主要行为能否从对应责任附近获得可靠 Evidence，而不是绕过边界拼装内部细节？先区分架构问题与测试基础设施 / 外部环境成本。

真实独立的 authority、lifecycle 和 domain semantics 可以合理跨边界。只有真实 strategic fork 仍存在时才保留多个候选；多个候选都成立时，再比较后续变化传播：优先让持续或已明确的未来变化少跨 responsibility / authority / dependency / verification surface，但不能吞并真实独立 owner、复制事实或隐藏跨边界语义。

## 持久化

只有跨变化仍会复用、未来会继续改变判断的稳定结论，才更新 repo 已有的 authoritative architecture source。记录责任、边界、依赖、通用 / 特化、重要约束和仍未决的结构问题；不要记录目录清单、实现步骤、一次性 migration 或当前代码说明。

已有权威来源优先原位更新，不建平行 SOT。repo 没有架构来源时，也不要因为一次 AE run 自动创建全量 `ARCHITECTURE.md`；只有结论已经稳定、未来确实会复用且用户授权时，才建立最小来源。
