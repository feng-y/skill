# Evaluate Architecture Evolution

只用于显式 smoke/eval，正常 runtime 不读。本文件冻结 behavior property 与 captured regression，不是 runtime 规范源。

## Static smoke

通过需要同时满足：

- AE 仍完成 Target Architecture + architecture-level evolution，并在 ready 时自行 Compile 成薄 Architecture Program；
- `SKILL.md` 默认锚定用户指定模块，只沿直接 upstream/downstream 与会改变判断的 provider / boundary 渐进展开，不把全 repo scan 当默认 Research；
- 现有 module 名称、provider/class taxonomy、consumer partition 都只是 evidence；必须允许从真实职责重新识别 capability、boundary 与 provider；没有稳定 specific variation 时不得为了对称/扩展性制造 provider boundary；
- `rules.md` 的 architecture kernel 仍只有 Layering & dependency、Cohesion & simplicity、Abstraction vs specific、Primary vs auxiliary responsibility、Real evolution；其他维度只是 evidence lenses；
- Brooks 仍只保留 Conceptual Integrity、Essential vs Accidental Complexity、Second-System Effect 三个按需反证 lens，不形成第二套 runtime taxonomy；
- `program-contract.md` 是唯一 ready artifact owner：完整 reasoning 被 Compile 成 Structural adjustment、Long-term architecture、最多 3 个真实 Architecture Improvements、必要 Route 与 completion；不要求固定 Markdown section；
- Top Improvements 不固定凑 3 个。每个都必须有 structural change、architecture gain、real exit、done condition；research/knowledge task、愿望和 implementation step 不能冒充 improvement；优先级来自 structural leverage，而不是实现便利或描述规模；
- 如果缺失 evidence 会决定一个 change 是否真能改善结构、会改变 Target Architecture 或真实推进依赖，则必须 `Architecture unresolved`；Compile 不能隐藏 blocker；
- ready output 不泄漏完整 alternatives、Brooks trace、文件 inventory、普通 unknown 或 implementation design；
- Target Architecture / improvement outcome 可以固定长期结构，但不把 class/API/file/helper/schema/task/test provider 当 architecture law；
- 三个状态互斥：`No architecture evolution / Architecture unresolved / Architecture decision ready`。

## Scenario smoke

### P1 — Named module: bounded research topology

用户指定一个历史模块；它有若干直接 caller/downstream，并引用当前 provider/family taxonomy。

PASS：

- 先恢复模块真实职责与直接 upstream/downstream，不先扫全 repo；
- 从行为重新识别它实际提供/参与的 capability，现有 module 名不自动等于 capability；
- 重新划 capability boundary，区分 caller / adjacent subsystem / stable common / specific；
- 只有 stable specific variation 有 decisive evidence 时才形成 provider boundary；没有就保持单一 capability。需要 provider 时才逐个展开会改变 architecture judgement 的 semantics、I/O、lifecycle、state、performance/deployment difference；
- 只有 authority/SOT、serialized/config identity、repo 外 contract 等局部无法关闭且会改变 Target Architecture 时，才 targeted wider search；
- 不因“更全面”继续扫描无关模块。

### P2 — ModelCurator / Hermes: capability before current taxonomy

publication ownership 已基本闭合，但多个 consumer 仍解释 feature config / Hermes usage；streaming 与 scoring 存在真实 semantic/input/lifecycle 差异。

PASS：

- 不停在“ownership 应闭合”；重新识别稳定 feature capability 与其 boundary；
- abstraction 只覆盖稳定共同语义，真实 streaming/scoring specific 保留；
- 不按当前 consumer/provider partition 生造长期 taxonomy，也不增加 manager/provider/adapter 层级换取表面统一；
- evolution 说明新 boundary 成立后哪些旧 consumer knowledge/path 退出。

### P3 — PredictExecutor scoring: primary responsibility and provider re-identification

executor 按 family identity 分派 scoring；feature preparation、metrics/writeback、shadow/sampling 与 family-specific execution 混在路径中。

PASS：

- 先识别 scoring / orchestration 的真实 primary responsibility，而不是以 `PredictExecutor` 名称固定 boundary；
- 当前 family switch 只是 evidence，重新判断哪些差异是真 stable specific semantics，哪些只是 historical implementation difference；没有稳定 specific 时不制造 provider；
- 被 semantic judgement 判为 auxiliary 的 concern 不反向塑造主架构；真实 semantic/lifecycle/performance variation 保留；
- 若多个 materially different Target Architecture 仍可行，只用会改变核心结构判断的 evidence 裁决；不足则 unresolved；
- evolution 让 executor-side family knowledge 真实退出，而不是搬到 registry/flag matrix/DSL。

### P4 — AI-friendly layering and dependency normativity

common/core 直接依赖 scenario/provider implementation；目录表面整齐，但依赖规范只能靠文档提醒。

PASS：Target Architecture 建立可从 repo territory 读出的稳定单向 dependency boundary；值得长期约束时优先可由 module/package/build/tooling 机械表达，而不是继续增加说明文档。

### P5 — Abstraction vs specific

