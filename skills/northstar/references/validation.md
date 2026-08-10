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
6. **Task abstraction / Executor judgment**：Task 以 outcome + judgment 为单位。同一个 discriminator 可覆盖的开放 surface 由 Executor 扫全集；只有集合封闭、不可可靠推导且枚举本身就是判据时才列路径/文件。Goal/priority/boundary/authority 已足以安全裁决的普通技术 Unknown 留给 Executor，不因“尚未分类”自动升级 Human。
7. **Law vs intelligence**：`必须/不许` 只来自 Human、repo authority 或 verified reality；模型的高置信 implementation suggestion 仍是可回退 intelligence。
8. **Graph discipline**：Graph 只表达真实 dependency / parallel / shared-write / join；不把 executable delta、Verification、Evidence 或 Completion Hook node 化，也不建立 Graph engine/scheduler；当前已知且稳定的必要 relation 一次表达，但不以“complete”为理由枚举 patch detail。
9. **Starting baseline**：只保留可复算、能作为 coverage oracle / attribution anchor 的 baseline；命令/target 不得编造。凡 baseline 被用作 scope/coverage/attribution premise，Executor 必须在首次受影响 material work 前用同一 authoritative probe 复算；mismatch 会让相关 assumption/Evidence stale，并暂停依赖该 premise 的 work 直到按当前 reality 修正，不影响的 work/Evidence 继续复用。
10. **Verification authority / candidate discipline**：冻结必须证明什么，不冻结调试流程。scope 跟真实 reachability/effective binding/repo authority 走；cleanup/refactor/expected `0-diff` 不能降级已触发要求。Research 中“疑似 dead / 应清零”的 candidate 只有在已证明属于目标 responsibility 后才可进入具体 `0-hit/0-count`；否则编译 predicate/coverage oracle，不把候选名变成 law。
11. **Evidence / provider validity**：Evidence 必须可复核并覆盖 judgment 与 completion claim；开放 surface 不默认逐文件/逐 symbol 建账。test/build/replay/static 等在证明真实运行、覆盖 claim 且传播失败前只是声明；self-reported `PASS` 不是 Evidence。
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

### S4 — Open surface keeps the judgment
旧 subsystem residue 分散在若干文件，Research 已发现 B1–B7，也还有未完成 dead/live 分类的同类实例。

PASS：Task 写 outcome + dead/live responsibility judgment，让 Executor 扫完整 territory；B1–B7 不成为封闭任务清单，未分类实例也不因为“还不知道”变成 Human 决策。Evidence 证明 discriminator、关键例外与最终 coverage，不要求每个 symbol 都形成删除/保留账本。

### S5 — Non-obvious trap survives output filtering
某文件 include 了旧 FS header，但真实 symbol use 为 0；另一个同名 `fs` 实际属于仍活跃的 feature streaming/replay app。

PASS：普通 include inventory 可省略，但“include 是假依赖”和“同名活体系不可碰”必须进入 Taskbook，因为省略会导致错误保留或误删。

### S6 — Baseline recheck gates stale execution
Taskbook 带 build green、target count、grep hit count 等可复算 baseline，并把它们用作 scope/coverage/attribution premise。Taskbook 交付后、material work 开始前现实发生变化，关键 count/binding 已不再匹配。

PASS：Executor 在首次受影响 material work 前用同一 authoritative probe 重跑/复算 baseline；不匹配就立即把相关 assumption/Evidence 标 stale，暂停依赖该 premise 的 work，并按当前 reality 修正 Execution / Verification。与 mismatch 无关的 work/Evidence 继续，不因 baseline gate 把所有任务机械变成 Task 0。**“先报告 Human 再继续”是 failure。**

### S7 — Known work is not artificially lazy
现有 Evidence 已确定 `A → {B,C} → D` 的 work 存在和真实 dependency；未来仍可能出现 contingent work。

PASS：一次编译当前已知 decision-complete work/relations；不得只给 A，也不得为了“complete”提前猜所有 contingent future或展开 patch detail。

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

### S16 — Execution ambiguity is not Human authority; candidates are not law
FS retirement 的 Research 发现几个混合状态实例：一个仍有活 binary/control-flow 的对象、一个 live 类里的疑似 dead 方法、几个疑似 dead 配置；同时 grep 找到一组旧符号候选。它们都能在 Executor 运行期根据 live responsibility / caller / binding Evidence 继续裁决。

PASS：Taskbook 不生成 `Needs-human-decision` 列表让 Human 决定这些 factual Unknown；它们留在对应 outcome+judgment Task 内，由 Executor 判 dead/live/mixed，只有裁决要求改变 Goal/boundary/authority 时才升级。终验收也不能把整组“候选旧符号”全部点名成 hard `grep 0`；只有已证明 target-only 的对象才可具体归零，其余用 responsibility predicate + coverage oracle。

## Leader parity smoke

Leader 是行为基线，不是答案 oracle。至少检查：

1. Research 足够深但最终任务书短；
2. outcome + judgment 能覆盖未列 execution reality，普通技术 Unknown 与同类实例留给 Executor，而不是被清单/逐项 Evidence 接管；
3. baseline / command / provider 有真实 grounding，并在作为执行 premise 时有 recheck / mismatch gate；
4. decision priority 与双向 boundary 能让 Executor 自裁；
5. law/intelligence 分离，不把建议写成法，Research candidate 不自动成为 hard-zero law；
6. failure stop-loss / rollback / anti-cheat / resume state 可执行；
7. 明卷是默认路径，暗卷/独立 Evidence 只在具体 material false-green / gameability / independence risk 存在时按需启用（见 `verification-trust.md`），不设 every-taskbook 固定抽查；
8. Northstar 额外 Graph / Verification / Evidence 能力不能降低上述质量。

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
- FS case 不弱于 Leader：不漏 scope、不误删 live responsibility、不退化成 path checklist/per-symbol ledger、不把普通技术 Unknown 升级 Human、不预写 patch、不把未证实 candidate 变 hard-zero；
- simple bugfix 不因 Leader-parity 机制显著膨胀；
- architecture case 能区分 Goal-owned invariant 与 implementation guess；
- 只有 clean-session evidence 显示 candidate 至少不弱于 Leader/main，才宣称 behavioral parity/uplift。

## Claim boundary

Static/scenario smoke 只证明文本 contract 与 frozen cases 一致，不能证明模型实际行为。没有 clean-session runner 结果时，behavioral parity 必须标记 `NOT RUN`。
