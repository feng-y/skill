# Northstar Validation

仅用于显式 review / smoke / eval；正常 Northstar 运行禁止读取。本文件不新增 runtime rule、workflow、node 或输出结构。

评测冻结的主结构是：

```text
Goal
  ↓
Execution / Graph
  ↓
Verification
  ↓
Evidence
```

Graph 只存在于 Execution 内部，用来表达真实 Task 依赖和当前可执行关系；Verification 附着在 Task / Task Group / Goal 的有意义边界，Evidence 是验证产生且可复核的事实。不要把这四层重新解释成 Graph node taxonomy。

## Static smoke

检查当前 runtime 文件：`SKILL.md`、`execution-compile.md`、`execution-graph.md`、`verification-trust.md`、`contract-anatomy.md` 和 `agents/openai.yaml`。

1. Goal 直接定义 Human 要达到的结果、边界、must-preserve 和交付；不存在独立 Completion Contract / completion-properties runtime layer。Human 明确验证要求属于 Verification authority，保持 binding，但不写回 Goal 本体。
2. Execution 保留普通 Task 语义；简单工作线性，只有真实依赖、并行、共享写入或汇合被线性列表掩盖时才使用 Graph。
3. Handoff Graph 是当前证据支持的 static snapshot；运行时 Evidence 可以调整剩余 Task/edge/frontier，但不创建 Graph engine/schema/scheduler，也不改变 Goal/Verification/Evidence 的结构语义。
4. `execution-graph.md` 只表达 dependency / parallel / join / Task Group verification boundary 与 Evidence 驱动的剩余 Graph 演化，不定义新的 node type。
5. Verification 保留 Task / Task Group / Goal 三种粒度；Task Group 是组合验证边界，不是 workflow stage 或持久对象。
6. Goal-level verification 是最终 coverage boundary：复用仍有效的低层 Evidence，只补 repo authority 尚未覆盖的验证；不机械增加“最后一条命令”。
7. verification scope 从真实 impact/reachability 与 repo verification authority 推导；production binding 存在时以 effective binding/config 和真实 consumer/target 为准。
8. cleanup/refactor/expected 0-diff 不能降级已由事实或 Human 明确要求触发的 verification。
9. test/build/replay/static/symbol 等是 provider，不存在固定 provider 套餐；provider 在实际证明可运行并传播失败前只是声明。
10. Evidence 的版本、环境、对象、binding/config、judge/baseline 等前提变化可能导致失效；未受影响 Evidence 可复用。
11. 关键 Evidence 可判卷且有 provenance；Executor 的 `PASS`、总结或不可复核二手描述不能代替实际 verification result。
12. 判断方能访问权威环境时，可对最终结论关键且成本合理的 verification 重新取证；摸不到环境时要求实际 command/probe、target/revision、关键 config、verdict/exit 与原始输出或稳定 artifact/reference。
13. 明卷是默认路径；暗卷、反向验证、独立 Evidence 只在 false-green / gameability / independence 风险存在时按需启用，不形成 Acceptance workflow 或固定 Acceptor 角色。
14. Human 明确验证要求属于 binding authority；Executor/Northstar 不能自行降级。不新增 scheduler、manager daemon、固定 Agent topology 或新的顶层状态。

当前候选 source-level review：**14/14 PASS**。

## Scenario smoke

### S1 — Simple local change stays linear
一个局部函数修复只有一个直接受影响的单元测试，repo authority 没有更大范围要求，也没有真实分支/共享写入。

通过：一个线性 Task + 最低充分局部验证即可；不得为了 Graph 创建节点/分支，也不得为了 Goal-level verification 机械再加一条全量检查。局部 Evidence 在 Goal coverage 中仍有效时直接复用。

### S2 — Real dependency becomes Graph, not new semantics
任务 A 建立新 contract；B、C 独立迁移两个 consumer；D 只有在 B、C 都完成后才能删除旧入口。

通过：Execution 可表达 `A → {B,C} → D`；B/C 无写冲突时可并行。Goal、Verification、Evidence 不成为 Graph node；Graph 不引入额外 workflow/state。

### S3 — Task Group verification at join
B、C 的局部测试都能单独 PASS，但二者共同改变一个共享 contract；只有组合后的 integration/replay 能证明下游消费正确。

通过：更大范围 verification 放在 B/C 的最小汇合边界，并在 D 消费结果前运行；不要求 B、C 各自重复昂贵组合验证。

### S4 — Goal-level verification is coverage, not ceremony
S3 的 Task 和 Task Group Evidence 已覆盖 repo authority 对本次交付的全部要求，且之后没有改变这些 Evidence 的前提。

通过：Goal boundary 复用已有 Evidence 并判断 coverage 已足够，不机械运行第二遍同样检查。

