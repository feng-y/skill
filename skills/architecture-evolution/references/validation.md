# Evaluate Architecture Evolution

只用于显式 smoke / eval；正常 runtime 不读。本文件冻结行为属性和回归案例，不定义 runtime。

## Static smoke

1. 主 Skill 保持 `research → judgment → anchor / focus → delivery`，没有 ready / completed / status lifecycle，也没有第二份 output / compile contract。
2. `strategic-design.md`、legacy、Brooks 都有独立 trigger，正常路径不要求全部加载；不存在只重复主 Skill 判断的通用 rules reference。
3. `agents/openai.yaml` 只是 thin invocation pointer；validation / regression 不进入 runtime。
4. AE 停在 architecture outcome / structural done condition；除非 authority 已绑定 representation，不固定 class / API / file / schema / MR / test provider。
5. 收敛后的当前 Program 同文写入 repo / workspace 外 handoff file；写入失败就是 blocker，handoff artifact 不替代 repo architecture SOT。

## Behavior properties

1. 当前 module / capability taxonomy、provider / layer 等表示只是 Evidence，不先验定义 Target Architecture。
2. Strategic Design 是核心 judgment：从 repo identity / architecture intent、领域语义、durable change 和真正 architecture-significant 的 binding constraints 恢复长期能力与责任；复杂或高频变化的辅助关注点不能自动塑造主架构。
3. capability boundary 应拥有并隐藏长期 design knowledge / decision，使对应变化在 owner 内被吸收；只有会改变 Target 的 authority / semantic / lifecycle / isolation 关系才需要显式，再设计 dependency direction。主要行为及完成变化所需的关键判断若长期必须跨无关责任或隐含知识重建，是 boundary / knowledge placement 可能未闭合的 Evidence，不是独立架构目标。
4. Target 必须包含当前 Evidence 已足以支持、未来仍会复用且会改变后续判断的战略事实，并保持最小充分；不把 reality 合理化成 Target，也不预编未来 capability / provider / layer / hook。
5. Program 是 Target 在当前 reality 上集中推进的一条演进主线。Target gap 先压缩成不超过 3 个高价值演进锚点作为 attention funnel；锚点不是 backlog。迁移成本、局部实现 pressure、执行风险与已有 patch 只决定聚焦什么和推进到哪里，不反向定义 Target；binding roadmap、durable change pressure 与长期承诺可以改变 Strategic Design。
6. abstraction 由 stable semantics / invariants 决定；能力和责任边界成立后再设计稳定单向依赖，通用语义不依赖具体实现。
7. 当前 Program 必须物化已确认的战略结构：责任更闭合、caller 更少重组私有事实、coupling 更低、dependency / information hiding 更稳定，并产生 structural gain + real exit。同一 responsibility / authority correction 的多个锚点若拆开仍保留同一个旧 authority / path，应先聚合再决定当前 focus；独立责任不能为集中而强行吞并。
8. real evolution 要求旧 authority / knowledge / dependency / special path 退出；已被结构替代的补偿性 guidance 同样退出。只增加新层而旧结构仍 authoritative 是 complexity relocation。
9. Research 只由仍未解决、且会 materially 改变当前架构判断（包括 Target / Program）的明确 fork / Unknown 驱动；每个新增 probe 必须能区分 material alternatives。若两个长期结构都能被现有 Evidence 支持、继续 prose judgment 不能提高区分度，而一个廉价、可丢弃的 structural probe 能直接挑战 boundary / ownership hypothesis，则做最小 probe；probe 只产生当前判断需要的 Evidence，不自动进入 Program、production path 或 architecture SOT。Evidence 足够后停止扩搜，已有 Evidence 默认跨 judgment 复用，除非其前提被新 Evidence / Human decision 推翻，不为新的 judgment pass 重扫 repo。
10. 当前 org / team topology 只作 reality / feasibility challenge，不自动成为长期 architecture law。
11. specialist 不抢 Human decision ownership；若剩余 material fork 本质是业务、兼容、风险、投入或 ownership 等 Human-owned trade-off，而非可继续调查的事实问题，就停止 autonomous research，返回 Evidence、best-known recommendation、真实选项和 decision surface。
12. 稳定战略设计结论优先维护原 authoritative architecture source；delivery 交当前 Strategic Design、必要的 Target 变化与已收敛的当前 Program。material correction / Human decision 后保留仍有效 Evidence / Target，只重算受影响判断；只有前提失效才重查对应 Evidence，并完整重交付。

