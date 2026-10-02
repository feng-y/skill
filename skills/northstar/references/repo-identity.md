# Intent-conditioned Repo Identity

只在 Northstar 承接**宽泛、repo-grounded 的 improvement / refactor / capability Intent**，且第一个局部 finding 很容易被误当成整体 target 时读取。

这个 reference 不创建新的 Repo Identity Skill、workflow、schema、knowledge graph 或持久数据库。Northstar 仍拥有 Intent；Unknowns First 仍关闭事实未知；Architecture Evolution 仍判断长期 responsibility / boundary / dependency；Verify 仍判断 proof sufficiency。Repo Identity 在这里是一份**按当前 Intent 临时编译的 repo understanding**。

核心规则：

> **先理解当前 repo 以什么稳定身份承载这个 Intent，再形成 target；不要让第一个容易证明的局部问题替代原始目标。**

## Identity slice

只收集会改变 target 的 repo identity，不做全量 inventory：

- **Stable concept / term**：repo 已经反复使用、且会影响理解或 handoff 的稳定概念与 canonical term。
- **Responsibility / authority**：谁拥有哪个决定、状态、knowledge 或长期责任；哪些 caller 只是 consumer。
- **Boundary / contract**：跨责任边界必须保持的行为、数据、兼容、缺席语义、生命周期或 authority 约束。
- **Evolution pressure**：当前哪些 change pressure 正在反复作用于这些 responsibility / boundary；只保留会改变 target 的 pressure。
- **Evidence anchor**：支持上述判断的 current code / test / config / repo contract / authoritative docs / history pointer。

事实优先级沿用 repo 规则：current territory 与 stable repo contract 优先于历史解释。未经核实的 narrative、一次 incident、某个 Agent 的推断都不能直接升级为 identity。

## Intent-conditioned projection

从原始 / Human-authorized Intent 出发，而不是从搜索结果出发：

1. **拆出 material dimensions**：哪些 capability、responsibility、boundary、contract 或 change pressure 如果漏掉，会让最终 target 偏离原始 Intent。
2. **映射 current identity**：给每个 material dimension 找到足以支持判断的 concept、owner、boundary 与 Evidence anchor。
3. **关闭 deciding unknown**：事实不清交 Unknowns First；长期 structure fork 交 Architecture Evolution；Human commitment 仍由 Northstar 处理。不要用 repo identity 名义吞掉其他 owner。
4. **检查 coverage**：第一个 local finding 只能作为 Evidence / input。只有当它能解释 material dimensions，或其余 dimensions 已明确不受影响，才可以把它提升为 target。
5. **停止扩图**：新增 repo knowledge 已不能改变 target、scope、responsibility、Acceptance 或 material next action 时停止。不要为了“理解完整 repo”继续 inventory。

这个过程是 reasoning support，不要物化成 persistent phase / state machine。简单、局部、已知 owner 的请求无需读取本 reference。

## Representation selection

同一 identity slice 可以针对 consumer 生成不同 projection。**Representation choice 是 intelligence 的一部分，但 projection 不是 repo truth。**

- Agent / worker 需要继续推理或执行 → 用紧凑的 structured context：concept、responsibility、boundary、contract、Evidence、unknown。
- Human 只需要确认一个局部判断 → concise text / table。
- Human 需要理解结构关系 → diagram。
- Human 需要判断迁移 / completion / evidence 状态 → dashboard 或 status view。
- Human 需要跨多个 responsibility / change pressure 探索 → 可生成一次性的 interactive artifact。
- 只有真正需要连续讲解复杂因果时才考虑 explainer；不要为了形式感默认生成 HTML / video。

Human-facing diagram、dashboard、interactive page 或 explainer 都是当前 identity slice 的**可丢弃 projection**。它们可以帮助理解、审查和决策，但不能成为 canonical Draft / Taskbook、repo contract 或新的长期 SOT。

## Durable fold-back

只把能避免未来重复 rediscovery、且有稳定 authority / cross-case Evidence 的 identity 事实回写到 repo 已有 authoritative surface。一次 Intent 的 projection、临时关系图、局部 evidence summary 默认不持久化。

当本次 work 需要 durable handoff 时，Northstar 只把会影响 intended change 的 responsibility、boundary、contract、Decision 或 Evidence pointer fold 回同一个 canonical Draft / Taskbook；不要再建立一份平行 Repo Identity 文档。

## Quality check

形成 target 前只问四个问题：

1. **Coverage**：原始 Intent 的 material dimensions 是否都已被理解或明确标为 unknown？
2. **Accuracy**：每个 identity claim 是否能回到 current repo / authoritative Evidence？
3. **Consistency**：concept、owner、boundary、contract 是否可以同时成立？
4. **Intent fidelity**：当前 target 是由完整 repo understanding 推出，还是只由第一个 local finding 推出？

任何一项失败，都不能用更详细的 solution prose 补偿；先修正 identity slice 或关闭真正的 deciding unknown。
