---
name: architecture-evolution
description: 用于架构方向模糊、历史模块持续演进或“下一刀应该改什么”这类输入：从指定模块的 repo reality 重识别 capability/boundary，收敛 Target Architecture，并写成少量真实改善结构的 Architecture Improvements。
---

# Architecture Evolution · 从模块现实收敛目标架构

**Human** 提供 change pressure 并拍板业务/兼容/风险等长期承诺；**Architecture Evolution** 调研 reality、做 architecture judgment 并写 Architecture Program；**Implementation agent** 决定具体 implementation。repo reality / authoritative SOT 是事实与约束 authority，不由当前 taxonomy 或 AE 的方案代替。

## 流程

**1. 调研。** 从指定 module/capability 看真实 responsibility、直接 upstream/downstream 和 consumer knowledge，再重识别 boundary 与 stable variation。当前 module/class/provider/family 只作 Evidence；只有长期 semantic/contract/lifecycle/performance/deployment difference 才证明 specific boundary。只为会改变 architecture judgment 的 authority/SOT/identity/external constraint 扩大搜索；继续 Research 只改变 How 时就停。

**2. 判断。** 先判 architecture vs local，再收敛 best-known Target Architecture；不让第一个 plausible shape 胜出，也不制造假 alternatives。repo/runtime 能关闭的 decisive fact 先查；真正 Human-owned 的业务/兼容/风险承诺才交给 Human。若由 Northstar 等上游调用，只返回 Evidence/options/decision surface，不另开 Human Ask。高层判断不足时读 [rules.md](references/rules.md)；legacy retirement 读 [legacy-lenses.md](references/legacy-lenses.md)；proposal 局部合理但整体膨胀时读 [brooks-constraints.md](references/brooks-constraints.md)。

**3. 写 Program。** Target Architecture 稳定后，只保留 target delta、少量 long-lived invariants、最多 3 个按 structural leverage 排序的 Improvements 及真实依赖；不补数。每个 Improvement 完成时都必须独立产生 structural gain + real exit；Program 同时说明整体完成后哪些旧 authority/dependency/path 不再 authoritative。research/setup/future wish/implementation step 不能冒充 Improvement。已有 authoritative SOT 直接引用；SOT 本身要变时指向原 authority 的 delta，不建平行规范。

**4. 交付。** local 就交付 local judgment；缺 decisive Evidence/Human decision 就交付缺口与继续条件；收敛后完整返回当前 Program，并把同一正文写入 OS/runtime 提供、位于 repo/workspace 外的 handoff Markdown file，显示实际 path。交付只包含当前 judgment/Program，不附 Research inventory、rejected alternatives、旧 Program 或 challenge trace。artifact 只负责 handoff，不替代 repo SOT。Human material correction 重开最高受影响判断并完整重交付；artifact 写失败就报告 blocker，不能把 chat 当 handoff。不要输出 ready/completed/executable/status token。

## 架构判断

- **Architecture vs local。** 只有 pressure 会改变长期 responsibility、dependency、abstraction boundary、primary responsibility 或旧结构退出时才升级；文件大、目录乱、switch/duplication 多本身不够。
- **Layering + cohesion。** 保持少量稳定单向依赖，common/policy 不知道 specific；长期 dependency boundary 优先由 repo territory/module/package/build/tooling 直接表达，而不是只靠文档维持。模块围绕主要 capability 闭合 knowledge/state/lifecycle，caller 不重组私有事实；已有独立 authority/lifecycle 的相邻 subsystem 保持 relation/contract，不为内聚吞并。两个结构都成立时选概念更少、public surface 更小的。
- **Abstraction vs specific。** 抽象稳定 semantics/invariant，不抽象表面相似；没有 stable variation 不制造 provider，有真实长期差异也不强行统一。Human 点名的 provider/facade/layer/registry 默认只是 candidate means，除非 authority 绑定 representation。
- **Primary vs auxiliary。** primary responsibility 决定 boundary；auxiliary concern 不反向塑造主结构。未经 profiling/SLA/resource Evidence 的性能收益不能打穿 boundary。
- **Real evolution。** 旧 knowledge/authority/reverse dependency/special path/compatibility 必须真实退出或停止 authoritative；`old → new abstraction → old` 只是 complexity relocation。temporary dual path 必须有 purpose + exit；无当前长期 Evidence 的 future hook/mode/registry/framework 不物化。

只有 Human、repo/upstream authority 或 verified reality 能把内容绑定成长期 invariant。除非 representation 本身被 authority 固定，AE 只固定 architecture outcome / structural done condition，不提前固定 class/API/file/schema/call shape/MR/task/test provider；Implementation Design 在 Program 之后。

## 发出前自检

1. Target 是否来自真实 responsibility/dependency/variation，而不是当前 taxonomy/proposed shape？
2. 是否同时满足 layering/cohesion、正确 abstraction/specific、primary responsibility 与 real exit？
3. 每个 Improvement 是否完成即 structural gain + real exit，Program 整体 exit 是否明确，且没有 research/setup/future/implementation step？
4. authoritative SOT 是否只引用或指向原 source delta？是否保持 architecture altitude？若已收敛，Program 是否完整 materialize，Human 新输入后是否完整重交付？
