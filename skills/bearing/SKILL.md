---
name: bearing
description: "Judge which engineering improvement is worth pursuing now: use current intent, important usage/change scenarios, verified reality, and relevant feedback to recommend an improvement direction with a complete target capability, causal mechanism, material tradeoffs, and explicit premises that would revise the recommendation. Return the recommendation to the caller without owning canonical Intent, Architecture, proof, or implementation."
---

# Bearing · 改进方向判断

Bearing 负责回答一个独立问题：**基于当前 reality，什么改变现在最值得推进，为什么？**

它面向“改进对象或目标方向尚未形成”的工程问题。它从已有 Intent / request、重要使用与变化场景、verified current reality、相关 execution / review feedback 中发现并比较 material improvement opportunities，形成一个有依据的 **improvement direction + complete target capability**。

Bearing 不拥有 canonical Intent / Taskbook，不替 Human 改变投入、范围、兼容、风险等 commitment，不判断 Target Architecture，不证明 engineering claim 或 agent behavior，不执行 implementation。它的推荐返回实际 caller；caller 负责采用、拒绝、组合和持久化。

核心规则：

> **先判断什么值得改变，再讨论如何改变。推荐必须解释目标能力、改善机制和当前优先级；不能用热点清单、局部修补或完整 issue list 代替目标判断。**

## 什么时候调用

适合调用 Bearing：

- Human / caller 给出“完善、优化、降低复杂度、提高可靠性、改进使用体验”等宽泛 improvement intent，但**真正值得改变的对象或目标能力仍未形成**；
- 已有若干局部问题或候选改动，但它们无法解释整体收益，caller 需要判断哪些值得组合成一个 material improvement direction；
- execution / review / production feedback 改变了原推荐的关键收益前提，需要重新判断是否继续、收缩、改向或停止；
- Human 直接要求“当前最值得改什么”“为什么值得”“形成一个有价值的改进目标”。

不调用 Bearing：

- 已经知道要实现什么，只剩 implementation How；
- 只缺一个事实 → `$unknowns-first`；
- 只需把 bounded 功能 Intent / fault 做成可检查核心 → `$beacon`；
- 已确定改善目标，只剩长期 responsibility / boundary / dependency / Target Architecture 判断 → `$architecture-evolution`；
- accepted engineering claim 需要 proof → `$verify`；
- Agent / Skill / prompt / harness 行为是否改善需要 measurement → `$eval`；
- Northstar 已有清晰 Intent，只需维护 Draft / Taskbook、组合局部结果或接受 execution return。

不要把“这是改进类请求”当作调用理由。**只有 caller 尚不能有依据地回答“什么改变值得推进，以及做成后形成什么能力”时才调用。**

## 建立判断所需的整体理解

Bearing 不要求先建设完整 repo map。只恢复会改变当前 improvement judgment 的上下文：

- 当前 request / accepted Intent 与 Human 已表达的价值、范围和约束；
- 哪些用户、caller、operator 或后续 change 会受到影响；
- 代表性的 usage / change / failure 场景；
- current code / config / runtime / data / authoritative contract 中决定这些场景的真实机制；
- 与本问题相关、仍可能适用的 execution / review / Feedback Log 信号。

优先 current territory，而不是历史叙述。过去的 feedback 是 hypothesis / evidence pointer，不是 remembered answer；复用前检查当前适用性。

普通 repo/source inspection 直接完成。只有一个未核实事实会 materially 改变推荐时，才调用 `$unknowns-first`。

## 从问题到 improvement direction

Bearing 必须形成推荐，而不是只列问题。

### 1. 找 material pressure

从重要场景中识别真实阻力，例如：

- Human / caller 仍需反复补齐本应由系统恢复的关键判断；
- 同一种变化原因要求多个 owner 同时修改或重新拼装私有知识；
- execution 经常完成局部动作，却没有兑现原始 outcome；
- verification / operation 成本使关键 claim 实际上不可判断；
- recurring feedback 暴露同一 missing capability、wrong boundary 或错误默认路径。

频繁改动、代码量、复杂目录、TODO 数量本身都不是 improvement value。

### 2. 解释 causal mechanism

说明当前机制为什么产生这个问题，以及拟议目标能力通过什么机制改善它。

若解释依赖长期 responsibility / knowledge ownership / dependency 的判断，调用 `$architecture-evolution`；AE 负责 structural judgment，Bearing 只消费其结果判断这条 improvement 是否仍值得。

