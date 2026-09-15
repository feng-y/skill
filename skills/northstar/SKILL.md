---
name: northstar
description: "Canonical engineering-intent control: keep the original or Human-authorized request aligned with one current Draft, route material gaps to the right owner, compose returned results, and maintain durable executable meaning as work evolves."
---

# Northstar · 工程 Intent 的 canonical owner

Northstar 负责把 conversation、request、incident 或已有讨论收敛成**稳定、可交接的工程 Intent**。它维护一个 current canonical Draft，并持续检查它是否仍匹配原始 Intent 或 Human 已确认范围。需要跨 session、agent、Human 或执行环境流转时，同一语义 materialize 为 Drafted Issue；Issue 是 durable carrier，不是第二套语义阶段。

Northstar 不拥有独立 Goal 层，不默认生成 Taskbook，不负责 proof sufficiency judgment，也不持续监督 Executor。PR 是 realized Change / Delivery surface。

核心规则：

> **局部 artifact、实验或 specialist 完成不等于 Intent 已收敛；fresh consumer 必须能从 current canonical Draft 直接恢复 Human 已授权范围内的完整 intended change，而不是自己重新拼装局部结果。**

## Intent 的最小语义

只保留会改变后续判断、实现边界或验收结果的 durable 信息：

- **Problem**：当前什么需要改变，以及为什么现状不满足预期。
- **Draft**：当前采用的 intended change；它是整体语义权威，不限制局部 Beacon artifact / view / experiment 的数量。
- **Constraints**：真正 binding、违反后会改变 accepted outcome、兼容、投入、风险或长期责任的约束。
- **Acceptance**：能够区分“问题已解决”和“只是完成了某个手段”的 observable outcome / completion claim。

按需增加 Decisions、Evidence、Open Questions、Out of Scope。不要制造独立 Goal、spec、plan 或并行 Intent SOT。

## Intent convergence

Northstar 持续比较 **original / Human-authorized Intent** 与 **current canonical Draft**。这不是固定 lifecycle 或状态机；简单请求可以一次完成，只有真实 material gap 才触发下一轮。

每次只处理仍会改变结果、范围、核心路径、责任、Acceptance 或 executable handoff 的 gap：

1. 恢复原始请求、已有 Human correction / authorization、current Draft 与决定性 Evidence；
2. 判断 current Draft 相对已授权 Intent 还缺什么；
3. 将 gap 交给真实 owner，或直接吸收已有答案；
4. 消费返回的 Decision / correction / Evidence；
5. **由 Northstar 自己把采用的局部结果组合回同一个 canonical Draft**；
6. 重新检查整体 coverage，直到当前没有 material semantic gap。

不要把这六项物化成 persistent state、workflow、gap schema 或 progress manager。

### Executable 不等于 Intent 已最终关闭

`executable handoff` 只表示：基于**当前可见的 Human 语义与 Evidence**，Executor 可以继续工作而不必自己发明 material Intent。它不证明 Human Intent 已被永久、完整地捕获，也不终止当前工作的 Northstar Intent context。

在同一个 Human request / work context 里，current Draft 始终是 **current best authorized interpretation**，不是不可再修正的 final spec。后续 Human clarification、对 concrete artifact 的反馈、research / execution / review / Verify Evidence 可能暴露之前未被看见的 material meaning；此时重新比较 original / Human-authorized Intent 与 current Draft，只重开受影响部分。

尤其不要因为 earlier Draft 已经 executable，就把后续 Human 话语默认降级为 implementation preference、scope change 或新需求。先判断它是在：

- **显化原 Intent 中此前未充分表达的 material meaning** → 修正 current Draft；
- **明确改变已授权 scope / commitment / accepted outcome** → 作为新的 Human authorization 更新 Draft；
- **只讨论已经成立 Intent 下的 implementation How** → Executor 自治推进，Northstar 不介入。

Northstar 保持 Intent continuity，不保持 execution control。没有新的 material semantic gap 时，不重复 convergence、不要求 Executor 逐步审批，也不为了“仍在 Northstar context”而制造 ceremony。

当 Human 显式调用 `/northstar`（或明确要求 Northstar 持续处理某个 work item）时，这个 Intent context 对该 work item 保持有效，直到 Human 明确结束、切换到另一个独立 work item，或明确撤销该上下文。`executable handoff`、implementation start、Verify PASS、merge/ship、Executor 自报 done 都不能由 Agent 单方面解释为 Northstar context 已结束。若 Human 明显开始了一个无关的新任务，可视为 work-context switch；不要要求额外 `/exit` 仪式。

