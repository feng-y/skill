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
6. 校验skill、引用、既有instrument回归与文件完整性。只推同一分支，不PR/merge/deploy

## Fixed environment correction

v1双方无Git history、禁外部、缺当前usage资料，而repo含大量eval内容且AGENTS要求行为证据；这个组合可能把选题诱导成再诊断。不能将其直接归因runtime本体。

v2给双方同一main近期20个真实commit及diff，并允许读其祖先历史和相关外部一手源码/文档。保留正常repo资料，全部来源同等可达，历史不是当前使用频率统计；不提供某个推荐答案，不移入本方案或v1实验输出。外部读取记录来源与证据，独立审查差异。仍是planning输出，不因实施权限影响高层采用判断。

## Status / next owner

- v2 runtime：已实现并冻结，独立源码与协议评审通过
- v2 paired runs：四个actor已启动；两个已冻结轻量guards在其后运行
- 当前下一责任：运行冻结对照与guard，独立审实际产物，回写采用判断；不按结果修稿或换题
- 所有后续执行继续沿用户对本分支的授权，不扩大到PR、主线或部署

## v1 retained history

v1源码commit cd06d63，结果commit 45b3528。两组旧条件下四个actor都转为诊断交接，没有确立具体能力改变；候选无可见增益，未推荐合入。两轻量守卫未观察到所测回归；其成功不等于uplift。

v1[结果与证据](../evals/northstar/RESULTS-evolution-value-selection-2026-10-02.md)保持原样，旧commit和归档不重写。v2不能改环境后把跨轮差异全归给新方法，采用判断只看v2同条件baseline/candidate。
