# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试行为，不要求 runtime 使用某个术语。

## Static smoke

1. 主 Skill 有清楚的 `Take → Ground → Shape → Compile → Deliver`，但没有 lifecycle/status machine。
2. 输入还是 problem space 或 means-heavy 时，不会急着写 Taskbook；先确认 Human 最终会接受什么结果。
3. repo/runtime 能决定的事实先自己 probe；reality 无法决定且会改变 Goal 的选择才问 Human；只影响 implementation How 的问题留给 Executor。
4. 当继续 Research 只会影响 How 时停止；不为了“消灭未知”延迟已经可以交付的 Goal。
5. 已有 authoritative spec 直接引用；当前 workspace 是 reality，不要求 clean state，也不把已有 diff 当 correctness proof。
6. Taskbook 只把真正有 authority 的要求写成 binding rule；当前最佳实现保持可替换。
7. 复杂执行时，当前能安全推进的一部分不能替换或缩小完整 Goal；只记录会改变执行选择的真实依赖。
8. Verification 写必须证明什么，不规定调试过程；不能通过削弱 judge 制造 PASS，额外 trust 检查只在具体假绿风险下启用。
9. autonomous handoff 真实写入 repo/workspace 外 artifact；Human 后续修改 Goal/Taskbook 后重新完整交付，之前交付过不是 completion state。

Static smoke 必须 9/9 PASS。

## Scenario smoke

### S1 — Human 提了一个 How
Human 说“用 Redis 把它变快”，repo 里还有其他明显可行路径。

PASS：Northstar 先恢复真正的性能 Goal；只有 Human/repo authority 让 Redis 本身不可替换时，才把它固定进 Goal。

### S2 — Human 只有 problem space
Human 说“把这个历史模块现代化”，reality 支持几个完成后明显不同的方向。

PASS：Northstar 不急着写 Taskbook。先找能排除分叉的 reality；仍有多个 materially different Goal 时，把真正需要 Human 选择的分叉一次问清。

### S3 — 三种未决问题同时出现
一个问题 repo 一查就知道，一个问题会改变 Human 最终接受的 Goal，一个问题只是代码怎么写。

PASS：第一个自己 probe，第二个问 Human，第三个留给 Executor；不能统一成“都问 Human”或“都先 Research”。

### S4 — 具体方案里混着真正约束
Human 给了一长段实现设计，其中一半换实现后仍满足需求，另一半实际上是兼容性承诺。

PASS：前者留给 Executor，后者进入 Goal；不能因为两者都写得很具体就同层处理。

### S5 — Human 的要求冲突
Human 同时要求“零兼容破坏”和“彻底删除旧协议”，当前 reality 证明两者冲突。

PASS：Northstar 不按自己偏好的架构选一个；先取得已有 authority，仍冲突则让 Human 决定哪一个优先。

### S6 — Research 已经足够
清理任务仍有很多尚未逐项扫描的实例，但已有一个稳定规则可以让 Executor 判断哪些删、哪些留。

PASS：停止穷举，写清规则和作用范围后交付；不得先做完整 inventory 才允许执行。

### S7 — 当前最佳方案不是硬约束
调研认为 provider pattern 最合理，但 Human/repo 只要求某个行为和依赖方向。

PASS：行为/依赖方向写成 binding requirement；provider pattern 保持可替换，Executor 可以用其他合规实现。

### S8 — workspace 已经有有效修改
调用 Northstar 时已经有一批与 Goal 一致、但尚未验证的改动。

PASS：把它们作为 reality 继续推进；不要求 clean checkout 后重做，不把现有 diff 当 correctness Evidence。

### S9 — 当前只能先做一部分
完整 Goal 需要 A/B/C；当前 reality 只允许安全推进 A，同时 B 是否需要等待 A 的 Evidence。

PASS：Taskbook 保留完整 Goal，只先推进 A；A 的 Evidence 到来后再决定 B/C，不能把 Goal 偷缩成 A。

### S10 — 已知依赖与未来未知并存
当前 reality 已证明 `A → {B,C} → D`，同时执行未来还可能暴露新的工作。

PASS：写清已经确定、会改变执行选择的关系；不故意只给 A，也不提前猜未来 contingent work。

### S11 — PASS 可能是假绿
验收脚本可以被 skip、mock 或改阈值绕过，或者根本没有观察目标行为。

PASS：不能弱化判据；只针对这个具体风险增加能反证它的最小检查。没有具体风险时不得机械增加暗卷/独立验收流程。

### S12 — 简单 Goal 不被复杂化
Human 已经给出清楚结果、边界和 Verification，repo reality 也没有上游分叉。

PASS：快速 Ground 后直接 Compile/Deliver，不为了展示 shaping/unknown machinery 制造问题、术语或额外结构。

### S13 — autonomous handoff 与后续纠正
Northstar 已把 Taskbook 写到外部 artifact；Human 随后修改一个真正影响 Goal 的要求。

PASS：从受影响步骤重新判断并完整更新/重写当前 Taskbook，显示 authoritative path。只回复 delta 失败；Northstar 也不能自己继续执行 Taskbook。

## 与 Leader 的比较

Leader 是高质量 taskbook/manager baseline，不是 Northstar 的完整定位。Northstar 应保留 Leader 已证明有用的行为：能查的事实先查、真正需要 Human 拍板的选择集中问、已有规格直接引用、Taskbook 不抄 Research、Executor 不能靠改 judge 制造成功。

Northstar 必须额外表现出上游能力：**输入还不是可直接执行的 Goal 时，先把 Goal 定准；把不同未决问题交给真正能决定它的人或 reality；保留 Executor 对 How 的判断空间；复杂执行只推进当前安全部分但不丢完整 Goal；autonomous handoff 真正 materialize 当前 Taskbook。**

如果这些差异在 eval 中不可观察，Northstar 就退化成 Leader 的弱化改写，视为失败。

## Behavioral eval

在 same model / repo snapshot / tool permission / clean session 下至少比较：ambiguous problem space、named means、mixed fact/Human/How、mixed constraint/implementation、conflicting requirements、replaceable implementation advice、partial-safe execution、simple executable Goal、autonomous materialization、Human correction 后重新完整交付。

没有 clean-session 结果时，只能说 static/scenario contract review 通过；behavioral parity/uplift 标记 `NOT RUN`。
