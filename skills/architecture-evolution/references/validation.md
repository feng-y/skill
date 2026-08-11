# Evaluate Architecture Evolution

只用于显式 smoke/eval，正常 runtime 不读。本文件冻结 behavior property 与 captured regression，不是 runtime 规范源。

## Static smoke

通过需要同时满足：

- North Star 是从 forces / repo reality 收敛 Architecture Decision + architecture-level evolution，不再只产出 Architecture Intent；
- `SKILL.md` 只拥有 stance、适用边界和三种终态，不要求固定 reasoning stage；
- `rules.md` 是 architecture judgement 的唯一 owner：architecture forces、minimal current model、design space、trade-off、complexity relocation、Target Architecture altitude、evolution；
- `intent-contract.md` 只拥有 ready decision 的语义义务，不要求固定 Markdown section；
- Target Architecture 可以固定长期 responsibility / authority / knowledge / control / lifecycle / dependency / essential variation boundary，但不把 class/API/file/helper/schema/调用实现/task/verification provider 当 architecture law；
- alternatives 只有 materially different architecture fork 才出现，不要求固定数量，也不把同一 representation 的不同命名/类层次算不同 architecture；
- 若多个 materially different architecture 都可行而 forces 不足以裁决，必须 `Architecture unresolved`，不能把第一个 plausible shape 当 ready；
- architecture decision 必须比较 complexity relocation：旧 complexity 真正退出什么，新 complexity 去哪里，是否形成 mini-framework / flag matrix / permanent adapter；
- ready decision 必须包含 architecture-level evolution：authority/boundary establishment、knowledge/control exit、temporary complexity exit、关键 ordering / reversibility；不能退化成 implementation task list；
- 三个状态互斥：`No architecture evolution / Architecture unresolved / Architecture decision ready`；
- legacy 与 Brooks 都只是按需 lens，不成为默认阶段或最终输出 taxonomy；
- README / agent prompt 与 v2 的 Target Architecture / Implementation Design 边界一致；
- captured case wording 不进入 runtime。

## Scenario smoke

### P1 — ModelCurator / Hermes: from diagnosis to architecture decision

已知：publication ownership 已基本闭合，但 prediction、prerank、item-embedding、feature-streaming 仍在 consumer 侧解释 feature config、Hermes lifecycle 或 usage protocol；streaming 与 scoring 存在真实 semantic/input/lifecycle 差异，repo 中已有 generation/model/provider 等多种可能承载边界。

PASS：

- current model 解释真正的 knowledge/control/variation relationship，而不是只列文件与 helper；
- 不止得到“capability ownership 应闭合”这一层 intent：若存在 materially different architecture fork，应比较至少 responsibility/knowledge/control/lifecycle 中一个长期 axis 的差异；
- 对仍可行 alternative 说明最重要的 force-based trade-off 与 complexity relocation；若 evidence 不足以选择则 `Architecture unresolved`；
- Target Architecture 保留真实 streaming/scoring essential variation，不按当前 consumer/provider partition 永久化 taxonomy；
- evolution 说明新 capability/authority 先成立后，哪些 consumer knowledge / old path 才能退出；不展开 class/API/migration task。

### P2 — PredictExecutor scoring: design-space reasoning

已知：executor 按 family identity 分派 scoring 路径，抽取前奏和后置步骤组合散落在 caller；同时 repo 可能支持 declarative contract、capability-owned behavior、load-time compiled runtime shape 等 materially different architecture。

PASS：

- switch/member/helper 只是 caller 持有 family-specific execution knowledge 的 evidence；不把这些 symbol 逐项删除冻结成 architecture acceptance；
- 至少识别真实 design-space fork；不要求固定三种方案，也不把 `Manager`/`Provider` 重命名当 alternative；
- 比较方案时回答 change locality、knowledge/control ownership、SOT、essential variation、runtime/lifecycle constraint 和 complexity relocation；
- 只有 forces 足以支持时选择 primary architecture，否则保持 unresolved；
- “variation 归正确 owner”不能自动翻译成 flag/metadata/虚函数/某一种 representation；
- evolution 说明 executor-side knowledge 如何在新 boundary 建立后退出，而不是输出 patch plan。

### P3 — False alternatives are not design space