## Regression cases

### Strategic Design

- **P1 Fork-driven research**：历史模块 + current provider taxonomy → 先恢复足以约束当前范围的最小 repo identity / architecture intent；之后只有明确且会 materially 改变当前架构判断（包括 Target / Program）的 unresolved fork / Unknown 才驱动继续扩搜，每个 probe 都必须能区分 material alternatives。现有 Evidence 足够后停止，不得为了“战略设计更完整”展开全 repo inventory，也不把相关 Unknown 强制串行化。
- **P2 Current shape is not Target**：历史模块 `X` 内部可以整理得自洽，但 repo identity、真实 consumer 与长期变化表明这里实际承载更大的 capability，或一部分应属于其他 owner → 不得把 `X` 当长期 boundary 后继续局部优化。
- **P3 Provider variation**：存在 family switch → 只有 stable semantic / contract / lifecycle / performance architecture / deployment variation 才形成 provider boundary；当前命名、代码相似或未来扩展愿望不够。
- **P4 Boundary before dependency**：`common/core → specific implementation` 或依赖图可被整理成单向 → 先确认长期 responsibility / capability decomposition 正确；单向依赖不能挽救知识仍散落在错误 owner 的结构。
- **P5 Abstraction**：代码相似但 semantics 不同 / 实现不同但 invariant 相同 → 前者保持 specific，后者才抽象 stable invariant。
- **P6 Binding quality / operational constraint**：logging / metrics 很复杂或性能看起来重要，但没有 authoritative SLO / isolation / rollout 等长期 Evidence → 不得让辅助 concern 塑造主架构。反之，binding latency SLO、fault isolation、zero-downtime rollout 若真实改变 responsibility / lifecycle / deployment / failure boundary，则必须进入 Strategic Design。
- **P7 Hidden design decision**：A、B 都能形成表面高内聚模块；A 仍让 caller 理解 backend selection / config / lifecycle 等会独立变化的私有决定，B 让 capability owner 独占并隐藏这些知识 → A 的 boundary 不成立。
- **P8 Boundary relationship**：能力 A / B 的 owner 和 dependency direction 已明确，但真实 workflow 仍要求语义翻译、独立 authority 或 lifecycle coordination / isolation，且这些关系会改变失败或变化传播 → Target 不能只画 `A → B`；若没有这种 material relationship，也不得为了完整图谱强行枚举 taxonomy。
- **P9 Minimal sufficient Target**：Evidence 只足以确定 A / B 的长期能力与 boundary，未来 C / provider / layer 尚不改变当前判断 → Target 只固定 A / B；但任何已证明会长期改变判断的 constraint / relationship 都不能为了“极简”被省略。
- **P10 Architecture source is Evidence, not oracle**：现实与已有 architecture source 冲突 → 判断是实现漂移还是 source 前提已失效；既不能因 reality 已存在自动覆盖 intent，也不能因旧文档存在强行把系统拉回过时目标。
- **P11 Strategic design before persistence**：repo 没有 architecture doc，但 identity、领域责任、authority、lifecycle 与长期 variation 已有足够 Evidence → 先形成当前最可信 Strategic Design；是否持久化是后续判断，不能因缺文档停止，也不能自动创建全量 `ARCHITECTURE.md`。
- **P12 Scoped strategic design**：当前只处理 runtime / provider → 恢复足以判断其在 repo 中预期角色的战略锚点，再只设计该范围；不得因为需要 repo identity 就生成全 repo blueprint。
- **P13 Capability boundary is not enough**：跨 capability responsibility 已清楚，但某 capability 内部仍让稳定语义依赖具体实现，或长期设计知识继续泄漏 → Target 不得停在 capability boundary；继续收敛内部稳定语义与允许依赖。
- **P14 Organization is a challenge, not law**：当前 team 恰好按 `X/Y` 分工或跨团队沟通很贵 → 可作为 feasibility / friction Evidence，但不能仅据 org chart 固化 Target boundary。若 Target 需要现实中不存在的 owner / coordination path，应暴露组织或 rollout 依赖，而不是默认改写责任模型。
- **P15 Evidence reuse**：一次 probe 已确认 capability owner、lifecycle 与真实 consumer，随后 dependency / abstraction / verification judgment 仍基于同一前提 → 默认复用已获得 Evidence，不重新打开同一批文件；只有新的 material fork 或 Evidence 表明原前提可能失效时，才重查受影响部分。
- **P16 Falsifiable Target / structural probe**：repo identity、authority 与长期变化同时支持两个 materially different 的 ownership Target；继续读同一批代码或写更多设计 prose 都不能区分，但迁一个代表性 consumer 就能观察它是否仍需穿透旧 owner 的私有 knowledge → 只做这个最小、可丢弃的 migration slice 作为 probe。按候选 boundary 完成 slice 后，若 consumer 仍需旧 owner internals，就把它作为候选 boundary 的 disconfirming Evidence 并只重算受影响 Target；migration 过渡期同时修改 old / new owner 本身不算失败。若新 boundary 成立，也只把结论 / Evidence 合回 Strategic Design。不得因为 probe 代码存在就把它自动升成 Program、production path、长期 provider / layer 或 architecture SOT；已有 Evidence 已足够区分时也不得为了“验证感”强制做 probe。

