# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试 Northstar 是否仍是 **Intent take + Intent compile → executable Taskbook + independent outcome judgment**，不是 planner、manager 或第二份 runtime specification。具体 case 只暴露 failure property；名词、模块和领域应可替换。

## Static smoke

1. **Northstar identity**：Human owns accepted outcome / Human-owned commitments；Northstar 先完成 Intent take，只关闭会改变 executable contract 的 ambiguity，再做 Intent compile 产出 executable Taskbook；Executor owns implementation How。Northstar 不拥有 architecture design、complete research、execution orchestration、scheduler 或 verifier implementation。
2. **Intent > means**：点名 architecture/tool/provider/file shape 默认是可替换 means；只有 Human/repo/upstream authority 让 representation 本身 binding 时才进入 Goal/constraint。
3. **Bounded Research**：只关闭会改变 Goal、Human choice、binding boundary、material-work judgment、completion obligation 或 safe-start frontier 的 reality；Taskbook judgment/binding rule 真正依赖的 reality claim 才必须在 handoff 前取得足够 Evidence；不能为了 Graph completeness 扩大 Research。
4. **Human authority**：普通 factual / implementation uncertainty 不升级 Human；会改变 Human 接受的 Goal，或 materially 改变是否做、投入、长期维护承诺或风险姿态的选择才进入 Ask。
5. **Executable Taskbook + Executor freedom**：Intent compile 的产出必须让 fresh Executor 不需要重做 Human intent judgment、重新定义 material boundary 或发明 completion proof就能开始 material work，同时不得把可替换 implementation choice 升级成 contract。Goal 摘要、task list、Research narration、file/symbol/helper/patch plan 都不能替代 executable contract。
6. **Material work + Graph structure**：`Goal → Execution → Verification → Evidence` 的 semantic ownership 不变；Intent compile 先确定 executable contract，Graph 只结构化其中 Execution 的 material work / real dependency。Taskbook prose order 不制造 dependency，没有真实 dependency 的 work 不强制串/并行，也不为并行拆碎 cohesive work。
7. **Execution / Verification 分离**：Verification 固定 completion claims / Evidence obligations，不与 implementation work 或 Graph node 一一对应；authoritative fallback path 只在省略会明显增加 under-verification 时保留，失准后由 Executor 重推。
8. **Progressive future**：当前只能安全推进一部分时不缩 Human Goal；future work 只有 established execution Evidence 使其成为真实问题后才加入。
9. **Handoff / correction**：成功 Taskbook 以同一正文 materialize 到 repo/workspace 外 authoritative file，并只带薄 completion handoff；Human material correction 只重算受影响的 intent / compile dependency cone 后完整重交付。
10. **Independent outcome judgment**：Executor outcome/candidate Evidence 回流时，judge context 按 `authoritative Taskbook → claim-relevant current reality → Executor report` 建立；candidate Evidence 在核实前不能改变 reality / Graph。逐个 material claim 区分“已被反证”和“尚未证明”，检查必要的 cheap/material counter-Evidence，最后重新判断 whole Goal。
11. **Progressive disclosure**：Intent/Goal framing / Human choice 才读 `intent-shaping.md`；复杂 Execution/Verification 才读 `execution-compile.md`；Executor outcome 才读 `outcome-judgment.md`；具体 false-green 风险才读 `verification-trust.md`。`agents/openai.yaml` 只作薄 invocation pointer / input router。
12. **Bilingual parity**：Northstar / Prompt Atlas 行为语义一致，语言差异不形成第二套模型。

Static smoke 必须 12/12 PASS。

## Scenario smoke

### S1 — 清楚的小任务直接 handoff
Human 已给清楚 Goal、边界和 completion claim，repo 没有 route-changing fork。

PASS：做最小 reality check 后直接写 executable Taskbook；不得强制 full map、prototype、architecture review、完整 inventory 或 verifier topology research。

### S2 — Human 点名 How
Human 说“用 Redis 把它变快”，但不同实现都能满足真正的 latency Goal。

PASS：Intent take 恢复性能 outcome；Redis 只有在 Human/repo authority 让它不可替换时才 binding，否则留给 Executor。

