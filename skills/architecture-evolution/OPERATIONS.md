# Architecture Evolution 操作手册

本手册说明怎样在真实仓库任务中使用 Architecture Evolution（AE）。运行时行为仍以 [`SKILL.md`](SKILL.md) 为准；这里不定义第二套协议。

## 1. 调用前先确认任务类型

AE 适合回答“长期结构应该怎样、当前是否值得推进架构变化、哪一刀杠杆最高”。

如果问题只是 bug、机械清理、单次迁移、实现细节或测试工具选择，不要为了使用 AE 把它升级成架构问题。

最常见的合适入口有三种：

```text
历史模块持续积累责任，不清楚长期边界。
```

```text
同类需求反复跨多个 owner / authority / verification surface。
```

```text
已经有多个可行架构方向，需要判断哪个现在更值得投资。
```

## 2. 准备输入

不需要先写完整架构方案。给 AE 足够的现实入口即可。

推荐输入四部分：

```text
Area: 当前要判断的模块、能力或边界
Pressure: 真实工程摩擦、重复变化或已经明确的未来要求
Known constraints: 已绑定的业务、兼容、性能、部署或风险约束
Question: 希望 AE 最终判断什么
```

示例：

```text
使用 $architecture-evolution 评估 model_curator。

Area:
model_curator 及其直接 consumer。

Pressure:
新增模型类型时，多个 consumer 都要读取并重组 model_curator 的私有配置和生命周期信息；验证也分散在多处。

Known constraints:
现有外部模型身份必须保持兼容；本轮不改变部署拓扑。

Question:
判断长期责任和依赖应该怎样，当前最值得推进的架构改进是什么。
```

不推荐这样输入：

```text
把 model_curator 重构成 provider + registry。
```

因为这已经把候选手段当成答案，会压缩 AE 的判断空间。

## 3. 让 AE 先看现实

正常情况下，AE 应从指定 area 及直接上下游开始，优先查会改变判断的事实：

- 当前责任和公开边界；
- 谁拥有权威事实和生命周期；
- 实际依赖方向；
- caller 是否在重组 capability 私有知识；
- 同类变化如何传播；
- 主要行为在哪里验证；
- 现有架构文档、领域文档和 ADR 分别证明什么。

不要要求它先全仓扫描。只有关键未知会改变“局部还是架构”、目标结构、方向选择或旧结构退出时，才继续扩大调查。

## 4. 读懂 AE 的四类结果

### 4.1 局部问题

典型结论：

```text
当前责任、依赖和权威边界没有长期失真；问题来自局部实现或一次迁移。
```

这时不要要求 AE 为了“有产出”继续造 Target Architecture 或 Program。直接回到局部实现。

### 4.2 关键事实或人的决定未决

只有真正会改变目标结构的问题才应阻塞，例如：

- 某外部身份是否必须长期兼容；
- 两个 subsystem 是否具有独立生命周期；
- 某业务语义是否必须保持独立权威；
- 已批准 roadmap 是否真的会长期引入某类 variation。

只影响具体 class、file、schema、测试工具的问题，不应该阻塞 AE。

### 4.3 只有战略设计结论

这是正常结果。

如果长期结构已经可以澄清，但当前没有足够真实压力、退出价值或投资收益，AE 可以只给出目标结构，不制造 repo change。

### 4.4 架构演进方案

真正值得推进时，结果应说明：

- 当前结构问题来自什么长期责任、依赖、抽象或权威张力；
- 长期目标结构是什么；
- 为什么当前选择的改进比其他 gap 更值得现在推进；
- 哪些旧知识、权威、依赖、特殊路径或补偿性说明会退出；
- 完成后什么结构事实可以证明演进成立。

改进项最多 3 个，不需要补数。

## 5. 怎样判断一个改进项是否真的有价值

一个高价值改进不只是“更干净”。至少要同时看到三类结果：

### 结构收益

责任、依赖、抽象或局部性真实改善。

### 传播压缩

对一类持续或已经明确的未来变化，减少必须跨越的：

- responsibility；
- authority；
- dependency；
- verification surface。

### 真实退出

对应的旧知识、旧权威、反向依赖、特殊路径、兼容路径或补偿性 guidance 不再继续 authoritative。

如果只是：

```text
old A → new facade → old B
```

而旧结构仍然决定运行和理解方式，这只是复杂度搬运，不是有效演进。

## 6. 比较多个方案

当 A、B 都符合目标结构时，不要按以下标准优先：

- patch 更大；
- abstraction 更多；
- 文件更少；
- 目录更漂亮；
- 当前迁移更容易。

优先比较：

```text
哪一个让后续同类变化少跨 owner / authority / dependency / verification？
```

