# 当 Human 还没真正决定 Goal

只在 `SKILL.md` 已经查过 reality，但仍无法确定 Human 最终会接受哪个 Goal 时读取。

Prompt、已有 plan 和 Northstar 自己都只是 map；repo、runtime、历史约束和真实使用者会暴露 map 没写出来的东西。这里不是把未知全找完，而是找到**会改变 Goal 的那个选择**。

## 找选择，不找信息

看到新的事实时只问：

> 如果这个事实换一个值，Human 会不会接受不同的 Goal？

不会，就留给 Executor 或忽略。会，才继续追。

业务/兼容约束、已有规格和历史决定、真实 consumer、repo 外 contract、当前 workspace 都可能藏着这种选择，但它们只是按需查看的地方，不是 checklist。

## 能查的先查

reality 能决定的事实自己 probe，不让 Human 猜。Reality 可以推翻一个实现手段，但不能替 Human 改 Goal。

如果 reality 已经把分叉排掉，就回主流程继续 Compile。只有几个 materially different 的 Goal 仍都说得通，而且 reality 无法替 Human 决定时，才把这些选择一次交给 Human；必要时给后果和推荐。

## 只剩 How 就停

一旦剩余未知只会改变 How，不会改变 Goal，就停止 Research。Implementation 中继续出现新问题是正常的，不需要 Northstar 提前消灭。
