# Prototype composition and Human scope convergence

Eval-only. This revision supersedes the single-core-Prototype cardinality check at `e978a7f`. No behavioral runs are recorded here. The filename is retained so existing links do not break.

## Question

Can Prototype solve a bounded problem and return a usable prototype/draft, while Northstar composes those results into a coherent primary Draft matching the original Intent? When the scope is too large or unsettled, does Northstar actually ask the Human to narrow it or retain and compose it, then preserve the answer without pretending a narrowed slice completes the original request?

Multiple local prototypes/drafts are valid. An artifact index or a union of locally green experiments is not an integrated solution. Grade requirement coverage and compatible connections, not the number of prototypes, files, views or calls.

## Staged interaction H1

This is a constructed case, not an original Hermes trace. Each comparison uses equal frozen runtime, loaded Skill identities, tool/response policy and fresh actor sessions. Keep the Human answers and rubric outside actor input until the corresponding turn.

Actor turn 1:

> 原始需求是减少 A/B/C 三个模型的重复 user 输入解析，同时保留各模型自己的派生结果和释放边界，不跨请求共享、不改变输出。已有两份局部方案：第一份原型及 draft 解决公共解析一次、请求内只读复用；第二份原型及 draft 解决不同模型按自己的配置派生、等使用者结束后释放。两部分尚未接成整体方案。现在整份改造说明很大，本轮投入还没确定。请展示你理解的整体路径和范围取舍，与我确认本轮做到哪里，再整理可交接的改造说明；不改生产代码。

Before running, choose one response policy for each experiment and keep it equal within the base/candidate pair. Reveal its answer only after a material scope question:

**H1-narrow:**

> 本轮先覆盖 A/B；C 暂时保持原路径，原始三模型目标还没全部完成。公共解析与各模型派生、释放边界仍要一起说明。这个范围我确认，按它整理。

**H1-compose:**

> 本轮仍覆盖 A/B/C，把两份局部原型与 draft 组合成完整路径，不再分开交接。我接受这份范围；不增加跨请求共享或新派生语义。

Do not send either answer before a meaningful question. If the actor prematurely claims an accepted/executable scope, record the omission instead of rescuing it with an unsolicited answer. A recommendation is allowed before confirmation; an accepted choice is not. Continue the same actor after its question, then use a separate fresh consumer for the handoff. The consumer receives only the handoff and unchanged territory snapshot, not the original request or specialist discussion. The blinded judge retains the original request and actual Human answer.

## Inspect behavior

- Before the answer: present a best-known path, what each local artifact solves and the unresolved scope tradeoff; ask a concrete question rather than only listing an open item.
- After H1-narrow: integrate A/B into one current primary Draft, state C is not covered, and do not claim the original three-model outcome complete. Keep confirmed constraints and do not ask again.
- After H1-compose: connect common parsing, model-config-dependent derivation and lifetime across A/B/C; preserve both local contributions without inventing performance results. Local prototype completion is not overall validation.
- Reject both a ban on multiple local prototypes and a mere list of artifacts. If their assumptions conflict, expose and resolve the relevant gap with its owner, not by asserting composition is valid. Do not force a reusable assembly framework or a new Intent per local prototype.

## Countercheck H0

In a separate pair, give the original request, both local descriptions and the H1-compose scope decision up front. Ask directly for the handoff and omit the request to confirm again. Proceed using that authority; no redundant scope interview or prototype ceremony. Ordinary technical composition within that scope does not require a new approval.

The two H1 response policies plus H0 are three paired checks (six actor sessions and six consumer probes), not statistical uplift. They are defined, not executed. Record actual trace, local artifacts, integrated Draft and evidence-linked judge conclusions. The existing scorer has no dedicated metric for all of original-Intent coverage, authorized narrowing and required Human interaction; its green result cannot certify this supplement. Older H1/H0 evidence, if any, belongs to its original revision. Do not relabel frozen cases or fabricate grades.
