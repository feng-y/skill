# 当 Goal 还没有定准

只在普通的输入理解与 reality 检查仍无法确定 Human 最终会接受哪个 Goal 时读取。

## 这是 Goal，还是 How

先做一个测试：

> **换一种 materially different 的实现仍满足它，Human 会接受吗？**

会，通常说明它只是 How，不该被 Northstar 固定。

不会，说明它描述的是 Human 真正在乎的结果、边界、风险承诺或验收要求，应留在 Goal。

当前实现、已有 class/provider、某个计划写得很具体，都不能自动把 How 抬成 Goal。反过来，如果 Human 明确要求某种 representation / compatibility / provider，因为它本身就是业务或技术承诺，它就可以成为 Goal 的一部分。

## 别把 map 当 reality

Prompt、已有 plan 和 Northstar 自己都只是 map；repo、runtime、历史约束和真实使用者可能暴露 map 没写出来、但会改变 Goal 的事实。

优先沿这种差异查：已有 authoritative spec / precedent、真实 consumer、repo 外 contract、serialized/config identity、部署/授权约束、当前 workspace 与 Human Goal 的真实关系。它们是按需 lens，不是 checklist。

发现一个新事实后，只问：**它换一个值，Human 会不会接受另一个 Goal？** 不会就停止展开。

## 要求发生冲突时

如果 Human 同时给出的要求无法一起满足，Goal 必须让 Executor 知道什么优先。这个优先级只能来自 Human、已有 authority 或不可替代的 reality；Northstar 不能因为某个实现更方便就偷偷重排。

reality 能排掉冲突就直接收敛；否则把真正需要 Human 拍板的冲突一次问清，并说明主要后果与推荐。

## 什么时候停

当剩余问题只会改变 How，而不会再改变 Human 会接受的 Goal，就停止 Intent Research。Implementation 中继续出现新 Unknown 是正常的；Northstar 不需要在执行前把它们消灭。
