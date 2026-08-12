# 当 Goal 还没有定准

只在普通的输入理解与 reality 检查仍无法确定 Human 最终会接受哪个 Goal，或关于是否做、投入与长期承诺的选择仍未关闭时读取。

如果已经不是单一 Goal/How 或 Human choice 的判断，而是多个耦合 Unknown 需要 source alignment，或长期模块责任、边界、依赖方向本身需要架构判断，回主 Skill 路由给对应 specialist capability；specialist 可以形成 Evidence/options/decision surface，但其中需要 Human 拍板的 choice 仍回 Northstar Ask，不要让 specialist 替 Human 关闭。不要在这里继续堆一套平行流程。

## 这是 Goal，还是 How

先做一个测试：

> **换一种 materially different 的实现仍满足它，Human 会接受吗？**

会，通常说明它只是 How，不该被 Northstar 固定。

不会，说明它描述的是 Human 真正在乎的结果、边界、风险承诺或验收要求，应留在 Goal。

当前实现、已有 class/provider、某个计划写得很具体，都不能自动把 How 抬成 Goal。反过来，如果 Human 明确要求某种 representation / compatibility / provider，因为它本身就是业务或技术承诺，它就可以成为 Goal 的一部分。

## 同一个 Goal，是否做、投入与长期承诺仍可能需要 Human 决定

两个路径即使满足同一个 Goal，只要它们在是否做、投入与长期承诺上 materially different，就不是 Northstar / Executor 可以按自身偏好默认关闭的 How。先查已有 authority 与 reality；仍有多个可接受选择时，把当前可回答的 options、主要后果与推荐交给 Human。

Northstar 仍可自主做廉价、可丢弃、可回退且不会改变这些选择的 probe / prototype 来购买 Evidence；一旦 prototype 本身改变这些选择，也回到 Human decision。需要判断长期结构 option 时，可以先回主 Skill 路由 architecture judgment 来获得 Evidence/options；specialist 判断结构，不替 Human 判断是否值得投入。不要因为“长期更正确”擅自扩大投入，也不要因为“当前路径更便宜”偷偷缩小承诺。

## 用 reality 校正当前 Goal 假设

Human 当前表达和已有 plan 可能漏掉会改变 Goal 的事实。只在它们可能改变 Human 最终接受结果时，检查 authoritative spec / precedent、真实 consumer、repo 外 contract、serialized/config identity、部署/授权约束，以及当前 workspace 与 Human Goal 的真实关系。

发现一个新事实后，只问：**它换一个值，Human 会不会接受另一个 Goal？** 不会就停止展开；如果差异已经耦合到需要完整 unknown/source map，回主流程交给对应 specialist owner。

## 要求发生冲突时

如果 Human 同时给出的要求无法一起满足，Goal 必须让 Executor 知道什么优先。这个优先级只能来自 Human、已有 authority 或不可替代的 reality；Northstar 不能因为某个实现更方便就偷偷重排。

reality 能排掉冲突就直接收敛；否则把**当前前提已经闭合、可以独立回答**的 Human-owned 冲突一起问清，并说明主要后果与推荐。依赖另一个尚未拍板前提的后续选择，等前提关闭后再问。Human 只回答一部分、插入新约束或中断时，把最新输入合入当前判断，只重新打开受影响部分；一旦剩余问题都能由 Executor 在同一个 Goal 下继续，就停止 Ask 并回主流程产出。

## 什么时候停

当剩余问题只会改变 How，而不会再改变 Human 会接受的 Goal，也不会 materially 改变这些选择时，就停止 Intent Research。Implementation 中继续出现新 Unknown 是正常的；Northstar 不需要在执行前把它们消灭。
