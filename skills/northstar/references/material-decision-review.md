# Material Decision Review

只在 Outcome Judgment 已从 claim-relevant current reality / Executor report 发现具体 signal：implementation 可能在 Taskbook / repo / upstream authority 空白处引入一个会改变长期 contract、authority、architecture、failure、security 或 Human commitment 的选择时读取。这里补 decision judgment，不增加 Decision Ledger、code-review phase、repair planner 或 manager lifecycle。

## 什么才是 material decision

一个选择只有在可能改变以下任一项时才进入本 reference：

- Human-owned 的投入、风险、长期维护或兼容承诺；
- Goal / completion contract、外部数据语义或兼容边界；
- 长期 responsibility、authority、dependency、lifecycle、failure / retry semantics；
- security / attack surface、允许访问的系统或数据范围；
- 后续同类变化必须持续遵守的 architecture boundary / invariant。

局部算法、容器类型、helper shape、命名、文件组织或可替换实现，只要没有产生这些长期后果，仍属于 Executor How，不记录、不升级 Human，也不因为 decision review 被重新设计。

## 独立审查

按以下顺序判断：

1. 从与当前 Goal / completion claims 相关的 code / config / runtime / behavior 建立**实际做出的选择**，而不是只相信 Executor 的解释；decision-first 不表示 implementation 是黑盒。
2. 判断 Taskbook / repo / upstream authority 是否已经绑定它，或它是否越过原 authority boundary。
3. 若 authority 已绑定，只建立 authority、current reality 与 contradiction；只有可能是新的 architecture fork 或 Human-owned choice 时，才继续找出真正决定选择的 Evidence / constraint 与 materially plausible alternatives。
4. 分类为：既有 contract / authority violation、仍在 Executor authority 内的可接受实现选择、需要 AE 重新判断的新 architecture fork、需要 Human authority 的 commitment，或当前 Evidence 仍不足。

这个审查由具体 signal 驱动。没有 claim-relevant signal 时，不得为了证明“没有其他隐藏 decision”扫描完整 diff、枚举所有 implementation choice 或扩大成 exhaustive decision inventory。

不强制 Executor 生成完整 decision ledger。若 Executor 提供 decision list、confidence 或“如果提问会问什么”，只把它当 audit navigation；self-reported confidence 不是 authority 或 Evidence。decision note 缺失也不表示 material decision 不存在。

Northstar 只在当前 judgment 中说明 minimum-sufficient decision basis，不创建或维护 decision SOT，也不把 rationale 累积进 Taskbook。长期持久化仍由既有 authoritative owner / source 决定：architecture decision 由 AE 与原 architecture source 判断是否记录；Human commitment 进入 Human-owned contract；普通 Executor choice 不持久化。

judge 不能为了得到干净报告而直接修改代码、生成 repair patch 或替 implementer 合理化选择。先给独立 judgment，再决定：

- **既有 Taskbook / repo / upstream authority 已绑定，但 implementation 违反**：直接判对应 claim 未成立或 authority conflict；这不是新的 architecture design，不研究 material alternatives，也不重新调用 AE。
- **Executor-owned 且符合 contract / authority**：不阻塞，也不由 Northstar 持久化。
- **新的 architecture fork**：只有 current reality 暴露了此前未决、且会改变 Target / boundary / dependency 的 material alternative 时，才把实际 choice、deciding Evidence、material alternative 与影响交给 `$architecture-evolution` 或更高受影响 compile judgment；tests green 不能静默批准。
- **Human-owned commitment**：只在 materially 改变是否做、投入、长期维护、兼容或风险姿态时回 Human。
- **与 Goal / authority / reality 冲突，或 Evidence 不足**：分别判为未成立或尚未证明，不用 confidence 补齐。

把 choice 路由给 AE / Human 只建立 blocker / re-entry surface，不等于 choice 已被解决。在对应 owner 返回 judgment，并把结果反映到当前 contract / authority 前，不得宣布 whole Goal proven。

输出只保留当前 judgment 需要的 material decision、basis、authority routing 与真实 gap；不要输出 line-by-line review、完整 decision log 或持续 audit protocol。
