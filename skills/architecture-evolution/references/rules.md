# Architecture Judgment

只在需要区分架构 intent、局部修改与候选方向时读取。

## North-star

局部 pressure 说明哪里疼；North-star 说明为什么值得成为下一步演化。

North-star source 必须声明期望的未来架构结果；只描述当前 reality 的 source 无论多权威，都只能约束 pressure 和 boundary。若 repo 当前 architecture / evolution source 明确把 area 放在一个上位目标中，Intent 写 area 对该目标的贡献；局部 ownership、interface 或 dependency 变化只作为结构杠杆。仍有效且明确点名 area 的 repo-level goal 优先于更近的 subsystem goal。没有已声明目标时，从重复的跨边界 pressure 推导最小 durable outcome，不发明战略口号。

本 Skill 以 AI-native 作为 architecture evolution 的 quality bar。贡献不是增加 agent 标签或自动化，而是把当前 pressure 中的 architecture judgment 编码成 repo 内可发现的边界、可机械执行的不变量与可独立验证的反馈；中央约束正确性和品味，局部方案保持自由。只写当前 intent 实际命中的贡献，不把这句话展开成 checklist。

North-star 清楚、success evidence 可观察、下游无需重新发现 why，而 target design 仍保持开放时，这个判断完成。

## Architecture threshold

形成 Architecture Intent 需要同时看见：

- pressure 会重复出现或恢复成本高；
- 一个结构原因造成多个可观察后果；
- 影响跨越单个局部实现，但仍能限定边界；
- 需要重新确定 semantics、owner、stable contract 或 dependency；
- 可以说出完成后什么旧知识、路径、判断或依赖会退出。

文件大、函数长、目录不整齐、模式不优雅或一次性修复不越过这条线。

## Reality

只观察会改变 intent 的面：

1. **Business semantics** — 同一业务是否有多套解释，还是不同 bounded context；
2. **Ownership & lifecycle** — config、resource、state、publication 与 lifetime 由谁拥有；
3. **Consumer knowledge** — caller 是否重组 implementation、config、ordering、identity 或 lifecycle 才能使用 capability；
4. **Dependency** — stable policy 是否被 provider、scenario 或 implementation 反向定义；
5. **Runtime control** — 谁选择、构造、驱动和消费 capability。

一个面整洁不能替另一个面作证。Consumer reassembly 是 signal，不是第五个 direction；纯 composition-root wiring 不是 reassembly。Ownership 只扩到 evidence 支持的 capability invariant，不自动吞并 execution、orchestration 或相邻 subsystem。

## Four levers

一个 intent 只选一个 primary lever，其他命中作为 consequence 或 obligation：

1. **Business Semantic Integrity** — 统一同一业务的事实解释，保留真实 bounded context；
2. **Stable Abstraction with Explicit Variation** — caller 依赖 capability，只有稳定 semantic/invariant difference 才成为 variation；
3. **Cohesive Capability Ownership** — capability、invariant、state 与 lifecycle 在一个可信边界闭合；
4. **Unidirectional Policy Dependency** — stable policy 通过 contract 约束易变 implementation，而不被它反向控制。

四个 lever 给结构变化命名，不替代 North-star outcome，也不直接物化成新 type、layer 或 topology。

## Real Evolution

Intent 必须指向真实减少，至少退出一项：

- 平行业务语义或重复事实解释；
- caller knowledge / capability reassembly；
- 无效 abstraction、特殊入口或永久 compat branch；
- 反向或循环 dependency。

只能说明“增加 facade/interface/manager/registry”时，intent 不成立。

## Guards

- **Explain first**：observed role、provider、family 或 consumer partition 是 evidence；只有稳定 semantics、invariant、ownership、change boundary 或 verification surface 才值得物化。
- **Preserve variation**：相似代码不证明业务相同；false unification 与 historical partition freeze 都是失败。
- **Keep ownership bounded**：关闭 consumer reassembly 不等于 ownership centralization；保留相邻 owner 的合法责任。
- **Close Unknown**：只调查会改变 intent、boundary 或 obligation 的 Unknown；probe 后明确 judgment changed / retained。
- **Use current evidence**：current code/runtime/config 优先；旧 snapshot 只作 provenance。Success evidence 写稳定规则，动态对象在实现时重算。
- **Reject relocation**：新 abstraction 必须让旧知识、路径或依赖退出，不能只搬进 helper、adapter、registry 或 caller。

## Ready

`Architecture intent ready` 需要同时满足：

- 一个 outcome，说明 North-star contribution 与 why now；
- 一个 primary lever，且没有锁死 target design；
- boundary、must preserve 与 material Unknown 清楚；
- 至少一个 replacement / exit；
- success evidence 直接证明 outcome、preservation 与 exit；
- 只携带当前方向真正相关的 Brooks constraints。
