# Verify One Architecture Design

只在 `Status: Design ready` 前读取。使用 Brooks-Lint 的架构标准验证目标设计，不再定义另一套改进维度。

验证的是设计假设，不是实现结果；未完成全仓库扫描时，不生成 Health Score。

## Standard

扫描 Brooks 六类 production-code decay risks：`R1–R6`。

遵守 Iron Law：

```text
先诊断，再接受 Remedy。
每个 finding：Severity → Symptom → Source → Consequence → Remedy → How to verify
```

- `Symptom` 来自当前代码或目标设计；
- `Source` 写 risk code，并引用对应经典原则或 smell；
- `Consequence` 写真实变化、维护、测试或业务理解成本；
- `Remedy` 必须已经进入目标设计，不能是额外建议；
- signal/threshold 不是 verdict；必须应用 tradeoff 与 false-positive guard。

## Risk scan

按 `R5 → R6 → R2 → R3 → R4 → R1` 检查 current 与 target。六类都要输出；无 finding 时写 `No finding` 和关键 guard。

| Risk | Diagnostic question | Source cues | Key guard |
| --- | --- | --- | --- |
| `R5 Dependency Disorder` | 是否存在循环、`common→scenario`、`policy→provider`，或底层反向控制 policy？ | Clean Architecture: DIP/ADP/SDP；Brooks: Conceptual Integrity | composition root 可知道具体实现；adapter 可连接 contract 与外部系统 |
| `R6 Domain Model Distortion` | capability、名称与 invariant 是否表达真实业务？是否错误合并 bounded context？ | DDD: Ubiquitous Language/Bounded Context；Fowler: Feature Envy/Data Class | 简单 CRUD、DTO 和边界 record 可以保持简单 |
| `R2 Change Propagation` | 改共同规则、增加 variation 或替换实现时，是否仍需无关位置同步修改？ | Fowler: Shotgun Surgery/Divergent Change；Pragmatic: Orthogonality；Hyrum's Law | 同一 bounded context 内的必要协调修改不自动构成 propagation |
| `R3 Knowledge Duplication` | 同一业务决定、配置解释或 variation 选择是否仍在多处表达？ | Pragmatic: DRY；Fowler: Duplicate Code；DDD: Ubiquitous Language | 不同 bounded context 的相似规则不自动属于重复知识 |
| `R4 Accidental Complexity` | 是否新增 facade/manager/registry/base/mode flag，却未替代旧结构？ | Fowler: Speculative Generality/Middle Man；Brooks: Second-System Effect；Ousterhout: Deep Modules | 真实吸收 vendor churn 的 adapter 和已被证明需要的 seam 可以保留 |
| `R1 Cognitive Overload` | module 与 caller 是否少知道步骤、状态、顺序、实现类型和隐含配置？ | Code Complete；Fowler；DDD；Ousterhout: Shallow Module | 深模块内部复杂度、清晰线性实现不因规模自动成为 finding |

## Output

```markdown
## Brooks verification

| Risk | Severity | Symptom | Source | Consequence | Remedy in target design | How to verify | Residual / tradeoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5 | | | | | | | |
| R6 | | | | | | | |
| R2 | | | | | | | |
| R3 | | | | | | | |
| R4 | | | | | | | |
| R1 | | | | | | | |

Brooks verdict: PASS / RETRY
```

`Severity`：`Critical / Warning / Suggestion / No finding`。

## Verdict

`PASS` 必须满足：

1. R1–R6 全部扫描并应用 guard；
2. 主要架构断点的 finding 有完整 Iron Law 链路和可执行验证；
3. 目标设计不引入新的 Critical；
4. 残留 Warning 有明确 tradeoff、owner 与验证边界；
5. `Real Evolution` 已让至少一个旧路径、重复知识、无效抽象或反向依赖退出；
6. 真实业务差异与 `Protected behavior` 被保留；
7. 未执行实现证据时，不声称 finding 已消失。

否则修改设计并返回 `RETRY`；缺代码/运行事实时返回 `Research required`；属于 Human-owned 业务或兼容承诺时返回 `Decision required`。
