# 当 Intent 还不足以支持当前判断

只在问题理解、当前委托、被接受的结果或 Human-owned choice 仍会改变下一步判断时读取。Intent shaping 属于 Intent take，不是每次必走的访谈或独立 Goal 产出阶段。

## 保留决定性意图

从当前有效的请求和来源区分：原来要解决什么、为什么需要处理、当前要求推进到哪里，以及哪些范围 / 约束 / 承诺已经成立。只保留会改变选择的信息，不要求填满字段，不把自己的解释当成事实或 Human 已接受的要求。

如果严格完成所提方案仍可能未解决原问题，比较最可信的解释，用可区分它们的最小事实或样例收敛；改变 accepted outcome 或投入承诺时交回 Human，不按实现便利偷偷换目标。相同结果不能抹去不同的 binding 投入与 obligation；已有义务不由模型按收益自行取消。

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

有当前倾向时分别给出支持/反对它的最强理由；framing 本身未定时比较最可信的解释，找出真正分歧、矛盾和隐含假设。若一个可查事实能裁决分歧，先 Research；事实已经足够而剩下的是价值判断时，一次只问当前最能区分立场的一个问题。Human 回答后重新判断 owner：仍是 Human judgment 才继续 Grill；变成事实、concrete shaping 或 specialist judgment 就交回对应 owner。一旦 trade-off 清楚，回正常 Ask batching。

## Specialist 与 concrete shaping

只有当前 Goal / Human choice、其关键结构后果，或可接受 Target 的具体形态无法由 bounded local judgment 可靠关闭时才扩大：

- 多个耦合 Unknown / source alignment 需要完整判断时，可交 `$unknowns-first`；
- 长期 module responsibility、boundary、dependency direction 或 Target Architecture 未定时，可交 `$architecture-evolution`；
- Goal / choice 已经大体理解，但核心路径、ownership、boundary、interface 或 usage 仅靠 prose 仍可能被 materially different 的 Target 合理解释时，model-invoke `$intent-shape`，用最低成本的 Core Path / Usage / Prototype 暴露 decision surface，再消费其 correction / Evidence。

specialist / concrete shaping 只回答当前 decision question，返回 decision / Evidence / option surface / correction；不成为第二份 Taskbook，也不替 Human 关闭 Human-owned choice。AE 可以在显式假设下回答未决承诺的结构后果，不需要先伪造已批准 Goal；技术结论不自动成为 binding commitment。`$intent-shape` 只把 Target 变得可观察，完成后返回 Northstar，不拥有 binding Intent，不自动 productionize artifact，也不增加已批准 scope。不要为了减少 Executor 的 implementation uncertainty 调 specialist。

## reality、冲突与停止

只检查会改变当前问题理解、委托范围、Goal / Human choice 的 reality。发现新事实后问：**它换一个值，会不会改变当前请求的答案、被接受的结果或 materially different commitment？** 不会就停止展开。

Human requirements 冲突时，priority 只能来自 Human、已有 authority 或不可替代 reality；不能按实现便利性偷偷排序。Human correction 替换被纠正 premise，只重新打开依赖它的 Goal/choice；无关且已关闭的选择保持关闭。

当前请求所需意图已清楚就交付；只做意图澄清 / 取舍判断时，不以能否开始实现作为停止条件。需要执行约定时，剩余问题只改变 Executor How、不再改变 Goal、Human commitment、binding boundary 或 safe start，就停止 Intent Research。执行期继续出现 Unknown 是正常的。
