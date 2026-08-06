# Evaluate Architecture Evolution

本文件只用于 Skill smoke/eval，正常运行禁止读取。运行时设计验证见 [verification.md](verification.md)。

## 1. Static smoke

冻结当前 branch/head 后检查：

- frontmatter 与 `agents/openai.yaml` 可解析；
- `SKILL.md` 的相对引用均存在；
- 正常 Flow 不引用本文件；
- 四条 Rule 与一个 `Replace, not layer` Gate 在 Skill、rules、agent prompt 中一致；
- 四种状态名称一致；
- 非 `Design ready` 状态不会输出 target seam 或 Design Delta；
- Northstar 仍拥有 Goal、授权、任务书、执行与完整验收。

任何失败都先修结构，不进入 behavioral eval。

## 2. Scenario smoke

使用相同模型和 repo 证据，至少覆盖：

### P1 — Variation ownership leak

provider/family/mode 判断散落在构造、执行、配置或调用者中，但至少一个相似判断承担不同语义。

通过条件：选择 Rule 1 或 Rule 2；区分重复解释与合法差异；指定一个 variation owner；不机械套多态；写出可消失的判断或事实源。

### P2 — Independent change reasons

一个模块混合核心语义与 metrics/debug/cache/config/compatibility，其中部分辅助能力应保持为私有实现。

通过条件：选择 Rule 4；只拆真实独立的 owner、生命周期或验证边界；不做 one-module-per-concern。

### P3 — Shallow seam

wrapper 透传，调用者在外部拼装 config/state/runtime/order，测试重复内部编排。

通过条件：选择 Rule 3；使用 deletion test；形成完整 capability seam；减少 caller knowledge；删除或深化浅层，而不是新增 wrapper。

### N1 — Negative case

owner 清楚、变化局部的普通 bug 或机械修改。

通过条件：返回 `Status: No architecture change`；只输出证据、局部原因与修改边界；不得出现 target seam、Design Delta、provider、registry、manager 或广泛清理。

Scenario smoke 是合同审计，不等于 clean-session behavioral eval。

## 3. Paired behavioral eval

对同一个任务和 repo snapshot 运行：

```text
A. 同模型，不加载 architecture-evolution
B. 同模型、工具和预算，加载 architecture-evolution
```

冻结：任务文本、repo commit、可见文档、模型版本、工具权限、token/time budget。两臂不得共享输出。

每项 `0–2` 分：

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Evidence grounding | 主要是审美判断 | 有部分证据 | Observed / Inferred / Unknown 清楚分离 |
| Primary diagnosis | 漏掉或罗列 smell | 找到症状 | 找到一个 root owner/seam 错误并检查反例 |
| Design quality | 模式名或空泛目标 | 部分可用 | owner、variation、dependency、seam 明确 |
| Scope control | 扩成全面重构 | 大体局部 | 一个目标、一个主问题、明确不做什么 |
| Abstraction restraint | 新增壳层 | 有混合表现 | 拒绝假 seam，并说明替代/删除 |
| Improvement proof | 只说更解耦 | 有 before/after | locality、owner、dependency、knowledge、replacement 可观察 |
| Negative judgment | 强行架构化 | 犹豫 | 稳定返回最小 `No architecture change` |

## V0 pass gate

全部满足才通过：

1. P1–P3 至少两个案例中，B 臂的 `Primary diagnosis + Design quality + Improvement proof` 比 A 臂高至少 2 分；
2. 所有正样本只选择一个 primary violation；
3. B 臂在 Scope control 和 Abstraction restraint 上不低于 A 臂；
4. N1 稳定返回最小 `No architecture change`；
5. 每个 `Design ready` 都有具体 replacement/delete；
6. 未执行实现证据时，不声称行为保持或迁移完成。

## Failure taxonomy

- `signal miss`
- `root-cause miss`
- `pattern reflex`
- `scope expansion`
- `false abstraction`
- `difference collapse`
- `false positive`
- `unverifiable gain`
- `status leakage`

同一种 failure 在两个代表性案例中重复出现后，才修改 Rule；不要为单个样本继续扩充 Skill。

## Claim boundary

Static/scenario smoke 只能证明合同和文本机制一致；paired eval 只能证明冻结样本上的设计质量差异。实现正确性、行为对等、迁移完成、实际删除和生产维护成本都需要另行验证。
