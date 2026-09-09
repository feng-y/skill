# Intent shaping and architecture responsibility review

Eval-only design/review record. Not a runtime reference or a new lifecycle.

Base: `feng-y/skill@48c200f6c336ed1480f11dd67a1bbab2ccdbc605`.
Review date: 2026-09-09. Scope: Northstar and Architecture Evolution (AE).

## Decision

Northstar's primary work is Intent take, including necessary intent shaping: recover the problem, accepted outcome, decision-relevant why/obligation, scope, constraints, and Human commitments. Intent compile is the execution handoff of those judgments, not a substitute for them. Goal remains the accepted-outcome semantic inside Intent/Taskbook; it does not need its own file, phase, approval, or mandatory heading.

AE owns technical strategic design under that intent: responsibility/knowledge ownership, boundaries, variation, justified dependencies, and falsifiable structural outcomes. It accepts enough intent to answer the current question, not a document bearing a particular name. It can answer a conditional structural question during shaping without inventing approval for that hypothesis. Neither skill owns execution orchestration; Northstar does not implement the Goal, and AE does not replace business intent with a preferred architecture.

These capabilities are not a compulsory linear pipeline. Clear local work can bypass AE. Unsettled intent can use bounded architecture evidence before a final execution contract exists. Each returns to the other only when new evidence changes a judgment that the other owns. One authoritative source per decision remains sufficient; this change introduces no `intent.md -> goal.md -> spec.md -> plan.md` file ladder.

## What the base already covers

The base already separates means from outcomes, binds Human commitments to Human authority, allows bounded prototypes, limits research to material decisions, preserves real Graph dependencies, and independently judges outcomes. Those contracts are retained rather than described as missing capabilities.

The reviewed weaknesses are narrower: Northstar's handoff describes Goal/constraints but does not explicitly preserve the problem/why needed to interpret choices; its root presentation makes shaping subordinate to producing a Taskbook even for a shaping-only request. AE's repeated Goal-first wording and invocation recipe can obscure its ability to answer an existing intent or a bounded question during shaping. These are instruction/contract findings, not measured failure frequencies. Compression of AE removes repeated exposition; it is not proof of better model behavior.

## Sources and selected changes

The user's X link is https://x.com/shao__meng/status/2093990789584236857 . Direct X retrieval returned 403. A matching attributed republication was found at https://www.jxxy.net/ai/articles/ai-native-sdlc-reports/ . It was used to locate the discussed materials, not as the technical authority for this change.

