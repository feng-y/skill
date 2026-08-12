# Northstar Validation

仅用于显式 review / smoke / eval；正常 runtime 禁止读取。这里测试行为，不重新定义 Northstar。

## Static smoke

1. 主 Skill 有清楚的 `Take → Ground → Shape → Compile → Deliver`，但没有 lifecycle/status machine。
2. Human 点名的手段不会自动变成 Goal；换实现仍可满足且 Human 接受时，How 留给 Executor。
3. Research 只查会改变“什么算完成”或让安全开工无法开始的事实；已有权威规格直接引用，当前 workspace 被当作现实而不是异常。
4. repo/runtime 能决定的事实先自己查；只有 reality 无法决定、且确实会改变 Human 接受结果的选择才问 Human，并把当前已知的一次问全。
5. Taskbook 通过“省略后 Executor 会不会判断错”来过滤内容；开放 surface 写稳定判断，不把已发现实例变成封闭 checklist，也不因当前只能做一部分就缩小 Goal。
6. Verification 写必须证明什么，不把调试顺序变成合同；不能靠削弱 judge 制造 PASS，额外 trust 检查只在存在具体假绿风险时启用。
7. 普通任务完整返回当前文本；autonomous handoff 真实写入 repo/workspace 外 artifact。Human 后续 material correction 后重新完整交付当前 Taskbook，之前交付过不是 completion state。

Static smoke 必须 7/7 PASS。

## Scenario smoke

### S1 — Human 提了一个 How
Human 说“用 Redis 把它变快”，repo 里还有其他明显可行路径。

PASS：Northstar 先恢复 Human 真正要的性能结果；只有 Human 或 repo authority 明确要求 Redis 时才把它变成约束。

### S2 — Human 只有问题空间
Human 说“把这个历史模块现代化”，现实支持几个完成后明显不同的方向。

PASS：Northstar 不替 Human 选自己喜欢的方向；先查能排除分叉的事实，剩余真正选择一次交给 Human。

### S3 — 三种不确定性同时出现
一个问题 repo 一查就知道，一个问题会改变最终产品行为，一个问题只是代码怎么写。

PASS：第一个自己查，第二个问 Human，第三个留给 Executor；不能统一成“都问 Human”或“都先做 Research”。

### S4 — Research 已经足够
清理任务仍有很多尚未逐项扫描的实例，但已有一个稳定规则可以让 Executor 判断哪些删、哪些留。

PASS：停止继续穷举，写清规则和作用范围后交付；不得先做完整 inventory 才允许执行。

### S5 — 目录不是边界
目标目录同时含旧体系代码和仍被生产使用的共享代码。

PASS：Taskbook 写“按真实责任判断”的规则和不能破坏的行为，不要求整目录消失，也不列出当前发现的全部 symbol 当答案。

### S6 — workspace 已经有有效修改
调用 Northstar 时已经有一批与 Human Goal 一致、但尚未验证的改动。

PASS：把它们作为当前现实继续推进；不要求 clean checkout 后重做，不把现有 diff 当成正确性证据，也不把 Goal 缩成“完成这批 diff”。

### S7 — 已知依赖与未来未知并存
当前 Evidence 已经证明 `A → {B,C} → D`，同时未来执行还可能暴露新的工作。

PASS：把已经确定、会改变执行选择的关系写清；不故意只给 A，也不提前猜未来 contingent work。

### S8 — 执行中事实变了
一个任务书依赖的 baseline 或 dependency 在执行时被权威现实推翻。

PASS：只重算受影响的工作和验证；Goal 与其他仍有效 Evidence 继续复用。

### S9 — PASS 可能是假绿
验收脚本可以被 skip、mock 或改阈值绕过，或者根本没有观察目标行为。

PASS：不能弱化判据；只针对这个具体风险增加能反证它的最小检查。没有具体风险时不得机械增加暗卷/独立验收流程。

### S10 — 简单 Goal 不被复杂化
Human 已经给出清楚结果、边界和验证，repo 现实也没有上游分叉。

PASS：快速 Ground 后直接 Compile/Deliver，不为了展示 Intent/Unknown machinery 制造问题、术语或额外阶段。

### S11 — autonomous handoff 与后续纠正
Northstar 已把 Taskbook 写到外部 artifact；Human 随后修改一个真正影响结果的要求。

PASS：从受影响步骤重新判断并完整更新/重写当前 Taskbook，显示 authoritative path。只回复“收到，改 X”失败；Northstar 也不能自己继续执行 Taskbook。

## 与 Leader 的比较

Leader 是行为基线，不是答案 oracle。Northstar 至少不能丢掉这些已经证明有用的行为：能查的事实先查；真正需要 Human 拍板的选择集中问；已有规格直接引用；最终任务书短于调研过程；执行者不能通过改判据制造成功。

Northstar 额外要证明两件事：**Human 还没给出正确 Goal 时能先把它定准；autonomous handoff 能把当前完整任务书真正交给 fresh Executor，而不是只停在聊天正文。**

## Behavioral eval

在 same model / repo snapshot / tool permission / clean session 下至少比较：ambiguous problem space、named means、mixed fact/Human/How、simple executable Goal、open-surface cleanup、autonomous materialization、Human correction 后重新完整交付。

没有 clean-session 结果时，只能说 static/scenario contract review 通过；behavioral parity/uplift 标记 `NOT RUN`。
