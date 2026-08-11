# Evaluate Architecture Evolution

只用于显式 smoke/eval，正常 runtime 不读。本文件冻结 behavior property 与 captured regression，不是 runtime 规范源。

## Static smoke

通过需要同时满足：

1. **Stable Flow**：主 Skill 明确 `Ground → Judge → Compile → Deliver`，只描述单次 invocation，不形成 phase/status lifecycle。
2. **Self-contained architecture contract**：主 Skill 自己就包含五个稳定结构判据；`rules.md` 只展开判别边界/反例，不是第二套 architecture model。
3. **Bounded Ground**：默认锚定用户指定模块，按 `module → direct upstream/downstream → real capability → boundary → stable variation/provider` 渐进展开；不把全 repo scan 当 Research 成功。
4. **Taxonomy is evidence**：现有 module/provider/class/family/consumer partition 只是 evidence；必须允许从真实 responsibility 重新识别 capability/boundary；没有 stable specific variation 时不得制造 provider。
5. **Architecture taste**：Layering & dependency、Cohesion & simplicity、Abstraction vs specific、Primary vs auxiliary responsibility、Real evolution 五项都能直接改变 Target Architecture；其他 lens 只作 evidence/challenge。
6. **Progressive challenge**：Brooks 与 legacy 只在 Judge 中按需读取，不形成第二套固定 Flow/taxonomy。
7. **Honest branch**：local pressure 直接交付 local judgment；真实 architecture fork 缺 decisive Evidence/Human decision 时直接交付缺口；两者都不制造 Architecture Program。
8. **Convergent Compile**：Target Architecture 足够稳定后才形成 Architecture Program；最多 3 个 independently improving improvements，不补数。每个完成时必须产生 structural gain 与 real exit；research task、future wish、implementation step、setup-only abstraction 不能冒充 improvement。
9. **SOT discipline**：Compile 优先引用 authoritative repo SOT，只保新增 architecture judgement / structural delta；旧 SOT 本身需演进时指向原 authority 的 delta，不建立平行规范。
10. **Architecture altitude**：AE 可固定长期 layer/dependency、capability/module responsibility、abstraction/specific、必要 authority/lifecycle/variation 与 structural done condition；不固定 class/API/file/schema/call implementation/MR/task/test provider，除非 representation 本身是 authoritative invariant。
11. **Delivery is not outcome state**：成功时直接完整输出当前 Architecture Program，不输出 ready/completed status；material Human update 从最高受影响 Flow step 重进并再次完整交付，prior delivery 不抑制输出。
12. **Thin entry / eval isolation**：`agents/openai.yaml` 只是 invocation pointer；`validation.md` 不进入正常 runtime。

## Scenario smoke

### P1 — Bounded module research
用户指定历史模块，存在 direct caller/downstream 与当前 provider/family taxonomy。

PASS：先恢复真实 responsibility 与 direct neighborhood，再识别 capability/boundary；只有 stable variation 有 decisive Evidence 时才形成 provider；只有局部无法关闭且会改变 Target Architecture 的 authority/SOT/identity/external constraint 才扩大搜索。

### P2 — ModelCurator / Hermes
publication ownership 已基本闭合，但 consumer 仍解释 feature config/Hermes usage；streaming 与 scoring 存在真实 semantic/input/lifecycle 差异。

PASS：不停在“ownership 应闭合”；抽象 stable common，保留真实 specific；不按当前 consumer/provider partition 生造 taxonomy；evolution 让旧 consumer knowledge/path 退出。

### P3 — PredictExecutor scoring
executor 按 family identity 分派 scoring，feature preparation、metrics/writeback、shadow/sampling 与 family-specific execution 混在路径中。

PASS：重新识别 scoring/orchestration primary responsibility；family switch 只作 evidence；真实 stable specific 才形成 provider；auxiliary concern 不塑造主架构；executor-side family knowledge 真退出而不是搬进 registry/DSL。

### P4 — AI-friendly dependency
common/core 直接依赖 scenario/provider implementation，依赖方向只能靠文档提醒。

PASS：Target Architecture 建立可从 repo territory 读出的稳定单向 dependency boundary，值得时由 module/package/build/tooling 机械约束。

### P5 — Abstraction vs specific
一组代码相似但 semantics/lifecycle/output contract 长期不同；另一组实现不同但 invariant 相同。

PASS：前者允许 specific，后者寻找 stable abstraction；代码相似度/current taxonomy 不能替 semantic judgement。

### P6 — Speculative performance
proposal 为可能的微小性能收益让 provider-specific fast path/cache 打穿 common boundary，但无 profiling/SLA/resource evidence。

PASS：默认保持 layering/cohesion/primary responsibility；只有真实 performance constraint 改变长期选择时才升级为 architecture force。

### P7 — Real evolution
proposal 新增 facade/manager/registry，但旧 SOT、caller branch 与 compat path 继续 authoritative。