| Primary source checked | What it supports | Change selected here |
| --- | --- | --- |
| [Anthropic, The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook), Planning/Design/Build | Capture what is wanted, why, constraints and open questions; design and implementation plans serve different purposes. | Preserve decision-relevant intent rather than only a Goal summary. Do not copy the article's artifact ladder or stage approvals into every task. |
| [OpenAI, Building an AI-native engineering team](https://cdn.openai.com/business-guides-and-resources/building-an-ai-native-engineering-team.pdf), printed pp. 5-8, 10, 12-13 | Code-aware scoping and prototypes help expose ambiguity; product direction and material commitments remain human-owned; proof must align with intended behavior. | Use bounded reality/prototypes for shaping, keep business authority distinct from technical analysis, and retain acceptance obligations. |
| [Addy Osmani, The New Software Lifecycle](https://addyosmani.com/blog/new-sdlc-vibe-coding/), Context engineering/Verification/How each phase changes | The whitepaper co-author explains on-demand context, requirements conversations/prototypes, structural trade-offs, and output plus trajectory evaluation. | Shorten AE's repeated root/invocation instructions without deleting strategic discriminators; keep probes conditional. The Kaggle whitepaper page was located but full PDF text was not retrieved. |
| [LangChain, The Agent Development Lifecycle](https://www.langchain.com/blog/the-agent-development-lifecycle), Test/Monitor/Iterate | Task-specific criteria, multi-turn evaluation, and feedback-derived cases distinguish a plausible response from task success. | Define separate shaping and architecture probes; do not grade non-coding outputs with code-quality scores or equate static review with reliability. |
| [AWS, AI-Driven Development Life Cycle](https://aws.amazon.com/blogs/devops/ai-driven-development-life-cycle/), How it works | Business intent is elaborated before construction; context is carried between activities. | Preserve clarified intent into design/handoff. Do not import new rituals, phase names, or blanket human approvals. |

These are design/practice sources, not controlled evidence that this candidate improves Northstar/AE. No productivity multipliers or benchmark claims are used.

## Focused probes

These are frozen semantic probe specifications and manual contract checks, not transcripts of executed agents. Resolve each probe to pinned repo/source facts and an exact user prompt before a clean-session run. Evaluate only the relevant outputs; a shaping-only call is not an executable-handoff failure.

| Probe | Input / distinction | Required observation | Failure to reject |
| --- | --- | --- | --- |
| I1 Existing clear intent | A request already states its outcome, why it matters, scope, and constraints, but has no Goal heading. | Reuse the content and complete the requested judgment or handoff. | Invent a Goal document, re-interview the Human, or add an approval gate. |
| I2 Same Goal, different intent | The same latency target serves either an exploratory experiment or an established obligation; allowed investment differs. | Preserve the decision-relevant why/obligation and commitment without preselecting implementation. | Erase the distinction in a Goal sentence, invent a business rationale, or cancel an obligation merely because ROI is low. |
| I3 Shaping only | Human asks to resolve a problem framing, not implement it. | Return the resolved intent or the genuine remaining choice. | Force an implementation Taskbook, Graph, new tool, or production change. |
| I4 Discriminating prototype | Two intent interpretations differ in user workflow; a cheap reversible sample can distinguish them. | State the question, use only the needed probe, and treat observation as evidence. | Ask endlessly, force a prototype when facts suffice, or silently promote it to production scope. |
| I5 Conditional AE consultation | Shaping needs to know the structural consequences of an unresolved long-term commitment. | AE answers under explicit assumptions; Northstar returns the genuine Human trade-off without treating it as settled. | Require a finalized Goal artifact before analysis, or treat technical feasibility as approval. |
| I6 Local work bypasses AE | Intent can be met inside existing stable responsibility/boundaries. | Compile or execute through the existing owner without compulsory Strategic Design. | Force the Northstar-to-AE-to-Executor ladder or invent a Program. |
| I7 Architecture proof | A proposed facade preserves behavior but leaves caller dependence on old private knowledge/authority. | Separate behavior parity from structural improvement; require the material legacy exit. | Accept test green as structural proof, or reduce design to byte/file-count scoring. |
| I8 Feedback re-entry | A verified observation either reveals an implementation gap or invalidates the intended workflow/structural premise; one unrelated branch remains valid. | Reopen only the affected judgment with the appropriate owner; preserve unaffected evidence. | Turn every failure into new strategy/intent, accept self-report, or reset the whole task. |

## Review scope and measurements

Retain the base's existing Northstar static/scenario contract and AE static/behavior properties. In particular, check known-Graph completeness, contingent frontier, real dependencies, whole-Goal judgment, candidate-Evidence gating, false-vs-unproven, Human authority, conditional references, and real structural exits. The existing references remain unchanged except `northstar/references/intent-shaping.md`; no new runtime reference is added.

For actual runs, record semantic outcomes rather than a generic score: loss of decision-relevant intent, redundant Human clarification, unsupported binding choices, fresh-Executor reinterpretation, unsupported architecture work, and missing structural proof. Measure latency/tools only together with accepted output. For executable Taskbook probes use the [existing paired eval](README.md); for shaping/architecture-only probes keep separate claim-based adjudication instead of relabeling them as handoffs. Do not alter the scorer's schema/sample gates.

Validation performed on the candidate: parse both frontmatters and UI YAMLs; check skill invocation names, UTF-8/newlines, relative runtime links against the pinned repository inventory, and that normal-runtime links do not pull in eval files. Manual review checks I1-I8 against the candidate and unchanged routed references. A review fix retained the existing exception for authority-bound representations in AE; ordinary file/API/test-provider selection stays with Executor.

No clean-session model runs or fresh-Executor executions were performed. The current environment has no Codex/Claude executable. No behavioral uplift, reliability percentage, or latency/token gain is claimed. Skill Doctor is not reintroduced, and unmerged PR #82 is neither merged nor rewritten by this change.
