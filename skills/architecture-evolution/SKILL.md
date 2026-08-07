---
name: architecture-evolution
description: 从仓库、模块或已知热点中的真实变化压力出发，发现并选择一个高价值架构演化机会，恢复业务现实，形成能够替代旧结构的目标设计，并用反例挑战与内置 Brooks 约束验证。不用于普通局部 bug、无变化压力的审美清理或全仓库战略重设计。
---

# Architecture Evolution · 发现机会，推进真实演化

North Star：**发现最值得处理的架构机会，并把其中一个推进为经代码现实、反例和 Brooks 约束验证，能够真正替代旧结构的目标设计。**

本 Skill 内置两类能力：

- **Opportunity discovery**：从真实变化压力中发现、比较并选择架构热点；
- **Design evolution**：恢复业务现实，形成目标设计，并对设计做反向挑战和风险验证。

一次只选择并深入一个热点，是 scope-control，不代表调用者必须预先知道热点。输入可以是仓库、模块、业务能力，也可以是已经明确的架构问题。

本文中的 `module` 是尺度无关的责任单元，可以是 class、package、service 或跨层 capability，不等于单个文件。

## Context loading

按需加载：

1. 先只用本文件限定搜索范围并发现变化压力；
2. 选中结构候选后再读 [rules.md](references/rules.md)；
3. 只有形成目标设计时才读 [design-contract.md](references/design-contract.md) 和 [verification.md](references/verification.md)；
4. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行禁止读取。

本 Skill 吸收 opportunity finding、improve 和 design grilling 的判断，但不调用或编排外部 Wayfinder、Improve、Grill 或 Brooks Skill。

## 何时使用

使用：

- 用户要求找出一个模块或局部代码库下一步最值得做的架构改进；
- 同一业务能力因入口、provider、family、团队或历史模块形成多套流程；
- 公共抽象充满 mode flag、optional 参数、外部 switch 或特殊入口；
- 一个模块混合多个独立变化原因，或完整能力被拆散给调用者组装；
- 通用层、Harness、Runtime 或稳定主流程反向依赖具体业务与实现；
- 新 facade、interface、registry 或 wrapper 没有替代旧路径。

跳过：

- 业务语义、owner 和依赖方向清楚的局部 bug 或机械改动；
- 只有审美不满，没有真实变化、维护或理解压力；
- 目标设计已经稳定，只需要实现或 code review；
- 用户要求的是多个平级目标或全仓库战略蓝图。

## Top architecture principles

1. **Business Semantic Integrity** — 同一业务语义统一，不同业务语义显式区分。
2. **Stable Abstraction with Explicit Variation** — 共同语义进入稳定抽象，真实差异限制在明确变化点。
3. **Cohesive Capability Ownership** — 一个模块拥有一项完整能力及其 invariant、状态和生命周期。
4. **Unidirectional Policy Dependency** — 源码依赖为 `policy → contract ← implementation`；底层不能反向定义或控制上层 policy。

共同 Gate：**Real Evolution** — 新结构必须替代并减少旧结构，不能只增加一层。

## Flow

### 1. Frame

限定架构搜索地界：

- `Area`：仓库局部、模块、业务能力或已知热点；
- `Pressure`：真实需求、重复修改、事故、维护阻塞或理解摩擦；
- `Scope`：发现和判断所需的最小上下游；
- `Out of scope`：本轮明确不碰的范围。

没有真实变化压力时，返回 `Status: No architecture opportunity`。

### 2. Discover

从代码、调用、测试、配置、变更历史、运行证据和仍有效文档中寻找结构机会。优先观察：

- 一条业务规则在多处同步修改；
- 调用者反复选择路径、实现或调用顺序；
- 模块同时承受不相关变化；
- 抽象增加但旧路径没有退出；
- 稳定层依赖易变场景或 provider；
- 业务名称、invariant 与代码结构互相冲突。

开放范围最多保留三个有证据的候选。已知热点不默认扩大搜索，只验证它是否是架构问题、是否存在更底层的局部根因。

每个候选都必须形成：