PASS：不能交付 Program；必须先形成会让旧 knowledge/authority/dependency/path 真退出的 Target Architecture/Improvement。temporary dual path 必须有 architecture purpose 与 exit。

### P8 — Brooks second-system
当前 pressure 可用简单结构解决，但 redesign 又加入 plugin framework、generic registry、future hooks/modes。

PASS：按需 Brooks challenge 后缩小方案；没有当前长期 Evidence 的 flexibility 不物化。

### C1 — Compile keeps only real improvements
5 个候选中 2 个只是 research/performance data collection，3 个能直接改变长期结构并让旧复杂度退出。

PASS：Program 只保留 3 个真实 improvement；Route 只表达真实 architecture dependency。

### C2 — Top 3 is ceiling
只有 2 个 bounded improvements 能确定改善结构，第三个只是未来 generalization。

PASS：只输出 2 个，不补数。

### C3 — Improvement must converge
“先建 abstraction，后面再迁旧 path”完成后没有旧 complexity 退出。

PASS：不能进入 Top Improvements；必须收敛成完成时自身就产生 structural gain/exit 的 bounded improvement，否则暂不交付 Program。

### C4 — Structural leverage
多个 improvements 都可推进：一个局部整理，一个消除多个 caller 的 knowledge reassembly，一个解除后续两项共同 reverse dependency。

PASS：优先后两者；排序不按实现最容易或描述最宏大。

### C5 — Authoritative SOT
repo 已有 authoritative schema/contract 定义稳定事实，本轮只新增其上的 architecture judgement；另一个旧 SOT 本身需要演进。

PASS：前者引用原 SOT；后者指出原 authoritative source 的 delta；Program 不复制第二份规范。

### N1 — Local stays local
问题只是 bug、dead getter、机械迁移或局部重复，不改变长期 architecture judgement。

PASS：直接说明保持 local 与理由，不制造 Target Architecture/Program，也不输出状态 token。

### R1 — Real fork unresolved
两个 materially different Target Architecture 均可行，当前缺一个 decisive semantic/lifecycle/performance constraint。

PASS：指出真正缺失的 Evidence/Human decision；不按模式偏好强选，不把“研究它”塞进 improvements，也不输出状态 token。

### L1 — Legacy identity
旧 token 不再影响 runtime branch，但可能承担 parse/serialization/deployment identity，本地无直接 reader。

PASS：只有 retirement 会改变 Target Architecture/evolution 时才按 legacy lens 升级最小 probe；不能由 local search absence 宣告可删。

### O1 — Stop before implementation
Evidence 足以确定长期 layer/dependency、module responsibility、abstraction/specific、primary responsibility，并能形成真实 improvements。

PASS：明确 Target Architecture、improvement outcome、architecture dependency、structural done condition；不规定具体 class/API/file/flag schema/MR split/verification provider。

### D1 — Human update re-delivers full outcome
AE 已交付完整 Architecture Program；Human 随后补充一个会改变 provider boundary 或 Target Architecture 的 material constraint。

PASS：从最高受影响的 Ground/Judge/Compile step 重进，复用不受影响 judgement，重新 Compile，并再次输出**完整当前 Architecture Program**。只回复“变更点”、解释旧 Program、或因为之前已经交付而不再输出 Program 都失败。

## Captured regression properties

1. module/provider/class/consumer partition 都只是 evidence，不自动成为 architecture taxonomy；
2. responsibility/variation ownership 不冻结 representation；
3. auxiliary concern 不因实现方便升级为 primary architecture owner；
4. caller/executor 不应重组 capability 私有 knowledge；
5. Real evolution 必须让旧 authority/knowledge/dependency/path 真退出；
6. Research 默认 bounded，Compile 只保留 real improvements；
7. authoritative repo truth 优先引用，不复制平行 SOT；
8. delivery 是本轮产出事件，不是 outcome lifecycle state；material Human update 必须重新完整交付。

## Paired behavioral eval

同一 model/repo snapshot/tool permission/budget：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 0–2：Research scope、Layering/dependency、Cohesion/simplicity、Abstraction/specific、Primary responsibility、Real evolution、Compile convergence、Architecture altitude、Human-update re-delivery、context cost。

### Pass gate

- P1–P8 / C1–C5 / N1 / R1 / L1 / O1 / D1 property 全部正确；
- B 不能靠更长 analysis 冒充能力提升；必须表现出 bounded research、真实 Target Architecture 与 convergent Compile；
- main Skill 在不读取 `rules.md` 时仍能给出正确高层 architecture taste；需要细节/反例时才下沉 reference；
- material Human update 后必须重新完整交付 current outcome；
- 没有 clean-session 结果时，不宣称 behavioral uplift。

## Claim boundary

Static/scenario smoke 只证明 contract 与 frozen properties 一致；没有 clean-session runner 结果时，behavioral uplift 标记 `NOT RUN`。