一组路径代码相似但业务语义/lifecycle/output contract 长期不同；另一组实现形状不同但业务 invariant 相同。

PASS：前者允许 specific，后者寻找稳定 abstraction；不能用代码相似度或 current provider/class partition 代替 semantic judgement。

### P6 — Speculative performance cannot own structure

proposal 为“可能少一次虚调用/少一个对象”把 provider-specific fast path/cache/instrumentation 打进 common primary flow，但没有 profiling/SLA/resource evidence。

PASS：默认保持 layering/cohesion/primary responsibility；只有真实 performance constraint 会改变长期 architecture choice 时才重新比较。

### P7 — Real evolution, not relocation

proposal 新增 facade/manager/registry，但旧 SOT、caller branch 与 compat path 继续 authoritative。

PASS：不能判 ready；必须说明什么旧 knowledge/authority/dependency/path 真实退出。temporary dual path 必须有 architecture purpose 与 exit condition。

### P8 — Brooks: second-system bloat

当前 pressure 已可用简单结构解决，但 redesign 又加入 plugin framework、generic registry、future hooks/modes 和 extension points；每个局部点都能解释，却无当前长期 requirement evidence。

PASS：按需读 `brooks-constraints.md`，用 Conceptual Integrity / Second-System Effect 缩小方案；保留最少 design ideas 与最窄 public surface。Conceptual integrity 不等于统一 implementation，稳定 specific variation 可以保留。

### C1 — Compile keeps only real improvements

完整 reasoning 形成 5 个候选推进点：其中 2 个只是“研究 provider 差异 / 收集 performance 数据”，3 个能直接改变长期结构并让旧复杂度退出。

PASS：Architecture Program 只保留 3 个真实 improvement；研究项不进入 Top Improvements。每个 improvement 都有 structural change、architecture gain、real exit、done condition；Route 只表达真实 architecture dependency。

### C2 — Top 3 is a ceiling, not a quota

Target Architecture 已稳定，但当前只有 2 个 bounded architecture improvements 能确定改善结构；第三个候选只是未来可能的 generalization。

PASS：只输出 2 个，不为了格式补第三个；future possibility 不物化。

### C3 — Improvement must converge

候选“先建立一层新 abstraction，后面再考虑迁移旧 path”完成后没有任何旧 knowledge/authority/dependency 退出，也没有独立结构收益。

PASS：不能进入 Top Improvements。要么收敛成一个同时产生结构收益/exit 的 bounded improvement，要么保持 unresolved；不能用纯铺垫 step 制造推进感。

### C4 — Top value means structural leverage

三个以上真实 improvement 都可推进：一个只是局部整理；一个能消除跨多个 caller 的 knowledge reassembly；另一个能先解除后续两项共同依赖的反向 boundary。

PASS：Top Improvements 优先后两者，而不是按实现成本最低、改动最大或描述最抽象排序。排序依据是能减少多少跨边界 knowledge/dependency/accidental complexity，以及是否解除后续结构性阻塞。

### N1 — Local fix stays local

问题只是 off-by-one、日志字段、dead getter、机械迁移或局部重复，不需要改变核心架构判断。

PASS：`Status: No architecture evolution`；不发明 Target Architecture / Program。

### R1 — Real architecture fork remains unresolved

两个 materially different Target Architecture 各有真实 trade-off，当前缺失一个会改变选择的 semantic/lifecycle/performance constraint。

PASS：`Status: Architecture unresolved`；指出真正缺失的 evidence / Human decision。不能按模式偏好强选，也不能把“研究该约束”塞进 Top Improvements 后假装 ready。

### L1 — Legacy identity is not runtime behavior

历史 token 不再影响 runtime branch，但可能承担 parse/serialization/deployment identity，本地没有直接 reader。

PASS：只有 Target Architecture / authority retirement 依赖它时才按 `legacy-lenses.md` 升级为 Material Unknown；不能因 local search absence 宣告可删。

### O1 — Target Architecture and Compile stop before Implementation Design

Evidence 已足以确定长期 layer/dependency、module responsibility、abstraction/specific、primary responsibility placement，并能形成真实 Architecture Improvements。

PASS：AE 可以明确 Target Architecture、improvement outcome、architecture dependency 与 structural done condition；若开始规定具体 class/API/file、flag schema、虚函数签名、MR split、patch 顺序或 verification provider，则失败。

## Captured regression properties

以下 property 来自真实 case，但不是 runtime prior：

1. consumer usage partition 是 evidence，不自动生成 consumer-specific public view/interface；
2. current provider/class/execution partition 不自动成为 stable variation taxonomy，也不能因为“应该有 provider”就制造新 taxonomy；
3. current member/switch/helper/flag residue 不自动成为 stable acceptance；判断其承载的结构 knowledge/responsibility/dependency 是否退出；
4. responsibility/variation ownership 不冻结 representation；
5. scoring-side “executor 不再拥有 family-specific execution knowledge”可以是 architecture outcome，但“必须显式声明差异”或指定 symbol 必删不是无条件 architecture law；
6. auxiliary concern 不能仅因实现方便升级为 primary architecture owner；
7. Research 默认从指定模块有限展开，而不是把 repo completeness 当成功；
8. Compile 中 research/knowledge task 不能冒充 architecture improvement；每个 improvement 都必须带来确定结构收益与 real exit。

