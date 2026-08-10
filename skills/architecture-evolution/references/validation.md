# Evaluate Architecture Intent

本文件只用于显式 smoke/eval，正常运行禁止读取。

## Static smoke

检查：

- North Star 原文保持不变：目标仍是把模糊架构担忧收敛成一个有证据、有边界、可继续设计或执行的 Architecture Intent；
- 主流程仍为 `Ground → Discover → Shape → Challenge and constrain`，没有新增 target-design / execution 阶段；
- `rules.md` 继续拥有 architecture judgment / discriminator；四个 architecture directions 完整保留为内部 lens；
- `brooks-constraints.md` 继续保留 R1–R6 的 guard，但只用于 reject / narrow / guard intent，不再要求输出 Brooks table；
- `Challenge`、counterexample、taxonomy 命中和 proof vocabulary 都属于 reasoning machinery，不作为 ready intent 的最终 section；
- 最终输出跟随用户主要语言，内部英文 taxonomy 不改变用户输出语言；
- ready intent 只物化 Architecture problem、Background、Direction、Boundary，以及必要时少量 Possible target identities；
- `Possible target identities` 仍服务于一个 intent，只描述基本 ownership / semantic / dependency identity，不成为多个并列改造项目；
- decisive evidence 只保留足以解释判断的少量事实，不输出完整 commit inventory、五面审计表或 reasoning trace；
- `Real Evolution` 仍要求至少一个旧路径、旧知识、旧责任、旧判断或旧依赖真实退出；
- 不再输出 `Primary architecture direction`、`Design obligations`、`Progressive Brooks constraints`、`Challenge`、`Success evidence`、`Current snapshot evidence`；
- `Architecture intent ready` 不包含 Material Unknown；任何仍会改变 intent / boundary / target identity 的未关闭 unknown 必须返回 `Intent unresolved`；
- capability ownership 不自动推导 execution / orchestration ownership；相邻 subsystem 的合法 authoritative ownership 不因 caller reassembly 被默认吞并；
- reasoning distinction / observed partition 不能因为被命名就自动 materialize 成 type/provider/adapter/layer/public seam；
- Stop line 明确禁止 class/interface/API/adapter、具体 responsibility placement、调用/执行流、迁移步骤、implementation slice、任务拆分和 verification plan；
- 输出状态仍只有 `No architecture intent / Intent unresolved / Architecture intent ready`，且三者语义互斥；
- 不调用外部 Wayfinder、Improve、Grill、Brooks 或 Northstar Skill。

## Scenario smoke

### P1 — Business semantics direction

用户说历史模块中两条路径长期重复修改，但不确定应合并还是保留。

通过：

- 找到真正的 semantic problem identity，而不是直接建议抽象；
- 背景解释为什么两条路径形成、哪些历史前提仍有效；
- target direction 说明应形成统一 semantic owner 或保留 bounded variation；
- 如果两种基本形态都值得后续比较，可以输出 2 个 target identities，但不能决定具体 interface；
- R6/R2/R3 可以用于内部 challenge，但最终输出不出现 Brooks 编号。

### P2 — Stable abstraction direction

调用者持续按 provider/family switch，公共接口充满 mode flag 和 optional 参数。

通过：

- problem identity 指向 implementation variation 泄漏给 consumer；
- direction 指向 caller-facing stable capability / explicit essential variation；
- 不把 `Stable Abstraction with Explicit Variation` taxonomy 标签当最终方案；
- 不只输出“新增 interface/manager”。

### P3 — Cohesive ownership direction

完整能力由 caller、helper、global state 和多个生命周期对象共同拼装。

通过：

- problem identity 指向 capability usage ownership 未闭合；
- target identity 可以是 generation-scoped capability、独立 capability owner 等基本形态；
- capability ownership 不自动扩大成 orchestration ownership；
- 不规定具体 owner class、factory、runner wrapper 或调用流程。

### P4 — Dependency direction

稳定 core/Harness/Runtime 被 provider 和具体场景持续牵引，底层通过 callback 或 registry 控制上层路由。

通过：

- problem identity 指向 policy/control dependency 失配；
- direction 描述恢复稳定 policy/contract/implementation 关系；
- R5 只作为内部 challenge，不输出 dependency lint 报告；
- composition-root guard 正确应用。

### P5 — Fuzzy module direction

用户只说“这个历史模块边界混乱，下一步应该怎么演进”。代码显示重复业务判断、caller 拼装顺序和多次兼容分支修改。

通过：形成一个 intent，说明真正的架构问题、形成背景、目标方向、边界和退出目标；必要时给出少量 target identities；不直接输出 class 拆分、target design 或 Brooks 表。

### P6 — Multiple symptoms, one intent

用户列出抽象泄漏、模块过大、反向依赖和测试脆弱。

通过：找到能解释主要压力的一个 intent；其他症状作为 evidence、consequence、guard 或 out of scope，不并列成多个改造项目。

### P7 — Reality axes do not substitute for each other

源码依赖已经很干净，只有一个 Provider 接口，但 runtime resource 仍由 caller 创建和 retain，多个 consumer 各自解释 lifecycle。

通过：不能因为 dependency/type surface 干净就判断 ownership 已闭合；intent 可以指向 usage ownership 问题，并把 caller lifecycle knowledge 作为 replacement / exit。

### P8 — Consumer reassembly is evidence, not final taxonomy

consumer 必须组合 config、provider type、runtime handle 和调用顺序才能使用一个能力。

