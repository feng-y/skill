---
name: architecture-evolution
description: 用于历史模块、反复扩散的变更或明确架构热点：基于有限规则识别架构坏味道，恢复错误的责任与变化归属，输出一个有代码证据、可验证且避免新增壳层的目标设计。适合分层、依赖方向、模块内聚、变化局部性、浅抽象和历史结构问题；不用于全仓库重设计或普通局部 bug。
---

# Architecture Evolution · 识别结构问题，设计更好的责任与边界

Architecture Evolution 是一个架构诊断与设计 Skill。它不拥有新的 workflow，不替 Northstar 重定 Goal，也不默认执行重构。它读取真实代码，识别为什么变化无法局部发生，然后重新设计责任、变化归属、依赖方向和 seam。

North Star：**让一个真实且高频的变化集中到正确 owner，让稳定主流程和调用者需要知道得更少，并明确哪些旧结构应当消失。**

“高内聚、低耦合、分层、单向依赖”只作为结果语言，不能直接充当结论。每个判断必须经过：

```text
代码证据 → 规则违反 → 责任根因 → 目标设计 → 改进验证
```

## 何时使用

用于以下情况：

- 一个需求反复修改多个模块、family、provider 或历史分支；
- 一个模块同时承载主流程、配置、构造、观测、兼容或优化等不同变化原因；
- 核心流程知道具体实现类型、特殊初始化、内部状态或隐含调用顺序；
- 调用者需要在模块外重新拼装配置、状态、类型、contract 或生命周期；
- 现有接口、基类、wrapper 或 adapter 增加了层次，却没有减少调用者知识；
- 用户指定一个历史模块或架构热点，希望先识别问题并形成设计。

跳过以下情况：

- 普通局部 bug、机械迁移、明确且安全的小改动；
- 没有现实变化压力，只是希望代码“更优雅”；
- 全仓库战略架构、多个平级目标模块或组织级重设计；
- 已有目标设计已经稳定，只需要实现、测试或 review。

## 运行原则

- **绑定一个目标。** 用户指定模块或路径时直接使用；否则只在真实变更热点中选择一个目标，不全仓库漫游。
- **先查事实，再作判断。** 读取真实调用、数据与状态 owner、配置、测试、相关历史和仍有效的 ADR。能从 repo 查明的事实不问 Human。
- **一次只选一个主要问题。** 次要信号最多记录两项，不把一次诊断扩成全面清理。
- **先设计责任，再设计类型。** 不从目录、类名、执行步骤或设计模式直接推导目标结构。
- **默认自主形成一个推荐设计。** 只有多个实质不同设计会改变长期边界、兼容承诺或高代价取舍，且 repo 证据无法裁决时，才返回 Human 决策；不要默认进入 grilling。
- **设计改善不等于实现完成。** 本 Skill 验证的是设计判断是否让变化更局部、知识更集中、依赖更稳定；行为不漂移仍是后续实现合同的证明义务。

## 流程

### 1. Bind：绑定目标与现实压力

写清：

- `Target`：本次分析的一个模块、能力或局部调用切片；
- `Trigger`：什么真实需求、修改扩散或维护摩擦暴露了问题；
- `Scope`：必须读取的上下游；
- `Out of scope`：本轮不扩展到哪里。

没有真实压力时，优先返回 `Status: No architecture change`，不要为了使用 Skill 制造重构理由。

### 2. Ground：恢复当前现实

最少恢复这些事实：

- 主流程和关键调用路径；
- 当前责任由谁承担；
- 数据、配置、状态和业务判断的 owner；
- 主要变化维度及其分布位置；
- 调用者必须知道的接口外知识；
- 受保护行为、测试和历史兼容面。

输出时严格分开：

- **Observed**：代码、调用、配置、测试或历史可直接证明的事实；
- **Inferred**：由证据支持的架构解释；
- **Unknown**：会改变责任、seam、兼容或验证判断，但当前不能确认的事项。

Unknown 必须改变下一步：继续查证、降级结论、返回 Human 决策或停止。不能列出后继续假装确定。

### 3. Diagnose：按有限规则诊断

读取 [rules.md](references/rules.md)，依次检查四条核心规则和一个设计 Gate：

1. **一个责任或变化维度只有一个 owner。**
2. **稳定主流程不依赖易变实现细节。**
3. **模块隐藏复杂度，调用者不在 seam 外重新组装能力。**
4. **独立变化原因具有独立责任边界。**

