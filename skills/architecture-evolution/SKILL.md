---
name: architecture-evolution
description: 用于根据长期 Target Architecture 与当前仓库现实判断是否值得结构演进，并收敛高杠杆 Evolution Program；Target 缺失或前提失效时 model-invoke architecture-shape。
---

# Architecture Evolution · 从 Target 收敛结构演进

Architecture Evolution 只负责 **Current reality → Target Architecture 的结构演进 Program**。长期 capability / responsibility / boundary / variation / dependency 的 Target judgment 由 `$architecture-shape` 拥有；AE 不重新设计 Target，也不进入 file/class/API/patch 等 implementation How。

Human 拥有业务、投入、兼容、长期维护和风险承诺；Northstar 拥有 binding Intent 与 Taskbook；Architecture Shape 拥有 Target；Executor 拥有具体实现。

## Target gate

优先复用仍有效的 authoritative Target。Current code 只证明 reality，不能因为已经存在就定义 Target。

仅在以下情况 model-invoke `$architecture-shape`：Target 缺失；新的 Goal / authority / verified reality 产生会 materially 改变长期 owner / boundary / variation / dependency / lifecycle / failure semantics 的 fork；或已有 Target 的 deciding premise 已失效。只把 Goal pressure、binding constraints、verified reality 与仍有效 Evidence 交给它，并消费返回的 Target / deciding Evidence / reopen condition。

如果变化只涉及当前迁移成本、顺序、实现难度或 patch shape，Target 不重算。

## Current → Target gap

Target 成立后，只调查会改变是否演进、Program scope、material dependency 或 real exit 的 current reality。Gap 只保留 Target 尚未兑现的 material structural outcome，例如：

- responsibility / authority / private knowledge 仍在错误 owner，或 caller 仍重建它；
- Target boundary / stable dependency 尚未成立，consumer 仍穿透旧 owner；
- justified variation 仍泄漏给 caller，或没有长期 variation 的旧 layer 仍制造复杂度；
- Target 要求退出的 legacy authority / special path 仍 authoritative；
- lifecycle / failure / isolation boundary 尚未兑现。

Current 已满足 Target，或 Goal 完全落在当前正确 owner 内且长期结构不变时，返回 local / no-evolution，不制造 Program。

## Evolution Program

从真实 gap 中选择当前最有 leverage 的 structural moves，通常不超过 3 个锚点，不凑数量。优先能：归位 responsibility / authority / knowledge；建立 Target boundary / dependency；解除后续演进 blocker；以及让旧 authority、duplicated knowledge、reverse dependency、special path 或被结构替代的 guidance **真实退出** 的变化。

同一 responsibility correction 拆开后若仍留下同一个旧 owner / compensation path，应聚合成 cohesive 主线；真正独立的 responsibility 与收益保持独立。**只新增 facade / registry / interface / provider，而旧 authority/path 仍然 authoritative，不算 structural gain。**

迁移成本、兼容窗口和当前投入只影响 Program 的优先级 / migration boundary，不能反向改写长期 Target。

Program 写 material structural outcome 与真实 dependency，不写 class、API、文件、schema、helper、MR、patch 顺序或具体测试命令，除非 authority 已绑定 representation。

## Evidence 与停止

code/config/test/runtime 证明 current reality；有效 architecture/domain authority 约束 Target；Goal/roadmap/Human commitment 决定当前投入。未关闭事实若会改变 Program scope、dependency 或 real exit，做最小 probe 或保留显式 Unknown；只影响 implementation How 的未知不扩大调查。

事实足够判断当前 Program 就停止，不为预演完整 migration、枚举 caller 或补齐 backlog 扩大 Research。

按需读取：

- [delivery-examples.md](references/delivery-examples.md)：Program / delivery 漂移成平台化、facade 或 patch plan 时。
- [legacy-lenses.md](references/legacy-lenses.md)：兼容身份或旧模式能否真实退出会改变 Program 时。
- [brooks-constraints.md](references/brooks-constraints.md)：Program 疑似 complexity relocation / second system 时。

## 交付与回流

交付当前 Goal / pressure、采用的 Target 与 authority、material Current → Target gap、Evolution Program、real exits / migration boundary，以及 structural claims 所需 Evidence obligation。Behavior parity 只能证明兼容，不证明 responsibility / authority / boundary / dependency 已改善。

Program 以同一正文写入 repo/workspace 外 Markdown handoff，显示真实 path。长期稳定 Target 只更新已有 authoritative architecture source；Program handoff 不替代它。

current reality、成本或 migration 条件变化只重算受影响 Program；Target premise 失效才再次 model-invoke `$architecture-shape`；accepted outcome / Human commitment 改变则回 Northstar。