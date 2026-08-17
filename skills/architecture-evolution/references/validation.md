# Evaluate Architecture Evolution

只用于显式 smoke/eval；正常 runtime 不读。本文件冻结 behavior property，不定义 runtime。

## Static smoke

1. 主 Skill 自己完成调研 → Strategic Design → Tactical Evolution → delivery；无 ready/completed/status lifecycle，Strategic Design 是核心 judgment，Evolution 只选择当前值得推进的架构 move。
2. 正常成功路径不依赖第二份 output/compile contract；`strategic-design.md`、`rules.md`、legacy/Brooks 都只在对应判断需要时读取。
3. Research 从指定 module/capability 与 direct neighborhood 渐进展开，同时只恢复会改变当前范围战略设计的 repo/system identity 与 architecture intent；已有架构意图、领域文档、真实 consumer、代码、ADR 与修改历史按各自 authority 使用，任何单一来源都不能独自定义 identity，修改历史/热点只作 discovery，不直接证明 architecture improvement。
4. 当前 taxonomy/proposed shape 只是 Evidence；没有 stable variation 不制造 provider。Provider、layer、facade、registry 等都只是 Strategic Design 可能确认或否定的结构手段，不因用户点名或当前代码形态自动成立。
5. Target Architecture 不能把当前 module/capability taxonomy 当固定候选集合后做局部优化；先依据 repo identity、领域语义与长期变化恢复预期 capability decomposition，再用 cohesion/coupling、理解/修改/切分/验证压力挑战它。责任边界成立后才设计 layering/dependency direction；长期 dependency boundary 优先由 repo/module/package/build/tooling 表达，独立 authority/lifecycle 的相邻 subsystem 不因 cohesion 被吞并；反复解释 ownership/dependency 的 guidance 可作为结构歧义 Evidence，但必须与不可消除的 domain semantics 区分。
6. 架构晋级可以由 durable change pressure 证明，也可以由当前最可信战略设计与现实之间造成持续工程摩擦的偏离证明；单个 smell/local pressure 不制造 Program，真实 fork 缺 decisive Evidence/Human decision 时保持 unresolved。
7. Strategic Design 先独立确定长期结构；现实与 Target 的 gap 只形成 Tactical Evolution 候选。当前 pressure、迁移成本、实现风险和已有 patch 只能改变现在选择哪一刀、推进到哪里，不能把更便宜或更容易的现实形态重定义成 Target。Program 最多 3 个 Improvements，不补数；必要时可以只有战略设计结论/权威架构来源的澄清或更新。
8. 每项 Tactical Evolution 必须把一个已确认的战略结构变得更真实：改善责任闭合、减少私有知识泄漏和不必要耦合、在已成立边界上形成稳定依赖与信息隐藏，并产生 real exit；只增加 layer/interface/provider 名称而旧 owner/knowledge/path 仍在，不算 evolution。
9. Program 引用或更新原 authoritative architecture source；候选战略设计与当前现实必须和既有 SOT 区分，handoff artifact 不成为 repo architecture SOT。
10. AE 停在 architecture outcome / structural done condition；除非 authority 绑定 representation，不固定 implementation。
11. 上游 shaping capability 调用时 AE 返回 Evidence/options/decision surface，不抢 Human Ask ownership。
12. 成功 Program 同文 materialize 到 repo/workspace 外 handoff file，交付只包含当前 judgment/Program；material correction 后完整重交付；写入失败不得假装成功。
13. `agents/openai.yaml` 是 thin invocation pointer；validation 不进入 runtime。
14. 主文件只保留执行所需的少量判断，使用普通中文表达；Strategic Design 是 AE 的核心判断，架构文档只是稳定结论的持久化载体，不是新的评分 taxonomy；具体案例留在 validation，难判细则按需读取。

## Regression cases

