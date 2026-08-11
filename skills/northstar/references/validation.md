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
6. **Task abstraction / Executor judgment**：Task 以 outcome + judgment 为单位。同一个 discriminator 可覆盖的开放 surface 由 Executor 扫全集；只有集合封闭、不可可靠推导且枚举本身就是判据时才列路径/文件。Goal/priority/boundary/authority 已足以安全裁决的普通技术 Unknown 留给 Executor，不因“尚未分类”自动升级 Human。若同一 handoff 已同时识别出多个真正 Human-owned blocker，应一并暴露而不是逐个填入 model default。
7. **Law vs intelligence**：`必须/不许` 只来自 Human、repo authority 或 verified reality；模型的高置信 implementation suggestion 仍是可回退 intelligence。
8. **Graph discipline**：Graph 只表达真实 dependency / parallel / shared-write / join；不把 executable delta、Verification、Evidence 或 Completion Hook node 化，也不建立 Graph engine/scheduler；当前已知且稳定的必要 relation 一次表达，但不以“complete”为理由枚举 patch detail。
9. **Starting baseline**：只保留可复算、能作为 coverage oracle / attribution anchor 的 baseline；命令/target 不得编造。凡 baseline 被用作 scope/coverage/attribution premise，Executor 必须在首次受影响 material work 前用同一 authoritative probe 复算；mismatch 会让相关 assumption/Evidence stale，并暂停依赖该 premise 的 work 直到按当前 reality 修正，不影响的 work/Evidence 继续复用。
10. **Verification authority / candidate discipline**：冻结必须证明什么，不冻结调试流程。scope 跟真实 reachability/effective binding/repo authority 走；Research candidate 只有在已证明属于目标 responsibility 后才可获得具体 acceptance authority，否则保留 predicate/coverage oracle，不把“被发现”本身变成 law。
11. **Evidence / provider validity**：Evidence 必须可复核并覆盖 judgment 与 completion claim；开放 surface 不默认逐文件/逐 symbol 建账。test/build/replay/static 等在证明真实运行、覆盖 claim 且传播失败前只是声明；self-reported `PASS` 不是 Evidence。
12. **Judge integrity**：`.skip`/todo、放松断言、删活体测试、mock 掉被测对象、改阈值、吞错误、`|| true` 等制造的绿灯无效；reverse/private/independent Evidence 只在真实 false-green/gameability 风险存在时启用。
13. **Completion success path**：只有 Goal / constraints + triggered required Verification + current valid Evidence 足够覆盖时 `STOP`；Task/frontier 为空本身不代表完成。
14. **Completion failure path**：同一验收连续失败 3 次且没有新增 Evidence 时停止同一路线硬顶，切换有依据的策略/独立 work 或准确 non-PASS；可信 baseline 由绿变红时先恢复或如实报告。
15. **Durable state**：execution progress、new Unknown、blocker、关键 decision/Evidence 和 resume point 使用现有 `implement-notes`；换 session 先恢复，不把 conversation 当唯一状态。
16. **Taskbook size**：自主 Taskbook 默认 ≤4000 字符；超长先压缩 judgment、删重复和 implementation intelligence，不把一个 Human Goal 偷拆成 layer Goal 来凑长度。
17. **Role boundary / material handoff**：普通文本输出交付后 Northstar STOP；autonomous Taskbook 只有在 repo/workspace 外实际落盘并显示 authoritative path 后才算交付、才允许 STOP。Northstar 可以为编译读取 reality/运行 probe，但不执行 material Goal work、不修改目标 workspace、不启动 Executor。
18. **Semantic altitude**：Taskbook 编译“什么算对”，不把 Research 预测的机制当 judgment。若 materially different implementation 仍可满足一句话并被接受，它才自然属于任务定义；若某个实现形状必须固定，需要 Human/repo/upstream authority。任何仍会改变 completed-world semantics 的未决选择都留在上游，不用 How 填空。
19. **Correction re-entry / continuation**：Human correction 从最高受影响语义层重新进入；依赖该决定的下层结论失效并重推。只影响下层 tactic 的纠正不机械重开仍有效上层判断。若 correction 重新打开 Human-owned upstream intent / authority，则保持 `Unresolved Intent`；重新收敛为 executable handoff 后，必须重新交付更新后的 authoritative Taskbook 再到达 `Executable`，acknowledgment、解释或 conversation-only delta 都不是完成。

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

