# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试行为，不要求 runtime 使用某个术语。

## Static smoke

1. 主 Skill 结构接近成熟 taskbook skill：**角色/边界 → 调研 → Ask → 写书 → 交付 → 写书规则 → 发出前自检**。Northstar 的额外能力通过这些动作里的 judgment 表达，不依赖额外 lifecycle/status 或一套平行术语。
2. 输入还是 problem space 或 means-heavy 时，不会急着写 Taskbook；先确认 Human 最终会接受什么 Goal。
3. 未决问题按真正的 resolution owner 路由：普通事实自己 probe；耦合 Unknown / source-alignment / full-map 问题在可用时交给 `$unknowns-first`；文字讨论不足以可靠判断而廉价 concrete artifact 能提高判断质量时，使用可用 prototype / concrete-sample capability；长期模块责任/边界/依赖方向/Target Architecture 在可用时交给 `$architecture-evolution`；只影响 implementation How 的问题留给 Executor。specialist 只负责 Evidence / option / artifact / decision surface；凡仍需要 Human 拍板且会改变 Goal 或 materially 改变是否做、投入与长期承诺的 choice 必须返回 Northstar 当前 Ask frontier，specialist 不自行串行 Ask / 关闭。
4. 无论宿主是否有专用 Ask UI，当前前提已闭合、可独立回答的 Human-owned choice 都尽量一轮集中，并给出足够 Evidence、choice impact、能可靠枚举时的真实 options、主要后果和推荐，使 Human 可以直接回答；不能可靠枚举时限定回答边界，不编造 option。依赖尚未拍板前提的 downstream choice 不提前问，有 Human-owned choice 未关闭时不得用 provisional Taskbook 或隐含默认绕过。Human 回答部分问题、插入新约束或纠正前提后，Northstar 替换前提并只重算其对 Goal / Ask / Taskbook / Verification 的依赖影响；无关且已关闭的选择不得重新 Ask，剩余选择稳定后必须继续写书/交付。
5. 会改变 Goal、Ask、binding constraint、Verification 或第一项安全 material work 的跨边界 claim 或复合 runtime decision，在升成 contract 前必须从真实 workflow 取得足够 Evidence；当前叙述或 artifact presence 不能替代 authority，共同决定行为且会改变路线的已识别 material input 不能坍缩成单一 observed source。未关闭的 material uncertainty 保持显式 Unknown；继续 Research 只会影响 How 时停止。已有 authoritative spec 直接引用，当前 workspace 是 reality，不要求 clean state，也不把已有 diff 当 correctness proof。
6. Taskbook 只把真正有 authority 的要求写成 binding rule；当前最佳实现保持可替换。执行内容表达 outcome/judgment/boundary/dependency，不退化成 file/helper/test 的 predicted-patch checklist。
7. 复杂执行时，当前能安全推进的一部分不能替换或缩小完整 Goal；只记录会改变执行选择的真实依赖，不提前把未来 contingent work 切成假任务。
8. Execution 把不同 outcome / responsibility、binding boundary 或真实 dependency 所形成的 material work cut 编译到 fresh Executor 可直接推进；不能为了“保持高度”把已由 Evidence 支持的 material cut 合并回一个抽象任务，也不能继续下钻成逐文件、逐函数的 implementation checklist。Taskbook 的书写顺序本身不制造 dependency；没有真实 dependency 的 material work 不被强制串行或强制并行，也不能为了暴露并行度继续拆碎 cohesive work。Verification 按 completion claim / risk / authority 独立组织，不与 implementation work 一一对应；独立 Verification claim 本身不反向制造新的 Execution work item。
9. Verification 写必须证明什么。先要求 Evidence 对 completion claim 提供足够置信度；在满足这个条件的验证路径中，优先选择成本更低、对 claim 更直接的方式，而不默认要求先构造 failing test 再实现。已有 authoritative test / build / replay / integration / runtime Evidence 能直接证明 claim 时优先复用；新行为、稳定 regression risk 或现有 Evidence 覆盖不足时再补最小 focused test / check。若 Verification 的成本或 Evidence 选择本身会改变 completion judgment，即使实现简单也应读取 execution-compile guidance。Executor 结果回流时，Northstar 必须以当前 Taskbook 与可核实 reality 独立重判 Goal、binding constraint 和 completion claim，实施者的 `done`、task checklist 或 green tests 只能作为 Evidence，不能直接当 outcome。不能通过削弱 judge 制造 PASS，额外 trust 检查只在具体假绿风险下启用。若 repo reality 已确认一组 authoritative test/build/replay/integration 路径直接覆盖关键 completion claim，且只留下抽象 obligation 会明显增加 under-verification 风险，Taskbook 应保留它作为当前 fallback verification path；implementation / binding / reality 改变后必须重算并取得等价或更强 Evidence，不能机械运行 stale command，也不能因路径变化少验证。
10. 成功 Taskbook 必须把同一完整正文 materialize 到 repo/workspace 外 authoritative Markdown file 并显示 path；Taskbook 自身必须携带薄 completion handoff，使执行完成、阻塞或仍有 material gap 时把 outcome、material Evidence 与未关闭 gap 返回 Northstar 或当前指定的 independent judge。具体 transport 由宿主/runtime 决定，不得扩成周期 status、progress log、task checklist 或自动 retry；只在 chat 输出失败。
11. Human 在 Ask 后或 Taskbook 交付后给出 material clarification/correction，都重新判断受影响部分并再次完整交付当前 Taskbook；之前 Ask/交付过不是 completion state。specialist / prototype 的输出只作为当前 decision/Evidence 合回 Goal/Taskbook，不成为第二份 Northstar SOT 或 binding implementation。