通过：识别 `consumer reassembly` 为 architecture signal；最终输出描述具体 problem / target identity，不新增 `Consumer Boundary` taxonomy，也不强制显示 Cohesive Capability Ownership 标签。

### P9 — Ownership scope follows the invariant

一个发布型 capability owner 需要闭合 generation/resource/config invariant；相邻 orchestration 当前拥有目标绑定、sequencing、并发和结果对齐。

通过：Architecture Intent 只能要求 evidence 支持的 capability closure；不得仅因 caller reassembly 把 orchestration 也纳入 owner；如果 possible target identity 提到 owner，只到 basic identity，不做具体 responsibility placement。

### P10 — Ownership closure does not imply centralization

当前 capability consumer 直接读取相邻 feature/runtime subsystem 的内部 config 与 resource；该 subsystem 自身已有清楚的 authoritative owner。

通过：intent 指向 consumer 不再重组内部事实，并形成稳定 relation/capability；不得默认把相邻 subsystem 的 config、resource、lifecycle 全部迁入当前 owner。

### P11 — ModelCurator / Hermes case

已知：ModelCurator 已拥有 published generation；FS 和 runtime-selection 已退出；prediction、prerank、item-embedding、feature-streaming 仍分别解析 feature config、借用 Hermes runner、构造 runtime context、执行并做部分结果处理；streaming 的输入和部分 config resolution 与 scoring family 不同。

通过：

- 输出语言为中文；
- problem identity 收敛为类似“publication ownership 已闭合，但 feature capability 的 usage ownership / execution protocol 仍散落在 consumers”；
- Background 解释多-runtime 历史前提已经失效，而 public boundary / consumer knowledge 未同步退出；
- Direction 指向 model-scoped feature capability 这类基本目标 identity；
- 可以保留两个值得后续设计比较的 basic identity，例如 generation-owned capability 与独立 feature-execution capability，但不得定义其 class/API/adapter/调用关系；
- scoring 与 feature-streaming 的差异作为 must-preserve / guard，不因 mechanics 相似被强制统一；
- 最终输出不出现 Brooks 五列表、R1–R6 编号、`Primary architecture direction`、Challenge、Success evidence、Material unknown 或完整 commit 清单；
- 不继续决定 projection/rehash/metadata 具体归谁，那属于 Target Design。

### N1 — Local fix

问题只是 off-by-one、日志字段、删除一个明确 dead getter 或机械迁移，且没有重复 pressure、consumer knowledge 或跨边界 structural consequence。

通过：`Status: No architecture intent`；只说明决定性证据和局部修改边界；不得发明 architecture direction、target identity 或 Brooks constraints。

### N2 — No real pressure

代码不够优雅，但没有重复变化、事故、caller friction 或明确业务需求。

通过：`Status: No architecture intent`；不得从审美和模式偏好发明 intent。

### N3 — Design already clear

用户已经给出目标 contract、模块边界、迁移步骤和验收标准。

通过：说明本 Skill 不适用；不重新生成 intent，也不把已有设计降格成 target identities。

### R1 — Evidence missing

存在多个可能方向，但无法确认消费者、变化频率或业务等价性。

通过：`Status: Intent unresolved`；指出 `Claim at risk`，只执行能改变 intent 的最小 probe，不提前输出猜测性的 target identities。

### R2 — Human decision

某兼容行为是长期业务 contract 还是迁移残留，代码无法裁决。

通过：`Status: Intent unresolved`；Human 决定必须明确对应会改变的 claim / boundary / exit，不伪造方向或退出承诺。

### R3 — No manufactured unknown

业务语义、owner boundary、consumer 和 runtime evidence 已足以支持 bounded intent，没有会改变方向的未决事实。

通过：`Architecture intent ready` 不输出 `Material unknown` section；不得为了模板完整输出 `None` 或虚构待确认项。

### R4 — Material unknown forces unresolved

当前存在一个未关闭事实：它可能改变 intent、boundary 或 target identity，例如无法确认 feature-streaming 与 scoring 是否共享同一业务语义，且不同答案会改变目标边界。

通过：必须返回 `Status: Intent unresolved`，输出 claim at risk 与最小 probe / Human decision；不得同时输出 `Architecture intent ready`，也不得把该 unknown 附在 ready artifact 后继续推进。

### L1 — Compat token is not runtime state

一个历史 token 已不再影响 runtime branch，但仍用于 parse/serialization/deployment identity。

通过：按需加载 `legacy-lenses.md`；不因 runtime 无 effect 就要求删除 token，Intent 在 `Must preserve` 或 Boundary 中保护仍有效 identity，不输出完整 legacy audit。

## Regression failures

以下任一出现即失败：

- 修改或弱化 North Star；
- 把 Architecture Evolution 扩成 Target Design / execution workflow；
- ready intent 固定输出 Brooks 表、Challenge、Primary architecture direction、Material unknown 或 verification plan；
- 同一个未关闭 material unknown 既允许 `Intent unresolved` 又允许 `Architecture intent ready`；
- 中文输入因为内部 taxonomy/reference 而输出英文主文；
- possible target identities 细化成 class/API/adapter/责任落位/调用流程；
- 为了“有方案”机械输出多个并列改造项目；
- 只因代码形状或文件大小升级为 architecture intent；
- consumer reassembly 被当成新 taxonomy，而不是 evidence；
- capability ownership 无证据扩张到 orchestration/adjacent subsystem；
- 新 facade/helper 没有 replacement/exit 却被判定为 Real Evolution。
