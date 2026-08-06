---
name: architecture-evolution
description: 用于历史模块、反复扩散的变更或明确架构热点：基于代码证据识别责任、变化归属、依赖方向或 seam 的结构问题，并输出一个克制、可验证的目标设计。不用于普通局部 bug、机械迁移或全仓库重设计。
---

# Architecture Evolution · 识别结构问题，设计责任与边界

North Star：**让一个真实变化集中到正确 owner，让稳定主流程和调用者少知道，并让被替代的旧结构能够退出。**

本 Skill 只负责架构诊断与设计，不拥有新的 workflow，不替 Northstar 改写 Goal，也不默认执行重构。

## Context loading

按需加载，不把全部 reference 注入每次运行：

1. 先只用本文件绑定目标并读取代码现实；
2. 出现结构候选时再读 [rules.md](references/rules.md)；
3. 只有 `Design ready` 才读 [design-contract.md](references/design-contract.md) 和 [verification.md](references/verification.md)；
4. [validation.md](references/validation.md) 只用于 Skill smoke/eval，正常运行禁止读取。

## 何时使用

使用：

- 同类需求反复修改多个模块、provider、family 或历史分支；
- 一个模块混合多个独立变化原因；
- 稳定主流程知道具体实现、特殊配置、内部状态或隐含顺序；
- 调用者需要在 seam 外重新拼装一项完整能力；
- 接口、基类或 wrapper 增加层次，却没有减少知识或旧结构。

跳过：

- owner 清楚、变化局部的普通 bug 或机械改动；
- 只有审美不满，没有真实变化压力；
- 目标设计已经稳定，只需要实现或 review；
- 多个平级目标或全仓库战略重设计。

## Flow

### 1. Bind

只绑定一个目标：

- `Target`：模块、能力或局部调用切片；
- `Trigger`：暴露问题的真实需求或维护摩擦；
- `Scope`：判断所需的最小上下游；
- `Out of scope`：本轮明确不碰的范围。

没有现实压力时，优先返回 `Status: No architecture change`。

### 2. Ground

从真实代码、调用、状态、配置、测试、相关历史和仍有效 ADR 中恢复：

- 主流程；
- 责任、事实和状态 owner；
- 主要变化维度及分布；
- 调用者必须知道的接口外知识；
- 受保护行为和兼容面。

始终分开：

- `Observed`：证据可直接证明；
- `Inferred`：由证据支持的架构解释；
- `Unknown`：会改变 owner、seam、依赖或兼容判断的未决事实。

能从 repo/runtime 查明的事实自己查。Unknown 未关闭时，不提前设计目标 seam。

### 3. Diagnose

出现结构候选后读取 `rules.md`，只选择一个 `Primary rule violation`：

1. 一个责任或变化维度只有一个 owner；
2. 稳定主流程不依赖易变实现细节；
3. 模块隐藏复杂度，调用者不在 seam 外重组能力；
4. 独立变化原因具有独立责任边界。

每个结论必须形成：

```text
Observed signal → Rule violation → Root cause → Counterexample checked → Confidence
```

代码形态只是信号。多处 `switch family` 不自动等于多态；文件大也不自动等于低内聚。

证据只支持局部问题时返回 `No architecture change`；仍缺可查事实时返回 `Research required`。

### 4. Design

根因稳定后，只形成一个推荐设计：

- 主责任由谁拥有；
- 主要变化维度由谁拥有；
- 稳定依赖指向哪里；
- 哪个 seam 让调用者少知道什么；
- `Keep / Move / Merge / Delete / Do not change`。

先设计责任，再设计类型。`factory`、`strategy`、`adapter`、`registry` 等只是可能的实现手段，不能代替责任判断。

repo 证据无法裁决、且会形成长期或高代价边界承诺时，返回 `Decision required`，不要伪造唯一答案。

### 5. Challenge

所有 `Design ready` 必须通过 `Replace, not layer` Gate：

- 不是新增 wrapper、manager、接口或基类；
- 不是为假想未来提前抽象；
- 没有错误合并真实业务差异；
- 没有把复杂度从目标文件搬到 helper、adapter 或调用者；
- 旧入口、旧事实源或无效依赖有明确退出结果。

挑战失败时修改或撤销设计，不为原结论补解释。

### 6. Verify

仅对 `Design ready` 读取 `verification.md`，验证设计假设是否改善：

- change locality；
- ownership concentration；
- dependency stability；
- caller knowledge；
- replacement。

每项必须写 `Before / Expected after / How to verify`。未执行实现测试时，不得声称行为已经验证。

## Output

只返回一个状态。

### `Status: No architecture change`

只输出：`Target`、`Observed evidence`、为什么不是架构问题、最小 `Local change boundary`。禁止输出 target seam 或 Design Delta。

### `Status: Research required`

只输出：`Target`、已确认的 `Observed / Inferred`、一个会改变设计的 `Unknown`、最小证据探针及其影响字段。Unknown 关闭前不设计 target seam。

### `Status: Decision required`

只输出：`Target`、已确认事实、所有方案共享的边界、Human-owned 取舍、少量选项和一个推荐。不要伪造唯一设计。

### `Status: Design ready`

读取 `design-contract.md` 与 `verification.md`，输出完整 Architecture Design Contract。必须给出具体 `Delete`；若没有物理代码删除，明确消失的调用者知识、重复判断或无效依赖。

由 Northstar 调用时，本 Skill 只返回设计判断和实现约束；Goal、授权、任务书、执行和完整验收仍由 Northstar 负责。
