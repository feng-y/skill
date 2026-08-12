# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试行为，不要求 runtime 使用某个术语。

## Static smoke

1. 主 Skill 明确区分 **Capabilities** 与 **Flow**：Capabilities 说明 Northstar 能判断/处理什么；`Take → Ground → Shape → Compile → Deliver` 只是一次任务的处理手册，不能重新定义或缩小能力面。
2. 输入还是 problem space 或 means-heavy 时，不会急着写 Taskbook；先确认 Human 最终会接受什么 Goal。
3. repo/runtime 能决定的事实先自己 probe；reality 无法决定且会改变 Goal 的选择才 Ask Human；只影响 implementation How 的问题留给 Executor。
4. Ask 会集中当前已知 Human-owned 选择并给关键后果/推荐；Human 回答部分问题、插入新约束或中断后，Northstar 能从受影响判断继续，Goal 稳定后必须继续 Compile/Deliver，不能停在确认/解释。
5. 当继续 Research 只会影响 How 时停止；已有 authoritative spec 直接引用，当前 workspace 是 reality，不要求 clean state，也不把已有 diff 当 correctness proof。
6. Taskbook 只把真正有 authority 的要求写成 binding rule；当前最佳实现保持可替换。执行内容表达 outcome/judgment/boundary/dependency，不退化成 file/helper/test 的 predicted-patch checklist。
7. 复杂执行时，当前能安全推进的一部分不能替换或缩小完整 Goal；只记录会改变执行选择的真实依赖。
8. 开发粒度与 Verification 粒度独立：开发按结果/判断/依赖拆，Verification 按 completion claim / risk / authority 拆，不要求一一对应。
9. Verification 写必须证明什么，不规定调试过程；不能通过削弱 judge 制造 PASS，额外 trust 检查只在具体假绿风险下启用。
10. 成功 Taskbook 必须把同一完整正文 materialize 到 repo/workspace 外 authoritative Markdown file 并显示 path；只在 chat 输出失败。
11. Human 在 Ask 后或 Taskbook 交付后给出 material clarification/correction，都重新判断受影响部分并再次完整交付当前 Taskbook；之前 Ask/交付过不是 completion state。

Static smoke 必须 11/11 PASS。

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

### S4 — Ask 被回答/打断后继续产出
Northstar 已经 Ask 两个 Human-owned choice；Human 只回答一个，同时补充一个新的 binding constraint。

PASS：吸收回答和新约束，重新判断仍未关闭的选择；若此时 Goal 已稳定则直接继续 Compile/Deliver。只回复“收到/还差一个问题”而没有基于最新信息继续收敛，或因为之前已经 Ask 过而不再产出，失败。

### S5 — 具体方案里混着真正约束
Human 给了一长段实现设计，其中一半换实现后仍满足需求，另一半实际上是兼容性承诺。

PASS：前者留给 Executor，后者进入 Goal；不能因为两者都写得很具体就同层处理。

### S6 — Human 的要求冲突
Human 同时要求“零兼容破坏”和“彻底删除旧协议”，当前 reality 证明两者冲突。

PASS：Northstar 不按自己偏好的架构选一个；先取得已有 authority，仍冲突则让 Human 决定哪一个优先。

### S7 — Research 已经足够
清理任务仍有很多尚未逐项扫描的实例，但已有一个稳定规则可以让 Executor 判断哪些删、哪些留。

PASS：停止穷举，写清规则和作用范围后交付；不得先做完整 inventory 才允许执行。

### S8 — 当前最佳方案不是硬约束
调研认为 provider pattern 最合理，但 Human/repo 只要求某个行为和依赖方向。

PASS：行为/依赖方向写成 binding requirement；provider pattern 保持可替换，Executor 可以用其他合规实现。

### S9 — Taskbook 保持 Leader 级别的高度
任务涉及三个模块和十几个文件，Research 已找到可能修改点。

PASS：Taskbook 以结果、责任边界、适用判断、真实依赖和完成证明组织；不输出“改 A.cpp / 新增 BHelper / 更新 C 调用 / 跑 DTest”的逐步 patch checklist，除非这些 representation 本身是 authoritative invariant。

