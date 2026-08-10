# Research Loop Regression

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。本文件记录真实执行 case 暴露出的通用缺口，不增加 runtime phase、state、budget、node 或 FS 特例。

## R1 — Stable Goal exits Research and starts the bounded executable frontier

Human 给出明确、可执行的 cleanup Goal：一个旧 subsystem 正在退役，需要在明确目录边界内继续删除它的实现。初始 repo Evidence 已经足以看出当前有哪些可安全删除的叶子、哪些 shared code 明显仍 live，同时仍存在没有穷尽的 consumer / dependency / external-usage Unknown。

通过：

- Goal / authority 已稳定，不因 ordinary implementation Unknown 回到 Intent Take；
- Research 只关闭真正阻止第一项 material action 的 Compile blocker；
- 当前 Evidence 已支持安全、bounded 的 ready frontier 时，直接 Compile/Handoff，不把尚未阻塞 frontier 的 Unknown 先转成 Task 0 或 discovery backlog；
- Graph 只表达当前已知会直接推进 Goal 的工作，并以 Goal / confirmed boundaries 作为 stop boundary；执行中发现的 adjacent residue 不自动扩 scope；
- 新 Evidence 真正挡住某个 ready leaf、证明当前 dependency 判断错误或触发 required Verification 时，只调整那个受影响节点/分支。

失败：

- 每次 observation 都生成新的“key question / real blocker / need to verify”；
- 把 candidate residue 的完整 reachability inventory 当成开始删除前的统一前置任务；
- 因为尚未穷尽 repo 内外 consumer、完整 dependency graph 或历史路径，就拒绝编译已经安全的叶子工作；
- 把“可能存在 repo 外 consumer”这类未证实假设升级成全局 blocker；
- 当前 Goal 已经有清楚 stop boundary，仍顺手扩大到所有相邻残留。

## R2 — Taskbook is the terminal artifact, not a prelude to execution

Human 直接调用 Northstar，并使用“开始清理 / 直接完成”这类执行式措辞。为了编译任务书，Northstar 可以读取代码、grep 依赖、核对 repo rule 或运行不会实现 Goal delta 的 probe。

通过：

- Northstar 先完成 Goal / Execution / Verification / Evidence 的编译并交付 authoritative Taskbook；
- 需要文件交接时可以把同一正文写到 workspace 外的临时文件，但文件写入只属于 Handoff；
- Taskbook 交付后本次 Northstar STOP，不启动 Executor，也不继续跑 Taskbook；
- “直接完成”不把 Northstar 从 compiler 变成 Executor。

失败：

- 在 Taskbook 形成前直接 `Update` / `Delete` 目标源码，随后再补写任务书解释已经做过的修改；
- Taskbook 写完后继续删除文件、修改 BUILD、运行目标实现的 build/replay，或发明 launcher 自动启动 Executor；
- 把 material edit 当成“为了理解 reality 的 Research”；
- 因为已经误做了一部分实现，就把任务书 Goal 缩成恰好覆盖这些修改的局部交付。

## R3 — Ready frontier does not become `Layer 1`

Human Goal 是在既定边界内让旧 subsystem implementation 完整退出；Human 同时明确了推进策略：从当前叶子直接删除，删除只服务旧/新体系并存期的 comparison，继续剥离新暴露的旧体系叶子，直到 implementation root 可以删除；其他 residual 后续单独处理。

通过：

```text
Goal: 旧 subsystem implementation 在 confirmed boundary 内完整退出；其他 residual 不属于本次 Goal。

ready frontier:
1. 删除当前已经成为叶子的 old-only implementation；
2. 删除只服务 old/new coexistence 的 comparison；
3. 由后续 Evidence 暴露新的 old-only leaf 后继续剥离；
4. 直到 implementation root 可以完整删除；
5. STOP，不扩展到明确排除的 residual。
```

- 当前只看得见 comparison/debug fixture 等叶子，不把 Goal 改写成“Layer 1 cleanup”；
- Human 已确认的 leaf-first / direct-delete strategy 作为 Execution constraint 保留，不替换成完整 inventory、先重构再删除或模型自造的多层项目；
- production ops config 等相邻 residual 若不属于 confirmed Goal，只记录为 out-of-scope reality，不顺手扩入本次 Graph。

失败：

- `Goal: 清理 Layer 1`，并把 Human 原始完整退出目标推迟成未来另一本 taskbook；
- 因为当前只能安全确定部分叶子，就把 ready frontier 当作 Goal boundary；
- 模型用自己的“更稳妥”分层覆盖 Human 已明确的执行策略。

## Captured FS cleanup shape

示例只用于复现，不进入 runtime prior：`fea_lib` / `fea_util` 中仍被 Hermes/model_server 使用的 shared pieces 保留；FS-only leaf 与 FS/Hermes comparison 按 Human 给出的策略逐步退出。类似“外部 Flink UDF 是否仍消费 libfs.so”的问题，只有它真的阻止当前具体 leaf/branch 时才取得 Evidence；它不是整个 cleanup 开始前必须穷尽的统一 Research/Task 0。`model_server/production/ops/script/*.py` 中同名 runtime 配置若属于其他 residual，则按 Goal boundary 留到后续。

## Claim boundary

这些 regression 只证明候选 runtime 文本能表达 Research closure、compiler/Executor boundary、Goal preservation 与 bounded-frontier judgment。没有 clean-session Skill runner / isolated model session 时，不宣称行为 uplift；真实 behavioral A/B 仍标记 `NOT RUN`。