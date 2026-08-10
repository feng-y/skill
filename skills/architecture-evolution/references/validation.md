# Evaluate Architecture Intent

只用于显式 smoke/eval，正常运行不读。

## Static smoke

通过需要同时满足：

- North Star 原文不变；
- 主流程仍是 `Ground → Judge → Shape → Challenge`；
- `SKILL.md` 主要拥有 Flow，`rules.md` 主要拥有 architecture judgement，`intent-contract.md` 只拥有输出形状；
- upper-goal 只是一条 conditional discriminator：已有明确覆盖当前 area 的有效上位 goal 时保留其贡献；否则从 pressure 收敛 durable outcome，不新增目标来源字段、全局搜索前置条件或 goal 层级协议；
- 四个 architecture directions 仍可用于内部 diagnosis，但不要求输出 taxonomy；
- Brooks 只用于 challenge judgement，不形成最终 section；
- ready intent 的物理 section 只有 Problem / Background / Direction / Boundary；`Stable acceptance rule` 位于 Direction，Possible shapes 仅按需出现；
- stable acceptance 只描述 outcome / boundary / replacement 何时成立，不固定 lint/test/evidence provider；具体验证方法属于下游；
- 未关闭且会改变 intent / boundary 的 Material Unknown 只能返回 `Intent unresolved`，ready 不携带 active Material Unknown；
- 最终输出跟随用户主要语言；
- 三个状态保持互斥：`No architecture intent / Intent unresolved / Architecture intent ready`；
- 不进入具体 Target Design；
- `agents/openai.yaml` 不重新引入旧的 design-obligation / Brooks-output / success-evidence 协议；
- 本文件和 `materialization-regression.md` 都只属于 eval，正常 runtime 不读。

## Scenario smoke

### P1 — ModelCurator / Hermes

已知：FS/runtime-selection 已退出；ModelCurator 已拥有 published generation，但 prediction、prerank、item-embedding、feature-streaming 仍各自解释 feature config、Hermes lifecycle 和固定执行协议；streaming 与 scoring family 存在真实输入/config 差异。

通过：

- problem 收敛到 publication ownership 已闭合、usage knowledge 仍散落在 consumers；
- background 解释多-runtime 历史前提失效而 consumer knowledge 未退出；
- direction 指向稳定 model-scoped feature capability；
- stable acceptance 说明 consumers 不再拥有 feature config / Hermes usage protocol，同时真实 streaming/scoring semantic difference 被保留；
- 可以简要点出 generation-owned / independent execution capability 这类 basic shape；
- 不决定 class/API、projection/rehash/metadata owner、调用流、migration 或验证套餐；
- 最终主文为中文，不出现 Brooks/taxonomy/challenge 表。

### P2 — False unification / ownership overreach

两个 consumer mechanics 相似，但属于不同 bounded context；相邻 runtime subsystem 已有正确 authoritative owner。

通过：不能因代码相似就统一业务语义，也不能因 caller reassembly 就把相邻 subsystem 的 config/resource/lifecycle 全部迁入当前 owner。

### P3 — Upper goal over local target

repo 已有仍有效且明确点名当前 area 的 architecture/evolution goal；局部 capability ownership / stable interface 本身合理，但只描述 target shape。

通过：Intent 说明该 area 对既有上位 goal 的贡献，局部 ownership/interface/dependency 收紧只作为结构杠杆；不新增目标来源字段、全局搜索前置条件或 goal 层级规则。若不存在已声明目标，则从跨边界 pressure 收敛最小 durable outcome，不发明战略口号。

### P4 — Stable acceptance without provider freeze

Direction、Boundary 和 Replacement / exit 已稳定，repo 同时存在 build/test/replay/dependency probe 等验证手段。

通过：Intent 只写一个 outcome-level stable acceptance rule；具体验证 provider 留给后续 design/implementation 根据最终 change surface 选择，不冻结当前 app/target/config 列表。

### N1 — Local fix

问题只是 off-by-one、日志字段、dead getter 或机械迁移，没有重复 pressure、consumer knowledge 或跨边界 structural consequence。

通过：`Status: No architecture intent`；不发明 architecture direction。

### R1 — Material unknown

一个未关闭事实会改变 intent 或 boundary，例如无法确认两条路径是否属于同一业务语义。

通过：`Status: Intent unresolved`；指出 claim at risk 和最小 probe / Human decision，不同时返回 ready。

### L1 — Legacy identity is not runtime behavior

一个历史 token 已不再影响 runtime branch，但仍可能承担 parse/serialization/deployment identity；本地搜索也没有直接 reader。

通过：按需读取 `legacy-lenses.md`；不因 runtime retirement 或 local search absence 宣布 identity 可删除。只有当前 replacement/exit 依赖该 identity 时才升级为 Material Unknown，否则放入 Must preserve 或 out of scope。

### O1 — Stop before Target Design

证据已经足够形成 direction，用户没有要求完整设计。

通过：输出到 architecture direction / basic shape 即停止；若开始决定 module/class/API、responsibility placement、调用流、migration、implementation 或验证 provider，即失败。

## Paired behavioral eval

