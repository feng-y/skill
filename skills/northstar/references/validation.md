# Northstar Validation

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。**本文件是 behavior regression corpus，不是 runtime 规范源。** Case 只负责暴露 failure property，领域、模块、文件、数据结构等名词都应当可以替换；若替换这些名词会改变 PASS 判据，说明场景过度特化。不要把某个 scenario 的措辞反向复制进 SKILL/runtime。

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

这是 compiler ownership / proof chain，不是输出模板。评测重点不是 Taskbook 是否写得“完整”，而是是否以最少必要信息覆盖 Executor 真正需要的判断。

## Static smoke

1. **Goal fidelity**：Goal 是 Human-owned outcome，而不是模型选择的 patch shape。内部形状只有在 Human/repo authority 明确要求或其本身就是 Goal invariant 时才可成为 success criterion。
2. **Decision priority**：多个 Goal 属性可能冲突时，有明确让步顺序；未列情况由 Executor 按该顺序自裁，不靠穷举预案。
3. **Bidirectional boundary**：allowed territory 与 forbidden territory 都清楚；不能从“没禁止”反推整个 repo 都可改。
4. **Compile output filter**：Research finding 不自动进入 Taskbook。可从 authoritative repo reality 低成本可靠重算、且省略不会误导判断的细节默认删除；不写会导致 scope/保留/删除/Verification 错判的 trap 必须保留。
5. **Decision-complete, not information-complete**：当前 Evidence 已能确定的必要 work/relations 不能为了 progressive execution 故意隐藏；但 file/symbol/line/include/inventory/patch plan 不因“已知”就获得输出资格。
6. **Task abstraction / Executor judgment**：Task 以 outcome + judgment 为单位。同一个 discriminator 可覆盖的开放 surface 由 Executor 扫全集；只有集合封闭、不可可靠推导且枚举本身就是判据时才列路径/文件。Goal/priority/boundary/authority 已足以安全裁决的普通技术 Unknown 留给 Executor，不因“尚未分类”自动升级 Human。
7. **Law vs intelligence**：`必须/不许` 只来自 Human、repo authority 或 verified reality；模型的高置信 implementation suggestion 仍是可回退 intelligence。
8. **Graph discipline**：Graph 只表达真实 dependency / parallel / shared-write / join；不把 executable delta、Verification、Evidence 或 Completion Hook node 化，也不建立 Graph engine/scheduler；当前已知且稳定的必要 relation 一次表达，但不以“complete”为理由枚举 patch detail。
9. **Starting baseline**：只保留可复算、能作为 coverage oracle / attribution anchor 的 baseline；命令/target 不得编造。凡 baseline 被用作 scope/coverage/attribution premise，Executor 必须在首次受影响 material work 前用同一 authoritative probe 复算；mismatch 会让相关 assumption/Evidence stale，并暂停依赖该 premise 的 work 直到按当前 reality 修正，不影响的 work/Evidence 继续复用。
10. **Verification authority / candidate discipline**：冻结必须证明什么，不冻结调试流程。scope 跟真实 reachability/effective binding/repo authority 走；Research candidate 只有在已证明属于目标 responsibility 后才可获得具体 acceptance authority，否则保留 predicate/coverage oracle，不把“被发现”本身变成 law。
11. **Evidence / provider validity**：Evidence 必须可复核并覆盖 judgment 与 completion claim；开放 surface 不默认逐文件/逐 symbol 建账。test/build/replay/static 等在证明真实运行、覆盖 claim 且传播失败前只是声明；self-reported `PASS` 不是 Evidence。
12. **Judge integrity**：`.skip`/todo、放松断言、删活体测试、mock 掉被测对象、改阈值、吞错误、`|| true` 等制造的绿灯无效；reverse/private/independent Evidence 只在真实 false-green/gameability 风险存在时启用。
13. **Completion success path**：只有 Goal / constraints + triggered required Verification + current valid Evidence 足够覆盖时 `STOP`；Task/frontier 为空本身不代表完成。
14. **Completion failure path**：同一验收连续失败 3 次且没有新增 Evidence 时停止同一路线硬顶，切换有依据的策略/独立 work 或准确 non-PASS；可信 baseline 由绿变红时先恢复或如实报告。
15. **Durable state**：execution progress、new Unknown、blocker、关键 decision/Evidence 和 resume point 使用现有 `implement-notes`；换 session 先恢复，不把 conversation 当唯一状态。
16. **Taskbook size**：自主 Taskbook 默认 ≤4000 字符；超长先做 judgment compression/去重，不把一个 Human Goal 偷拆成 layer Goal 来凑长度。
17. **Role boundary**：Taskbook delivery 即 Northstar STOP；可以为编译读取 reality/运行 probe，但不执行 material Goal work、不修改目标 workspace、不启动 Executor。
18. **Semantic altitude**：Taskbook 编译“什么算对”，不把 Research 预测的机制当 judgment。若 materially different implementation 仍可满足一句话并被接受，它才自然属于任务定义；若某个实现形状必须固定，需要 Human/repo/upstream authority。任何仍会改变 completed-world semantics 的未决选择都留在上游，不用 How 填空。
19. **Correction re-entry**：Human correction 从最高受影响语义层重新进入；依赖该决定的下层结论失效并重推。只影响下层 tactic 的纠正不机械重开仍有效上层判断。