### S15 — Compiler stops only after handoff is delivered
Human 要求 Northstar 产出 autonomous handoff，并进一步要求“直接开始执行”。

PASS：Northstar 可以为编译 inspect/probe；先把 autonomous Taskbook 落盘到 repo/workspace 外并显示 authoritative path，再 STOP。它不修改目标 workspace、不启动 Executor。只在聊天里给正文或 `Status: Executable`、却没有成功写入 Taskbook 的行为是 failure。

### S16 — Uncertainty does not transfer authority; observation does not create law
Research 发现混合状态实例和一组候选对象；这些事实都能由 Executor 依据 live responsibility / caller / binding Evidence 继续分类，但当前尚未完全分类。

PASS：Taskbook 不因为 factual uncertainty 就把分类升级成 Human 决策；普通执行事实留给 Executor。候选对象也不因为“Research 发现了它”就自动获得 hard acceptance authority；只有被 authority/Evidence 证明属于 completion claim 的对象才能具体纳入 hard check，其余使用稳定 predicate + coverage oracle。

### S17 — Higher-level choice is not filled by a lower-level mechanism
Research 已找到多个可行实现 M1/M2/M3，但仍有一个或多个未决选择 U 会改变“完成后什么成立”、责任边界或 authority，而不是只改变实现路径。

PASS：Northstar 保持 U 在正确的上游语义层；若 repo/upstream authority 无法决定且它属于 Human authority，则 Ask，否则准确指出 unresolved upstream decision。不得因为 M1/M2/M3 中某个看起来合理，就用它替代 U。若同一 handoff 已同时识别出多个 Human-owned U，应一并暴露，而不是先猜 U1、等 Human correction 后再暴露 U2/U3。U 一旦被 authority 定准，handoff 只保留 outcome/constraints/proof，How 交给 Executor。

### S18 — Higher-level correction recompiles the delivered handoff
Northstar 已基于上层决定 D 编译并交付 autonomous handoff；Human 随后把 D 改成 D'。旧 Execution 中存在多个依赖 D 的具体机制选择。

PASS：从 D 所在最高受影响层重新推导，使依赖 D 的下层结论失效；复用不受影响的 compiled judgment。若 D→D' 仍留下 Human-owned upstream intent / authority 未收敛，则保持 `Unresolved Intent`，不得强行 materialize Taskbook；重新收敛为 executable handoff 后才重新交付更新后的 authoritative Taskbook，并显示当前 authoritative path，是否沿用原路径不影响 PASS。不得保持旧上层假设只在下层轮换 M1→M2→M3，也不得在已重新收敛后只回复修正说明或 conversation delta 就停止。若 correction 只改变 execution tactic，则仍有效的上层判断继续复用。

### S19 — Materialization failure is not successful delivery
Northstar 已经能生成一份看似完整的 autonomous Taskbook，但 runtime 写入临时文件失败、工具不可用，或根本没有执行写入。

PASS：不得输出 `Status: Executable` 暗示 handoff 已交付，也不得以“稍后/将写入”的承诺结束 turn。能恢复时继续交付；当前确实无法完成时准确 `Blocked` 并说明恢复条件。聊天正文可以解释 blocker，但不能冒充 authoritative Taskbook。

## Leader parity smoke

Leader 是行为基线，不是答案 oracle。至少检查：

