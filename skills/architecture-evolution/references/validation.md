# Evaluate Architecture Evolution

只用于显式 smoke/eval，正常 runtime 不读。本文件冻结 behavior property 与 captured regression，不是 runtime 规范源。

## Static smoke

通过需要同时满足：

- North Star 仍允许 AE 完成 Target Architecture + architecture-level evolution，而不是退回 abstract intent；
- `SKILL.md` 只拥有 stance、适用边界和三种终态，不要求固定 reasoning stage；
- `rules.md` 的 architecture kernel 只有五个主判断：Layering & dependency、Cohesion & simple organization、Abstraction vs specific、Primary vs auxiliary responsibility、Real evolution；
- `change locality / knowledge / SOT / control / lifecycle / variation / complexity relocation` 只作为 evidence lenses，不与五个主判断平级，也不要求逐项输出；
- `decision-contract.md` 只定义 ready decision 的语义义务，不要求固定 Markdown section 或 judgment taxonomy；
- Target Architecture 可以固定长期 layer/dependency、module responsibility、abstraction/specific、必要 authority/control/lifecycle/variation boundary，但不把 class/API/file/helper/schema/task/verification provider 当 architecture law；
- alternatives 只有 materially different architecture fork 才出现，不要求固定数量；同一 responsibility/boundary 的命名、类层次或文件布局不算不同 architecture；
- 未经 profiling/SLA/resource evidence 证明的“可能性能更好”不能无条件覆盖 layering、cohesion、abstraction 或 primary-responsibility judgement；
- ready decision 必须说明真实 structural exit 与 architecture-level evolution；temporary adapter/dual path/compat 必须有 architecture purpose 与 exit condition；
- 三个状态互斥：`No architecture evolution / Architecture unresolved / Architecture decision ready`；
- legacy 与 Brooks 都只是按需 lens；captured case wording 不进入 runtime。

## Scenario smoke

### P1 — ModelCurator / Hermes: abstraction and cohesion

已知：publication ownership 已基本闭合，但多个 consumer 仍解释 feature config / Hermes usage；streaming 与 scoring 存在真实 semantic/input/lifecycle 差异。

PASS：

- 不停在“ownership 应闭合”这类口号；明确哪个 module/capability 应成为主要责任面，以及哪些 consumer knowledge 应退出；
- abstraction 只覆盖稳定共同语义，真实 streaming/scoring specific 保留；不按当前 consumer/provider partition 生造长期 taxonomy；
- target repo 组织应比当前更容易解释，不能用更多 manager/provider/adapter 层级换取表面统一；
- 若存在 materially different 的长期 boundary 方案才比较；evidence 不足以选则 `Architecture unresolved`；
- evolution 说明新 boundary 成立后哪些旧 knowledge/path 退出，不展开 class/API/MR task。

### P2 — PredictExecutor scoring: primary responsibility over auxiliary concerns

已知：executor 按 family identity 分派 scoring；抽取前奏、metrics、score writeback、shadow/sampling 等逻辑散落在路径中，部分 family 有真实调用差异。

PASS：

- switch/member/helper 只是 evidence；architecture problem 要落到 layering/cohesion/abstraction/responsibility，而不是要求指定 symbol 必删；
- 先识别 scoring 的 primary responsibility，再判断 metrics/shadow/sampling/debug/compat 等 auxiliary concern 是否扭曲主结构；不能因为 auxiliary concern 组合不同就直接把每个 family 永久 specific；
- 真实 semantic/lifecycle/performance variation 保留，历史 implementation difference 不自动成为 architecture variation；
- 若 declarative、behavior-owned、compiled 等 materially different Target Architecture 都可行，用五个核心判断比较；不能因当前代码更像某一种就强选；
- “variation 归正确 boundary”不能自动物化成 flag/metadata/虚函数；
- evolution 要让 executor-side family knowledge 真正退出，而不是搬到新 registry/flag matrix。

### P3 — AI-friendly layering and dependency normativity

一个 repo 的 common/core 层直接依赖 scenario/provider implementation；目录与接口表面整齐，但规则只能靠文档提醒“不再继续反向依赖”。

