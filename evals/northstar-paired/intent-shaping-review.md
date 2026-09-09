# Northstar / AE implementation review

Eval-only。方案在 commit `12173679118b601efb6327e6d6a77bf9631379ea` 先行提交，之后才开始本轮 runtime 修改。基线为 `48c200f6c336ed1480f11dd67a1bbab2ccdbc605`；原 #88 `cef0747` 只作被替换候选，不作为已接受语义。

[两轮方案评审及实施范围](intent-shaping-sdlc.md)；[18 个固定输入微探针](intent-architecture-cases.md)。所有 review 均由当前主 Agent 分不同角度完成，不是独立模型/外部 reviewer。后续远端最终核对与合入意见记录在 PR #88 的 review comment。

## Implementation R1 — 契约一致性

对象：从 main 生成的 `implementation-r1.diff`；当前主 Agent 的逐项 diff/reference review，不是模型行为实验。

| 严重度 | 发现 | 修复 |
| --- | --- | --- |
| P1 | outcome-judgment 看到 signal 后直接按 contract 失效处理，会把未核实提示升级成事实。 | 必须核实遗漏/新增承诺；authority 不明只保留缺口，不能信任 report 或猜测。 |
| P2 | root 开头允许 shaping-only，但后面的“就直接 compile”和 Human correction 后“完整重交付 Taskbook”仍是无条件表述。 | 限定到需要执行约定/已有 Taskbook 的输入；判断类请求交付判断，不制造执行产物。 |
| P2 | AE 的“不新增 ADR”可能覆盖用户/仓库已经绑定的表示要求。 | 改成不额外引入强制 ADR/ledger；保留已有 authority-bound representation。 |
| P2 | intent-shaping 把“实验 vs obligation”具体案例写进 runtime，且 root reality filter 未显式包括原问题/委托。 | 将案例留在 eval，runtime 仅保留投入/义务区分原则；补齐原问题与当前委托的 bounded reality discriminator。 |

处理：上述缺陷均在 R2 前修复。没有删除 Graph 完整度、真实依赖、候选 Evidence 核实、独立判卷或结构退出要求。

## Implementation R2 — 正反场景与职责归属

对象：R1 修复后的候选，18 个固定输入微探针；人工契约 review，不是 18 次模型运行。

发现并修复：Northstar 的“评估”表述过宽，可能被理解成接管任意技术评审。root、YAML 和 shaping reference 收敛为意图/取舍判断；专业架构问题仍由 AE 承担。交接所需 authority 无法核实时，显式保留缺口，不把缺失出处压缩成“已批准”。

| 探针 | 对照判断 | 契约审查结果 |
| --- | --- | --- |
| F1a/F1b | 评估与已授权实施不能混淆；宿主不能在交接处提前停止；更新 PR 不等于 merge。 | root 输入路由/交付边界明确；专业研究不归 Northstar。 |
| F2a/F2b | 不需要 Goal 标题；下游无法访问链接时仍应恢复已核实的必要意图。 | compile 的内容义务与来源约束闭合；无并行 SOT。 |
| F3a/F3b | 相同数值结果不抹掉投入/义务差别。 | root 与 shaping 保留决定性理由，Human 承诺没有转交 AE。 |
| F4a/F4b/F4c | 局部错误不触发重构；真实知识泄漏触发边界判断；条件咨询不等于承诺。 | 原战略主体与新增入口兼容，没有强制 pipeline。 |
| F5a/F5b | 假退出应拒绝，真实独立 authority 的合法依赖不能为减 edge 被吞并。 | 原有 real exit、behavior/architecture proof 分离规则保留。 |
| F6a/F6b/F6c/F6d | 实现、结构、真正意图变化、环境失败分别归正确 owner。 | 只重算受影响前提；不将用户后来变更记为原先失败。 |
| F6e/F6f | 交接偏离原 authority 与仅有未核实 signal 必须不同。 | 只有核实确认才判 contract 失效；缺证据不虚构错误。 |
| F6g | 近期 Program 小，不表示长期 Target 小。 | main 原有 Target/Program discriminator 原样保留。 |

原 Northstar S1-S40 和 AE P/V 等案例继续适用于其原输入，未标成运行通过。重点对照保留了 Graph 完整度、独立分支、safe start、同文交接、false-vs-unproven、candidate-Evidence gating、真实独立责任、representation authority 和 real exit。

R2 修复后，没有发现新的阻塞契约冲突。最后一轮只核对实际发布 diff、元数据/链接及远端内容一致性；不重复声称行为收益。

## 验证证据与限制

本地实际执行了两个 Skill 的 YAML/frontmatter 解析、两个 invocation YAML 的键和 skill 名检查、相对链接/运行时不引用 eval 的检查、UTF-8/结尾换行/尾随空白检查；逐字比较保留的 Northstar Graph、Verification，以及 AE Strategic Design 主体、判断 discriminator 四段。18 个事实卡均有独立 ID、固定事实、exact prompt、应观察与应拒绝内容。它们是输入与判据，不是模型运行结果。

实际执行环境有 Python、Git 和 Node，但没有 Codex/Claude CLI；未发现已连接可用于 clean-session 的远端执行入口。容器 git clone 因 DNS 失败，使用 GitHub connector 读取的固定版本文本构建局部快照；七个基线文件的 Git blob SHA 与远端一致，不宣称完成了全仓 checkout 或工作负载测试。未修改的 RDR/Unknowns/scorer 没有重跑无关测试。

本轮未运行 clean-session / fresh-Executor。不能宣称减少确认、降低 token/latency、提高成功率，也不能把微探针当成 paired eval 所需真实任务。静态一致性/人工契约 review 通过与行为收益未证明可以同时成立；发现剩余契约或包装缺陷仍应阻止合入，不能用缺少模型环境掩盖它们。

## 变更审查依据

新增语义由现有 Intent take/compile 和 AE responsibility/decision 所有，不新建 owner。根入口仅说明当前委托和必要交付；细节仍按需进入已有 references。保留原 Goal/Graph/Verification/Evidence、Human choice、authority-bound representation、独立判卷与结构退出语义。根 AGENTS.md、Northstar execution-compile / material-decision-review、AE strategic-design 和既有 validation 保持原样；新增微探针按输入形态补充它们，不把原执行场景改成纯聊天。

上一候选重写了 AE 主体；本轮回到 main 保留战略判定内容，仅修改入口、条件咨询、复用决定性依据和反馈归属。文件变长或变短均不是验收指标。

## Implementation R3 — 包装与发布前收口

Git diff 检查发现微探针文件 EOF 多余空行，已删除；README 仍使用过宽的“评估”字样，已与 runtime 收敛为意图/取舍评估。修复后重新核对相关文本与 `git diff --check`。不为这两个局部修复重新宣称整套行为测试。

远端收口复核又发现 F1b/F2b/F5b 的事实卡依赖前一案例，单独给出时不自足；已展开为独立事实，F1b 明示已接受方案及允许改动的范围。随后只复核这三项输入与文件格式，不重跑未变化的 runtime 检查。