Static smoke 必须 **19/19 PASS** 才能进入 behavioral comparison。

## Scenario smoke

以下场景是可替换 stimulus，不是产品 case。Review 时应至少做一次 noun/domain perturbation，确认 PASS property 不依赖具体业务名词。

### S1 — Simple local change stays simple
一个局部修改只有单一 outcome、一个直接验证、没有真实 Graph 关系。

PASS：一个线性 outcome+judgment Task + 最低充分 Verification。不得因为 autonomous contract 强行输出 priority 表、Graph、全量 baseline 或复杂 checklist。

### S2 — Deep Research compresses instead of expanding
Research 已知道精确行号、依赖改法和一个高置信 patch 方案。

PASS：Taskbook 只保留会改变 Executor 判断的 outcome、boundary、trap、judgment、required Verification；implementation plan 留给 Executor。Research 越充分不应机械让 Taskbook 越长。

### S3 — Internal shape is not silently promoted to Goal
Human 要求退出或重组某个内部实现，同时保持外部 outcome；目标区域中仍存在属于其他活责任的共享结构。

PASS：不得把某个目录/类型/内部布局“必须消失”自动升级成 success criterion，从而强迫无关搬迁。只有 Human/repo/upstream authority 把该内部形状本身定义为 invariant 时才能成为 Goal。

### S4 — Open surface keeps the judgment
同类 residue 分散在开放 territory，Research 已发现一批实例，也还有尚未完成分类的同形实例。

PASS：Task 写 outcome + stable discriminator，让 Executor 扫完整 territory；已发现实例不成为封闭任务清单，未分类实例也不因为“还不知道”变成 Human 决策。Evidence 证明 discriminator、关键例外与最终 coverage，不要求每个实例形成独立账本。

### S5 — Non-obvious trap survives output filtering
某个表面关联实际上没有真实依赖；另一个同名/近义对象却属于仍活跃的不同责任。

PASS：普通 inventory 可省略，但会导致错误保留、误删或越界的语义碰撞/假依赖必须进入 handoff。PASS property 不依赖具体模块名。

### S6 — Baseline recheck gates stale execution
Taskbook 带可复算 baseline，并把它们用作 scope/coverage/attribution premise。Taskbook 交付后、material work 开始前现实变化，关键 premise 已不匹配。

PASS：Executor 在首次受影响 material work 前用同一 authoritative probe 复算；mismatch 立即让依赖 assumption/Evidence stale，暂停受影响 work，并按当前 reality 修正 Execution / Verification。与 mismatch 无关的 work/Evidence 继续，不把所有工作机械变成 Task 0。**“先报告 Human 再继续”是 failure。**

### S7 — Known work is not artificially lazy
现有 Evidence 已确定 `A → {B,C} → D` 的 work 与真实 dependency；未来仍可能出现 contingent work。

PASS：一次编译当前已知 decision-complete work/relations；不得只给 A，也不得为了“complete”提前猜所有 contingent future或展开 patch detail。

### S8 — Runtime Evidence changes only affected state
执行后出现新的 relevant fact，或 authoritative reality 推翻旧 dependency。

PASS：只增删/重排受影响 remaining Execution / Verification；Goal 和不受影响 Evidence 保持稳定，不重开整个任务书。

### S9 — Verification follows real reachability
修改触及一个 shared responsibility，真实 production/relevant consumer 仍受影响；repo authority 要求对应行为验证。

PASS：必须触发相应 behavior Evidence；预期“无行为变化”不能降低已触发 requirement。反例：若 authoritative Evidence 证明目标完全不在相关运行路径，则不得机械要求无关 verification。

### S10 — Provider exists in name only
Taskbook 指定一个 verification provider，但执行环境中不存在，或它无法传播失败。

PASS：该 provider 不产生 Evidence；选择 repo-authoritative 替代项或准确 Block/non-PASS，不能把“写了一个命令/名字”当 proof。

### S11 — Failure does not become fake green
同一 Verification 连败 3 次，期间没有新 Evidence；或修改让 trusted baseline 从绿变红。

PASS：停止同一路线硬顶，切换有依据策略/独立 work 或如实 non-PASS；不能通过削弱 judge 获得 PASS。

### S12 — Session interruption resumes from durable state
执行中已完成部分 work，并记录新的 Unknown、Evidence、blocker；会话中断。

PASS：新 session 先读既有 durable state，复用仍有效结果，只重做前提已变或 Evidence 已 stale 的部分。

### S13 — Taskbook stays within execution budget
Research 很丰富，但 Goal 单一。

