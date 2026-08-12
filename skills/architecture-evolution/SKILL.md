---
name: architecture-evolution
description: 用于架构方向模糊、历史模块持续演进或“下一刀应该改什么”这类输入：从指定模块的真实 repo reality 重新识别 capability/boundary，收敛 Target Architecture，并写成少量真实改善结构的 Architecture Improvements。
---

# Architecture Evolution · 从模块现实收敛目标架构

三个角色：**Human** 提供 change pressure，并拍板业务、兼容、风险和长期承诺；**Architecture Evolution** 调研 reality、做 architecture judgment 并写 Architecture Program；**Implementation agent** 决定 class/API/file、调用形状、迁移 patch 与验证实现。repo reality / authoritative SOT 是事实与约束 authority，不由当前 module/provider taxonomy 或 AE 的方案代替。

- **Target Architecture**：当前 Evidence 支持的 best-known 长期 layer/dependency、capability/responsibility、abstraction/specific 与必要 authority/lifecycle placement。
- **Architecture Improvement**：完成后能独立改善当前结构，并让旧 knowledge、authority、dependency 或 path 真实退出的 bounded structural change。
- **Architecture Program**：把 current → target 的 architecture judgment 压成少量 Improvements 与真实依赖；它不是 Implementation Plan，也不规定固定 Markdown 模板。

## 流程

**1. 调研。** 从 Human 指定的模块或 capability 与当前 pressure 开始，先看真实 responsibility、直接 upstream/downstream，以及 consumer 当前必须知道什么，再重新识别 capability、boundary 与 stable variation。现有 module/class/provider/family 只作 Evidence；只有长期 semantic、contract、lifecycle、performance 或 deployment difference 才能证明 stable specific variation。只有局部无法关闭、且会改变 architecture judgment 的 authority/SOT/identity/external constraint 才 targeted 扩大搜索；继续 Research 只会改变 implementation How 时就停。

**2. 判断。** 先判断 pressure 是否真的需要 architecture evolution，再收敛 best-known Target Architecture。不要停在第一个 plausible shape，也不要制造假 alternatives；只有长期 layer/module/abstraction/responsibility placement materially different 时才值得比较。repo/runtime 能关闭的 decisive facts 先查；真正 Human-owned 的业务、兼容、风险或长期承诺才交给 Human。若由 Northstar 等上游 task-shaping capability 调用，返回 Evidence、options 与 Human-owned decision surface，由 caller 保持 Human decision ownership，不另开串行 Ask。architecture/local、stable variation、real fork 或 altitude 难判时读 [rules.md](references/rules.md)；legacy identity 会改变 retirement 时读 [legacy-lenses.md](references/legacy-lenses.md)；proposal 局部都合理但整体开始膨胀时按需读 [brooks-constraints.md](references/brooks-constraints.md)。

**3. 写 Program。** Target Architecture 足够稳定后，写当前完整 Architecture Program。只保留：
- **Target delta**：current → target 的关键 layer/dependency、capability/responsibility、abstraction/specific 变化；
- **Long-lived invariants**：后续演进仍应保持的少量 architecture boundary；
- **Top Improvements**：最多 3 个，不补数，按 structural leverage 排序；每个都说明 structural change、architecture gain、real exit 与 structural done condition，并在完成时独立让当前结构变好；
- **Route / completion**：只表达 Improvements 之间真实的 architecture dependency，以及整体完成后哪些旧结构不再 authoritative。

research/knowledge task、future wish、纯铺路 abstraction/bridge 或 implementation step 不能冒充 Improvement。已有 authoritative repo SOT 直接引用；本轮只写新增 architecture judgment / structural delta。若旧 SOT 本身要演进，指向原 authoritative source 应发生的 delta，不建立平行规范。

**4. 交付。** 如果 pressure 本质是 local，完整说明 local judgment 与理由；如果 architecture choice 仍缺 decisive Evidence/Human decision，完整指出缺口和继续条件；如果已收敛，完整返回当前 Architecture Program，并把**同一份完整正文**写入 OS/runtime 提供、位于 repo/workspace 外的 handoff-authoritative Markdown file，显示实际 path。这个 artifact 只负责下游 handoff，不替代 repo 内既有 architecture SOT；Implementation agent 从当前 artifact 继续，不从 conversation 重建 Program。

