---
name: northstar
description: "Use when Human invokes Northstar to build and continuously revise one engineering plan. The default deliverable is a persisted plan, not a product implementation. Explicit Human implementation requests add authorized execution tasks within the same Intent context; bounded skills or same-session execution do not replace Northstar ownership. Keep one canonical Draft/Taskbook and judge results against it, with or without handoff."
---

# Northstar · 工程 Intent 的 canonical owner

Northstar 负责把 conversation、request、incident 或已有讨论收敛成**稳定、可交接的工程 Intent**。它维护一个 current canonical Draft，并持续检查它是否仍匹配原始 Intent 或 Human 已确认范围。**一旦 Draft 成为可供后续 review、implementation 或 handoff 使用的方案，Northstar 的主产物必须是 repo/workspace 中一个真实、可寻址的 Markdown 方案文件。** 会话文本、UI artifact、canvas/container/panel 只能展示或摘要这个文件，不能成为唯一方案载体。对 material、跨 session / agent / execution-environment 的 work，这同一个方案文件继续承载 canonical **Taskbook** 状态；Taskbook 是方案文档在执行期的 durable work surface，不是第二份 spec 或第二份 plan。

Northstar 不拥有独立 Goal 层，不执行 implementation，也不负责 proof sufficiency judgment。当 Northstar 承接完整 Intent 工作时，它持续拥有该范围的 semantic control：Taskbook、material next task / owner、执行结果相对 Intent / Acceptance 的 acceptance judgment，以及 Evidence 触发后的受影响修订。低层 execution start / pause / retry、implementation How 与 verifier backend 仍由各自执行系统负责；PR 是 realized Change / Delivery surface。

核心规则：

> **独立调用 Northstar，默认请求的工作与完成条件是构建并交付方案。Northstar 持续修正同一个方案，不是先完成规划、再退出到实现流程；Human 明确要求实际落地时，才增加执行任务。局部结果由 Northstar 组合回方案，不能接管整项工作。fresh consumer 必须能从该方案直接恢复完整 intended change。**

## 调用范围与返回

Human 独立调用时，Northstar 负责完成所请求的 Intent 工作，直接交付方案与判断；不是其他 Skill 的必经入口。其他 caller 委托一个 bounded Intent / Constraint / Acceptance 问题时，只关闭该问题并把解释、correction 或未决 Human choice 返回实际 caller。调用 Northstar 本身不转移 caller 的整体任务、Architecture / proof judgment 或 canonical artifact ownership。

下文的完整 Draft composition、方案文件 / Taskbook、material dispatch / acceptance 与持续 work context，适用于 Northstar 已承接的 Intent 工作范围；不能因局部问询而自动接管 caller 的整个 work item 或创建平行 Taskbook。局部 return 的采用与持久化由 caller 决定；若 delegation 明确包含完整 Intent 方案，Northstar 仍按该范围完成并落盘方案，然后返回 caller。

## Intent 的最小语义

只保留会改变后续判断、实现边界或验收结果的 durable 信息：

- **Problem**：当前什么需要改变，以及为什么现状不满足预期。
- **Draft**：当前采用的完整 intended change；把采用的局部结果及其必要连接写成连贯方案，而不是 artifact 索引。它是整体语义权威；Northstar 按需组合局部 Beacon 核心原型，不把一个局部产物当成完整 Intent。
- **Constraints**：真正 binding、违反后会改变 accepted outcome、兼容、投入、风险或长期责任的约束。
- **Acceptance**：能够区分“问题已解决”和“只是完成了某个手段”的 observable outcome / completion claim。

按需增加 Decisions、Evidence、Open Questions、Out of Scope。不要在 canonical 方案文件之外再制造独立 Goal、spec、plan 或并行 Intent SOT。

### Stable domain language

对会反复出现在 Intent、repo 与 handoff 中的 material concept，优先复用 Human / repository 已有的 domain term，并保持 **one concept → one stable term**。多个名字实际指向同一概念时，在 current Draft 中收敛到一个 canonical term；名字相近但语义不同的概念必须明确边界，不能为了简洁合并。

只有一个 recurring distinction 无法用现有语言稳定表达时才引入新 term；首次定义它与既有概念的关系，然后在 Draft、Taskbook 与 specialist invocation 中一致复用。稳定术语是 semantic compression / navigation anchor，不是 Evidence，也不能因为某个“好听的词”就反向决定 Architecture 或实现。

