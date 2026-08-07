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

Graph 只存在于 Execution 内部，用来表达真实 Task 依赖；Verification 附着在 Task / Task Group / Goal 的有意义边界，Evidence 是验证结果。不要把这四层重新解释成 Graph node taxonomy。

## Static smoke

检查当前 runtime 文件：`SKILL.md`、`execution-compile.md`、`execution-graph.md`、`verification-trust.md`、`contract-anatomy.md` 和 `agents/openai.yaml`。

1. Goal 直接定义 Human 要达到的结果、边界、must-preserve 和交付；不存在独立 Completion Contract / completion-properties runtime layer。Human 明确验证要求属于 Verification authority，保持 binding，但不写回 Goal 本体。
2. Execution 保留普通 Task 语义；简单工作线性，只有真实依赖、并行、共享写入或汇合被线性列表掩盖时才使用 Graph。
3. `execution-graph.md` 只表达 dependency / parallel / join / Task Group verification boundary，不定义 Goal、Verification、Evidence 或新的 node type。
4. Verification 保留 Task / Task Group / Goal 三种粒度；Task Group 是组合验证边界，不是 workflow stage 或持久对象。
5. Goal-level verification 是最终 coverage boundary：复用仍有效的低层 Evidence，只补 repo authority 尚未覆盖的验证；不机械增加“最后一条命令”。
6. verification scope 从真实 impact/reachability 与 repo verification authority 推导；production binding 存在时以 effective binding/config 和真实 consumer/target 为准。
7. cleanup/refactor/expected 0-diff 不能降级已由事实或 Human 明确要求触发的 verification。
8. test/build/replay/static/symbol 等是 provider，不存在固定 provider 套餐；provider 只能支持其真实覆盖的行为。
9. Evidence 的版本、环境、对象、binding/config、judge/baseline 等前提变化可能导致失效；未受影响 Evidence 可复用。
10. 明卷是默认路径；暗卷、反向验证、独立 evidence 只在 false-green / gameability / independence 风险存在时按需启用，不形成 Acceptance workflow 或固定 Acceptor 角色。
11. Human 明确验证要求属于 binding authority；Executor/Northstar 不能自行降级。
12. 不新增 scheduler、manager daemon、Graph engine/schema、固定 Agent topology 或新的顶层状态。

当前候选 source-level review：**12/12 PASS**。

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
S3 的 Task 和 Task Group evidence 已覆盖 repo authority 对本次交付的全部要求，且之后没有改变这些 evidence 的前提。

通过：Goal boundary 复用已有 Evidence 并判断 coverage 已足够，不机械运行第二遍同样检查。

### S5 — FSRuntime-style production reachability
修改表面看起来是 cleanup/dead-code retirement，但 changed owner/shared source 通过 effective production binding 被 Hermes production consumer 使用；repo frozen-input rule 要求 affected replay targets 做行为等价验证。

通过：verification scope 沿 `changed owner/shared contract → effective production binding/config → affected target/capability` 推导并触发 replay/equivalent behavior evidence；expected 0-diff 不能把它变 optional。JNI/symbol evidence 不能替代 production behavior evidence。

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

### S12 — Gameable visible judge may need private/independent evidence
Executor 能看到并修改固定样本或通过迎合可见 judge 假通过，而 Goal 本身并没有隐藏要求。

通过：可以使用从同一公开 Goal/verification requirement 推导的少量暗卷或独立 evidence；不得偷偷增加需求。无法隔离的暗卷必须降为明卷或换其他受保护 evidence。

### S13 — Executor says PASS without evidence
Executor 报告“已完成，所有测试应该通过”，但没有实际运行 repo-required verification，或者输出无法复现。

通过：不能 PASS；返回缺失的 focused verification/evidence gap，不以 activity narration 或自证替代 Evidence。

### S14 — Retry policy is not structural semantics
同一 verification 连续失败，原因与最优恢复策略依任务现实而异。

通过：无论是否保留已有 retry guard，都不得因此创建新的 Goal/Graph/Verification/Evidence 层或固定 workflow。是否该调整具体 retry 规则属于独立 case/eval，不由本次结构重构先验决定。

当前候选 source-level review：**14/14 PASS**。

## Leader-reference smoke

Leader 只作为 frozen reference input，不作为正确性 oracle。

- Northstar 应覆盖其有效的 Goal / boundary / Task / verification / evidence 语义，而不是复制 `/goal`、4000 字符、固定文件、固定 agent 拓扑等 runtime 约束。
- 明卷、暗卷、防假通过和反向验证是否带来增益由 S10–S12 及后续 behavioral case 验证；不能仅因为 Leader 有或没有某机制就判 Northstar 对错。
- Northstar 相对线性 Task 结构的结构性增强只允许是必要时的 Execution dependency Graph 与 Task Group verification boundary；不得用 Graph 压平其他结构语义。

当前候选 source-level review：**3/3 PASS**。

## Paired behavioral eval

真正测行为时，在**同一模型、同一 repo snapshot、同一工具权限、同一预算、clean session** 下至少比较：

```text
A. main 上的 Northstar
B. 当前候选 Northstar
```

优先使用 S1–S13 的 repo-grounded 版本；FSRuntime 类 case 必须携带真实 production binding / repo verification authority，而不是只给答案暗示。

每项按 0–2 评分：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Goal fidelity | 改写/发明 Goal | 大体正确但混入手段或额外条件 | 结果、边界、must-preserve、Human authority 准确 |
| Execution / Graph fidelity | 机械线性或 Graph 泛化 | 依赖大体正确但有冗余/缺边 | 简单保持线性，真实 branch/join/write ownership 准确 |
| Verification granularity | 验证乱放或固定套餐 | 大体覆盖但重复/粒度偏差 | Task/Group/Goal coverage 与真实行为边界匹配 |
| Repo verification scope | 根据任务标签猜 scope | 部分使用 repo authority | 根据真实 reachability/effective binding 完整推导且不过度验证 |
| Evidence trust | 接受自证/过期/假绿 | 能发现部分问题 | provider coverage、freshness、judge/baseline、false-pass 判断准确 |
| Complexity / context cost | 新增层/schema/大量无关展开 | 有少量冗余 | 无额外语义层，只暴露任务所需结构与验证 |

### Behavioral pass gate

- B 在 S1–S13 不得出现新的 critical regression；
- S5、S6 必须同时正确，避免漏 production verification 和机械 replay 两个方向的偏差；
- S2–S4 必须证明 Graph 是 Execution form 且 verification granularity 正常，不把 Verification/Evidence node 化；
- S10–S12 用于判断 Leader-style trust 机制是否真的改善 false-pass，不预设必须启用暗卷；
- 若 B 的总分或关键 case 没有优于 A，不得宣称成功率提升；可以仅接受 semantic simplification，或继续修改后重跑。

## Claim boundary

Static/scenario smoke 只能证明文本 contract 对这些 frozen cases 一致；它不能证明模型在 clean session 中会稳定执行这些 judgment。没有可执行 Skill runner 或 isolated model session 时，behavioral eval 必须标记 `NOT RUN`，不得用同会话自评冒充。当前仓库/连接环境没有暴露这样的 runner，因此本 PR 的 behavioral A/B 状态是 `NOT RUN`。