同一模型、repo snapshot 和预算：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 `0–2`：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Pressure grounding | 从审美或模式偏好出发 | 有部分 evidence | 真实 pressure、decisive evidence 和 boundary 清楚 |
| Reality separation | 用单一接口/依赖信号替代整体判断 | 部分区分 | semantics/ownership/consumer/dependency/runtime 按需要分开判断 |
| Architecture judgment | local/architecture 混淆或 solution-first | 大方向合理但根因不稳 | 正确裁决 architecture vs local，并形成一个 evidence-backed direction |
| Durable outcome | 局部 target shape 冒充 outcome | why 大致成立但下游仍需重建 | why/direction/boundary 已稳定；有明确上位 goal 时说明 area 贡献，否则从 pressure 得出最小 durable outcome |
| Invariant quality | class/API/library 被当成架构规范 | boundary 大致清楚 | 少量 stable invariant/boundary + 明确 local autonomy，且不提前设计 enforcement |
| Ownership scope | 从 reassembly 直接扩张 owner | scope 大致正确但 relation 含糊 | owner 只扩到 invariant evidence，execution/orchestration/adjacent owner 不被无证据吞并 |
| Unknown handling | 猜测、制造 unknown 或 ready 带 active blocker | 有 probe 但影响不清 | 只处理会改变 intent/boundary 的 unknown；未关闭则 unresolved |
| Challenge quality | 只做自我确认 | 检查有限 | 主动检查 false unification、relocation、reassembly、owner overreach、exit 与 Human decision |
| Acceptance quality | 没有判定 outcome 是否成立，或冻结验证套餐 | 有验收描述但混入 provider | 一个 stable outcome-level acceptance rule；provider 与动态 target 留给下游 |
| Output discipline | 输出 taxonomy/Brooks/trace 或重型协议 | 大致精简但有多余 machinery | 仅 Problem / Background / Direction / Boundary，Possible shapes 按需，Material Unknown 不泄漏到 ready |
| Target-design boundary | 直接规定 module/class/API/migration | 偶有责任放置或调用流泄漏 | freeze why/outcome/boundary，how 保持开放并在 basic shape 前后正确停止 |
| Status / invocation | 状态或适用范围错误 | 正确但冗长 | 三状态互斥，local/已明确设计/直接实现请求正确退出 |

## V0 pass gate

1. P1–P4 的 paired eval 中，B 臂在 `Architecture judgment + Durable outcome + Invariant quality + Output discipline` 合计至少高于 A 臂 2 分，且这些维度没有新增 0 分退化；
2. N1 / R1 / L1 / O1 的路由和停止条件全部正确；
3. ready 输出只有四个 section；stable acceptance 只在 Direction 表达 outcome，Possible shapes 不展开，且不输出 taxonomy、Brooks、Challenge trace 或 active Material Unknown；
4. upper-goal discriminator 正确应用：有明确相关 goal 时保留其贡献，没有时从 pressure 得出 durable outcome；不得因此新增目标发现协议；
5. `materialization-regression.md` 的 M1–M4 全部通过，尤其不能冻结 observed partition、verification provider 或扩大 ownership；
6. README、SKILL、agent default prompt 与当前薄 contract / Target Design 边界一致，eval 变化不扩大正常 runtime context。

## Regression failures

以下 failure class 应保持可判定：

- `pressure-free-intent` — 从审美发明方向；
- `local-escalation` — 局部问题被升级成 architecture intent；
- `reality-collapse` — 用 clean interface/provider/dependency 等单一信号替代 semantics、ownership 或 runtime reality；
- `consumer-reassembly-miss` — caller 仍重组 capability facts，但被误判为 boundary 已闭合；
- `consumer-reassembly-false-positive` — 把纯 composition-root wiring 误判为 capability reassembly；
- `ownership-scope-creep` — 从 capability ownership 无 evidence 扩张到 execution/orchestration/adjacent subsystem；
- `ownership-centralization` — 为关闭 caller reassembly 吞并相邻 subsystem 的合法 ownership；
- `north-star-loss` — 已有明确相关上位 goal 时，局部 target 合理却替代了 area 应推进的 durable outcome；
- `false-unification` — 错误合并不同 bounded context；
- `historical-difference-lock-in` — 把当前 provider/class/execution partition 永久化；
- `speculative-intent` — 只能新增 abstraction，不能说明旧知识、路径或依赖退出；
- `materialization-creep` — reasoning distinction 被自动物化成长期 type/provider/adapter/layer；
- `unknown-swallowed` — 关键未知被猜测填补；
- `unknown-manufacture` — 没有会改变 intent/boundary 的 unknown 仍人为制造 blocker；
- `acceptance-provider-freeze` — 把 build/test/replay 或当前 target 列表冻结进 stable acceptance；
- `premature-design` — intent 阶段决定具体 module/class/API/responsibility/call flow/migration；
- `output-protocol-regression` — ready 输出重新出现 Brooks/taxonomy/Challenge/重型 proof machinery；
- `legacy-runtime-collapse` — 把 compat/serialized identity 与 runtime behavior 混为一谈；
- `search-absence-deletion` — 因 local search 无 reader 就宣告 identity/config 可删除；
- `status-leakage` — 非 ready 状态输出稳定 Architecture Intent，或 ready 保留 active Material Unknown。

Static/scenario smoke 只证明文本机制一致；paired eval 才用于衡量压缩后的 judgment 是否真实优于不加载 Skill 的基线。