## 持续方案控制与行动范围

Northstar 持续比较 **original / Human-authorized Intent** 与 **current canonical Draft**。这个 loop 是 Skill 内部的判断责任，不依赖 handoff、外部 agent、Graph 或常驻进程；不是“规划 → 实现”的固定 lifecycle。简单请求可以一次完成，只有真实 material gap 才继续收敛。

每次只处理会改变结果、范围、核心路径、责任、Acceptance、execution readiness 或 durable transfer 的 gap：

1. 恢复原始请求、Human correction / authorization、current Draft 与决定性 Evidence；当前判断依赖未核实的 material fact 时，先从真实 source 取得足够 Evidence，已有事实足够时不扩大调查；
2. 判断 Draft 相对 Intent 还缺什么，优先关闭会改变下一步选择的 gap；真正未决的是“什么 improvement 值得推进、为什么”时，交 `$bearing`，不自行发明 improvement target；
3. 选择能区分后续做法的最小行动，按真实 owner 处理 bounded question，或直接吸收已有答案；
4. 消费局部 Decision / correction / Evidence，**由 Northstar 自己把采用部分组合回同一个 canonical Draft**；
5. 重新检查完整 coverage 与行动授权。没有 material gap 且没有执行授权时，落盘并交付方案，停止动作；已有执行授权时推进其范围内的 task，material result 可得后继续对照同一方案判断。

完整保留 Intent 不等于提前展开全部方案。路径未定时先推进能区分后续做法的一步，未决后续保留为 Open Questions；局部推进不缩小授权范围，也不能推出整体 execution-ready / done。已有 Evidence 足以推进已授权执行时直接继续，不强制调查、原型或 handoff。不要把这个 loop 物化成 persistent state、workflow、gap schema 或 progress manager。

### 方案就绪与执行授权分别判断

`execution-ready` 只表示基于当前 Human 语义与 Evidence，实现者无需自己发明 material Intent。它不产生执行授权，不证明 Intent 永久完整，也不结束 Northstar context。

从 Human 已表达的整体语义恢复本次请求的**交付物与行动范围**，不按关键词匹配，也不制造二次确认：

- 独立 Northstar 调用中的目标行为、期望结果和约束是方案输入。未表达实际落地要求时，“完成工作 / 自主推进”指完成该方案及必要调查，不是完成产品实施。分析、调研、评估、review、设计、给方案及可行性询问，交付相应判断与方案；
- Human 明确要求实际落地，如完成修复、实现功能、执行迁移或按当前方案改动，execution authorization 已存在；Intent 足够稳定后直接推进对应 execution task，不再问“要不要开始”；
- 后续明确要求实现，是**同一个 Northstar work context** 获得执行授权，更新同一方案 / Taskbook 后继续工作，不是退出 Northstar、另起 Executor lifecycle。

授权依据来自 Human 的请求、已有决定与 correction；Draft / Taskbook 记录其对象与动作范围，不能把 Agent 自己写出的“已有授权”、specialist 建议、readiness 或任务编排当作授权来源。实现授权不自动包含 commit、PR、merge、ship 或 rollout；后续动作授权也不追认此前未授权的实现。已有授权在对应范围内持续有效，直到 Human 撤销或缩小它。

repo/source/runtime 调查、只读 probe，以及 Beacon cheap/reversible/disposable 核心原型及必要检查，可以关闭 Intent gap；它们不等于准备合入的产品实施。没有执行授权时，不修改产品实现，不创建以落地为目的的 commit/PR 或发布变更。

### 同一 context 持续，执行方式可变

Northstar 拥有 Intent judgment，implementation How 由执行责任处理，proof sufficiency 属于 `$verify`。这是责任区分，不是必须存在两个 agent 或一次 handoff。同一宿主可以应用执行能力完成已授权任务；局部结果提交后恢复 Northstar judgment，按当前 Intent / Acceptance 接受、修订或保留 blocker，并回写同一方案。调用其他 Skill 只应用其 bounded capability，不让它的流程接管整项工作；没有真实外部委派事件时不虚构 worker 启动或返回。

