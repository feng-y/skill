# Materialization Regression

仅用于显式 smoke/eval；正常 Architecture Evolution 运行禁止读取。它验证 case 暴露出的判断是否被压回既有语义，不新增 runtime stage、direction、proof model 或 output contract。

## M1 — Consumer usage partition is evidence, not architecture boundary

当前多个 consumer 各自只使用 capability 的一部分事实，且完整对象暴露导致 caller knowledge/reassembly。

通过：Intent 描述稳定 capability semantics 与应退出的 caller knowledge，但不因当前 consumer 切片直接产出一-consumer一-seam 的长期 public abstraction。只有 seam 有稳定 semantics/invariant、ownership、essential variation 或长期 change-boundary evidence 时，才成为下游 design obligation。

失败：把“consumer 只需要一部分事实”直接等价为“按 consumer 形状创建长期 public view/interface”。

## M2 — Stable variation is not current implementation partition

当前 provider/family 映射到若干不同 class hierarchy 或调用形状，但部分差异可能只是历史 API、implementation accident 或过渡状态。

通过：先用可观察 semantic / invariant difference 判断 essential variation；provider 名称、class hierarchy 和 execution shape 只作为 evidence。只有差异会稳定改变 protected behavior、precondition、output semantics、lifecycle 或其他 architecture invariant 时，才进入长期 variation。

失败：把当前 provider/class/execution partition 直接冻结成 target taxonomy。

## M3 — Evidence obligation does not freeze provider

Architecture Intent 已经写清 desired end state、must-preserve、boundary、design obligations 和 replacement/exit，repo 中同时存在 build/test/replay/dependency probe 等 evidence provider。

通过：Success evidence 直接指出上述 intent claim 中哪些必须被实际证明；不额外生成 proof-property taxonomy。具体 provider 由后续 design/implementation 根据 repo verification authority 和最终 change surface 选择。provider 本身是稳定受保护判卷标准，或必须点名才能消除歧义时，才在 Intent 固定。动态 affected scope 仍保留 scope derivation。

失败：默认冻结 `build + tests + replay/diff` 套餐，或把 evidence provider 本身写成 architecture property。

## M4 — Local deepening is a lever, not the North-star

repo 已声明与当前 module 相关的 architecture goal，同时存在 module-local ownership / interface pressure。

通过：Intent 说明 module 对 North-star 的贡献；局部 deepening 只作为结构杠杆、obligation 或下游 target-design candidate。

失败：primary intent 只要求 capability ownership、truthful provider、consumer knowledge 退出或 stable interface，仍需下游重新发现为什么值得推进。

## Captured ModelCurator regression

对 2026-08-07 captured Architecture Intent 检查：

1. `按消费角色可直接使用` 不能自动物化成 consumer-specific views；应收敛为 consumer 依赖稳定 capability semantics、退出无关内部知识。
2. `真实执行形状` 不能仅因当前调用形状存在就被冻结为长期 variation；必须有 semantic/invariant evidence。
3. `定向测试、build、replay/diff` 不能作为固定 acceptance 套餐；应保留当前 Intent 的 evidence obligation，provider 在后续按 repo verification authority 选择。
4. owner-scope、adjacent-owner、dynamic snapshot 和 evidence-driven Brooks cardinality guards 不得回退。
5. ModelCurator 的局部 capability closure 不能替代它对 repo evolution horizon 的贡献；AI-native 贡献还必须形成 agent 可发现、可执行并可独立验证的 architecture / taste invariant。

## General failure classes

- `observed-partition-materialization` — 没有稳定 semantic/invariant/change-boundary evidence，却把当前 consumer/provider/class/execution partition 物化成长期 architecture contract。
- `evidence-provider-freeze` — 在 Intent 阶段冻结具体验证套餐，而不是保留现有 Intent claim 的 evidence obligation。
- `north-star-loss` — 局部 target 合理，却替代了 area 对上位 architecture goal 的贡献。