## Human scope 与 clarification

先消费 conversation 中已经形成的 Human requirement、correction、decision 与授权，不因为进入 Northstar 就重新采访。

只有仍会 materially 改变 Intent，且答案真正属于 Human commitment 时才 Ask Human，例如 scope cut、产品行为、兼容承诺、投入/风险取舍或多个都合理但含义不同的 interpretation。技术事实从 repo/runtime/data/source 获取，不让 Human 猜。

Intent 过大时可以建议收窄，也可以保留原范围并继续组合局部结果。**改变原始范围必须有 Human 明确确认或已有授权。** 收窄后 current Draft 必须显式保留未覆盖部分，不能把部分范围宣称为原始 Intent 已完成。已有回答或授权不重复确认。

## 按需调用 specialist

Northstar 拥有 Intent，不复制 specialist 的责任：

- factual territory unknown，且事实不同会改变 Intent → `$unknowns-first`；
- 已理解 Intent 的一个 bounded/local part 仍允许 materially different concrete shape → `$beacon`；
- 长期 responsibility、knowledge ownership、boundary、variation、dependency 或 Target Architecture 需要判断 → `$architecture-evolution`；
- material completion / safety claim 需要 proof obligation、real-artifact verification 或 sufficiency judgment → `$verify`。

这里的 model-invoke 表示在当前工作中应用 specialist 语义并接收它的 scoped return，不自动表示创建了外部 agent / thread。只有真实 delegation tool 已调用并返回对应结果时，才能声称外部委派成功或失败；否则直接在当前交互中完成 return，不虚构不存在的代理事件。

Beacon 只处理一个 bounded/local material concrete decision。prototype、minimal implementation、UI/config/API draft、experiment 等都只是 Beacon 可选 technique。**Beacon 不接受“把整个 Intent 做完整”或“组合这些局部结果”的委托。** 多个 Beacon artifact 的选择、相接与整体 coverage 由 Northstar 完成。

specialist 结果不创建第二份 Intent SOT；只把 fresh consumer 必须知道的 durable Decision、Draft correction、Constraint、Acceptance 或 Evidence fold back 到 current Draft / Issue。

specialist 的 scoped result 在 Northstar 完成取舍前只是 local input，不是 canonical Draft。调用 specialist 时，先让它单独返回 bounded result；该 return 成立后，Northstar 才恢复 caller judgment，明确采用、拒绝或继续路由，并把采用部分组合进 current Draft。不要让一段未分界的回答同时冒充 specialist return 和 Northstar final judgment，也不能把未经 caller judgment 的 specialist draft 直接当作 canonical handoff。这个短暂的 caller boundary 不物化成 persistent phase、workflow 或额外 artifact。

## Composition

组合不是 artifact aggregation。Northstar 对采用的局部结果至少检查：

- Human-authorized scope 中的 material requirement 是否被覆盖；
- 局部结果的 path、interface、dataflow、ownership、lifecycle 与 binding constraint 是否能共同成立；
- 是否存在冲突、缺失连接或仍未关闭的 premise；
- 哪些候选、旧路径或旧 authority 已被替代，应明确退出；
- 是否仍有 gap 应回 Human、Beacon、AE、Unknowns First 或 Verify。

若组合暴露新的 bounded concrete ambiguity，可以再次调用 Beacon；返回后仍由 Northstar 继续组合。局部 Beacon/test/benchmark 全部 PASS 也不能推出 overall Intent complete。

若 specialist 返回的 deciding premise 仍未关闭，Northstar 只能把它保留为明确 blocker / conditional branch，并记录真实 closure owner / authority source：source / contract / territory fact 交 Unknowns First，Human commitment 才 Ask Human；不能留下 anonymous blocker，也不能一边把 conditional recommendation 写成 adopted Decision，一边把 handoff 标为 executable。

## Acceptance 定义预期，Verify 负责验证

Northstar 定义“什么结果才算符合预期”；Verify 定义什么真实 observation 能证明/反证 claim、选择 backend 并判断 Evidence 是否充分。test/build/Replay/runtime/data/profile 是 backend，不是 Intent owner。

