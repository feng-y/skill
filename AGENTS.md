# Skill Repo Evolution Discipline

本文件约束**如何修改这个 skill repo 本身**，不是任何单个 Skill 的 runtime 语义。修改 Northstar、Beacon、Architecture Evolution、Verify、Eval、Unknowns First 或其他 Skill 前先遵守这里。

总原则：**优先语义压缩，不做规则堆积。先增强、归位或简化既有模型；只有 Evidence 证明存在独立且稳定的责任，并且存在独立 invocation reason，才新增持久 Skill surface。**

## Structure and complexity

- **Existing semantics first.** 先判断缺口是否已经属于现有 Intent / Beacon / Architecture / engineering Verification / agent behavioral Eval / factual unknown 语义。能通过修正、压缩或增强既有 owner 解决，就不要新增 layer、phase、state、role、contract、schema、workflow、protocol 或 taxonomy。
- **Evidence before materialization.** Observation、distinction、partition、role、variation、provider、execution shape、case difference 默认只是 reasoning/evidence。只有它对应稳定 semantic、invariant、ownership 或长期 change boundary，并且独立调用有价值时，才考虑物化。
- **New structure must remove something.** 新 abstraction / layer / protocol 必须让重复知识、分支、依赖、责任泄漏、旧路径或旧结构真实退出。若只是 `old A → new layer → old B`，默认是 complexity relocation。
- **Protocol complexity needs reality.** 复杂协议必须由真实跨边界不确定性、独立生命周期、失败语义或稳定多实现需求证明；普通单 owner / 同步协作不因“解耦”自动升级成协议。
- **Runtime and eval stay separate.** runtime 只保留正常运行需要的 stable invariant / authority / boundary；具体 incident/counterexample 留在 eval；behavioral claim 必须由真实 eval 支撑。不要因 regression 增加而同步扩大 runtime context。

## Semantic migration history

删除、重命名或合并顶层 Skill，迁移稳定 responsibility，或有意退役稳定 concept / artifact / flow，属于 **breaking semantic migration**。这类变更必须在同一个 change 中更新 `CHANGELOG.md`，至少记录：

- old surface / responsibility；
- new owner，或明确标记 `retired`；
- 仍需保留的 invariant / behavior；
- 有意不再保留的 semantics；
- 对应 PR / change identity。

`CHANGELOG.md` 是历史 migration ledger，不是 runtime contract；当前真值仍以本文件、各 `SKILL.md` 和 focused eval 为准。不要因为历史文件里曾存在某个 concept 就恢复它；retired semantics 重新进入 runtime 仍必须满足当前 Evidence + independent invocation reason。

## One semantic owner per skill

当前 canonical capability map：

- **`northstar`**：conversation / request / incident → canonical engineering Intent；把 Intent 收敛到 `execution-ready` 不会制造 Human execution authorization，已有明确授权也不重复确认。对 material、跨 session / agent / execution-environment 的 work，Northstar 将 current Draft 与 material execution contract 落盘为一个 canonical **Taskbook**，持续维护 material task / status / next owner，并在执行结果返回后判断它是否满足 Intent / Acceptance。Northstar 不执行 implementation，也不判断 proof sufficiency；后者仍属于 Verify。Drafted Issue 可以作为 tracker / 外部 carrier，但不能与 Taskbook 形成平行 Intent SOT。
- **`beacon`**：基于真实 repo，为一个 bounded 功能 Intent 或故障构建最小、可检查的核心原型。接口与调用草图、代表性输入输出、最小实现或故障复现都可表达这个核心，不要求可执行代码；问题与 Evidence 服务于原型。它是 **caller-neutral、主要由 model 按需调用的 specialist**；原 caller 保留选择、比较、组合及 Intent / Architecture / Verification judgment。
- **`architecture-evolution`**：拥有长期 Target Architecture judgment + Current → Target Evolution Program。两层 judgment 必须分开，但不拆成两个顶层 Skill。
- **`verify`**：拥有 engineering verification；从 authoritative claim 推导 proof obligation，选择并驱动 real-artifact verifier/backend，收集 Evidence 并判断 proven / false / unproven。
- **`eval`**：拥有 agent behavioral evaluation engineering；从真实 agent surface、repo 与可用 traces 中选择 material capability/failure，构建 Task + Environment + Verifier，驱动或消费 eval backend，检查 agent/verifier trajectories 并形成可重复 measurement。它不验证产品/工程 claim，也不把 Harbor 等 backend 变成 semantic owner。
- **`unknowns-first`**：只拥有 map-versus-territory 的**事实未知关闭**；它可以做 probe / source alignment，但不替其他 owner 关闭 Intent、concrete shape、Architecture、engineering verification 或 agent behavioral eval judgment。

