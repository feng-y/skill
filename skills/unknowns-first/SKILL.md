---
name: unknowns-first
description: "Close factual map-versus-territory unknowns with the smallest useful probe or source alignment. Route intent, concrete-shape, architecture, and verification-sufficiency questions to their semantic owners instead of solving them here."
---

# Unknowns First · 只关闭事实未知

Unknowns First 是 engineering work 的 **factual uncertainty specialist**。它处理 prompt / plan / docs / memory / assumptions 与 code / config / runtime / data / authoritative source 之间可能不一致的问题。

核心规则：

> **当下一步判断依赖一个尚未核实的事实时，不猜；用最小 probe 建立 Evidence，或明确这个问题其实属于别的 semantic owner。**

Unknowns First 不拥有 Intent，不做 concrete-shape design，不决定 Target Architecture，不定义 completion contract，也不判断一个 engineering claim 是否已经被充分验证。

## 什么时候使用

使用 Unknowns First，当一个**事实答案**不同会改变 route、scope、attribution、boundary、implementation safety 或 proof source identity，例如：

- 当前 producer / consumer / caller / runtime path 到底是谁；
- config / feature flag / data / schema / deployed artifact 实际是什么；
- baseline 是否真的 green、某条路径是否真实 reachable；
- authoritative source / reference implementation / historical contract 是什么；
- Replay/test/runtime artifact 对应哪个 build/config/input，是否 fresh；
- implementation / review 中发现 map 与 territory 冲突，需要确认实际情况。

不要因为任务复杂就默认进入 Unknowns First。没有事实 unknown 时直接返回 caller。

## Owner discriminator

先区分当前未决点属于哪种问题：

- **事实是什么？** → Unknowns First；
- **我们要什么 / Human commitment 是什么？** → `$northstar`；
- **Intent 已理解，但具体 path / usage / interface 应长什么样？** → `$prototype`；
- **长期 responsibility / boundary / dependency 应是什么？** → `$architecture-evolution`；
- **一个 accepted completion/safety claim 应如何验证、现有 Evidence 是否足够？** → `$verify`。

Unknowns First 可以发现这些问题，但不把它们吞进自己的 full-map workflow。

## L1 · Light gate

只建立四件事：

- **Decision context**：哪个当前判断依赖这个事实；
- **Territory**：哪个 code/config/runtime/data/source 能回答；
- **Unknown**：第一个会让当前 map 错掉的事实；
- **Closure Evidence**：最小什么证据足以关闭该事实。

选择一个终点：

- `continue`：事实已经足够，不需要 probe；
- `probe: <fact>; next: <territory check>`：一个小检查可以关闭；
- `ask-fact: <question>; changes: <route/scope>`：只有 Human 掌握一个事实型上下文，且答案改变 route；
- `route: <owner>; reason: <why this is not a factual unknown>`：问题属于其他 semantic owner；
- `full-map: <why coupled factual unknowns block work>`：多个事实 unknown 相互耦合，需要 L3。

只有 `continue` 可以保持静默；其他结果应让 caller 知道 next owner / probe。

## L2 · Local moves

只使用能关闭事实 unknown 的 move：

| Move | Use when | Output |
| --- | --- | --- |
| Focused probe | code/config/runtime/data 可回答 | 一个最小 read/query/log/repro |
| Reference first | existing implementation / trace / contract 是 authority | source identity + relevant semantics |
| Source alignment | docs、branch、runtime、data 相互冲突 | 区分各 source identity / provenance / freshness |
| Blindspot pass | touched responsibility surface 可能有隐藏 factual coupling | 少量 landmine + Evidence + changed action |
| Runtime/data check | static repo 不能证明真实行为 | 最小 runtime/data observation |
| Implementation note | work 可继续但存在保守事实假设 | assumption + evidence gap + impact |

不要在这里生成候选设计、mock/prototype、architecture options、build plan、proof plan、review checklist 或 decision ledger；把相应问题路由给 owner。

## L3 · Full factual map

只有用户明确要求完整 unknown map，或多个**事实未知**耦合到无法继续时，读取 [references/full-map-workflow.md](references/full-map-workflow.md)。L3 的目的只是把 unknown、Evidence、closer 与 owner 映射清楚，不成为第二套 SDLC / handoff / execution workflow。

## 与 Verify 的边界

Unknowns First 可以证明一个**事实**，例如“production 仍路由到旧 path”“这个 Replay artifact 来自 build X/config Y”“baseline 在这组 input/config 下已经 red”。

`$verify` 消费这些 factual Evidence，对 authoritative engineering claim 建立 proof obligation 与 `proven / false / unproven` judgment。若 Verify 只是缺一个事实，可以调用 Unknowns First；事实关闭后立即返回 Verify。

Unknowns First 不因为“某个事实已成立”就推导 whole-outcome PASS。例如确认 production 仍有 legacy path 是一个 fact；它是否反证当前 replacement claim 由 Verify 判断。

## 与 Prototype 的边界

如果 unknown 不是“真实系统现在是什么”，而是“Human 看到具体 path / usage / interface 后会选择哪一个”，这不是 territory probe，交 `$prototype`。Unknowns First 不再用 mock / sample / prototype 替代 concrete-shape owner。

## Feedback / fold back

返回 caller 的内容保持最小：verified fact、Evidence source / provenance / freshness、对当前判断的影响，以及仍未关闭的 factual unknown。

只有能避免重复 rediscovery 的事实才进入 durable docs / notes；一次性的 probe output 不自动成为新的 SOT。

## 常见错误

- 把 unclear Intent 当 factual unknown，在这里重新采访需求。
- 用 `Concrete sample / Four directions / Mock` 做 Prototype 的工作。
- 把 backend output 当成 whole-outcome verification judgment，而不是返回 Verify。
- 为了完整感进入 L3，把 unknown mapping 扩成 implementation plan / verification workflow。
- 事实已经足够后继续 inventory / research。
