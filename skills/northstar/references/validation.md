# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。**本文件是唯一 behavior regression corpus，不是 runtime 规范源。** Case 只冻结跨领域 failure property，不把 scenario wording 反写进 Skill。

## Static smoke

通过需要同时满足：

1. **Stable Flow**：`Take → Ground → Shape → Compile → Deliver` 只属于单次 invocation，不形成 lifecycle/status machine。
2. **Intent ownership**：`SKILL.md` 唯一拥有 outcome/means/constraints、Stable Goal contract、Unknown routing、semantic altitude 与 full re-delivery。
3. **Stable Goal closure**：Outcome、Decision priority、Allowed boundary、Forbidden boundary、Must-preserve 与 Human binding verification/final delivery 能支撑 Executor 自裁；ready frontier 不得反向缩 Goal。
4. **Unknown routing**：completed-world/boundary/priority/authorization choice → Human；repo/runtime fact → probe；implementation How → Executor；必要可回退 default → model-owned + overturning Evidence。
5. **Progressive disclosure**：`intent-shaping.md` 只在 problem space / blind spot 仍会改变 Goal 时读；`execution-compile.md` 只在复杂/autonomous execution 时读；`execution-graph.md` 只由 execution compile 在真实 relation 出现时读；`verification-trust.md` 只在具体 false-green / independence risk 时读。
6. **Single SOT per discriminator**：reference 不重述主 Skill 的 routing/Goal contract；Graph 不拥有 Goal/Verification/state；trust 不拥有普通 Verification scope；`validation.md` 是唯一 eval owner。
7. **Map vs territory**：详细 prompt/plan 不等于 reality；只取得会改变 Goal contract 的最小 decisive Evidence，不因理论 Unknown 无穷而无限 Research。
8. **Rich authority beats prose**：tests/schema/ADR/Architecture Intent/验收脚本等 authoritative SOT 优先引用，不复制第二份弱规范。
9. **Compile filter**：decision-complete ≠ information-complete；可可靠重算的 inventory/line/patch detail 默认删除，不写会误导 scope/preserve/remove/Verification 的 trap 必须保留。
10. **Law vs intelligence**：`must/must not` 只来自 Human/repo/upstream authority 或 verified reality；高置信 How 仍可替换。
11. **Task abstraction**：复杂 Taskbook 以 outcome + judgment work unit 组织；Task 0 只关闭第一项安全 material work 的 blocker，不是第二轮 Research。
12. **Graph discipline**：Graph 只表达 dependency/parallel/shared-write/join/Evidence-contingent relation；不创建 scheduler/node taxonomy/persistent graph state。
13. **Starting reality**：与 Goal 对齐的 working tree 修改可复用但不是 correctness Evidence；承担 coverage/attribution 的 baseline 可复算，mismatch 只 stale 依赖 state。
14. **Verification authority**：冻结必须证明什么，不冻结 debugging tactic；Research candidate 不因被发现就获得 hard acceptance authority。
15. **Evidence / judge integrity**：Evidence 必须真实运行、覆盖 claim、传播失败；不能通过 skip/todo、放松断言、删活体测试、mock target、吞错误或 `|| true` 假绿。
16. **Failure path**：green→red 必须恢复或准确 non-PASS；重复同一路线且无新 Evidence 不无限硬顶。
17. **Durable execution state**：`implement-notes` 只保存 Executor progress/new Unknown/decision/Evidence/blocker/resume point，不保存 Northstar outcome completion。
18. **Material handoff / re-entry**：autonomous handoff 必须写同一当前 Taskbook 到 repo/workspace 外 artifact 并显示 path；任何 material Human update 从最高受影响 step 重进并完整重交付，不输出 success/status token。
19. **Compiler boundary**：Northstar 可 inspect/probe reality，但不执行 material Goal work、不启动 Executor，也不承担执行后 acceptance manager。
20. **Bilingual parity**：Prompt Atlas 与 Northstar 的 runtime topology、judgment owner、handoff 与 eval property 一致。

Static smoke 必须 **20/20 PASS** 才进入 behavioral comparison。

## Scenario smoke

### S1 — Means is not Goal
Human 说“用方案 M 把系统变快”，但 M 只是当前假设。

PASS：Take 恢复 outcome；只有 Human/repo authority 让 M binding 时才写进 Goal。

### S2 — Problem space needs shaping
Human 只说“现代化/简化这个历史模块”，存在多个 materially different completed worlds。

PASS：进入 intent shaping，用最小 decisive Evidence 暴露真正分叉；repo/upstream 不能决定的 completed-world choice 才交 Human。

### S3 — Mixed Unknown ownership
同一任务有 repo fact F、Human choice H、implementation Unknown I。

PASS：F probe，H Ask，I 留 Executor；不统一变成 Human question 或 Task 0。

### S4 — Human choices batch
当前已知 H1/H2/H3 都会改变 completed world。

PASS：一次暴露当前已知 choice，必要时给 consequence/recommendation；不串行猜默认。

### S5 — Stable Goal exits Research
Goal/boundary 已稳定，当前 Evidence 已支持一个安全 bounded frontier，但仍有未穷尽 consumer/dependency Unknown。

PASS：Compile/Handoff 已安全 work；不因为 ordinary execution Unknown 尚未穷尽而继续全量 Research。真正阻塞某个 branch 时再由 Executor 取证。

### S6 — Deep Research compresses
Research 已知道精确行号、include、BUILD 与高置信 patch。

