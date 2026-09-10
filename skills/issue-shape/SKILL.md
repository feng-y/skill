---
name: issue-shape
description: "Turn current engineering intent into a durable Drafted Issue: preserve the problem, concrete intended shape, binding constraints, decisions, and acceptance needed for a fresh agent to continue without the original conversation."
---

# Issue Shape · 把工程意图编译成 Drafted Issue

Issue Shape 负责把当前 conversation、外部需求或已有讨论**编译成一个可以独立流转的 Drafted Issue**。Issue 是需求生命周期中的 canonical work-intent surface；它可以直接交给 Human、普通 coding agent、MultiCA，或在确实困难时交给 Northstar。Issue Shape 不要求 Northstar、MultiCA 或任何特定执行平台存在。

核心规则：

> **原会话消失、执行者换成 fresh agent、且 Northstar / MultiCA 都不存在时，这个 Issue 仍应让对方正确理解为什么改、准备改成什么样、哪些约束不能破坏，以及什么结果算成立。**

Issue Shape 不拥有长期 Target Architecture，不实现代码，不拆细粒度 execution tickets，不设计验证器，也不维护第二份 intent/spec/plan SOT。PR 是实际 Change / Delivery 的主对象；实现期设计、diff、validation 与 review 默认留在 PR 或其局部文档中。

## 什么时候使用

使用 Issue Shape：

- 用户要求把当前讨论、需求、incident 或外部 signal 形成 / 更新为 Issue；
- 当前 intent 需要脱离 conversation，交给另一个人、agent、session 或执行平台继续；
- Issue 已存在，但新 correction / Evidence / decision 需要判断是否 fold back 到 canonical body；
- 需要在执行前把只靠 prose 容易漂移的 intended change 做成可观察 Draft。

不因为“流程完整”强制所有临时讨论都创建 Issue。若用户只要当场完成一个不需要 tracker 生命周期的局部任务，直接完成即可。

## Drafted Issue 的最小语义

Issue body 只保留**当前仍会影响后续判断或执行的 durable 信息**。不要为了填模板制造字段。常见的最小形态是：

### Problem

当前什么需要改变，以及为什么现状不满足预期。保留真正决定优先级或取舍的 context；背景叙事不影响判断时省略。

### Draft

把 intended change 变成可观察的具体形态。根据问题选择最低成本 representation，例如：

- material `Current → Target`；
- core path / ownership / boundary / dataflow；
- caller usage；
- API / CLI / schema / config / interface；
- state transition / interaction example；
- 已完成 prototype 所回答问题的 decision-rich 结果。

Draft 不是 implementation plan。不要放 file/helper/patch 顺序、agent assignment、PR split 或可替换实现细节。

Draft 也是 reaction surface，不因被写出来就自动成为 binding commitment。Human correction、已有 authority 或已经关闭的 choice 决定哪些内容进入 durable Decision / Constraint。

### Constraints

只写真正 binding、违反后会改变 accepted outcome、兼容性、投入、风险或长期责任的约束。当前实现习惯、候选工具和可替换 How 不自动升级成 constraint。

### Acceptance

只写 fresh agent 无法可靠推导的 observable outcome / completion claim。不要把 implementation steps 或测试命令伪装成 Acceptance。

按需增加：

- **Decisions**：已经关闭、后续不应重新猜的 material choice；
- **Evidence**：会改变 Draft / Decision / Acceptance 的 repo、runtime、数据或 authoritative source；
- **Open Questions**：仍会 materially 改变 accepted outcome / boundary / commitment 的未决点；
- **Out of Scope**：只有容易被合理误解成 scope 时才写。

`Goal` 不是必填字段。只有抽象 outcome 本身能增加 decision information、区分手段与真正结果，或防止 Draft 解决了手段却没解决原问题时才显式写 Goal。

## 先综合已有讨论，不重新采访

优先消费当前 conversation 已经形成的 Human requirement、correction、decision 与已有 Evidence。不要因为进入 Issue Shape 就重做完整 intent interview。

