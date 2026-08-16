# Evaluate Architecture Evolution

只用于显式 smoke/eval；正常 runtime 不读。本文件冻结 behavior property，不定义 runtime。

## Static smoke

1. 主 Skill 自己完成调研 → architecture judgment → Program → delivery；无 ready/completed/status lifecycle。
2. 正常成功路径不依赖第二份 output/compile contract；`strategic-design.md`、`rules.md`、legacy/Brooks 都只在对应判断需要时读取。
3. Research 从指定 module/capability 与 direct neighborhood 渐进展开；已有架构意图、领域文档、ADR 与修改历史按各自 authority 使用，修改历史/热点 只作 discovery，不直接证明 architecture improvement。
4. 当前 taxonomy/proposed shape 只是 Evidence；没有 stable variation 不制造 provider。
5. Layering/cohesion、abstraction/specific、primary/auxiliary、real evolution 都能改变 Target Architecture；长期 dependency boundary 优先由 repo/module/package/build/tooling 表达，独立 authority/lifecycle 的相邻 subsystem 不因 cohesion 被吞并；反复解释 ownership/dependency 的 guidance 可作为结构歧义 Evidence，但必须与不可消除的 domain semantics 区分。
6. 架构晋级可以由 durable change pressure 证明，也可以由当前最可信战略设计与现实之间造成持续工程摩擦的偏离证明；单个 smell/local pressure 不制造 Program，真实 fork 缺 decisive Evidence/Human decision 时保持 unresolved。
7. 目标结构不是 obligation list；现实与目标之间的 gap 只形成候选演进。Program 最多 3 个 Improvements，不补数；必要时可以只有目标结构/权威架构来源的澄清或更新。每项 Improvement 必须在当前压力、长期结构收益、real exit、迁移成本与风险之间有足够理由优先现在推进；未选 gap 可以延期、保留或等待更多 Evidence。
8. Program 引用或更新原 authoritative architecture source；候选战略设计与当前现实必须和既有 SOT 区分，handoff artifact 不成为 repo architecture SOT。
9. AE 停在 architecture outcome / structural done condition；除非 authority 绑定 representation，不固定 implementation。
10. 上游 shaping capability 调用时 AE 返回 Evidence/options/decision surface，不抢 Human Ask ownership。
11. 成功 Program 同文 materialize 到 repo/workspace 外 handoff file，交付只包含当前 judgment/Program；material correction 后完整重交付；写入失败不得假装成功。
12. `agents/openai.yaml` 是 thin invocation pointer；validation 不进入 runtime。
13. 主文件只保留执行所需的少量判断，使用普通中文表达；Strategic Design 是 AE 的核心判断，架构文档只是稳定结论的持久化载体，不是新的评分 taxonomy；具体案例留在 validation，难判细则按需读取。

## Regression cases