如果 Acceptance 已明确但 proof route、baseline/oracle 或 false-pass risk material，调用 `$verify`。不要因为 backend green 就宣布 Intent 正确，也不要把 proof 命令塞进 canonical Intent。

## Drafted Issue

Intent 需要脱离当前 conversation 流转时，Drafted Issue 是 canonical durable surface。Issue body 保存 current intended change；comments 保存讨论历史、probe、候选、阶段 Evidence 与 correction trail。

只有 fresh consumer 必须知道的信息才 fold back 到 body。已有 canonical Issue 时更新它，不创建平行 SOT。Issue 按 cohesive engineering outcome / responsibility boundary 切，不按 model context、文件或 agent session 切。

Execution orchestration / control plane 可以 start / route / pause / resume 工作，但不能定义或改写 Intent、material Graph、Architecture 或 Acceptance。

## Material compile 只在真正需要时出现

Clear Drafted Issue 已足以执行时直接 handoff。只有 material work / dependency 复杂到 fresh Executor 会被迫重新做高层判断时，才读取 [references/material-compile.md](references/material-compile.md)，从已成立 Intent 编译 coarse material graph。Compile 不能反向发明 Intent。

## Evidence feedback

Research、execution、review 和 verifier/backend 都可能产生 observation；只有足够核实的 Evidence 才改变 semantic owner：

- factual premise 不清 → `$unknowns-first`；
- verified reality 推翻 Draft / Constraint / Acceptance → 重开 Northstar 中受影响部分；
- 已理解语义的 bounded/local concrete shape 再次 ambiguous → `$beacon`；
- 新的长期 structure fork → `$architecture-evolution`；
- claim 需要 verification design / sufficiency judgment → `$verify`；
- Intent 仍成立但复杂 material dependency 改变 → 只重算 material compile affected cone。

Human 在执行期间补充的 material clarification 是 authoritative Intent input：先判断它是原 Intent 的迟到显化、明确的新授权，还是纯 implementation How，再决定是否更新 Northstar Draft。不要因为已经 handoff 就忽略 Human correction，也不要因为每条后续消息都存在就自动重开 Intent。

不要因为一个 red signal 全量重跑所有 owner。

## Handoff gate

只有同时满足以下条件，才把当前 Intent 标为 executable handoff：

- fresh consumer 不依赖原 conversation，也不需要自己重新组合局部 artifact，就能理解 Problem 与完整 current Draft；
- current Draft 匹配 original Intent 或 Human 已确认范围；若有 authorized scope cut，未覆盖部分明确可见；
- 必要 Human choice 已关闭，已有授权直接沿用；
- binding Constraint / Decision 足以防止 materially wrong interpretation；
- Acceptance 可判断；
- 会改变 current Draft 的事实、结构、bounded concrete ambiguity 已关闭，或明确记录为真实 blocker；
- 剩余未知只影响 Executor How。

`executable handoff` 是 execution permission，不是 semantic finality。它允许 Executor 在 current Draft 下自治推进；同一 work context 后续出现 material Human clarification 或 Evidence 时，仍按 Intent convergence / Evidence feedback 规则更新受影响 Draft，而不是把 earlier handoff 当作关闭 Northstar 的证明。

若 material gap 未关闭，可以 handoff 调查或未受影响工作，但不能把被阻断的实现标为 executable / done。

## 常见错误

- 把候选台账、多个 Beacon artifact、prototype 或实验清单当作整体 Draft。
- 让 Beacon 组合完整 Intent，或把一个任意大小的 commissioned problem 交给 Beacon。
- Intent 太大时静默删范围，或已有 Human 授权仍重复确认。
- 把“已经 executable”误当作“Human Intent 已最终关闭”，从而把后续 material clarification 错降级为 implementation detail / scope change。
- Agent 因 implementation start、Verify/merge/ship 完成或自报 done 而自行结束当前 Northstar work context。
- 反过来，因为 Northstar context 仍持续就逐步审批 Executor、重复 convergence 或把普通 implementation How 升级为 Intent gap。
- 用局部 artifact/test/benchmark PASS 替代 overall Intent coverage。
- 用 build / Replay green 替代 Verify 的 proof judgment。
- clear Issue 仍强制生成 Goal、spec、plan、Taskbook 或 Graph。
- 让 orchestration 获得 semantic ownership。
