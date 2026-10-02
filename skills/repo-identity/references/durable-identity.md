# Durable Repo Identity

只在同一 repository 的 identity 会被反复消费，或 Human 明确要求“构建 / 维护 repo identity”时使用。一次性理解或单次 improvement analysis 不需要持久化。

## Placement

优先复用目标 repo 已有 authoritative surface：

1. 项目级 `AGENTS.md` 指定的 architecture/domain/design 文档；
2. 已有 architecture / ownership / contract index；
3. 如果没有合适 surface，才创建一个项目内可寻址的 derived identity 文档，例如 `.repo-identity/identity.md`。

不要为了 Repo Identity 把原有 contract 再复制一遍。Identity 文档应主要做**索引、映射、关系与 evidence anchoring**。

## Minimal durable shape

推荐保持一个文件即可：

```text
Repository thesis
  owns / does-not-own

Capability & responsibility map
  capability → owner / authority → evidence

Boundary & contract map
  producer/consumer → stable contract → evidence

Key flows
  only material identity-bearing paths

Evolution pressure
  repeated change reason → affected identities → evidence

Identity drift / open unknowns
  claim → supported / contradicted / unknown

Validation baseline
  current branch/ref/commit + authoritative sources
```

这不是固定 schema。项目已有更自然的表达时复用它。

## Evidence discipline

Durable claim 不写“模型认为”“历史上大概”“通常如此”。至少绑定一个 authoritative anchor：

- code symbol / stable path；
- test / fixture；
- config / schema / generated contract；
- project rule / design contract；
- current authoritative docs；
- commit / PR 只用于解释演化来源或已被 current reality 保留的 contract。

记录 source identity，而不是复制大段 source 内容。

## Refresh

不要定期全量重建。更新 target repo 后：

1. 看 changed paths / symbols / contracts 是否命中已有 evidence anchors；
2. 只重验 affected identity cone；
3. 若 source 只是 implementation refactor 且 stable responsibility/contract 未变，保持 identity；
4. 若 authority、boundary、contract 或 thesis 变了，更新 claim + downstream projections；
5. 无法确认时标 `unknown/stale`，不要沿用旧 claim。

## Anti-corruption

以下情况说明 durable identity 正在腐化：

- 一个 claim 已没有 current Evidence，但仍写成事实；
- current code/test 与 identity 冲突，却靠历史文档解释继续保留；
- implementation detail 被写成长期 responsibility；
- 每次任务都往 identity 加一次性 path / log / case；
- diagram/HTML 成为唯一可查的 repo truth；
- 同一 responsibility 在 Identity、architecture doc、Taskbook 各自维护完整副本。

修正方式是**回到 authority + evidence**，删掉过时 duplication，而不是给 identity 再加版本层、confidence taxonomy 或同步 protocol。
