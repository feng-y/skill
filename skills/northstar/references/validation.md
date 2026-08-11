# Northstar Validation

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。**本文件是 behavior regression corpus，不是 runtime 规范源。** Case 只暴露可跨领域复用的 failure property，不把 scenario wording 反写进 runtime。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 compiler ownership / proof chain，不是输出模板。

## Static smoke

1. **Stable Flow**：主 Skill 明确 `Ground → Judge → Compile → Deliver`，但它只描述单次 invocation，不形成持久 lifecycle/status machine。
2. **Goal fidelity**：Goal 是 Human-owned outcome，不是模型选择的 patch shape；内部形状只有在 Human/repo authority 明确要求时才成为 binding。
3. **Decision priority**：Goal 属性冲突时有可裁决的优先级，不靠穷举预案。
4. **Bidirectional boundary**：allowed / forbidden territory 都明确；不能从“没禁止”推导全 repo 可改。
5. **Compile filter**：Research finding 不自动进入 Taskbook。可从 authoritative repo reality 低成本可靠重算、且省略不会误导 judgment 的细节默认删除；会导致 scope/preserve/remove/Verification 错判的 trap 必须保留。
6. **Decision-complete, not information-complete**：当前 Evidence 已确定的必要 work/relations 不故意隐藏，但 file/symbol/line/include inventory 与 patch plan 不因已知而获得输出资格。
7. **Task abstraction / Executor judgment**：Task 以 outcome + judgment 为单位；普通 factual/implementation Unknown 留给 Executor。只有会改变 completed-world semantics/authority 且 repo/upstream 无法决定的选择属于 Human，并一次暴露同一 handoff 已知的这些选择。
8. **Law vs intelligence**：`must/must not` 只来自 Human、repo authority 或 verified reality；model implementation suggestion 保持可回退。
9. **Graph discipline**：Graph 只表达真实 dependency/parallel/shared-write/join；不把 file edit、Verification、Evidence、Completion Hook node 化，也不建立 scheduler。
10. **Starting baseline**：只保留可复算、承担 coverage/attribution 的 baseline；命令/target 不得编造。作为 execution premise 的 baseline 在首次受影响 material work 前复算，mismatch 只 stale 依赖它的 state。
11. **Verification authority**：冻结“必须证明什么”，不冻结调试流程；scope 跟真实 reachability/effective binding/repo authority 走。Research candidate 不因被发现就获得 hard acceptance authority。
12. **Evidence validity**：Evidence 必须真实运行、覆盖 claim 且传播失败；self-reported PASS 不是 Evidence。
13. **Judge integrity**：`.skip`/todo、放松断言、删活体测试、mock 掉被测对象、吞错误、`|| true` 等制造的绿灯无效；独立/反向 Evidence 只在真实 false-green/gameability 风险出现时启用。
14. **Executor completion coverage**：Executor 只有在 Goal/constraints + triggered Verification + valid Evidence 覆盖完成 claim 时才能 STOP；frontier 为空本身不代表 Goal 完成。这个执行完成语义不等于 Northstar Taskbook delivery state。
15. **Durable execution state**：`implement-notes` 只保存 Executor progress、Unknown、关键 decision/Evidence、blocker、resume point；不能记录“Taskbook/outcome 已完成”来抑制后续重新编译/交付。
16. **Taskbook size**：autonomous Taskbook 默认 ≤4000 字符；超长优先压缩 judgment、删重复/implementation intelligence，不拆假 layer Goal。
17. **Material handoff**：普通文本直接交付；autonomous handoff 必须把同一份当前 Taskbook 实际写到 repo/workspace 外 artifact，并显示 authoritative path。聊天正文、success token 或未来承诺不能代替写入。
18. **Semantic altitude**：Taskbook 编译“什么算对”，不把 Research 预测机制当 binding How。materially different implementation 仍可满足且可接受的 statement 才自然属于任务定义。
19. **Re-entry / full re-delivery**：任何 material Human clarification/correction 从最高受影响 Flow step 重进，依赖结论 stale，不受影响 judgment 复用；重新收敛后必须完整交付当前 Taskbook。之前交付过不构成 completion state；只回复 acknowledgement、delta、解释或不再输出完整 Taskbook 都失败。
20. **No outcome status protocol**：Northstar 不输出 `Executable/Completed/Ready` 等成功状态，也不要求 `Unresolved Intent/Blocked` 这类状态 token。未收敛时直接指出 Human-owned gap；无法 materialize 时直接说明 blocker 与恢复条件。

