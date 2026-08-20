# 当 Goal 还没有定准

只在普通理解与 bounded reality 检查后，Human 最终会接受哪个 Goal 仍不清楚，或真正需要 Human authority 的选择仍未关闭时读取。这里负责 Goal shaping，不建立第二套 Northstar workflow。

## Goal 还是 How

只问一个问题：

> **换一种 materially different 的实现仍满足它，Human 会接受吗？**

会，通常是 How，留给 Executor。不会，且它表达 Human 真正在乎的结果、边界、兼容/风险承诺或 representation，则进入 Goal / binding constraint。当前实现、class/provider、候选方案写得再具体，也不会因此获得 authority。

Human requirement 与 reality claim 分开：Human 有权给出的要求可以直接 binding；关于 owner、producer、consumer、readiness、runtime behavior 等事实仍需 reality Evidence，不能用 Human/模型叙述或 artifact presence 代替。

## 哪些选择必须给 Human

reality 无法关闭，且不同答案会改变 Human 最终接受的 Goal，或 materially 改变**是否做、投入规模、承诺寿命、长期维护责任或风险姿态**时，由 Northstar Ask。两个 implementation 都能满足同一功能结果，也可能因为投入/长期承诺 materially different 而仍属于 Human choice。

当前前提已闭合、可以独立回答的 Human-owned choices 尽量同一轮给出：说明会改变什么，给足 Evidence；能可靠枚举时给真实 options、主要后果和推荐，不能可靠枚举就限定回答边界，不编造 option。依赖另一个尚未拍板前提的 downstream choice 等前提关闭后再问。Human 不在场而必须先做选择时，只能采用可回退、且不会改变任何 Human-owned choice、allowed boundary、Verification 或授权的显式默认，并保留依据；真正 Human-owned choice 不能被默认关闭。

## Human 还没形成 trade-off 时

只有 Human 自己还在探索“真正的问题是什么”或“哪种取舍更重要”时才 Grill，不把清楚的 choice 再复杂化。

有当前倾向时分别给出支持/反对它的最强理由；framing 本身未定时比较最可信的解释，找出真正分歧、矛盾和隐含假设。若一个可查事实能裁决分歧，先 Research；事实已经足够而剩下的是价值判断时，一次只问当前最能区分立场的一个问题。Human 回答后重新判断 owner：仍是 Human judgment 才继续 Grill；变成事实、prototype 或 specialist judgment 就交回对应 owner。一旦 trade-off 清楚，回正常 Ask batching。

## Specialist 与 prototype

只有当前 Goal / Human choice 无法由 bounded local judgment 关闭时才扩大：

- 多个耦合 Unknown / source alignment 需要完整判断时，可交 `$unknowns-first`；
- 长期 module responsibility、boundary、dependency direction 或 Target Architecture 未定时，可交 `$architecture-evolution`；
- 文字讨论仍不能可靠决定，而一个廉价、可丢弃、可回退的 concrete artifact 能明显提高判断质量时，可以做最小 prototype / sample。

specialist / prototype 只回答当前 decision question，返回 decision / Evidence / option surface；不成为第二份 Taskbook，也不替 Human 关闭 Human-owned choice。不要为了减少 Executor 的 implementation uncertainty 调 specialist。

## reality、冲突与停止

只检查会改变当前 Goal / Human choice 的 reality。发现新事实后问：**它换一个值，会不会让 Human 接受另一个 Goal 或 materially different commitment？** 不会就停止展开。

Human requirements 冲突时，priority 只能来自 Human、已有 authority 或不可替代 reality；不能按实现便利性偷偷排序。Human correction 替换被纠正 premise，只重新打开依赖它的 Goal/choice；无关且已关闭的选择保持关闭。

当剩余问题只改变 Executor How，而不再改变 Human 会接受的 Goal、Human-owned commitment 或 binding boundary 时，停止 Intent Research。执行期继续出现 Unknown 是正常的。
