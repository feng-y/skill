---
name: architecture-evolution
description: 当工程意图、相关目标或指定范围需要长期责任、边界、依赖与架构取舍判断时使用。依据 repo identity 与现实推导 AI-native Target Architecture，收敛有 structural gain 和 real exit 的演进 Program；不接管需求 shaping 或实现。
---

# Architecture Evolution · 从 Intent 压力推导目标架构

AE 的核心是**战略设计**：判断系统结构应怎样演进，才能在正确责任边界内吸收当前意图及 Evidence 支持的同类未来变化。Target 回答长期结构应该是什么；Program 回答当前最值得推进哪项结构变化，不是重构清单或 implementation plan。

**Northstar** 负责 Intent take / shaping 与执行约定；**AE** 负责技术上的 responsibility、boundary、dependency、variation 和结构取舍判断；**Human** 拥有业务优先级、投入、兼容与风险承诺；**Executor** 决定具体实现并执行。技术判断不因涉及 architecture 就一律退回 Human，Human commitment 也不因模型能给方案就被静默关闭。

## 从当前意图进入，不要求独立 Goal 产物

输入可以是 Human 表达、issue、已整形的 intent / specification、一个或多个 Goal、或需要演进的 module。需要的是足以判断当前结构问题的预期结果、约束与 scope，而非名为 Goal 的标题、文件或 Northstar 前置调用。点名 module 是调查入口，不默认它就是 Target boundary；也不为了容易实现而把当前形态反推成目标。

输入尚有 Human-owned choice 时，只要一个带明确假设的结构问题可以独立回答，就给其可核实后果与建议，帮助上游 shaping；不能把条件候选当已批准 Target。若不同意图解释会改变业务结果、长期承诺或 owner，且无足够依据，就返回具体 decision surface，而不是自行改写需求或产出完整蓝图。

相关 Goal 只有共享 material architecture pressure，或涉及的能力与边界必须协同设计时才共同形成 Strategic Design；独立目标不为“统一架构”强行合并。普通实现、局部修复或纯整洁没有长期结构压力时，直接给 no-evolution / local judgment，不强制完整 Program。

## 判断 Target

从 intent 所要求的能力变化、repo identity / architecture intent、领域责任与 verified reality 恢复 **change pressure**：什么需要新增、替换、独立演进或吸收 variation；同类变化为何要求多个 owner 共同重建同一知识；哪些长期 binding 的性能、隔离、部署、兼容或 failure constraints 真正改变结构。长期承诺须有 Human / repo / upstream authority，当前事实须有 verified reality。旧 architecture source 是待核实的依据，不是 oracle；事实与 authority 冲突时区分实现漂移和前提失效，不擅自覆盖任一方。

Target 的核心关系是 `change pressure → responsibility → boundary → variation / dependency → local understanding / change / verification`。这是设计判断，不是逐项填写的固定流程：

- **责任与知识归属。** 长期能力应拥有并隐藏同一变化原因所需的 knowledge、state、behavior、authority、lifecycle 和主要 verification。不能直接从 Goal 跳到新 module，也不能用局部高内聚掩盖错误 capability decomposition。
- **真实 variation 与独立关系。** owner 内部存在稳定语义与可独立变化的 implementation / provider / lifecycle 等边界时才分层。具有独立语义、authority 或 lifecycle 的能力不能为“内聚”被吞并；真实跨边界语义翻译、生命周期协同 / 隔离或失败传播需要时应明确，不为完整感枚举 taxonomy。
- **可解释的单向依赖。** dependency 应依赖 owner 的稳定 contract，而非私有实现，并能由 semantic / authority / lifecycle / failure relationship 解释。仅由 helper 位置、复用或调用方便造成的依赖，是重判 ownership 的 Evidence；真实必要关系不为减少 edge 而删除或藏在 facade 后面。

Target 必须包括已证明会长期改变判断的结构事实，但不预编未经证明的 future capability、provider、layer 或协作关系。当前迁移难度、已有 patch 和短期成本可改变 Program 的范围，不能替代长期设计；已批准 roadmap 与 durable constraints 则可以改变 Target。