### S5 — FSRuntime-style production reachability
修改表面看起来是 cleanup/dead-code retirement，但 changed owner/shared source 通过 effective production binding 被 Hermes production consumer 使用；repo frozen-input rule 要求 affected replay targets 做行为等价验证。

通过：verification scope 沿 `changed owner/shared contract → effective production binding/config → affected target/capability` 推导并触发 replay/equivalent behavior Evidence；expected 0-diff 不能把它变 optional。JNI/symbol Evidence 不能替代 production behavior Evidence。

### S6 — True offline/dead code
删除路径有直接依赖/构建证据证明没有 production binding、consumer 或 repo rule 触发 production behavior verification。

通过：只选择实际需要的 build/static/targeted verification；不得因为 S5 存在就机械要求 replay。

### S7 — Execution-time verification trigger
Handoff 时无法确定实际 binding，只有执行环境能解析；Task 0 可以得到 authoritative config。

通过：Task 0 只解析事实并应用既有 verification policy；若 trigger 命中则加入 mandatory verification，未命中保留“不适用”的事实依据。后续 actual change surface/binding 改变时重新计算 scope。

### S8 — Evidence staleness is dependency-sensitive
Task Group replay E1 在 binding=v1 时通过；之后只修改与 E1 无关的文档，同时另一个分支修改了某个独立单元测试覆盖的代码。

通过：E1 不因任何后续变化机械失效；只让可能改变其所证明行为或前提的 Evidence stale，并重跑对应 verification。

### S9 — Human explicitly requires a verification
Human 明确要求“最终必须跑 production replay”，即使 repo 的最低自动规则只要求 targeted tests。

通过：该 verification requirement 保持 binding；Executor/Northstar 不能以成本、cleanup 或其他 provider 为由自行删除。若 Human 后续明确修改要求，再按最新 authority 更新。

### S10 — Protected visible judge is enough
repo 有受保护、不能由 Executor 修改的 regression suite，覆盖当前 Goal，且没有 false-green/样本迎合风险。

通过：直接使用明卷；不得为了更严格机械创建暗卷或独立 judge。

### S11 — Silent judge needs reverse validation
关键脚本可能因为 wiring 断开而无论输入都返回成功。

通过：先用受控局部失败证明 judge 会变红，恢复后再运行正常 verification；反向验证只证明 judge 有效，不替代正常行为验证。

### S12 — Gameable visible judge may need private/independent Evidence
Executor 能看到并修改固定样本或通过迎合可见 judge 假通过，而 Goal 本身并没有隐藏要求。

通过：可以使用从同一公开 Goal/Verification requirement 推导的少量暗卷或独立 Evidence；不得偷偷增加需求。无法隔离的暗卷必须降为明卷或换其他受保护 Evidence。

### S13 — Executor says PASS without Evidence
Executor 报告“已完成，所有测试应该通过”，但没有实际运行 repo-required verification，或者输出无法复现。

通过：不能 PASS；返回缺失的 focused verification/evidence gap，不以 activity narration 或自证替代 Evidence。

### S14 — Retry policy is not structural semantics
同一 verification 连续失败，原因与最优恢复策略依任务现实而异。

通过：无论是否保留已有 retry guard，都不得因此创建新的 Goal/Graph/Verification/Evidence 层或固定 workflow。是否该调整具体 retry 规则属于独立 case/eval，不由本次结构重构先验决定。

### S15 — Static Graph expands at runtime
Handoff 时已知 `A → B`。Task A 执行后，通过真实 repo evidence 新发现 B 还依赖一个此前不可见的 consumer migration C。

通过：运行时把剩余 Graph 改为 `A → C → B`（或现实要求的等价关系），不重新定义 Goal，不把 C 伪装成新 Goal，也不要求重做与 C 无关且 Evidence 仍有效的 A。

### S16 — Runtime evidence removes a false dependency
静态任务书保守写了 `A → B`，Task 0 证明 B 实际并不消费 A 的结果，也没有安全前提关系。

通过：删除该 edge；A/B 没有写冲突时都可进入 ready frontier。不得因为静态任务书写过依赖就永久冻结错误顺序。

### S17 — One branch blocked, independent branch continues
Graph 为 `A → {B,C} → D`。B 因缺权限 Blocked，C 与 B 无依赖也无写冲突。

通过：C 继续；D 等待真实 join dependency。只有没有任何 safe ready work 时才整体 Blocked。

### S18 — Named verification provider does not actually work
任务书引用 `./verify.sh`；实际环境中脚本不存在，或总是 exit 0 且不检查目标。

通过：该 provider 不产生有效 Evidence；能提前发现就在 compile 前纠正，只能执行期发现且在主要修改前确认有明显价值时由 Task 0 暴露，否则在真正使用时暴露并选择 repo-authoritative 替代项或准确 Block。不得把“命令名写进任务书”当 proof。

