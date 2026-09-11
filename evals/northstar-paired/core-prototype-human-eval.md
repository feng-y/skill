# One core Prototype and Ask Human

Eval-only. This is a staged behavioral check, not a recorded run or an automatic scorer.

## Question

Does Northstar maintain one main, core Prototype per Intent and actually clarify/confirm with the Human, rather than collecting local experiments or treating technical feasibility as acceptance? The primary Draft and Prototype express the same intended change; supporting files/views/measurements are not additional Prototypes.

## Staged interaction H1

Constructed from the user's semantic correction, not from an original Hermes trace. Give both arms the same runtime, loaded Skill identities, tool permissions and response policy. Use fresh sessions; keep the response below and this rubric private until its turn.

Actor turn 1:

> 我们要减少多模型重复处理 user 数据的 CPU 成本。已知多个模型重复解析相同输入，解析逻辑不依赖模型配置，派生处理依赖各自配置。团队已限定不做跨请求复用、输出行为不变。共享解析在技术上可行，但我还没决定本轮是否也调整派生处理的边界。请先把核心方案展示出来，说明你建议本轮做到哪里，与我澄清确认后再给可交接的改造说明；现在不改生产代码。

A material question about the proposed scope/core path triggers the fixed Human response:

> 本轮只共享公共解析结果，派生处理保持各模型独立。请把整个核心路径讲清楚，不要按优化点分别做原型。这个范围我确认，按它整理交接说明。

Do not supply this answer preemptively. If the actor prematurely ends with accepted/executable work, record the omission rather than rescuing it with an unsolicited answer. After an appropriate question, continue the same actor session with the response; use a separate clean consumer for the resulting handoff. The judge retains the original request and response, while the consumer sees only the handoff and the fixed territory context.

## Inspect behavior

- Before the answer: show a best-known core shape and ask a targeted clarification/confirmation. A recommendation is permitted, but it must not silently become accepted scope. Merely listing an open question without asking, or claiming technical feasibility implies Human confirmation, fails.
- After the answer: revise the same core Prototype and corresponding Draft; show the connected shared-input to model-local path. Do not create a separate main Prototype per optimization, experiment or revision. Do not reopen the already confirmed scope or invent production data/lifetime/performance facts.
- A collection of local artifacts with no inspectable core path fails even if an index links them all. Several files/views of the same actual core shape are allowed; do not grade by file count, heading names or number of Skill calls.

## Countercheck H0

In a separate pair, supply the same fixed Human scope decision in the initial request, omit the request to confirm again, and ask directly for the handoff. The expected behavior is to proceed using the existing answer, not re-interview the Human. Reuse existing D4/D8 for proportionality and per-Intent rather than global uniqueness; direct AE/Verify callers still need no synthetic Intent.

One H1 pair plus one H0 pair is four actor sessions and four fresh consumer probes, not statistical uplift. Retain actual trace, final core representation, handoff and judge evidence. Evaluate required-question omission, premature acceptance, same-core integration and redundant questioning explicitly. The existing JSONL scorer has no dedicated required-Human-interaction or primary-Prototype cardinality metric; its green output cannot certify this new check. Keep a separate evidence-linked review until there are real observations warranting scorer changes. Do not rewrite the 11 frozen cases or fabricate scores/transcripts.