PASS：Target Architecture 应建立清楚、可从 repo territory 读出的单向 dependency boundary；若稳定到值得长期约束，优先能由 module/package/build/tooling 机械表达，而不是增加更多说明文档。不能以“当前能工作”为理由保留 policy→specific 反向知识。

### P4 — Abstraction vs specific

两条路径代码高度相似，但其业务语义、lifecycle 或 output contract 长期不同；另有两条实现形状不同但业务 invariant 完全相同。

PASS：前者允许保持 specific，后者应寻找稳定 abstraction；不能用代码相似度或当前 class/provider partition 代替 semantic judgement。

### P5 — Auxiliary performance does not own the architecture

一个 proposal 为了“可能少一次虚调用 / 少一个对象 / 更快一点”把 provider-specific fast path、cache state 或 instrumentation 直接打进 common primary flow，但没有 profiling、SLA 或资源 evidence 证明这会改变长期架构选择。

PASS：默认保持清晰 layering、cohesion 与 primary responsibility，让辅助优化附着于主结构；只有真实 performance constraint 成为长期 force 时才允许重新比较 architecture trade-off。不能以 speculative performance 为由永久污染主 boundary。

### P6 — Real evolution, not relocation

一个 proposal 新增 facade/manager/registry，但旧 source of truth、caller branch 与 compat path 全部继续 authoritative。

PASS：不能判 ready；必须说明什么旧 knowledge/authority/dependency/path 真正退出。temporary dual path 必须有 exit condition，否则只是 complexity relocation。

### N1 — Local fix stays local

问题只是 off-by-one、日志字段、dead getter、一次机械迁移或局部重复，没有持续 structural pressure，也不需要改变五个核心架构判断中的任何一个。

PASS：`Status: No architecture evolution`；不发明 Target Architecture 或 alternatives。

### R1 — Real architecture fork remains unresolved

两个 materially different Target Architecture 在五个核心判断上各有真实 trade-off；当前 evidence 尚不能确认一个会改变选择的 semantic/lifecycle/performance constraint。

PASS：`Status: Architecture unresolved`；指出真正缺失的 evidence / Human decision。不能按模式偏好或“更优雅”强选一个。

### L1 — Legacy identity is not runtime behavior

一个历史 token 已不再影响 runtime branch，但仍可能承担 parse/serialization/deployment identity；本地搜索没有直接 reader。

PASS：按需读取 `legacy-lenses.md`；只有 Target Architecture / authority retirement 依赖它时才升级为 Material Unknown。不能因 runtime retirement 或 local search absence 宣布 identity 可删除。

### O1 — Target Architecture altitude

Evidence 已足以判断长期 layer/dependency、module responsibility、abstraction/specific 与 primary responsibility placement；Implementation Design 尚未开始。

PASS：允许 AE 明确这些结构关系及必要 authority/lifecycle boundary，并形成 architecture-level evolution；但若开始规定具体 class/API/file、flag schema、虚函数签名、patch 顺序或 verification provider，则失败。

## Captured regression properties

以下是 case 暴露出的 property，不是 runtime prior：

1. consumer usage partition 是 evidence，不自动生成 consumer-specific public view/interface；
2. current provider/class/execution partition 不自动成为 stable variation taxonomy；
3. build/test/replay/diff 不冻结为 architecture acceptance provider；
4. existing upper architecture goal 可以成为当前约束/evidence，但不建立新的 goal-discovery protocol；
5. current member/switch/helper/flag residue 不自动成为 stable acceptance；判断它承载的结构性 knowledge/responsibility/dependency 是否真正退出；
6. responsibility/variation ownership 不冻结 representation；
7. scoring-side captured case 中，“executor 不再拥有 family-specific execution knowledge”可以是 architecture outcome，但“必须显式声明差异”或“指定 symbol 必须消失”不是无条件 architecture law；
8. auxiliary metrics/debug/compat/performance concern 不能仅因实现方便就升级为 primary architecture owner。

## Paired behavioral eval

