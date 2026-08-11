# Architecture Reasoning Kernel

只在需要 architecture judgement 时读取。本文件拥有 Architecture Evolution 的核心判断；它不是固定推理流程，也不要求逐项输出。

架构原则保持少而稳定。`change pressure / knowledge / SOT / control / lifecycle / variation / complexity relocation` 用来证明或推翻架构判断，不与架构原则本身平级。

## Architecture or local

Architecture work 必须来自真实 structural pressure，而不是模式偏好。文件大、函数长、目录不整齐、switch/if 多或一次局部修改都只是 evidence。

如果一个局部修复就能消除 pressure，且不需要重新确定长期 layer / dependency、module responsibility、abstraction boundary、primary responsibility 或旧结构退出，就保持 local。

## Five architecture judgments

### Layering & dependency normativity

系统应有少量清晰、可解释的层与稳定单向依赖。上层 policy / business capability 不应被下层 provider、scenario 或 implementation 反向定义；common/core 不应知道 specific 场景。

Layer 是稳定 responsibility + dependency boundary，不是为了整齐增加目录层级。优先让架构能从 repo territory 直接被人和 Agent 读出，并在值得时由 structure / tooling 机械约束；不要靠长期口头约定维持依赖方向。

### Cohesion & simple organization

一个模块优先围绕一个主要 capability / responsibility 组织，拥有少量清楚入口，并把完成该责任必需的内部知识、状态与协作细节闭合在边界内。caller 不应为了使用 capability 重新拼 implementation identity、configuration interpretation、ordering、lifecycle 或其他内部事实。

抽象数量、manager/provider/helper/registry 层级本身不是价值。两个方案都正确时，优先概念更少、public surface 更小、repo 更容易解释和继续修改的结构。

### Abstraction vs specific

真正稳定的共同 semantics / invariant 才值得 abstraction；稳定且重要的差异应保持 specific。代码相似不证明应该统一，当前实现不同也不证明应该永久分开。

判断 variation 时优先看它是否长期改变 business semantics、precondition、output contract、consistency/lifecycle、performance architecture、deployment boundary 或其他稳定 invariant。provider 名称、class hierarchy、mode、consumer partition 和当前调用形状都只是 evidence。

对外 capability 应尽量表达独立、唯一的业务/工程语义，而不是暴露历史 implementation taxonomy；但一个 specific 若本身具有稳定独立语义，就应被直接承认，不为“通用”强行合并。

### Primary vs auxiliary responsibility

先确定模块真正的 primary responsibility surface；它决定主要 boundary、依赖和组织形态。metrics、debug/shadow、sampling、compat、fallback、cache、观测或局部性能优化只是常见的 auxiliary 候选，是否属于辅助责任必须由 capability semantics 和长期责任判断，不能由名字预设。被判定为 auxiliary 的 concern 应附着于主责任，而不是反过来塑造主架构。

不要为了未经证明的性能收益打穿 layering、cohesion 或 abstraction boundary。只有 profiling、SLA、resource constraint 或其他真实 evidence 证明性能会改变长期架构选择时，性能才升级为 architecture force；否则结构清晰、责任自然和长期可演进性优先。

### Real evolution

Architecture change 必须让旧复杂度真实退出，而不是增加一层后继续保留旧知识和旧路径。至少应能说明哪些 duplicate semantics / caller knowledge / reverse dependency / special branch / old authority / permanent compatibility 会停止 authoritative 或被删除。

`old A → new abstraction → old B` 默认只是 complexity relocation。temporary adapter / dual path / compat 若不可避免，必须有明确 architecture purpose 和 exit condition。

## Evidence lenses

只展开会改变上述五个判断的 evidence：

- **Change locality** — future change 为什么跨多个模块传播；用于判断 Cohesion / Abstraction 是否切错。
- **Knowledge reassembly** — caller 为完成责任必须知道什么内部事实；用于判断 Cohesion / Primary responsibility 是否泄漏。
- **Authority / SOT / control / lifecycle** — 谁定义事实、选择实现、驱动执行、拥有状态与生命周期；用于判断 Layering / Responsibility 是否清楚。不要因为这些责任相关就默认集中到同一 owner。
- **Variation evidence** — 差异是否由稳定 semantics / lifecycle / performance / deployment 证明；用于判断 Abstraction vs specific。
- **Complexity relocation** — 被删除的 complexity 去了哪里、由谁承担；用于判断是否发生 Real evolution。

一个 lens 干净不能替另一个作证：clean dependency graph 不等于模块内聚；单一 owner 不等于 abstraction 正确；统一 interface 不等于 specific variation 应消失。

## Architecture decision

先恢复足以改变上述判断的最小 current architecture model，不做无关 inventory。不要在第一个 plausible shape 上停止，但也不要为了完整性制造多个方案。

只有当 materially different architecture 改变长期 layering、module boundary、abstraction/specific boundary 或 primary responsibility placement 时才形成真实 design-space fork；命名、文件布局或同一 responsibility 的类层次不是不同 architecture。

真实 fork 的选择只围绕**哪些核心架构判断产生了实质 trade-off**。在满足稳定业务语义与必要约束的前提下，优先选择分层更清楚、模块更内聚、抽象更自然、主责任更突出、旧复杂度退出更多且整体组织更简单的结构。若 materially different Target Architecture 仍无法由真实 repo / runtime evidence 区分，保持 `Architecture unresolved`，不要按模式偏好强选。

需要经典架构约束辅助判断时按需读 `brooks-constraints.md`；它只能帮助区分上述 trade-off，不成为另一套 architecture taxonomy。

## Target Architecture altitude

AE 可以固定长期 layer / dependency、module responsibility、capability boundary、authority/SOT、knowledge/control/lifecycle direction、essential variation 与 architecture-level acceptance。

AE 不因 model preference 固定具体 class、API、file、helper、flag/metadata schema、虚函数形式、调用实现、migration task 或 lint/test/provider 套餐。只有 Human/repo authority 或不可替代技术约束使某种 representation 本身成为 invariant 时才例外。

## Architecture evolution

Architecture Decision 不能只有目标状态，还要说明 architecture 如何从 current 进入 target，但只表达结构依赖：先建立什么 boundary / authority，哪些旧 knowledge / dependency / path 随后才能退出，temporary complexity 的 purpose / exit 是什么，以及哪些 transition 会形成长期 lock-in。

它不是文件修改顺序、MR 拆分、测试命令或发布计划。若 transition 只能靠永久 dual authority / adapter 才成立，或最终结构比当前更难解释，decision 尚未成立。

## Material Unknown & evidence lifetime

只有会改变 architecture vs local、五个核心判断、Target Architecture 或 architecture-level evolution 的 unknown 才是 Material Unknown。

```text
Claim at risk → Minimal probe / Human decision → Evidence → Decision changed / retained
```

能从 repo/runtime reality 关闭就先 probe；真正属于 Human-owned 的业务、兼容、风险或长期承诺才 Ask。不会改变 architecture decision 的 unknown 留给 Implementation Design / execution。

同一事实或 judgment 只保留一份 current authoritative state。新 authoritative evidence 改变前提时，只重新判断受影响的 architecture conclusion；不要保留新旧两份 active truth，也不要为了保住旧结论新增 guard。