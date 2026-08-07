# Architecture Evolution Rules

只在出现有证据的架构候选后读取。一次只选择一个热点和一个 `Primary architecture break`。

```text
Pressure → Opportunity → Selection → Reality → Root cause → Design → Grill → Proof
```

## Opportunity discovery

架构机会必须来自真实变化压力，不从模式偏好或代码外观出发。

### Useful evidence

- 同一业务规则或配置解释反复在多处同步修改；
- 新需求持续增加特殊入口、mode flag、provider/family switch；
- 事故、回归或测试脆弱性集中在同一结构边界；
- 调用者必须知道内部步骤、状态、生命周期或实现类型；
- 一个模块同时承受多个互不相关的变化原因；
- 新抽象不断增加，但旧路径、旧事实源和旧判断仍然存在；
- common/core/Harness/Runtime 被具体场景或 provider 牵引。

### Candidate contract

每个候选只写：

```text
Pressure evidence
Structural symptom
Consequence
Candidate boundary
What could exit
Counterexample checked
```

开放范围最多保留三个候选。只有审美、文件大小、函数长度、目录不整齐或单次局部修改，不构成候选。

## Select one opportunity

不使用分数。比较以下判断：

1. **Pressure** — 是否存在重复、高频或高恢复成本的真实变化；
2. **Leverage** — 一个根因是否造成多个变化、理解或测试后果；
3. **Boundary** — 是否可以在一个有限上下游内判断；
4. **Replacement** — 是否能指出将退出的旧路径、重复知识、调用者知识或反向依赖；
5. **Evidence** — 是否足以继续，或存在一个最小高价值探针。

选择一个最强候选。其余候选只写一句 defer reason，例如：压力不足、属于独立业务、证据不足、边界过大或收益依赖当前热点先解决。

已知热点仍要通过该判断；如果它只是局部问题，返回 `No architecture opportunity`，不要为了服从输入而升级。

## Primary architecture break

- 同一业务存在多套语义或事实解释 → Principle 1
- 共同语义已明确，但实现差异泄漏进 contract 或稳定流程 → Principle 2
- 完整能力被混合或拆散，模块不围绕一个 invariant → Principle 3
- policy 与 implementation 的依赖或控制方向反转 → Principle 4

其他命中项只作为 consequence。

## Principle 1 — Business Semantic Integrity

**Rule**：同一业务语义统一，不同业务语义显式区分。

**Signals**

- 相同业务在入口、family、provider 或历史模块中走不同主流程；
- 同一输入产生不同输出、错误、状态或副作用；
- 同一配置、能力或业务事实被多次解释；
- 修改一条业务规则必须同步多套实现。

**Consequence**

系统没有唯一 canonical semantics，调用者和测试必须知道“走哪条路径”；或者不同业务被错误压进一个模糊概念。

**Guards**

- 不同 bounded context、invariant、一致性、错误或生命周期可以保持独立；
- 迁移期双轨必须声明 authoritative path 和退出条件；
- 代码相似不是业务相同的证据。

**Design / proof**

定义 canonical capability 与共同 input/output/error/invariant/lifecycle；显式保留本质差异，删除重复解释和平行 canonical path。证明一条业务规则只需修改一个权威位置，且不同业务仍可区分。

## Principle 2 — Stable Abstraction with Explicit Variation

**Rule**：共同语义由一个稳定抽象承载，本质差异只存在于明确 variation point。

**Signals**

- 公共 interface 是历史字段和方法的并集；
- mode flag、optional provider config 或外部 switch 泄漏给调用者；
- 新增实现必须修改稳定 flow 和多个调用者；
- facade/base/registry 外面统一，内部仍保留多套判断和特殊入口。

**Consequence**

调用者依赖实现差异而不是业务能力；抽象只统一形状，没有统一语义。

**Guards**

- 单一内部实现不一定需要 seam；
- external protocol 或 closed enum 上的 switch 可以合理；
- thin adapter 如果真实吸收外部变化，可以保留；
- 性能具体表示必须局部且不外泄。

