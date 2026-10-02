# Human Projection for Repo Identity

Human projection 的目的不是“更漂亮”，而是让理解、审查和决策所需的信息以最低认知成本呈现。

Repo Identity 的 current evidence-backed model 是输入；projection 是一次性 view。

## Representation selector

### Concise text / table

适合：
- 一个 capability / owner；
- 少量 contract；
- 一个 improvement candidate；
- Human 只需要确认一个 material judgment。

### Diagram

适合：
- 多个 responsibility / authority 之间的关系；
- request/data/model/result flow；
- caller/owner boundary；
- current → target 结构差异（Target 必须已经由 AE / accepted design 提供）。

图里只保留会改变判断的 node / edge，并能回到 Evidence anchor。

### Dashboard

适合：
- migration/adoption/completion；
- 多条 contract 的 proven/unproven/unknown；
- identity drift；
- hotspot / change pressure 的对比。

Dashboard 的状态必须来自真实 source，不从文字结论反推数据。

### Timeline / evolution map

适合：
- 为什么某 responsibility 逐步迁移；
- 多个 PR/commit 是否在反复补同一个 mismatch；
- raw churn 与 semantic hotspot 的区别。

按 semantic change reason 聚合，不按 commit 数量制造趋势。

### Interactive artifact

适合：
- repo 大、responsibility 多；
- Human 需要在 owner / contract / evidence / history 之间来回探索；
- 静态图会塞入大量次要信息。

若宿主支持，可即时生成 disposable HTML：默认视图只展示 repo thesis + capability map；点击 node 再展开 contracts、evidence、evolution、current Intent impact。不要先建设长期前端。

### Explainer

只有当一个复杂因果链必须按顺序解释才能理解，并且 text/diagram/interactive view 仍不足时使用。它不是默认输出。

## Authority

任何 projection 都必须满足：

- 可以追到当前 evidence / source；
- 不新增只有 projection 才存在的 semantic truth；
- projection 与 repo reality 冲突时，以 repo authority 为准并修 projection；
- 删除 projection 不应丢失 canonical Intent、architecture contract 或 durable repo truth。
