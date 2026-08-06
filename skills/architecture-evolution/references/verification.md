# Verify One Architecture Design

只在 `Status: Design ready` 前读取。本文件使用 Brooks-Lint 的架构审计标准验证目标设计，不再定义另一套改进维度。

它验证设计假设，不验证实现正确性；未完成全仓库扫描时，不生成 Health Score。

## Verification standard

检查 Brooks 六类 production-code decay risks：

- `R1 Cognitive Overload`
- `R2 Change Propagation`
- `R3 Knowledge Duplication`
- `R4 Accidental Complexity`
- `R5 Dependency Disorder`
- `R6 Domain Model Distortion`

遵守 Iron Law：

```text
先完成风险诊断，再接受 Remedy。
每个 finding 必须形成：
Severity → Symptom → Source → Consequence → Remedy → How to verify
```

其中：

- `Symptom` 必须来自当前代码或目标设计的具体结构；
- `Source` 写 Brooks risk code，并引用对应经典原则或 smell；
- `Consequence` 写真实变化、维护、测试或业务理解成本；
- `Remedy` 必须已经体现在目标设计中，不能是额外建议清单；
- threshold、文件大小、fan-out、switch 和 wrapper 只属于 signal，不是 verdict；
- 检查合理 tradeoff 和 false-positive guard，不能为了消除 finding 破坏真实业务差异。

## Audit order

按架构影响顺序扫描同一个 Target 的 current 与 target：

1. `R5 Dependency Disorder`
2. `R6 Domain Model Distortion`
3. `R2 Change Propagation`
4. `R3 Knowledge Duplication`
5. `R4 Accidental Complexity`
6. `R1 Cognitive Overload`

所有六类都必须检查。无 finding 时写 `No finding` 和最关键 guard，不要省略该风险。

## Risk questions

### R5 Dependency Disorder

源码依赖是否遵循 `policy → contract ← implementation`？是否仍有循环、common→scenario、policy→provider，或 callback/global state/registry 的隐式反向控制？

合理例外：composition root 可以知道具体实现；adapter 可以连接 contract 与外部系统。

### R6 Domain Model Distortion

canonical capability、模块名称和 invariant 是否表达真实业务？是否把不同 bounded context 错误合并，或把数据库、provider、历史类结构当成业务模型？

合理例外：简单 CRUD 可以使用 transaction script；DTO 和边界 record 可以只承载数据。

### R2 Change Propagation

修改共同业务规则、增加一个 variation 或替换实现时，是否仍要求无关模块、调用者和测试同步修改？

合理例外：同一 bounded context 内的必要协调修改，不自动构成 propagation。

### R3 Knowledge Duplication

同一业务决定、配置解释、capability 判断或 variation 选择是否仍在多个位置表达？

合理例外：不同 bounded context 的相似规则，或明确边界上的协议常量，不自动属于重复知识。

### R4 Accidental Complexity

目标设计是否新增 facade、manager、registry、base、mode flag 或 optional contract，却没有替代旧结构？是否存在 speculative seam、middle man 或复杂度搬家？

合理例外：真实吸收 vendor churn 的薄 adapter，以及已有替换需求证明的 seam，可以保留。

### R1 Cognitive Overload

目标模块和调用者是否更容易说明、使用和验证？公开 contract 是否减少调用顺序、状态、实现类型和隐含配置知识？

合理例外：被深模块隐藏的内部复杂度不是问题；清晰的线性实现不因行数较多自动构成 overload。

## Output

```markdown
## Brooks verification

| Risk | Severity | Symptom | Source | Consequence | Remedy in target design | How to verify | Residual / tradeoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R5 Dependency Disorder | | | | | | | |
| R6 Domain Model Distortion | | | | | | | |
| R2 Change Propagation | | | | | | | |
| R3 Knowledge Duplication | | | | | | | |
| R4 Accidental Complexity | | | | | | | |
| R1 Cognitive Overload | | | | | | | |

Verdict: PASS / RETRY
```

`Severity` 使用 `Critical / Warning / Suggestion / No finding`。

## Verdict

`PASS` 必须同时满足：

1. 六类风险已完整扫描，并应用 false-positive guard；
2. 主要架构断点对应的 Brooks 风险有具体 Remedy 和可执行验证；
3. 目标设计没有引入新的 Critical finding；
4. 新增或残留的 Warning 有明确业务 tradeoff、owner 和验证边界；
5. `Real Evolution` Gate 已通过，至少一个旧路径、重复知识、无效抽象或反向依赖退出；
6. 真实业务差异和 `Protected behavior` 被保留；
7. 未执行实现证据时，不声称行为保持、迁移完成或 finding 已经消失。

不满足时修改设计并返回 `RETRY`；若缺失的是代码或运行事实，返回 `Research required`；若属于 Human-owned 业务或兼容承诺，返回 `Decision required`。
