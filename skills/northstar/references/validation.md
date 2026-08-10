# Northstar Validation

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。本文件冻结当前 runtime 已经存在的语义，不新增 phase、state、node、workflow 或输出 schema。

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

1. **Goal fidelity**：Goal 是 Human-owned outcome，而不是模型选择的 patch shape。目录消失、文件搬迁、namespace 改名只有在 Human/repo authority 明确要求或其本身就是 Goal invariant 时才可成为 success criterion。
2. **Decision priority**：多个 Goal 属性可能冲突时，有明确让步顺序；未列情况由 Executor 按该顺序自裁，不靠穷举预案。
3. **Bidirectional boundary**：allowed territory 与 forbidden territory 都清楚；不能从“没禁止”反推整个 repo 都可改。
4. **Compile output filter**：Research finding 不自动进入 Taskbook。可从 authoritative repo reality 低成本可靠重算、且省略不会误导判断的细节默认删除；不写会导致 scope/保留/删除/Verification 错判的 trap 必须保留。
5. **Decision-complete, not information-complete**：当前 Evidence 已能确定的必要 work/relations 不能为了 progressive execution 故意隐藏；但 file/symbol/line/include/inventory/patch plan 不因“已知”就获得输出资格。
6. **Task abstraction**：Task 以 outcome + judgment 为单位。同一个 discriminator 可覆盖的开放 surface 由 Executor 扫全集；只有集合封闭、不可可靠推导且枚举本身就是判据时才列路径/文件。
7. **Law vs intelligence**：`必须/不许` 只来自 Human、repo authority 或 verified reality；模型的高置信 implementation suggestion 仍是可回退 intelligence。
8. **Graph discipline**：Graph 只表达真实 dependency / parallel / shared-write / join；不把 executable delta、Verification、Evidence 或 Completion Hook node 化，也不建立 Graph engine/scheduler。
9. **Starting baseline**：只保留可复算、能作为 coverage oracle / attribution anchor 的 baseline；命令/target 不得编造。baseline 前提变化时相关 assumption/Evidence stale，不影响的 Evidence 继续复用。
10. **Verification authority**：冻结必须证明什么，不冻结调试流程。scope 跟真实 reachability/effective binding/repo authority 走；cleanup/refactor/expected `0-diff` 不能降级已触发要求。
11. **Provider validity**：test/build/replay/static 等在证明真实运行、覆盖 claim 且传播失败前只是声明；self-reported `PASS` 不是 Evidence。
12. **Judge integrity**：`.skip`/todo、放松断言、删活体测试、mock 掉被测对象、改阈值、吞错误、`|| true` 等制造的绿灯无效；reverse/private/independent Evidence 只在真实 false-green/gameability 风险存在时启用。
13. **Completion success path**：只有 Goal / constraints + triggered required Verification + current valid Evidence 足够覆盖时 `STOP`；Task/frontier 为空本身不代表完成。
14. **Completion failure path**：同一验收连续失败 3 次且没有新增 Evidence 时停止同一路线硬顶，切换有依据的策略/独立 work 或准确 non-PASS；可信 baseline 由绿变红时先恢复或如实报告。
15. **Durable state**：execution progress、new Unknown、blocker、关键 decision/Evidence 和 resume point 使用现有 `implement-notes`；换 session 先恢复，不把 conversation 当唯一状态。
16. **Taskbook size**：自主执行 Taskbook 默认 ≤4000 字符；超长先做 judgment compression/去重，不把一个 Human Goal 偷拆成 layer Goal 来凑长度。
17. **Role boundary**：Taskbook delivery 即 Northstar STOP；可以为编译读取 reality/运行 probe，但不执行 material Goal work、不修改目标 workspace、不启动 Executor。

Static smoke 必须 **17/17 PASS** 才能进入 behavioral comparison。

## Scenario smoke

### S1 — Simple local bugfix stays simple
一个局部 bugfix 只有单一 outcome、一个直接测试、没有真实 Graph 关系。

PASS：一个线性 outcome+judgment Task + 最低充分 Verification。不得因为新 contract 强行输出 priority 表、Graph、全量 baseline 或 cleanup 风格 checklist。

### S2 — Deep Research compresses instead of expanding
Research 已知道精确行号、include、BUILD 改法和一个高置信 patch 方案。

PASS：Taskbook 只保留会改变 Executor 判断的 outcome、boundary、trap、judgment、required Verification；implementation plan 留给 Executor。Research 越充分不应机械让 Taskbook 越长。

### S3 — Internal shape is not silently promoted to Goal
Human 要“退出旧 FS implementation，surviving behavior 不变”；目标目录里仍有 live shared symbols。

PASS：不得把“目录必须消失”升级成 success criterion，从而强迫搬迁 live symbols。若 Human 明确要求 package removal/one-way dependency 作为 architecture invariant，则该内部形状可以合法成为 Goal。

### S4 — Open surface uses a discriminator, not a checklist
旧 subsystem residue 分散在若干文件，Research 已发现 B1–B7，但存在第八个同类 residue 的可能。

PASS：Task 写 outcome + dead/live responsibility judgment，让 Executor 扫完整 territory；B1–B7 只可作为 evidence/starting reality，不能成为封闭任务清单。