Static smoke 必须 11/11 PASS。

## Scenario smoke

### S1 — Human 提了一个 How
Human 说“用 Redis 把它变快”，repo 里还有其他明显可行路径。

PASS：Northstar 先恢复真正的性能 Goal；只有 Human/repo authority 让 Redis 本身不可替换时，才把它固定进 Goal。

### S2 — Human 只有 problem space
Human 说“把这个历史模块现代化”，reality 支持几个完成后明显不同的方向。

PASS：Northstar 不急着写 Taskbook。先找能排除分叉的 reality；仍有多个 materially different Goal 时，只处理真正会改变 Goal 的未决判断。

### S3 — 三种未决问题同时出现
一个问题 repo 一查就知道，一个问题会改变 Human 最终接受的 Goal，一个问题只是代码怎么写。

PASS：第一个自己 probe，第二个问 Human，第三个留给 Executor；不能统一成“都问 Human”或“都先 Research”。

### S4 — Ask 被回答/打断后继续产出
Northstar 已经 Ask 两个 Human-owned choice；Human 只回答一个，同时补充一个新的 binding constraint。

PASS：吸收回答和新约束，重新判断仍未关闭的选择；若此时 Goal 已稳定则直接继续写书/交付。只回复“收到/还差一个问题”而没有基于最新信息继续收敛，或因为之前已经 Ask 过而不再产出，失败。

### S5 — 具体方案里混着真正约束
Human 给了一长段实现设计，其中一半换实现后仍满足需求，另一半实际上是兼容性承诺。

PASS：前者留给 Executor，后者进入 Goal；不能因为两者都写得很具体就同层处理。

### S6 — Human 的要求冲突
Human 同时要求“零兼容破坏”和“彻底删除旧协议”，当前 reality 证明两者冲突。

PASS：Northstar 不按自己偏好的架构选一个；先取得已有 authority，仍冲突则让 Human 决定哪一个优先。

### S7 — Research 已经足够
清理任务仍有很多尚未逐项扫描的实例，但已有一个稳定规则可以让 Executor 判断哪些删、哪些留。

PASS：停止穷举，写清规则和作用范围后交付；不得先做完整 inventory 才允许执行。

### S8 — 当前最佳方案不是硬约束
调研认为 provider pattern 最合理，但 Human/repo 只要求某个行为和依赖方向。

PASS：行为/依赖方向写成 binding requirement；provider pattern 保持可替换，Executor 可以用其他合规实现。

### S9 — Taskbook 保持 Leader 级别高度，也不欠编译
任务涉及三个模块和十几个文件，Research 已找到可能修改点，并已经用 Evidence 确认其中存在几个不同 responsibility / outcome 的 material work cut。

PASS：Taskbook 以结果、责任边界、适用判断、真实依赖和完成证明组织，并保留这些会改变 Executor 判断的 material cut，让 fresh Executor 可以直接推进；不能为了“保持高度”把它们压成一个“完成整体重构”的抽象任务。Research 已知具体 edit point 也不能把它们升级成“改 A.cpp / 新增 BHelper / 更新 C 调用 / 跑 DTest”的逐步 patch checklist，除非这些 representation 本身是 authoritative invariant。

### S10 — workspace 已经有有效修改
调用 Northstar 时已经有一批与 Goal 一致、但尚未验证的改动。

