---
name: architecture-evolution
description: 用于架构方向模糊、历史系统持续演进或“下一刀应该改什么”这类输入：从真实 change pressure 和 repo reality 中重建关键 architecture forces，比较 materially different 的架构方向，收敛一个可长期成立且可渐进演进的 Architecture Decision。局部修复、实现方案已明确或只需要执行计划时不使用。
---

# Architecture Evolution · 从现实约束收敛 Architecture Decision

North Star：**从真实 change pressure、系统现实和稳定约束中，重建关键 architecture forces，探索 materially different 的架构方向，比较复杂度与演进代价，收敛一个可长期成立且可渐进迁移的 Architecture Decision。**

本 Skill 可以完成 Target Architecture：稳定的 responsibility、knowledge、authority、control、lifecycle、dependency 与 essential variation boundary；不完成 Implementation Design，不规定 class/API/file、具体调用实现、任务拆分或验证套餐。

## Context loading

1. 本文件只负责 stance、适用边界和终态；
2. 需要 architecture judgement 时读 [rules.md](references/rules.md)；
3. 遇到历史 mode、compat、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时按需读 [legacy-lenses.md](references/legacy-lenses.md)；
4. 只有当前方案的 complexity relocation / conceptual integrity 难以判断时，按需读 [brooks-constraints.md](references/brooks-constraints.md)；
5. architecture decision 收敛后读 [decision-contract.md](references/decision-contract.md) 输出；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行不读。

## 何时使用

使用：架构方向仍模糊；历史系统出现重复 change pressure、跨边界知识泄漏、长期兼容负担、依赖/控制反转，或需要判断多个可能架构方向与渐进演进路径。

跳过：局部 bug、机械迁移、明确 code review；Target Architecture 已稳定只差 Implementation Design / execution；只有审美不满而没有真实 pressure。

## Architecture stance

先恢复足以改变架构判断的 reality，不把 Research 深度本身当价值。最小 architecture model 只保留与当前 decision 有关的 responsibility、authority / SOT、knowledge、control / lifecycle、dependency、variation 和 change-pressure 关系。

Architecture vs local、forces、design space、trade-off、complexity relocation 与 evolution judgement 由 `rules.md` 决定。不要因为看到第一个合理 shape 就停止，也不要为了“比较方案”制造表面不同的假 alternatives；只有 materially different 的 architecture fork 才需要展开。

Target Architecture 可以决定长期 architecture boundary 与 owner，但不能把这些判断偷换成某种代码 representation。若两个 materially different 的 Target Architecture 都能满足当前 outcome，却没有足够 forces 判断为什么选其中一个，保持 unresolved，而不是把第一个 plausible shape 当结论。

Architecture Evolution 必须说明真正的结构退出与 architecture-level transition：什么 authority / knowledge / control / dependency 被建立、迁移或退休，什么 temporary complexity 必须有明确退出条件。它不是 implementation task list。

## Output

只返回一个状态：

- **`Status: No architecture evolution`** — 当前 pressure 不构成 architecture problem，或保持局部修改更合理；
- **`Status: Architecture unresolved`** — 一个 Material Unknown / Human decision，或 materially different architecture fork 仍缺少足以裁决的 forces；
- **`Status: Architecture decision ready`** — Target Architecture、关键 trade-off、boundary 与 architecture-level evolution 已足够稳定，可以进入 Implementation Design / execution。

最终输出跟随用户主要语言；代码符号、文件名和稳定协议名称可以保留原文。