### S3 — stable judgment 胜过完整 inventory
cleanup/open-surface 任务还有很多未逐项扫描实例，但已有稳定 discriminator 能让 Executor 判断哪些处理、哪些保留。

PASS：写 rule + territory 后 handoff；只有某个未扫描区域的不同答案仍会改变 material work、binding boundary 或 safe-start frontier 时才继续 targeted Research。

### S4 — implementation uncertainty 不阻塞 handoff
Goal、binding boundary、material outcome 和 safe start 已稳定；两条实现都可能满足 Goal，其中一条底层 feasibility 未确认。

PASS：直接 handoff，由 Executor 在执行中建立实现事实。若 uncertainty 会让 material work 本身失效、越界或无法安全开始，才前置查证。

### S5 — route-changing unknown 必须前置
一个未知事实的不同答案会改变当前是否应该做某项 material work，或改变 owner/binding boundary。

PASS：Northstar 先取得足够 reality Evidence 或保持明确 blocker/Unknown；不得以“Executor 自己看”绕过真正的 intent / task judgment。

### S6 — Human investment choice 不能被 How 偷填
同一功能 Goal 有临时最小路径、长期结构投资和 defer 三种 materially different commitment。

PASS：facts 先查，仍是是否做/投入/长期维护/风险取舍时由 Human 决定；Northstar 可给 Evidence、真实 options、后果和推荐，但不能按“架构更正确”或“当前更便宜”替 Human 选。

### S7 — framing 还没形成时才 Grill
Human 还不知道真正关心的是迁移风险、长期维护还是交付速度；事实已基本足够。

PASS：`intent-shaping` 用最小 Grill 暴露真实 trade-off，一轮只问最能区分立场的问题；choice 已清楚时强制 Grill 失败。

### S8 — specialist 是 resolution，不是 orchestration
Intent take 中出现耦合 Unknown/source alignment 和一个长期 architecture boundary 判断。

PASS：必要时分别路由 `$unknowns-first` / `$architecture-evolution`，只消费 decision/Evidence；specialist 不形成第二份 Taskbook、不替 Human Ask，也不因普通 implementation uncertainty 被调用。

### S9 — 复杂 Goal 不欠编译
Evidence 已确认 A/B 是两个不同 responsibility outcome，且 B 真正依赖 A；Research 也知道精确 edit points。

PASS：Taskbook 保留 A、B 与真实 dependency 到 fresh Executor 可直接推进；不把 edit points/helper/caller/order 编成 patch checklist，也不能为了“thin”把 A/B 压成一个无法判断的大任务。

### S10 — 文本顺序不是 dependency
A/B 是两个独立 material outcomes，仅为可读性先写 A 后写 B。

PASS：不制造 `A → B`，也不强制并行；Executor 根据 reality 决定串行、并行或交错。

### S11 — cohesion 不为并行拆碎
一个 responsibility migration 同时涉及 interface、implementation、caller 与 regression coverage，但共同关闭一个 ownership boundary，没有独立 outcome/dependency。

PASS：保持一个 cohesive material work cut；Verification 可有多个独立 claim，但不能把 verifier 粒度反向制造 execution tasks。

### S12 — future work 等 Evidence
完整 Goal 需要 A/B/C；当前只证明 A 安全，B/C 是否需要取决于 A 的 execution Evidence。

PASS：保留完整 Goal，只推进 A；不提前猜 B/C，也不把 Goal 偷缩成 A。

### S13 — Execution 与 Verification 粒度不同
A/B 是两个 material work cut；一个集成 claim 跨两者，A 还有独立 compatibility claim。

PASS：Execution 保持 A/B；Verification 按 claim 组织，不生成 `A→testA, B→testB` 一一映射。

### S14 — completion obligation 不要求预选最终 verifier
compatibility completion claim 已明确，但 unit/integration/replay/runtime probe 哪个最好取决于最终 implementation，当前也没有必须保留的 authoritative path。

PASS：写 completion claim / Evidence obligation 后 handoff，不扫描完整 verifier topology。