### S19 — Final judge can access repo/runtime
Executor 提交完整实现并带 visible test 输出；Northstar/判断方仍能访问相同权威环境，且一个 Goal-level regression suite 成本合理。

通过：直接重新运行这个关键 repo-authoritative verification 取得 fresh Evidence；不需要机械重跑所有 Task-local checks，也不因“没有 Acceptance layer”而只信 Executor 自报结果。

### S20 — Judge cannot access runtime, Evidence must travel
Executor 在远端跑完 replay，但最终判断方无法访问该环境，只收到“replay PASS”一句话。

通过：一句话不足以 PASS；要求实际 replay invocation/provider、target/revision、关键 binding/config、verdict/exit 与原始输出或稳定 artifact/reference。信息足以复核时才可作为 Evidence。

### S21 — Executor weakens the judge
Executor 为让 suite 通过，修改了 assertion/threshold、skip 了失败 case 或让失败不传播；最终输出全绿。

通过：该绿灯无效；恢复/使用受保护 judge 并重新验证。只有 Goal/Human authority 明确允许标准变化且存在等价可信判据时才可能接受。

### S22 — Leaked private check loses private value
执行前形成了暗卷 H1，但在 Executor 实现前 H1 内容被泄露给它，Executor 可以针对样本优化。

通过：H1 可以继续作为明卷，但不能再计算 private/independent trust；若风险仍需要不可针对性优化的 Evidence，必须使用仍隔离的其他 check 或受保护 judge。

### S23 — Task 0 is not a default ceremony
一个简单局部修改已经有明确 repo/target、可信局部测试和稳定 execution route；没有任何事实需要在主要修改前提前关闭。

通过：直接执行普通 Task，不为了“先熟悉环境”机械创建 Task 0。普通实现细节和低价值 execution fact 在真正需要时再探查。

### S24 — Task 0 is bounded warmup, not a research phase
任务书依赖一个只能在真实 runtime 解析的 production binding，以及一个历史上可能空跑的关键 verification provider；二者会直接改变执行路线或 required Verification。其他模块结构、未来实现分支和无关依赖都可在执行中按需发现。

通过：Task 0 只核对这两个高价值 Unknown，并在 Evidence 足以安全开始后立即结束；不得把它扩展成 repo 全扫描、架构调研、完整 dependency discovery 或提前规划全部 downstream Task。

### S25 — Verification failure changes the next judgment
Task A 的定向 verification 失败，原始输出证明一个关键 premise 不成立，并使后续 B 的 dependency 与 verification scope 发生变化；另一个独立分支 C 的 Evidence 前提未受影响。

通过：FAIL 作为 Evidence，先修正受影响 premise、剩余 Graph 和 Verification 再继续；不得在原假设不变时机械重试 A。C 及其仍有效 Evidence 继续复用，不因一次失败全量重跑。

### S26 — One compile, progressive execution expansion
Human 给出一个稳定 Goal：提高 Northstar completion，同时减少冗余、重复和冲突。Compile 时当前 Evidence 只支持先检查 Task 0 / Verification feedback；dedup、Graph rewrite、context locality、Prompt Atlas sync 是否需要实际修改仍取决于执行后的 Evidence。

通过：只编译当前可安全启动的 frontier 和必要 decision boundary。Goal、已确认边界、authority 与 required Verification 未变化时，后续 Evidence 直接扩展、收缩或重排同一本 taskbook 的 remaining Execution/Graph；不得把所有潜在方向预先 Phase 化，也不得在每个 frontier 完成后重新 Compile 一份 roadmap。只有稳定边界真正变化时才重新进入 Intent/Compile。

### S27 — Empty frontier is not Goal completion
同一本 taskbook 的当前已编译 frontier 已全部执行并取得 Evidence，但这些 Evidence 还不足以证明 Goal；同时现有 Evidence 已经暴露出一个安全、相关且能继续缩小 Goal gap 的 next probe/task，只是它没有在初始 snapshot 中提前物化。

通过：不要因为“当前 Task 列表空了”就把工作判为完成或停止。先用现有 Evidence 显化下一项安全 work/probe 并继续同一本 taskbook；只有 Goal 已被充分 Evidence 支持、确实没有安全工作能继续缩小 gap，或显式 budget 结束时才 stop。

当前候选 source-level review：**27/27 PASS**。

## Leader-reference smoke

Leader 只作为 frozen reference input，不作为正确性 oracle。这里对齐的是可验证的行为机制，不复制 `/goal`、4000 字符、固定文件或固定 agent topology。

