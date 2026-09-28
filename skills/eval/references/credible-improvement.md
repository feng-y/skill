# 可信改进

仅在评估改进结论或开展多轮优化时读取。这是现有 Eval 的 measurement judgment，不是新控制面；执行仍用项目已有 backend，候选编辑沿用已有授权与 owner。

## 信号是否支持当前决策

先固定优化目标、允许修改的 surface、最小值得采用的变化及质量/成本边界。目标可以是质量提升，也可以是在质量守住预设容差时降成本；不要在看到结果后换目标。普通回归 smoke 不要求进入 hillclimb。

抽查完整 scored trajectories，确认熟悉任务的人能依据 candidate 可见要求理解 verdict。语义 judge 对同一输出重判以检查一致性；同时排除 timeout、API error、截断、配置未生效及前次运行残留。可用时比较更强模型或更多 effort，反常结果是调查线索，不是模型必须单调或 grader 必错的裁决。

复用或重复固定 identity 下的 baseline，按独立任务与重复层级估计波动/不确定性，判断它是否小于最小有用变化；不足时补代表性任务或重复，仍不足则 `inconclusive`。近饱和评测可用于回归，但不支持继续追逐质量提升；是否转向成本/延迟取决于原目标或 Human commitment，不能为制造 headroom 填入无实际价值的难题。

## 变化能否归因并泛化

优化前固定 train / held-out 划分与 measurement identity；同一任务的重复、近似变体或共同来源不要跨组泄漏。编辑者只读 train 输入与失败轨迹，backend 对 held-out 只回传决策所需汇总；被测 actor 执行自己的 Task，但不能访问 golden、评分答案或 variant label。隔离应由已有 backend 的可见范围保证，不靠一句“不要读”。已供编辑者读取的旧 case 不能靠重新贴标签成为未见；无法隔离时明确只做诊断或回归。

每轮只提出一个可归因的根因修改，固定其余模型/环境/评测条件。读取 train failures 理解机制，不把失败原文、case ID 或答案贴进 runtime。对每个候选运行同一 measurement；改动 eval 本身时先重建可比 baseline，修测量与调 candidate 分开判断。

## 保留、回退或停止

质量目标下，train 上升但 held-out 持平是过拟合警讯，不足以保留该轮修改；可采用的改善须超过测量不确定性，并守住预设退化边界。成本目标下，成本确实下降且 train/held-out 质量均守住预设容差即可，不要求质量分数同步上涨；质量证据不足也不能叫作 parity。退化或无可辨别收益时回退该轮候选，保留上一个有证据支持的版本，不自动 merge。

连续两三轮停滞，或任何单项修复的可能收益都低于噪声时，先归并剩余 train failures 的根因，不继续堆规则。区分真实 candidate 缺口、Task 歧义、Verifier 错判、Environment/运行故障与随机性；先修 measurement，再只针对仍成立的 behavior gap 继续。不得把不可比试卷上的 score 上涨报告成 Skill 提升。

## 结果的证据边界

报告 baseline/候选身份、样本来源与覆盖、独立任务数及重复数、目标指标与不确定性估计、每轮保留/回退依据和可检查的轨迹位置。无可用 actor/backend 时报告缺失，不把场景规格、合成 scorer tests 或历史 smoke 当作本轮行为测量。

多轮用于挑选版本的 held-out 结果属于 selection evidence；要声称最终泛化，需另有未参与选择的样本或后续独立验证。没有则限定结论，不把小样本 smoke 扩成强制三份数据集。沿用 `trustworthy / needs-eval-fix / inconclusive`，不增加评分系统或状态协议。
