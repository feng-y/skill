# Skill Repo Evolution Discipline

本文件约束**如何修改这个 skill repo 本身**，不是任何单个 Skill 的 runtime 语义。修改 Northstar、Architecture Evolution、Prompt Atlas 或其他 Skill 前先遵守这里。

总原则：**优先语义压缩，不做规则堆积。先增强、归位或简化既有模型；只有 evidence 证明存在独立且稳定的责任，才新增持久结构。**

## Structure and complexity

- **Existing semantics first.** 先判断缺口是否已经属于现有 Goal / Execution / Verification / Evidence、intent / boundary / obligation 等语义。能通过修正、压缩或增强既有语义解决，就不要新增 layer、phase、state、role、contract、schema、workflow、protocol 或 taxonomy。
- **Evidence before materialization.** Observation、distinction、partition、role、variation、provider、execution shape、case difference 默认只是 reasoning/evidence。只有它对应稳定 semantic、invariant、ownership 或长期 change boundary 时，才考虑物化。
- **New structure must remove something.** 新 abstraction / layer / protocol 必须让重复知识、分支、依赖、责任泄漏、旧路径或旧结构真实退出。若只是 `old A → new layer → old B`，默认是 complexity relocation。
- **Protocol complexity needs reality.** 复杂协议必须由真实跨边界不确定性、独立生命周期、失败语义或稳定多实现需求证明；普通单 owner / 同进程 / 同步协作不因“解耦”自动升级成协议。
- **Incidents stay in eval by default.** Concrete incidents / failures can enter validation / regression directly. Runtime guidance requires independent authority or cross-case Evidence for a transferable invariant / discriminator; a single example becoming green is not improvement Evidence. If existing semantics already cover the failure, keep runtime unchanged.
- **Runtime and eval stay separate.** runtime 只保留正常运行需要的 stable invariant / authority / boundary；具体 incident/counterexample 留在 eval；behavioral claim 必须由真实 eval 支撑。不要因 regression 增加而同步扩大 runtime context。
- **Northstar / Prompt Atlas stay bilingual, not divergent.** 两者是同一 Skill semantics 的中文/英文 surface。对 Goal / Execution / Verification / Evidence、Unknown、Taskbook、Completion Hook、trust 或 eval case 的行为性修改必须双边同步；只允许语言、名称和纯表达层差异。若要改变其中一边的 semantics，先把它当作 shared semantic change review，而不是独立 Skill 演化。

## Graph and loop

- **Work is a graph.** Material engineering work 默认按 work / outcome 与真实 dependency 组成的 Graph 判断，而不是按 prose list 判断。简单或线性工作只是 Graph 的退化形式；复杂度只决定多少关系需要显式表达。独立分支保持独立，文本顺序不能制造 dependency。
- **Keep a best-known complete graph.** 当前 Evidence 已支持的 material work 与真实关系应完整表达，不为了“thin”或 lazy 故意漏掉已知结构。若下游 work 的存在、scope 或 dependency 仍取决于上游 outcome，就停在当前 frontier，不提前猜后续 Graph。
- **Progress through a loop.** Research、execution、review、verification 都会产生新 Evidence；用它扩展、删除、拆分、合并或重算受影响的 dependency cone，并保留无关分支和仍有效 Evidence。一个 branch blocked 不冻结独立 work，一个 premise 改变也不要求全量重来。
- **Graph / loop are engineering forms, not new semantics.** 不为了“使用 Graph / Loop”新增 Graph object/schema、node taxonomy、persistent state、scheduler、manager protocol 或第二套 lifecycle。既有 semantic owner 继续负责；只有真实 ownership、lifecycle、failure semantics 或稳定多实现需求要求时，才物化额外 runtime structure。

## Context engineering and judgment quality

- **Context improves judgment; it does not replace judgment.** 暴露 intent、reality、invariant、authority、decisive evidence；不要在模型可以自行判断时编码固定 reasoning path 或答案。真实 repo / environment 约束可以规定 HOW，纯 epistemic HOW 默认交给模型。
- **Load only decision-relevant context.** Always-on / current context 中的信息必须能实际改变当前 judgment。背景、历史、示例和未来可能有用的信息优先 routing/reference，按需 progressive disclosure。
- **Encode discriminators, not remembered answers.** 描述让两个 case 真正不同的 discriminator / invariant，而不是记住某个 case 的结论。例如 `scope follows actual reachability / authority`，而不是 `cleanup 要 replay`。
- **Prefer territory over duplicated descriptions.** 默认事实优先级：`current code / test / config / runtime evidence > stable repo contract > authoritative current docs > historical explanation > case narrative`。能从 repo reality 重新判断的事实，不复制成第二份易漂移 SOT。
- **Examples do not become runtime priors.** Example、incident、captured output、regression 用于 eval；runtime 只保留有 authority 或 generalization Evidence 支持的 general invariant。

## Review gate

修改 `AGENTS.md`、`CLAUDE.md`、`SKILL.md` 或 runtime references 时，至少回答：

1. 新增 context / structure 支持哪个具体 judgment 或责任？
2. 已有语义为什么不能拥有它？
3. 它有 independent authority，或有跨 case Evidence 支持为 stable invariant / discriminator，还是一次 case 的答案？
4. 它加入后什么旧规则、知识、结构或复杂度会退出？
5. 它能否下沉到按需 reference 或 eval，而不是进入 always-on runtime？

答不出基于 evidence 的理由，默认不新增。

## Placement

- Repo-wide evolution / context rules：只放这里。
- Skill runtime invariant：放对应 `SKILL.md` 或按需 runtime reference。
- Case / incident / counterexample：放 validation / regression，正常 runtime 禁止读取。
- `CLAUDE.md` 只作为薄入口指向本文件，不复制规则。