不要复制 owner：Northstar 不判 proof sufficiency；Verify 不重写 Intent、设计 Target 或承担 agent behavioral eval；Eval 不验证产品 outcome 或改写 engineering semantics；Beacon 不接管 caller 的 semantic ownership；AE 不用 Program convenience 反推 Intent；Unknowns First 不把 factual probe 扩成 intent interview、concrete shaping、architecture design、proof judgment 或 eval design。

**Beacon routing rule:** Northstar、AE、Verify、Unknowns First 或其他 caller 在一个局部功能或故障需要核心原型、或已有原型需要局部修订时，可 model-invoke `$beacon`。不必先制造多个候选或查清全部故障根因。Beacon 返回一个基于 repo 的核心原型及必要 Evidence / correction；原 caller 继续判断，Northstar 负责完整 Intent 的组合与编译。不要把 Beacon 做成 Human 必经入口或固定阶段。

`prototype` 不再是顶层 Skill identity 或 runtime route；Beacon 的主体是核心原型，可执行 prototype/mock/minimal implementation 只是表达它的方式，不恢复 `$prototype`。

`Goal` 不属于稳定跨 Skill semantic model。若一个抽象 outcome 真的增加 decision information，把它落到 Problem、Draft、Constraint、Decision 或 Acceptance；不要维护独立 Goal artifact / field / lifecycle。

## Verifier / eval / control-plane boundary

**Verify 是 capability，不是 lifecycle stage。** 可以在实现前收敛 proof obligation、实现中修正 proof premise、实现后判断 realized result；不得强制每个 Issue / PR 都经过 Verify。

**Verification backend 是执行系统，不是 semantic owner。** test/build/integration、project-local verify harness、runtime probe、data query、profile，以及 DaVinci harness 的 Replay 都可以产出 observation / artifact；Verify 决定为什么运行、identity 是否可信、这些结果证明哪个 claim、是否达到 proof 门槛。已有 backend 的 Launch / Doctor / Drive / Capture / Cleanup contract 由 backend 自己拥有，Verify 只消费，不重建第二套 lifecycle。

**Eval 是 Agent behavior measurement capability，不是产品 Verify，也不是 mandatory CI stage。** 它负责从 agent surface / traces 设计和审计 Task + Environment + Verifier，运行后检查完整 trajectory 与 verifier Evidence，并区分 measurement defect 与 candidate behavior defect。Skill/prompt/tool/harness 的 behavior claim 交 Eval；产品功能、迁移、性能、结构 completion claim 仍交 Verify。

**Eval backend 也是执行系统，不是 semantic owner。** Harbor、clean-session runner、trajectory recorder、project-local evaluator 或 containerized task runner 可以执行 Eval artifact；Eval 决定要测什么、Environment 是否 representative、Verifier 是否 hard-to-game、结果是否足够可信。不要因为某个 eval framework 可用就新增同名 Skill 或把 framework format 变成跨项目 semantic contract。

**Execution authorization 与 control plane 都正交。** `execution-ready` 只表示实现者无需发明 material Intent；是否实施、commit、建 PR、merge、ship 或 rollout 取决于 Human 已表达的对应对象与动作范围。已有授权直接沿用，缺失授权不能由 readiness、compile、handoff 或外部 orchestration 制造。外部 orchestration 可以 start / route / pause / resume / retry，但不能定义 Intent、material Graph、Architecture、Verify/Eval semantics 或 artifact authority。

不要为了某个现有 backend 新增同名 Skill。执行能力和 semantic responsibility 分开演进。

