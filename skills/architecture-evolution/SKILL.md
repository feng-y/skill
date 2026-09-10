---
name: architecture-evolution
description: "Resolve long-term structural ownership and evolve current reality toward it: establish or reuse the Target Architecture, compare Current → Target, then converge a focused Evolution Program with real exits."
---

# Architecture Evolution · Target judgment + current structural evolution

Architecture Evolution 负责两层连续但不同的判断：

1. **Target Architecture judgment**：长期 capability / responsibility / authority / knowledge 应由谁拥有，boundary、variation、dependency、lifecycle / failure semantics 应是什么；
2. **Evolution Program**：基于 verified current reality，判断当前最值得推进哪些 structural moves 才能兑现 Target，并让旧 authority / duplicated knowledge / reverse dependency / special path 真实退出。

这两层语义必须分开，但不需要拆成两个顶层 Skill。Program convenience 不能反向定义 Target；Current code 只能证明 reality，不能因为已经存在就成为长期 Target。

Architecture Evolution 不拥有 canonical Intent，不替 Human 改变投入、兼容、长期维护或风险 commitment，不进入 file/class/API/patch 等 implementation How，也不负责 behavior verification / outcome judgment；这些分别属于 Northstar / Human、Executor 与 `$replay`。

## 输入：Intent pressure，不建立独立 Goal 层

从当前 Northstar Intent / Drafted Issue、Human correction、稳定 architecture/domain authority 与 verified reality 中提取**会长期改变结构的 change pressure**。只保留会影响 responsibility、authority、knowledge ownership、boundary、variation、dependency、lifecycle、failure/isolation 或兼容承诺的信息。

不要求也不维护独立 `Goal` artifact。若一个抽象 outcome 真正影响结构判断，它已经应当体现在 Intent 的 Problem、Draft、Constraint、Decision 或 Acceptance 中。

## Target gate

优先复用仍有效的 authoritative Target。只有 Target 缺失、已有 premise 失效，或新的 Intent / authority / verified reality 产生会 materially 改变长期 owner / boundary / dependency / lifecycle 的 fork 时，才重新做 Target judgment。

若变化只涉及当前迁移成本、顺序、patch shape 或 implementation difficulty，Target 不重算。

### Responsibility / knowledge ownership first

先判断哪个长期 capability 应拥有并隐藏完成同一变化原因所需的 knowledge、state、behavior、authority、lifecycle 与主要 structural verification semantics。正确 owner 应让 caller 不再重组这些私有决定。

当前 module、目录或用户点名范围只是 investigation scope，不自动成为 Target boundary。高内聚低耦合是正确 knowledge ownership 的结果，不是独立评分。

### Variation / layering second

只有 stable semantics 与可独立变化的 implementation/provider/storage-runtime adapter/lifecycle/deployment/performance architecture 等之间存在长期差异时，才引入 layer / provider。没有 stable variation 不造层次；不要套固定 `interface → domain → provider → infrastructure` 模板。

### Dependency after ownership

能力与 responsibility 先成立，再设计 dependency direction。长期 dependency 必须由真实 semantic / authority / lifecycle / failure relationship 解释，并尽量依赖 owner 的 stable contract，而不是历史 helper 位置。

单向依赖不能挽救错误的 capability decomposition；合法 authoritative dependency 也不能为了减少 edge 数被复制或吞并。

### 用 change locality 挑战 Target

对至少一个代表性当前 change pressure 检查：

- fresh implementer 是否主要在正确 owner 附近恢复关键设计决定；
- 修改是否主要由应吸收它的 responsibility 承担；
- structural / behavior Evidence 是否能从责任边界附近建立，而不是绕过 contract 穿透 implementation。

新增 facade / registry / interface 后，如果 judgment/change/verification propagation 基本不变，只是 complexity relocation，不是 architecture gain。

## Current → Target gap

Target 成立后，只调查会改变是否演进、Program scope、material dependency 或 real exit 的 current reality。Gap 只保留 Target 尚未兑现的 material structural outcome，例如：

- responsibility / authority / private knowledge 仍在错误 owner，或 caller 仍重建它；
- Target boundary / stable dependency 尚未成立，consumer 仍穿透旧 owner；
- justified variation 仍泄漏给 caller；
- Target 要求退出的 legacy authority / special path 仍 authoritative；
- lifecycle / failure / isolation boundary 尚未兑现。

Current 已满足 Target，或 change pressure 完全落在当前正确 owner 内且长期结构不变时，返回 local / no-evolution，不制造 Program。

## Evolution Program

从真实 gap 中选择当前最有 leverage 的 structural moves，通常不超过 3 个锚点，不凑数量。优先能：

- 归位 responsibility / authority / knowledge；
- 建立 Target boundary / stable dependency；
- 解除后续演进 blocker；
- 让旧 authority、duplicated knowledge、reverse dependency、special path 或被结构替代的 guidance **真实退出**。

同一 responsibility correction 拆开后若仍留下同一个旧 owner / compensation path，应聚合成 cohesive 主线；真正独立的 responsibility 与收益保持独立。只新增 facade / registry / interface / provider，而旧 authority/path 仍 authoritative，不算 structural gain。

Program 写 material structural outcome、dependency、migration boundary 与 real exit，不写 file、class、API、schema、helper、PR split、patch 顺序或具体测试命令，除非 authority 已绑定 representation。

## Evidence 与 Replay

code/config/runtime/test 证明 current reality；有效 architecture/domain authority 约束 Target；Northstar Intent / Human commitment 约束 accepted boundary。

`$replay` 负责 behavior / compatibility / completion claims 的验证与 outcome judgment。Replay green 只能证明对应 behavior claim，不自动证明 responsibility / authority / dependency 已改善；architecture gain 还需要 structural Evidence。Replay 若暴露此前未知的 architecture fork，将该 finding 路由回 AE，只重开受影响 Target / Program。

未关闭事实若会改变 Target、Program scope、dependency 或 real exit，先用最小 Evidence 关闭，必要时调用 `$unknowns-first`；只影响 implementation How 的未知不扩大调查。

## 返回与持久化

返回当前调用方所需的最小充分结果：

- adopted / re-established Target Architecture 与 deciding Evidence；
- material Current → Target gap；
- focused Evolution Program、real exits / migration boundary；
- 会改变 Target / Program 的 unresolved Evidence 或 Human choice。

被 Northstar 调用时，只把后续执行需要的 durable structural Decision / Constraint / Draft correction fold back 到 canonical Intent / Issue。独立调用且用户需要 architecture handoff 时才形成持久文档；AE 不强制每次生成第二份 Markdown SOT。

current reality、成本或 migration 条件变化只重算受影响 Program；Target premise 失效才重做 Target judgment；accepted Intent / Human commitment 改变则回 Northstar / Human。

## 按需 references

- [delivery-examples.md](references/delivery-examples.md)：Program 漂移成平台化、facade 或 patch plan 时；
- [legacy-lenses.md](references/legacy-lenses.md)：旧身份 / compatibility 是否能 real exit 会改变 Program 时；
- [brooks-constraints.md](references/brooks-constraints.md)：候选 Program 疑似 complexity relocation / second system 时。
