---
name: verify
description: "Verify engineering results against authoritative completion or safety claims: derive proof obligations, choose and drive the closest real-artifact verification backend, collect Evidence, and judge proven / false / unproven without owning implementation or the backend runtime."
---

# Verify · 验证开发结果符合预期

Verify 负责回答一个独立问题：**当前 engineering claim 是否真的成立，我们拿什么真实 Evidence 证明。**

它不拥有 Intent，不定义长期 Architecture，不实现产品代码，也不拥有 test/build/replay/runtime harness。Northstar 定义 accepted outcome / Acceptance；Architecture Evolution 定义 adopted structural Target / completion semantics；Verify 把这些 authoritative claims 转成 proof obligation，选择最直接的 observation surface 与可用 verifier/backend，驱动或消费结果后判断 `proven / false / unproven`。

在 DaVinci 中，Replay 是可执行的 verification system/backend，而不是这个 Skill 的 semantic owner。Verify 可以调用或消费 Replay，就像使用 build、test、runtime probe、data readback、profile 或其他已有 harness 一样。

核心规则：

> **先固定 claim，再验证 real artifact。Verify 负责验证；Evidence 是证明产物；Replay/test/build/runtime 是可选 backend。**

## 什么时候调用

Verify 不是固定的 post-PR stage。它可以在实现前、实现中或实现后按需调用：

- **实现前**：Acceptance 已明确，但 proof route / baseline / oracle / blast-radius check 需要先收敛，输出 proof obligation 与 backend requirement；尚无 realized change 时不制造 PASS；
- **实现中**：新的 material risk / source identity / verifier limitation 会改变“如何证明”时，只更新受影响 proof surface；
- **实现后**：对 realized change 取得 Evidence 并判断 `proven / false / unproven`。

适合：

- 需要验证一个 feature / bug fix / migration / refactor 是否真的满足 Acceptance；
- behavior-preserving change 需要 baseline / candidate / oracle 对齐；
- replacement / rollout 声称旧 path / authority / writer 已退出；
- performance change 需要 before/after measurement；
- small diff 看起来 green，但存在 material blast-radius / false-pass 风险；
- Architecture Evolution 已采用 structural Target，需要验证 owner / dependency / authority exit 已真实落地；
- Human 明确要求“verify it”“证明它符合预期”“给 Evidence”“独立验收”。

trivial/local change 若一个已有 authoritative focused test 已直接覆盖 claim，Verify 可以直接接受/运行该 proof，不为了流程完整强制 Replay 或额外 verification ceremony。

## Claim first

先读取 authoritative contract，只恢复当前 verification 需要的 claim：

- Northstar 的 Acceptance / binding Constraint / Decision；
- 已存在的 Issue/spec/accepted request 中明确的 completion claim；
- AE 已采用的 structural outcome；
- performance / compatibility / safety 等已有明确 target。

不要从 diff、测试名、Replay 配置、Executor report 或现有命令反推“应该证明什么”。若 completion criteria 本身缺失、冲突或需要 Human commitment，返回 `$northstar`；若 structural Target 本身未决定，返回 `$architecture-evolution`。

### Concrete observable shape 不清时调用 Prototype

如果 authoritative claim 已经明确，但同一个 claim 在真实 user path / API usage / interface interaction / core path 上仍允许 materially different concrete interpretations，导致 Verify 无法稳定“应该观察什么”，可以 model-invoke `$prototype` 把这些 concrete shapes 变成可观察对比。

Prototype 只澄清 observable surface；**Verify 仍然拥有 proof obligation 与 verdict**。如果 ambiguity 实际改变 accepted outcome / commitment，返回 Northstar；如果它改变长期 structural Target，返回 AE；如果只是 backend mechanics，不调用 Prototype。

## 把 claim 变成 proof obligation

对每个 material claim 明确：

1. **Observable world**：如果 claim 成立，真实系统中必须能直接观察到什么；
2. **Falsifier**：哪个便宜而 material 的观察可以直接推翻它；
3. **Scope / identity**：哪个 build、artifact、config、input、runtime、consumer path 或 baseline 才是当前 claim 的真实对象；
4. **Evidence strength**：最低什么直接性 / authority / provenance / freshness 足够；
5. **Backend**：现有哪个执行系统最适合取得该 Evidence。

不要把 implementation step、task completion 或“命令成功”本身当 proof obligation。

## 优先验证真实 artifact

优先证明真实东西，而不是 proxy：

- CLI / service change → 跑真实 command / request，观察 output 与 side effect；
- UI / workflow → drive changed user path，观察 resulting state；
- parser / migration / behavior-preserving refactor → pin baseline，并对同一 input 做 equivalence / replay；
- storage / data change → read back authoritative written state；
- performance → 对齐 workload / config，比较 before/after profile 或 metric；
- structural claim → 直接检查 realized owner、dependency、consumer penetration、legacy authority/residue；
- safety/blast-radius claim → 找到真正 load-bearing 的一两个 safety fact，并尽量运行真实代码证明，而不是列一长串假设风险。

