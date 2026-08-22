# Outcome Judgment

只在输入已经是 Executor outcome / completion report / Evidence，且存在当前 authoritative Taskbook 时读取。这里负责**独立判卷**：判断 Taskbook 承诺的完成世界是否已经成为 current reality，同时作为 Execution 中 Graph 演进的 Evidence feedback boundary。先判当前 outcome、核实 candidate Evidence；若 implementation 可能在 contract 空白处引入 material decision，再按需读取 [material-decision-review.md](material-decision-review.md)；最后决定受影响 Graph 或更高 judgment 是否需要演进。这里不是 execution replay、repair planning 或 manager loop。

## Judge context：先合同，再现实，再报告

判卷顺序本身是 independence boundary：

1. 先读取当前 authoritative Taskbook，以及之后仍有效的 Human correction / repo / upstream authority；从中恢复 Goal、binding constraints、completion claims 和真正需要证明的 material boundaries。
2. 再针对这些 claims 检查 current repo/runtime reality，只读取足以判断 outcome 的 territory；不要因为 Executor 改过哪些文件就把 judging scope 缩成 diff。
3. 最后消费 Executor report / task checklist / test output / decision note。它们只能作为 candidate Evidence、定位线索或需要核实的 claim，不能先替 judge 定义“完成了什么”或“为什么这样做”，也不能在核实前改变 Graph。

若 Executor narrative 与 authoritative Taskbook 或 verified reality 冲突，以 Taskbook / current authority / verified reality 为准。不要为了独立而重做完整 Research；只补当前 outcome judgment 真正需要的 Evidence。

## 重建实际完成世界

不要按“做了哪些步骤”判卷，要重建**现在实际成立什么**。

对每个 material Goal / binding / completion claim：

- 找到能直接观察它的当前 reality / authoritative Evidence；
- claim 涉及真实 consumer、runtime binding、ownership、compatibility 或 failure behavior 时，检查对应真实路径，而不是只看实现附近的局部检查；
- current workspace 就是 reality，已提交 commit、已修改文件或 tests green 都不能替代 outcome；
- 一个 material work cut 自己通过，不代表跨 cut 的 Goal-level outcome 自动成立。

Taskbook 没有要求的 architecture、style、test form 或 implementation preference 不得在判卷时新增成 success criterion。

## Contract 空白中的 material choice trigger

若 claim-relevant current reality 或 Executor report 暴露具体 signal，表明 implementation 在 Taskbook / repo / upstream authority 未规定处做了一个选择，而且该选择可能改变 Human commitment、Goal / compatibility、长期 responsibility / authority / dependency / lifecycle / failure / retry、security / attack surface 或 architecture invariant，读取 [material-decision-review.md](material-decision-review.md) 做独立判断。

普通算法、容器、helper、命名、文件组织和其他可替换 How 不触发。decision note / confidence 只是线索，缺少 ledger 也不表示 choice 不存在；必要时仍读取代码 / config / runtime 作为 current reality Evidence。没有具体 signal 时，不得为了证明“没有其他隐藏 decision”扩大到完整 diff / implementation inventory 或穷举所有实现选择。

## Evidence 与反证

Evidence 必须对当前 claim 有足够直接性、authority、provenance、freshness，并能传播失败。Executor 自报 `PASS`、命令存在、测试名匹配、artifact presence 或“高置信 decision”本身都不是 proof。

对高价值 claim 做最小反证判断：**有没有一个便宜且 material 的 current-reality check，能直接推翻 Executor 的完成叙述或 material decision rationale？** 有就检查；没有具体风险时不要为了“更严格”扩大成 exhaustive adversarial research。

如果存在具体“实现错了但当前检查仍可能 PASS”的风险，读 [verification-trust.md](verification-trust.md)，只补能反证该风险的最小检查。

缺少 Evidence 与 Evidence 证明 claim 为假必须区分：

- reality / Evidence 已与 claim 冲突 → claim 未成立；
- 当前 Evidence 还不足以判断 → claim 尚未被证明；
- 不得把“没证明”虚构成 implementation defect，也不得把“没发现反例”当作证明。

## Whole-Goal judgment

最后重新对整个 Goal 判卷，而不是把局部 green 汇总成 PASS。接受前必须同时成立：