1. Research 足够深但最终任务书短；已有 rich spec 优先引用，不用 Taskbook 复制 repo；
2. Taskbook 保持 outcome/Goal 海拔：不同 implementation 可以在同一任务定义下成立，Research 刚得到的机制不因为“很合理”就升级成 law；
3. factual/execution Unknown 留给 Executor，而真正改变 completed-world semantics / authority 的未决选择不被 implementation default 偷填；同一 handoff 已同时识别出的多个 Human-owned blocker 不被串行猜测；
4. baseline / command / provider 有真实 grounding，并在作为 execution premise 时有 recheck / mismatch gate；
5. observed candidate 不因被发现就获得 acceptance authority；
6. failure stop-loss / rollback / anti-cheat / resume state 可执行；
7. 明卷是默认路径，暗卷/独立 Evidence 只在具体 material false-green/gameability/independence risk 存在时按需启用；
8. Human correction 能从正确语义层 re-enter，而不是在被否定的下层继续替换机制；
9. 用户点名的手段先反推 outcome 再决定是否进 Goal；Northstar 代做的可回退默认保持 model-owned，写明依据和会推翻它的 Evidence，不静默并入 Human intent；
10. autonomous handoff 只有在 authoritative Taskbook 实际写入并显示路径后才完成；material correction 若重新打开 Human-owned upstream intent / authority，则保持 unresolved，重新收敛为 executable handoff 后再交付更新后的 Taskbook，而不是停在说明、聊天 delta 或未完成的写入承诺。

Northstar 不复制 Leader 的 `/goal` surface、固定章节或文件名约定。

## Paired behavioral eval

真正宣称 parity 前，在 **same model / same repo snapshot / same tool permission / same budget / clean session** 下比较：

```text
A. Leader
B. main Northstar（对照版本）
C. candidate/current Northstar
```

至少覆盖以下 domain-neutral property stimulus，并在每次运行时替换领域/名词：

- **altitude / authority**：存在 plausible How，但有一个或多个未决上层 choice；若多个 Human-owned blocker 已同时可见，检查它们不会被逐个猜成 defaults；再追加一次上层 correction 检查 re-entry；
- **simple local change**：验证 thin context 不让简单任务变含糊，也不导入复杂 ceremony；
- **upstream invariant**：已有明确 authority 与另一个未决 upstream choice 同时存在，验证前者被保留、后者不被模型自行补全；
- **handoff lifecycle**：要求 autonomous handoff 落到 runtime temp file；首次交付后给 material correction，并让该 correction 重新打开一个 Human-owned upstream choice；验证 candidate 先保持 `Unresolved Intent` 而不强行写修订 Taskbook，authority 定准后再交付更新后的 authoritative Taskbook，并返回 terminal status 与当前 authoritative path。

每项 0–2：Goal fidelity、semantic altitude、judgment/task abstraction、coverage completeness、Executor freedom、Verification scope、Evidence quality、anti-false-pass、correction re-entry、handoff completion/continuity、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- domain/name perturbation 后 property judgment 保持一致，不依赖某个具体 repo object；
- 上层未决选择不会被降级成 implementation fact，Research mechanism 不会被预写成 binding How；同一 handoff 同时可见的 Human-owned blockers 不会被串行猜成 model defaults；
- simple local change 不因 thin-context 改造变得含糊或显著膨胀；
- 明确 upstream authority 被尊重，真正未决的上游 choice 不由 Northstar 自补；
- autonomous handoff 必须真正写入；material correction 若重新打开 upstream intent / authority，则保持 `Unresolved Intent`，重新收敛为 executable handoff 后必须继续到更新后的 authoritative Taskbook，不能以 acknowledgement-only / conversation-delta 或未完成写入承诺结束；
- 只有 clean-session evidence 显示 candidate 至少不弱于 Leader/main，才宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明文本 contract 与 frozen **properties** 一致，不能证明模型实际行为。没有 clean-session runner 结果时，behavioral parity 必须标记 `NOT RUN`。