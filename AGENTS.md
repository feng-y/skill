# Skill Repo Evolution Discipline

本文件约束**如何修改这个 skill repo 本身**。它不是任何单个 Skill 的 runtime 语义。修改 Northstar、Architecture Evolution、Prompt Atlas 或其他 Skill 前，先遵守这里的约束。

总原则：**优先语义压缩，不做规则堆积。先增强或收回既有模型；只有证据证明存在独立且稳定的责任，才新增持久结构。**

## 1. Structure and complexity

### Existing semantics first

发现缺口时，先问它是否已经属于现有 Goal / Execution / Verification / Evidence、intent / boundary / obligation 等既有语义。

能通过修正、压缩、归位或增强既有语义解决，就不要新增 layer、phase、state、role、contract、schema、workflow、protocol 或 taxonomy。

### Evidence before materialization

Observation、distinction、partition、role、variation、provider、execution shape、case difference 等默认只是 reasoning/evidence，不自动成为持久结构。

只有 evidence 证明它对应稳定 semantic、invariant、ownership 或长期 change boundary，才考虑物化。

### New structure must remove something

新增 abstraction / layer / protocol 必须说明它会让什么真实退出：重复知识、分支、依赖、责任泄漏、旧路径或旧结构。

如果只是 `old A → new layer → old B`，而旧知识、旧路径和旧责任仍存在，默认视为 complexity relocation，而不是改进。

协议复杂度必须由真实跨边界不确定性、独立生命周期、失败语义或稳定多实现需求证明；普通单 owner / 同进程 / 同步协作不因为“解耦”自动升级成复杂协议。

### Incidents stay in eval by default

单个 case / failure 默认进入 validation / regression，而不是 runtime rule。

只有它能被压缩成一个脱离原 case 仍成立的 stable invariant 时，才晋升为 runtime guidance；晋升应优先 generalize / replace 已有规则，而不是在旁边继续追加 case-specific rule。

### Runtime and eval stay separate

- runtime：agent 正常运行时真正需要的 stable invariant / authority / boundary；
- eval：证明这些 invariant 没退化的具体 case、incident、counterexample；
- behavioral claim：必须由真实 eval 支撑，不能由 source review 冒充。

不要因为 regression 增加，就同步扩大 runtime context。

## 2. Context engineering and judgment quality

### Context improves judgment; it does not replace judgment

Context 应暴露 intent、reality、invariant、authority、decisive evidence；不要在模型可以根据这些信息判断时，编码固定 reasoning path 或答案。

真实 repo / environment 约束可以规定 HOW；纯 epistemic HOW 默认交给模型判断。

### Load only decision-relevant context

进入 always-on 或当前 runtime context 的信息，必须能实际改变当前 judgment。

背景、历史、示例、未来可能有用的信息优先保留 routing/reference，按需 progressive disclosure，不因为“可能有帮助”就全部注入。

### Encode discriminators, not remembered answers

Repo guidance 应描述让两个 case 真正不同的 discriminator / invariant，而不是记住某个 case 的结论。

例如写“scope follows actual reachability / authority”，而不是“cleanup 要 replay”；写“observed partition is evidence, not architecture boundary”，而不是枚举每种禁止 abstraction。

### Prefer territory over duplicated descriptions

判断事实时优先级默认是：

`current code / test / config / runtime evidence > stable repo contract > authoritative current docs > historical explanation > case narrative`。

能从 repo reality 重新判断的事实，不要在 instructions 中复制成第二份易漂移 SOT。

### Examples do not become runtime priors

Example、incident、captured output、regression 用于 eval，不应在正常 runtime 中形成默认答案暗示。

具体 case 留在 validation/regression；runtime 只保留已经被压缩后的 general invariant。

## 3. Review gate for repo changes

修改 `AGENTS.md`、`CLAUDE.md`、`SKILL.md` 或 runtime references 时，至少回答：

1. 这段新增 context / structure 支持哪个具体 judgment 或责任？
2. 已有语义为什么不能拥有它？
3. 它是 stable invariant / discriminator，还是一次 case 的答案？
4. 它加入后什么旧规则、知识、结构或复杂度会退出？
5. 它是否可以下沉到按需 reference 或 eval，而不是进入 always-on runtime？

如果这些问题不能给出基于 evidence 的答案，默认不新增。

## 4. Placement

- Repo-wide evolution / context rules：只放这里，避免复制进每个 Skill。
- Skill runtime invariant：放对应 `SKILL.md` 或按需 runtime reference。
- Case / incident / counterexample：放 validation / regression，正常 runtime 禁止读取。
- `CLAUDE.md` 只作为薄入口指向本文件，不复制本规则。