**用代表性变化挑战结构，而不是给架构形容词打分。** 一个有当前需求或已批准未来需求支持的变化，是否更容易从正确 owner 附近理解、修改和验证？caller 是否不再重建 owner 私有知识？旧 authority / 反向依赖是否真正退出？保留能证实或推翻 material boundary 的 Evidence obligation；行为不变与结构改善是不同的 claim，不能用 test green 互相替代。

Research 只由会改变 Target / Program 的明确 unresolved fork 驱动；probe 应能区分 material alternatives。两个候选都说得通而一个廉价、可丢弃的 structural slice 能区分时，做最小 probe，不把它自动升为 production 或 Program。Evidence 足够时停止扩搜；若剩下的是 Human 的投入、业务或风险取舍，给 best-known recommendation、真实选项和后果，交回对应 owner。没有新前提变化就复用 Evidence，不因新的 judgment pass 重扫 repo。

## 收敛当前 Program

Target 与 reality 的 gap 只是候选，不自动成为任务。用不超过 3 个高价值锚点比较当前 leverage，不凑满数量、不生成 backlog。同一 responsibility / authority correction 若拆开仍留下相同旧知识、特殊路径或补偿性 guidance，应合成一条聚焦演进主线；真正独立的责任与结构收益保持独立。

Program 描述 material structural moves：责任、knowledge 或 authority 如何归位，哪个 boundary 建立或退出，dependency 如何改向，variation 如何归属，以及哪些旧 authority / path / reverse dependency 必须消失。可包含有真实 dependency 的 structural cuts；除非 Human / repo / upstream authority 已固定表示，file、class、API、patch 顺序与 test provider 归 Executor。只加 facade、registry、interface 而旧结构继续 authoritative，或仅为未来铺脚手架，不算 structural gain。

没有值得立即修改的内容，可以只交 Strategic Design 判断。若当前 Program 成立，给 migration boundary 和 real exit；投入规模、长期维护等 Human commitment 未决时明确保留，不以“架构更好”自动授权实施。

## 交付与协作

交付深度随当前问题：局部问题交局部判断；阻塞交 decisive Evidence / choice 与继续条件；收敛的设计交与意图相关的 change pressure、current constraints、Target，以及当前值得推进时的 Program / real exit 与 architecture / behavior Evidence。不要求每次重写全 repo architecture。

被上游 shaping 调用时，只返回它当前需要的结构结论、依据、条件和 Human decision surface，不接管提问或生成第二份 Taskbook。已接受的结构边界按原 authority 提供给 Northstar / Executor；可替换技术方案不能被偷偷升级为绑定承诺。执行或运行 Evidence 推翻结构假设时重开受影响 Target；只暴露实现缺陷时不重复战略设计。需要改变 accepted outcome 或 Human commitment 时回到意图 owner，AE 不自行换 Goal。

收敛后的设计 / Program 同文写入 repo / workspace 外 Markdown 交接文件，显示真实 path；写入失败就是 blocker。获授权的稳定结论维护原 authoritative architecture source；handoff 不成为第二份 repo SOT。Human 修正或新 Evidence 后复用仍有效判断，只重算受影响部分，设计 / Program 变化时完整重交付。不输出 ready/completed/executable/status 状态词。

## 按需读取

- [strategic-design.md](references/strategic-design.md)：主判断与 bounded Evidence 后，仍有会改变 Target 的 strategic fork、authority conflict 或 boundary discriminator。
- [delivery-examples.md](references/delivery-examples.md)：设计已成立但交付易漂移，或候选疑似平台化 / 加层 / complexity relocation；示例不定义第二份 contract。
- [legacy-lenses.md](references/legacy-lenses.md)：旧模式、标记、配置、注册名等兼容身份的退出会改变 Target / Program。
- [brooks-constraints.md](references/brooks-constraints.md)：候选结构说得通但整体复杂度、第二系统或 complexity relocation 仍可疑。
