# Architecture Reasoning Details

本文件展开 [SKILL.md](../SKILL.md) 中五个 architecture rules 的判别边界与反例；主 Skill 拥有稳定 architecture contract，本文件不建立第二套流程或输出规范。`change locality / knowledge / SOT / control / lifecycle / variation / complexity relocation` 只在能区分主 Skill 的结构判断时作为 evidence 使用。

## Architecture or local

只有真实 structural pressure 需要改变长期 layer/dependency、module responsibility、abstraction boundary、primary responsibility 或旧结构退出时，才升级为 architecture work；文件大、目录乱、switch 多或一次局部修改都不足以证明。

## Layering & dependency

保持少量清晰层与稳定单向依赖：policy/common 不应知道 specific provider/scenario。Layer 必须对应稳定 responsibility + dependency boundary；值得长期约束的方向优先从 repo territory / tooling 可见，而不是靠口头规则维持。

## Cohesion & simplicity

模块围绕一个主要 capability/responsibility 组织，闭合完成该责任所需的内部 knowledge/state/lifecycle，避免 caller 重新拼装内部事实；相邻 subsystem 已有正确 authoritative owner 时保持清晰 relation/contract，不为“内聚”无证据吞并其责任。两个结构都正确时，优先概念更少、public surface 更小、repo 更容易解释和修改的方案。

## Abstraction vs specific

只抽象稳定共同 semantics/invariant；稳定且重要的差异保持 specific。代码相似、当前 class/provider/mode/consumer partition 都只是 evidence；只有长期 semantic、contract、lifecycle、performance architecture、deployment 等差异才证明 stable variation。没有这种差异，不制造 provider；有则不为表面统一强行消除。

## Primary vs auxiliary responsibility

先由 capability semantics 判断 primary responsibility，让它决定主要 boundary 与组织。其他 concern 只有被判断为 auxiliary 后才应附着于主结构；名称本身不预分类。未经 profiling/SLA/resource evidence 证明的性能收益不能打穿 layering、cohesion 或 abstraction boundary。

## Real evolution

Target Architecture 必须让旧 knowledge/authority/reverse dependency/special path/compatibility 真实退出或停止 authoritative；`old A → new abstraction → old B` 只是 complexity relocation。temporary adapter/dual path 必须有 architecture purpose 与 exit condition；architecture-level transition 只表达结构依赖，不展开文件/MR/test/发布步骤。

## Architecture decision

不要停在第一个 plausible shape，也不要制造假 alternatives。只有长期 layering、module boundary、abstraction/specific 或 primary-responsibility placement 不同时才是 materially different architecture fork。

满足稳定业务语义与必要约束后，优先选择分层更清楚、内聚更高、抽象更自然、主责任更突出、旧复杂度退出更多且整体更简单的结构。真实 fork 若仍缺少 decisive repo/runtime evidence，不按模式偏好强选；明确缺失的 evidence / Human decision，由 Flow 的 Deliver 交付。

## Altitude & unknowns

AE 可以固定长期 layer/dependency、module/capability responsibility、必要 authority/SOT/control/lifecycle direction、essential variation 与 architecture-level acceptance；除非 Human/repo authority 或不可替代技术约束使 representation 本身成为 invariant，否则不固定 class/API/file/helper/schema/call implementation/task/test provider。

只有会改变 architecture-vs-local、Target Architecture 或 architecture-level evolution 的 unknown 才阻塞；repo/runtime 能关闭的先 probe，真正 Human-owned 的业务、兼容、风险或长期承诺才 Ask。其他 unknown 留给 Implementation Design / execution。