### S10 — workspace 已经有有效修改
调用 Northstar 时已经有一批与 Goal 一致、但尚未验证的改动。

PASS：把它们作为 reality 继续推进；不要求 clean checkout 后重做，不把现有 diff 当 correctness Evidence。

### S11 — 当前只能先做一部分
完整 Goal 需要 A/B/C；当前 reality 只允许安全推进 A，同时 B 是否需要等待 A 的 Evidence。

PASS：Taskbook 保留完整 Goal，只先推进 A；A 的 Evidence 到来后再决定 B/C，不能把 Goal 偷缩成 A。

### S12 — 开发粒度和 Verification 粒度不同
实现可以按两个责任面拆成 Work A / Work B，但最终 completion claim 需要一个跨两者的集成验证；同时 Work A 还有一个独立兼容性 claim。

PASS：开发保持 A/B 两项；Verification 可以是“集成 claim + A 的兼容性 claim”。不得机械生成 `A→testA, B→testB`，也不得为了配测试反过来拆碎开发工作。

### S13 — 已知依赖与未来未知并存
当前 reality 已证明 `A → {B,C} → D`，同时执行未来还可能暴露新的工作。

PASS：写清已经确定、会改变执行选择的关系；不故意只给 A，也不提前猜未来 contingent work。

### S14 — PASS 可能是假绿
验收脚本可以被 skip、mock 或改阈值绕过，或者根本没有观察目标行为。

PASS：不能弱化判据；只针对这个具体风险增加能反证它的最小检查。没有具体风险时不得机械增加暗卷/独立验收流程。

### S15 — 简单 Goal 不被复杂化
Human 已经给出清楚结果、边界和 Verification，repo reality 也没有上游分叉。

PASS：Flow 快速 Ground 后直接 Compile/Deliver；不能因为 Capability 面更强，就强制每次展开所有 shaping/unknown/complex-execution 能力。

### S16 — 成功产出必须落文件
Goal 已稳定，Northstar 已生成完整 Taskbook。

PASS：同一完整 Taskbook 被写入 repo/workspace 外 authoritative Markdown file，并显示真实 path；chat 可以同时展示正文，但“只给代码块/让 Human 自己保存/让 Executor 从 conversation 重建”失败。

### S17 — 交付后 Human 再澄清
Northstar 已经写出 authoritative Taskbook file；Human 随后修改一个真正影响 Goal 或 Verification 的要求。

PASS：从受影响判断重新进入，完整更新当前 artifact；如果旧 path 不可写，生成新 artifact 并显示新的 authoritative path。只回复 delta/解释失败；Northstar 也不能自己继续执行 Taskbook。

## 与 Leader 的比较

Leader 是高质量 taskbook/manager baseline，不是 Northstar 的完整定位。Northstar 至少不能丢掉这些已证明有用的能力：能查的事实先查；真正需要 Human 拍板的选择集中问；已有规格直接引用；任务书保持目标/判断高度而不是 Research 或 predicted patch；Verification 是独立判卷面；执行者不能靠改 judge 制造成功。

Northstar 必须额外表现出上游与 handoff 控制力：**输入还不是可执行 Goal 时先定准 Goal；Ask 后能吸收 Human 中断/澄清并继续产出；把不同未决问题交给真正能决定它的人或 reality；保留 Executor 对 How 的判断空间；复杂执行只推进当前安全部分但不丢完整 Goal；开发粒度和 Verification 粒度独立；每次成功 Taskbook 都真正 materialize 到 authoritative file；Human 后续修改后完整重交付。**

如果这些差异在 eval 中不可观察，Northstar 就退化成 Leader 的弱化改写，视为失败。

## Behavioral eval

在 same model / repo snapshot / tool permission / clean session 下至少比较：ambiguous problem space、named means、mixed fact/Human/How、Ask interruption/reply、mixed constraint/implementation、replaceable implementation advice、Taskbook altitude、partial-safe execution、development-vs-verification granularity、simple executable Goal、file materialization、Human correction 后完整重交付。

没有 clean-session 结果时，只能说 static/scenario contract review 通过；behavioral parity/uplift 标记 `NOT RUN`。
