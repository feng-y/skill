# Architecture Evolution Rules

只在已经出现结构候选时读取。一次只选一个主要违反点。

固定判断链：

```text
Signals → Diagnosis → Counterexample → Design move → Improvement proof
```

Signal 不是结论；设计模式也不是结论。

## Rule 1 — 一个责任或变化维度只有一个 owner

**Signals**

- 同类需求反复修改固定的一组模块；
- provider/family/mode 判断散落多处；
- 同一配置、状态、能力或业务事实被多次解释；
- 多条路径可能对同一事实得出不同结果。

**Diagnosis**

责任、事实或变化维度没有 authoritative owner，多个局部模块都在解释它。

**Counterexample**

相似语法可能承担不同责任，例如外部格式解析、输入校验、运行时选择和标签上报。必须先说明谁拥有事实，其他位置只是 projection 或 guard。

**Design move**

为该责任或变化维度指定一个 owner；其他模块消费稳定结果、capability 或 metadata，不再重复解释。只抽公共 helper、enum 或 registry 名单，但保留分散判断，不算解决。

**Improvement proof**

解释位置减少；新增一个代表性 variant 只修改 owner 和必要 adapter；冲突事实源消失。

## Rule 2 — 稳定主流程不依赖易变实现细节

**Signals**

- core flow import、构造或判断具体实现；
- 公共 contract 暴露 provider 专属配置、类型或生命周期；
- common 模块依赖场景模块，或双方互相依赖；
- 替换实现必须修改稳定执行流程。

**Diagnosis**

依赖方向跟随当前文件布局或构造顺序，而不是稳定性与责任；易变细节泄漏进稳定路径。

**Counterexample**

具体类型可能本身就是稳定领域 contract；单一且完全内部的实现不一定需要 seam；性能关键路径可以使用具体表示，但必须局部、显式且不向调用者扩散。

**Design move**

从稳定消费者的需要定义 contract；实现选择、构造和专属配置留在实现 owner 一侧。只有真实 variation、生产/测试 adapter 或当前替代需求证明 seam 有价值时才引入 seam。

**Improvement proof**

新增或替换实现不修改稳定主流程；core 不再知道具体类型；依赖变成单向，且没有新增透传层。

## Rule 3 — 模块隐藏复杂度，调用者不重组能力

**Signals**

- wrapper 基本一对一透传；
- 调用者必须按隐含顺序调用多个方法；
- 调用者自行拼装 config、state、runtime、type 或 adapter；
- 测试重复内部编排或穿透私有状态；
- interface 复杂度接近 implementation。

**Diagnosis**

seam 围绕文件或类，而不是一项完整能力；复杂度被暴露或搬家，没有被隐藏。

**Counterexample**

小型纯函数可以拥有完整 contract；外部 transport adapter 可以很薄；有时编排确实属于更高层 owner。行数不是 depth。

使用 deletion test：删除模块后，如果只是少一层间接调用，它可能是浅模块；如果必要知识重新散回多个调用者，它才在创造 leverage。

**Design move**

围绕调用者真正需要的完整能力放置 seam，把顺序、状态迁移、校验和错误转换收进模块；缩小公开方法、参数和特殊入口；合并浅模块或删除 middle man。

**Improvement proof**

调用者需要的步骤和概念减少；测试通过同一个 seam 验证可观察行为；复杂度集中而非转移。

## Rule 4 — 独立变化原因具有独立责任边界

**Signals**

一个模块混合多种独立变化原因，例如：

- 业务语义；
- 输入适配或序列化；
- provider 选择与构造；
- metrics、tracing、debug；
- cache、batch、内存或延迟优化；
- compatibility fallback；
- runtime lifecycle 与资源 owner。

不同需求总是修改模块中互不相关的区域，或需要不同验证与 owner。

**Diagnosis**

模块边界跟随执行顺序或历史堆积，而不是一个连贯的 reason to change；主责任与辅助责任被错误绑定。

**Counterexample**

不要把每个 concern 升级成 public module。观测和优化可以是主能力的私有 collaborator；为了同一个 invariant 必须共同变化的步骤仍然是内聚的；文件大不是证据。

**Design move**

先用一句话定义主责任。其余内容分类为 intrinsic behavior、internal implementation、adapter、observer、policy、compatibility boundary 或 removable history。优先私有组合，只拆真实独立的 owner、生命周期或验证边界。

**Improvement proof**

主 owner 不再需要“同时还负责”；辅助逻辑不参与业务决策；无关变化不再修改同一责任面。

## Design Gate — Replace, not layer

`Design ready` 只有在减少现有负担时才成立。

拒绝：

- 新 wrapper/interface/manager 与旧 canonical path 并存；
- registry 只集中名字，判断仍然散落；
- 目标文件变小，但复杂度转移到 helper 或调用者；
- 只有假想未来收益，今天没有任何知识、重复判断、无效依赖或历史路径消失。

临时双轨只在以下内容明确时允许：当前 authoritative path、迁移证据、删除条件和最大 residual boundary。

每个 `Design ready` 必须写：

```text
Keep / Move / Merge / Delete / Do not change
```

至少一个具体负担必须消失；新 seam 必须替代旧结构，而不是遮住它。
