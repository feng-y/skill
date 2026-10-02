# 宽泛改进请求的价值与演化选择

## Problem / Target

用户要求在新分支执行已讨论方案，再对照评估。Current main 已有完整 Draft / Taskbook、反馈修订、AE Target / Program、高杠杆与真实退出能力；不将它们重复包装成新缺口。待验证的窄假设是：在具体改进对象被采用之前，Northstar 的选择动作能以重要场景、现有方向和实际能力判断结果价值及演化贡献，而不先选容易落地的缺陷再补理由。

目标状态是得到一项有根据、可修订的采用判断，并能沿现有 composition 形成目标状态、机制、相依变化、Acceptance 和剩余范围完整相接的方案。允许局部修复、风险必要项、复用现状和 no-op；不以更多规则或更长输出作为改善。

## Current → Delta

- 基线：feng-y/skill main b3612ee82261ff65132d21ce8503b13e223c66fb，2026-10-02 13:25 UTC 经连接器核对
- 独立分支：northstar-evolution-value-selection-20261002-1325
- 仅调整 Northstar 的 Intent convergence 第 2 项及其既有宽泛请求解释；价值判断前移到采用对象前，随后直接接回既有完整 Draft
- 不改 AE、Beacon、Unknowns First、Verify，不新增 Skill / Goal / schema / controller / scorer。Northstar 不实施；其他 skill caller-neutral
- 不恢复旧 no-op 分支，不覆盖 fix/northstar-strategic-target-20261002 或其他工作
- 不做 breaking semantic migration：既有 owner 与 artifact authority 不变，无需历史迁移条目

## Adoption reasoning

借鉴 CE 的真实候选与价值压力测试、DORA outcome-first、Thoughtworks 以业务能力和演化路线连接技术选择。仅吸收决策区别，不复制候选定额、流程或模板。

来源：[CE 机会筛选](https://github.com/EveryInc/compound-engineering-plugin/blob/9af474a70e7f2a844338519ad9e92aafbd92d4fb/skills/ce-ideate/references/post-ideation-workflow.md)、[CE 价值压力测试](https://github.com/EveryInc/compound-engineering-plugin/blob/9af474a70e7f2a844338519ad9e92aafbd92d4fb/skills/ce-brainstorm/references/product-pressure-test.md)、[DORA outcome-first](https://dora.dev/guides/value-stream-management/)、[整合技术战略](https://martinfowler.com/articles/creating-integrated-tech-strategy.html)、[渐进替代](https://martinfowler.com/articles/patterns-legacy-displacement/)。这些是方法依据，不是本候选的行为证据。

实际贡献假设：把容易被工具、目录或眼前失败主导的选择，变成重要结果驱动的取舍；复用现有语义比新 Strategy skill 成本低，也不要求所有工作先制定战略。反向成本是更多前置比较和泛化论述，须由行为输出直接检验。

## Acceptance

1. Runtime diff 只改变上述选择段，原有 owner、授权、完整方案与持续上下文边界保持
2. 冻结相同原始请求“完善 skill 体系”及既有目标背景，使用 current baseline 与 candidate 的真实 fresh actors，对实际选题、因果贡献、完整方案、可推进性及无用前置做独立比较；不将字数、字段或自报动作作为结果
3. 所有结果包括 no-op/不利结果保留；最多两组成对 broad runs，另做明确局部修复和反证返回的 candidate-only 轻量守卫。若输出无实际增益，明确建议不推广
4. 运行 repo 相关静态 / instrument 回归与 skill validator，区分其通过与行为改善证据
5. 给出 commit / 分支、实际 delta、方案符合性、证据局限与保留/撤回建议；不得自动 PR / merge / deploy

## Work / status

- Source / scope：已核对；runtime candidate 在 commit cd06d63b8c1a382a061cb52ad9ca496e126edb7a，未按输出修订
- Runtime candidate：仅 Northstar convergence；净增 511 字符 / 1,415 UTF-8 bytes
- Behavioral comparison：两组固定成对真实 actor 全部完成。四次都选择先检验宽泛改进选题能力，再决定是否修既有 owner；两 baseline 也有成本替代、连贯诊断交接、后续条件分支与保留范围
- Independent judgment：两对均无可采用的实际优势。候选语言更明确不计为增益，四者仍未确立值得采用的具体能力改动，不能据无差异宣布 main 已完成原始诉求
- Guards：局部 parser planning/handoff 通过所测边界；真实 RDR 反证返回已完成，实质改变采用 / 依赖 / Acceptance并保留完整原始目标。两者均 candidate-only，不是成对 uplift
- Checks：6 个 skill validator、51 个既有 instrument 回归与 diff --check 通过；独立审查重跑 51 项亦通过。均不冒充行为改善
- Branch publication：首版实现已在独立分支远端核验；最终结果和可重现证据已完成，随同一分支交付；main 未改

## Current acceptance judgment

方案在源码层符合既有选择责任与边界，但本轮成对观察没有证明它比 current main 选得更好、形成更有用的路线或减少有害前置。四个产物都把具体能力改动推迟到后续“先发现缺口再修 owner”，未证明这笔诊断投入优于其他现实机会；它们形成了可推进的有界诊断交接，但未达成用户期望的实际有价值能力目标方案。保留主线的决定依赖实际收益，不依赖实现是否写完。

目前建议不推广 runtime 增量；保留未合入分支供对照检查，不为获得正结果增加新题、平台或提醒。后续没有独立的 matched no-op 测量，也没有实际产品战略/演化执行验证；不从文本推断这些能力已可靠。

## Evidence / next owner

详细事实、局限与原始产物入口见 [成对结果](../evals/northstar/RESULTS-evolution-value-selection-2026-10-02.md)。已冻结比较与守卫全部完成；本轮实现和评估交付已完成，不再追加测试。最终建议保留分支作为负面实验记录、撤回 runtime 进入主线的采用建议；本轮不再有待执行的实验或实现工作。本轮不 PR、合入或部署。