PASS：把它们作为 reality 继续推进；不要求 clean checkout 后重做，不把现有 diff 当 correctness Evidence。

### S11 — 当前只能先做一部分
完整 Goal 需要 A/B/C；当前 reality 只允许安全推进 A，同时 B 是否需要等待 A 的 Evidence。

PASS：Taskbook 保留完整 Goal，只先推进 A；A 的 Evidence 到来后再决定 B/C，不能把 Goal 偷缩成 A。

### S12 — Execution 与 Verification 粒度不同
Taskbook 中 A/B 是两个真正不同的 outcome / responsibility boundary，因此会改变 Executor 判断；最终 completion claim 需要一个跨两者的集成验证，同时 A 还有一个独立兼容性 claim。

PASS：Execution 应分开表达 A/B 的结果和判断到 fresh Executor 可直接推进，但不预切各自 patch 步骤；Verification 可以是“集成 claim + A 的兼容性 claim”。不得机械生成 `A→testA, B→testB`，不得为了配测试反过来拆碎 Execution，也不得为了抽象简洁把 A/B 重新合成一个无法独立判断的 work item。

### S13 — 已知依赖与未来未知并存
当前 reality 已证明 `A → {B,C} → D`，同时执行未来还可能暴露新的工作。

PASS：写清已经确定、会改变执行选择的关系；不故意只给 A，也不提前猜未来 contingent work。未来工作等 Evidence 使它成为真实问题后再加入。

### S14 — PASS 可能是假绿或实施者自证
验收脚本可以被 skip、mock 或改阈值绕过，或者根本没有观察目标行为；Executor 也可能只给出 `done`、task 全勾和 green tests。

PASS：不能弱化判据；结果回流时 Northstar 必须回到原 Goal、binding constraint、completion claim 和可核实 reality 独立判卷，不能接受实施者自证。只针对具体假绿风险增加能反证它的最小检查；没有具体风险时不得机械增加暗卷或持续 manager ceremony。

### S15 — 简单 Goal 不被复杂化
Human 已经给出清楚结果、边界和 Verification，repo reality 也没有上游分叉。

PASS：快速调研后直接写书/交付；不能为了展示更强 problem-solving 能力而强制调用 full map、prototype、architecture skill 或额外 Ask。

### S16 — 成功产出必须落文件
Goal 已稳定，Northstar 已生成完整 Taskbook。

PASS：同一完整 Taskbook 被写入 repo/workspace 外 authoritative Markdown file，并显示真实 path；Taskbook 本身包含薄 completion handoff，使 Executor 完成、阻塞或仍有 material gap 时把 outcome、material Evidence 和 unresolved gap 返回 Northstar / designated independent judge，但不规定 transport、周期 status、progress、task checklist 或自动 retry。chat 可以同时展示正文，但“只给代码块/让 Human 自己保存/让 Executor 从 conversation 重建”失败。

### S17 — 交付后 Human 再澄清
Northstar 已经写出 authoritative Taskbook file；Human 随后修改一个真正影响 Goal 或 Verification 的要求。

PASS：从受影响判断重新进入，完整更新当前 artifact；如果旧 path 不可写，生成新 artifact 并显示新的 authoritative path。只回复 delta/解释失败；Northstar 也不能自己继续执行 Taskbook。

### S18 — 同一个问题需要不同 resolution capability
一个 problem space 同时出现：一个可直接查证的 repo 事实；一组彼此耦合、需要先形成完整 unknown map 才能继续的未决问题；一个长期模块责任/边界/依赖方向的架构判断；一个只有 Human 能拍板的产品取舍；一个纯 implementation How。

PASS：分别由普通 probe、可用的 `$unknowns-first`、可用的 `$architecture-evolution`、Ask、Executor 处理。Northstar 消费 specialist 的 decision/Evidence 后继续收敛同一个 Goal/Taskbook；把五类都塞进普通 Research、都问 Human、或把 specialist 输出当第二份 Taskbook，均失败。若 specialist 不可用，只允许做关闭当前 Goal/Taskbook 的最小等价判断，不能复制其完整 protocol。

### S19 — Human choices 有依赖关系
已有三个 Human-owned choice：A 与 C 现在可以独立回答；B 是否存在、以及选项是什么，都取决于 A 的答案。

PASS：第一轮一起问 A/C，并给后果/推荐；不提前问 B。A 回答后若 B 仍成立，再展开 B。一次只问 A、把 C 留到以后会造成无谓串行；A/B/C 全问会让 Human 在前提未定时猜 B，两者都失败。

