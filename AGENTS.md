# Skill Repo Evolution Discipline

本文件约束如何修改这个 skill repo 本身，不是任何单个 Skill 的 runtime 语义。

总原则：**优先语义压缩，不做规则堆积。** 只有 Evidence 证明存在独立且稳定的责任，并且存在独立 invocation reason，才新增持久 Skill surface。

## Canonical capability map

- `northstar`：conversation / request / incident → canonical engineering Intent；需要 durable handoff 时 materialize 为 Drafted Issue。
- `beacon`：caller-neutral、主要由 model 按需调用的 local intent-concretization specialist。只处理 already-understood semantic question 中一个 bounded/local part 的 concrete reaction / inspection surface。Core Path、Usage / Interface Draft、behavior example、config/schema shape、UI draft、minimal implementation、experiment、disposable prototype 都只是可选手段。
- `architecture-evolution`：长期 Target Architecture judgment + Current → Target Evolution Program。
- `verify`：从 authoritative claim 推导 proof obligation，选择 real-artifact backend，收集 Evidence 并判断 proven / false / unproven。
- `unknowns-first`：只关闭 map-versus-territory 的事实未知。

不要复制 owner：Northstar 不判 proof sufficiency；Verify 不重写 Intent 或设计 Target；Beacon 不接管 caller 的 semantic ownership；AE 不用 Program convenience 反推 Intent；Unknowns First 不把 factual probe 扩成其他 semantic judgment。

### Beacon routing

Northstar、AE、Verify、Unknowns First 或其他 semantic caller 都可以在“当前语义已理解，但其中一个 bounded/local concrete path / usage / interface / interaction / artifact 仍存在 material ambiguity”时 model-invoke `$beacon`。

Beacon 只返回 concrete contrast / correction / Evidence 给原 caller；原 caller继续做自己的 judgment。Northstar 负责多个局部 Beacon artifact 的组合与最终 Intent 编译。

`prototype` **不再是顶层 Skill identity，也不存在 `$prototype` runtime 路由**。prototype / mock / minimal implementation 只是 Beacon 可选的 implementation technique。

## Structure and complexity

- Existing semantics first：能由现有 owner 解决就不新增 layer / phase / state / role / protocol / taxonomy。
- Evidence before materialization：一次 observation / case 默认只是 Evidence，不自动升级为稳定结构。
- New structure must remove something：新增 abstraction 必须让重复知识、分支、责任泄漏或旧路径真实退出。
- Runtime and eval stay separate：runtime 只保留 stable invariant / authority / boundary；case / incident / counterexample 留在 `evals/`。

## Artifacts

- Drafted Issue：Northstar Intent 的 durable carrier。
- PR：realized change；implementation How、diff、implementation-local validation 与 review 默认留在 PR。
- Beacon artifact：bounded reaction / inspection surface，通常可丢弃；durable correction / Evidence 返回原 caller。
- Architecture handoff：只有独立调用或真实跨边界需要时持久化。
- Verify result：Claim + proof obligation + Evidence basis + proven/false/unproven verdict + owner routing。

## Verifier / control-plane boundary

Verify 是 capability，不是 lifecycle stage。test/build/integration、project-local verify harness、runtime probe、data query、profile、DaVinci Replay 等是 backend，不是 semantic owner。

Execution control plane 与 semantic ownership 正交；可以 start / route / pause / resume / retry，但不能定义 Intent、Architecture、Verify semantics 或 artifact authority。

## Graph and feedback loop

Clear Drafted Issue 可以直接执行；只有复杂 material dependency 会迫使 fresh Executor 重新做高层判断时，Northstar 才按需 compile coarse material graph。

Research、execution、review、Verify 产生的新 Evidence 只重开真正受影响的 owner：

- factual gap → Unknowns First；
- Intent premise / Constraint / Acceptance 被推翻 → Northstar；
- bounded/local concrete ambiguity → Beacon，结果返回当前 caller；
- 长期 responsibility / boundary / dependency fork → Architecture Evolution；
- completion / safety claim 的 proof judgment → Verify。

不要因为一个 red signal 全量重跑所有 Skill。

## Context discipline

优先 territory：`current code / test / config / runtime Evidence > stable repo contract > authoritative current docs > historical explanation > case narrative`。

只加载会改变当前 judgment 的 context；编码 discriminator / invariant，不编码一次 case 的答案。

## Breaking migrations

删除、重命名、合并顶层 Skill 或迁移稳定 responsibility 时，同一 change 必须更新 `CHANGELOG.md`。Changelog 是历史 ledger，不是 runtime contract。

## Placement

- Repo-wide evolution / context rules：`AGENTS.md`
- Skill runtime invariant：对应 `SKILL.md` 或 runtime reference
- Breaking semantic migration：`CHANGELOG.md`
- Case / incident / counterexample：`evals/`
- `CLAUDE.md`：薄入口，不复制规则