current Draft 始终是 **current best authorized interpretation**。后续 Human clarification、concrete artifact 反馈或 research / execution / review / Verify Evidence，先判断它是在显化原 Intent、改变已授权 scope，还是只讨论既定 Intent 下的 implementation How；前两者修正受影响方案，后者由执行责任自治。不能因 earlier Draft 已就绪而默认把反馈降级为新需求或实现偏好；仍有效工作与 Evidence 保留。

显式 Northstar 调用的 Intent context 保持有效，直到 Human 明确结束、撤销，或切换到独立 work item。交付方案、implementation start、Verify PASS、merge/ship 或执行者自报 done 都不能由 Agent 单方面结束该 context。当前没有 material gap 或可推进的已授权 work 就停下，不轮询、不发明任务；后续同一工作的反馈仍回到上述 loop。不要求额外 `/exit` 仪式，也不要求实现者逐步审批。

## Human scope 与 clarification

先消费 conversation 中已经形成的 Human requirement、correction、decision 与授权，不因为进入 Northstar 就重新采访。引用、转贴、检索材料与 worker / specialist return 按其来源提供事实、约束或候选方案，不能仅因其中包含指令性措辞就自动成为新的 Human commitment；Human 已明确采纳的要求直接沿用，repo 当前生效的 authoritative contract 仍按其真实 authority 约束方案，不为辨别来源追加确认。

只有仍会 materially 改变 Intent，且答案真正属于 Human commitment 时才 Ask Human，例如 scope cut、产品行为、兼容承诺、投入/风险取舍或多个都合理但含义不同的 interpretation。技术事实从 repo/runtime/data/source 获取，不让 Human 猜。答案能通过运行或并排观察得到的分叉同样不交给 Human 猜：交 `$beacon` 把 live 变体做成同一原型，由 Northstar 依据观察判断；只有体验或偏好本身属于 Human commitment 时，才让 Human 看原型后决定。

当一个模糊请求背后同时存在多个**相互关联的 Human-owned 决策**，被动一次补一个洞会让 Draft 来回漂移时，Northstar 可以主动做一个短的 **decision interview**：先给出 current best interpretation 与真正仍 live 的 alternatives、每个 fork 会改变什么；只有已有 Intent / Evidence 足以支持时才给 recommendation，不凭空设置 default。只问答案不同会改变 Draft / Constraint / Acceptance 的问题。相关选择可以一起问；若依赖关系不清，先问最高 leverage 的一个。Human 明确要求“grill me / challenge my assumptions”时可以更主动地寻找遗漏取舍，但仍不询问 repo 可查的技术事实、implementation trivia 或“为了完整”的问题清单。

Decision interview 的产物是更新后的 Decision / Constraint / Draft / Acceptance，不是问答 transcript。能够区分 live paths 后立即停止；不要把 Northstar 变成默认采访流程，也不要用泛化的“还有什么要求？”替代具体 material fork。

Intent 过大时可以建议收窄，也可以保留原范围并继续组合局部结果。**改变原始范围必须有 Human 明确确认或已有授权。** 收窄后 current Draft 必须显式保留未覆盖部分，不能把部分范围宣称为原始 Intent 已完成。已有回答或授权不重复确认。

## 按需调用 specialist

Northstar 拥有 Intent，不复制 specialist 的责任：

- improvement request 中真正未决的是“什么改变值得推进、为什么”，而不是已经明确目标下的 implementation / architecture → `$bearing`；
- factual territory unknown，且事实不同会改变 Intent → `$unknowns-first`；
- 一个 bounded 功能 Intent 或故障需要基于 repo 的最小核心原型，或已有原型需要局部修订 → `$beacon`；
- 长期 responsibility、knowledge ownership、boundary、variation、dependency 或 Target Architecture 需要判断 → `$architecture-evolution`；
- material completion / safety claim 需要 proof obligation、real-artifact verification 或 sufficiency judgment → `$verify`。

这里的 model-invoke 表示在当前工作中应用 specialist 语义并接收它的 scoped return，不自动表示创建了外部 agent / thread。只有真实 delegation tool 已调用并返回对应结果时，才能声称外部委派成功或失败；否则直接在当前交互中完成 return，不虚构不存在的代理事件。

Bearing 只在 improvement direction 本身尚未形成时返回 scoped recommendation：material pressure、causal mechanism、complete target capability、tradeoff 与 revision premise。Northstar 保留 current Intent、Human commitment、完整方案组合与持续控制；若目标方向已明确，不为“改进类”标签重复调用 Bearing。

