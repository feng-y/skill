---
name: architecture-evolution
description: 用于历史模块、平行业务路径、抽象分裂或明确架构热点：基于代码证据统一同一业务语义，建立承载真实差异的稳定抽象，收敛模块责任与依赖方向，并让旧结构退出。不用于普通局部 bug、机械迁移或全仓库重设计。
---

# Architecture Evolution · 统一业务，收敛结构

North Star：**让同一业务只有一套 canonical semantics 和一个稳定使用面，让真实差异停留在明确变化点，让模块内聚、依赖单向，并让历史平行结构退出。**

本 Skill 从一个真实架构热点完成业务判断、目标设计和设计验证；不拥有新的 workflow，不替 Northstar 改写 Goal，也不默认执行重构。

本文中的 `module` 是尺度无关的责任单元，可以是 class、package、service 或跨层 capability，不等于单个文件。

## Context loading

按需加载，不把全部 reference 注入每次运行：

1. 先只用本文件绑定目标并恢复业务现实；
2. 确认存在结构候选后再读 [rules.md](references/rules.md)；
3. 只有 `Design ready` 才读 [design-contract.md](references/design-contract.md) 和 [verification.md](references/verification.md)；
4. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常架构分析禁止读取。

## 何时使用

使用：

- 同一业务能力因入口、provider、family、团队或历史模块形成多套流程；
- 公共抽象只是历史实现的并集，充满 mode flag、optional 参数或外部 switch；
- 一个模块混合多个独立变化原因，或完整能力被拆散给调用者组装；
- 通用层、Harness、Runtime 或稳定主流程反向依赖具体业务与实现；
- 新 facade、interface、registry 或 wrapper 没有替代旧路径。

跳过：

- 业务语义和 owner 已清楚、变化局部的普通 bug 或机械改动；
- 两条路径属于不同业务语义或 bounded context，且没有错误共享；
- 只有审美不满，没有真实变化压力；
- 目标设计已经稳定，只需要实现或 review；
- 多个平级目标或全仓库战略重设计。

## Top architecture principles

1. **Business Semantic Integrity** — 同一业务语义统一，不同业务语义显式区分。
2. **Stable Abstraction with Explicit Variation** — 共同语义进入稳定抽象，真实差异限制在明确变化点。
3. **Cohesive Capability Ownership** — 一个模块拥有一项完整能力及其 invariant、状态和生命周期。
4. **Unidirectional Policy Dependency** — 业务策略依赖稳定能力，具体实现不能反向定义或控制策略。

共同 Gate：**Real Evolution** — 新结构必须替代并减少旧结构，不能只增加一层。

## Flow

### 1. Bind

只绑定一个架构目标：

- `Target`：业务能力、模块或局部调用切片；
- `Trigger`：暴露问题的真实需求、重复变化或维护摩擦；
- `Scope`：判断所需的最小上下游；
- `Out of scope`：本轮明确不碰的范围。

没有真实变化压力时，优先返回 `Status: No architecture change`。

### 2. Recover business reality

从代码、调用、配置、状态、测试、运行证据、历史和仍有效 ADR 中恢复：

- 现有入口和主流程；
- 输入、输出、错误、状态、生命周期和外部副作用；
- 业务事实与配置由谁解释；
- 各路径的共同语义和差异；
- 调用者必须知道的实现细节；
- 当前依赖与控制方向。

始终分开：

- `Observed`：证据可直接证明；
- `Inferred`：由证据支持的架构解释；
- `Unknown`：会改变“同一业务/不同业务”、variation、模块边界、依赖或兼容判断的未决事实。

能从 repo/runtime 查明的事实自己查。设计关键 Unknown 未关闭时，不提前统一业务或抽象。

### 3. Classify differences

先回答业务问题，再回答结构问题：

1. 这些路径是否表达同一项业务能力？
2. 共同的输入、输出、错误、invariant 和生命周期是什么？
3. 哪些差异是 **essential differences**：真实业务、协议、性能或一致性要求？
4. 哪些差异是 **accidental differences**：入口、团队、provider、历史实现或兼容残留？

不能证明“同一业务”时，不得为了复用强行统一；不能证明差异本质时，也不得把历史分支永久化。

### 4. Diagnose

出现结构候选后读取 `rules.md`，选择一个 `Primary architecture break`：

- 同一业务存在多套语义或事实解释 → Principle 1；
- 业务语义已可统一，但抽象暴露或复制实现差异 → Principle 2；
- 完整能力被混合或拆散，模块不围绕一个 invariant → Principle 3；
- 策略层与实现层的依赖或控制方向反转 → Principle 4。

其他命中项作为 secondary consequence。每个主要结论必须形成：

```text
Observed evidence → Structural consequence → Primary break → Root cause → Counterexample checked → Confidence
```

代码形态只是信号。多处 switch 不自动等于需要多态；文件大不自动等于低内聚；具体依赖也不自动等于反向依赖。

### 5. Design

根因稳定后，只形成一个推荐设计：

- `Canonical business capability`：统一后的业务名称、语义和 invariant；
- `Stable abstraction`：调用者依赖的完整 contract；
- `Variation points`：每项本质差异由谁处理，如何隔离；
- `Cohesive module`：能力、状态、生命周期和内部 collaborator 的归属；
- `Dependency direction`：源码依赖为 `policy → contract ← implementation`；运行控制向下，result/evidence 向上；
- `Design delta`：`Keep / Move / Merge / Delete / Do not change`。

先统一业务，再形成抽象；先定义 capability 与 invariant，再决定 class、factory、strategy、adapter 或 registry。

repo 证据无法裁决、且会形成长期业务承诺或高代价兼容边界时，返回 `Decision required`。

### 6. Challenge

所有 `Design ready` 必须通过 `Real Evolution` Gate：

- 没有把不同业务错误统一；
- 不是用 union interface、mode flag 或 optional 参数包住多套旧语义；
- 没有把每个 concern 都升级成公开模块；
- 没有让实现、callback、global state 或 registry 反向控制 policy；
- 没有把复杂度搬到 helper、adapter 或调用者；
- 旧入口、旧事实源、重复抽象或反向依赖有明确退出结果。

挑战失败时修改或撤销设计，不为原结论补解释。

### 7. Verify

仅对 `Design ready` 读取 `verification.md`，验证：

- business semantic integrity；
- variation containment；
- capability cohesion；
- dependency direction；
- real replacement。

每项必须写 `Before / Expected after / How to verify`。未执行实现证据时，不得声称行为保持、迁移完成或旧路径已经删除。

## Output

只返回一个状态。

### `Status: No architecture change`

只输出：`Target`、`Observed evidence`、为什么不是架构问题、最小 `Local change boundary`。禁止输出 unified abstraction 或 Design Delta。

### `Status: Research required`

只输出：`Target`、已确认的 `Observed / Inferred`、一个 design-changing `Unknown`、最小证据探针及其影响字段。Unknown 关闭前不统一业务或设计抽象。

### `Status: Decision required`

只输出：`Target`、已确认事实、所有方案共享的业务边界、Human-owned 取舍、少量选项和一个推荐。不要伪造唯一业务定义或兼容承诺。

### `Status: Design ready`

读取 `design-contract.md` 与 `verification.md`，输出完整 Architecture Design Contract。必须给出具体 `Delete`；若没有物理代码删除，明确消失的平行业务语义、调用者知识、重复判断或反向依赖。

由 Northstar 调用时，本 Skill 只返回设计判断和实现约束；Goal、授权、任务书、执行和完整验收仍由 Northstar 负责。
