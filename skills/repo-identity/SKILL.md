---
name: repo-identity
description: "Build evidence-grounded Repo Identity Intelligence for a target repository: map stable capabilities, responsibilities, authority, boundaries, contracts, key flows and evidence anchors; detect semantic evolution pressure; compile intent-conditioned repo projections; and surface high-leverage improvement opportunities without mistaking raw churn or the first local defect for the repo's identity."
---

# Repo Identity Intelligence

Repo Identity 直接作用于**目标 repository**。它的目标不是给 Skill system 增加一层抽象，而是让 Agent / Human 能回答：

- 这个 repo 长期在负责什么，哪些责任/authority/contract 构成它的稳定身份；
- 当前实现如何兑现这些责任，哪些只是可替换 implementation detail；
- 哪些变化压力正在反复作用于同一 identity surface；
- 一个当前 Intent 真正相关的 repo slice 是什么；
- 哪些 evidence-backed friction 表明 repo 值得改，以及改进应落在哪个责任面。

核心规则：

> **先建立“repo 为什么存在、谁拥有决定、边界靠什么 contract 成立”的 identity，再用变化证据寻找改进；不要把目录结构、文件 churn 或第一个容易证明的局部问题当成 repo identity。**

Repo Identity 不拥有 Human 产品 Intent、Target Architecture、implementation plan 或 proof sufficiency。Northstar 仍拥有 accepted Intent；Architecture Evolution 仍拥有长期 Target judgment；Unknowns First 关闭事实未知；Verify 判断 claim 是否 proven。

## 什么时候使用

直接使用 `$repo-identity`：

- Human 要“理解这个 repo / subsystem 到底是谁、为什么这样组织”；
- Human 要“找 DaVinci / Hermes / 任意 repo 的高价值改进点”，但不想从第一个局部问题开始拍方案；
- broad change / improvement Intent 需要知道应该落到哪些 responsibility / contract / flow；
- 历史上已经有 repo identity / architecture map，需要判断哪里 drift；
- 想把复杂 repo understanding 编译成更适合 Human 审查的 diagram / dashboard / interactive artifact。

一个已知文件里的局部 bug、一个已知 owner 内的普通实现 How，不需要 Repo Identity。不要为了“有地图”全量扫描 repo。

## Identity model

Repo Identity 只保留跨具体 patch 仍有判断价值的 stable semantics，并让每个 claim 回到 Evidence。

### 1. Repo thesis

先用当前 authoritative source 回答：

- 这个 repo / subsystem 对上游提供什么长期 capability；
- 它拥有哪类决定、state、knowledge 或 lifecycle；
- 明确不拥有什么，哪些目标/策略/authority 留在上游或相邻系统。

Repo 名称、README slogan 或当前目录布局不能单独定义 thesis。

### 2. Capability / responsibility / authority

围绕真实 change reason 建 identity：

- 哪个 capability 长期存在；
- 哪个 owner 应持有完成它所需的 knowledge / decision / state；
- caller 依赖的是 stable contract 还是 private representation；
- 同一个 authoritative rule 是否在多个地方重复定义。

目录/类只是 evidence anchor。只有当它们稳定承载 responsibility 时才进入 identity。

### 3. Boundary / contract

只记录会影响跨边界理解和改进判断的 contract，例如：

- input/output semantics；
- absence/default/error behavior；
- compatibility；
- lifecycle / ownership / release boundary；
- schema / protocol / generation boundary；
- authority precedence；
- runtime/data/control boundary。

Contract 必须指向 current code/test/config/spec 或 authoritative doc；历史讨论只能作为解释，不能替代 current authority。

### 4. Key flows

只画能解释 responsibility 与 contract 如何兑现的 material flow。常见是 request/data/model/control/result flow。

不要把 call graph、文件树或所有依赖复制进 identity。一个 edge 只有在改变 ownership、boundary、failure、compatibility 或当前 Intent 判断时才值得保留。

### 5. Evidence anchors

每个 durable identity claim 至少有一个可复查 anchor：

- current code symbol / owner path；
- test / fixture / verifier；
- config / schema / generated contract；
- project AGENTS / design contract；
- authoritative current docs；
- 必要时用 commit/PR history 解释 identity 为什么演化到当前状态。

优先稳定 symbol/path/contract，不把易漂移的 line number 当长期 identity。

## Evolution Intelligence

Repo Identity 不把“经常改的文件”直接称为 hotspot。目标是找 **semantic evolution pressure**。

重点看：

- 同一 change reason 是否反复跨多个 owner 修改；
- caller 是否重复重建某个 owner 的 private knowledge；
- 一条 contract 是否在多个 surface 被同步维护；
- 新需求是否持续绕过现有 boundary；
- 同一 semantic change 是否需要沿长 dependency path 传播；
- history 中的多次局部 patch 是否都在补偿同一个 responsibility mismatch；
- stable identity claim 的 source anchor 是否持续被改写或被另一 authority 取代。

### Semantic hotspot != raw churn

高 churn generated file、vendor code、机械 rename、格式化不是 semantic hotspot。

一个真正值得关注的 hotspot 应该能表达为：

> **repeated change pressure → touched identity surfaces → recurring friction / authority drift → Evidence**

只有这个链条成立，才进入 improvement map。

