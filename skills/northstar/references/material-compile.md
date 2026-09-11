# Material Compile

只在当前 Northstar Intent / Drafted Issue 已经成立，但复杂 material work / dependency 仍使 fresh Executor 无法安全开始时读取。这里组织 executable handoff，不重新定义 Intent，不设计 implementation How，也不拥有 verification judgment 或 execution progress。

## Intended delta before work graph

先从 canonical Intent 恢复已经成立的 `Current → Intended` material delta。只保留为了让 Draft / Constraint / Acceptance 成立而真正需要兑现的差异，例如 responsibility / authority 归位、核心路径改变、binding boundary 建立、明确要求退出的 legacy path，以及必须保持的 invariant。

不要从 task list、文件结构、当前 module 或候选 patch 反推 Intended state；不要把仍会改变 Intent 的 unresolved alternative 编成 Executor branch。

## Best-known complete material graph

复杂 work 用当前 Evidence 已经支持的 material outcomes 与真实 dependency 组织：

- 一个 cut 对应一个可独立判断的 cohesive outcome / responsibility / binding boundary，而不是一个文件、helper 或 verifier；
- prerequisite、共享 authoritative surface / conflict、或必须共同成立的 outcome 才形成 dependency；
- 文本顺序不形成 dependency，独立 work 保持独立；
- 当前已知且省略会迫使 Executor 重新发现的 material cut / relation 应保留；
- contingent future 的存在、scope 或 dependency 仍取决于未来 execution Evidence 时，停在当前 frontier，不提前猜；
- independently falsifiable verification claim 不自动成为独立 execution cut。

简单/线性工作是 Graph 的退化形式，不需要显式 diagram、schema、node taxonomy 或 scheduler。**Best-known complete 不等于 research-complete**：不能为了让 Graph 看起来完整扩大 inventory、预证 implementation How 或制造未来占位 node。

## Verify boundary

Compile 只携带 Northstar 已定义的 Acceptance / completion claims 与 material work relation，不选择具体 test/Replay/runtime command，也不把 verification step 编成 execution phase。

如果 complex handoff 需要明确某个 claim 必须被验证，可以记录 **claim identity / proof obligation pointer**，但 proof obligation、backend selection、Evidence sufficiency 与 verdict 属于 `$verify`。DaVinci Replay、tests、build、runtime 等只是 Verify 可选择的 backend。

一个 implementation cut 通过不代表整体 Acceptance 自动成立；一个 verification claim 也不自动变成一个 execution cut。

## Evidence-driven loop

Material Graph 不是一次性计划，也不是 control-plane state。Research、execution、review 或 `$verify` 已核实的 **verified Evidence** 如果真正改变 material work / dependency，而 Intent 本身仍成立，只重算受影响 dependency cone：

- contingent work 因新 reality 成为真实工作 → 扩展对应 cone；
- Evidence 证明 branch / dependency 不存在 → 删除；
- material boundary / relation 改变 → 拆分、合并或重排受影响 work；
- 只影响 implementation How → Graph 不变；
- Evidence 推翻 Intent / Acceptance → 返回 Northstar Intent judgment，而不是在 Graph 内修补；
- Evidence 暴露长期 architecture fork → 返回 `$architecture-evolution`。

无关 branch、仍有效 work 与 Evidence 保持有效；已完成 work 不因 Graph 改写机械重开，除非它依赖的 premise / Evidence 被影响。

Execution orchestration 可以触发下一次 compile，但不拥有 Graph semantics，也不要求 Northstar 维护 retry/debug/progress/scheduler state。

## 交付

默认把必要 material relation fold 回 Drafted Issue。只有复杂度、下游访问边界或明确委托确实需要独立 execution contract 时，才生成额外 Taskbook；它不能复制第二份长期 Intent SOT。

当 fresh Executor 已能在 binding boundary 内开始、剩余未知只影响 implementation How 时停止 compile。