### Evolution and leverage

- **V1 Low-value cleanup**：候选 change 能删 helper / namespace 或减少表面 dependency，但同类真实变化仍必须跨原 owner / authority / verification surfaces → 不得仅因代码更整洁成为高价值演进锚点。
- **V2 Positive leverage**：Strategic Design 确认某类 knowledge / authority 本应由一个 capability owner 闭合；候选锚点让同类变化从多个 owner 收敛到一个 owner，并让旧跨边界 path 退出 → 即使 patch 不大，也属于高价值 Architecture Evolution anchor。
- **V3 Planned pressure is Evidence**：已批准 roadmap / binding requirement 已明确未来一类变化，即使尚未重复发生，也可支撑长期 boundary / variation 判断并提高当前锚点优先级；“以后可能有用”的猜测不算。
- **V4 Durable leverage**：一次性 migration 当前跨多个 owner，但完成后没有持续 pressure、重复变化或 binding future requirement → 不得仅凭本次 propagation compression 晋级长期 Architecture Improvement。
- **V5 Structural friction without repeated feature change**：主要行为长期必须跨多个不相干 owner 才能理解 / 验证，需求也无法沿责任边界切分，并且持续违反最可信 Strategic Design → 可以升级为架构问题，不要求先观察多次 feature change。
- **V6 Smell without architectural tension**：大文件、复杂分支、重复或测试 setup 很重，但 responsibility / authority / dependency 与 Strategic Design 一致且没有持续结构摩擦 → 不得仅凭 smell 改 architecture。
- **V7 Requirement-shaping false positive**：需求本身混合多个独立业务结果或 ownership 尚未决定 → 先回到 requirement shaping，不能据此重塑架构。
- **V8 Testability false positive**：测试慢或 setup 重来自外部环境、集成基础设施或数据准备，而主要行为仍能从正确责任边界验证 → 不得仅凭测试成本改 boundary。
- **V9 Local cohesion cannot rescue wrong identity**：候选 A 让历史模块 `X` 更内聚、依赖更单向，但仍把 identity-level capability 拆在 `X/Y/Z`；候选 B 先重划 capability boundary → A 不能因局部结构漂亮成为 Target。
- **V10 Legibility is evidence, not objective**：fresh implementer 需要较多搜索才能理解某 capability，但责任、authority、dependency 与 verification 都由正确 owner / authoritative source 稳定表达，额外成本主要来自 repo 规模、tooling 或领域固有复杂度 → 不得为了“agent 更容易读”重塑 architecture。反之，若每次都必须跨无关责任重建同一私有知识或依赖隐含、非权威事实，才把它作为 boundary / knowledge placement 的 Evidence。

### Program selection and completion