## Artifact ownership

- **Taskbook**：Northstar 对 material / cross-session work 的 canonical durable artifact；保存 current Draft、binding Decision / Constraint / Acceptance、material tasks / status、决定性 Evidence pointer、last Northstar judgment 与 next owner。它不是第二份 plan，而是 current Intent 的持久化 work surface。
- **Feedback Log**：material work 的 append-only execution-learning sidecar；由 Northstar 在 material return judgment 后按需记录 worker return / decisive Evidence pointer、Taskbook 的 material delta、当次 judgment，以及值得后续复用的判断失误、surprise 或有效模式。它不是 current Intent / task state / Evidence sufficiency 的 authority，不参与 dispatch、resume 或 acceptance；后续 Skill 改进可把它当作 trace-like input，但 behavior claim 仍必须进入 Eval。
- **Session handoff**：只保存从 canonical Taskbook 恢复所需的 session delta：Taskbook pointer、last completed/current task、仍 live 的 blocker/decision、next task / owner、需要返回 Northstar 的 judgment point。不得复制 Taskbook 的架构、方案、验收全文；需要重述的 durable 内容应回写 Taskbook。
- **Drafted Issue**：tracker / 外部协作 carrier。material / cross-session work 的 canonical state 始终在 Taskbook；Issue 只指向它并保留讨论历史 / 外部协作信息，禁止复制一份可独立漂移的方案。
- **PR**：realized Change / Delivery；implementation How、diff、implementation-local validation 与 review 默认留在 PR。
- **Beacon artifact**：基于 repo 的 bounded 核心原型，通常可丢弃；原型及必要 correction / Evidence 返回原 caller，由 caller 决定采用、组合与 durable fold back。
- **Architecture handoff**：只有独立调用或真实跨边界需要时持久化；被 Northstar 调用时先返回 scoped result，由 Northstar 采纳后 fold durable structural decision 回 current Draft；material / cross-session work 回写 canonical Taskbook，Issue 只引用它。
- **Verify result**：Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing；默认留在 PR / review / verification surface，不成为第二份 Intent SOT。
- **Eval artifact**：Capability/failure + Task + Environment + Verifier + backend binding + Run Evidence/Trajectory + measurement status；默认进入 `evals/` 或项目已有 eval surface，不成为 canonical Intent、产品 verification SOT 或 implementation plan。

## Graph and loop

- **Work is a graph.** Material engineering work 按 cohesive outcome 与真实 dependency 判断，而不是 prose list。简单/线性工作只是 Graph 的退化形式；不为了“使用 Graph”新增 Graph object/schema、node taxonomy、persistent state、scheduler 或 manager protocol。
- **Compile only what execution needs.** Clear Draft 可以直接达到 execution-ready；material / cross-session work 把它持久化进 canonical Taskbook。只有 fresh implementer / worker 会因缺失 task boundary 或 dependency 而重新做高层判断时，Northstar 才展开 material task / dependency compile；简单线性工作保持 compact Taskbook，不强制 Graph。已有 scoped Human execution authorization 时可以直接选择并 handoff next material execution task / owner，没有时停在 Draft / Taskbook；真正的 start / pause / resume / retry 仍属于 execution system，compile 不制造授权，也不等同于 session handoff。
- **Progress through a loop.** Research、execution、review、Verify 都可能产生 new verified Evidence。只有它真正改变 material work、dependency、Intent premise 或 architecture premise 时，才重开对应 owner / affected dependency cone；无关 branch、仍有效 work 与 Evidence 保持有效。
- **Proof scales with claim.** 普通 implementation-local focused test 可以直接成为 Evidence；behavior-preservation、replacement、cross-boundary Acceptance、false-pass risk、perf 或 merge/ship gate 需要更强、更直接或更独立的 proof。Execution node 不与 verification claim 一一对应。
- **Agent learning uses Eval, not product proof.** Skill/prompt/tool/harness change 若声称改善 agent behavior，必须通过可重复 behavioral eval；Replay/test green 只能证明对应产品/工程 claim，不能证明 agent 行为变好。Eval 发现稳定 behavior gap 后才驱动 runtime semantics / harness 改进，并使用同一 measurement 重跑。