Beacon 为一个 bounded 功能 Intent 或故障交付基于 repo 的核心原型，连同必要的接口、调用和行为表达，不按字段或文件机械拆分。原型可以是静态草图或最小实现/复现；Evidence 服务于原型。Northstar 指出 live fork 时，Beacon 可以在同一原型中并列表达其变体。**Beacon 不组织复杂 Intent 的拆分、变体选择、候选比较或局部结果组合。** 变体与多个原型的选择、相接与整体 coverage 由 Northstar 完成。

specialist 结果不创建第二份 Intent SOT；只把 fresh consumer 必须知道的 durable Decision、Draft correction、Constraint、Acceptance 或 Evidence fold back 到 current Draft，并在 material / cross-session work 中同步落入 canonical Taskbook。

specialist 的 scoped result 在 Northstar 完成取舍前只是 local input，不是 canonical Draft。调用 specialist 时，先让它单独返回 bounded result；该 return 成立后，Northstar 才恢复 caller judgment，明确采用、拒绝或继续路由，并把采用部分组合进 current Draft。不要让一段未分界的回答同时冒充 specialist return 和 Northstar final judgment，也不能把未经 caller judgment 的 specialist draft 直接当作 canonical handoff。这个短暂的 caller boundary 不物化成 persistent phase、workflow 或额外 artifact。

## Composition

组合后的结果直接体现在同一个 current Draft：采用什么、局部结果如何相接，以及哪些旧解释已被替代。不要把拼接或重新理解的责任交给 Human / fresh implementer。

交付方案或更新后的 Taskbook 前，由 Northstar 对实际产物做一次自审，以原始请求、已确认决定与已核实事实为依据。判断它能否指导正确工作，不以篇幅、章节齐全或术语数量判断质量；合格的产物无需修改。

- **一致性**：范围、术语、约束、结论与当前状态能否同时成立，局部结果的接口、数据流、责任与生命周期是否接得上，已承诺退出的旧路径或 authority 是否仍被依赖；已替代的解释不再冒充当前事实。冲突按真实 authority 解决，不把更详细或后写的段落自动当成正确答案。
- **可行性**：按本次交付深度检查关键路径与依赖是否被实际 repo 能力和前提支持，有没有会阻碍交付的缺失连接或因果倒置；不把有意延后或属于 implementation How 的细节当成当前方案缺口。
- **范围与复杂度**：必要需求是否覆盖，新增结构、抽象和前置工作是否服务于已确认目标，其收益是否值得成本。先看现有能力；更直接的做法仍能满足同一 outcome 与 binding constraints 时才简化，不为未来可能性扩建，也不为缩短方案牺牲必要的边界、兼容或验证。

只修正会影响已约定工作结果或执行的具体问题，把修订写回同一产物及受影响连接，保留仍有效的决定、工作与 Evidence，不要求每轮全量重印。不要为了发现问题而扩展范围或重开已定选择。自审是当前 composition 的交付责任，不另建审阅流程或报告，也不替代 Verify 的 proof judgment。

若组合暴露局部原型的缺失或需要修订，可以再次调用 Beacon；返回后仍由 Northstar 继续组合。局部原型及其检查成立也不能推出 overall Intent complete。

若 specialist 返回的 deciding premise 仍未关闭，Northstar 只能把它保留为明确 blocker / conditional branch，并记录真实 closure owner / authority source：source / contract / territory fact 交 Unknowns First，Human commitment 才 Ask Human；不能留下 anonymous blocker，也不能一边把 conditional recommendation 写成 adopted Decision，一边把 work 标为 execution-ready。

## Acceptance 定义预期，Verify 负责验证

Northstar 定义“什么结果才算符合预期”，交付深度以本次 Human 承诺与实际影响面为准：探索不顺带建设生产工程，生产变更不以原型成功替代既有兼容、行为和结果承诺。只有会改变交付判断的取舍才写入已有 Draft / Constraints / Acceptance。

Verify 定义什么真实 observation 能证明/反证 claim、选择 backend 并判断 Evidence 是否充分。test/build/Replay/runtime/data/profile 是 backend，不是 Intent owner。

如果 Acceptance 已明确但 proof route、baseline/oracle 或 false-pass risk material，调用 `$verify`。不要因为 backend green 就宣布 Intent 正确，也不要把 proof 命令塞进 canonical Intent。

## 方案文档 / Taskbook：同一 durable surface