- **P1 Bounded research**：历史模块 + current provider taxonomy → 从责任/直接上下游重识别 boundary，仅 decisive unknown 扩搜。
- **P2 Consumer/cohesion boundary**：consumer 仍解释 capability 私有事实，且相邻 subsystem 已有独立 authority/lifecycle → Target 让旧 consumer knowledge/path 退出，但不为 cohesion 吞并相邻 owner。
- **P3 Provider taxonomy**：family switch 存在 → 只有 stable semantic/lifecycle/performance/deployment variation 才形成 provider。
- **P4 Dependency**：common/core 依赖 specific implementation → Target 建立稳定单向 dependency boundary，并优先由 module/package/build/tooling 机械表达，而非仅靠文档约定。
- **P5 Abstraction**：代码相似但 semantics 不同 / 实现不同但 invariant 相同 → 前者 specific，后者抽象 stable invariant。
- **P6 Performance**：无 profiling/SLA/resource Evidence 的 fast path → 不得打穿 primary boundary。
- **P7 Real evolution**：新增 facade/registry 但旧 authority/path 仍在 → 不得算 evolution；Program completion 必须指出整体完成后哪些旧 authority/dependency/path 不再 authoritative。
- **P8 Second system**：简单 pressure 引入 plugin/framework/hooks → 无当前长期 Evidence 就缩小。
- **P9 Prose-compensated boundary**：同一 ownership/dependency 规则在 AGENTS/comment/runbook 中反复解释，而 repo territory/build dependency 仍无法直接表达 → 把这种重复 guidance 作为 architecture Evidence 继续判断；若它只是不可从结构推出的 domain semantics，则保留 guidance，不得为了“agent 更好读”强行改 architecture。
- **P10 Guidance exit**：Architecture Improvement 已把原本只能靠 prose 约束的 owner/dependency 物化进 module/package/build/tooling → 对应补偿性 guidance 应退出或停止 authoritative；若仍有独立 domain semantic/contract，则只删除已被结构替代的部分。
- **P11 Architecture source is not reality**：当前代码长期形成 `core → specific` 依赖，但既有 architecture source 明确要求相反方向 → 不得因为 reality 稳定就把当前形状恢复成目标结构；先判断是实现漂移还是原意图前提已失效。
- **P12 Scoped strategic design**：repo 没有完整 architecture doc，当前只在处理 runtime/provider → 只恢复这一范围的责任、依赖、通用/特化与公开边界，不生成全 repo 蓝图。
- **P13 Docs have distinct authority**：CONTEXT/domain glossary 给出业务语言、ADR 记录历史 trade-off、git history 给出 hot spot → 三者都可提供 Evidence，但任何一个都不能单独充当 Target Architecture。
- **P14 Strategic design before persistence**：repo 没有 architecture doc，但领域责任、权威归属、依赖与长期差异已有足够 Evidence → AE 应先形成当前范围的 当前最可信战略设计；是否写入 repo 是后续持久化判断，不能因缺文档而停止。
- **P15 Architecture doc is persistence, not oracle**：已有架构文档与新 Evidence 冲突 → 用战略设计重新检验双方，不得把文档当成不可挑战的规则，也不得因 reality 已存在就自动覆盖文档。
- **V1 Low-value cleanup**：一个候选 change 能删掉旧 helper/namespace、让 dependency 更干净，也满足 structural gain + real exit，但同一类真实 change 仍需跨原有 owner / authority / verification surfaces → 不得仅因结构更漂亮进入 Top Improvements；最多作为 local cleanup/附带退出处理。
- **V2 Positive leverage**：一类真实需求每次都要跨多个 owner 重组私有 knowledge；候选 Target 让 capability responsibility/dependency/authority 闭合，使后续同类变化从跨多个 owner 收敛到单一 owner，并由稳定 Evidence 验证，同时旧跨边界 path 退出 → 这是优先 Architecture Improvement，即使实际 patch 不大。
- **V3 可局部理解是结果**：候选结构让后续修改所需的责任、允许依赖、权威状态、重要约束和完成证据能从局部仓库结构或工具中发现并验证，减少跨边界重建知识 → 可作为清晰边界的正向结果；若只是增加文档、导航或上下文说明，或为了智能体方便而破坏主要责任、制造额外层，则失败。
- **V4 Planned pressure is evidence**：已批准 roadmap / binding requirement 已明确未来一类变化，即使尚未发生多次，也算真实 change pressure；AE 可以据此选择能解除其结构约束的 Improvement。仅凭“以后可能有用”的猜测仍不得物化 future hook/framework。
- **V5 Propagation compression**：两个候选都满足架构约束并有 real exit；A 只让现有模块内部更清楚，B 让同一类真实 change 从 `多个 owner + 多份 authority + 多处验证` 收敛为 `一个 owner + 一个 authority + 局部验证` → 优先 B。若所谓“压缩”只是隐藏真实跨边界语义或把已有独立 authority/lifecycle 的 owner 错吞成一个，则失败。
- **V6 Durable leverage**：一次性 migration 当前确实跨多个 owner / authority / verification surface；候选 Target 也能把这一次 change 压缩到更局部并有 real exit，但 migration 完成后没有持续存在的 pressure、已证实会重复的一类变化或 binding future requirement 继续经过该 boundary → 不得仅凭当前一次 propagation compression 晋级为优先 Architecture Improvement；只保留当前 change 必需的最小结构调整。若未来变化由 roadmap / authority 明确绑定，则按 V4 处理，不要求历史重复。
- **V7 Structural friction without repeated feature change**：某模块近期需求不多，但主要行为必须跨多个 owner 才能理解和验证，需求也无法沿责任边界切分；Evidence 表明它持续违反 当前最可信战略设计 → 可以升级为架构问题，不要求先观察多次 feature change。
- **V8 Smell without architectural tension**：大文件、复杂分支或测试 setup 很重，但 responsibility/dependency/authority 与 当前最可信战略设计 一致，且没有持续工程摩擦 → 不得仅凭 smell 进入 Architecture Improvements。
- **V9 Design-only value**：调研确认当前 repo 结构合理，但既有 architecture doc 模糊或过时；本次可以只澄清/更新稳定的目标结构，不为了“有产出”制造 repo refactor。
- **V10 Stale architecture source**：既有架构来源要求统一实现，但已出现两个长期独立 lifecycle/authority → 不得把 repo 强行拉回旧目标结构；应先修正目标结构判断，再据此判断后续结构演进。
- **V11 Four-pressure design check**：候选结构在 change locality 上更好，但理解仍需跨多个不相干 owner、需求仍无法按责任切分或验证必须绕过公开边界 → 不能仅凭改动范围变小判为更优战略设计。
- **V12 Requirement-shaping false positive**：一个需求跨度很大、难以拆分，但根因是目标本身混合了多个独立业务结果或 ownership 尚未决定；当前模块责任与依赖并未失真 → 先回到需求 shaping，不得据此改架构。
- **V13 Testability false positive**：测试很慢或 setup 很重，但根因是外部环境、集成基础设施或数据准备，主要行为仍能通过正确责任边界验证 → 不得仅凭测试成本重塑架构。
- **E1 Target gap is not obligation**：战略设计识别出 3 个长期 gap，但其中 2 个当前没有真实/已明确未来压力，或迁移风险显著高于结构收益 → 不得因为它们更接近目标结构就全部塞进 Program；可以明确延期、保留或等待更多 Evidence。
- **E2 Best next move**：A、B 两个候选都符合目标结构；A 更“理想”但当前收益有限且退出价值低，B 能解除正在发生的结构摩擦并让旧 authority/path 真实退出 → 当前优先 B，即使 A 在最终目标图上变化更大。
- **C1 Improvement quality**：research/data collection 不进 Top Improvements；只有解除真实 pressure 暴露的结构约束、压缩真实 change propagation，并同时产生 structural gain + real exit 的 change 可进。
- **C2 Ceiling**：只有 2 个真实 Improvements → 只输出 2 个。
- **C3 Setup-only**：先建 abstraction、以后再迁 → 若当前不产生 gain/exit，不得入 Program。
- **C4 Leverage**：多个真实 Improvements → 优先显著减少同类 change 必须跨越的 owner / authority / dependency / verification surface，而不是最易实现、最整洁或只减少表面 dependency 的项。
- **C5 SOT**：已有 authoritative contract → 引用原 SOT；需演进时指向原 source delta。
- **N1 Local**：bug/dead getter/mechanical cleanup → local judgment，不制造 Target/Program。
- **R1 Real fork**：两个长期结构都可行且缺 decisive constraint → unresolved，不按模式偏好强选。
- **H1 Human ownership**：Northstar 路由来的 Human-owned choice → AE 返回 decision surface，不自行串行 Ask。
- **L1 Legacy**：旧 token 本地无 reader但可能外部可见 → search absence 不等于可删，只做 decision-relevant probe。
- **O1 Altitude**：Target 已稳定 → 固定 architecture outcome，不规定 class/API/file/schema/MR/test provider。
- **D1 Re-entry**：Program 交付后 Human material correction → 重开受影响判断并完整重交付当前 Program，不附 Research inventory、rejected alternatives 或旧 Program。
- **D2 Artifact failure**：Program 已收敛但外部 file 不可写 → blocker，不把 conversation 当成功 handoff。