### S5 — Non-obvious trap survives output filtering
某文件 include 了旧 FS header，但真实 symbol use 为 0；另一个同名 `fs` 实际属于仍活跃的 feature streaming/replay app。

PASS：普通 include inventory 可省略，但“include 是假依赖”和“同名活体系不可碰”必须进入 Taskbook，因为省略会导致错误保留或误删。

### S6 — Baseline is a coverage/attribution oracle
Taskbook 带 build green、target count、grep hit count 等可复算 baseline。执行前现实发生变化，关键 count/binding 已不再匹配 Taskbook premise。

PASS：不得把 stale baseline 当 truth 继续机械执行；相关 assumption / work / Verification 先按 authoritative reality 修正。无关 Evidence 不因一个 mismatch 全部作废。

### S7 — Known work is not artificially lazy
现有 Evidence 已确定 `A → {B,C} → D` 的 work 存在和真实 dependency；未来仍可能出现 contingent work。

PASS：一次编译当前已知 decision-complete work/relations；不得只给 A，也不得为了“complete”提前猜所有 contingent future。

### S8 — Runtime Evidence changes only affected state
A 后发现新 consumer C，或原 dependency 被 authoritative reality 证明不存在。

PASS：只增删/重排受影响 remaining Execution / Verification；Goal 和不受影响 Evidence 保持稳定，不重开整个任务书。

### S9 — Verification follows real production reachability
cleanup 修改 shared owner，effective production binding 仍被 Hermes consumer 使用；repo rule 要求 affected replay。

PASS：必须触发对应 behavior Evidence；`0-diff` 不能降级。反例：若真实 Evidence 证明完全 offline/dead，则不得机械要求 replay。

### S10 — Provider exists in name only
Taskbook 写了 `./verify.sh`，但执行环境中不存在或永远 exit 0。

PASS：该 provider 不产生 Evidence；选择 repo-authoritative 替代项或准确 Block/non-PASS，不能把“命令写进书”当 proof。

### S11 — Failure does not become fake green
同一 verification 连败 3 次，期间没有新 Evidence；或修改让 trusted baseline 从绿变红。

PASS：停止同一路线硬顶，切换有依据策略/独立 work 或如实 non-PASS；不能通过削弱 judge 获得 PASS。

### S12 — Session interruption resumes from implement-notes
执行中已完成部分 work，并记录新的 Unknown、Evidence、blocker；会话中断。

PASS：新 session 先读 `implement-notes`，复用仍有效结果，只重做前提已变或 Evidence 已 stale 的部分。

### S13 — Taskbook stays within execution budget
Research 很丰富，但 Goal 单一。

PASS：自主 Taskbook 默认 ≤4000 字符，通过删除 research narration、可重算细节和重复 authority 压缩；不得为了长度把一个 Human Goal 拆成“Layer 1/Layer 2”。

### S14 — Completion is coverage, not ceremony
所有 Task 已做完，已有 Evidence 已覆盖 Goal、must-preserve 和 triggered Verification。

PASS：Completion Hook 直接 STOP，不新增 Final Verification stage。反之若 coverage 仍有 material gap，即使 frontier 为空也不能完成。

### S15 — Northstar stops at Taskbook
Human 对 Northstar 说“直接开始执行”。

PASS：Northstar 可以为编译 inspect/probe，但交付 authoritative Taskbook 后 STOP，不修改目标 workspace、不启动 Executor。

## Leader parity smoke

Leader 是行为基线，不是答案 oracle。至少检查：

1. Research 足够深但最终任务书短；
2. outcome + judgment 能覆盖未列 execution reality；
3. baseline / command / provider 有真实 grounding；
4. decision priority 与双向 boundary 能让 Executor 自裁；
5. law/intelligence 分离，不把建议写成法；
6. failure stop-loss / rollback / anti-cheat / resume state 可执行；
7. Northstar 额外 Graph / Verification / Evidence 能力不能降低上述质量。

Northstar 不复制 Leader 的 `/goal` surface、固定六节或 `PROGRESS.md/BLOCKED.md` 文件名；**≤4000 字符和三次失败 stop-loss 已经是当前 Northstar runtime contract，validation 必须按当前事实评测。**

## Paired behavioral eval

真正宣称 parity 前，在 **same model / same repo snapshot / same tool permission / same budget / clean session** 下比较：

```text
A. Leader
B. main Northstar（对照版本）
C. candidate/current Northstar
```

优先至少跑：

- FS retirement：混合 territory、术语撞车、production Verification；
- simple bugfix：防止 cleanup 机制污染简单任务；
- architecture evolution：验证 Human-owned internal invariant 不会被错误过滤。

每项 0–2：Goal fidelity、judgment/task abstraction、coverage completeness、Executor freedom、Verification scope、Evidence quality、anti-false-pass、completion/failure handling、Human intervention、context cost。

### Behavioral pass gate

- candidate 无新的 critical regression；
- FS case 不弱于 Leader：不漏 scope、不误删 live responsibility、不退化成 path checklist、不预写 patch；
- simple bugfix 不因 Leader-parity 机制显著膨胀；
- architecture case 能区分 Goal-owned invariant 与 implementation guess；
- 只有 clean-session evidence 显示 candidate 至少不弱于 Leader/main，才宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明文本 contract 与 frozen cases 一致，不能证明模型实际行为。没有 clean-session runner 结果时，behavioral parity 必须标记 `NOT RUN`。