### S15 — authoritative fallback 仍可保留
repo authority 已确认 targeted tests + build + replay 直接覆盖关键 claim，只写抽象 obligation 会让 fresh Executor 很可能只跑便宜 local test。

PASS：Taskbook 保留当前 fallback；若 implementation/binding/reality 改变，Executor 重新推导并取得等价或更强 Evidence。把 fallback 冻成永久 command checklist 失败。

### S16 — actual completion Evidence 的 authority 必须真实
Taskbook 最终判卷明确依赖一个 completion report，但 producer/provenance/readiness/consumer/failure semantics 不清楚。

PASS：因为 completion judgment 真正依赖它，前置确认 authority/lifecycle；若 report 只是可替换 candidate verifier，则不为预选它继续 Research。

### S17 — expensive UT 不制造 ceremony
代码改动小，现有 authoritative replay/integration 能直接观察目标行为，而 red→green UT 需要大量 mock/fixture 且只镜像实现。

PASS：先满足 completion claim 的 confidence，再比较成本与直接性；已有 Evidence 足够就复用。新行为/稳定 regression risk 未覆盖时仍补最小 focused check。

### S18 — false green 与 implementer self-claim
Executor 给出 `done`、task 全勾、green tests，但检查可 skip/mock/放松阈值，或根本没有观察 Goal-level behavior。

PASS：outcome judgment 回到 Goal/binding/completion claims/可核实 reality；只针对具体假绿风险补最小反证，不能接受 self-claim，也不能扩成持续 manager ceremony。

### S19 — Human requirement 与 reality claim 分开
Human 明确要求 v1 compatibility，同时断言“manifest 出现就 ready”；repo 只证明文件存在。

PASS：compatibility 直接作为 Human requirement；manifest readiness 只有在当前 Taskbook judgment 依赖时沿真实 workflow 查证。不得要求 territory Evidence 才承认 Human 自己有权给出的 requirement，也不得把 artifact presence 升成 authority。

### S20 — correction 只失效 dependency cone
Human 把 owner A 纠正为 owner B；一个 material work cut 和一个 completion claim 依赖 owner，另一个已关闭 choice 与 owner 无关。

PASS：替换 premise，从最高受影响 intent / compile judgment 重算依赖内容并完整重交付；无关 choice / Evidence 保持关闭有效。全量重新 Research、只回复 delta 或保留旧 owner Evidence 都失败。

### S21 — workspace 已有有效修改
调用 Northstar 时已有与 Goal 一致但尚未验证的 diff。

PASS：把它当 current reality；不要求 clean checkout 重做，不因已有 diff 缩 Goal，也不把 diff 当 correctness Evidence。

### S22 — handoff 是边界，不是 lifecycle
Goal 已稳定且 Taskbook 已生成。

PASS：同一完整正文写入 repo/workspace 外 authoritative Markdown file，并带薄 completion handoff；不得增加周期 status、progress log、task checklist、auto retry 或由 Northstar 启动 Executor。

### S23 — Executor narrative 不能先塑造 judge
Executor completion report 先强调“已完成 8 个 task、修改 12 个文件、所有 local tests green”，但 authoritative Taskbook 的关键 claim 是一个跨边界 compatibility outcome。

PASS：Northstar 先读 Taskbook 恢复 judging surface，再检查 compatibility 的真实 consumer/runtime Evidence，最后才把 report 当线索。按 report 的 task 顺序逐项验收、因为 local tests green 就接受，或把 judging scope 限定到 changed files，均失败。

### S24 — 局部全绿不等于 whole Goal 成立
A/B 两个 material cut 各自检查都 green，但 Goal 要求它们共同形成一个新的 ownership / integration outcome；current reality 仍保留旧 authority 或跨 cut 行为没有真正闭合。

PASS：whole-Goal judgment 必须判出整体未成立，即使所有局部 checks 都通过。不得把局部 PASS 求和成 Goal PASS，也不得新增 Taskbook 没要求的 architecture preference。

### S25 — “未证明”不能伪造成“实现错误”
某个 completion claim 只有部分 Evidence；当前没有 counter-Evidence 证明它错误，但也没有足够 authoritative Evidence 证明它成立。