## Captured properties

1. taxonomy / proposed shape 是 Evidence，不是 law；
2. Target / Improvements 必须由长期结构 Evidence 支撑：可以是持续/重复/已明确的未来变化被结构放大，也可以是 当前最可信战略设计 与现实之间造成持续工程摩擦的偏离；smell、hotspot 与一次性 migration 只能触发调查，不能单独晋级；
3. abstraction 由 stable semantics/invariants 决定；
4. 长期依赖边界优先由仓库结构和工具直接表达，内聚不能吞并已有独立权威来源和生命周期的系统；清晰边界还应让后续修改所需的责任、重要约束和完成证据更局部可发现和验证，但这只是好架构的结果，不是单独重构的理由；
5. auxiliary concern 不塑造 primary architecture，caller 不重组 capability 私有 knowledge；
6. real evolution 要求旧 authority/knowledge/dependency/path 退出，已被结构替代的补偿性 guidance 同样退出；
7. Research bounded；目标结构与当前演进分离，gap 不自动成为 obligation，Program 只保留现在值得推进且 independently improving 的 changes；
8. 稳定战略设计结论优先维护原 authoritative architecture source；domain glossary、ADR、code/history 各按自身 authority 使用，不拼成平行 SOT；
9. repeated ownership/dependency prose 只是 architecture Evidence，必须先区分 structural ambiguity 与 irreducible domain semantics；
10. specialist 不抢 Human decision ownership；
11. delivery 交当前 judgment、必要的目标结构变化与 Program，且不是 lifecycle state；material update 后必须完整重交付；
12. handoff artifact 只承担 transport authority，不替代 repo SOT。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget：
`A. 不加载 architecture-evolution` vs `B. 加载 architecture-evolution`。

评分：Research scope、change-pressure alignment、strategic-design quality、intent/reality discrimination、architecture taste、Program leverage/convergence、architecture altitude、Human routing、re-entry、handoff integrity、context cost。

只有 clean-session paired Evidence 才能声明 behavioral uplift；否则标记 `NOT RUN`。
