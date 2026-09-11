# Skill Repo Evolution Discipline

本文件约束**如何修改这个 skill repo 本身**，不是任何单个 Skill 的 runtime 语义。修改 Northstar、Prototype、Architecture Evolution、Verify、Unknowns First 或其他 Skill 前先遵守这里。

总原则：**优先语义压缩，不做规则堆积。先增强、归位或简化既有模型；只有 Evidence 证明存在独立且稳定的责任，并且存在独立 invocation reason，才新增持久 Skill surface。**

## Structure and complexity

- **Existing semantics first.** 先判断缺口是否已经属于现有 Intent / Prototype / Architecture / Verification / factual unknown 语义。能通过修正、压缩或增强既有 owner 解决，就不要新增 layer、phase、state、role、contract、schema、workflow、protocol 或 taxonomy。
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

- **`northstar`**：conversation / request / incident → canonical engineering Intent；需要 durable handoff 时 materialize 为 Drafted Issue。Issue 是 Intent carrier，不是独立 Skill。
- **`prototype`**：只拥有 already-understood Intent 的 concrete reaction surface；Core Path / Usage / disposable Prototype 都是手段，不拥有 Intent SOT。
- **`architecture-evolution`**：拥有长期 Target Architecture judgment + Current → Target Evolution Program。两层 judgment 必须分开，但不拆成两个顶层 Skill。
- **`verify`**：拥有 engineering verification；从 authoritative claim 推导 proof obligation，选择并驱动 real-artifact verifier/backend，收集 Evidence 并判断 proven / false / unproven。
- **`unknowns-first`**：只拥有 map-versus-territory 的**事实未知关闭**；它可以做 probe / source alignment，但不替其他 owner 关闭 Intent、concrete shape、Architecture 或 verification judgment。

不要复制 owner：Northstar 不判 proof sufficiency；Verify 不重写 Intent 或设计 Target；Prototype 不决定 Architecture；AE 不用 Program convenience 反推 Intent；Unknowns First 不把 factual probe 扩成 intent interview、prototype、architecture design 或 proof judgment。

`Goal` 不属于稳定跨 Skill semantic model。若一个抽象 outcome 真的增加 decision information，把它落到 Problem、Draft、Constraint、Decision 或 Acceptance；不要维护独立 Goal artifact / field / lifecycle。

## Verifier / control-plane boundary

**Verify 是 capability，不是 lifecycle stage。** 可以在实现前收敛 proof obligation、实现中修正 proof premise、实现后判断 realized result；不得强制每个 Issue / PR 都经过 Verify。

**Backend 是执行系统，不是 semantic owner。** test/build/integration、project-local verify harness、runtime probe、data query、profile，以及 DaVinci harness 的 Replay 都可以产出 observation / artifact；Verify 决定为什么运行、identity 是否可信、这些结果证明哪个 claim、是否达到 proof 门槛。已有 backend 的 Launch / Doctor / Drive / Capture / Cleanup contract 由 backend 自己拥有，Verify 只消费，不重建第二套 lifecycle。

**Execution control plane 也正交。** 外部 orchestration 可以 start / route / pause / resume / retry，但不能定义 Intent、material Graph、Architecture、Verify semantics 或 artifact authority。

不要为了某个现有 backend 新增同名 Skill。执行能力和 semantic responsibility 分开演进。

## Artifact ownership

- **Drafted Issue**：Northstar Intent 的 durable carrier / canonical intended change。
- **PR**：realized Change / Delivery；implementation How、diff、implementation-local validation 与 review 默认留在 PR。
- **Prototype artifact**：reaction surface，可丢弃；durable correction / Evidence 回 caller。
- **Architecture handoff**：只有独立调用或真实跨边界需要时持久化；被 Northstar 调用时优先 fold durable structural decision 回 Issue。
- **Verify result**：Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing；默认留在 PR / review / verification surface，不成为第二份 Intent SOT。

## Graph and loop

- **Work is a graph.** Material engineering work 按 cohesive outcome 与真实 dependency 判断，而不是 prose list。简单/线性工作只是 Graph 的退化形式；不为了“使用 Graph”新增 Graph object/schema、node taxonomy、persistent state、scheduler 或 manager protocol。
- **Compile only when earned.** Clear Drafted Issue 可以直接执行；只有复杂 material dependency 会迫使 fresh Executor 重新做高层判断时，Northstar 才按需 compile coarse material graph / execution contract。
- **Progress through a loop.** Research、execution、review、Verify 都可能产生 new verified Evidence。只有它真正改变 material work、dependency、Intent premise 或 architecture premise 时，才重开对应 owner / affected dependency cone；无关 branch、仍有效 work 与 Evidence 保持有效。
- **Proof scales with claim.** 普通 implementation-local focused test 可以直接成为 Evidence；behavior-preservation、replacement、cross-boundary Acceptance、false-pass risk、perf 或 merge/ship gate 需要更强、更直接或更独立的 proof。Execution node 不与 verification claim 一一对应。

## Feedback routing

任何 research / execution / review / verification finding 都按 semantic owner 回流：

- factual map-versus-territory gap → Unknowns First；
- Intent premise / Constraint / Acceptance 被推翻 → Northstar；
- already-understood Intent 仍出现 materially different concrete shape → Prototype；
- 新的长期 responsibility / boundary / dependency fork → Architecture Evolution；
- 当前 contract 的 material completion / safety claim 需要定义、补足或判断 proof → Verify；
- 复杂 material graph 的 work/dependency 被 verified Evidence 改变、但 Intent 仍成立 → Northstar material compile 只重算 affected cone。

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
8. 如果新增的是 verifier / harness / control-plane capability，为什么它不是 backend，而必须成为 semantic Skill？

答不出基于 Evidence 的理由，默认不新增。

## Placement

- Repo-wide evolution / context rules：只放这里。
- Skill runtime invariant：放对应 `SKILL.md` 或按需 runtime reference。
- Breaking semantic migration history：放 `CHANGELOG.md`，不复制到 runtime Skill。
- Case / incident / counterexample：放 `evals/`，正常 runtime 禁止读取。
- `CLAUDE.md` 只作为薄入口指向本文件，不复制规则。