设计 Gate：**新设计必须替代旧结构，而不是再包一层。**

选择一个 `Primary rule violation`。每个结论都必须包含：

```text
Observed signal
→ Rule violation
→ Root-cause ownership/seam hypothesis
→ Counterexample checked
→ Confidence
```

代码形态只是信号。例如多处 `switch family` 不能自动推出多态；先确认这些判断是否真的重复解释同一个变化维度，还是分别承担不同业务语义。

如果证据只支持局部实现问题，直接返回 `No architecture change`。如果会改变设计的事实仍可通过 repo/runtime 查明，返回 `Research required`，不要提前设计 seam。

### 4. Design：形成一个推荐目标设计

只在根因已经足够稳定时继续。先回答四个问题：

1. **谁拥有主责任？**
2. **谁拥有主要变化维度？**
3. **稳定依赖应该指向哪里？**
4. **哪个 seam 能让调用者少知道什么？**

设计必须包含：

- `Target responsibility map`：责任、owner、输入、输出、owned truth/state、不得拥有的内容；
- `Variation ownership`：provider、family、输入来源、策略、观测、兼容等差异由谁处理；
- `Dependency direction`：稳定 contract 与易变 implementation 的方向；
- `Target seam`：调用者仍需知道什么、不再需要知道什么；
- `Design delta`：`Keep / Move / Merge / Delete / Do not change`。

默认只给一个推荐设计。只有当前 seam 存在两个以上真实、长期且证据无法裁决的取舍时，才返回 `Status: Decision required`。

不要用模式名代替设计。`factory`、`strategy`、`adapter`、`registry`、`observer` 只有在责任与变化归属已经成立后，才可能成为实现手段。

### 5. Challenge：反向攻击设计

至少检查：

- 是否只是增加 wrapper、manager、接口或基类；
- 是否为尚不存在的未来变化提前抽象；
- 是否把真实业务差异错误合并；
- 是否移动了代码，但事实、状态或判断仍有多个 owner；
- 是否缩小了目标文件，却把复杂度重新散到 helper、adapter 或调用者；
- 是否仍有旧入口、旧事实源或历史路径继续承重；
- 新 seam 是否只有一个假想 adapter，且没有测试替代或真实变化证明其存在价值；
- 现有 ADR 或兼容承诺是否构成反例。

挑战失败时，修改或撤销设计，不为保持原结论而补解释。

### 6. Verify：验证设计假设

读取 [verification.md](references/verification.md)，比较：

- **Change locality**：同类变化需要修改和理解的位置是否减少；
- **Ownership concentration**：同一责任、事实或变化判断是否收敛到一个 owner；
- **Dependency stability**：稳定主流程是否不再知道具体实现差异；
- **Caller knowledge**：调用者必须知道的状态、顺序、配置和特殊入口是否减少；
- **Replacement**：哪些旧 switch、重复判断、wrapper、入口、事实源或无效依赖能够消失。

不能只写“更符合高内聚/低耦合”。每项改善必须有 `Before / Expected after / How to verify`。

行为不漂移以 `Protected behavior` 的形式交给后续实现：输入输出、错误语义、配置兼容、调用顺序、副作用、状态生命周期和必要性能边界。未实际执行测试时，不得声称行为已经验证。

## 输出

按 [design-contract.md](references/design-contract.md) 根据状态输出最小充分信息。

只返回一个状态：

- **`Status: No architecture change`**：输出目标、证据、为什么不是架构问题，以及推荐的局部修改边界；不要输出目标 seam 或架构 Delta。
- **`Status: Research required`**：输出已确认事实、会改变设计的 Unknown、最小证据探针及其可能改变的设计字段；不要提前编造目标结构。
- **`Status: Decision required`**：输出已确认事实、Human-owned 取舍、选项、推荐和后果；只描述已经被证据支持的共同设计边界。
- **`Status: Design ready`**：输出完整 Architecture Design Contract：一个主要规则违反、一个推荐设计、Design Delta、Protected behavior 和改进验证。

每个 `Design ready` 必须给出具体 `Delete`；若没有物理代码删除，必须明确哪个调用者知识、重复判断或无效依赖将被消除。

本 Skill 不新增 scheduler、manager、固定 Agent 拓扑或第二套执行 Flow。由 Northstar 调用时，它只返回设计判断与实现约束；Goal、授权、任务书编译、执行和完整验收仍由 Northstar 的既有 Flow 负责。
