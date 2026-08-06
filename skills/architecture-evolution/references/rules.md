# Architecture Evolution Principles

只在确认存在结构候选后读取。一次只选一个 `Primary architecture break`。

```text
Evidence → Consequence → Primary break → Root cause → Counterexample → Design → Proof
```

如果无法判断两条路径是不是同一业务，先返回 `Research required`。

## Primary selection

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

**Consequence / diagnosis**

系统没有唯一 canonical semantics，调用者和测试必须知道“走哪条路径”；或者不同业务被错误压进一个模糊概念。

**Guards**

- 不同 bounded context、invariant、一致性、错误或生命周期可以保持独立；
- 迁移期双轨必须声明 authoritative path 和退出条件；
- 代码相似不是业务相同的证据。

**Design**

定义 canonical business capability 与共同 input/output/error/invariant/lifecycle；将本质差异显式化，删除偶然差异、重复解释和平行 canonical path。

**Proof**

同一业务只有一个标准定义；代表性场景语义一致；一条业务规则只修改一处；不同业务仍可清楚区分。

## Principle 2 — Stable Abstraction with Explicit Variation

**Rule**：共同语义由一个稳定抽象承载，本质差异只存在于明确 variation point。

**Signals**

- 公共 interface 是历史字段和方法的并集；
- mode flag、optional provider config 或外部 switch 泄漏给调用者；
- 新增实现必须修改稳定 flow 和多个调用者；
- facade/base/registry 外面统一，内部仍保留多套判断和特殊入口。

**Consequence / diagnosis**

调用者依赖实现差异而不是业务能力；抽象只统一形状，没有统一语义。

**Guards**

- 单一内部实现不一定需要 seam；
- external protocol 或 closed enum 上的 switch 可以合理；
- thin adapter 如果真实吸收外部变化，可以保留；
- 性能具体表示必须局部且不外泄。

**Design**

从 canonical capability 定义 stable contract；明确 variation、owner 与专属配置；调用者只依赖 capability；合并重复抽象并删除外部 switch 和特殊入口。

**Proof**

新增或替换一个 variation 不修改稳定 flow；公共 contract 不含实现并集；调用者不再选择或拼装实现；至少一个旧抽象或入口退出。

## Principle 3 — Cohesive Capability Ownership

**Rule**：一个模块拥有一项完整能力及其 invariant、状态和生命周期。

**Signals**

- 模块混合业务、provider 选择、metrics/debug、cache、compatibility 和资源生命周期；
- 主责任必须用“同时还负责”才能描述；
- 状态和生命周期散落在 manager、helper 或全局对象；
- wrapper 透传，调用者和测试在外部重组顺序与行为。

**Consequence / diagnosis**

无关变化互相影响，关键 invariant 没有完整 owner，复杂度泄漏到调用者和测试。

**Guards**

- observer、cache 和优化可以是 private collaborator；
- 为同一 invariant 共同变化的步骤仍然内聚；
- composition root 的编排与高 fan-out 可以合理；
- 文件大或函数长不是架构结论。

使用 deletion test：删除模块后，复杂度若只消失，它可能是壳；必要知识若散回多个调用者，它才在创造 leverage。

**Design**

定义完整 capability；收回 invariant、状态、生命周期、错误转换和必要顺序；只分离真实独立的 policy、adapter 或 compatibility boundary；合并浅模块并缩小公开面。

**Proof**

模块责任可一句话说明；状态与生命周期有明确 owner；调用者少知道步骤和顺序；独立变化不再修改同一责任面。

## Principle 4 — Unidirectional Policy Dependency

**Rule**：policy 依赖稳定 capability，implementation 不能反向定义或控制 policy。

**Signals**

- core/domain/common/Harness import、构造或 switch 具体 provider、场景或基础设施；
- 通用模块依赖具体 Application workflow，或双方互相依赖；
- contract 由 implementation package 定义；
- callback、global state、service locator 或 registry 让底层决定上层流程。

**Consequence / diagnosis**

易变 detail 获得 policy 控制权，实现和场景变化会扩散到稳定层。

**Guards**

- composition root 可以知道具体实现；
- adapter 可以同时依赖 domain contract 与外部系统；
- 稳定领域类型可以是具体类型；
- event/result 可以向上报告，但底层不能拥有上层目标和路由。

**Design**

由稳定 policy 定义 capability contract；implementation 朝 contract 提供能力；构造和选择留在 composition/implementation 一侧；用 result/evidence/event 上报；删除 common→scenario、policy→provider 等 forbidden edge。

**Proof**

实现替换不修改 policy；通用 Harness/Runtime 不知道具体 Application workflow；contract 不再由易变实现拥有；至少一条反向或循环依赖消失。

## Gate — Real Evolution

拒绝以下伪演化：

- 不同业务被强行塞进同一抽象；
- union interface、mode flag 或 optional 参数只包住旧语义；
- 新 wrapper/interface/manager/registry 与旧 canonical path 并存；
- 复杂度转移到 helper、adapter 或调用者；
- 类型依赖倒置，但 callback/global state 继续反向控制；
- 没有任何旧业务路径、抽象、调用者知识、重复判断或无效依赖消失。

临时双轨必须声明 authoritative path、迁移证据、删除条件和最大 residual boundary。

每个 `Design ready` 必须写：

```text
Keep / Move / Merge / Delete / Do not change
```

新结构必须替代旧结构，而不是遮住它。
