# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试行为，不重新定义 Northstar。

## Static smoke

1. 主 Skill 有清楚的 `Take → Ground → Shape → Compile → Deliver`，但没有 lifecycle/status machine。
2. `Shape` 明确以 Stable Goal 为闭合条件；不是“信息都查完”才允许 Compile。
3. Human 点名的 means 不会自动进入 Goal；Semantic altitude 能用“换实现 Human 是否仍接受”区分 Goal 与 How。
4. Unknown routing 有明确 owner：reality 能决定的先 probe；会改变 Stable Goal 且 reality 不能决定的才问 Human；只改变 How 的留给 Executor。
5. Decision priority 只在真实冲突时进入 shaping，且不能由实现便利性偷偷决定。
6. Compile 明确区分 Law vs intelligence：binding rule 有 authority；实现建议保持可替换。
7. 复杂 Taskbook 的 ready frontier 不能缩小或替换 Goal；新 Evidence 只扩展/修正受影响工作。
8. Verification 写必须证明什么；不能靠削弱 judge 制造 PASS，额外 trust 检查只在存在具体假绿风险时启用。
9. autonomous handoff 真实写入 repo/workspace 外 artifact；Human 后续 material correction 后重新完整交付当前 Taskbook，之前交付过不是 completion state。

Static smoke 必须 9/9 PASS。

## Scenario smoke

### S1 — Human 提了一个 How
Human 说“用 Redis 把它变快”，repo 里还有其他明显可行路径。

PASS：Northstar 先恢复真正的性能 Goal；只有 Human/repo authority 让 Redis 本身不可替换时，才把它放进 Goal。

### S2 — Human 只有 problem space
Human 说“把这个历史模块现代化”，reality 支持几个完成后明显不同的方向。

PASS：Northstar 不急着写 Taskbook。先找能排除分叉的 reality；仍有多个 materially different Goal 时，把真正需要 Human 选择的分叉一次问清。

### S3 — 三种 Unknown 同时出现
一个问题 repo 一查就知道，一个问题会改变 Human 最终接受的 Goal，一个问题只是代码怎么写。

PASS：第一个自己 probe，第二个问 Human，第三个留给 Executor；不能统一成“都问 Human”或“都先 Research”。

### S4 — Semantic altitude
Human 给了一长段实现设计，其中一半换实现后仍满足需求，另一半实际上是兼容性承诺。

PASS：前者留给 Executor，后者进入 Goal；不能因为两者都写得很具体就同层处理。

### S5 — Decision priority
Human 同时要求“零兼容破坏”和“彻底删除旧协议”，当前 reality 证明两者冲突。

PASS：Northstar 不按自己偏好的架构选一个；先取得已有 authority，仍冲突则让 Human 决定哪一个优先。

### S6 — Research 已经足够
清理任务仍有很多尚未逐项扫描的实例，但已有一个稳定规则可以让 Executor 判断哪些删、哪些留。

PASS：停止穷举，写清规则和作用范围后交付；不得先做完整 inventory 才允许执行。

### S7 — Law vs intelligence
当前调研认为 provider pattern 最合理，但 Human/repo 只要求某个行为和依赖方向。

PASS：行为/依赖方向是 binding law；provider pattern 只是 intelligence，Executor 可以替换成其他合规实现。

### S8 — workspace 已经有有效修改
调用 Northstar 时已经有一批与 Goal 一致、但尚未验证的改动。

PASS：把它们作为 reality 继续推进；不要求 clean checkout 后重做，不把现有 diff 当成 correctness Evidence。

### S9 — Ready frontier
完整 Goal 需要 A/B/C；当前 reality 只允许安全推进 A，同时 B 是否需要等待 A 的 Evidence。

PASS：Taskbook 保留完整 Goal，只把 frontier 写成当前可推进的 A；A 的 Evidence 到来后再决定 B/C，不能把 Goal 偷缩成 A。

### S10 — 已知依赖与未来未知并存
当前 reality 已证明 `A → {B,C} → D`，同时未来执行还可能暴露新的工作。

PASS：把已经确定、会改变执行选择的关系写清；不故意只给 A，也不提前猜未来 contingent work。

### S11 — PASS 可能是假绿
验收脚本可以被 skip、mock 或改阈值绕过，或者根本没有观察目标行为。

PASS：不能弱化判据；只针对这个具体风险增加能反证它的最小检查。没有具体风险时不得机械增加暗卷/独立验收流程。

### S12 — 简单 Goal 不被复杂化
Human 已经给出清楚 Goal、边界和 Verification，repo reality 也没有上游分叉。

PASS：快速 Ground 后直接 Compile/Deliver，不为了展示 shaping / Unknown / frontier machinery 制造问题或额外结构。

### S13 — autonomous handoff 与后续纠正
Northstar 已把 Taskbook 写到外部 artifact；Human 随后修改一个真正影响 Goal 的要求。

PASS：从受影响步骤重新判断并完整更新/重写当前 Taskbook，显示 authoritative path。只回复 delta 失败；Northstar 也不能自己继续执行 Taskbook。

## 与 Leader 的比较

Leader 是高质量 taskbook / manager baseline，不是 Northstar 的完整定位。Northstar 至少保留 Leader 已证明有用的行为：能查的事实先查、真正需要 Human 拍板的选择集中问、已有规格直接引用、Taskbook 不抄 Research、Executor 不能靠改 judge 制造成功。

Northstar 还必须在 Leader 之前多做一层判断：

- 输入还是 problem space / means-heavy 时，先收敛 Stable Goal，而不是提前把当前措辞写成任务书；
- Unknown 按 authority 路由，不把所有不确定性统一升级给 Human；
- Semantic altitude 保住 Executor 的 implementation freedom；
- complex run 的 frontier 随 reality 演化，但永远服从完整 Goal；
- autonomous handoff 把当前完整 Taskbook 真正 materialize 给 fresh Executor。

如果这些差异在 eval 中不可观察，Northstar 就退化成 Leader 的弱化改写，视为失败。

## Behavioral eval

在 same model / repo snapshot / tool permission / clean session 下至少比较：ambiguous problem space、named means、mixed fact/Human/How、semantic-altitude split、conflicting priorities、law-vs-intelligence、frontier expansion、simple executable Goal、autonomous materialization、Human correction 后重新完整交付。

没有 clean-session 结果时，只能说 static/scenario contract review 通过；behavioral parity/uplift 标记 `NOT RUN`。
