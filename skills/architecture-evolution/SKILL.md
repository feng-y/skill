---
name: architecture-evolution
description: 用于架构方向模糊、历史模块持续演进或“下一刀应该改什么”这类输入：从指定模块的真实 repo reality 重新识别 capability/boundary，收敛 Target Architecture，并编译成少量真实改善结构的 Architecture Improvements。
---

# Architecture Evolution · 从模块现实收敛目标架构

AE 不是架构建议生成器。它从一个真实模块及其 change pressure 出发，重新判断 capability、boundary、stable variation 和长期依赖方向，得到 best-known Target Architecture，再把大段 reasoning 压成少量可以持续收敛的结构改进。

三个责任面：**Human** 提供目标压力、业务/兼容/风险等真正需要 Human authority 的约束；**Architecture Evolution** owns bounded research、architecture judgment 与 Architecture Program compile；**Implementation agent** owns class/API/file、具体调用形状、迁移 patch 与验证实现。repo reality / authoritative SOT 是证据与约束 authority，不由当前 module/provider taxonomy 代替。

## Flow

**1. Ground.** 锚定用户指定模块，先看真实 responsibility 与直接 upstream/downstream，再重新识别它实际提供/参与的 capability，重划 capability boundary。现有 module/class/provider/family 只作 evidence；只有 semantics/contract/lifecycle/performance/deployment 等长期差异证明 stable specific variation 时才形成 provider boundary。局部无法关闭且会改变 architecture decision 的 authority/SOT/identity/external constraint，才 targeted 扩大搜索。

**2. Judge.** 用下面的 architecture rules 判断这是不是 architecture work、Target Architecture 应是什么、旧复杂度如何真实退出。不要停在第一个 plausible shape，也不要为了显得全面制造假 alternatives。只有 materially different 的长期 layer/module/abstraction/responsibility placement 才值得比较；缺 decisive evidence 时指出真正缺失的 repo/runtime Evidence 或 Human decision，不按模式偏好强选。需要细化边界时读 [rules.md](references/rules.md)；legacy identity 会改变 retirement 时读 [legacy-lenses.md](references/legacy-lenses.md)；proposal 局部都合理但整体开始膨胀时按需读 [brooks-constraints.md](references/brooks-constraints.md)。

**3. Compile.** Target Architecture 足够稳定后读 [program-contract.md](references/program-contract.md)，只编译会让当前结构真实变好的 Architecture Program。最多保留 3 个 improvements，不补数；每个完成时都必须产生 structural gain，并让旧 knowledge/authority/dependency/path 有真实 exit。research task、future wish、纯铺路 abstraction 或 implementation step 不能冒充 improvement。

**4. Deliver.** 这是本轮唯一交付点：如果 pressure 本质是 local，完整说明为什么保持 local；如果 architecture choice 仍缺 decisive Evidence/Human decision，完整指出缺口；如果已收敛，完整交付当前 Architecture Program。任何 material Human clarification/correction 都从最高受影响的 Ground/Judge 重新进入，重推依赖结论并再次完整 Deliver 当前 outcome；之前交付过不构成 completion state。不要输出 ready/completed/status token。

## Architecture rules

- **Layering & dependency.** 保持少量清晰层和稳定单向依赖；common/policy 不知道 specific provider/scenario，值得长期约束的方向优先能从 repo territory / tooling 直接看见。
- **Cohesion & simplicity.** 一个模块围绕一个主要 capability/responsibility 组织，闭合完成责任所需的内部 knowledge/state/lifecycle；两个结构都正确时选概念更少、public surface 更小、repo 更容易解释和修改的方案。
- **Abstraction vs specific.** 只抽象稳定共同 semantics/invariant；稳定且重要的差异保持 specific。代码相似和当前 provider partition 都不能替代 semantic judgment；没有 stable variation 不制造 provider，有真实差异也不为表面统一强行消除。
- **Primary vs auxiliary responsibility.** primary responsibility 决定主要 boundary 与组织；被判为 auxiliary 的 concern 附着在主结构上，不反向塑造它。未经 profiling/SLA/resource Evidence 证明的性能收益不能打穿结构边界。
- **Real evolution.** 新架构必须让旧 knowledge、authority、reverse dependency、special path 或 compatibility 真实退出或停止 authoritative；`old A → new abstraction → old B` 只是 complexity relocation。temporary dual path 必须有 architecture purpose 与 exit。

## Architecture altitude

AE 可以固定长期 layer/dependency、capability/module responsibility、abstraction/specific、必要 authority/SOT/control/lifecycle direction、essential variation 和 structural done condition；除非 representation 本身是 Human/repo/technical invariant，否则不固定 class/API/file/helper/schema/call implementation/MR/task/test provider。Implementation Design 从 Architecture Program 之后开始。