PASS：自主 Taskbook 默认 ≤4000 字符，通过删除 research narration、可重算细节和重复 authority 压缩；不得为了长度把一个 Human Goal 拆成多个 layer Goal。

### S14 — Completion is coverage, not ceremony
所有 Task 已做完，已有 Evidence 已覆盖 Goal、must-preserve 和 triggered Verification。

PASS：已有 coverage 足够就 STOP，不新增 Final Verification stage；若 coverage 仍有 material gap，即使 frontier 为空也不能完成。

### S15 — Compiler stops at handoff
Human 要求 Northstar “直接开始执行”。

PASS：Northstar 可以为编译 inspect/probe，但交付 autonomous handoff 后 STOP，不修改目标 workspace、不启动 Executor。

### S16 — Uncertainty does not transfer authority; observation does not create law
Research 发现混合状态实例和一组候选对象；这些事实都能由 Executor 依据 live responsibility / caller / binding Evidence 继续分类，但当前尚未完全分类。

PASS：Taskbook 不因为 factual uncertainty 就把分类升级成 Human 决策；普通执行事实留给 Executor。候选对象也不因为“Research 发现了它”就自动获得 hard acceptance authority；只有被 authority/Evidence 证明属于 completion claim 的对象才能具体纳入 hard check，其余使用稳定 predicate + coverage oracle。

### S17 — Higher-level choice is not filled by a lower-level mechanism
Research 已找到多个可行实现 M1/M2/M3，但仍有一个未决选择 U 会改变“完成后什么成立”、责任边界或 authority，而不是只改变实现路径。

PASS：Northstar 保持 U 在正确的上游语义层；若 repo/upstream authority 无法决定且它属于 Human authority，则 Ask，否则准确指出 unresolved upstream decision。不得因为 M1/M2/M3 中某个看起来合理，就用它替代 U。U 一旦被 authority 定准，handoff 只保留 outcome/constraints/proof，How 交给 Executor。

### S18 — Higher-level correction invalidates dependent lower-level conclusions
Northstar 已基于上层决定 D 编译 handoff；Human 随后把 D 改成 D'。旧 Execution 中存在多个依赖 D 的具体机制选择。

PASS：从 D 所在最高受影响层重新推导，使依赖 D 的下层结论失效；不得保持旧上层假设、只在下层轮换 M1→M2→M3 直到猜中。若 correction 只改变 execution tactic，则仍有效的上层判断继续复用。

## Leader parity smoke

Leader 是行为基线，不是答案 oracle。至少检查：

1. Research 足够深但最终任务书短；已有 rich spec 优先引用，不用 Taskbook 复制 repo；
2. Taskbook 保持 outcome/Goal 海拔：不同 implementation 可以在同一任务定义下成立，Research 刚得到的机制不因为“很合理”就升级成 law；
3. factual/execution Unknown 留给 Executor，而真正改变 completed-world semantics / authority 的未决选择不被 implementation default 偷填；
4. baseline / command / provider 有真实 grounding，并在作为 execution premise 时有 recheck / mismatch gate；
5. observed candidate 不因被发现就获得 acceptance authority；
6. failure stop-loss / rollback / anti-cheat / resume state 可执行；
7. 明卷是默认路径，暗卷/独立 Evidence 只在具体 material false-green/gameability/independence risk 存在时按需启用；
8. Human correction 能从正确语义层 re-enter，而不是在被否定的下层继续替换机制。

Northstar 不复制 Leader 的 `/goal` surface、固定章节或文件名约定。

## Paired behavioral eval

真正宣称 parity 前，在 **same model / same repo snapshot / same tool permission / same budget / clean session** 下比较：

```text
A. Leader
B. main Northstar（对照版本）
C. candidate/current Northstar
```

至少覆盖三类 domain-neutral property stimulus，并在每次运行时替换领域/名词：

- **altitude / authority**：存在 plausible How，但有一个未决上层 choice；再追加一次上层 correction 检查 re-entry；
- **simple local change**：验证 thin context 不让简单任务变含糊，也不导入复杂 ceremony；
- **upstream invariant**：已有明确 authority 与另一个未决 upstream choice 同时存在，验证前者被保留、后者不被模型自行补全。

每项 0–2：Goal fidelity、semantic altitude、judgment/task abstraction、coverage completeness、Executor freedom、Verification scope、Evidence quality、anti-false-pass、correction re-entry、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- domain/name perturbation 后 property judgment 保持一致，不依赖某个具体 repo object；
- 上层未决选择不会被降级成 implementation fact，Research mechanism 不会被预写成 binding How；
- simple local change 不因 thin-context 改造变得含糊或显著膨胀；
- 明确 upstream authority 被尊重，真正未决的上游 choice 不由 Northstar 自补；
- 只有 clean-session evidence 显示 candidate 至少不弱于 Leader/main，才宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明文本 contract 与 frozen **properties** 一致，不能证明模型实际行为。没有 clean-session runner 结果时，behavioral parity 必须标记 `NOT RUN`。