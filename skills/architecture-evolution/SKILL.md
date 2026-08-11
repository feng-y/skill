---
name: architecture-evolution
description: 用于架构方向模糊、历史模块持续演进或“下一刀应该改什么”这类输入：从真实 repo reality 收敛 Target Architecture，并编译成少量可持续推进的 Architecture Improvements。局部修复、Target Architecture 已明确或只需执行计划时不使用。
---

# Architecture Evolution

North Star：**从真实 change pressure 与稳定约束中收敛更清晰、简单、可演进的 Target Architecture，并把它编译成少量真实改善结构的推进点。**

AE 可以决定长期 architecture boundary 与 architecture-level evolution；不完成具体 class/API/file、调用实现、任务拆分或验证设计。

## Context

- 需要 architecture judgement 时读 [rules.md](references/rules.md)。
- 历史 mode、compat、旧 config/registration、serialized/provider identity 可能改变 retirement 判断时，按需读 [legacy-lenses.md](references/legacy-lenses.md)。
- proposal 局部合理但整体概念膨胀，或 essential/accidental complexity 难判时，按需读 [brooks-constraints.md](references/brooks-constraints.md)。
- Target Architecture 收敛后读 [program-contract.md](references/program-contract.md) Compile；[validation.md](references/validation.md) 只用于显式 eval。

## Research boundary

默认从用户指定模块开始，只沿直接 upstream/downstream 与会改变 architecture decision 的边界展开；从真实 responsibility 重新识别 capability 与 stable variation，不接受现有 module/provider taxonomy 作为答案。只有局部无法关闭 decision-changing 的 authority/SOT/identity/external constraint 时才扩大搜索。

## Status

- **`Status: No architecture evolution`** — pressure 保持 local 更合理。
- **`Status: Architecture unresolved`** — 仍有会改变 Target Architecture / architecture-level evolution 的 Material Unknown，或还无法形成真实 structural improvement。
- **`Status: Architecture decision ready`** — Target Architecture 已稳定，并能 Compile 出至少一个 independently improving Architecture Improvement；随后进入 Implementation Design / execution。