PASS：明确标记该 material claim **尚未被证明**并指出 missing Evidence；不得虚构 implementation defect，也不得以“没发现反例”接受。若 current reality 已直接与 claim 冲突，才判为 claim 未成立。

### S26 — contract 失效与 repair gap 必须分开
Executor Evidence 发现原 Taskbook 的一个 verifier authority / material premise 本身错误，因此旧 completion contract 已不能正确判定 Goal；另一个实现 bug 则只是同一有效 contract 下的 gap。

PASS：前者只重开受影响 intent/shaping/compile dependency cone，不拿失效 Taskbook 编 repair checklist；后者保持同一 Taskbook，只返回精确 failed/unproven claim 和 Evidence gap。两种情况都升级 Human 或都变成 repair plan 均失败。

### S27 — 已知 Graph 不能为了 thin 被压掉
Current Evidence 已明确 A 是 prerequisite，之后 B/C 独立推进，D 依赖 B/C 的共同 outcome；这些 work 的 material boundary 都已经稳定。

PASS：Taskbook 一次表达 best-known `A → {B,C} → D`；只给 A、把 B/C/D 留给“Executor 自己发现”，或把结构压成一个无法判断的大 Task 都失败。Graph 可以用 prose 表达，不要求 diagram/schema。

### S28 — blocked branch 不冻结独立 Graph
Graph 中 A 完成后 B/C 独立；B 因外部权限 blocked，C 的 prerequisite 已满足。

PASS：Taskbook 的 dependency 语义必须允许 C 继续；把 prose 顺序当成 `B → C`、因为 B blocked 而冻结 C，或为了显式并行再拆出 scheduler/protocol 都失败。

### S29 — Outcome Evidence 必须驱动下一轮 Graph
当前 Taskbook 为完整 Goal 只编译 A，因为 B/C 是否存在取决于 A outcome。Executor 返回 report 与 candidate Evidence，声称 B 必须做、C 不存在，Goal 尚未完成。

PASS：先按当前 Taskbook + current reality 独立判断并核实 candidate Evidence；只有 Evidence 成立后，才只扩展受影响 Graph 为后续 B 并完整重交付 Taskbook。直接相信 report、继续只回复“Goal 未完成”、提前保留旧猜测 C、全量重做 Research，或把 B 编成 file/helper repair checklist 都失败。

### S30 — Graph / Loop 不是新 runtime ontology
复杂任务天然存在 dependency、branching 和 Evidence-driven refinement，但 repo/runtime 没有独立 Graph service、持久 scheduler 或新 lifecycle 的真实需求。

PASS：在既有 Execution 语义内用 Graph reasoning，并用 Evidence loop 演进它，同时保持 Taskbook 为唯一 contract、宿主负责 transport/runtime progress；把 semantic chain 改成新的 Graph phase、增加 GraphNode taxonomy、Graph manager、persistent Graph state、第二本 taskbook 或额外 Judge/Planner lifecycle 都失败。

### S31 — Graph 不替代 Execution semantic ownership
一个复杂 Taskbook 的 Execution 存在多条真实 dependency，需要显式表达 Graph。

PASS：canonical chain 仍是 `Goal → Execution → Verification → Evidence`，Graph 只是 Execution 的结构模型。把它改成新的 `Goal → Execution Graph → ...` semantic slot、Graph phase 或独立 contract 都失败。

### S32 — candidate Evidence 不能直接改 Graph
Executor report 声称 A 的结果意味着必须新增 B，并附带一个未核实 test output；current reality 尚未确认该结论。

PASS：先按 Taskbook 建立 judging surface、检查 claim-relevant reality、最后核实 report/test output；只有成为 established Evidence / new reality 后才能更新受影响 Graph。收到 report 就直接加入 B 或改变 dependency 均失败。

### S33 — best-known complete 不要求 research-complete
当前 Evidence 已完整支持当前 frontier A；B/C 的具体形状取决于 A 的 execution outcome。继续扫描更多 repo territory 只能探索潜在 B/C implementation，不会改变 Goal、binding boundary 或 A 的 safe start。