- 所有 material Goal / binding / completion claims 都有足够 Evidence；
- 没有 current reality 与这些 claims 发生 material contradiction；
- 已知 residue、partial path、legacy authority 或 runtime branch 没有让 Goal 在真实作用域中仍然不成立；
- Evidence 覆盖的是 Taskbook 要求的真实 outcome，而不是仅覆盖 patch proximity；
- current Evidence 已暴露的 contract-silent material choices 已完成独立判断：仍在 Executor authority 内的 choice 已确认符合 contract / authority；需要更高 authority 的 choice 已由对应 owner 解决并反映到当前 contract / authority。

最后一项不是要求证明“implementation 中不存在任何其他隐藏 choice”。没有具体 signal 时不扩大 Research；一个合法的普通 implementation choice也不因未写 decision note 而阻塞完成。**Routing 不等于 resolution**：只把 choice 交给 AE / Human、但对应 judgment 尚未返回时，它仍是 blocker，不能作为 Goal acceptance Evidence。一个 integration / ownership / compatibility outcome 可以跨多个 implementation cut；局部 checks 全绿仍可能整体不成立。

需要表达**任务完成度**时，按 material claim coverage 说明哪些已经证明、哪些被反证、哪些尚未证明，以及哪个 gap 阻止 whole Goal 成立。不要把 task 数、diff 大小、测试数量或 `7/8 tasks` 换算成完成百分比；这些活动量不代表 Goal coverage。

## 判卷之后

判卷先产生当前 judgment，再决定同一 Goal 的 Execution 中 Graph 或更高层 decision 是否需要更新；不能跳过 judgment 直接把 Executor report / decision note 编成 repair plan：

- **Goal 已证明**：接受当前 outcome，并给出支持它的 material Evidence basis。若当前接受结论必须解释一个已核实的 material choice，只在本次 judgment 中说明 minimum-sufficient basis；Northstar 不创建或维护 decision SOT，也不把 rationale 累积进 Taskbook。
- **Taskbook 仍有效，且只是已有 claim 未成立 / 尚未证明**：指出精确 claim、当前 counter-Evidence / missing Evidence，以及它为什么 material；若核实后的 Evidence 没有改变剩余 material work / dependency，就不要把 gap 改写成 file/helper/test tasklist。
- **Taskbook 仍有效，但 established Evidence / new reality 让原先 contingent 的 material work 成为真实工作，或改变剩余 work / dependency**：只重新进入受影响的 Execution dependency cone，按 Graph 扩展、删除、拆分、合并或重排真正受影响的 work，并按最新 reality 完整重交付 Taskbook；无关 Graph、Goal 和仍有效 Evidence 继续复用。
- **核实后的 contract-silent material choice**：既有 Taskbook / repo / upstream authority 已绑定而 implementation 违反时，直接判对应 claim 未成立或 authority conflict，不研究 material alternatives，也不重新调用 AE；仍在 Executor authority 内且符合 contract 时不阻塞；只有 current reality 暴露此前未决、会改变 Target / boundary / dependency 的新 architecture fork 时才交给 `$architecture-evolution` 或更高受影响 compile judgment；真正改变投入、长期维护、兼容或风险承诺时才回 Human。路由到 AE / Human 只建立 blocker / re-entry surface，在对应 judgment 返回并更新当前 contract / authority 前，不得宣布 whole Goal proven。
- **Taskbook premise / authority / completion contract 被新 reality 推翻**：从更高的受影响 Intent take / Intent compile judgment 重新进入；不把一个已失效 contract 当 repair specification。
- **缺少判卷所必需的 authoritative reality**：准确说明 blocker 与恢复条件；不接受 Executor self-report 代替。

普通 implementation failure 不返回 Human。只有出现新的 Human-owned choice / 授权，或 reality 使安全继续本身需要 Human 决定时才回 Human。

输出保持 minimum-sufficient：若只需要 judgment，就给结论、material claim basis、当前判断必须说明的 material choice 与真实 gap；是否长期持久化由既有 authoritative owner / source 决定，不属于 Northstar。若 established Evidence 已改变 Execution 中的 Graph，则返回按受影响 cone 重编后的完整 Taskbook。不要输出 line-by-line code review、完整 decision log、execution progress、debug narrative 或持续监督协议。
