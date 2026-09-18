# Material Compile

只在当前 Northstar Intent / canonical Taskbook 已经成立，但 material work / dependency 复杂到 fresh implementer 或真实 transfer consumer **仍会被迫重新做高层判断**时读取。

Compile 的目标不是建立完整 work graph，而是把已成立 Intent 编译成 canonical Taskbook 中**最小充分的 task / dependency contract**：让后续执行者知道必须兑现哪些 cohesive outcomes、哪些真实 dependency 不能打乱，以及哪些 Acceptance / Constraint 必须保持。简单线性 work 只需要 compact task，不为了 planning ceremony 构建 Graph；session handoff 是另一件事，只记录 resume delta。

Compile 不重新定义 Intent，不产生或扩大 Human execution authorization，不设计 implementation How，不拥有 verification judgment。它可以维护 material task status / next owner，供 Northstar 判卷与续接；低层 execution progress / scheduler state 仍属于执行系统。

## 从 Intended delta 出发

先从 canonical Intent 恢复已经成立的 `Current → Intended` material delta。只保留为了让 Draft / Constraint / Acceptance 成立而真正需要兑现的差异，例如 responsibility / authority 归位、核心路径改变、binding boundary 建立、明确要求退出的 legacy path，以及必须保持的 invariant。

不要从文件结构、当前 module、候选 patch 或已有 task list 反推 Intended state；不要把仍会改变 Intent 的 unresolved alternative 编译成 implementation branch。

## 最小 task / dependency handoff

只 materialize fresh implementer 若不知道就会重新做高层判断的 work：

- 一个 task 对应一个 cohesive material outcome / responsibility / binding boundary，不按文件、helper、agent session 或 verifier 拆分；
- 只有 prerequisite、共享 authoritative surface / conflict、或必须共同成立的 outcome 才记录 dependency；
- 文本顺序不形成 dependency，能够独立推进的 work 保持独立；
- 省略某个 task / relation 会迫使 fresh implementer重新恢复 material Intent 时才保留；
- 仍取决于未来 execution Evidence 的 contingent work 不提前创建 placeholder task；
- verification claim 不因为可独立验证就自动成为 execution task。

简单或线性的 material work 不需要 Graph，只在 canonical Taskbook 中保留一个或少量 cohesive task。多个 task 也不自动等于多个 Issue；Taskbook 按一个 engineering Intent 持久化，Issue / external orchestration 只有真实协作边界时才按最小必要范围 materialize。不要为了“完整规划”把探索过程展开成 issue graph。

## Verify boundary

Compile 只携带 Northstar 已定义的 Acceptance / completion claim identity 与 material dependency，不选择具体 test / Replay / runtime command，也不把 verification step 编成 execution phase。

需要 proof obligation、backend selection、Evidence sufficiency 或 verdict 时交 `$verify`。一个 task 完成不代表整体 Acceptance 自动成立；一个 verification claim 也不自动成为 task。

## Evidence feedback

Research、execution、review 或 `$verify` 的 verified Evidence 只有在它使**现有 task / dependency 不再成立**时才修订 Taskbook：

- 新 reality 证明某个已记录 task 不需要或边界错误 → 删除 / 合并 / 修正对应 task；
- prerequisite 或 conflict 改变 → 只修订受影响 dependency；
- 只影响 implementation How → Taskbook 不变；
- Evidence 推翻 Intent / Acceptance → 返回 Northstar；
- Evidence 暴露新的长期 architecture fork → 返回 `$architecture-evolution`。

不要维护“持续演进的完整 Graph”，也不要因为局部 Evidence 变化重算无关 work。

## 交付与停止

默认把必要 task / dependency relation fold 回 canonical Taskbook；Taskbook 与 current Draft 是同一 Northstar work 的 durable surface，不再额外生成一份 session handoff 作为方案副本。需要跨 session 时另写短 handoff，只指向 Taskbook 并记录 resume delta。

当 fresh implementer / worker 已能在 binding boundary 内继续、剩余未知只影响 implementation How 时停止 compile。已有 Human execution authorization 时由 Northstar 选择并 handoff next material task / owner；真正启动执行由宿主 / worker / orchestration 负责。没有授权时 Taskbook 停在 execution-ready。worker 返回 material result / Evidence 后回到 Northstar judgment，再决定是否推进 task state；implementation-local substeps 不逐项回流 Northstar。