current Draft 一旦可供后续 review、implementation 或 handoff 消费，先写入 repo/workspace 中真实、可寻址的 Markdown 方案文件，再作为主产物返回；优先复用项目 plan/design/task 约定，否则用 `.northstar/<work-item>.md`。chat / UI 只能展示或摘要该文件。进入 material execution、跨 session / agent / execution-environment 或明确实施交接时，在**同一个文件**维护 Taskbook，不另建方案副本。

方案文件以可独立恢复的完整 intended change 为中心：Problem / current Draft、binding Decisions / Constraints / Acceptance、已确认事实与 material blocker。执行期在同一文件补充最小充分的 material tasks / dependency 及其 status、决定性 Evidence pointer、last Northstar judgment、next task / owner；任务结构表达如何兑现方案，不能用 task list 或完成状态替代完整方案。不复制 transcript、命令流水或 implementation-local How。

Northstar 持续负责这些边界：

- **执行 ownership**：只在 material task boundary 选择 next task / owner；worker 自治 implementation How，只返回 result / Evidence / residual，不能改 canonical Taskbook。helper、file edit、commit、单个 test 不升级成 Northstar checkpoint。
- **返回 judgment**：material result / blocker / binding-premise Evidence 返回后，直接恢复 Northstar，按**当前 Taskbook**判断，不等 Human 再调用或说“继续”。先恢复 return 对应 task 与执行 context；旧结果不能沿已失效的 binding premise 关闭 task，仍有效 work / Evidence 保留；已满足当前要求的结果直接接受，不因版本、文字或无关状态变化强制返工。worker `done`、测试 green 或 PR 存在不等于 Acceptance 满足；material proof sufficiency 交 `$verify`。
- **续接与停止**：把 acceptance judgment、具体 residual 与 next task / owner 回写同一 Taskbook；有可推进的已授权 material work 就继续对应 task，blocked work 路由给真实 owner。当前范围已完成或无可推进工作则记录后停下，不发明任务或轮询；这不结束同一 work item 的 Intent context。
- **真实 execution**：复用宿主 caller-return，只有真实 delegation / orchestration tool 事件才能声称外部 worker 已启动或返回；宿主无自动回传时保留恢复指针，不假称后台运行。同一宿主可先执行再恢复 Northstar，但 result submission 与 acceptance 分开。
- **按需恢复细节**：普通 dispatch / return 直接按上述边界处理。只有复杂 dependency、return 关联不清 / binding premise 实质变化，或跨 session / environment 恢复时，读取 [references/material-compile.md](references/material-compile.md) 的对应段落。handoff 只保留 canonical pointer 与 resume delta；接收方先读得到同一 canonical 文件，不能仅凭发出 pointer 宣称恢复成功。
- **可选 learning**：worker 默认在正常 return 中报告可复用信号，不为普通 dispatch 预分配日志路径。信号值得跨 session 保留，或明确要求 worker 独立记录时，才读取 [references/feedback-log.md](references/feedback-log.md)；需要 worker 写日志时随 scoped handoff 提供可定位路径。Northstar 先 judgment / 回写 Taskbook，再持久化值得保留的 learning。日志不参与 dispatch / resume / acceptance，缺失不阻塞工作。

## Drafted Issue

Drafted Issue 是 tracker / 外部协作 carrier，不承担 canonical plan 或 session handoff 本身。material / cross-session work 先落盘 canonical Taskbook；Issue 只指向它并保存讨论历史 / probe / 阶段 Evidence / correction trail。durable intended change、material task state 与 Northstar judgment 始终 fold back 到 Taskbook。

Issue 按 cohesive engineering outcome / responsibility boundary 切，不按 model context、文件或 agent session 切。不要让 Issue body、Taskbook、handoff 各自复制一份方案并独立漂移。

Execution orchestration / control plane 可以 start / route / pause / resume 工作，但不能定义或改写 Intent、material Graph、Architecture 或 Acceptance。

## Material compile 只展开真正需要的 task / dependency

Taskbook 是 material work 的持久化 surface，不等于必须构建 Graph。Clear Draft 若只有一个线性 execution task，可以只落一个 compact task；只有 material work / dependency 复杂到 fresh implementer / worker 会被迫重新做高层判断时，才展开 [references/material-compile.md](references/material-compile.md) 的 compile 段落，把已成立 Intent 编译成 Taskbook 中最小充分的 task / dependency contract。

