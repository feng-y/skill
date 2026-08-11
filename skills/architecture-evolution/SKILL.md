---
name: architecture-evolution
description: 用于架构方向模糊、历史系统持续演进或“下一刀应该改什么”这类输入：从真实 change pressure 和 repo reality 中比较 materially different 的架构方向，收敛一个可长期成立且可渐进演进的 Architecture Decision，并编译成可持续推进的 Architecture Program。局部修复、实现方案已明确或只需要执行计划时不使用。
---

# Architecture Evolution · 从现实约束收敛 Architecture Decision

North Star：**从真实 change pressure、系统现实和稳定约束中判断系统应如何分层、组织、抽象并演进，必要时比较 materially different 的架构方向，收敛 Target Architecture，并把它编译成少量可真实改善结构的推进点。**

本 Skill 可以完成 Target Architecture：稳定的 layer / dependency、module responsibility、abstraction / specific boundary，以及必要的 authority、control、lifecycle 与 variation boundary；不完成 Implementation Design，不规定 class/API/file、具体调用实现、任务拆分或验证套餐。

## Context loading

1. 本文件只负责 stance、适用边界、research/compile boundary 和终态；
2. 需要 architecture judgement 时读 [rules.md](references/rules.md)；
3. 遇到历史 mode、compat、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时按需读 [legacy-lenses.md](references/legacy-lenses.md)；
4. 当前方案局部都合理但整体概念变多，或 conceptual integrity / essential-vs-accidental complexity / complexity relocation 难以判断时，按需读 [brooks-constraints.md](references/brooks-constraints.md)；
5. architecture decision 收敛后读 [decision-contract.md](references/decision-contract.md) 完成 Compile；
6. [validation.md](references/validation.md) 只用于显式 smoke/eval，正常运行不读。

## 何时使用

使用：架构方向仍模糊；历史系统出现重复 change pressure、跨边界知识泄漏、长期兼容负担、依赖/控制反转，或需要判断多个可能架构方向与渐进演进路径。

跳过：局部 bug、机械迁移、明确 code review；Target Architecture 已稳定只差 Implementation Design / execution；只有审美不满而没有真实 pressure。

## Research topology

默认锚定用户指定模块，不做全 repo architecture scan。先看该模块的真实职责与直接 upstream / downstream，从行为和依赖重新识别它实际提供或参与的 capability；**现有 module 名称和 provider taxonomy 只是 evidence，不是边界答案。**

识别 capability 后重新判断 boundary：哪些 responsibility 属于 capability，哪些属于 caller / adjacent subsystem，哪些是 stable common，哪些是 specific。随后重新识别真正的 provider / variation boundary，并只沿会改变 architecture judgement 的 provider 逐个展开 semantics、input/output、lifecycle、state、performance/deployment constraint 等 decisive difference。

只有当局部边界无法关闭 authority/SOT、serialized/config identity、repo 外 contract 或其他会改变 Target Architecture 的 constraint 时，才做 targeted wider search；Research 深度本身不是价值。

## Architecture stance

Architecture judgement 主要落在五件事：**清晰分层与单向依赖、模块内聚与简洁组织、abstraction 与 specific 的取舍、primary 与 auxiliary responsibility 的主次、旧复杂度是否真实退出。**

`change locality / knowledge / SOT / control / lifecycle / variation / complexity relocation` 只是帮助判断这五件事的 evidence，不要求逐项分析或输出。不要因为看到第一个合理 shape 就停止，也不要为了“比较方案”制造表面不同的假 alternatives；只有 materially different 的 architecture fork 才需要展开。

Target Architecture 可以决定长期 architecture boundary 与 owner，但不能把这些判断偷换成某种代码 representation。若两个 materially different 的 Target Architecture 都满足核心架构判断，却没有足够 reality 判断为什么选其中一个，保持 unresolved，而不是把第一个 plausible shape 当结论。

Architecture Evolution 必须说明真正的结构退出与 architecture-level transition；temporary complexity 必须有明确 architecture purpose 和 exit condition。它不是 implementation task list。

## Compile

Architecture reasoning 可以很大，最终交付必须很薄。`Architecture decision ready` 只有在 Target Architecture 已稳定，并且能编译出至少一个**实际改善结构**的 Architecture Improvement 时成立。

Improvement 不是 research question、知识补全、未来愿望或 implementation task。它完成后必须让至少一个核心架构判断可观察地变好，并让某个旧 knowledge / authority / dependency / special path / accidental complexity 真实退出或停止 authoritative，同时有明确 done condition。最多保留 3 个最高价值 improvement；不足 3 个时不补数。

推进路线只表达这些 improvement 之间真实的 architecture dependency；没有依赖就允许并行，不为 roadmap 制造顺序。

## Output

只返回一个状态：

- **`Status: No architecture evolution`** — 当前 pressure 不构成 architecture problem，或保持局部修改更合理；
- **`Status: Architecture unresolved`** — 一个 Material Unknown / Human decision，或 materially different architecture fork 仍缺少足以裁决的 evidence；也包括当前还无法形成实际 architecture improvement 的情况；
- **`Status: Architecture decision ready`** — Target Architecture 已稳定，并已 Compile 成可推进的 Architecture Program，可以进入 Implementation Design / execution。

最终输出跟随用户主要语言；代码符号、文件名和稳定协议名称可以保留原文。
