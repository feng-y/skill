# Northstar / Architecture Evolution 改进候选（ECC 对照）

> Status: backlog only. 本文只收集候选，不改变任何 Skill runtime、reference、agent、eval 或执行行为。

## Goal

从 ECC 当前实现里只保留可能提高 **evidence → judgment → contract** 质量的机制，和 `main` 上现有 Northstar / Architecture Evolution 做 delta 对照，避免把已经覆盖的语义再次实现成新 layer、schema、checklist 或 workflow。

后续若实施，应一次性从这份 backlog 重新 review 后形成一个 cohesive change；本文本身不是 implementation contract。

## Baseline on current main

当前实现已经覆盖以下能力，不作为新的待实现功能：

- Architecture Evolution 已显式区分 `Observed / Inferred / Unknown`，并要求 material unknown 通过 `claim at risk → minimal probe → evidence → intent changed / retained` 关闭；
- Architecture Evolution 已按 judgment need 恢复最小现实，只展开会改变 intent / boundary / obligation 的 evidence；
- Architecture Evolution 已有 `Replacement / exit` 与 `Replacement evidence`，并要求新 abstraction 真实替代旧路径/知识/依赖；
- Northstar 已保持 `Goal → Execution / Graph → Verification → Evidence`，Verification 从真实 impact/reachability、repo authority 和 Human authority 编译，而不是固定 build/test/replay 套餐；
- Northstar 已把具体 agent topology / scheduler / Graph engine 排除在 Taskbook runtime semantics 之外；
- Northstar 已要求重要 Research 结论回到 source pointer，并让 Completion Hook 只依赖 current valid Evidence。

因此 ECC 中 generic planner/architect、固定 verification checklist、通用 high-cohesion/low-coupling rules 不进入 backlog。

## Implementation candidates

### A1. Architecture Evolution — strengthen decisive evidence with enforcement / consumption anchors

**Signal from ECC:** `spec-miner` 不只记录“哪个文件相关”，还把行为绑定到真实 enforcement point、caller/test anchor，并在文档声明与实际 caller 行为冲突时优先 cross-validate territory。

**Current gap:** Architecture Evolution 已要求代码/runtime evidence，但 `Decisive reality and evidence` 仍可能停在 declaration、命名、文档或表面结构。对 semantic owner、ownership/lifecycle、runtime control、consumer reassembly 这类判断，真正决定架构现实的往往是“谁实际 enforce / choose / consume / sequence / own lifetime”。

**Candidate strengthening:**

- 对会决定 intent 的 ownership / semantic-authority / runtime-control claim，优先寻找真实 enforcement / consumption anchor；
- declaration / type shape / docs 可以作为 evidence，但在它们与 runtime/caller reality 冲突时不能单独支持 decisive judgment；
- 保持在现有 `Evidence` / `Decisive reality and evidence` owner 内，不新增 `declared_at/enforced_at/consumed_by` 输出 schema；这些只作为 reasoning vocabulary 或 source pointer precision；
- 只在该 anchor 会改变 architecture judgment 时继续展开，避免变成全 repo trace checklist。

**Regression cases worth adding before runtime change:**

1. 名义上的 manager/provider 看似 owner，但 caller 仍组合 ordering/config/lifecycle；
2. 配置声明显示路径 A，effective runtime binding 实际选择路径 B；
3. doc/interface 声称统一语义，但 callers 依赖不同 enforced behavior；
4. clean source dependency 与真实 runtime ownership 不一致。

**Success condition:** 更少把 apparent ownership / declaration 当成 effective architecture reality，同时不增加 mandatory template 字段或扫描深度。

---

### A2. Architecture Evolution — make `Replacement evidence` prove architecture delta, not only behavioral preservation

**Signal from ECC:** `codehealth-mcp` 有一个值得保留的最小思想：记录 change 前的 structural evidence，change 后检查 delta，而不是只看“功能仍然能跑”。不采用它的 numeric score。

**Current coverage:** `main` 已有 Real Evolution gate、Replacement / exit、Replacement evidence，因此这不是新 completion layer。

**Candidate strengthening:** 在已有 `Replacement evidence` / Brooks `Proof expected` 语义里明确：如果 intent 承诺删除 duplicated semantic owner、caller reassembly、reverse dependency、compat branch 或旧知识，downstream closure 必须证明该 **architecture delta 实际发生**；behavioral tests PASS 只能证明 must-preserve，不足以证明 evolution 完成。

典型可观察 proof：

- old semantic owner / duplicate interpretation 不再 active；
- callers 不再需要重新组合本应由 capability owner 持有的知识；
- forbidden/reverse dependency 消失，而不是被 wrapper/registry 转移；
- compatibility/legacy path 在承诺退出时真实退休；
- 新 abstraction 吸收旧结构后，旧 branching/knowledge 确实减少。

不要求固定 pre/post score、统一 metric 或新的 `Architecture Delta` section；优先增强现有 replacement proof 的判卷质量。

**Success condition:** 能抓住“tests 全绿但只是 old A → new wrapper → old B”的 complexity relocation。

---

### N1. Northstar — preserve verification authority anchors through compile