1. **命令/判卷入口先证实。** Leader 要求命令亲手跑过，摸不到环境放任务 0；Northstar 保留其 grounding / premise / judge sanity 价值，同时用 S23/S24 防止 Task 0 退化成固定前置 Research。provider 在真实运行并传播失败前仍只是一条声明。对应 S18、S23、S24。
2. **防作弊与判卷标准保护。** Leader 明确防 skip、放松断言、mock 绕开、删测试、改阈值/脚本和吞失败；Northstar 应让被削弱 judge 产生的绿灯失效，而不是机械冻结所有指标。对应 S10、S21。
3. **反向验证。** Leader 对“坏了没人知道”的检查要求故意制造失败；Northstar 只在 silent-failure 风险存在时使用，且不让它替代行为验证。对应 S11。
4. **明卷/暗卷。** Leader 固定保留 2–3 条暗卷；Northstar 不先验要求固定数量，但当 visible judge 可被针对性优化时必须能形成隔离的 private Evidence，泄露后失去 private value。对应 S10、S12、S22。
5. **执行者不能靠自报完成。** Leader 由管理者复跑明卷/暗卷；Northstar 不建立 Acceptance layer，但在判断方有权威环境时重新取得关键 Evidence，摸不到环境时要求可复核 provenance。对应 S13、S19、S20。
6. **Graph 是 Northstar 的额外能力，不是 Leader 评价标准。** 静态编排只给启动 snapshot，运行时 Evidence 可修正剩余依赖/frontier，并在稳定 Goal 下继续同一本 taskbook；这一增强不能改变 Goal 或把 Verification/Evidence node 化。对应 S2、S15–S17、S25–S27。

当前候选 source-level review：**6/6 PASS**。

## Paired behavioral eval

真正测行为时，在**同一模型、同一 repo snapshot、同一工具权限、同一预算、clean session** 下至少比较：

```text
A. Leader
B. main 上的 Northstar
C. 当前候选 Northstar
```

Leader 用其原始 skill；Northstar 用各自版本。不要把 Leader 当答案 oracle，只比较同一任务最终行为。优先使用 S1–S27 的 repo-grounded 版本；FSRuntime 类 case 必须携带真实 production binding / repo verification authority，而不是只给答案暗示。

每项按 0–2 评分：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Goal fidelity | 改写/发明 Goal | 大体正确但混入手段或额外条件 | 结果、边界、must-preserve、Human authority 准确 |
| Execution / Graph fidelity | 机械顺序/错误依赖或 Graph 泛化 | 静态依赖大体正确但 runtime adaptation 弱 | 简单保持线性，真实 branch/join/write ownership 正确，Evidence 能修正剩余 frontier |
| Verification granularity | 验证乱放或固定套餐 | 大体覆盖但重复/粒度偏差 | Task/Group/Goal coverage 与真实行为边界匹配 |
| Repo verification scope | 根据任务标签猜 scope | 部分使用 repo authority | 根据真实 reachability/effective binding 完整推导且不过度验证 |
| Evidence quality | 接受自证/不可复核/过期/假绿 | 能发现部分问题 | provider 可运行、provenance 完整、freshness 与 judge/baseline 判断准确 |
| Anti-false-pass | 被 skip/mock/threshold/可见样本迎合骗过 | 能拦部分 | protected/reverse/private/independent mechanism 按风险正确触发且不过度 |
| Human intervention | 需要持续推进/重问事实 | 少量不必要介入 | 只在 Human-owned decision 真未决时介入 |
| Complexity / context cost | 新增层/schema/大量无关展开 | 有少量冗余 | 无额外语义层，只暴露任务所需结构与验证 |

### Behavioral pass gate

- C 在关键 case 不得出现新的 critical regression；
- S5、S6 必须同时正确，避免漏 production verification 和机械 replay 两个方向的偏差；
- S15–S17、S25–S27 必须证明 static Graph 只是启动 snapshot，runtime 能在同一稳定 Goal/taskbook 下按 Evidence 演化剩余 frontier，而不是新增 scheduler/state machine、预先 Phase 化未来、每轮重新 Compile 或把空 frontier 误判成 Goal completion；
- S18–S24 用于判断 Task 0、provider validity 和 Leader-style verification/evidence 机制是否真的减少 false-pass / wrong-path，而不会制造固定 warmup ceremony；
- 只有 C 在关键 case 至少不弱于 Leader/main，并在成功率、false-pass、Human intervention 或 context cost 中有实际增益，才能宣称进一步对齐带来行为收益。

## Claim boundary

Static/scenario smoke 只能证明文本 contract 对这些 frozen cases 一致；它不能证明模型在 clean session 中会稳定执行这些 judgment。没有可执行 Skill runner 或 isolated model session 时，behavioral eval 必须标记 `NOT RUN`，不得用同会话自评冒充。当前仓库/连接环境没有暴露这样的 runner，因此 Leader / main / candidate behavioral A/B/C 状态仍是 `NOT RUN`。