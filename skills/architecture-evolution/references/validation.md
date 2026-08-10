# Evaluate Architecture Intent

只用于显式 smoke/eval，正常运行不读。

## Static smoke

通过需要同时满足：

- North Star 原文不变；
- 主流程仍是 `Ground → Discover → Shape → Challenge`；
- `SKILL.md` 主要拥有 Flow，`rules.md` 主要拥有 architecture judgement；
- 四个 architecture directions 仍可用于内部 diagnosis，但不要求输出 taxonomy；
- Brooks 只用于 challenge judgement，不形成最终 section；
- ready intent 只输出 Problem / Background / Direction / Boundary，必要时简要列 basic shape；
- 最终输出跟随用户主要语言；
- 三个状态保持互斥：`No architecture intent / Intent unresolved / Architecture intent ready`；
- 不进入具体 Target Design。

## Scenario smoke

### P1 — ModelCurator / Hermes

已知：FS/runtime-selection 已退出；ModelCurator 已拥有 published generation，但 prediction、prerank、item-embedding、feature-streaming 仍各自解释 feature config、Hermes lifecycle 和固定执行协议；streaming 与 scoring family 存在真实输入/config 差异。

通过：

- problem 收敛到 publication ownership 已闭合、usage knowledge 仍散落在 consumers；
- background 解释多-runtime 历史前提失效而 consumer knowledge 未退出；
- direction 指向稳定 model-scoped feature capability；
- 可以简要点出 generation-owned / independent execution capability 这类基本形态；
- 保留 streaming/scoring 的真实差异，不强制统一；
- 不决定 class/API、projection/rehash/metadata owner、调用流或 migration；
- 最终主文为中文，不出现 Brooks/taxonomy/challenge 表。

### P2 — False unification / ownership overreach

两个 consumer mechanics 相似，但属于不同 bounded context；相邻 runtime subsystem 已有正确 authoritative owner。

通过：不能因代码相似就统一业务语义，也不能因 caller reassembly 就把相邻 subsystem 的 config/resource/lifecycle 全部迁入当前 owner。

### N1 — Local fix

问题只是 off-by-one、日志字段、dead getter 或机械迁移，没有重复 pressure、consumer knowledge 或跨边界 structural consequence。

通过：`Status: No architecture intent`；不发明 architecture direction。

### R1 — Material unknown

一个未关闭事实会改变 intent 或 boundary，例如无法确认两条路径是否属于同一业务语义。

通过：`Status: Intent unresolved`；指出 claim at risk 和最小 probe / Human decision，不同时返回 ready。

### O1 — Stop before Target Design

证据已经足够形成 direction，用户没有要求完整设计。

通过：输出到 architecture direction / basic shape 即停止；若开始决定 module/class/API、responsibility placement、调用流、migration 或 implementation，即失败。

## Regression failures

以下任一出现即失败：

- 修改 North Star；
- 用新规则系统替代 Flow + Judgement；
- ready intent 输出 Brooks、taxonomy、Challenge 或 reasoning trace；
- 中文输入输出英文主文；
- basic shape 被展开成具体 Target Design；
- local smell 被升级成 architecture intent；
- capability ownership 无 evidence 扩张到 orchestration 或 adjacent subsystem；
- 新 facade/helper 没有真实 replacement / exit 却被判定为 evolution。