## Feedback routing

任何 research / execution / review / verification finding 都按 semantic owner 回流：

- factual map-versus-territory gap → Unknowns First；
- Intent premise / Constraint / Acceptance 被推翻 → Northstar；
- 一个 bounded 功能 Intent 或故障需要核心原型，或已有原型的局部表达需要修订 → Beacon，结果返回当前 caller；
- 新的长期 responsibility / boundary / dependency fork → Architecture Evolution；
- 当前 contract 的 material completion / safety claim 需要定义、补足或判断 proof → Verify；
- Skill / prompt / tool / harness 的 agent behavior claim 需要构建、审计或解释可重复 measurement → Eval；
- 复杂 material graph 的 work/dependency 被 verified Evidence 改变、但 Intent 仍成立 → Northstar material compile 只重算 affected cone。

Feedback Log 只保存已经发生的 return → judgment → Taskbook delta 与可复用观察，不创建新的 semantic owner，也不替代当前 work 的正常 feedback routing。若某条反馈说明 current Intent / task state 需要修正，先按上述 owner 更新 canonical Taskbook；若它被用于改进 Skill，则把它当作 observation / trace input，而不是直接把单条经验写成 runtime rule。

Eval result 是对 agent behavior 的 measurement，不直接改写产品 Intent / Architecture / factual reality；只有 measurement 暴露对应 owner 的稳定 contract gap 时，才修改那个 runtime owner。

不要因为一个 red signal 全量重跑所有 Skill，也不要在 owner 之间来回 ping-pong：specialist 回答 bounded question 后返回 caller，只有 premise 真正变化才 re-enter owner。

## Context engineering and judgment quality

- **Context improves judgment; it does not replace judgment.** 暴露 Intent、reality、invariant、authority、decisive Evidence；不要在模型可以自行判断时编码固定 reasoning path 或答案。
- **Load only decision-relevant context.** Always-on context 必须能改变当前 judgment。背景、历史、示例优先 routing/reference，按需 progressive disclosure。
- **Encode discriminators, not remembered answers.** 描述让两个 case 真正不同的 discriminator / invariant，而不是记住某个 case 的结论。
- **Prefer territory over duplicated descriptions.** 默认事实优先级：`current code / test / config / runtime Evidence > stable repo contract > authoritative current docs > historical explanation > case narrative`。
- **Examples do not become runtime priors.** incident / captured output / regression 用于 eval；runtime 只保留有 authority 或跨 case Evidence 支持的 general invariant。

## Review gate

修改 `AGENTS.md`、`CLAUDE.md`、`SKILL.md` 或 runtime references 时，至少回答：

1. 新增 context / structure 支持哪个具体 judgment 或责任？
2. 已有 semantic owner 为什么不能拥有它？
3. 它是否有 independent invocation reason，而不只是内部 reasoning step？
4. 它有 independent authority / cross-case Evidence，还是一次 case 的答案？
5. 它加入后什么旧规则、知识、结构或复杂度会退出？
6. 它能否下沉到按需 reference 或 eval，而不是进入 always-on runtime？
7. 如果这是 breaking semantic migration，`CHANGELOG.md` 是否明确记录 old surface → new owner / retired reason？
8. 如果新增的是 verifier / eval / harness / control-plane capability，为什么它不是 backend，而必须成为 semantic Skill？

答不出基于 Evidence 的理由，默认不新增。

## Placement

- Repo-wide evolution / context rules：只放这里。
- Skill runtime invariant：放对应 `SKILL.md` 或按需 runtime reference。
- Breaking semantic migration history：放 `CHANGELOG.md`，不复制到 runtime Skill。
- Case / incident / counterexample：用于修改本 Skill system 的稳定 case 仍放 `evals/`；正常产品/工程 semantic runtime 禁止读取。项目执行过程中产生的 Feedback Log 是 raw work observation，不是 eval case；只有需要形成可重复 behavioral measurement 时，才由 `$eval` 消费相关条目 / trace 并把判别性 case 放入 `evals/`。
- `CLAUDE.md` 只作为薄入口指向本文件，不复制规则。
