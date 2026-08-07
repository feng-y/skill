# Materialization Regression

仅用于显式 smoke/eval；正常 Architecture Evolution 运行禁止读取。与 `validation.md` 一起检查，不新增 runtime stage、direction 或 output contract。

## M1 — Consumer knowledge reduction is not consumer-shaped abstraction

当前多个 consumer 各自只使用 capability 的一部分事实，且完整对象暴露导致 caller knowledge/reassembly。

通过：Intent 描述稳定 capability semantics 与应退出的 caller knowledge，但不因现有 consumer 切片直接产出 `ParseView / GRView / DenseView / ExecutorView` 或等价一-consumer一-seam 设计。只有 seam 有稳定 invariant、essential variation 或长期 change-boundary evidence 时，才成为下游 design obligation。

失败：把“consumer 只需要一部分事实”直接等价为“为每个 consumer 创建专用 public interface/view”。

## M2 — Stable variation is not the current execution-shape taxonomy

当前 provider/family 映射到若干不同调用形状，但部分差异可能只是历史 API 或 implementation accident。

通过：先用可观察 semantic / invariant difference 判断 essential variation；provider 名称、class hierarchy 和当前 execution shape 只作为 evidence。只有 shape 对 protected behavior、precondition、output semantics 或其他稳定 invariant 有真实差异时，才可进入 target variation。

失败：从“provider identity 不应泄漏”机械跳到“按当前 execution shape 建永久 taxonomy”。

## M3 — Success evidence is property-first

Intent 已能描述完成后必须成立的行为、boundary 或 replacement，但 repo 中存在 build/test/replay/dependency probe 等多种 evidence provider。

通过：Success evidence 先写必须证明的稳定 properties；具体 evidence provider 由后续 design/implementation 根据 repo verification authority 和最终 change surface 选择。只有 provider 本身是稳定受保护判卷标准，或当前必须点名才能消除验收歧义时，才在 Intent 固定它。动态 affected scope 仍在验收时重新推导。

失败：默认编译 `build + tests + replay/diff` 等固定套餐，或把某个 evidence provider 当成 architecture property。

## Captured ModelCurator regression

对 2026-08-07 的最新 captured Architecture Intent，至少检查：

1. `按消费角色可直接使用` 不得自动物化成 consumer-specific views；应收敛为 consumer 依赖稳定 capability semantics、退出无关内部知识。
2. `真实执行形状` 不得仅因当前调用形状存在就被冻结为长期 variation；必须有 semantic/invariant evidence。
3. `定向测试、build、replay/diff` 不得作为固定 acceptance 套餐；Intent 应保留 proof properties，provider 在后续按 repo verification authority 选择。
4. 已正确形成的 owner-scope、adjacent-owner、dynamic snapshot 和 evidence-driven Brooks cardinality guards 不得回退。

## Failure classes

- `consumer-shaped-abstraction` — 用当前 consumer 切片直接塑造长期 public abstraction。
- `variation-axis-lock-in` — 把 provider 名称、class hierarchy 或当前 execution shape 直接冻结成稳定 variation taxonomy。
- `evidence-provider-freeze` — 在 Intent 阶段把 build/test/replay 等 provider 套餐冻结成长期 acceptance contract，而不是先定义 proof properties。
