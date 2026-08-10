# Architecture Intent Contract

只在 `Status: Architecture intent ready` 时读取和输出。本文件只定义最终 Intent 的物理形状；architecture judgment、ready/discriminator、Brooks challenge 和 evidence lifetime 由 `SKILL.md` / `rules.md` / `brooks-constraints.md` 拥有，不在这里复制第二套判定逻辑。

最终输出跟随用户当前主要语言。内部 taxonomy、Brooks 编号、challenge 过程或英文 reference 不要求出现在最终 artifact 中；代码符号、类型名、文件名和必须保持稳定的协议名称可以保留原文。

```markdown
# Architecture Intent

Status: Architecture intent ready

## Architecture problem
- Problem: <一句话说明真正的 structural / semantic / ownership / dependency 问题>
- Why architectural: <为什么局部 cleanup、helper 或单点修复不能消除主要 pressure>

## Background
- Why now: <当前变化压力，以及哪个历史前提、variation 或 boundary 假设已经失效>
- Decisive evidence: <只保留理解该判断所需的少量决定性 evidence；不要输出调查日志、完整 commit 清单或五面审计表>

## Direction
- Intent: <应该演化什么>
- Desired end state: <完成后业务、调用者、ownership 或依赖关系有什么不同>
- Possible target identities: <可选；仅当一个 intent 下确有 2–3 个值得后续设计比较的基本架构形态时出现。每个 identity 只写核心 ownership / semantic / dependency identity 和主要取舍，不进入具体设计>

## Boundary
- In scope:
- Out of scope:
- Must preserve:
- Replacement / exit: <至少一个必须退出的旧知识、路径、判断、责任或依赖>
```

只有真实存在会改变 intent、boundary 或 target identity 的 material unknown 时，才在 `Boundary` 前追加：

```markdown
## Material unknown
- Claim at risk:
- Minimal probe / Human decision:
- It changes: <会改变哪个 intent / boundary / target identity>
```

## Discipline

- 一个 intent；`Possible target identities` 是同一 intent 下的基本目标形态，不是并列多个改造项目；
- 输出重点是“真正的问题是什么 → 为什么形成 → 希望变成什么 → 哪些基本形态值得继续设计”；
- decisive evidence 只用于让判断 grounded，不输出完整 evidence inventory、变化历史流水账或 reasoning trace；
- 内部 architecture taxonomy 可以帮助选择和 challenge intent，但不输出 `Primary architecture direction` 标签；
- Brooks R1–R6、Risk/Guard/Proof 表和 counterexample challenge 都属于内部 reasoning machinery，不作为最终 section；如果它们改变了 intent，只把结果以普通架构语言沉淀到 Direction / Boundary / Must preserve / Replacement；
- 不输出 `Design obligations` 清单。只有会改变 intent 含义或防止明显错误物化的 identity-level guard 才进入 Boundary / Must preserve；具体“谁负责 projection / rehash / lifecycle helper”等问题属于后续目标设计；
- 不输出 success/verification plan、proof provider、scope derivation 或 implementation acceptance checklist；Real Evolution 只需通过 `Replacement / exit` 表明旧知识、路径、责任或依赖会真实退出；
- `Observed / Inferred / Unknown` 不混写；Material Unknown 只在确实会改变 intent 时出现，不填空占位；
- 描述 architecture identity，不提前指定 class、interface、API、factory、strategy、registry、adapter、对象组合、调用流程、迁移步骤、implementation slice、任务拆分或 verification plan；
- 当问题、背景、方向、边界和必要的 possible target identities 已足以让后续目标设计继续时停止。
