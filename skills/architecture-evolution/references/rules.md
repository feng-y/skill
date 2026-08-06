# Architecture Evolution Principles

只在已经出现结构候选时读取。一次只选择一个 `Primary architecture break`，其余命中项作为 consequence 或 secondary signal。

固定判断链：

```text
Signals → Structural consequence → Diagnosis → Counterexample → Design move → Improvement proof
```

Signal 不是结论；复用、抽象、分层和设计模式也不是结论。

## Primary break selection

按业务到结构的顺序选择最接近根因的一条：

1. **同一业务存在多套语义或事实解释** → Principle 1；
2. **业务语义可统一，但实现差异泄漏进公共 contract 或稳定流程** → Principle 2；
3. **能力、状态和 invariant 被混合或拆散，模块不内聚** → Principle 3；
4. **业务 policy 与实现 detail 的依赖或控制方向反转** → Principle 4。

如果无法判断两条路径是不是同一业务，先返回 `Research required`，不要跳到抽象设计。

## Principle 1 — Business Semantic Integrity

**Rule**

同一业务语义必须统一；不同业务语义必须显式区分。

**Signals**

- 相同业务触发在不同入口、family、provider 或历史模块中走不同主流程；
- 同一输入在不同路径产生不同输出、错误、状态或副作用；
- 同一配置、能力或业务事实被多次解释；
- 相同概念使用不同名称，或不同概念被同一个通用名称掩盖；
- 修改一个业务规则必须同步多套平行实现。

**Structural consequence**

系统没有唯一 canonical semantics。调用者、测试和维护者必须知道“走哪条路径”，业务变更会产生语义漂移和同步成本。

**Diagnosis**

同一业务被历史结构拆成多套解释，或不同业务被错误压进一个模糊概念。

**Counterexample**

不要因为代码相似就统一：

- 不同 bounded context 可以有相似但独立的模型；
- 相同输入形态可能对应不同一致性、错误或生命周期语义；
- 外部协议适配与内部业务解释可以有意分离；
- 迁移期双轨可以暂时存在，但必须有 authoritative path 和退出条件。

必须明确哪些语义相同、哪些差异属于业务本身。

**Design move**

- 定义一个 `Canonical business capability`；
- 固定共同输入、输出、错误、invariant、状态与生命周期；
- 将本质差异写成显式业务规则或 variation；
- 删除偶然差异、重复事实解释和平行 canonical path；
- 统一业务语言，不让目录、数据库表或 provider 名称反向定义业务。

**Improvement proof**

- 同一业务只有一个标准定义和主流程；
- 代表性场景在所有入口具有一致语义；
- 一个业务规则只修改一处 canonical interpretation；
- 不同业务的差异仍然清楚、可验证。

## Principle 2 — Stable Abstraction with Explicit Variation

**Rule**

共同业务语义由一个稳定抽象承载；本质差异只存在于明确 variation point。

**Signals**

- 公共 interface 是历史实现字段和方法的并集；
- mode flag、optional 参数、provider config 或类型判断出现在调用者和稳定流程；
- 新增一个实现必须修改 factory、executor、parser、metrics 和多个调用者；
- 新 facade、base class 或 registry 外面统一，内部仍保留多套 switch；
- 同一能力存在多个相互重叠的抽象或特殊入口。

**Structural consequence**

调用者依赖实现差异而不是业务能力；新 variation 会修改稳定代码，抽象只统一形状，没有统一语义。

**Diagnosis**

稳定 contract 未从共同业务需要中抽取，或抽象忠实复制了历史实现差异。

**Counterexample**

- 单一、稳定且完全内部的实现不一定需要抽象；
- 外部协议或 closed enum 上的 switch 可以合理；
- thin adapter 如果真正吸收 vendor churn，可以有价值；
- 性能关键路径可以使用具体表示，但必须局部且不向调用者扩散。

“有 interface”不是成功标准；真实 variation 能否被局部替换才是。

**Design move**

- 从 canonical business capability 定义稳定 contract；
- 明确每个 variation point、owner、输入和输出；
- 将 provider/family 专属配置、构造和生命周期留在 variation 内部；
- 调用者只依赖 capability，不依赖实现类型和组合顺序；
- 合并重复抽象，删除特殊入口和外部 switch。

**Improvement proof**

- 新增或替换一个代表性 variation 不修改稳定主流程；
- 公共 contract 不再包含实现专属字段；
- 调用者不再选择、构造或拼装具体实现；
- 至少一个旧抽象、switch 或入口退出。

## Principle 3 — Cohesive Capability Ownership

**Rule**

一个模块拥有一项完整能力及其 invariant、状态和生命周期；独立变化原因不应错误绑定，完整能力也不应拆散给调用者组装。

