# Research Loop Regression

仅用于显式 review / smoke / eval；正常 Northstar runtime 禁止读取。本文件记录一次真实执行 case 暴露出的通用 loop 缺口，不增加 runtime phase、state、budget、node 或 FS 特例。

## R1 — Stable Goal exits Research instead of recursively discovering

Human 给出明确、可执行的 cleanup Goal：一个旧 subsystem 正在退役，需要清理两个目录中的残留代码。初始 repo Evidence 已经区分出部分明确 live 的 shared code、部分 candidate residue，以及若干仍未穷尽的 consumer / dependency / external-usage Unknown。

通过：

- Goal / authority 已稳定，不因 ordinary implementation Unknown 回到 Intent Take；
- Research 只关闭 Handoff 前真正的 Compile blocker；
- 一旦已有至少一个安全 Task 或必要 Task 0 可编译，且 Verification authority / trigger 已明确到 concrete scope/provider/target 可以安全留给执行期，立即停止 Research 并进入 Compile/Run；
- candidate residue 的 deletion-relevant reachability 可以成为 Task 0 或普通 Executor probe；
- 新 grep / dependency observation 若只是继续细化 consumer、dependency、history 或 implementation scope，不自动重新打开全局 Research；
- runtime Evidence 只调整受影响的 contingent / invalidated Execution / Verification。

失败：

- 每次 observation 都生成新的“key question / real blocker / need to verify”；
- 因为尚未穷尽 repo 内外 consumer、完整 dependency graph 或历史路径，就拒绝编译已有安全工作；
- 把“可能存在 repo 外 consumer”这类未证实假设升级成全局 blocker；
- Research 自身形成 `inspect → new Unknown → inspect more` 的递归 loop，导致明确 Goal 长时间不能进入 `Status: Executable`。

## Captured FS cleanup shape

示例只用于复现，不进入 runtime prior：

- `fea_lib` / `fea_util` 中同时存在仍被 Hermes/model_server 使用的 shared pieces 与旧 FS residue；
- 初始扫描已经足以保留明显 live code，并把 candidate residue 的 reachability 判断编译为 execution work；
- “外部 Flink UDF 是否仍消费 libfs.so”等问题只有在它会阻止对应删除分支安全推进时才需要先取得 Evidence，不要求在任何 cleanup 开始前穷尽全部 repo 外现实。

## Claim boundary

这个 regression 只证明候选文本能表达正确的 Research closure discriminator。没有 clean-session Skill runner / isolated model session 时，不宣称行为 uplift；真实 behavioral A/B 仍应标记 `NOT RUN`。