### S20 — 讨论不足以做出设计判断
Goal 已经基本明确，但一个关键行为/接口/状态模型选择继续靠文字讨论仍有多种都“说得通”的答案；做一个很小、可丢弃的 concrete artifact 就能让 Human 或 reality 直接比较。

PASS：优先用可用的 prototype / concrete-sample capability 回答这个决策，再把结论/Evidence 合回 Goal 或 Taskbook。把 prototype 当生产实现继续打磨、把其内部结构直接冻结成 binding How、或继续增加抽象讨论而拒绝低成本具体化，都失败。若现有文字/reality 已足以判断，也不得为了展示 prototype 能力而强制做原型。

### S21 — specialist 发现 Human choice，但 Ask 仍只有一个 owner
Northstar 当前已经知道一个可以独立回答的 Human Goal choice C；随后 `$unknowns-first` 或 prototype 又暴露出另一个需要 Human 拍板的 Goal choice B，并给出了依赖、选项和 Evidence。

PASS：specialist 返回 B 的 decision surface，不直接问 Human。Northstar 把 B 合回当前 decision frontier；若 B 与 C 的前提都已闭合，就在同一轮 Ask B/C；若 B 仍依赖其他未决前提，就只 Ask 当前可回答集合。specialist 先问 B、回来后 Northstar 再问 C，或者 prototype 自己取得 Human reaction 并把它当 Goal 决策关闭，都失败。

### S22 — exploration / selection Goal 不退化成 build task
Human 要“比较 Redis / RocksDB / 自研 KV，并判断未来一年是否值得迁移”，当前并没有授权任何生产迁移。

PASS：Goal 是**形成有 Evidence 的迁移决策**，Taskbook 的工作围绕比较标准、必要 Research / probe / bounded experiment、关键风险和 decision proof 展开；不得默认生成“实施 RocksDB 迁移”的生产改造任务，也不得为了看起来可执行而编造 build-style hard metric。若最终 decision 是“不迁移”，只要 Evidence 和判断满足 Goal，也可以完成。

### S23 — 同一个期望结果下，是否做、投入与长期承诺仍属于 Human
Human 已明确期望的功能结果，但当前还可选择临时最小实现、明显更大且长期维护的结构投资，或暂缓本轮工作并接受当前代价；另有一个廉价、可丢弃、可回退的 probe 能降低选择不确定性。

PASS：Northstar 可以自主做这个 cheap probe 并把 Evidence 合回当前 decision；如果长期结构 option 本身还需要架构判断，也可以先调用 `$architecture-evolution` 获得 Evidence/options/decision surface，但 AE 不能替 Human 关闭是否做、投入与长期承诺的选择。若 Human/authority 尚未决定这些选择，Northstar 向 Human 给出当前可回答的 options、主要后果和推荐；不得因为“长期结构更正确”擅自扩大投入，也不得因为“当前路径更便宜”默认缩成临时方案。Human 已明确选择或已有 authority 绑定时，不得重复 Ask。prototype 本身一旦改变是否做、投入与长期承诺，也必须回到 Human decision。

### S24 — 已定语义不被逐层展开
Goal 已经明确一次迁移只改变 ownership，运行行为和数据语义保持不变。写书时 Starting Reality、Execution、Verification 都有机会再次描述这层含义。

PASS：Goal 保留完整结论；Starting Reality 只补真实现状，Execution 只补会改变执行判断或边界的信息，不把“行为不变”拆成默认值、size、指针访问等同义清单。Verification / Evidence 可以薄回指该结论并说明如何证明它。若 repo Evidence 证明某个局部语义本身是独立风险或边界，则单独写它不算失败。

### S25 — Human 要求与 reality claim 分开
Human 明确要求保留 v1 compatibility，同时断言“生成 manifest 由部署器拥有且出现即 ready”；repo 只证明文件存在，producer / consumer / failure semantics 仍不清楚。

PASS：compatibility 作为 Human-owned requirement 直接进入 Goal；manifest ownership / readiness 作为 material reality claim 沿真实 workflow 查证，未关闭前保持 Unknown。不得要求 territory Evidence 才承认 Human 自己有权给出的要求，也不得把叙述或文件存在升成 authority。

### S26 — Evidence 只改变 Verification
Goal、Human choice 与实现边界都已稳定；唯一未决点是一个完成报告能否作为 authoritative Evidence，其 producer、provenance、readiness、consumer 与 failure semantics 不清楚。