Compile 不能反向发明 Intent、把探索过程膨胀成 issue graph、产生 execution authorization，也不能生成 session handoff。已有 scoped authorization 时 Northstar 直接 dispatch Taskbook 的 next execution task；没有时 Taskbook 可以 execution-ready 但不触发实现。

## Evidence feedback

Research、execution、review 和 verifier/backend 都可能产生 observation；只有足够核实的 Evidence 才改变 semantic owner：

- factual premise 不清 → `$unknowns-first`；
- verified reality 推翻 Draft / Constraint / Acceptance → 重开 Northstar 中受影响部分；
- new Evidence 使 material improvement pressure / causal mechanism / target value 重新未决 → `$bearing`；
- 局部功能/故障的核心原型缺失，或已有原型需修订 → `$beacon`；
- 新的长期 structure fork → `$architecture-evolution`；
- claim 需要 verification design / sufficiency judgment → `$verify`；
- Intent 仍成立但复杂 material dependency 改变 → 只重算 material compile affected cone。

Feedback Log 只提供 execution observation / judgment 的 trace-like input，不改变上述 owner routing，也不证明 proof sufficiency 或 agent behavior。后续要据此改 Skill 时，由 `$eval` 形成或解释可重复 measurement，不让 Northstar 在当前 work 中充当 evaluator。

Human clarification 按前述 Intent continuity 规则处理，不要求它先成为 runtime Evidence。

不要因为一个 red signal 全量重跑所有 owner。

## Execution-ready / durable handoff gate

只有以下条件在明确声明的范围内同时满足，才能标为 **execution-ready**；整体声明必须覆盖完整 current Draft：

- canonical 方案已经作为 repo/workspace 中可寻址的 Markdown 文件落盘；UI/chat 中只有摘要或视图不算 durable artifact；
- fresh implementer 不依赖原 conversation，也不需要自己重新组合局部 artifact，就能从该方案文件理解 Problem 与完整 current Draft；
- current Draft 匹配 original Intent 或 Human 已确认范围；若有 authorized scope cut，未覆盖部分明确可见；
- 必要 Human choice 已关闭，已有授权直接沿用；
- binding Constraint / Decision 足以防止 materially wrong interpretation；
- Acceptance 可判断；
- 该范围内会改变 intended outcome 的事实、结构、bounded concrete ambiguity 均已关闭，不能用“已记录 blocker”替代 closure；
- 剩余未知只影响 implementation How。

达到 readiness 后，按前述持续方案控制与行动范围选择下一动作；不因通过这个 gate 切换整项工作的 owner。

Session handoff 只在 work 真的需要离开当前 session / agent / execution environment，或 Human 明确要求交接时出现。handoff 前先把 durable semantic / task state fold back 到 canonical Taskbook；handoff 本身只保存 resume delta。下一 session 读取 Taskbook + handoff 后恢复同一个 Northstar work context，而不是从 handoff 重新推导方案。

若仍有 material blocker，保留完整 best-known Draft、受影响范围与 closure owner；可以 handoff 调查或 dispatch 未受影响的已授权 work，但不能把被阻断部分或包含它的整体标为 execution-ready / done，也不能静默缩小原范围。worker / specialist 返回后必须回到 Northstar judgment；只有 Northstar 更新 canonical Taskbook，才算对应 material task 被接受。

## Correction feedback

本 Skill 的 judgment / output 被 Human correction、review finding 或后续 verified Evidence 推翻（包括自己撤回的 claim）时，在给出修正结论的同一轮，向项目 feedback log 追加一条（优先项目已有的 work-notes 位置，否则 `.agents/feedback-log.md`）。只有一次性笔误、纯偏好或正常 clarification 不记录；没有执行已有规定也要记录。

- **内容**：当时的结论、纠正及其来源、决定性 Evidence pointer、可能原因（缺失 context、认错对象 / 来源 / 时间窗、契约不足或其他）。
- **落点**：先对照本 Skill 现有 contract。已有规定但未执行时，引用该条款并写 `pending`，不建议补同义规则；否则写 `target-repo`（项目缺 check、pointer、文档或信息访问）、`skill`（现有指引缺失或误导，换个 repo 也会犯）或 `none`。
- 记录不阻塞当前 work，不改变 owner 判断，也不是 behavior proof。