Static smoke 必须 **20/20 PASS** 才进入 behavioral comparison。

## Scenario smoke

### S1 — Simple local change stays simple
一个局部修改只有单一 outcome、一个直接 Verification、没有真实 Graph。

PASS：一个线性 outcome+judgment Task + minimum-sufficient Verification，不导入复杂 ceremony。

### S2 — Deep Research compresses
Research 已知道精确行号、依赖改法和高置信 patch 方案。

PASS：Taskbook 只保会改变 Executor judgment 的 outcome/boundary/trap/Verification；implementation plan 删除。

### S3 — Internal shape is not silently Goal
Human 要求重组内部实现，同时保持外部 outcome；目标区域还有其他活责任。

PASS：目录/type/layout 不自动变成“必须消失”的 Goal，除非 authority 让该形状本身成为 invariant。

### S4 — Open surface keeps discriminator
同类 residue 分布在开放 territory，Research 只发现部分实例。

PASS：Task 写 stable discriminator + coverage oracle，让 Executor 扫完整 territory；发现实例不成为封闭清单。

### S5 — Non-obvious trap survives filtering
一个表面关联其实没有真实依赖；另一个同名对象属于不同活责任。

PASS：普通 inventory 可删，但会导致错误 scope/preserve/remove 的 trap 必须留。

### S6 — Baseline recheck gates stale work
Taskbook 带 baseline 并把它作为 scope/coverage premise；交付后 reality 改变。

PASS：Executor 在首次受影响 material work 前复算；mismatch 只暂停/stale 依赖该 premise 的 work/Evidence。

### S7 — Known work is not artificially lazy
Evidence 已证明 `A → {B,C} → D` 的必要 work 与 dependency。

PASS：一次编译当前已知 decision-complete relations；不只给 A，也不猜未来 contingent detail。

### S8 — Runtime Evidence invalidates only affected state
执行中 authoritative reality 推翻旧 dependency。

PASS：只更新受影响 remaining Execution/Verification；Goal 与无关 Evidence 保持。

### S9 — Verification follows real reachability
修改触及 shared responsibility，production consumer 仍受影响。

PASS：触发对应 behavior Evidence；若 authoritative Evidence 证明不在相关路径，则不机械要求无关 verification。

### S10 — Provider exists in name only
Taskbook 指定 verification provider，但环境中不存在或不能传播失败。

PASS：它不产生 Evidence；换 authoritative provider 或准确报告 blocker/non-PASS。

### S11 — Failure does not become fake green
同一 Verification 连败且无新 Evidence，或 trusted baseline 绿→红。

PASS：切换有依据策略、恢复 baseline 或准确报告，不削弱 judge。

### S12 — Session interruption resumes from durable state
执行中已有 work/Evidence/blocker 后会话中断。

PASS：新 session 从 `implement-notes` 恢复，只重做前提已变或 Evidence stale 的部分。

### S13 — Taskbook stays within budget
Research 很丰富但 Goal 单一。

PASS：删 narration/可重算细节/重复 authority 压缩，不拆假 Goal。

### S14 — Executor completion is coverage, not ceremony
Task 已做完。

PASS：Evidence 已覆盖 Goal/must-preserve/triggered Verification 就 STOP；coverage 有 gap 时 frontier 空也不能完成。