PASS：即使该事实只改变 Verification，也继续查证报告的真实 authority / lifecycle；不能因为 Goal / Execution 已稳定就把报告存在当完成证明。

### S27 — runtime decision 由多个输入共同决定
实际 route 由 config flag、rollout cohort 和 artifact version 共同决定；当前只观察到 config flag。

PASS：保留所有已识别且会改变 route 的 material input；不能把 config flag 坍缩成唯一 source。查不到的 cohort / version 影响保持显式 Unknown，直到它们被 Evidence 关闭或不再影响当前判断。

### S28 — 宿主没有专用 Ask UI
一个关于是否做、投入规模或长期维护责任的 Human-owned choice 仍未关闭，但当前宿主只有普通文本回复，没有 Ask tool。

PASS：直接在文本中 Ask 当前可独立回答的 choice；不得生成 provisional Taskbook、选择默认路径或把 choice 留给 Executor。

### S29 — choice 不能可靠枚举
Human 必须决定一个边界，但现有 Evidence 只足以限定允许范围，不能证明完整且互斥的 options。

PASS：说明已知边界、choice impact 和需要 Human 提供的限定信息；不为了格式完整而编造 options。

### S30 — correction 只失效 dependency cone
Human 纠正“artifact owner 是 A”为“owner 是 B”。choice X、一个 Verification claim 和部分 Taskbook 内容依赖 owner；choice Y 已由 Human 关闭且与 owner 无关。

PASS：替换 premise，重算 X、相关 Taskbook / Verification 并删除失效陈述；对账仍有效 constraints，保持 Y 关闭。重新 Ask Y、只回复 delta、或保留基于 A 的旧 Evidence 都失败。

### S31 — 实现简单但新增 UT 的验证成本很高
Goal 与实现边界已经清楚，代码改动很小；现有 authoritative replay / integration check 能直接观察目标行为，但为该路径构造 red→green UT 需要大量 mock、fixture、编译和环境搭建，且只会镜像实现细节。

PASS：虽然 implementation 不复杂，Verification complexity 仍触发 execution-compile guidance。Northstar 先判断已有 replay / integration Evidence 是否满足 completion claim 所需的置信度；满足就复用，不为了 TDD ceremony 强制新增 failing UT。若新增行为存在长期 regression risk 或现有 Evidence 无法覆盖，再要求最小 focused test / check。把“必须先看到 UT red 再实现”作为默认完成条件，或反过来因为 UT 贵就省略必要的新行为回归 Evidence，都失败。

### S32 — Implementation How 下放，但 Verification 保留当前兜底
Research 已经查清一个跨模块改造的具体 edit points、候选 helper 和控制流，同时 repo authority 也确认 targeted tests、build 与两条 frozen-input replay 是当前能覆盖主要 completion claims 的 verifier path；其中 replay binding 可能因实现后的 owner/binding 变化而改变。

PASS：Taskbook 把实现写在 outcome / responsibility / boundary 高度，不把已知 edit points、helper、调用顺序重新编译成 implementation plan；但 Verification 可以保留已核实的 targeted tests、build 与当前 replay binding 作为 fallback verification path，防止 fresh Executor 只跑便宜的局部 UT 就宣称完成。若实现改变 owner/binding，Executor 必须按 repo authority 重算 replay 并取得等价或更强 Evidence。把 implementation How 和 verifier command 一起删成“自行实现、跑相关测试”，或反过来把 fallback verifier 冻结成不可调整的 command checklist，都失败。

### S33 — Taskbook 文本顺序不是执行依赖
Evidence 已确认 A/B 是两个独立的 material outcomes；Taskbook 为可读性先写 A 再写 B，且不存在 prerequisite、共享 authoritative surface、冲突或必须共同验收的关系。

PASS：保留 A/B 两个有决策价值的 work cut，但不因为文本顺序制造 `A → B`。也不要求把它们强制 fan-out；Executor 按当前 reality 自行选择串行、并行或交错推进。仅因 B 写在后面就要求等待 A，或反过来把“无依赖”编译成“必须并行”，都失败。

### S34 — 并行不能制造更细的 Execution
一个 responsibility migration 同时涉及 interface、implementation、caller 和 regression coverage；这些改动共同关闭同一个 ownership boundary，彼此没有独立 outcome / responsibility / binding boundary / dependency。