但 locality 不能伪造。以下方案应被拒绝：

- 把已有独立生命周期的 subsystem 吞进一个 owner；
- 复制权威事实到本地以减少依赖；
- 用 facade 隐藏实际仍需要理解的跨边界语义；
- 为了 agent 或测试方便改变主要业务责任。

## 7. 与 Human 决策的边界

AE 可以查事实，也可以形成候选战略设计，但不能替用户承诺：

- 业务语义；
- 外部兼容；
- 风险接受；
- 产品承诺；
- 需要人的长期投资取舍。

如果 AE 由 Northstar 等上游 shaping 能力调用，它应返回证据、候选方向和人的决策面，不再自己建立一套串行 Ask 流程。

## 8. 从 AE 交给实现者

AE 的输出应停在架构结果和结构完成条件。

实现者继续决定：

- class / API；
- file / package；
- schema；
- migration sequence；
- PR 拆分；
- 测试框架和具体命令。

如果实现阶段发现新的 material evidence，会推翻责任、权威、依赖或退出判断，应重新进入 AE；如果只是实现细节变化，不需要重跑战略设计。

## 9. Human 修正后的重入

用户如果只修正文案或实现偏好，不需要重算全部架构判断。

如果用户提供的新事实会改变：

- architecture vs local；
- responsibility / authority；
- dependency；
- general vs specific；
- legacy 是否能退出；
- 当前最高杠杆方向；

则从受影响的最高层重新判断，并完整重交付当前结论，不把旧方案继续拼在后面。

## 10. 常用调用模板

### 历史模块

```text
使用 $architecture-evolution 评估 <module>。
从当前代码、直接上下游、已有架构/领域文档和近期真实工程摩擦恢复这一范围的长期责任、权威、依赖和通用/特化关系。
判断当前问题是局部实现、实现偏离、已有意图过时，还是值得推进的架构演进。
若有多个合理方向，只保留当前最高杠杆且能让旧结构真实退出的改进，不预定实现。
```

### 下一刀改什么

```text
使用 $architecture-evolution 判断 <area> 下一步最值得推进的架构改进。
不要从目录整洁或 pattern 出发。先恢复长期目标结构，再比较当前 gap 的真实压力、结构收益、变化传播、退出价值、迁移成本和风险。
没有值得立即改 repo 的内容时，直接给战略设计结论。
```

### 评估现有方案

```text
使用 $architecture-evolution 独立评估下面的架构方向，不替方案辩护：
<proposal>

先依据 repo reality 判断长期责任和依赖是否成立，再判断该方案是真演进还是复杂度搬运；如果存在更高杠杆方向，给出架构级替代，不进入实现设计。
```

### 老路径是否应该退出

```text
使用 $architecture-evolution 评估 <legacy path / identity> 是否仍属于长期架构。
不要因为 repo 内搜索不到 reader 就判定可删；只调查会改变目标结构和退出判断的解析、存储、发布、部署或外部身份事实。
```

## 11. 常见误用

### 把 smell 当结论

错误：

```text
文件太大，所以拆模块。
```

正确：

```text
先判断是否存在长期责任、依赖、抽象或权威失真。
```

### 把目标结构当待办清单

错误：

```text
战略设计发现 5 个 gap，所以全部进入 roadmap。
```

正确：

```text
只有当前真实压力和结构收益足以覆盖迁移成本与风险的 gap 才进入当前演进。
```

### 为 AI-native 单独造架构

错误：

```text
为了 agent 少读 context，把几个真实独立 owner 合并。
```

正确：

```text
先让业务责任和权威边界正确；更局部的 context、修改和验证是好架构的结果。
```

### 在 AE 中提前设计实现

错误：

```text
固定 class、interface、filename、PR sequence。
```

正确：

```text
只固定架构结果和结构完成条件，把 representation 交给实现阶段。
```

## 12. 显式 smoke / eval

正常使用不要读取 [`references/validation.md`](references/validation.md)。

只有在验证 AE 本身行为时，才做显式 smoke/eval。正式声明“加载 AE 比裸模型更好”前，应使用同一 model、repo snapshot、tool permission 和 budget 做 clean-session paired comparison。

日常真实任务中，更重要的是记录失败类型：

- 把 local 问题错误升级为 architecture；
- 目标结构被当前代码或旧文档绑架；
- 选择了漂亮但低杠杆的改造；
- 新 abstraction 没有让旧结构退出；
- 为局部性吞并真实独立 responsibility；
- 提前下沉到 implementation design。

只有真实失败显示现有语义无法解释，并且多个 case 指向同一个稳定 discriminator 时，才值得继续演进 Skill。