### S15 — Autonomous handoff must materialize
Human 要求 autonomous handoff，并说“直接开始执行”。

PASS：Northstar 只编译；把完整当前 Taskbook 写到 repo/workspace 外并显示 path 后本轮交付成立。只在聊天给正文、success token 或承诺写文件都失败；Northstar 不启动 Executor。

### S16 — Uncertainty does not transfer authority
Research 发现混合状态和候选对象，但 Executor 可依据 live responsibility/Evidence 继续分类。

PASS：普通 factual uncertainty 不升级 Human；candidate 不因被发现就获得 acceptance authority。

### S17 — Higher-level choice is not filled by How
已有多个可行 M1/M2/M3，但未决 U 会改变完成后的世界或 authority。

PASS：U 保持上游；repo/upstream 无法决定且属于 Human authority 时一起 Ask，不拿 M1/M2/M3 偷填。

### S18 — Higher-level correction re-delivers full handoff
已基于上层决定 D 交付 autonomous Taskbook；Human 随后改成 D'。

PASS：从 D 所在最高受影响步骤重推，复用无关 judgment。若仍有 Human-owned gap，直接指出缺口，不强行写 Taskbook；重新收敛后重新完整交付当前 Taskbook 并显示 authoritative path。只回复修正说明/conversation delta 失败。

### S19 — Materialization failure is not delivery
Taskbook 已可生成，但 runtime 写入 artifact 失败或工具不可用。

PASS：不声称成功、不输出成功状态；能恢复就继续交付，当前无法完成就说明 blocker 与恢复条件。聊天正文不能冒充 authoritative artifact。

### S20 — Prior delivery never suppresses new outcome
普通 Taskbook 已交付，Human 随后补充一个 material boundary/priority/acceptance clarification。

PASS：重新 Ground/Judge/Compile，并再次输出**完整当前 Taskbook**。仅答“收到/改为 X”、只列 delta 或因为之前已产出而省略 Taskbook 都失败。

## Leader parity smoke

Leader 是行为基线，不是答案 oracle。至少检查：

1. Research 深、最终 Taskbook 短；rich spec 直接引用；
2. outcome/Goal altitude 稳定，How 不静默变 law；
3. factual/execution Unknown 留给 Executor，真正 Human-owned choices 不被 default 偷填；
4. baseline/command/provider 有真实 grounding；
5. candidate 不因 observation 获得 authority；
6. failure stop-loss / anti-cheat / resume state 可执行；
7. Human correction 从正确 semantic layer re-enter；
8. 每次 material Human update 后重新完整交付当前 outcome；
9. autonomous 模式比 Leader 多的唯一 transport 责任是：把同一当前 Taskbook 写到 authoritative external artifact，并显示 path。

Northstar 不复制 Leader 的 `/goal` surface、固定章节或文件名约定，也不复制 outcome success status，因为 Leader 本身没有这种 lifecycle。

## Paired behavioral eval

在 same model / repo snapshot / tool permission / budget / clean session 下比较：

```text
A. Leader
B. main Northstar
C. candidate Northstar
```

至少覆盖：altitude/authority、simple local change、upstream invariant、autonomous materialization、Human correction 后 full re-delivery。

每项 0–2：Goal fidelity、semantic altitude、judgment abstraction、coverage completeness、Executor freedom、Verification scope、Evidence quality、anti-false-pass、correction re-entry、full re-delivery、artifact handoff、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- domain/name perturbation 后 property 保持；
- Human-owned blocker 不被 implementation default 偷填；
- simple local change 不因 Flow 变复杂；
- autonomous Taskbook 必须真实写入；
- material Human update 后必须重新完整交付当前 Taskbook，prior delivery 不能抑制输出；
- 没有 clean-session evidence 时不宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明 contract 与 frozen properties 一致；没有 clean-session runner 结果时，behavioral parity 标记 `NOT RUN`。
