# AE 交付示例与反例

只在已经完成主 Skill 的 Goal pressure / Strategic Design 判断后，交付形状仍容易漂移，或候选 Target 看起来“更 AI-native”但可能只是平台化、加层或 complexity relocation 时按需读取。

本文件只提供表达示例，不定义新的 runtime phase、输出 schema、Architecture Contract 或必填字段。实际交付只保留当前判断需要的部分；没有 Evidence 支持的 capability / layer / provider 不为了填模板而补齐。

## 一个稳定但非固定的交付形状

典型交付可以按下面的语义顺序展开：

```text
Goal / Goal set
  ↓
Architecture change pressure
  ↓
Current architecture constraint
  ↓
Target Architecture
  - capability / responsibility
  - module boundary / cohesion
  - justified internal variation / layering
  - stable dependency direction
  - expected reasoning / change / verification locality
  ↓
Current Program
  - structural moves
  - real exit
  - migration boundary
  ↓
Evidence
  - architecture evidence
  - behavior evidence
```

这只是可读性顺序。局部判断可以只给局部结论；no-evolution 可以直接说明当前 boundary 为什么已经能吸收 Goal；Human-owned fork 可以停在 Evidence + recommendation + decision surface。

## 反例：把 AI-native 误做成“大平台化”

### Goal

- 支持更多模型类型接入；
- 新模型尽量少改调用方；
- runtime 实现未来可能替换。

### Current reality

`ModelManager` 同时承担部分 model semantics、runtime selection 与历史配置拼装；多个 caller 直接知道 runtime 类型和配置细节。资源调度已有独立 authority / lifecycle，并不属于 model capability。

### 看起来合理但错误的 Target

新增一个 `ModelPlatform`，再统一增加：

- `BaseModel`；
- `ModelRegistry`；
- `RuntimeProvider`；
- `ModelFacade`。

但迁移后：

- caller 仍需要选择 runtime 并拼接 backend-specific config；
- 原 `ModelManager` 仍是旧配置和生命周期路径的 authority；
- `ModelPlatform` 又把独立的 resource owner 吞进自己的 lifecycle；
- 新增模型仍需同时修改 caller、旧 manager、registry 和 resource glue；
- replay 可以通过，但旧 dependency / authority 没有退出。

### 为什么失败

这不是高内聚低耦合，只是增加一层结构：

1. **没有完成 responsibility / knowledge ownership correction。** runtime selection 和 backend config 仍泄漏给 caller。
2. **没有 real exit。** 旧 manager / path 仍 authoritative，新 facade 只是并存。
3. **错误吞并独立责任。** resource authority 有独立语义和 lifecycle，不能为了“平台统一”并入 model owner。
4. **layer/provider 没有证明 change isolation。** abstraction 数量增加，但代表性 Goal 的 judgment / change / verification surface 没有缩小。
5. **behavior parity 不能证明 architecture improvement。** 测试通过只证明没有改坏。

### 更可信的演进方向

先从 Goal pressure 判断哪些长期知识应由 model capability 吸收：让 model owner 隐藏 model-specific semantics、runtime selection 与 backend-specific configuration；只有 runtime 确有稳定可替换 variation 时才形成内部 provider boundary。resource owner 保持独立，通过稳定 contract 与 model capability 形成可解释的单向关系。

当前 Program 应要求 caller-specific runtime/config knowledge 退出、旧 `ModelManager` 对应 authority 退出或归位，并用代表性“新增一种模型 / 替换一种 runtime”验证变化是否主要闭合在正确 owner，而不是先规定必须存在 `ModelPlatform`、`BaseModel`、registry 或 facade。