同一个 owner/boundary 下只有不同类名、文件布局、factory/manager/provider 命名或同构 API 方案。

PASS：不把这些包装成 architecture alternatives；继续寻找真正改变 responsibility / authority / knowledge / control / lifecycle / dependency / variation axis 的 fork，找不到则按已有 forces 直接 decision，不制造比较 ceremony。

### P4 — Evolution is architecture, not task planning

Target Architecture 已清楚，但 current system 仍有旧 SOT、旧 caller knowledge 和一个为兼容存在的 dual path。

PASS：说明新 authority 先建立、旧 authority 何时失去 authoritative status、caller knowledge 在什么 architecture condition 下退出、dual path 的 purpose/exit 与关键 lock-in；不列文件修改顺序、MR 切分、测试命令或发布步骤。

### P5 — Complexity relocation challenge

一个 proposal 删除 central switch，却新增一组组合型 flags / registry / adapter，使相同决策知识仍由 caller 或另一个 generic layer 解释。

PASS：不能因 switch 消失就判 architecture improved；明确指出 complexity relocation，并比较是否有 materially different architecture 能真正减少 decision knowledge / change propagation。

### N1 — Local fix stays local

问题只是 off-by-one、日志字段、dead getter、一次机械迁移或局部重复，没有持续 change pressure、跨边界 knowledge/control/authority consequence。

PASS：`Status: No architecture evolution`；不发明 Target Architecture 或 alternatives。

### R1 — Real architecture fork remains unresolved

两个 materially different Target Architecture 都满足 outcome：一个集中 execution control，另一个把 behavior/lifecycle 下沉 capability；当前 evidence 尚不能确认未来 variation frequency、lifecycle constraint 或 authoritative SOT。

PASS：`Status: Architecture unresolved`；指出真正会改变选择的 force/evidence/Human decision。不能按当前代码形状、个人模式偏好或“更优雅”强选一个。

### L1 — Legacy identity is not runtime behavior

一个历史 token 已不再影响 runtime branch，但仍可能承担 parse/serialization/deployment identity；本地搜索没有直接 reader。

PASS：按需读取 `legacy-lenses.md`；只有 Target Architecture / authority retirement 依赖它时才升级为 Material Unknown。不能因 runtime retirement 或 local search absence 宣布 identity 可删除。

### O1 — Target Architecture altitude

Evidence 已足以判断长期 capability owner、authority/SOT、knowledge/control direction、lifecycle boundary 和 essential variation；Implementation Design 尚未开始。

PASS：允许 AE 明确这些 architecture placement，并形成 decision/evolution；但若开始规定具体 class/API/file、helper、flag schema、虚函数签名、patch 顺序或 verification provider，则失败。

## Captured regression properties

以下是 case 暴露出的 property，不是 runtime prior：

1. consumer usage partition 是 evidence，不自动生成 consumer-specific public view/interface；
2. current provider/class/execution partition 不自动成为 stable variation taxonomy；
3. build/test/replay/diff 不冻结为 architecture acceptance provider；
4. existing upper architecture goal 只作为 force/authority，不建立新的 goal-discovery protocol；
5. current member/switch/helper/flag residue 不自动成为 stable acceptance；判断它承载的 knowledge/responsibility/dependency 是否真正退出；
6. variation ownership 不冻结 representation；
7. scoring-side captured case 中，“executor 不再拥有 family-specific execution knowledge”可以是 architecture outcome，但“必须显式声明差异”或“指定 symbol 必须消失”不是无条件 architecture law。

## Paired behavioral eval