- **E1 Target gap is not obligation**：Strategic Design 识别多个长期 gap，其中一些当前没有真实 / 已明确未来 pressure，或迁移风险远高于当前结构收益 → Target 保持不变，但这些 gap 可以延期、保留或等待 Evidence，不自动进入 Program。
- **E2 Best next move**：A、B 都符合 Target；A 更接近最终形态但当前收益低，B 能解除正在发生的结构摩擦并让旧 authority / path 退出 → 当前优先 B，不因此把 B 的局部形态抬成新 Target。
- **E3 Tactical pressure cannot redefine Target**：Target 已确认 capability `X` 应拥有某类 knowledge / lifecycle，但完整迁移当前很贵 → 可以局部推进、延期或不改 repo；不得把现有跨 `X/Y` ownership 重新解释为长期正确结构。
- **E4 Materialization**：Target 已确认一个 capability / provider boundary；当前 Program 只新增接口或目录，但 caller 仍重组私有 knowledge、specific implementation 仍反向影响 stable layer、旧 switch / path 仍 authoritative → 不得判为有效 evolution。
- **C1 Anchor quality**：research / data collection 不成为演进锚点；只有对应已确认战略结构上的 material correction，且有真实 pressure、durable change pressure 或可产生 durable structural leverage 的切入点，才进入高价值锚点集合。
- **C2 Attention ceiling**：候选很多 → 在进入关系判断前只保留不超过 3 个高价值锚点；只有 2 个就保留 2 个，不补数。这个上限限制 attention，不要求最终交付 3 个项目。
- **C3 Setup-only**：先建 abstraction、以后再迁；如果当前不产生 gain / exit → 不得成为当前 Program。
- **C4 Leverage**：多个真实锚点 → 优先显著减少同类 change 和关键判断必须跨越的 owner / authority / dependency / verification surface，而不是最易实现、最整洁或只减少表面 dependency 的项。
- **C5 SOT**：已有 authoritative architecture source → 引用原 SOT；需要演进时更新原处，不建平行规范。
- **C6 Aggregate one correction**：config ownership、lifecycle ownership、runtime behavior ownership 被识别成 3 个锚点，但 Evidence 表明它们都来自 capability `X` 未成为真实 owner，且任何一个单独推进都会让 caller 继续持有同一 authority / private knowledge → 不得按 3 个 backlog item 平铺；聚合成一个围绕 `X` ownership closure 的当前演进主线，再界定当前可产生 real exit 的切面。
- **C7 Do not over-aggregate**：provider ownership、logging isolation、deployment boundary 位于相邻代码且都值得改，但长期语义、authority / lifecycle 与 structural gain / exit 各自独立 → 不得因为“集中推进”吞成一个大重构；分别保留为独立锚点，只选择当前最高价值 focus。
- **C8 Focus convergence**：已经得到 3 个高价值锚点 → 不能把三项直接当 Program 交付。先判断聚合关系和 leverage，通常收敛到一个当前 focus，并继续 shaping 其 architecture outcome、责任、边界、依赖、structural done condition 与 real exit；其余锚点只有在会改变当前判断时保留，而不是默认 backlog。

### Boundaries and re-entry

- **N1 Local**：bug / dead getter / mechanical cleanup → local judgment，不制造 Target / Program。
- **R1 Real fork**：默认形成一个 best-known Target；只有两个 materially different 长期结构都被 Evidence 支持、且最小 probe 后仍缺 decisive constraint 时才同时保留，不能为了“方案比较”主动制造候选。
- **H1 Human-owned fork**：剩余 material fork 取决于业务、兼容、风险、投入或 ownership 等 Human-owned choice，而不是更多 repo Evidence → 立即停止 autonomous research，返回当前 Evidence、best-known recommendation、真实 alternatives 与 decision surface；Human 决定后沿单一路径继续，不重新分析已淘汰方向。
- **L1 Legacy**：旧 token / identity 本地无 reader 但可能外部可见 → search absence 不等于可删；只有能否退出会改变 Target / Program 时做最小 probe。
- **O1 Altitude**：Target 已稳定 → 固定 architecture outcome / structural done condition，不规定 class / API / file / schema / MR / test provider。
- **D1 Re-entry**：Program 交付后出现 material correction / Human decision → 保留仍有效 Evidence / Target，只重算受影响 Strategic Design / Program；只有新 Evidence 使原前提失效时才重查对应部分，并完整重交付。
- **D2 Artifact failure**：Program 已收敛但外部 handoff file 不可写 → blocker，不把 conversation 当成功 handoff。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget：
`A. 不加载 architecture-evolution` vs `B. 加载 architecture-evolution`。

评分：Research scope、research-stop quality、Evidence reuse、repo-identity grounding、strategic-focus、strategic-design quality、architecture-hypothesis falsifiability、structural-probe quality、hidden-knowledge boundary、boundary-relationship quality、target-sufficiency、strategic/tactical separation、Human convergence、change-pressure alignment、intent/reality discrimination、architecture taste、anchor ranking / aggregation、focus convergence、Program leverage、boundary-knowledge recoverability、architecture altitude、re-entry、handoff integrity、context cost。

同时记录 total / tool-return token、probe 数、文件读取数与重复读取；只有在 architecture judgment 不退化的前提下，较低成本才算改进。只有 clean-session paired Evidence 才能声明 behavioral uplift；否则标记 `NOT RUN`。