---
name: northstar
description: 用于处理 Drafted Issue 或工程请求中仍无法局部关闭的困难 Intent、关键取舍与 material execution compile；已有执行约定与结果时独立验收。
---

# Northstar · 处理困难 Intent

Northstar 是 **difficult-intent compiler / outcome judge**，不是所有工程需求的默认入口。一个已经足以让 fresh Executor 正确理解 intended change、binding boundary 与 Acceptance 的 Drafted Issue，可以直接进入 Human、普通 agent 或 MultiCA；不因为“流程完整”强制经过 Northstar。

当存在多个 binding interpretation、Human-owned material trade-off、复杂 `Current → Target` delta / dependency Graph，或现有 Issue 仍不足以安全开始时，Northstar 才接管这部分困难 judgment。Human 拥有预期结果与投入、兼容、长期维护、风险等承诺；AE 负责战略架构判断；Executor 决定实现 How。已有 Drafted Issue 时，Northstar 只 enrich 这个 canonical intent，不重建第二份 intent/spec。

已有 authoritative execution contract / Taskbook 与执行结果时，直接读 [outcome-judgment.md](references/outcome-judgment.md) 独立判卷，不重做仍有效的 shaping。

## 什么时候值得调用 Northstar

优先直接执行已有 Drafted Issue；只有以下复杂度会改变是否能安全开始时才扩大到 Northstar：

- 两个或更多都合理的解释会改变 accepted outcome、binding boundary 或长期 commitment；
- 事实已经足够，但仍存在必须由 Human 关闭的 material trade-off；
- material `Current → Target` delta 跨多个 cohesive outcome，依赖关系本身会影响执行边界；
- 下游无法只靠 Issue Draft / Acceptance 区分“解决原问题”和“完成所提手段”；
- 已有复杂 execution contract 需要独立 outcome judgment。

不要把 clear small / medium Issue 重新编译一遍。Issue 创建、tracker lifecycle、routing tag、MultiCA 调度都不属于 Northstar。

## Intent judgment：只保留会改变选择的信息

从当前 authoritative request、Drafted Issue、Human correction 与相关 Evidence 开始，不重建已经成立的上下文。理解原问题、当前要求推进到哪里，以及哪些范围 / 约束 / commitment 会改变选择；不把假设补成事实或授权。

`Goal` 是可选 reasoning representation，不是必交字段。只有抽象 outcome 能实际区分手段与结果、改变 Human choice / binding boundary，或防止一个具体 Draft “正确实现了手段却没解决原问题”时才显式恢复 Goal。若 `Problem + Draft + Constraint + Acceptance` 已足够，不再制造同义 Goal。

点名的工具、架构或实现默认是 means：**换一种实现仍满足 accepted result，Human 是否接受？** 接受则留给 Executor；只有有效 authority 固定结果、承诺或 representation 时才 binding。

Human 有权给出的 requirement 可直接 binding；owner、readiness、runtime behavior 等 reality claim 需要 Evidence。优先使用现有权威来源；候选方案、prototype、edit point 和自报 confidence 只是情报。authority 与 verified reality 冲突时暴露冲突及影响，不用现状覆盖目标，也不把文档变成事实。

调查只为改变当前 Intent judgment、material work、binding boundary、completion obligation 或 safe start。决定工作是否合法或能否开始的 Unknown，应关闭或保留为显式 dependency / blocker；只影响可替换 How 的未知留给 Executor，不为补齐 inventory、预选 verifier 或未来实现扩大调查。

只有事实不能决定、且答案会改变 accepted outcome 或 Human commitment 时才 Ask。意图、framing 或 trade-off 未定时读 [intent-shaping.md](references/intent-shaping.md)；其中 Grill 按问题需要使用，不是固定访谈。必要的 territory Unknown 交 `$unknowns-first`；长期结构问题交 `$architecture-evolution`；当 Intent / choice 已大体理解，但核心路径、ownership、boundary、interface 或 usage 仅靠 prose 仍可能导向 materially different Target 时，调用 `$intent-shape` 做最小 concrete shaping。只消费当前 decision 所需的 correction / Evidence，不替 Human 关闭 Human-owned choice。

## Compile：只有直接 Issue 不够时才增加 execution structure

Northstar compile 的目标是让困难 Intent 变成**同一个 canonical work intent 下可执行、可验收的 material contract**，不是固定生成 Taskbook 文件。

优先 enrich 已有 Drafted Issue：补充真正 durable 的 Decision、material `Current → Target` delta、coarse execution relation 或 Acceptance。只有复杂度、下游访问边界或明确委托要求独立执行合同 / Taskbook 时，才生成额外 artifact；它应引用 canonical Issue，并避免复制一套长期漂移的 Intent SOT。

对于存在 material Target 的非平凡变化，只有当它能实际约束 material work 时，才用已经成立的 Target 与 verified reality 建立 `Current → Target` delta。Target 可以来自清楚的 Human / authority，也可以来自 `$intent-shape` 的 concrete shaping 与后续 correction；Draft / prototype 本身只是 reaction / Evidence surface，不因存在而 binding。

Task decomposition 不能负责发现、补完或偷偷改变 Target。若 compile 时发现仍有 materially different Target interpretation 会改变 accepted outcome、核心路径、ownership、binding boundary 或 interface / usage，停止受影响的 decomposition，回到 shaping / Human decision，而不是把未决方案编成并行 task 或让 Executor 重猜。

**Material work 按 best-known complete Graph 判断。** 已知的 cohesive outcomes 与真实 dependency 完整表达；Graph 只组织已经由 intended change / verified delta 支持的 Execution，不反推 Goal 或 Target。依赖未来 Evidence 才能确定存在、scope 或关系的 work 停在当前 frontier。独立分支保持独立，不为并行拆碎 cohesive work；文本顺序不制造 dependency，一个 blocker 不冻结无关分支。简单工作不需要显式 Graph；复杂切分 / dependency 判断才读 [execution-compile.md](references/execution-compile.md)。file、helper、patch 顺序和可替换实现仍是 How。

**Verification 按结果 claim，而非步骤或 Graph 节点评判。** repo 已确认的 authoritative test/build/replay/integration path，只有省略会明显增加 under-verification 时才进入当前 contract；失准后由 Executor 从 repo authority 重推等价或更强 Evidence。存在具体“实现错而检查仍可 PASS”的风险时，才读 [verification-trust.md](references/verification-trust.md)。

## 交付与停止

完成当前可交付的困难 judgment 或 material contract。已有 Drafted Issue 时，只把后续 consumer 必须知道的 durable Decision、Constraint、Draft correction、material relation 或 Acceptance fold back 到 canonical Issue；阶段性 reasoning、progress 与普通 implementation How 不进入 Northstar 自己的第二份 SOT。

下游无法访问 canonical Issue / source 时，在交付中复制最小必要 context 与出处；不要复制完整聊天。Northstar 不维护 progress/status/retry 协议，不持续监督 MultiCA / Executor，也不因为 execution session 变化而把一个 cohesive Issue 拆成 context-window-sized tickets。

Human correction 或核实后的 Evidence 只重开最高受影响判断及其 dependency cone，保留无关选择与仍有效 Evidence，删除失效陈述。普通实现失败不交回 Human；宿主维持 execution / feedback loop。

当 Drafted Issue / contract 已足以让 fresh Executor 在 binding boundary 内安全开始，剩余未知只影响 implementation How 时停止。不要为了证明 Northstar“完成过流程”额外生成 Goal、Taskbook、Graph 或文件。
