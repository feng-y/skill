# Research Loop Regression

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。本文件记录一次真实执行 case 暴露出的通用 loop 缺口，不增加 runtime phase、state、budget、node 或 FS 特例。

## R1 — Stable Goal exits Research and starts the bounded executable frontier

Human 给出明确、可执行的 cleanup Goal：一个旧 subsystem 正在退役，需要在明确目录边界内继续删除它的实现。初始 repo Evidence 已经足以看出当前有哪些可安全删除的叶子、哪些 shared code 明显仍 live，同时仍存在没有穷尽的 consumer / dependency / external-usage Unknown。

通过：

- Goal / authority 已稳定，不因 ordinary implementation Unknown 回到 Intent Take；
- Research 只关闭真正阻止第一项 material action 的 Compile blocker；
- 当前 Evidence 已支持安全、bounded 的 ready frontier 时，直接 Compile/Run，不把尚未阻塞 frontier 的 Unknown 先转成 Task 0 或 discovery backlog；
- Graph 只表达当前已知会直接推进 Goal 的工作，并以 Goal / confirmed boundaries 作为 stop boundary；执行中发现的 adjacent residue 不自动扩 scope；
- 新 Evidence 真正挡住某个 ready leaf、证明当前 dependency 判断错误或触发 required Verification 时，只调整那个受影响节点/分支；
- runtime Evidence 只调整受影响的 contingent / invalidated Execution / Verification。

失败：

- 每次 observation 都生成新的“key question / real blocker / need to verify”；
- 把 candidate residue 的完整 reachability inventory 当成开始删除前的统一前置任务；
- 因为尚未穷尽 repo 内外 consumer、完整 dependency graph 或历史路径，就拒绝执行已经安全的叶子工作；
- 把“可能存在 repo 外 consumer”这类未证实假设升级成全局 blocker；
- 当前 Goal 已经有清楚 stop boundary，仍顺手扩大到所有相邻残留。

## Captured FS cleanup shape

示例只用于复现，不进入 runtime prior。对下面的 case，期望的 execution judgment 应接近：

```text
Goal: 让 FS implementation 在本次边界内完整退出；其他残留后续单独处理。

ready frontier:
1. 直接删除当前已经成为叶子的 FS-only 实现；
2. 直接删除只用于 FS / Hermes 并存时期的比较逻辑；
3. 随删除结果继续剥离新暴露的 FS-only 叶子；
4. 直到 FS implementation 可以完整删除；
5. STOP，不扩展到与这次退出无关的其他 residue。
```

`fea_lib` / `fea_util` 中仍被 Hermes/model_server 使用的 shared pieces 保留。类似“外部 Flink UDF 是否仍消费 libfs.so”的问题，只有它真的阻止当前准备删除的具体 leaf/branch 时才取得 Evidence；它不是开始整个 cleanup 前必须穷尽的统一 Research/Task 0。

## Claim boundary

这个 regression 只证明候选文本能表达正确的 Research closure 与 bounded-frontier judgment。没有 clean-session Skill runner / isolated model session 时，不宣称行为 uplift；真实 behavioral A/B 仍应标记 `NOT RUN`。