只有一个未决答案仍会 materially 改变 Issue 的 Problem、Draft、binding boundary、Acceptance 或 Human commitment，且无法从 territory / authority 得到时，才把它暴露为 Human decision。能先查 repo/runtime reality 的事实先查，不向 Human 询问可以由 territory 回答的问题。

## 需要时调用 specialist

Issue Shape 只拥有 Issue shaping，不复制 specialist 的判断：

- **territory fact 未知**，且事实不同会改变 Issue：调用 `$unknowns-first`，消费最小 Evidence；
- **Goal / choice 已大体理解，但同一 prose 仍容许 materially different Target**：调用 `$intent-shape`，消费 Core Path / Usage / Prototype 带来的 correction / Evidence；
- **长期 responsibility、module boundary、dependency direction 或 Target Architecture 本身需要判断**：调用 `$architecture-evolution`（由其按需调用 Architecture Shape），消费结构 decision；
- **多个 binding interpretation、Human-owned trade-off 或复杂 material delta 仍无法局部关闭**：可以把现有 Drafted Issue 交 `$northstar` 做 difficult-intent judgment / compile，而不是把 Northstar 作为默认前置阶段。

specialist 结果不创建第二份 SOT。只把后续执行真正需要的 durable Decision、Draft correction、Constraint 或 Evidence fold back 到同一个 Issue。

## Issue body 与 comments

把两者视为不同职责：

- **Issue body**：当前 canonical intent / intended shape；
- **Issue comments**：讨论历史、probe 结果、候选方案、阶段性 Evidence、Human correction 与 reasoning trail。

comment 中的信息只有在后续 fresh consumer 必须知道时才 fold back。典型需要 fold back 的内容包括：新的 binding constraint、accepted Draft correction、durable decision、改变完成定义的 Acceptance。

不要把所有 comments 重写进 body，也不要让 body 因历史累积越来越长。更新时替换失效 premise，保留无关且仍有效的内容。

## Issue 粒度与执行交接

Issue 按 **cohesive engineering outcome / responsibility boundary** 切，不按一个 model context window、一次 agent session 或一个文件改动切。

Drafted Issue 可以直接交给：

- Human / 普通 coding agent；
- MultiCA 或其他 execution coordinator；
- Northstar，仅当 intent complexity 确实需要更强 judgment / Graph compile。

执行平台可以在 Issue 上增加 routing / activation tag，但 Issue Shape 不定义调度协议。接管方必须拿到或能确定性获取完整 canonical Issue；不要依赖原 conversation 或隐藏 session state 补全 Intent。

实现开始后，Issue 继续拥有 intended change；PR 拥有 realized change。普通 implementation How、diff、validation、review 进入 PR。若 PR 实施或 review 发现 Issue Draft / Decision 本身错误，先把 finding 作为 Issue Evidence / correction 回流，更新受影响的 canonical body，再让 PR 跟随新的 intent。

## 停止条件

满足以下条件就停止 shaping：

- fresh consumer 不需要原 conversation 就能理解当前 Problem 与 intended Draft；
- binding Constraint / Decision 已足以防止 materially wrong interpretation；
- Acceptance 足以区分“解决问题”和“只完成所提手段”；
- 剩余未知只影响 Executor How，或已作为真实 blocker / Open Question 暴露。

不要为了让 Issue 看起来“完整”继续 Research、设计实现、拆 tickets 或生成 spec/plan/Taskbook。

## 常见错误

- 把 Drafted Issue 写成另一份 Taskbook，塞入 file/patch/test 顺序。
- 强制恢复 Goal，即使 `Problem + Draft + Constraint + Acceptance` 已经没有歧义。
- 让 `$intent-shape`、AE 或 Northstar 生成平行 artifact，而不是 fold back 到 Issue。
- 把 Issue 切成适配单次 agent context 的细粒度 tickets；session continuity 属于 Harness / coordinator。
- 把 comments 全量复制进 body，导致 canonical surface 被历史淹没。
- 在 PR 发现 intent 错误后只修实现，不更新 Issue 的 intended change。
