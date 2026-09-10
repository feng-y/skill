---
name: architecture-evolution
description: 用于根据长期 Target Architecture 与当前仓库现实，判断是否值得结构演进并收敛高杠杆 Evolution Program；Target 缺失或前提失效时 model-invoke architecture-shape。
---

# Architecture Evolution · 从 Target 收敛结构演进

Architecture Evolution 负责 **从长期 Target 到当前值得推进的结构演进 Program**。Target Architecture 的责任、边界、variation/layering 与 dependency direction 由 `$architecture-shape` 拥有；AE 消费已经成立的 Target，与 current reality 比较后判断是否需要演进、当前最有价值的 structural gap 是什么，以及哪些旧 authority / knowledge / path 必须真实退出。

Human 拥有业务、投入、兼容、长期维护和风险承诺；Northstar 负责 binding Intent 与 Taskbook；Architecture Shape 负责长期 Target judgment；Executor 决定具体实现 How。AE 不生成 patch plan、file/class/API 设计或执行调度。

输入可以是现有表达、issue、specification、Goal、指定范围或已有 Target，不要求独立 Goal 文件或 Northstar 前置调用。点名 module 是调查入口，不自动成为 Target boundary。

## 先确认 Target 是否可用

优先复用 repo 中仍有效的 authoritative architecture source 或当前上下文里已有、Evidence 足够且前提未失效的 Target。**Current code 不能因为“已经存在”而自动定义 Target。**

只有以下情况才 model-invoke `$architecture-shape`：

- 没有足以指导当前结构判断的长期 Target；
- 新 Goal / roadmap / authority / verified reality 产生会 materially 改变 capability owner、boundary、variation、dependency、lifecycle 或 failure/isolation semantics 的 fork；
- 现有 Target 的 deciding premise 已失效或与新的 authority / reality 冲突。

调用时只传当前 Goal pressure、binding constraint、verified reality 与仍有效的 architecture Evidence；消费它返回的 Target / deciding Evidence / alternative / reopen condition，不让它设计当前 Program。

如果剩余问题只是当前迁移成本、先后顺序、实现难度或 patch shape，Target 没有失效，不重跑 Architecture Shape。

## 建立 Current → Target gap

Target 成立后，只调查会改变 **是否演进、Program scope、material dependency、real exit 或 safe structural start** 的 current reality。已有 Evidence 默认复用，不为了“完整理解”重扫 repo。

把 gap 表达在长期责任真正要求改变的地方，例如：

- authority / knowledge 仍在错误 owner 或被多个 caller 重建；
- Target boundary 尚未建立，consumer 仍穿透旧 implementation；
- 已证明的 variation 仍泄漏到 caller，或反之存在没有长期 variation 的多余 layer；
- dependency 仍指向错误 knowledge owner；
- Target 要求退出的 legacy authority / special path 仍然 authoritative；
- Target 的 lifecycle / failure / isolation boundary 尚未兑现。

行为持平、test green 或新 facade 存在，只能证明对应行为/结构事实；不能替代 responsibility、authority、dependency 或 real-exit gap 的判断。

如果 current reality 已经满足 Target，或 Goal 是一次性局部变化且正确 owner / boundary / dependency 无需改变，返回 **local / no-evolution**，不要制造 Program。

## 收敛 Evolution Program

Program 回答：**在当前现实约束下，哪几项结构变化最值得现在推进，才能真实逼近已经成立的 Target？** 它不是完整 backlog，也不是 Target 的另一份描述。

先把 Current → Target gap 作为候选，再以不超过 3 个高价值锚点比较 leverage，不凑数量：

- 是否把长期 responsibility / authority / private knowledge 归回正确 owner；
- 是否建立 Target 要求的 boundary / dependency，并减少后续同类变化跨无关 responsibility 的传播；
- 是否让旧 authority、duplicated knowledge、reverse dependency、special path 或被结构替代的 guidance **真实退出**；
- 是否解除会阻塞后续 Target 演进的结构前提。

同一 responsibility / authority correction 如果拆开仍留下同一个旧 owner 或补偿性路径，应聚合成一条 cohesive evolution 主线；真实独立的 responsibility 和收益保持独立。

**Structural gain 必须伴随 real exit。** 只新增 facade / registry / interface / provider，而旧 authority、旧特殊路径或 caller knowledge reconstruction 仍然存在，不算 architecture evolution；仅为未来可能性搭脚手架也不算。

迁移成本、实现难度、兼容窗口与当前团队投入可以改变 Program 的优先级、范围和 migration boundary，但不能反过来把更便宜的 current subset 改写成长期 Target。

## Program 的 altitude

Program 表达 material structural outcome，不表达 implementation How。可以包含：

- 哪个 responsibility / authority / knowledge ownership 要归位；
- 哪个 boundary / stable dependency 要建立或改向；
- 哪个 internal variation 要收进 owner，或哪个无依据 layer 要退出；
- 哪些旧 authority / paths / duplicated decisions 必须消失；
- structural cuts 之间真实存在的 prerequisite / dependency；
- 哪些 architecture Evidence 可以证明结构结果成立。

除非 Human / authority 已绑定 representation，类、API、文件、schema、MR、helper、patch 顺序和具体测试命令都留给 Executor / repo reality。Program 不是实现 checklist。

## Evidence、Unknown 与停止

current code / config / test / runtime 证明现实；有效 architecture source / domain authority 约束 Target；Goal / roadmap / Human commitment 决定当前是否值得投入。外部 pattern 只用于挑战，不替代 repo Evidence。

未关闭事实如果会改变 Program 是否成立、scope、dependency 或 real exit，应做最小 probe 或保留显式 Unknown；只影响可替换 implementation How 的未知不扩大调查。Human-owned 的投入、兼容、风险或长期维护选择无法由 Evidence 关闭时，返回 decision surface，不替 Human 决定。

事实足以判断当前 Program 就停止。不要为了预演完整迁移、预选 verifier、枚举所有 caller 或让 Program 看起来完整而扩大 Research。

按当前问题读取以下 reference，不作固定序列：

- [delivery-examples.md](references/delivery-examples.md)：Program / delivery 容易漂移成平台、facade 或 patch plan 时参考。
- [legacy-lenses.md](references/legacy-lenses.md)：兼容身份或旧模式能否真实退出会改变 Program 时参考。
- [brooks-constraints.md](references/brooks-constraints.md)：候选 Program 只是 complexity relocation、第二系统或额外协调时参考。

长期 Target 的战略设计不再由 AE reference 拥有；需要重判时调用 `$architecture-shape`。

## 交付与回流

局部问题交 local / no-evolution 判断；有演进价值时交付：当前相关 Goal / pressure、采用的 Target 与 authority、Current → Target 的 material gap、当前 Program、real exits、migration boundary，以及结构 claim 所需的 Evidence obligation。

**Behavior parity 只证明没有改坏，不证明结构改善。** Program 完成也必须分别证明 responsibility / authority / boundary / dependency / real-exit 等 material structural claims。

收敛的 Program 以同一正文写入 repo/workspace 外 Markdown handoff，显示真实 path；写入失败即 blocker。已有 authoritative architecture source 只由稳定 Target conclusion 更新，Program handoff 不替代长期 architecture SOT。

current reality、成本或迁移条件变化，只重算受影响 Program；Target 的 deciding premise 失效才重新 model-invoke `$architecture-shape`；accepted outcome 或 Human commitment 变化则回 Northstar。保留无关 Evidence 与仍有效的 Target / Program 判断，不因实现波动全量重做。