同一模型、repo snapshot、tool permission 和预算：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 `0–2`：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Pressure / forces | 从审美或模式偏好出发 | 有 evidence 但 forces 模糊 | 真实 change pressure 与决定 architecture 的 forces 清楚 |
| Current architecture model | 文件/类 inventory | 部分 boundary 判断 | responsibility/authority/knowledge/control/lifecycle/variation/change edges 足以解释问题 |
| Architecture judgment | local/architecture 混淆 | direction 合理但根因不稳 | 正确裁决 structural cause 与 architecture scope |
| Design-space quality | 第一个方案即结论，或假 alternatives | 有多个 shape 但差异浅 | 只展开 materially different architecture axes，不制造数量 ceremony |
| Trade-off quality | 只列优点 | 有局部利弊 | 能解释 change locality、SOT、knowledge/control、essential variation 与最坏 architecture cost |
| Complexity relocation | 只看旧结构消失 | 知道有新复杂度 | 明确旧 complexity 退出与新 complexity owner，识别 flag/registry/framework relocation |
| Decision quality | pattern preference | 有理由但无法排除 alternative | force-based 选择 primary architecture；不足时诚实 unresolved |
| Evolution quality | 没有 evolution 或 task list | 有迁移方向但 authority 模糊 | authority/knowledge/control exit、temporary complexity、ordering、reversibility 清楚且不落 task |
| Architecture altitude | 只给 abstract intent，或直接进代码设计 | 能描述部分 target boundary | 完成 Target Architecture，同时保持 Implementation Design 自由 |
| Essential variation | 锁死当前 partition 或错误统一 | 部分正确 | 只保留有 semantic/lifecycle/performance/deployment evidence 的长期 variation |
| Evidence / Unknown | 猜测或无限研究 | 有 probe 但影响不清 | 只关闭会改变 decision/evolution 的 Material Unknown |
| Output discipline | checklist/trace/重型模板 | 大致可读但 ceremony 多 | decision-relevant result；无 taxonomy/Brooks/固定 section ceremony |

## V2 pass gate

1. P1 / P2 的 B 臂在 `Current architecture model + Design-space quality + Trade-off quality + Decision quality + Evolution quality` 合计至少高于 A 臂 3 分，且这些维度没有新增 0 分退化；
2. P3–P5 / N1 / R1 / L1 / O1 的 discriminator 与停止边界全部正确；
3. B 臂不能只把旧 `Architecture Intent` 写得更长：必须出现真实 architecture alternatives/trade-off/decision/evolution 能力，或有 evidence 地判断无需 alternatives；
4. ready result 可以完成 Target Architecture，但不能泄漏 Implementation Design；
5. captured regression properties 1–7 全部可判定，且具体 case 名词不出现在 runtime；
6. README / SKILL / agent prompt / output contract 与 v2 capability 一致；
7. 只有 clean-session paired Evidence 才能宣称 behavioral uplift；static/scenario review 只证明 contract/eval consistency。

## Regression failures

- `pressure-free-architecture` — 从审美发明 architecture work；
- `local-escalation` — local problem 被升级成 architecture evolution；
- `inventory-as-model` — 文件/类清单冒充 current architecture model；
- `first-shape-wins` — 第一个 plausible shape 直接成为 decision；
- `fake-alternatives` — 同一 architecture representation 的不同命名冒充 design space；
- `force-free-choice` — 没有 force-based 理由就选择 alternative；
- `complexity-relocation` — 旧 switch/layer 消失但 decision knowledge/branch/adapter 只是搬家；
- `knowledge-leakage` — caller 仍需重建 capability-private knowledge；
- `authority-duplication` — 新旧 SOT / policy source 长期并存；
- `ownership-centralization` — 无 evidence 吞并相邻 subsystem 的合法 owner；
- `historical-variation-lock-in` — current partition 被永久化；
- `representation-freeze` — owner/boundary judgement 被物化成固定 class/API/flag/schema/虚函数形态；
- `acceptance-residue-freeze` — 当前 symbol/residue 的逐项消失冒充 architecture acceptance；
- `evolution-as-task-plan` — architecture evolution 退化成文件/MR/test/发布步骤；
- `permanent-transition` — adapter/dual path/compat 没有 architecture exit condition；
- `premature-implementation-design` — Target Architecture 阶段规定具体实现；
- `abstract-intent-stop` — 只说“ownership 应闭合/依赖应单向”就宣布 ready，没有 architecture decision；
- `unknown-swallowed` — Material Unknown 被偏好填补；
- `unknown-manufacture` — 不改变 decision 的 unknown 被升级成 blocker；
- `output-protocol-regression` — taxonomy/评分/Brooks/checklist 被要求进入最终结果。

Static/scenario smoke 只证明文本 contract 与 frozen properties 一致；没有 clean-session paired run 时，behavioral uplift 必须标记 `NOT RUN`。
