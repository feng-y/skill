# Full Factual Map Workflow

只在 `$unknowns-first` L3 被触发时读取：用户明确要完整 unknown map，或多个**事实未知**相互耦合到当前 work 无法继续。

这个 reference 只负责 map-versus-territory source alignment。它不是第二套 SDLC，不拥有 Intent、Prototype、Architecture、Execution plan、Proof plan 或 post-change review。

## Source model

- **Map**：prompt、plan、docs、memory、assumptions、historical explanation。
- **Territory**：current code、config、runtime、data、tests、authoritative external source、verifier artifacts。
- **Failure mode**：map 已经被 territory 反证，但后续判断仍沿旧 map 前进。
- **Control rule**：只调查答案会改变当前 route / scope / attribution / owner judgment 的 factual unknown。

## Map contract

对每个 material unknown 记录：

- **Question**：缺的事实是什么；
- **Why material**：不同答案会改变哪个当前判断；
- **Territory / source**：谁能回答；
- **Closer**：`territory`、`user-fact`、或 `OPEN`；
- **Evidence**：source identity、provenance、freshness 与最小 decisive excerpt / observation；
- **Status**：`closed` / `open`；
- **Next owner**：事实关闭后回哪个 semantic owner。

优先级按 blast radius 与 dependency 排，不按文档章节顺序。

## 四类扫描

### Known knowns

只列当前已有 authoritative Evidence 支持、且会约束后续判断的事实。历史解释或未核实 docs 不因为写得明确就进入 known knowns。

### Known unknowns

列当前已经知道缺失、且不同答案会改变 route / scope / attribution 的事实。能用一个 probe 关闭就直接关闭，不为了完整 map 延后。

### Unknown knowns

寻找已经存在但 caller 没带入 map 的 authoritative source：repo contract、runtime config、release identity、existing trace、data ownership、reference implementation、Replay/test artifact identity 等。只找会改变当前判断的 source。

### Unknown unknowns

只在 touched responsibility surface 上做 landmine sweep：隐藏 caller、legacy authority、alternate runtime path、stale config/data、source identity mismatch 等。每个 landmine 都必须有 Evidence 或明确 OPEN，不做泛化风险清单。

## Semantic routing

L3 可以发现非事实问题，但必须路由，而不是在 map 内解决：

- accepted outcome / Human commitment → `$northstar`；
- concrete path / usage / interface reaction → `$prototype`；
- long-term responsibility / boundary / dependency → `$architecture-evolution`；
- completion/safety claim 的 proof obligation、false-pass、sufficiency judgment → `$verify`。

不要在 full map 里生成 mock、candidate design、architecture program、build plan、proof plan、review checklist、quiz 或 repair plan。

## Handoff

最终只交付：

1. 已关闭的 material facts + Evidence；
2. 仍 OPEN 的 factual unknown + closer；
3. 哪些原 map premise 被纠正；
4. 每个非事实问题应返回的 semantic owner；
5. next action / owner。

当 factual map 足以让原 caller 继续，就立即返回 caller。只有真实 OPEN factual blocker 存在时才停在 Unknowns First；不要把“完成 full map”本身当成新的审批 gate。

## Fold-back

只持久化能避免未来重复 rediscovery 的 stable fact / source identity / discriminator。一次性日志、临时 line number、unversioned artifact 或当前 session inventory 默认不成为长期 SOT。
