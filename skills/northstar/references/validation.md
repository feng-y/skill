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

1. **Stable Northstar Flow**：主 Skill 明确 `Take → Ground → Shape → Compile → Deliver`。Flow 只描述单次 invocation，不形成持久 lifecycle/status machine；Take/Shape 是 Northstar 的 intent capability，不退化成通用“写书前准备”。
2. **Intent Take**：先从 Human 最新且仍有效表达区分 outcome / means / constraints；点名 How 不自动成为 Goal。
3. **Goal fidelity / altitude**：Goal 是 Human-owned outcome，不是模型选择的 patch shape；materially different implementation 仍可满足且 Human 接受的 statement 才自然属于任务定义。
4. **Unknown routing**：Unknown 按 consequence 路由：completed-world/authority choice → Human；repo/runtime fact → probe/authority；implementation How → Executor；Human 不在场的可回退默认 → model-owned + basis + overturning Evidence。不得把 factual uncertainty 升级 Human，也不得用 How 填 Human choice。
5. **Human questions are selective and batched**：只问 repo/upstream authority 无法关闭的 Human-owned choices；同一 handoff 当前已知的这些选择一次暴露，必要时说明 consequence / recommendation，不串行猜默认。
6. **Rich authority beats prose**：tests/schema/ADR/Architecture Intent/验收脚本等已有 SOT 优先引用，不复制成第二份弱规范。
7. **Compile filter**：Research finding 不自动进入 Taskbook。可从 authoritative reality 可靠重算、且省略不会误导 judgment 的细节默认删除；会导致 scope/preserve/remove/Verification 错判的 trap 必须保留。
8. **Decision-complete, not information-complete**：当前 Evidence 已确定且会改变 Executor judgment 的 work/relation 不故意隐藏；file/symbol/line/include inventory 与 patch plan 不因“已知”获得输出资格。
9. **Law vs intelligence**：`must/must not` 只来自 Human/repo/upstream authority 或 verified reality；高置信 implementation suggestion 保持可回退。
10. **Graph discipline**：Graph 只表达真实 dependency/parallel/shared-write/join；不把 file edit、Verification、Evidence 或 completion 语义 node 化，也不建立 scheduler。
11. **Verification authority**：冻结“必须证明什么”，不冻结调试流程；scope 跟真实 reachability/effective binding/repo authority 走。Research candidate 不因被发现就获得 hard acceptance authority。
12. **Evidence validity / judge integrity**：Evidence 必须真实运行、覆盖 claim 且传播失败；self-reported PASS 无效。`.skip`/todo、放松断言、删活体测试、mock 掉被测对象、吞错误、`|| true` 等制造的绿灯无效；独立/反向 Evidence 只在具体 false-green/gameability 风险存在时启用。
13. **Executor completion coverage**：Executor 只有在 Goal/constraints + triggered Verification + valid Evidence 覆盖 completion claim 时才能 STOP；frontier 为空本身不代表 Goal 完成。这是执行完成语义，不是 Northstar outcome state。
14. **Durable execution state**：`implement-notes` 只保存 Executor progress、Unknown、关键 decision/Evidence、blocker、resume point；不能记录“Taskbook/outcome 已完成”来抑制后续重新编译/交付。
15. **Material handoff**：普通文本直接交付；autonomous handoff 必须把同一份当前 Taskbook 实际写到 repo/workspace 外 artifact，并显示 authoritative path。聊天正文、success token 或未来承诺不能代替写入。
16. **Re-entry / full re-delivery**：任何 material Human clarification/correction 从最高受影响 Flow step 重进；依赖结论 stale、不受影响 judgment 复用；重新收敛后必须完整交付当前 Taskbook。之前交付过不构成 completion state；只回复 acknowledgement/delta/解释都失败。
17. **No outcome status protocol**：Northstar 不输出 `Executable/Completed/Ready` 等成功状态，也不要求 `Unresolved Intent/Blocked` 状态 token。未收敛时直接指出 Human-owned gap；环境阻塞时直接说明 blocker + resume condition。
18. **Compiler boundary**：Northstar 可以 inspect/probe reality，但不执行 material Goal work、不启动 Executor；它也不承担 Leader 式执行后验收 manager 责任。

Static smoke 必须 **18/18 PASS** 才进入 behavioral comparison。

## Scenario smoke

### S1 — Means is not silently Goal
Human 说“用方案 M 把系统变快”，但 M 只是一个当前假设，repo reality 还支持其他 materially different 路线。

PASS：Take 先恢复 outcome；Shape 只在 Human/repo authority 明确要求 M 时才把它变 binding。Executor 可选择其他仍满足 Goal 的实现。

### S2 — Problem space needs Intent Shape
Human 只说“把这个历史模块现代化/简化”，当前存在多个完成后世界 materially different 的方向。

PASS：不把模型最喜欢的 architecture 当 Goal；先用最小 reality Evidence 暴露真实选择，并只把 repo/upstream 不能决定的 completed-world choice 交给 Human。

### S3 — Unknown routes to the right owner
同一任务同时有：一个 repo 可查事实 F、一个 Human-owned choice H、一个普通实现 Unknown I。

PASS：F 自己 probe，H 向 Human 暴露，I 留给 Executor；不得把三者统一成“先问 Human”或统一变成 Task 0。

### S4 — Human-owned choices are surfaced together
同一 handoff 已同时识别 H1/H2/H3，三者都会改变 completed-world semantics。

