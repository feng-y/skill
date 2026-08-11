---
name: architecture-evolution
description: 用于架构方向模糊、历史模块持续演进或“下一刀应该改什么”这类输入：从真实 repo reality 收敛 Target Architecture，并编译成少量可持续推进的 Architecture Improvements。局部修复、Target Architecture 已明确或只需执行计划时不使用。
---

# Architecture Evolution

North Star：**从真实 change pressure 与稳定约束中收敛更清晰、简单、可演进的 Target Architecture，并把它编译成少量真实改善结构的推进点。**

AE 可以决定长期 architecture boundary 与 architecture-level evolution；不完成具体 class/API/file、调用实现、任务拆分或验证设计。

## Context

- architecture judgement 读 [rules.md](references/rules.md)。
- 历史 mode、compat、旧 config/registration、serialized/provider identity 可能改变 retirement 判断时，按需读 [legacy-lenses.md](references/legacy-lenses.md)。
- proposal 局部合理但整体概念膨胀，或 essential/accidental complexity 难判时，按需读 [brooks-constraints.md](references/brooks-constraints.md)。
- Judge 已足够收敛时读 [program-contract.md](references/program-contract.md) Compile；[validation.md](references/validation.md) 只用于显式 eval。

## Flow

**1. Ground.** 从用户指定模块开始，只沿直接 upstream/downstream 与会改变 architecture decision 的边界展开；从真实 responsibility 重新识别 capability 与 stable variation，不接受现有 module/provider taxonomy 作为答案。只有局部无法关闭 decision-changing 的 authority/SOT/identity/external constraint 时才扩大搜索。

**2. Judge.** 用 `rules.md` 判断 architecture vs local，并收敛 best-known Target Architecture。若仍有会改变 Target Architecture / architecture-level evolution 的 Material Unknown，指出真正缺失的 evidence / Human decision，不拿 implementation 填空；若 pressure 保持 local 更合理，直接说明 local judgment 与理由。

**3. Compile.** Target Architecture 足够稳定时，用 `program-contract.md` 压成 Architecture Program；至少存在一个 independently improving Architecture Improvement 才值得交付 Program。不要把 research task、未来愿望或 implementation step 冒充推进点。

**4. Deliver.** 直接完整交付当前 Architecture Program；不输出 ready/completed status。任何 material Human clarification / correction 都从最高受影响步骤重新进入，使依赖结论 stale，并再次完整交付当前 outcome；之前交付过不构成 completion state，也不能抑制重新输出。