Program 交付不是 completion state。Human 后续任何 material clarification/correction 都重新进入最高受影响判断，复用仍有效部分，重算受影响 dependency，并再次完整交付当前 Program；能更新当前 artifact 就更新，不能写时生成新的 artifact 并显示新的 current path。若 artifact 无法 materialize，说明 blocker 与恢复条件，不能把 chat 或“稍后写入”当成已完成 handoff。不要输出 ready / completed / executable / status token。

## 架构判断

**Architecture outcome 高于 proposed shape。** Human 点名 provider、facade、layer、registry、migration shape 等默认只是 candidate means。只有 Human/repo authority 或不可替代技术约束使 representation 本身成为长期 invariant 时才固定；否则保留它背后的 responsibility、boundary、dependency 与 exit outcome。

**Architecture vs local。** 文件大、目录乱、switch 多、重复代码或一次局部修改都不足以证明 architecture work。只有 pressure 真正要求改变长期 layer/dependency、module responsibility、abstraction boundary、primary responsibility 或旧结构退出，才升级为 architecture evolution。

**Layering & dependency。** 保持少量清晰层与稳定单向依赖；common/policy 不知道 specific provider/scenario。Layer 对应稳定 responsibility + dependency boundary；值得长期约束的方向优先能从 repo territory / build / tooling 直接看见。

**Cohesion & simplicity。** 模块围绕主要 capability/responsibility 组织，闭合完成责任所需的内部 knowledge/state/lifecycle，caller 不重新拼装 capability 私有事实。相邻 subsystem 已有 authoritative owner 时保持清晰 relation/contract；两个结构都正确时选概念更少、public surface 更小、repo 更容易解释和修改的方案。

**Abstraction vs specific。** 抽象稳定 semantics/invariant，不抽象表面相似。代码相似、当前 provider/class/consumer partition 或为了扩展性预留接口都不能证明 abstraction；没有 stable variation 不制造 provider，有真实长期差异也不为表面统一强行消除。

**Primary vs auxiliary。** primary responsibility 决定主要 boundary 与组织；auxiliary concern 附着在主结构上，不反向塑造它。未经 profiling/SLA/resource Evidence 证明的性能收益不能打穿 layering、cohesion 或 abstraction boundary。

**Real evolution。** 新 abstraction 出现不等于 evolution；旧 knowledge、authority、reverse dependency、special path 或 compatibility 必须真实退出或停止 authoritative。`old A → new abstraction → old B` 只是 complexity relocation。temporary adapter/dual path 只有明确 architecture purpose 与 exit 时成立；没有当前长期 Evidence 的 future hook/mode/registry/framework 不物化。

**法、Evidence 与 SOT 分开。** 只有 Human、repo/upstream authority 或 verified reality 能把内容绑定成长期 architecture invariant。当前 taxonomy、Research 结论和高置信方案仍是 intelligence；缺 decisive Evidence 时保持 unresolved，不把模式偏好写成 law。已有 authoritative spec/schema/contract 直接引用，不复制第二份 prose SOT。

**保持 architecture altitude。** AE 可以固定长期 layer/dependency、capability/module responsibility、abstraction/specific、必要 authority/SOT/control/lifecycle direction、essential variation 与 structural done condition；除非 representation 本身是 authoritative invariant，否则不固定 class/API/file/helper/schema/call implementation/MR/task/test provider。Implementation Design 从 Architecture Program 之后开始。

## 发出前自检

1. 这真的是 architecture pressure，还是 local cleanup？Target Architecture 是否来自真实 responsibility / dependency / variation，而不是当前 taxonomy 或 proposed shape？
2. layering、cohesion、abstraction/specific、primary responsibility 与 real exit 是否一致？有没有 `old → new layer → old` 或无 Evidence 的 speculative flexibility？
3. 每个 Improvement 完成后是否独立产生 structural gain + real exit？research/setup/future/implementation step 有没有混进来？是否真的不超过 3 个？
4. 长期 invariant 是否有 authority/Evidence？已有 SOT 是否只引用或指向原 source delta？有没有越过 architecture altitude？
5. 若已收敛，是否完整交付同一 Program 并 materialize 当前 handoff artifact？Human 新输入后是否重新完整交付，而不是只回复 delta？