- **P1 Bounded research**：历史模块 + current provider taxonomy → 先恢复会影响该范围预期角色的 repo identity / architecture intent，再从责任/直接上下游重识别 boundary；只对 decisive unknown 扩搜，不做全 repo inventory。
- **P2 Consumer/cohesion boundary**：consumer 仍解释 capability 私有事实，且相邻 subsystem 已有独立 authority/lifecycle → Strategic Design 先确认长期 capability/owner 边界；若选择当前推进，Tactical Evolution 让旧 consumer knowledge/path 退出，但不为 cohesion 吞并相邻 owner。
- **P3 Provider taxonomy**：family switch 存在 → Strategic Design 先判断 variation 是否具有 stable semantic/contract/lifecycle/performance/deployment 差异；只有长期结构 Evidence 足够才确认 provider boundary。若当前选择推进该 gap，Tactical Evolution 再把 variation knowledge/state/lifecycle 收回 owner、让 caller 只依赖 stable contract，并让旧 switch/reconstruction/path 退出；仅增加 Provider interface/factory 不算完成。
- **P4 Dependency**：common/core 依赖 specific implementation → 先确认两者的长期责任边界成立，再让 Tactical Evolution 建立稳定单向 dependency boundary，并优先由 module/package/build/tooling 机械表达，而非仅靠文档约定。
- **P5 Abstraction**：代码相似但 semantics 不同 / 实现不同但 invariant 相同 → 前者 specific，后者抽象 stable invariant。
- **P6 Performance**：无 profiling/SLA/resource Evidence 的 fast path → 不得打穿 primary boundary。
- **P7 Real evolution**：新增 facade/registry 但旧 authority/path 仍在 → 不得算 evolution；Program completion 必须指出整体完成后哪些旧 authority/dependency/path 不再 authoritative。
- **P8 Second system**：简单 pressure 引入 plugin/framework/hooks → 无当前长期 Evidence 就缩小。
- **P9 Prose-compensated boundary**：同一 ownership/dependency 规则在 AGENTS/comment/runbook 中反复解释，而 repo territory/build dependency 仍无法直接表达 → 把这种重复 guidance 作为 architecture Evidence 继续判断；若它只是不可从结构推出的 domain semantics，则保留 guidance，不得为了“agent 更好读”强行改 architecture。
- **P10 Guidance exit**：Architecture Improvement 已把原本只能靠 prose 约束的 owner/dependency 物化进 module/package/build/tooling → 对应补偿性 guidance 应退出或停止 authoritative；若仍有独立 domain semantic/contract，则只删除已被结构替代的部分。
- **P11 Architecture source is not reality**：当前代码长期形成 `core → specific` 依赖，但既有 architecture source 明确要求相反方向 → 不得因为 reality 稳定就把当前形状恢复成目标结构；先判断是实现漂移还是原意图前提已失效。
- **P12 Scoped strategic design**：repo 没有完整 architecture doc，当前只在处理 runtime/provider → 先恢复足以判断 runtime/provider 在 repo 整体中预期角色的 identity / intent，再只设计这一范围的长期能力、责任、依赖、通用/特化与公开边界；不得因为需要 strategic anchor 就生成全 repo 蓝图。
- **P13 Docs have distinct authority**：CONTEXT/domain glossary 给出业务语言、ADR 记录历史 trade-off、git history 给出 hot spot → 三者都可提供 Evidence，但任何一个都不能单独充当 repo identity 或 Target Architecture。
- **P14 Strategic design before persistence**：repo 没有 architecture doc，但 repo 核心职责、领域责任、权威归属、依赖与长期差异已有足够 Evidence → AE 应先形成当前范围的当前最可信战略设计；是否写入 repo 是后续持久化判断，不能因缺文档而停止。
- **P15 Architecture doc is persistence, not oracle**：已有架构文档与新 Evidence 冲突 → 用 repo identity、领域语义与现实重新检验双方，不得把文档当成不可挑战的规则，也不得因 reality 已存在就自动覆盖文档。
- **P16 Capability boundary is not enough**：两个 capability 的 responsibility、authority 与跨 capability 依赖已清楚，但其中一个 capability 内部仍让稳定语义依赖具体实现，或仍有会长期影响理解、修改、切分或验证的内部结构复杂性 → Target 不得停在 capability boundary；继续收敛内部稳定语义、具体实现隔离边界和单向依赖。已有仍有效的 layering/dependency authority 应在内部目标结构中实例化并优先机械约束；若 authority 前提已失效则不再约束候选，并把原 source 的演进纳入战略设计；没有 authority 不自造固定层数或命名。
- **P17 ModelCurator anchor / two-scale target**：用户从 `ModelCurator` 及周边 feature completion、runner/getter/generation 等叶子摩擦进入，但 repo identity 与 Evidence 表明长期责任落在 Feature 与 Infer/QServer family 两类能力，且 repo authority 约束能力内分层与单向依赖 → `ModelCurator` 只作调查锚点；Target 先按预期能力重新收敛责任、权威和边界，再设计跨能力与能力内部依赖。叶子 gap 只能作为 Evidence、退出条件或由目标结构推出的改进，不能替代两尺度战略设计；运行时 pipeline 不能冒充代码依赖方向。
- **P18 Repo identity prevents local rationalization**：用户从历史模块 `X` 进入，`X` 内部责任和单向依赖可以被整理得自洽，但 repo 核心职责、真实 consumer 与长期变化都表明这里实际承载的是更大的 capability，或其中一部分应属于其他 owner → Target 不得把 `X` 当长期边界后继续优化；先恢复预期 capability decomposition，再判断哪些当前模块保留、合并、拆分或退出。
- **V1 Low-value cleanup**：一个候选 change 能删掉旧 helper/namespace、让 dependency 更干净，也满足 structural gain + real exit，但同一类真实 change 仍需跨原有 owner / authority / verification surfaces → 不得仅因结构更漂亮进入 Top Improvements；最多作为 local cleanup/附带退出处理。
- **V2 Positive leverage**：一类真实需求每次都要跨多个 owner 重组私有 knowledge；Strategic Design 确认这些 knowledge/state/authority 本应由一个 capability owner 闭合，候选 Tactical Evolution 能使后续同类变化从跨多个 owner 收敛到单一 owner，并让旧跨边界 path 退出 → 这是优先 Architecture Improvement，即使实际 patch 不大。
- **V3 可局部理解是结果**：候选结构让后续修改所需的责任、允许依赖、权威状态、重要约束和完成证据能从局部仓库结构或工具中发现并验证，减少跨边界重建知识 → 可作为清晰边界被战术物化后的正向结果；若只是增加文档、导航或上下文说明，或为了智能体方便而破坏主要责任、制造额外层，则失败。
- **V4 Planned pressure is evidence**：已批准 roadmap / binding requirement 已明确未来一类变化，即使尚未发生多次，也算真实 change pressure；它可以支撑 Strategic Design 对长期 variation/boundary 的判断，也可以提高某个 Tactical Evolution 的当前优先级。仅凭“以后可能有用”的猜测仍不得物化 future hook/framework。
- **V5 Propagation compression**：两个战术候选都满足同一个 Target 并有 real exit；A 只让现有模块内部更清楚，B 让同一类真实 change 从 `多个 owner + 多份 authority + 多处验证` 收敛为 `一个 owner + 一个 authority + 局部验证` → 优先 B。若所谓“压缩”只是隐藏真实跨边界语义或把已有独立 authority/lifecycle 的 owner 错吞成一个，则失败。
- **V6 Durable leverage**：一次性 migration 当前确实跨多个 owner / authority / verification surface；候选 Tactical Evolution 也能把这一次 change 压缩到更局部并有 real exit，但 migration 完成后没有持续存在的 pressure、已证实会重复的一类变化或 binding future requirement 继续经过该 boundary → 不得仅凭当前一次 propagation compression 晋级为优先 Architecture Improvement；只保留当前 change 必需的最小结构调整。若未来变化由 roadmap / authority 明确绑定，则按 V4 处理，不要求历史重复。
- **V7 Structural friction without repeated feature change**：某模块近期需求不多，但主要行为必须跨多个 owner 才能理解和验证，需求也无法沿责任边界切分；Evidence 表明它持续违反当前最可信战略设计 → 可以升级为架构问题，不要求先观察多次 feature change。
- **V8 Smell without architectural tension**：大文件、复杂分支或测试 setup 很重，但 responsibility/dependency/authority 与当前最可信战略设计一致，且没有持续工程摩擦 → 不得仅凭 smell 进入 Architecture Improvements。
- **V9 Design-only value**：调研确认当前 repo 结构合理，但既有 architecture doc 模糊或过时；本次可以只澄清/更新稳定的战略设计，不为了“有产出”制造 Tactical Evolution。
- **V10 Stale architecture source**：既有架构来源要求统一实现，但已出现两个长期独立 lifecycle/authority → 不得把 repo 强行拉回旧目标结构；应先修正 Strategic Design，再据此判断后续 Tactical Evolution。
- **V11 Four-pressure design check**：候选 Target 在 change locality 上更好，但理解仍需跨多个不相干 owner、需求仍无法按责任切分或验证必须绕过公开边界 → 不能仅凭改动范围变小判为更优战略设计。
- **V12 Requirement-shaping false positive**：一个需求跨度很大、难以拆分，但根因是目标本身混合了多个独立业务结果或 ownership 尚未决定；当前模块责任与依赖并未失真 → 先回到需求 shaping，不得据此改架构。
- **V13 Testability false positive**：测试很慢或 setup 很重，但根因是外部环境、集成基础设施或数据准备，主要行为仍能通过正确责任边界验证 → 不得仅凭测试成本重塑架构。
- **V14 Local cohesion cannot rescue wrong identity**：候选 A 让历史模块 `X` 内部更内聚、依赖更单向，但仍把 repo identity 里本应闭合的一项长期 capability 拆在 `X/Y/Z` 三个 owner；候选 B 先重划 capability boundary，再形成局部闭合和单向依赖 → A 不能因局部结构更漂亮成为 Target，优先按 B 的战略结构继续判断。
- **E1 Target gap is not obligation**：Strategic Design 识别出 3 个长期 gap，但其中 2 个当前没有真实/已明确未来 pressure，或迁移风险显著高于当前结构收益 → 不得因为它们更接近 Target 就全部塞进 Program；Target 保持不变，这两个 gap 可以延期、保留或等待更多 Evidence。
- **E2 Best next move**：A、B 两个 Tactical Evolution 都符合同一个 Target；A 更接近最终形态但当前收益有限且退出价值低，B 能解除正在发生的结构摩擦并让旧 authority/path 真实退出 → 当前优先 B，不因此把 B 的局部形态抬升为新的 Target。
- **E3 Tactical pressure cannot redefine Target**：Strategic Design 已确认 capability `X` 应拥有某类 knowledge/lifecycle，但完整迁移当前成本高；不得因此把现有跨 `X/Y` 的 ownership 重新解释为长期正确结构。可以只选安全的局部 evolution、延期或不改 repo；只有新的长期 Evidence 推翻战略前提才重算 Target。
- **E4 Tactical materialization**：Strategic Design 已确认一个长期 capability/provider boundary；Tactical Evolution 只新增接口或目录但 caller 仍重组私有 knowledge、specific implementation 仍反向影响 stable layer、旧 switch/path 仍 authoritative → 不得判为有效 evolution。需要 responsibility closure + lower coupling + stable dependency + real exit 中与该 Target gap 对应的结构事实真正成立。
- **C1 Improvement quality**：research/data collection 不进 Top Improvements；只有实现已确认战略结构、解除真实 pressure 暴露的结构约束，并同时产生 structural gain + real exit 的 change 可进。
- **C2 Ceiling**：只有 2 个真实 Improvements → 只输出 2 个。
- **C3 Setup-only**：先建 abstraction、以后再迁 → 若当前不产生 gain/exit，不得入 Program。
- **C4 Leverage**：多个真实 Tactical Evolution → 优先显著减少同类 change 必须跨越的 owner / authority / dependency / verification surface，而不是最易实现、最整洁或只减少表面 dependency 的项。
- **C5 SOT**：已有 authoritative contract → 引用原 SOT；需演进时指向原 source delta。
- **N1 Local**：bug/dead getter/mechanical cleanup → local judgment，不制造 Target/Program。
- **R1 Real fork**：两个长期结构都可行且缺 decisive constraint → unresolved，不按模式偏好强选。
- **H1 Human ownership**：Northstar 路由来的 Human-owned choice → AE 返回 decision surface，不自行串行 Ask。
- **L1 Legacy**：旧 token 本地无 reader但可能外部可见 → search absence 不等于可删，只做 decision-relevant probe。
- **O1 Altitude**：Target 已稳定 → 固定 architecture outcome，不规定 class/API/file/schema/MR/test provider。
- **D1 Re-entry**：Program 交付后 Human material correction → 若改变战略前提则重算受影响 Strategic Design，再重选 Tactical Evolution；若只改变当前成本/执行 reality，则保留仍有效 Target，只重算受影响战术选择，并完整重交付当前 Program。
- **D2 Artifact failure**：Program 已收敛但外部 file 不可写 → blocker，不把 conversation 当成功 handoff。

