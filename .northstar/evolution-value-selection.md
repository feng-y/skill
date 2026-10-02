# 从开放改进请求发现可采纳机会

## Current Intent / Target

用户要求继续在独立分支实现并实测。当前优先目标：用户只说“完善这个 repo”，体系就能沿重要使用场景、演进热点和真实摩擦发现有价值的机会，比较收益与投入，主动推荐能力目标，再形成完整目标状态、必要变化和渐进路线。

这不要求每次强行推荐，也不以生产故障或量化 ROI 为提案门槛；可以由直接观察、适用外部先例、清楚的因果推理形成有依据的暂定提案。真正会翻转采用判断的未知仍需先关闭。效果与推广需实证，但不能让“先证明选题能力有问题”成为给出有内容方案的必经前置。

## Current → v2 Delta

- current main：b3612ee82261ff65132d21ce8503b13e223c66fb；同一实验分支的已有head：45b352876b13d31fa3f13f5ccf27284908d15e14
- 替换 v1 常驻的泛化价值段；Northstar main 只保留改进对象未定时的条件入口与完整方案/未知/停止边界
- 新增一个按需 reference：沿真实工作取材 → 因果提案 → 用当前实现、最近修复、完整已有路径及成本反驳 → 给有根据的推荐 → 接回同一个完整 Draft
- 已有路径是竞争证据，不是默认正确答案；不把总能力与子能力伪装为替代。真实新能力可以胜出，旧 roadmap 也可被新事实修正
- 明确局部修复不重新选题；Northstar仍不实现。AE、Beacon、Unknowns First、Verify、Eval及AGENTS全部不改，不加Skill/Goal/schema/controller/scorer、候选配额或新持久artifact

## Why this change

v1只有采用前的价值标准，缺少如何取得候选、如何沿实际工作发现摩擦、如何用完整路径和最近修复反驳机会的操作。v2将具体方法下沉到条件reference，替换泛化要求，不在多个章节复制标准。

这复用 CE 的 grounded ideation / pressure test、Matt 的真实变化与工作摩擦取材，保留现有 Northstar/AE 的采用、结构与完整方案职责。它是待验证的方法假设，不是已证实能力。

## Acceptance

1. 当前runtime仅上述Northstar两文件变化；入口为对象未定的开放改进请求，其他工作不强制加载或执行新方法
2. 双方在同一当前source、真实main变更历史、用户用途和外部参考权限下处理原始请求；actor看不到v2设计、旧四次结论或本轮判据
3. 判断实际产物：是否形成内容具体、有依据的可采用机会；淘汰已具备/已修/伪必要投入；推荐及完整目标、必要变化、渐进路线相接。只返回“以后诊断要改什么”不算该目标完成；有事实支持的no-change或decisive blocker仍有效
4. 不以字数、章节、指定候选数或术语给分；不把无量化收益等同不能提案，不把存在workaround等同只能维持现状
5. 预先冻结两组成对重放与两个轻量边界守卫；不按结果换题。真实对照和独立评审决定保留或撤回，无增益要直报
6. 校验skill、引用、既有instrument回归与文件完整性。在同一分支交付；用户后续已授权创建Draft PR供最终评估，仍不merge/deploy

## Fixed environment correction

v1双方无Git history、禁外部、缺当前usage资料，而repo含大量eval内容且AGENTS要求行为证据；这个组合可能把选题诱导成再诊断。不能将其直接归因runtime本体。

v2给双方同一main近期20个真实commit及diff，并允许读其祖先历史和相关外部一手源码/文档。保留正常repo资料，全部来源同等可达，历史不是当前使用频率统计；不提供某个推荐答案，不移入本方案或v1实验输出。外部读取记录来源与证据，独立审查差异。仍是planning输出，不因实施权限影响高层采用判断。

## Status / current adoption judgment

- v2 runtime：source commit c544a0f34f6f31d2b46777084151c18433912322，冻结后未按结果修稿
- 两组成对运行已完成：两 candidate 从实际维护路径采用“可移植、可信、可重跑的既有评测证据链”能力，明确当前机制、复用、相依变化、渐进路线和验收；两 baseline 仍把具体改变留给后续选题诊断
- 独立复核：旧 multi-turn runner 仍在当前 README 和 Eval adapter 中使用，新 CW 的 fresh 三段不能替代它。identity负控可复现；RDR大文件probe仅支持已知普通文件路径，非任意stdout/退出后/严格时序保证
- 两guard已完成：明确局部任务不加载机会方法；生产契约缺失时保留条件与实际closure owner、不宣称whole-ready。它们不代表所有开放发现中的未知情况
- 校验完成：6个Skill validator、51个既有instrument回归、diff检查、输入/记录完整性及独立源码/结果审读。静态测试不算行为提升
- 建议条件保留 v2 作为未合入的方法候选；不恢复 v1，不依据两对就直接推广合入。backend方案尚未实施，未扩大本轮任务

观察到的是更可采用的具体规划进展。环境已较 v1 修正，跨轮差异不能全归于方法；这又是self-repo任务，改动同时影响active instruction和可见机会集，不能声称纯instruction因果、战略最优、实际ROI或一般可靠性已证。

本轮实现/比较已结束，不增加样本、平台或后续backend实施。结果与必要证据见 [v2评估](../evals/northstar/RESULTS-opportunity-discovery-v2-2026-10-02.md)。用户后续已授权公开评估资料并创建 [Draft PR #125](https://github.com/feng-y/skill/pull/125)，当前进入最终合入评估；未merge或deploy。

## v1 retained history

v1源码commit cd06d63，结果commit 45b3528。两组旧条件下四个actor都转为诊断交接，没有确立具体能力改变；候选无可见增益，未推荐合入。两轻量守卫未观察到所测回归；其成功不等于uplift。

v1[结果与证据](../evals/northstar/RESULTS-evolution-value-selection-2026-10-02.md)保持原样，旧commit和归档不重写。v2不能改环境后把跨轮差异全归给新方法，采用判断只看v2同条件baseline/candidate。