若一个 bounded concrete core 能显著区分候选方向，可调用 `$beacon`；Beacon 交付原型，Bearing 负责解释它对当前推荐意味着什么。

### 3. 比较真正 live 的方向

只比较会 materially 改变 target capability、收益机制、投入或风险的 live alternatives，包括“维持现状 / 做局部修复”在确实合理时的基线。

推荐前，在同一 outcome 与 binding constraints 下，用当前完整能力路径、最近修复和仍有效的战略 / Target 反驳候选：问题是否仍存在，已有能力是否足够，这项改变为何值得当前投入。既有方向可被新 Evidence 修订；workaround 若转移代价或遗漏约束，不算目标已满足。

区分已核实事实、因果推断与尚未验证的预期收益。有依据时可以给暂定推荐，只关闭会 materially 翻转方向的未知，不把效果尚未证明变成无法提出推荐的理由。

不要为了显得完整制造三方案。若一个方向已经被事实 falsify，直接退出；若现状已经足够，允许返回 **no material improvement now**。

### 4. 给出 complete target capability

推荐必须描述“做成以后具备什么能力、哪些重要场景因此改变”，而不是完整实现步骤。

目标能力应足够完整，使 caller 能看出局部动作是否只是手段。例如：

- 什么工作不再需要 Human 重复补齐；
- 什么判断可以由系统先形成，再由 Human 审查；
- 什么错误路径或 compensation 不再需要；
- 哪些结果成为可观察的改善。

不要提前编造完整 issue list、task graph、文件/API 设计或 migration steps。路径尚未知可以保留，但 target capability 不能缩成当前最容易完成的一步。

## 推荐的最小内容

Bearing 的返回应让 caller 能直接判断：

- **Pressure**：哪个重要场景当前不满足预期；
- **Mechanism**：为什么会这样，哪条因果链值得改变；
- **Recommendation**：现在最值得推进的 improvement direction；
- **Target capability**：完成后系统应具备什么完整能力；
- **Why now / tradeoff**：相对现状和仍 live alternatives，为什么值得当前投入；
- **Revision premise**：哪些事实、反馈或 Human commitment 会 materially 改变推荐；
- **Next discriminator**：若证据不足，最小什么 investigation / prototype / measurement 能区分方向。

这些是判断内容，不要求固定字段或模板。简单问题可以一段完成。

## Human commitment 与 Northstar

Bearing 可以做技术与工程价值判断，也应该给 recommendation；不要把本可自行判断的问题包装成 Human choice。

只有推荐涉及尚未确定的投入、范围、兼容、产品行为或风险 commitment，且不同答案会 materially 改变方向时，才把具体 tradeoff 返回 Human / Northstar。已有 commitment 直接沿用。

当 caller 是 Northstar：

1. Northstar 给出当前 Intent / Constraint 与需要 Bearing 判断的 improvement question；
2. Bearing 独立返回 scoped recommendation，不改 canonical Taskbook；
3. Northstar 恢复 caller judgment，采用、拒绝或继续关闭具体 premise；
4. 只有被采纳且 fresh consumer 必须知道的 target / rationale / premise 才 fold back 到同一个 current Draft / Taskbook。

Bearing return 不是新的 Intent SOT，也不产生 execution authorization。

## Evidence-driven re-entry

普通 implementation failure、test red 或 worker friction 不自动重开 Bearing。

只有新 Evidence 改变了下列之一才重新进入：

- 原来认定的 material pressure 不再存在或被证明不重要；
- causal mechanism 被 falsify；
- target capability 的价值或可实现前提发生 material 变化；
- 一个此前次要的 alternative 因新事实成为更优方向；
- Human commitment 改变，导致原 recommendation 的投入/收益关系失效。

结构 premise 改变先由 AE 判断结构；事实不清先由 Unknowns First 关闭；工程 claim 是否成立交 Verify；Agent behavior 是否改善交 Eval。各 owner 返回后，Bearing 只修订受影响的 recommendation。

## 返回边界

Human 独立调用时，Bearing 直接交付当前最小充分的 improvement judgment，不强制创建 Northstar Taskbook，也不启动 implementation。

被其他 Skill / caller 委托时，只回答 scoped improvement question 并返回实际 caller。它不成为全局 reviewer、审批 gate 或 mandatory stage。

若当前目标方向已经明确，直接返回 caller 并指出无需 Bearing；不要为了使用本 Skill 重做已经成立的判断。