`build green`、文件存在、agent self-report、branch 名叫 `clean/golden`、cached artifact、测试数量都只能是 candidate Evidence，不能自动成为 proof。

## Backend 是执行能力，不是 owner

Verify 优先复用项目已有 verification system：

- DaVinci harness Replay；
- repo 的 tests / build / integration / equivalence harness；
- project-local `verify-<app>` / control harness；
- runtime probe、data query、profile、trace 或其他 direct observation。

backend 的职责是**执行并返回 observation/artifact**。Verify 决定为什么运行它、输入身份是否正确、结果证明哪个 claim，以及 proof 是否充分。

若 backend 已经定义自己的 Launch / Doctor / Drive / Capture / Cleanup contract，Verify 直接遵循它，不复制或重写 backend lifecycle。backend readiness / version / identity 是 proof validity 的一部分；backend 内部实现不是 Verify 的第二套 workflow。

一个 backend 可以证明多个 claim；一个 claim 也可能需要多个 Evidence source。不要把 `one task → one test` 或 `one claim → one replay` 固化成流程。

## Baseline / oracle discipline

behavior-preserving、migration、compatibility、perf 等比较型 claim 必须先确认 baseline / oracle identity：

- baseline 是否真的代表 intended behavior，而不只是某个分支名；
- candidate / baseline 是否使用同一 input / config / environment；
- replay artifact / runtime result 的 producer、version、freshness 是否可追溯；
- baseline 自己 red 时，不能把 candidate 同样 red 归因为当前 change；
- golden / release 只有在 authority 明确时才是 oracle。

如果这些事实未知，交 `$unknowns-first` 关闭 factual gap；Verify 不用猜测的 baseline 判卷。

## Verdict

对当前 scope 内的 material claims 只给三种状态：

- **proven**：direct current Evidence 已达到 claim 所需门槛；
- **false**：authoritative current reality 与 claim 冲突；
- **unproven**：Evidence 不足、backend 不可用、identity 不可信，或关键 fact 仍未关闭。

`unproven` 不是 implementation defect；“没发现反例”也不是 proven。无法执行需要的 backend 时，明确报告 `unproven` 与恢复条件。只有 proof obligation 已经有 realized artifact / observation 可判断时才给 `proven` / `false`；纯 pre-execution proof design 默认仍是 `unproven` / not-yet-run。

## Independence scales with risk

普通 local check 可以由 Executor 自己执行并提供 Evidence。以下情况更需要 fresh / independent verification：

- merge/ship 依赖该 claim；
- behavior-preserving migration / replacement；
- cross-boundary outcome；
- false-pass 成本高；
- author 与 judge 使用同一叙事容易形成 observer/self-report bias。

独立 verifier/judge 不重新定义 contract，只独立取得和判断 Evidence。

## 失败路由

Verify 先给 verdict，再按 premise 路由：

- implementation / realized behavior 不满足当前 valid claim → PR / Executor；
- factual source / baseline / runtime identity 不清 → `$unknowns-first`；
- verified reality 推翻 Intent Draft / Constraint / Acceptance → `$northstar`；
- verification 暴露此前未决的新长期 architecture fork → `$architecture-evolution`；
- 已理解 claim 的 concrete observable shape 再次出现 material ambiguity → `$prototype`，然后返回 Verify；
- 需要改变投入、兼容、长期维护或风险 commitment → Northstar / Human；
- backend 本身坏或不可运行 → 报 backend blocker，不把 product 判成 false。

## 输出与持久化

保持 minimum-sufficient：

- **Claim**：正在验证什么；
- **Proof obligation**：真实世界必须满足什么；
- **Evidence basis**：source/backend、identity、inputs/config、关键 observation；
- **Verdict**：proven / false / unproven；
- **Gap / falsifier**：若未证明，缺什么；
- **Next owner**：需要谁继续。

Verify result 默认留在当前 PR / review / verification surface。只有它证明 canonical Intent / Acceptance 本身失效，或形成后续 fresh consumer 必须知道的 durable correction，才 fold back 到 Northstar Issue；只有它暴露新的长期 structural fork 才回 AE。不要生成 repair plan、execution backlog、第二份 Intent 或第二份 verification SOT。

## 与 eval 的区别

Verify 验证**产品/工程 claim**。Skill/prompt/harness 语义变更本身是否改善 agent behavior，应该使用 blinded behavioral eval，而不是拿产品 Replay 代替。候选必须在 clean / sanitized session 中运行，judge 看真实产物与行为，而不是候选自报“我遵守了规则”。
