# 当 Human 还没真正决定结果

只在 `SKILL.md` 已经查过现实，但仍无法确定 Human 最终会接受哪个结果时读取。

Prompt、已有 plan 和 Northstar 自己都只是 map；repo、runtime、历史约束和真实使用者才会暴露 map 没写出来的东西。这里的目标不是把 Unknown 全找完，而是找到**会改变 Human 对“做完”的判断**的那一个缺口。

## 找选择，不找信息

看到新的事实时只问：

> 如果这个事实换一个值，Human 会不会接受不同的完成结果？

不会，就不属于 Intent shaping；留给 Executor 或忽略。会，才继续追。

因此可以按需看业务/兼容约束、已有规格和历史决定、真实 consumer、repo 外 contract、当前 working tree 等，但它们只是可能藏着选择的地方，不是固定 checklist。

## 能查的先查

repo/runtime 能决定的事实自己 probe，不让 Human 猜。Reality 可以推翻一个实现手段，但不能替 Human 改结果。

如果现实已经把选择排掉，就回主流程继续 Compile。只有几个 materially different 的完成结果仍都说得通，而且现实无法替 Human 决定时，才把这些选择一次交给 Human；必要时给后果和推荐。

## 什么时候停

一旦剩余不确定性只会影响“怎么做”，而不会改变 Human 接受的结果，就停止 Intent Research。Implementation 中继续出现 Unknown 是正常的，不需要 Northstar 提前消灭。