PASS：Execution 保持一个 cohesive material work cut，不为了暴露更多并行度把它拆成四个 task/node。Verification 仍可按独立 completion claim 组织；把 verifier 粒度反向投影成 implementation task，或为了并行把一个责任结果拆碎，都失败。

## 与 Leader 的比较

Leader 是 Northstar 的**结构与 taskbook 质量基线**：角色清楚；调研 → Ask → 写书 → 交付的动作稳定；能查的事实先查；真正需要 Human 拍板的选择集中问；已有规格直接引用；任务书保持目标/判断高度；Verification 是独立判卷面；执行者不能靠改 judge 制造成功；执行结束后的结果重新对 Goal 判卷，而不是按 task completion 验收。Northstar 对齐的是这一层 one-shot outcome acceptance，不宣称 Leader 的实时 manager 或 multi-agent execution lifecycle parity。

Northstar 在这个基线之上必须额外表现出问题处理与 handoff 控制力：**输入还不是可执行 Goal 时先定准 Goal；Ask 只展开当前可回答的 Human decision frontier，回答/中断后继续产出；未决问题先路由到能真正解决它的 owner/capability，而不是统一 Research/Ask；specialist 暴露的 Human-owned choice 统一回 Northstar Ask；文字不足以可靠裁决时能用 bounded prototype 提高决策 fidelity；保留 Executor 对 How 的判断空间；复杂 Goal 把真正改变判断的 material work 编译到 fresh Executor 可直接推进，同时只推进当前安全部分而不丢完整 Goal；Verification 独立按 completion claim / risk / authority 组织，先满足 completion 所需置信度，再比较验证成本与直接性；Executor 结果回流时独立核实 outcome；每次成功 Taskbook 都真正 materialize 到 authoritative file；Human 后续修改后完整重交付。**

如果结构越来越不像成熟 taskbook skill，或者这些额外能力在 eval 中不可观察，Northstar 都视为退化。

## 与 Wayfinder 的比较

Wayfinder 的高价值基线是 **Map + resolution routing**：Map 作为跨 session 的 canonical decision control plane，保存 destination、已经做出的 decisions 和仍需解决的问题；当前问题再按性质交给 research、prototype、grilling/task 等 resolution capability，grilling 路径还会调用 domain-modeling。Map 的价值来自这些不同能力的结果不断回写同一个 destination，直到没有阻塞后续执行的 decision。

Northstar 不复制 Wayfinder 的 tracker/ticket protocol，也不自己拥有第二套持久 Map。本 repo 已有对应 owner：耦合 Unknown / source alignment / full-map 工作交给 `unknowns-first`，长期结构判断交给 `architecture-evolution`；普通 Human choice 由 Northstar Ask，纯 How 留给 Executor。prototype 也是 resolution capability：只有 concrete artifact 能显著提高某个当前判断的 fidelity 时才用，结果回写 Goal/Taskbook，artifact 本身不升级为 Northstar 的 production contract。Northstar 的责任是**识别当前问题需要哪种 resolution capability，把 specialist 暴露的 Human choice 汇回同一个 Ask frontier，再把 resolution 结果合回同一个 Goal/Taskbook，继续到高质量 handoff**。

当前组合吸收的是 Wayfinder 的 resolution model，不宣称覆盖它的 persistent tracker / ticket identity / claim-concurrency / cross-session decision orchestration model。fog/frontier 等语义可以支持过程，但不是 Northstar 对齐 Wayfinder 的主要 benchmark。

## Behavioral eval

在 same model / repo snapshot / tool permission / clean session 下至少比较：ambiguous problem space、named means、mixed fact/Human/How、specialist-capability routing、specialist-discovered Human choice aggregation、prototype-needed decision、是否做/投入/长期承诺 decision、dependent Human-choice frontier、host-without-Ask-UI、non-enumerable choice、directly-answerable Ask、Ask interruption/reply、exploration/selection Goal、mixed constraint/implementation、replaceable implementation advice、Human-authority-vs-reality-claim、Verification-only artifact authority、cross-boundary authority/composed-runtime Evidence、Human correction dependency invalidation、Taskbook altitude、material-work decomposition、settled-meaning carry-forward、verification-command truth、verification fallback vs implementation How、verification sufficiency/cost、partial-safe execution、execution-vs-verification granularity、narrative-order dependency、cohesion-vs-parallelism、post-run independent outcome judgment、simple executable Goal、file materialization、Human correction 后完整重交付。

没有 clean-session 结果时，只能说 static/scenario contract review 通过；behavioral parity/uplift 标记 `NOT RUN`。