同一模型、repo snapshot、tool permission 和预算：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 `0–2`：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Layering / dependency | 反向依赖或边界含混仍被接受 | 大致分层但依赖规范弱 | 层次清楚、依赖单向，稳定约束可从 repo territory 表达 |
| Cohesion / simplicity | 继续堆 helper/manager/registry | responsibility 大致集中但概念多 | 主要 capability 内聚、public surface 小、组织明显更简单 |
| Abstraction / specific | 过度统一或锁死历史 partition | 大方向正确但 variation 理由弱 | common 与 specific 由稳定 semantics/invariant 决定 |
| Primary responsibility | auxiliary concern 反向塑造主架构 | 主次大致清楚 | primary surface 主导结构，辅助 concern 附着且不污染 boundary |
| Real evolution | 新层叠在旧结构上 | 有部分退出 | 旧 knowledge/authority/dependency/path 明确退出，temporary complexity 有 exit |
| Decision quality | 第一个模式即答案 | 有 alternatives/trade-off 但理由一般 | 仅在真实 fork 时比较，并用上述结构判断 + decisive evidence 选择或 unresolved |
| Architecture altitude | 只给口号或直接进入代码设计 | 能描述部分 target | 完成 Target Architecture，同时保持 Implementation Design 自由 |
| Evidence discipline | 猜测、无限研究或 speculative performance | 有 evidence 但影响不清 | 只使用会改变架构判断的 evidence；性能无证据不劫持主结构 |

## V2 pass gate

1. P1 / P2 的 B 臂在五个核心 architecture dimension 合计至少高于 A 臂 3 分，且没有新增 0 分退化；
2. P3–P6 / N1 / R1 / L1 / O1 的 discriminator 与停止边界全部正确；
3. B 臂不能只把旧 Architecture Intent 写得更长，也不能靠输出更多 analysis dimension 冒充能力提升；
4. ready result 可以完成 Target Architecture，但不能泄漏 Implementation Design；
5. captured regression properties 1–8 全部可判定，且具体 case 名词不出现在 runtime；
6. README / SKILL / agent prompt / decision contract 与 compact kernel 一致；
7. 只有 clean-session paired Evidence 才能宣称 behavioral uplift；static/scenario review 只证明 contract/eval consistency。

## Regression failures

- `pressure-free-architecture` — 从审美发明 architecture work；
- `local-escalation` — local problem 被升级成 architecture evolution；
- `layering-disorder` — policy/common 继续依赖 specific implementation，或依赖方向只能靠口头约定；
- `cohesion-loss` — responsibility 被 helper/manager/registry 分散，组织复杂度上升；
- `false-abstraction` — 不同稳定语义被强行统一；
- `historical-specific-lock-in` — 当前 provider/class partition 被永久化；
- `auxiliary-takes-over` — metrics/debug/compat/cache/speculative performance 扭曲 primary architecture；
- `first-shape-wins` — 第一个 plausible shape 直接成为 decision；
- `fake-alternatives` — 同一 architecture 的 representation 差异冒充 design space；
- `complexity-relocation` — 旧结构消失但 knowledge/branch/adapter 只是搬家；
- `authority-duplication` — 新旧 SOT 长期并存；
- `representation-freeze` — architecture judgement 被物化成固定 class/API/flag/schema/虚函数；
- `evolution-as-task-plan` — architecture evolution 退化成文件/MR/test/发布步骤；
- `permanent-transition` — adapter/dual path/compat 没有 architecture exit condition；
- `premature-implementation-design` — Target Architecture 阶段规定具体实现；
- `abstract-intent-stop` — 只说“内聚/单向依赖/ownership 应闭合”就宣布 ready，没有具体 Target Architecture；
- `unknown-swallowed` — Material Unknown 被偏好填补；
- `unknown-manufacture` — 不改变 architecture decision 的 unknown 被升级成 blocker；
- `output-protocol-regression` — 五项 judgment、Brooks、评分或 reasoning trace 被要求进入最终结果。

Static/scenario smoke 只证明文本 contract 与 frozen properties 一致；没有 clean-session paired run 时，behavioral uplift 必须标记 `NOT RUN`。
