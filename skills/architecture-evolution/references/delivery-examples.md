# AE 交付示例与反例

只在 Target judgment 已成立、AE 已建立 Current → Target gap 后，Program / 交付形状仍容易漂移，或候选 evolution 看起来“更 AI-native”但可能只是平台化、加层或 complexity relocation 时按需读取。

本文件只提供表达示例，不定义新的 runtime phase、schema、Decision Ledger 或必填字段。

## 一个稳定但非固定的交付形状

```text
Intent / structural pressure
  ↓
Current architecture reality
  ↓
Target Architecture
  - capability / responsibility / knowledge ownership
  - justified boundary / variation
  - stable dependency direction
  ↓
Current → Target gap
  ↓
Evolution Program
  - structural moves
  - real exits
  - migration boundary
  ↓
Evidence obligations
```

这只是可读性顺序。局部判断可以只给局部结论；no-evolution 可以直接说明 current reality 为什么已经满足 Target；Human-owned fork 可以停在 Evidence + recommendation + decision surface。

## 反例：把 AI-native 误做成“大平台化”

Current reality：`ModelManager` 同时承担 model semantics、runtime selection 与历史配置拼装；多个 caller 直接知道 runtime 类型和 backend-specific config。resource scheduling 已有独立 authority / lifecycle。

看起来整洁但错误的 Target：新增 `ModelPlatform + BaseModel + Registry + RuntimeProvider + Facade`，但 caller 仍选 runtime，旧 manager 仍是 config/lifecycle authority，resource owner 又被吞进 platform，新增模型仍跨多个 owner 修改。

失败原因：

1. responsibility / knowledge ownership 没归位；
2. old authority 没 real exit；
3. 独立 lifecycle 被错误合并；
4. layer/provider 没减少代表性 change 的 judgment/change/verification propagation；
5. `$replay` green 只能证明对应 behavior/compatibility claim，不能证明 architecture gain。

更可信的方向：Target judgment 先让 model capability 隐藏 model-specific semantics、runtime selection 与 backend config；只有 runtime 确有稳定 variation 才形成内部 provider boundary；resource owner 保持独立。AE 再从 current reality 选择 caller knowledge exit、old manager authority exit 等少量 structural moves，而不是先规定必须存在某组 class / registry / facade。