**Signal from ECC:** `spec-miner` 的稳定 anchor 思路比 generic verification checklist 更有价值；一个 claim 不只要有 proof，还要能追溯“哪里真正 enforce / verify 它”。

**Current coverage:** Northstar 已要求 Research 结论有 source pointer，Verification 已保留 stable trigger/authority，Evidence 也记录 provider/target/revision/binding。

**Potential gap:** 在 compile 压缩后，material required Verification 可能保留“要 replay/test/check 什么”，但弱化“为什么这个 obligation 是 binding”的 authority provenance，导致 Executor 后续把它重新解释成 optional check。

**Candidate strengthening:**

- 对 material required Verification，保证它能追溯到至少一个真实 authority / trigger：Human explicit requirement、repo verification authority、或由 actual impact/reachability 推导出的 binding rule；
- authority anchor 只需 source pointer / derivation，不新增 Verification schema；
- provider 可以运行期 materialize，但 binding obligation 的 provenance 不能随压缩丢失；
- expected `0-diff`、cleanup/refactor 标签不能覆盖这个 authority anchor。

**Regression cases worth adding before runtime change:**

1. shared source owner 触发 production replay，但 task label 看起来只是 offline cleanup；
2. Human 明确要求某验证，Executor 找到更便宜 provider 后误降级 coverage；
3. repo rule 只在 effective binding 成立时触发，Task 0 关闭 binding 后 obligation 应稳定 materialize；
4. summary 保留 check 名称但丢失 trigger，后续 agent 把它当建议而非 requirement。

**Success condition:** Verification 仍保持轻量、provider-neutral，但 binding gate 不因 compile/handoff 摘要化而失去 authority。

## Watch items — do not implement without new evidence

### N2. Taskbook → Execution Projection boundary

ECC `plan-orchestrate` 把 authoritative plan 映射到 agent chain，这个 separation 有参考价值；但 Northstar 当前已经明确不拥有 fixed agent topology / scheduler，并把 implementation judgment 留给 Executor。

暂不新增 `Execution Projection` layer、section 或 protocol。只有后续真实 case 证明 agent/tool/session/parallelism 再次泄漏进 Taskbook semantic ownership，才考虑增强既有 Executor/runtime boundary；优先修改现有 owner，不物化新层。

### A3. Sample-and-expand discovery

ECC `spec-miner` 的 sample-and-expand 与 Architecture Evolution 当前“恢复最小现实、只展开会改变 judgment 的 evidence”基本同义。当前版本按 **judgment need** 停止，比固定 file-count/token budget 更合适。

不实现 ECC 的 `15 files`、固定 call-depth 或 scan-depth taxonomy。若以后出现 discovery 失控，应先增加 eval case，证明缺的是 stop discriminator，而不是机械预算。

### A4. Fact / inference / uncertainty

已经由 `Observed / Inferred / Unknown` 和 Material Unknown falsification 覆盖。不要重复成 `fact/inference/uncertainty` 第二套 taxonomy。

### N3. Fixed verification loop

ECC `verification-loop` 的 build/type/lint/test/security/diff 固定阶段只作为反例。Northstar 继续从 Goal、impact/reachability、repo/Human authority 编译 obligation，不吸收固定套餐。

## Source signals

Pinned ECC sources reviewed for this backlog:

- `spec-miner`: https://github.com/affaan-m/ECC/blob/2d46e80e0925c7be0907f18c1812311ac212a6c5/agents/spec-miner.md
- `plan-orchestrate`: https://github.com/affaan-m/ECC/blob/2d46e80e0925c7be0907f18c1812311ac212a6c5/skills/plan-orchestrate/SKILL.md
- `codehealth-mcp`: https://github.com/affaan-m/ECC/blob/2d46e80e0925c7be0907f18c1812311ac212a6c5/skills/codehealth-mcp/SKILL.md
- `verification-loop` (counterexample): https://github.com/affaan-m/ECC/blob/2d46e80e0925c7be0907f18c1812311ac212a6c5/skills/verification-loop/SKILL.md

## Later implementation gate

实施前重新 review 本文与届时 `main`，并遵守：

1. **Delta first** — 已被 current semantics 覆盖的条目直接删除，不机械实现 backlog；
2. **Existing owner first** — A1/A2 优先增强 Architecture Evolution 现有 Evidence / Success evidence；N1 优先增强 Northstar 现有 Verification / Evidence，不新增 layer/schema/status；
3. **Eval before prose** — 先写能复现 gap 的 general regression case，再决定是否需要 runtime wording；
4. **One cohesive implementation** — 剩余候选一起 review ownership/duplication/context cost 后再实施，避免连续小 PR 堆规则；
5. **No uplift claim without evidence** — source-level consistency 只能证明结构合理，behavioral uplift 需要独立 eval。

## Explicit non-goals of this backlog PR

- no changes to `skills/northstar/**`;
- no changes to `skills/architecture-evolution/**`;
- no new runtime rule, reference, agent, role, state, schema, stage, workflow or verification package;
- no implementation of ECC agents/skills;
- no claim that ECC is a correctness oracle;
- no claim of measured behavioral improvement.