## Captured properties

1. taxonomy / proposed shape 是 Evidence，不是 law；当前 module/capability 划分和 provider/layer 等手段同样不能先验成为 Target；
2. Strategic Design 是核心：先恢复会约束当前范围的 repo/system identity 与 architecture intent，再据此、领域语义和长期变化形成预期 capability decomposition、稳定 variation/boundary 与长期依赖；不能把现有模块局部合理化成目标结构；
3. Tactical Evolution 是战略设计在当前 reality 上的选择和物化；当前 pressure、迁移成本、风险与已有 patch 只决定现在做什么，不反向定义 Target；
4. abstraction 由 stable semantics/invariants 决定；能力与责任边界先成立，再设计稳定单向依赖；
5. Tactical Evolution 应使已确认责任的 knowledge/state/behavior/authority/lifecycle/verification 更闭合，减少 caller 对私有事实的重组和不必要 coupling，并在正确边界上形成稳定 dependency / information hiding；
6. 长期依赖边界优先由仓库结构和工具直接表达；内聚不能吞并已有独立权威来源和生命周期的系统；
7. real evolution 要求旧 authority/knowledge/dependency/path 退出，已被结构替代的补偿性 guidance 同样退出；
8. Research bounded；恢复 repo identity 不等于全 repo inventory；Target 与当前 Tactical Evolution 分离，gap 不自动成为 obligation，Program 只保留现在值得推进且 independently improving 的 changes；
9. 稳定战略设计结论优先维护原 authoritative architecture source；README、domain glossary、ADR、consumer、code/history 各按自身证明力使用，不拼成平行 SOT，也没有任何单一来源独自定义 identity；
10. repeated ownership/dependency prose 只是 architecture Evidence，必须先区分 structural ambiguity 与 irreducible domain semantics；
11. specialist 不抢 Human decision ownership；
12. delivery 交当前 Strategic Design、必要的 Target 变化与 Tactical Evolution，且不是 lifecycle state；material update 后必须完整重交付；
13. handoff artifact 只承担 transport authority，不替代 repo SOT。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget：
`A. 不加载 architecture-evolution` vs `B. 加载 architecture-evolution`。

评分：Research scope、repo-identity grounding、strategic-design quality、strategic/tactical separation、change-pressure alignment、intent/reality discrimination、architecture taste、Program leverage/convergence、architecture altitude、Human routing、re-entry、handoff integrity、context cost。

只有 clean-session paired Evidence 才能声明 behavioral uplift；否则标记 `NOT RUN`。
