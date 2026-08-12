# 当 Goal 还没有定准

只在主 Skill 已经开始 Ground / Shape，但仍无法形成 Stable Goal 时读取。这里不重新定义 Unknown routing；只处理两个容易让 Goal 写错的判断。

## Semantic altitude

一句话应该留在 Goal，还是留给 Executor，先做这个测试：

> **换一种 materially different 的实现仍满足它，Human 会接受吗？**

会 → 它通常是 How / intelligence，不应被 Northstar 固定。

不会 → 它描述的是 Human 真正在乎的结果、边界、风险承诺或验收要求，应留在 Goal。

当前实现、已有 class/provider、某个计划写得很具体，都不能自动把 How 抬成 Goal。反过来，Human 明确要求某种 representation / compatibility / provider，因为它本身就是业务或技术承诺时，这个 representation 可以成为 Goal 的一部分。

## Map is not territory

Prompt、已有 plan 和 Northstar 自己都只是 map；repo、runtime、历史约束和真实使用者可能暴露 map 没写出来、但会改变 Goal 的事实。

只沿这种差异追 reality：已有 authoritative spec / precedent、真实 consumer、repo 外 contract、serialized/config identity、部署/授权约束、当前 workspace 与 Human Goal 的真实关系。它们是按需 lens，不是 checklist。

找到候选后只问：**如果它取另一个值，Stable Goal 会不会不同？** 不会就停止展开。

## Decision priority

如果 Human 同时给出的要求会发生真实冲突，Stable Goal 必须让 Executor 知道冲突时什么优先。priority 只能来自 Human、已有 authority 或不可替代的现实约束；Northstar 不能因为某个实现更方便而偷偷重排。

reality 能排掉冲突就直接收敛；否则把仍需要 Human 拍板的冲突一次问清，并说明选择的主要后果与推荐。

## Stop shaping

当剩余问题只会改变 How，而不会再改变 Human 会接受的 Goal，就停止 Intent Research，回主流程 Compile。Implementation 中继续出现新 Unknown 是正常的；Northstar 不需要在执行前把它们消灭。