## Paired behavioral eval

同一模型、repo snapshot、tool permission 和预算：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 `0–2`：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Research scope | 全 repo 漫游或按目录 inventory | 大致围绕模块但扩散明显 | 指定模块→直接上下游→capability/boundary→必要 specific/provider，按判断渐进展开 |
| Layering / dependency | 反向依赖仍被接受 | 大致分层但规范弱 | 层次清楚、依赖单向，稳定约束可从 repo territory 表达 |
| Cohesion / simplicity | 继续堆 helper/manager/registry | responsibility 大致集中但概念多 | capability 内聚、public surface 小、组织更简单 |
| Abstraction / specific | 过度统一、锁死历史 partition 或制造 provider | 大方向正确但 variation 理由弱 | common/specific 由稳定 semantics/invariant 决定，仅真实 variation 形成 provider |
| Primary responsibility | auxiliary concern 塑造主架构 | 主次大致清楚 | primary surface 主导结构，辅助 concern 附着且不污染 boundary |
| Real evolution | 新层叠在旧结构上 | 有部分退出 | 旧 knowledge/authority/dependency/path 明确退出，temporary complexity 有 exit |
| Compile convergence | reasoning dump、研究清单或固定 3 项 | 有推进点但收益/完成态不稳 | 最多 3 个真实 improvement，每个有 change/gain/exit/done；top value 来自 structural leverage，route 只保真实依赖 |
| Architecture altitude | 只给口号或直接进代码设计 | 能描述部分 target | 完成 Target Architecture + Program，同时保持 Implementation Design 自由 |

## V2 pass gate

1. P1–P3 / C1–C4 的 discriminator 全部正确；
2. P4–P8 / N1 / R1 / L1 / O1 的边界全部正确；
3. B 臂不能靠更长 analysis 冒充能力提升：必须表现出 bounded research、重新识别 capability/真实 variation、具体 Target Architecture 和 convergent Compile；
4. ready 必须至少有一个真实 Architecture Improvement，且不能以 research task 补数；
5. captured regression properties 1–8 全部可判定，具体 case 名词不进入 runtime；
6. README / SKILL / agent prompt / program contract 与 module-anchored Research + Compile 语义一致；
7. Brooks 能挑战局部合理但整体膨胀的 proposal，却不成为另一套 taxonomy；
8. 只有 clean-session paired Evidence 才能宣称 behavioral uplift；static/scenario review 只证明 contract/eval consistency。

## Regression failures

- `research-scope-explosion` — 指定模块任务被无证据扩大成全 repo 扫描；
- `module-shape-lock-in` — 当前 module 名称/目录被当成长期 capability boundary；
- `provider-shape-lock-in` — current provider/family/class partition 被永久化；
- `provider-manufacture` — 没有稳定 specific variation evidence 仍为对称/扩展性制造 provider boundary；
- `layering-disorder` — policy/common 继续依赖 specific implementation；
- `cohesion-loss` — responsibility 被 helper/manager/registry 分散或概念膨胀；
- `false-abstraction` — 不同稳定语义被强行统一；
- `auxiliary-takes-over` — auxiliary/speculative performance 扭曲 primary architecture；
- `first-shape-wins` — 第一个 plausible shape 直接成为 decision；
- `fake-alternatives` — representation 差异冒充 design space；
- `complexity-relocation` — 旧结构消失但 knowledge/branch/adapter 只是搬家；
- `authority-duplication` — 新旧 SOT 长期并存；
- `compile-as-summary` — Compile 只是压缩 reasoning，没有形成可推进 architecture outcomes；
- `non-improving-top-item` — Top Improvement 完成后结构没有确定变好或没有 real exit；
- `research-as-improvement` — “研究/确认/收集数据”进入 Top Improvements；
- `forced-top3` — 不足 3 个真实 improvement 时为补数制造 future work；
- `value-by-convenience` — Top Improvements 按容易实现/改动大/叙述宏大排序，而不是 structural leverage；
- `roadmap-ceremony` — 无 architecture dependency 仍强制串行路线；
- `representation-freeze` — architecture judgement/Program 被物化成固定 class/API/flag/schema/虚函数；
- `evolution-as-task-plan` — architecture evolution/route 退化成文件/MR/test/发布步骤；
- `permanent-transition` — adapter/dual path/compat 没有 exit condition；
- `premature-implementation-design` — AE 阶段规定具体实现；
- `abstract-intent-stop` — 只说“内聚/单向依赖”就 ready，没有 Target Architecture / Program；
- `unknown-swallowed` — Material Unknown 被偏好或 Compile 隐藏；
- `output-protocol-regression` — judgement/Brooks/reasoning trace 被要求进入最终结果。

Static/scenario smoke 只证明文本 contract 与 frozen properties 一致；没有 clean-session paired run 时，behavioral uplift 必须标记 `NOT RUN`。
