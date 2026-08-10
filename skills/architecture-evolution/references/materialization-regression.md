# Materialization Regression

仅用于显式 smoke/eval；正常 Architecture Evolution 运行禁止读取。它验证 case 暴露出的判断是否被压回既有语义，不新增 runtime stage、direction、proof model 或 output contract。

## M1 — Consumer usage partition is evidence, not architecture boundary

当前多个 consumer 各自只使用 capability 的一部分事实，且完整对象暴露导致 caller knowledge/reassembly。

通过：Intent 描述稳定 capability semantics 与应退出的 caller knowledge，但不因当前 consumer 切片直接产出一-consumer一-seam 的长期 public abstraction。只有 seam 有稳定 semantics/invariant、ownership、essential variation 或长期 change-boundary evidence 时，才值得作为 basic shape 交给后续设计。

失败：把“consumer 只需要一部分事实”直接等价为“按 consumer 形状创建长期 public view/interface”。

## M2 — Stable variation is not current implementation partition

当前 provider/family 映射到若干不同 class hierarchy 或调用形状，但部分差异可能只是历史 API、implementation accident 或过渡状态。

通过：先用可观察 semantic / invariant difference 判断 essential variation；provider 名称、class hierarchy 和 execution shape 只作为 evidence。只有差异会稳定改变 protected behavior、precondition、output semantics、lifecycle 或其他 architecture invariant 时，才进入长期 variation。

失败：把当前 provider/class/execution partition 直接冻结成 target taxonomy。

## M3 — Acceptance rule does not freeze verification provider

Architecture Intent 已写清 Direction、Boundary、Replacement / exit 和 stable acceptance rule；repo 中同时存在 build/test/replay/dependency probe 等 evidence provider。

通过：stable acceptance rule 只说明 intent outcome 与 exit 何时成立，不固定验证套餐。具体 provider 由后续 design/implementation 根据 repo verification authority 和最终 change surface 选择；当前 target/config/app 枚举不能被冻结为长期 architecture contract。

失败：默认冻结 `build + tests + replay/diff` 套餐，或把 evidence provider 本身写成 architecture property。

## M4 — Upper goal remains a discriminator, not a protocol

repo 已有仍有效且明确点名当前 area 的 architecture/evolution goal，同时存在局部 ownership/interface/dependency pressure。

通过：Intent 说明该 area 对既有上位 goal 的贡献，局部 target 只作为结构杠杆；不新增固定目标来源字段、全局搜索前置条件或 goal 层级协议。若没有已声明目标，则从跨边界 pressure 收敛最小 durable outcome。

失败：局部 target 合理却替代上位 outcome；或在没有 authoritative goal 时发明战略口号；或为了避免前两者建立新的目标发现协议。

## Captured ModelCurator regression

对 2026-08-07 captured Architecture Intent 检查：

1. `按消费角色可直接使用` 不能自动物化成 consumer-specific views；应收敛为 consumer 依赖稳定 capability semantics、退出无关内部知识。
2. `真实执行形状` 不能仅因当前调用形状存在就被冻结为长期 variation；必须有 semantic/invariant evidence。
3. build/test/replay/diff 不能成为固定 acceptance 套餐；Intent 只保留稳定 outcome-level acceptance，provider 由下游按最终 change surface 选择。
4. false-unification、owner-scope、adjacent-owner 与 Target Design stop guards 不得回退。