```text
Change pressure → Structural symptom → Consequence → Candidate boundary → Counterexample
```

### 3. Select one

选择一个本轮热点，不打分。优先选择同时满足以下条件的候选：

- 有重复或高代价的真实变化压力；
- 一个结构根因产生多个可观察后果；
- 可以限定最小分析边界；
- 能说明什么旧路径、重复知识或反向依赖将退出；
- 现有证据足以继续，或存在成本最低的关键探针。

其余候选只记录一句 defer reason。不得把多个平级问题拼成一个“大架构改造”。

用户只要求发现和选择时，可返回 `Status: Opportunity selected`；否则继续推进设计。

### 4. Ground business reality

对选中热点恢复：

- 当前入口、主流程与消费者；
- 输入、输出、错误、状态、生命周期和外部副作用；
- 业务事实与配置由谁解释；
- 共同语义、差异和调用者必须知道的实现细节；
- 当前源码依赖、运行控制和 composition 位置。

始终分开：

- `Observed`：证据直接证明；
- `Inferred`：证据支持的架构解释；
- `Unknown`：会改变业务判断、目标结构或兼容边界的未决事实。

能从 repo/runtime 查明的事实自己查。设计关键 Unknown 未关闭时返回 `Research required`。

### 5. Diagnose

先判断路径是否表达同一业务，再区分：

- **essential differences**：真实业务、协议、性能、一致性或生命周期要求；
- **accidental differences**：入口、团队、provider、历史实现或迁移残留。

读取 `rules.md`，只选择一个 `Primary architecture break`。其他问题作为 consequence：

```text
Observed evidence → Structural consequence → Primary break → Root cause → Counterexample → Confidence
```

### 6. Design

只形成一个推荐设计：

- canonical business capability；
- stable abstraction；
- explicit variation points；
- cohesive module ownership；
- `policy → contract ← implementation` 的依赖方向；
- `Keep / Move / Merge / Delete / Do not change`。

先统一业务，再形成抽象；先定义 capability 与 invariant，再决定具体模式。无法由证据裁决、且会形成长期业务或兼容承诺时返回 `Decision required`。

### 7. Grill

对推荐设计做反向攻击，而不是为它补解释：

- 是否把不同业务错误统一；
- 是否用 union interface、mode flag 或 optional 参数遮住旧语义；
- 是否把每个 concern 都升级成公开模块；
- 是否只改变类型依赖，callback/global state/registry 仍反向控制 policy；
- 是否把复杂度搬到 helper、adapter、配置或调用者；
- 是否存在代码、测试、ADR、兼容事实或迁移现实反驳设计；
- 删除目标是否真实，还是旧路径仍然 load-bearing。

挑战失败就修改、缩小或撤销设计。

### 8. Verify

只对最终设计读取 `verification.md`。使用本 Skill 内置的 Brooks R1–R6 和 Iron Law；禁止调用或依赖外部 Brooks Skill。

每个适用 finding 使用：

```text
Severity → Symptom → Source → Consequence → Remedy → How to verify
```

Remedy 必须已经进入目标设计。未实现和完成代码扫描时，不生成 Health Score，也不声称行为保持、迁移完成或旧路径已删除。

## Output

只返回一个状态：

- **`Status: No architecture opportunity`** — 搜索范围、变化压力证据、为什么不值得升级为架构工作、局部边界；
- **`Status: Opportunity selected`** — 仅在用户只要求发现/选择时输出：候选范围、选中热点、选择依据、deferred candidates 和下一步证据边界；
- **`Status: Research required`** — 已确认事实、一个会改变选择或设计的 Unknown、最小探针及其影响；
- **`Status: Decision required`** — 已确认边界、Human-owned 取舍、少量选项和推荐；
- **`Status: Design ready`** — 读取 `design-contract.md` 与 `verification.md`，输出完整 Architecture Design Contract；必须选择一个热点、一个主要断点、一个推荐设计，并给出具体 `Delete` 与 Brooks `PASS`。

本 Skill 的终点是架构机会选择或目标设计。后续任务书、实现和完整验收属于调用方，不进入本 Skill 的核心定义或输出协议。