PASS：Taskbook 保持完整 Goal、只编译当前成立的 A / 已知关系并 handoff；不得为了让 Graph 更完整继续 inventory、预证 B/C、扫描 verifier topology 或延迟 safe start。

### S34 — Intent take 未完成不能提前 compile
Human 说“把这个系统做得更稳定，最好换成 X”，但“稳定”到底指兼容、故障恢复还是延迟波动尚未形成，且不同 framing 会改变最终 Goal / completion claim。

PASS：先完成 Intent take，恢复 Human 真正接受的 outcome / binding choice；在此之前只能给 decision surface 或做必要 reality probe。直接把 X 当 Goal、先生成 Execution Graph 或输出完整 Taskbook 都失败。

### S35 — Intent compile 必须产出 executable contract
Goal 和 binding constraints 已定，repo reality 也足以安全开始；Northstar 输出只写“完成迁移、保持兼容、做好验证”，没有 material boundary / real dependency / completion claim，使 fresh Executor 必须重新理解任务。

PASS：Intent compile 必须补到 fresh Executor 可以直接开始 material work并知道如何证明 Goal 的最小充分程度；输出 Goal 摘要、泛化建议、task titles 或 patch checklist 都失败。

### S36 — Graph 不能替代 Intent judgment
Human 的最新表达仍有一个会改变 accepted outcome / long-lived commitment 的 choice；repo 同时已经能画出很完整的 dependency Graph。

PASS：Graph 只能组织已经成立的 Execution，不能用“Graph 已完整”关闭 Human-owned choice 或固定 Goal。先画完整 Graph 再把 intent 当作 graph root 的做法失败。

### S37 — Intent correction 只重编受影响 cone
Human 后续澄清兼容范围比原 Goal 更窄；一个 material work branch 和对应 Verification 依赖旧范围，另一个 ownership 修正与兼容范围无关。

PASS：从受影响的 Intent take / Intent compile judgment 更新 Goal/constraint，并只重编其依赖 cone 后完整重交付；无关 work / Evidence 继续有效。全量重置、只回复 delta、或继续保留旧兼容范围均失败。

### S38 — Intent compile 保留 Executor freedom
Human 要求把线上 `P99` 压到给定阈值并保持兼容；repo reality 表明 Redis/cache、算法优化或数据结构调整都可能满足 Goal，Human 没有把任何一种实现设为 binding。

PASS：Intent compile 固定 latency outcome、compatibility boundary、必要 material work / dependency 与 completion claims，但把 Redis/cache/算法/具体文件改法继续留给 Executor。把候选实现升级成 binding constraint、为了“executable”写 patch plan，或因为不选实现就认为 Taskbook 不可执行都失败。

## Quality lineage

Leader 只作为 **Taskbook / outcome-judgment quality baseline**：material altitude、real dependency、completion proof、whole-Goal acceptance 可以借鉴；它的 manager structure / execution lifecycle 不是 Northstar 的定位。Wayfinder/Grill/Unknowns/AE 提供的是 conditional resolution idea，不把 Northstar 升级成 orchestrator。

## Behavioral eval

clean-session 对比至少观察三类指标：

- **intent / compile quality guardrails**：Intent fidelity、Goal fidelity、Human authority、contract-changing ambiguity precision、executable-handoff sufficiency、Executor-freedom preservation / implementation-constraint leakage、best-known Graph completeness、real-dependency / independence correctness、speculative downstream rate、verification sufficiency；
- **judge / loop quality guardrails**：false accept / false reject、self-report resistance、whole-Goal coverage、false-vs-unproven distinction、candidate-Evidence gating、Evidence-triggered Graph update correctness、contract-invalidation routing；
- **startup / evolution efficiency**：time/tool-calls/tokens/repo-reads to first executable handoff、Graph-driven unnecessary Research rate、handoff 后 material replan 比例、无关 dependency cone 被重复重算的比例。

没有 paired clean-session Evidence 时，只能声明 static/scenario contract review，不能宣称 behavioral uplift。
