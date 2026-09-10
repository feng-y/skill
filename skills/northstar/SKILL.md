---
name: northstar
description: 用于处理 Drafted Issue 或工程请求中仍无法局部关闭的困难 Intent、关键取舍与 material execution compile；已有执行约定与结果时独立验收。
---

# Northstar · 处理困难 Intent

Northstar 是 **optional difficult-intent compiler / outcome judge**，不是所有工程需求的默认入口。一个已经足以让 fresh Executor 理解 intended change、binding boundary 与 Acceptance 的 Drafted Issue 可以直接执行，不因为“流程完整”强制经过 Northstar。

Human 拥有 accepted result 与投入、兼容、长期维护、风险等 commitment；AE 负责长期结构判断；Executor 决定实现 How。已有 Drafted Issue 时，Northstar 只 enrich 这个 canonical intent，不重建第二份 intent/spec，也不拥有 tracker lifecycle 或 MultiCA 调度。

## 什么时候值得调用

只有直接 Issue 仍不足以安全开始时才扩大到 Northstar，典型包括：

- 多个合理解释会改变 accepted outcome、binding boundary 或长期 commitment；
- 事实已经足够，但仍存在 Human-owned material trade-off；
- material `Current → Target` delta / dependency 跨多个 cohesive outcome，关系本身会改变执行边界；
- 下游仍可能把“完成所提手段”误当成“解决原问题”；
- 已有复杂 execution contract / Taskbook 与结果需要独立 outcome judgment。

clear small / medium Issue 直接绕过 Northstar。

## Difficult intent judgment

从当前 authoritative request / Drafted Issue、Human correction 与 decision-relevant Evidence 开始，不重建已经成立的上下文，不把假设补成事实或授权。

`Goal` 只是可选 reasoning representation：只有它能实际改变 choice / boundary 或防止具体 Draft 偏离原问题时才显式恢复；`Problem + Draft + Constraint + Acceptance` 已足够时不制造同义 Goal。需要处理 framing、Human choice、Goal-vs-How 时按需读 [intent-shaping.md](references/intent-shaping.md)。

reality claim 需要 Evidence；只调查会改变 Intent judgment、material work、binding boundary、completion obligation 或 safe start 的事实。territory Unknown 交 `$unknowns-first`；长期结构问题交 `$architecture-evolution`；已理解 Intent 仍有 materially different concrete Target 时交 `$intent-shape`。只消费当前 decision 所需的结果，不替 Human 关闭 Human-owned choice。

## Material compile

只有 direct Issue 仍缺少必要 execution structure 时才 compile。优先把 durable Decision、material delta、coarse dependency 或 Acceptance enrich 回 canonical Issue；只有复杂度、下游访问边界或明确委托要求独立执行合同 / Taskbook 时才生成额外 artifact，且不复制第二份长期 Intent SOT。

`Current → Target` 只在能约束 material work 时显式建立。Task decomposition 不能负责发现或补完 Target；发现仍会改变 accepted result 的 Target ambiguity 就回到受影响的 shaping / Human decision。

复杂 material work / dependency 按 best-known complete Graph 判断，细节按需读 [execution-compile.md](references/execution-compile.md)；简单工作不显式造 Graph。Verification 按 outcome claim，而不是步骤或节点；只有存在具体 false-pass 风险时才读 [verification-trust.md](references/verification-trust.md)。

## 交付与停止

已有 Drafted Issue 时，只把后续 fresh consumer 必须知道的 durable Decision、Constraint、Draft correction、material relation 或 Acceptance fold back；阶段性 reasoning、progress 与普通 implementation How 不进入 Northstar 自己的第二份 SOT。下游无法访问 canonical source 时才复制最小必要 context 与出处。

已有 authoritative execution contract / Taskbook 与执行结果时，读 [outcome-judgment.md](references/outcome-judgment.md) 独立判卷。Human correction 或新 Evidence 只重开受影响判断及 dependency cone；Northstar 不持续监督 Executor / MultiCA，也不把 cohesive Issue 拆成 context-window-sized tickets。

当 fresh Executor 已能在 binding boundary 内安全开始、剩余未知只影响 implementation How 时停止。不要为了证明 Northstar“完成过流程”额外生成 Goal、Taskbook、Graph 或文件。