**Signals**

- 一个模块同时承担业务语义、provider 选择、metrics、debug、cache、compatibility 和资源生命周期；
- 主责任无法用一句话表达，必须连续使用“同时还负责”；
- 状态和生命周期散落在多个 manager、helper 或全局对象；
- wrapper 一对一透传，调用者必须按隐含顺序调用多个方法；
- 测试重复内部编排或穿透私有状态；
- 完整能力被拆成多个浅模块，最终由调用者重新组装。

**Structural consequence**

无关变化互相影响，关键 invariant 没有完整 owner；复杂度没有被模块吸收，而是泄漏到调用者和测试。

**Diagnosis**

模块边界跟随历史文件、执行顺序或技术 concern，而不是一项完整 capability 及其 reason to change。

**Counterexample**

- 不要把每个 concern 都升级成 public module；
- metrics、cache 和优化可以是主能力的 private collaborator；
- 为同一 invariant 必须共同变化的多个步骤仍然内聚；
- composition root 的编排和高 fan-out 可以合理；
- 文件大、函数长或代码复杂不是单独的架构证据。

使用 deletion test：删除模块后，如果只是少一层间接调用，它可能是壳；如果必要知识重新散回多个调用者，它才在创造 leverage。

**Design move**

- 用一句话定义完整 capability；
- 将 invariant、状态、生命周期、错误转换和必要顺序放入同一 owner；
- 将独立 policy、adapter、observer 或 compatibility boundary 分离；
- 辅助能力优先保持 private composition；
- 合并浅模块，缩小公开方法、参数和特殊入口。

**Improvement proof**

- 模块主责任无需“同时还负责”；
- 状态和生命周期具有明确 owner；
- 调用者需要的步骤、概念和顺序减少；
- 独立变化不再修改同一责任面；
- 测试通过调用者使用的同一 capability seam 验证行为。

## Principle 4 — Unidirectional Policy Dependency

**Rule**

业务 policy 依赖稳定 capability；具体实现、基础设施和辅助机制不能反向定义或控制 policy。

**Signals**

- core/domain/common/Harness 层 import、构造或 switch 具体 provider、场景或基础设施；
- 通用模块依赖具体 Application workflow，或双方互相依赖；
- contract 由具体 implementation package 定义，稳定消费者被迫引用它；
- callback、global state、service locator 或 registry 让底层反向决定上层流程；
- observer、metrics、cache 或 compatibility 逻辑参与业务决策；
- 替换实现需要修改 policy 层。

**Structural consequence**

易变 detail 获得上层控制权；实现、部署和场景变化会扩散到稳定 policy，模块无法独立演化。

**Diagnosis**

依赖方向跟随构造顺序、目录布局或历史便利，而不是 policy/detail 与稳定性边界。

**Counterexample**

- composition root 可以知道具体实现；
- adapter 可以同时依赖 domain contract 和外部 infrastructure；
- 具体领域类型本身可以是稳定 contract；
- 性能关键表示可以被稳定层直接使用，但必须局部且显式；
- 事件和结果可以从底层上报，但不能让底层拥有上层目标和路由权。

**Design move**

- 从稳定 policy 的需要定义 capability contract；
- implementation 朝 contract 提供能力；
- 构造、选择和专属配置留在 composition/implementation 一侧；
- 用 result、evidence 或 event 向上报告，不用 callback/global state 反向接管流程；
- 删除 common→scenario、policy→provider 等 forbidden edge。

**Improvement proof**

- 依赖图和控制流方向一致、可解释；
- 实现替换不修改 policy；
- 通用 Harness/Runtime 不知道具体 Application workflow；
- contract 不再由易变实现拥有；
- 至少一条反向或循环依赖消失。

## Design Gate — Real Evolution

`Design ready` 只有在新设计统一业务并减少现有结构负担时才成立。

拒绝：

- 不同业务被强行塞进同一抽象；
- union interface、mode flag 或 optional 参数只是包住多套旧语义；
- 新 wrapper/interface/manager/registry 与旧 canonical path 并存；
- 文件变小，但复杂度转移到 helper、adapter 或调用者；
- 依赖在类型图上倒置，却通过 callback、global state 或配置重新反向控制；
- 只有假想未来收益，今天没有业务分支、旧抽象、调用者知识、重复判断或无效依赖消失。

临时双轨只在以下内容明确时允许：当前 authoritative path、迁移证据、删除条件和最大 residual boundary。

每个 `Design ready` 必须写：

```text
Keep / Move / Merge / Delete / Do not change
```

至少一个具体旧负担必须消失；新结构必须替代旧结构，而不是遮住它。
