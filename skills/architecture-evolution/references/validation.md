# Evaluate Architecture Evolution

只用于显式 smoke/eval，正常 runtime 不读。本文件冻结 behavior property 与 captured regression，不是 runtime 规范源。

## Static smoke

通过需要同时满足：

1. **Natural flow**：主 Skill 能完成调研 → architecture judgment → Architecture Program → delivery，不依赖 ready/completed/status lifecycle，也不要求固定英文 phase 名。
2. **Self-contained success path**：主 Skill 自己拥有稳定 architecture judgment 与 Program contract；正常成功路径不需要第二份 compile/output contract。
3. **Progressive disclosure**：`rules.md` 只处理难判 discriminator，Brooks/legacy 只在相关 case 按需读取；它们不重复主模型、不形成第二套 Flow/taxonomy。
4. **Bounded research**：默认从指定 module/capability → direct upstream/downstream → real responsibility → boundary → stable variation 渐进展开；只有会改变 architecture judgment 的 authority/SOT/identity/external constraint 才扩大搜索。
5. **Taxonomy is Evidence**：当前 module/provider/class/family/consumer partition 与 proposed shape 都不是 architecture law；没有 stable variation 不制造 provider。
6. **Architecture taste**：Layering/dependency、Cohesion/simplicity、Abstraction/specific、Primary/auxiliary、Real evolution 都能直接改变 Target Architecture。
7. **Honest outcome**：local pressure 交付 local judgment；真实 fork 缺 decisive Evidence/Human decision 时交付缺口；两者都不制造 Architecture Program。
8. **Convergent Program**：Target Architecture 足够稳定后才写 Program；Top Improvements 最多 3 个且不补数，每个完成时独立产生 structural gain + real exit；research/setup/future/implementation step 不能冒充 Improvement。
9. **SOT discipline**：Program 引用 authoritative repo SOT，只保新增 judgment / structural delta；原 SOT 需演进时指向原 authority 的 delta，不建立平行规范。handoff artifact 不是 repo architecture SOT。
10. **Architecture altitude**：AE 固定长期 architecture outcome 与 structural done condition，不提前固定 implementation representation，除非 representation 本身被 authority 绑定。
11. **Human decision ownership**：独立调用可暴露真正 Human-owned choice；由 Northstar 等上游 task-shaping capability 调用时只返回 Evidence/options/decision surface，不抢占其 Human Ask ownership。
12. **Material handoff is re-entrant**：成功 Program 以同一正文 materialize 到 repo/workspace 外的 current handoff artifact；material Human update 重新打开受影响判断并完整重交付。artifact 写入失败时不得假装 handoff 成功。
13. **Thin entry / eval isolation**：`agents/openai.yaml` 只是 invocation pointer；`validation.md` 不进入正常 runtime。

## Scenario smoke

### P1 — Bounded module research
用户指定历史模块，存在 direct caller/downstream 与当前 provider/family taxonomy。

PASS：先恢复真实 responsibility 与 direct neighborhood，再识别 capability/boundary；只有 stable variation 有 decisive Evidence 时才形成 provider；只有局部无法关闭且会改变 Target Architecture 的 authority/SOT/identity/external constraint 才扩大搜索。

### P2 — ModelCurator / Hermes
publication ownership 已基本闭合，但 consumer 仍解释 feature config/Hermes usage；streaming 与 scoring 存在真实 semantic/input/lifecycle 差异。

PASS：不停在“ownership 应闭合”；抽象 stable common，保留真实 specific；不按当前 consumer/provider partition 生造 taxonomy；evolution 让旧 consumer knowledge/path 退出。

### P3 — PredictExecutor scoring
executor 按 family identity 分派 scoring，feature preparation、metrics/writeback、shadow/sampling 与 family-specific execution 混在路径中。

PASS：重新识别 scoring/orchestration primary responsibility；family switch 只作 Evidence；真实 stable specific 才形成 provider；auxiliary concern 不塑造主架构；executor-side family knowledge 真退出而不是搬进 registry/DSL。

### P4 — AI-friendly dependency
common/core 直接依赖 scenario/provider implementation，依赖方向只能靠文档提醒。

PASS：Target Architecture 建立可从 repo territory 读出的稳定单向 dependency boundary，值得时由 module/package/build/tooling 机械约束。

### P5 — Abstraction vs specific
一组代码相似但 semantics/lifecycle/output contract 长期不同；另一组实现不同但 invariant 相同。

PASS：前者允许 specific，后者寻找 stable abstraction；代码相似度/current taxonomy 不能替 semantic judgment。

### P6 — Speculative performance
proposal 为可能的微小性能收益让 provider-specific fast path/cache 打穿 common boundary，但无 profiling/SLA/resource Evidence。

PASS：默认保持 layering/cohesion/primary responsibility；只有真实 performance constraint 改变长期选择时才升级为 architecture force。

### P7 — Real evolution
proposal 新增 facade/manager/registry，但旧 SOT、caller branch 与 compat path 继续 authoritative。

PASS：不能交付 Program；必须形成会让旧 knowledge/authority/dependency/path 真退出的 Target Architecture/Improvement。temporary dual path 必须有 architecture purpose 与 exit。

### P8 — Brooks second-system
当前 pressure 可用简单结构解决，但 redesign 又加入 plugin framework、generic registry、future hooks/modes。

PASS：按需 Brooks challenge 后缩小方案；没有当前长期 Evidence 的 flexibility 不物化。