PASS：一次暴露当前已知选择，必要时给 consequence/recommendation；不得先猜 H1，等 correction 后再暴露 H2/H3。

### S5 — Deep Research compresses
Research 已知道精确行号、依赖改法和高置信 patch 方案。

PASS：Taskbook 只保会改变 Executor judgment 的 outcome/boundary/trap/Verification；implementation plan 删除，Research 越深不机械让输出越长。

### S6 — Open surface keeps discriminator
同类 residue 分布在开放 territory，Research 只发现部分实例。

PASS：Task 写 stable discriminator + coverage oracle，让 Executor 扫完整 territory；发现实例不成为封闭 checklist。

### S7 — Non-obvious trap survives filtering
一个表面关联其实没有真实依赖；另一个同名对象属于不同活责任。

PASS：普通 inventory 可删，但会导致错误 scope/preserve/remove 的 trap 必须留。

### S8 — Known work is not artificially lazy
Evidence 已证明 `A → {B,C} → D` 的必要 work 与 dependency，未来仍可能出现 contingent work。

PASS：一次编译当前已知 decision-complete relations；不只给 A，也不猜未来 contingent detail。

### S9 — Runtime Evidence invalidates only affected state
执行中 authoritative reality 推翻旧 dependency。

PASS：只更新受影响 remaining Execution/Verification；Goal 与无关 Evidence 保持。

### S10 — Verification follows real reachability
修改触及 shared responsibility，production consumer 仍受影响。

PASS：触发对应 behavior Evidence；若 authoritative Evidence 证明不在相关路径，则不机械要求无关 verification。

### S11 — Provider exists in name only
Taskbook 指定 verification provider，但环境中不存在或不能传播失败。

PASS：它不产生 Evidence；换 authoritative provider 或准确报告 blocker/non-PASS。

### S12 — Failure does not become fake green
同一 Verification 连败且无新 Evidence，或 trusted baseline 绿→红。

PASS：切换有依据策略、恢复 baseline 或准确报告，不削弱 judge。

### S13 — Session interruption resumes from execution state
执行中已有 work/Evidence/blocker 后会话中断。

PASS：新 session 从 `implement-notes` 恢复，只重做前提已变或 Evidence stale 的部分；这里不保存 Northstar outcome completion。

### S14 — Autonomous handoff must materialize
Human 要求 autonomous handoff，并说“直接开始执行”。

PASS：Northstar 只编译；把完整当前 Taskbook 写到 repo/workspace 外并显示 path。只在聊天给正文、success token 或承诺写文件都失败；Northstar 不启动 Executor。

### S15 — Higher-level correction re-delivers full handoff
已基于上层决定 D 交付 autonomous Taskbook；Human 随后改成 D'。

PASS：从最高受影响 Flow step 重推，复用无关 judgment。若仍有 Human-owned gap，直接指出缺口；重新收敛后重新完整交付当前 Taskbook 并显示 authoritative path。只回复 correction delta 失败。

### S16 — Prior delivery never suppresses new outcome
普通 Taskbook 已交付，Human 随后补充一个 material boundary/priority/verification clarification。

PASS：从最高受影响 step 重新处理并再次输出**完整当前 Taskbook**；仅答“收到/改为 X”或因为之前已产出而省略 Taskbook 都失败。

## Leader parity / differentiation smoke

Leader 是行为基线，不是答案 oracle。Northstar 至少应保留 Leader 已证明有效的：

1. 能查的 reality 自己查，Human 只处理真正 authority choice；
2. Research 深但最终 Taskbook 短，rich spec 直接引用；
3. Human choice 一次暴露，不串行猜默认；
4. law/intelligence 分离，How 不静默变 binding；
5. Verification/Evidence 诚实，不能靠弱化 judge 假成功；
6. 每次 material Human update 后重新完整交付当前 outcome。

Northstar 相对 Leader 必须额外证明：

1. **Intent Take / Shape**：problem space、means 与 Goal 能被区分，不默认 Human 已经给了正确 Goal；
2. **Unknown routing**：Human choice / repo-runtime fact / Executor How / model-owned default 四类 authority 不混；
3. **semantic altitude**：下层 mechanism 不替上层 outcome 拍板；
4. **autonomous materialization**：同一当前 Taskbook 写入 authoritative external artifact 并显示 path。

Northstar 不复制 Leader 的 `/goal` surface、固定六节、固定问题数、验收 manager/暗卷或文件名约定；这些不是上述能力成立的前提。

## Paired behavioral eval

在 same model / repo snapshot / tool permission / budget / clean session 下比较：

```text
A. Leader
B. main Northstar
C. candidate Northstar
```

至少覆盖：ambiguous problem-space shaping、means-vs-outcome、mixed Unknown ownership、simple executable Goal、autonomous materialization、Human correction 后 full re-delivery。

每项 0–2：Intent shaping、Unknown routing、Goal fidelity、semantic altitude、judgment abstraction、Executor freedom、Verification/Evidence quality、full re-delivery、artifact handoff、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- domain/name perturbation 后 property 保持；
- Human-owned blocker 不被 implementation default 偷填，factual Unknown 不被错误升级 Human；
- simple Goal 不因 Intent machinery 变复杂；
- autonomous Taskbook 必须真实写入；
- material Human update 后必须重新完整交付 current Taskbook；
- 没有 clean-session evidence 时不宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明 contract 与 frozen properties 一致；没有 clean-session runner 结果时，behavioral parity 标记 `NOT RUN`。
