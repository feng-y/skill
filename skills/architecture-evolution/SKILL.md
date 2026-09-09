---
name: architecture-evolution
description: 用于长期责任、边界、变化隔离与依赖的架构判断；从当前意图和仓库现实推导 Target，并收敛值得推进的结构演进。
---

# Architecture Evolution · 战略设计与结构演进

AE 判断系统的长期结构如何吸收当前意图及已有 Evidence 支持的同类未来变化。**Target 是长期目标架构；Program 是当前值得推进的结构演进，不是重构清单或 implementation plan。** AE 在授权边界内作技术判断；Human 拥有业务、投入、兼容、长期维护和风险承诺，Northstar 负责意图整形，Executor 决定具体实现。

输入可以是现有表达、issue、specification、Goal 或指定范围，不要求独立 Goal 文件或 Northstar 前置调用。点名 module 是调查入口，不自动成为 Target boundary。多个目标只有共享结构压力，或责任 / 边界 / 依赖须协同设计时才一起处理。

## 战略判断：结构由什么决定

从当前有效意图、repo identity / architecture intent、领域语义和 verified reality 恢复 **change pressure**：哪些能力需要新增、替换或独立变化，哪些私有知识被多个 owner 反复重建，哪些长期约束真实改变结构。当前目录、设计模式、已有 patch 和局部整洁不定义 Target；性能、隔离、部署、兼容等约束只有长期 binding 且影响责任 / 生命周期 / failure boundary 时才塑造架构。

- **责任与知识。** 正确 owner 应拥有并隐藏同一变化原因所需的 knowledge、state、behavior、authority、lifecycle 和主要验证；局部高内聚不能掩盖错误的能力边界，也不能吞并真实独立语义或权威。
- **变化与分层。** 抽象 stable semantics，而非表面相似；只隔离确需独立变化的实现、provider 或生命周期差异。没有 stable variation 不造层次，具有独立 contract / authority / lifecycle 的差异也不能降成内部实现。
- **关系与依赖。** 责任成立后，依赖应指向 owner 的稳定 contract，并能由 semantic / authority / lifecycle / failure relationship 解释，保持少量稳定的单向关系。仅因 helper 位置、复用或调用便利存在的依赖，是重判 ownership 的 Evidence；合法关系不能为减少 edge 被删除、复制权威或藏进 facade。会改变 Target 的语义翻译、生命周期协同 / 隔离和失败传播须明确，不强制枚举关系 taxonomy。

**用代表性变化检验 AI-native 改善。** 正确 owner 是否能更局部地理解、修改和验证主要变化，caller 是否不再重建它的私有决定？表面模块更小、依赖更少或 test green 都不能代替这些结构证据。

Target 应包含已证明会长期改变判断的能力、关系和约束，不省略必要结构，也不预编猜测的 future provider / layer。approved roadmap 与长期承诺可以改变 Target；当前迁移难度、成本或已有实现只决定 Program，不能把方便实现的子集改写成长期目标。

## 调查与未决选择

只为会改变 Target / Program 的 unresolved fork 扩展调查；已有 Evidence 默认复用。一个廉价、可丢弃的 structural probe 能区分候选时才做，结果不自动成为 production、Program 或架构 SOT。事实足够就停止；材料不足时保留具体 Unknown，不用方案完整度或 confidence 代替 Evidence。

Human choice 未定不妨碍回答可独立判断的条件性结构问题：标明假设、后果和依据，不把候选当成已批准 Target。剩下的是业务、投入、维护或风险承诺时，给出真实选项、后果和 best-known recommendation，返回对应 decision surface，不冻结无关判断。被 Northstar 调用时仅返回其需要的结构结论与 Evidence，不接管意图提问或生成第二份 Taskbook。

当前事实由 code/config/test/runtime 核实；长期承诺由 Human、repo 或 upstream authority 约束。旧架构来源是可挑战的依据，不是 oracle；与现实冲突时辨别实现漂移与前提失效，不能擅自覆盖目标或制造虚假事实。

按当前问题读取，不作必读序列：

- [strategic-design.md](references/strategic-design.md)：bounded Evidence 后仍有会改变 Target 的结构分歧、authority conflict 或 boundary discriminator。
- [delivery-examples.md](references/delivery-examples.md)：设计已成立但交付形状易漂移，或候选疑似只加平台 / facade；示例不定义第二份 contract。
- [legacy-lenses.md](references/legacy-lenses.md)：兼容身份或旧模式能否退出会改变 Target / Program。
- [brooks-constraints.md](references/brooks-constraints.md)：候选说得通但整体复杂度、第二系统或 complexity relocation 仍可疑。

## Program：结构收益与真实退出

Target / reality gap 先作为候选，以不超过 3 个高价值锚点比较 leverage，不凑数量或生成 backlog。同一 responsibility / authority correction 若拆开仍留下相同旧知识、特殊路径或补偿性 guidance，应聚合成一条聚焦演进主线；真实独立的责任与收益保持独立。

Program 表达责任 / knowledge / authority 的归位、boundary 的建立或退出、variation 的归属与 dependency 改向，并要求对应旧 authority、私有知识重建、反向依赖、特殊路径及被结构替代的 guidance 退出。**只新增 facade / registry / interface 而旧结构仍 authoritative，或仅为未来搭脚手架，不算 structural gain + real exit。** Program 可包含有真实依赖的 structural cuts；除非 authority 已绑定 representation，类、API、文件、schema、MR、patch 顺序和测试工具都留给 Executor。

没有长期结构压力时给 local / no-evolution 判断；有可信 Target 但没有值得立即推进的变化时，可以只交战略设计，不强制 Program。

## 交付与修正

局部问题交局部判断；条件咨询交结论、假设和依据；收敛的设计交与意图有关的 change pressure、current constraints、Target，以及当前成立的 Program / migration boundary / real exit 和 architecture / behavior Evidence obligations。**Behavior parity 只证明没有改坏，不证明结构改善**；决定理由成立也不等于实际结构已兑现。每个 material structural claim 应能被现实检查证实或推翻。

下游确需复用时，保留决定性 Evidence / binding constraint，以及必要的真实 alternative 与 reopen condition，不额外强制 ADR、ledger 或完整推理记录。引用原意图与架构 authority，不复制第二份 SOT。

收敛的设计 / Program 以同一正文写入 repo/workspace 外 Markdown handoff，显示真实 path；写入失败即 blocker。获授权的稳定结论更新原 authoritative architecture source，handoff 不替代它。不输出 ready/completed/executable/status 状态标记。

修正只重算受影响判断：实现违反仍有效结构约定时不重做战略；结构前提失效才重开对应 Target，accepted outcome 或 Human commitment 改变则回意图 owner。保留无关 Evidence 与结论，只有前提失效才重查；设计 / Program 改变后完整重交付。