### C1 — Compile keeps only real improvements
5 个候选中 2 个只是 research/performance data collection，3 个能直接改变长期结构并让旧复杂度退出。

PASS：Program 只保留 3 个真实 Improvement；Route 只表达真实 architecture dependency。

### C2 — Top 3 is ceiling
只有 2 个 bounded Improvements 能确定改善结构，第三个只是未来 generalization。

PASS：只输出 2 个，不补数。

### C3 — Improvement must converge
“先建 abstraction，后面再迁旧 path”完成后没有旧 complexity 退出。

PASS：不能进入 Top Improvements；必须收敛成完成时自身就产生 structural gain/exit 的 bounded Improvement，否则暂不交付 Program。

### C4 — Structural leverage
多个 Improvements 都可推进：一个局部整理，一个消除多个 caller 的 knowledge reassembly，一个解除后续两项共同 reverse dependency。

PASS：优先后两者；排序不按实现最容易或描述最宏大。

### C5 — Authoritative SOT
repo 已有 authoritative schema/contract 定义稳定事实，本轮只新增其上的 architecture judgment；另一个旧 SOT 本身需要演进。

PASS：前者引用原 SOT；后者指出原 authoritative source 的 delta；Program 不复制第二份规范。

### N1 — Local stays local
问题只是 bug、dead getter、机械迁移或局部重复，不改变长期 architecture judgment。

PASS：直接说明保持 local 与理由，不制造 Target Architecture/Program，也不输出状态 token。

### R1 — Real fork unresolved
两个 materially different Target Architecture 均可行，当前缺一个 decisive semantic/lifecycle/performance constraint。

PASS：指出真正缺失的 Evidence/Human decision；不按模式偏好强选，不把“研究它”塞进 Improvements，也不输出状态 token。

### H1 — Routed Human decision ownership
Northstar 把长期 boundary/provider fork 路由给 AE，其中一个 business/compat choice 最终需要 Human 拍板。

PASS：AE 返回当前 Evidence、material options、主要 trade-off 与 decision surface 给 Northstar；不自己连续 Ask Human，也不把 choice 偷写成 architecture law。

### L1 — Legacy identity
旧 token 不再影响 runtime branch，但可能承担 parse/serialization/deployment identity，本地无直接 reader。

PASS：只有 retirement 会改变 Target Architecture/evolution 时才按 legacy lens 升级最小 probe；不能由 local search absence 宣告可删。

### O1 — Stop before implementation
Evidence 足以确定长期 layer/dependency、module responsibility、abstraction/specific、primary responsibility，并能形成真实 Improvements。

PASS：明确 Target Architecture、Improvement outcome、architecture dependency、structural done condition；不规定具体 class/API/file/flag schema/MR split/verification provider。

### D1 — Human update re-delivers full Program
AE 已交付完整 Architecture Program；Human 随后补充一个会改变 provider boundary 或 Target Architecture 的 material constraint。

PASS：重新打开最高受影响判断，复用不受影响部分，重算 Program，并再次输出完整 current Program；只回复 delta、解释旧 Program 或因之前已交付而停止都失败。

### D2 — Artifact failure is not success
AE 已收敛 Program，但 runtime 提供的 external artifact 无法写入。

PASS：报告 materialization blocker 与恢复条件；不把 conversation output 或“稍后写入”当成成功 handoff。

## Captured regression properties

1. module/provider/class/consumer partition 都只是 Evidence，不自动成为 architecture taxonomy；
2. Human proposed shape 默认是 candidate means，不自动成为 architecture invariant；
3. responsibility/variation ownership 不冻结 representation；
4. auxiliary concern 不因实现方便升级为 primary architecture owner；
5. caller/executor 不应重组 capability 私有 knowledge；
6. Real evolution 必须让旧 authority/knowledge/dependency/path 真退出；
7. Research 默认 bounded，Program 只保留 real Improvements；
8. authoritative repo truth 优先引用，不复制平行 SOT；
9. specialist 不抢占上游 Human decision ownership；
10. delivery 是本轮产出事件，不是 outcome lifecycle state；material Human update 必须重新完整交付；
11. handoff artifact 只承担当前 Program transport authority，不替代 repo architecture SOT。

## Paired behavioral eval

同一 model/repo snapshot/tool permission/budget：

```text
A. 不加载 architecture-evolution
B. 加载 architecture-evolution
```

每项 0–2：Research scope、Layering/dependency、Cohesion/simplicity、Abstraction/specific、Primary responsibility、Real evolution、Program convergence、Architecture altitude、Human-decision routing、Human-update re-delivery、handoff integrity、context cost。

### Pass gate

- P1–P8 / C1–C5 / N1 / R1 / H1 / L1 / O1 / D1–D2 property 全部正确；
- B 不能靠更长 analysis 冒充能力提升；必须表现出 bounded research、真实 Target Architecture 与 convergent Program；
- main Skill 不读取任何 reference 时能完成常规 architecture judgment + Program；只有难判/legacy/Brooks case 才下沉 reference；
- material Human update 后必须完整重交付 current Program，artifact failure 不得伪装成功；
- 没有 clean-session 结果时，不宣称 behavioral uplift。

## Claim boundary

Static/scenario smoke 只证明 contract 与 frozen properties 一致；没有 clean-session runner 结果时，behavioral uplift 标记 `NOT RUN`。
