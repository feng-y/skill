# Evaluate Architecture Evolution

本文件只用于 Skill smoke/eval，正常运行禁止读取。运行时设计验证见 [verification.md](verification.md)。

## Static smoke

冻结当前 branch/head 后检查：

- frontmatter 与 `agents/openai.yaml` 可解析；
- `SKILL.md` 的相对引用均存在；
- 正常架构分析不指示读取本文件；
- 四条 Rule 与一个 `Replace, not layer` Gate 在 `SKILL.md` 和 `rules.md` 中一致；
- agent prompt 不重复注入完整规则；
- 四种状态名称一致；
- 非 `Design ready` 状态不会输出 target seam 或 Design Delta；
- Northstar 仍拥有 Goal、授权、任务书、执行与完整验收。

任何失败都先修结构，不进入 behavioral eval。

## Scenario smoke

### P1 — Variation ownership leak

provider/family/mode 判断散落多处，但至少一个相似判断承担不同语义。

通过：Rule 1 或 Rule 2；区分重复解释与合法差异；指定 variation owner；不机械套多态；写出可消失的判断或事实源。

### P2 — Independent change reasons

模块混合核心语义与 metrics/debug/cache/config/compatibility，部分辅助能力应保持私有。

通过：Rule 4；只拆真实独立的 owner、生命周期或验证边界；不做 one-module-per-concern。

### P3 — Shallow seam

wrapper 透传，调用者在外部拼装 config/state/runtime/order，测试重复内部编排。

通过：Rule 3；使用 deletion test；形成完整 capability seam；减少 caller knowledge；不新增 wrapper。

### N1 — No architecture change

owner 清楚、变化局部的普通 bug 或机械修改。

通过：`No architecture change`；只输出证据、局部原因与修改边界；无 target seam 或 Design Delta。

### R1 — Research required

legacy path 是否仍有消费者会改变 owner 和删除方案；repo/runtime 可查，但证据缺失。

通过：`Research required`；只输出已确认事实、一个 design-changing Unknown、最小探针和受影响字段；不提前设计。

### D1 — Decision required

两种结构都可行，但公开兼容与长期双轨成本属于 Human 取舍。

通过：`Decision required`；只输出共同边界、Human-owned 决策、少量选项和推荐；不伪造唯一答案。

Scenario smoke 是合同审计，不等于 clean-session behavioral eval。

## Paired behavioral eval

在支持隔离 clean session 的 runtime 中，对同一任务和 repo snapshot 运行：

```text
A. 同模型，不加载 architecture-evolution
B. 同模型、工具和预算，加载 architecture-evolution
```

冻结任务、repo commit、可见文档、模型版本、工具权限和预算；两臂不得共享输出。

每项 `0–2` 分：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Evidence grounding | 审美判断 | 部分证据 | Observed / Inferred / Unknown 分离 |
| Primary diagnosis | 漏掉或罗列 smell | 找到症状 | root owner/seam 错误 + 反例 |
| Design quality | 模式名或空泛目标 | 部分可用 | owner、variation、dependency、seam 明确 |
| Scope control | 全面重构 | 大体局部 | 一个目标、一个主问题、明确不做什么 |
| Abstraction restraint | 新增壳层 | 混合 | 拒绝假 seam，并说明替代/删除 |
| Improvement proof | 只说更解耦 | 有 before/after | 五个维度可观察 |
| Status judgment | 状态错误/泄漏 | 正确但偏重 | 正确且最小充分 |

## V0 pass gate

1. P1–P3 至少两个案例中，B 臂的 `Primary diagnosis + Design quality + Improvement proof` 比 A 臂高至少 2 分；
2. 正样本只选择一个 primary violation；
3. B 臂的 Scope control 和 Abstraction restraint 不低于 A 臂；
4. N1、R1、D1 状态正确且无 status leakage；
5. 每个 `Design ready` 有具体 replacement/delete；
6. 未执行实现证据时，不声称行为保持或迁移完成。

失败分类：`signal miss`、`root-cause miss`、`pattern reflex`、`scope expansion`、`false abstraction`、`difference collapse`、`false positive`、`unverifiable gain`、`status leakage`。

同一种 failure 在两个代表性案例重复出现后，才修改 Rule。

## Claim boundary

Static/scenario smoke 只能证明合同和文本机制一致；paired eval 只能证明冻结样本上的设计质量差异。实现正确性、行为对等、迁移完成、实际删除和生产维护成本都需另行验证。
