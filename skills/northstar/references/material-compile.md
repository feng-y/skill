# Material Compile

只在当前 Northstar Intent / Drafted Issue 已经成立，但复杂 material work / dependency 仍使 fresh Executor 无法安全开始时读取。这里组织 executable handoff，不重新定义 Intent，不设计 implementation How，也不拥有 Verification。

## Intended delta before work graph

先从 canonical Intent 恢复已经成立的 `Current → Intended` material delta。只保留为了让 Draft / Constraint / Acceptance 成立而真正需要兑现的差异，例如 responsibility / authority 归位、核心路径改变、binding boundary 建立、明确要求退出的 legacy path，以及必须保持的 invariant。

不要从 task list、文件结构、当前 module 或候选 patch 反推 Intended state；不要把仍会改变 Intent 的 unresolved alternative 编成 Executor branch。

## Best-known complete material graph

复杂 work 用当前 Evidence 已经支持的 material outcomes 与真实 dependency 组织：

- 一个 cut 对应一个可独立判断的 cohesive outcome / responsibility / binding boundary，而不是一个文件或 helper；
- prerequisite、共享 authoritative surface / conflict、或必须共同成立的 outcome 才形成 dependency；
- 文本顺序不形成 dependency，独立 work 保持独立；
- 当前已知且省略会迫使 Executor 重新发现的 material cut / relation 应保留；
- contingent future 的存在、scope 或 dependency 仍取决于未来 execution Evidence 时，停在当前 frontier，不提前猜。

简单/线性工作是 Graph 的退化形式，不需要显式 diagram、schema、node taxonomy 或 scheduler。

## Verification boundary

Compile 只携带 Northstar 已定义的 Acceptance / completion claims 与必要 Evidence obligations，不选择具体 test/replay/runtime command，不把 verification step 编成 execution phase。

`$replay` 根据 current reality 选择和核实 claim-relevant Evidence，并独立判断 outcome。一个 implementation cut 通过不代表整体 Acceptance 自动成立。

## 交付

默认把必要 material relation fold 回 Drafted Issue。只有复杂度、下游访问边界或明确委托确实需要独立 execution contract 时，才生成额外 Taskbook；它不能复制第二份长期 Intent SOT。

当 fresh Executor 已能在 binding boundary 内开始、剩余未知只影响 implementation How 时停止 compile。