## Intent-conditioned projection

当 Human / caller 带着一个 Intent 来时，不把完整 Repo Identity 塞进 context。编译最小相关 slice：

1. 从 Intent 提取会改变结果的 material dimensions：capability、responsibility、contract、flow、compatibility、lifecycle 或 performance pressure；
2. 找到对应 identity owners / boundaries / Evidence anchors；
3. 展开一跳或必要多跳的 contract / dependency，只到足以判断 impact；
4. 标出 related evolution pressure、recent identity drift 与 deciding unknown；
5. 新信息已不能改变 target/scope/owner/acceptance 时停止。

输出应让 fresh consumer 看见：

`Intent → relevant identity → affected boundaries/contracts → evidence → unknowns / pressure`

而不是一份全 repo inventory。

## Improvement discovery

Repo Identity 可以直接发现和说明 **improvement opportunities**，但不把它们冒充 Human 已接受的 Intent 或长期 Target Architecture。

高价值候选优先来自：

- **decision duplication**：多个 caller 重建同一 private decision；
- **authority split**：同一 rule 在 code/config/docs/generated artifacts 中存在多个可独立漂移的 authority；
- **contract leakage**：consumer 依赖 owner 的 private representation / incidental layout；
- **cross-boundary change spread**：一个 semantic change 反复穿越多个本不该共同修改的责任面；
- **compensation path**：adapter/facade/special case 只是在补偿错误 ownership；
- **identity drift**：当前 implementation / docs / tests 已经无法同时支持历史 identity claim；
- **proof spread**：一个责任的正确性必须绕过 owner contract 才能建立 Evidence。

每个候选至少表达：

1. **Pressure**：什么变化反复发生；
2. **Identity mismatch**：哪条 responsibility / authority / contract 因此暴露问题；
3. **Evidence**：哪些 current source / history / tests 支持；
4. **Improvement direction**：应消除什么 duplicated knowledge / authority / propagation / ambiguity；
5. **Expected leverage**：如果修正，哪些 future changes / judgments / proofs 会更 locality；
6. **Owner routing**：若已变成长期 structural Target fork → Architecture Evolution；若只是 bounded concrete shape → Beacon / Executor；若事实仍不清 → Unknowns First。

不要按“架构感”“文件数”或通用 best practice 排序。优先 repeated pressure + high decision/proof spread + clear evidence 的候选。

## Human representation

Repo Identity 的内部理解不要求 Human 读长文本。根据当前判断任务选择 representation；详见 [references/human-projection.md](references/human-projection.md)。

默认原则：

- 单个责任/contract → concise text / table；
- 多 owner / boundary 关系 → diagram；
- migration / adoption / evidence 状态 → dashboard；
- evolution / hotspot → timeline + change map；
- 多维 repo exploration → disposable interactive artifact；
- 只有需要连续解释复杂因果时才考虑 explainer。

Representation 是 intelligence 的输出，不是 authority。生成的 HTML、diagram、dashboard、video 可以一次性使用并丢弃。

## Durable identity 与防腐化

一次性分析默认不制造新长期文档。Human 明确要求“构建/维护 Repo Identity”，或同一 repo 会反复消费 identity 时，读取 [references/durable-identity.md](references/durable-identity.md)。

Durable identity 是 **derived index**，不是第二份 architecture truth。它必须：

- 指向 authoritative evidence；
- 标明校验基线（branch/ref/commit 或可定位 source identity）；
- 区分 stable identity 与 current implementation note；
- source anchor 变化时只重验 affected identity cone；
- contradicted claim 明确替换/退役，不保留两个 current truth。

## 与其他 Skill 的边界

- **Northstar**：Repo Identity 提供 repo understanding / improvement evidence；Northstar 决定什么成为 accepted Intent / Draft。
- **Architecture Evolution**：Repo Identity 描述 current identity、pressure 与 drift；AE 判断长期 Target owner / boundary / dependency。
- **Unknowns First**：Repo Identity 遇到一个决定性事实不清时交给 Unknowns First 关闭；不要用 identity narrative 猜事实。
- **Beacon**：一个 improvement direction 需要可检查的 bounded concrete shape 时可以调用 Beacon；Beacon 不拥有整个 Repo Identity。
- **Verify**：Repo Identity 的 source anchors 支撑理解；具体 completion/safety claim 是否被证明仍由 Verify 判断。
- **Eval**：如果声称 Repo Identity Skill 本身改善了 agent 行为，进入 Eval；一个漂亮 repo map 不证明 behavioral uplift。

## Return

一次调用只交付当前任务需要的最小充分结果：

- **Identity**：repo thesis + relevant capability/responsibility/authority；
- **Boundary / contracts / key flow**：只列当前判断相关部分；
- **Evolution pressure**：semantic hotspot / drift 及 Evidence；
- **Intent projection**：若有当前 Intent；
- **Improvement map**：有 Evidence 的候选、预期 leverage 与 owner routing；
- **Human representation**：当复杂度值得时生成/建议最合适的 view；
- **Unknown / stale claims**：明确哪些还不能作为 current identity。

不要以“扫描完成”“图画完整”作为完成标准。完成标准是：Human / caller 可以基于这份 identity 更快地理解 repo、定位变化、形成或审查改进判断，而不需要重新从文件树拼装语义。