**Design / proof**

从 canonical capability 定义 stable contract；明确 variation、owner 与专属配置；调用者只依赖 capability。证明新增或替换 variation 不修改稳定 flow，且至少一个旧抽象、switch 或入口退出。

## Principle 3 — Cohesive Capability Ownership

**Rule**：一个模块拥有一项完整能力及其 invariant、状态和生命周期。

**Signals**

- 模块混合业务、provider 选择、metrics/debug、cache、compatibility 和资源生命周期；
- 主责任必须用“同时还负责”才能描述；
- 状态和生命周期散落在 manager、helper 或全局对象；
- wrapper 透传，调用者和测试在外部重组顺序与行为。

**Consequence**

无关变化互相影响，关键 invariant 没有完整 owner，复杂度泄漏到调用者和测试。

**Guards**

- observer、cache 和优化可以是 private collaborator；
- 为同一 invariant 共同变化的步骤仍然内聚；
- composition root 的编排与高 fan-out 可以合理；
- 文件大或函数长不是架构结论。

使用 deletion test：删除模块后，复杂度若只消失，它可能是壳；必要知识若散回多个调用者，它才在创造 leverage。

**Design / proof**

收回 invariant、状态、生命周期、错误转换和必要顺序；只分离真实独立的 policy、adapter 或 compatibility boundary。证明模块责任可一句话说明，调用者少知道步骤与顺序。

## Principle 4 — Unidirectional Policy Dependency

**Rule**：源码依赖为 `policy → contract ← implementation`；implementation 不能反向定义或控制 policy。

**Signals**

- core/domain/common/Harness import、构造或 switch 具体 provider、场景或基础设施；
- 通用模块依赖具体 Application workflow，或双方互相依赖；
- contract 由 implementation package 定义；
- callback、global state、service locator 或 registry 让底层决定上层流程。

**Consequence**

易变 detail 获得 policy 控制权，实现和场景变化扩散到稳定层。

**Guards**

- composition root 可以知道具体实现；
- adapter 可以同时依赖 domain contract 与外部系统；
- 稳定领域类型可以是具体类型；
- event/result 可以向上报告，但底层不能拥有上层目标和路由。

**Design / proof**

由稳定 policy 定义 capability contract；implementation 朝 contract 提供能力；构造和选择留在 composition 一侧。证明实现替换不修改 policy，且至少一条反向或循环依赖消失。

## Grill

对设计逐项寻找反证：

- **Reality** — 代码、调用、测试、配置、ADR 或兼容事实是否反驳业务判断；
- **Difference** — 是否把本质差异消掉，或把历史差异永久化；
- **Abstraction** — 是否是 union interface、mode flag 或 speculative seam；
- **Cohesion** — 是否过度拆分，或继续让调用者组装完整能力；
- **Dependency** — 类型箭头改变后，运行控制是否仍然反向；
- **Migration** — 新结构是否能渐进进入，旧结构是否有真实退出条件；
- **Complexity** — 复杂度是否只是转移到 helper、adapter、配置、registry 或调用者；
- **Deletion** — `Delete` 是否具体、可观察且最终不再 load-bearing。

挑战失败时修改、缩小或撤销设计，不增加第二个推荐方案来逃避结论。

## Gate — Real Evolution

拒绝以下伪演化：

- 不同业务被强行塞进同一抽象；
- 新 wrapper/interface/manager/registry 与旧 canonical path 并存；
- 复杂度只转移位置；
- 类型依赖倒置，但隐式控制方向未变；
- 没有任何旧业务路径、抽象、调用者知识、重复判断或无效依赖消失。

临时双轨必须声明 authoritative path、迁移证据、删除条件和最大 residual boundary。

每个 `Design ready` 必须写：

```text
Keep / Move / Merge / Delete / Do not change
```

新结构必须替代旧结构，而不是遮住它。