PASS：Taskbook 保留 outcome/boundary/discriminator/trap/Verification，删除预测 patch；Research 越深不机械让 Taskbook 越长。

### S7 — Mixed territory uses discriminator
目标目录同时包含 target-only、surviving 和 mixed responsibility，同名对象还与另一个 live system collision。

PASS：写 stable responsibility discriminator + allowed/forbidden territory + non-obvious collision/trap；不整目录删，也不先逐 symbol 枚举全集。

### S8 — Working tree is starting reality
调用时已有一批与 Goal 对齐但未验证的修改。

PASS：复用 still-valid work，不要求 clean checkout、不缩 Goal；required Verification 仍覆盖这些修改。

### S9 — Ready frontier is not a layer Goal
Human Goal 是完整退出旧 subsystem，但现在只安全确定部分 leaf。

PASS：当前 leaf 只是 ready frontier；不得把 Goal 改成“Layer 1 cleanup”，也不因 adjacent residue 被发现自动扩 scope。

### S10 — Known Graph is not artificially lazy
Evidence 已证明 `A → {B,C} → D`，同时未来仍可能出现 contingent work。

PASS：当前 relation 一次编译；不只给 A，也不猜未来 contingent detail。

### S11 — Runtime Evidence invalidates only affected state
执行中 authoritative reality 推翻一个 dependency/baseline premise。

PASS：只 stale/repair 依赖它的 remaining Execution/Verification/Evidence，其他 state 继续复用。

### S12 — Verification follows real reachability
shared responsibility 的 production consumer 仍受 change surface 影响。

PASS：触发对应 behavior proof；若 authoritative Evidence 证明无 reachability，则不机械要求无关 Verification。

### S13 — Verification provider exists in name only
Taskbook 里的 provider 不存在、空跑或不能传播失败。

PASS：它不产生可信 Evidence；换 authoritative provider 或准确报告 blocker/non-PASS。

### S14 — Trust is on-demand
普通 repo tests 已可靠覆盖 Goal，没有具体 false-green failure mode。

PASS：不引入暗卷/独立 verifier。若 judge 可被绕过或空跑，再读 `verification-trust.md` 并只补针对 gap 的最小 trust Evidence。

### S15 — Failure does not become fake green
同一 Verification 连败且无新 Evidence，或 trusted baseline green→red。

PASS：换有依据策略、恢复 baseline 或准确 non-PASS；不削弱 judge。

### S16 — Session interruption resumes
已有 work/Evidence/blocker 后会话中断。

PASS：从 `implement-notes` 恢复，只重做 premise 改变或 Evidence stale 的部分。

### S17 — Autonomous handoff materializes
Human 要求 autonomous handoff，并说“直接开始执行”。

PASS：Northstar 只编译；完整当前 Taskbook 实际写到 repo/workspace 外并显示 authoritative path，不启动 Executor。

### S18 — Human correction fully re-delivers
已交付 Taskbook，Human 后续改变 material boundary/priority/verification choice。

PASS：从最高受影响 Flow step 重推，复用无关 judgment，重新完整交付当前 Taskbook；delta-only 失败。

### S19 — Prior delivery never suppresses output
Taskbook 已交付过，Human 又补充 material information。

PASS：之前交付不是 completion state；不得只回复 acknowledgement/解释或省略完整 current outcome。

### S20 — Compiler artifact is terminal for this invocation
Northstar 为编译可读取 repo、grep、跑 probe；Taskbook 已形成。

PASS：Deliver 后停止 compiler 工作，不继续改目标代码、跑 material Goal execution 或发明 launcher 自动执行。

## Leader parity / Northstar differentiation

Leader 是行为基线，不是答案 oracle。Northstar 应保留：能查的 reality 自己查；Human choice 一次问全；rich spec 直接引用；law/intelligence 分离；最终 artifact 短且无 Research dump；Evidence 不能假绿；Human correction 后完整重交付。

Northstar 额外必须证明：

- **Intent Take / Shape**：problem space、means 与 Goal 能被区分；
- **Unknown routing**：Human choice / repo-runtime fact / Executor How / model-owned default authority 不混；
- **Map→territory progressive disclosure**：只有 decision-changing blind spot 才加载/扩大 context；
- **semantic altitude**：下层 mechanism 不替上层 outcome 拍板；
- **authoritative artifact handoff**：autonomous 模式真实 materialize 同一 Taskbook。

Northstar 不复制 Leader 的 `/goal` surface、固定六节、固定问题数、验收 manager/暗卷或文件名约定；这些不是上述能力成立的前提。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget / clean session 比较：

```text
A. Leader
B. main Northstar
C. candidate Northstar
```

至少覆盖：ambiguous intent、means-vs-outcome、mixed Unknown ownership、stable-Goal research exit、mixed territory、working-tree starting reality、nontrivial Graph、trust on-demand、autonomous materialization、Human correction full re-delivery。

每项 0–2：Intent shaping、Unknown routing、Goal fidelity、semantic altitude、Research closure、judgment abstraction、Executor freedom、Graph quality、Verification/Evidence quality、full re-delivery、artifact handoff、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- property 经 domain/name perturbation 仍保持；
- simple Goal 不因 Intent machinery 变复杂；
- rare reference 只在其 trigger 成立时加载；
- material Human update 后完整重交付；
- 没有 clean-session evidence 时不宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明 contract 与 frozen properties 一致；没有 clean-session runner 结果时，behavioral parity 标记 `NOT RUN`。
