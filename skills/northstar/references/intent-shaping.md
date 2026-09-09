# 当 Intent 还不足以支持下一步判断

只在问题 framing、Human 真正接受的结果、边界或承诺仍会改变下一步判断时读取。Intent shaping 是 Intent take 中的判断，不是另一个阶段、问卷或 Goal 文档生产流程。已有意图清楚时不重复访谈。

## 恢复问题，而不只是重述所提方案

从原始表达、需求来源与必要 reality 区分：Human 遇到了什么问题、希望谁的什么行为或处境改变、为什么现在需要处理，以及哪些约束和取舍已经成立。只保留会改变下一步选择的内容，不要求每次填满一套字段，也不替 Human 编造业务价值或数值目标。

一个 Goal 句子可能准确却仍不足以交接：相同结果可能服务于不同用户、obligation 或投入承诺。让下一位判断者能从当前意图区分这些差异；原始来源足够时直接引用。只有不同解释会导致 materially different work 或 acceptance，才继续追问或调查。

## Goal 还是 How

只问：**换一种 materially different 的实现仍满足它，Human 会接受吗？**

会，通常是 How，留给 Executor。不会，且它表达 Human 真正在乎的结果、边界、兼容/风险承诺或 representation，则进入 Goal / binding constraint。当前实现、class/provider、候选方案写得具体，不会因此获得 authority。

Human requirement 与 reality claim 分开：Human 有权给出的要求可以直接 binding；owner、producer、consumer、readiness、runtime behavior 等事实仍需 Evidence，不能用叙述或 artifact presence 代替。发现手段与原问题不匹配，修正问题理解或候选路径，而不是把手段本身当成功。

## 哪些选择必须给 Human

reality 无法关闭，且不同答案会改变 Human 最终接受的 Goal，或 materially 改变**是否做、投入规模、承诺寿命、长期维护责任或风险姿态**时，由 Northstar Ask。两个 implementation 都满足同一功能，也可能因投入/长期承诺不同而属于 Human choice。是否做与投入多少分开：已有 obligation 不因收益低被取消，可以选择满足 obligation 的最小充分投入。

当前前提已闭合、可以独立回答的 choices 尽量同轮给出：说明会改变什么，给足 Evidence；能可靠枚举时给真实 options、主要后果和推荐，否则限定回答边界，不编造 option。依赖未定前提的 downstream choice 等前提关闭后再问。Human 不在场时，只能采用可回退且不改变 Human-owned choice、allowed boundary、Verification 或授权的显式默认；真正 Human-owned choice 不能被默认关闭。

## Human 还没形成 trade-off 时

只有 Human 自己还在探索“真正的问题是什么”或“哪种取舍更重要”时才 Grill，不把清楚的 choice 再复杂化。

有当前倾向时给支持/反对它的最强理由；framing 未定时比较最可信解释，找真正分歧、矛盾与假设。可查事实能裁决分歧就先 Research；事实足够而剩下的是价值判断时，一次只问当前最能区分立场的问题。回答后重新判断 owner：仍是 Human judgment 才继续；变成事实、prototype 或 specialist judgment 就交回对应 owner。trade-off 清楚后回正常 Ask batching。

## Specialist 与 prototype

只有当前 intent / Human choice 不能由 bounded local judgment 关闭时才扩大：耦合 Unknown / source alignment 可交 `$unknowns-first`；长期 responsibility、boundary、dependency 或 Target Architecture 问题可交 `$architecture-evolution`。

specialist 可基于明确假设比较结构后果，返回 decision / Evidence / options，不必先把未决 Human choice 伪装成已批准 Goal。技术后果回到同一 intent judgment；没有新的架构问题，不因进入新阶段重复调用 AE。

若一个廉价、可丢弃、可回退的 sample / prototype 能比继续讨论更好地区分意图解释或真实取舍，做最小 probe，并说明它回答哪个问题、什么观察会推翻当前解释。probe 只产生 Evidence，不成为第二份 Taskbook，不自动进入 production、长期架构或已批准 scope。只减少实现不确定性的工作留给 Executor。

## reality、冲突与停止

只检查会改变当前 intent / Human choice 的 reality。发现事实后问：**它换一个值，会不会让 Human 接受不同结果、范围或 materially different commitment？** 不会就停止展开。

requirements 冲突时，priority 只能来自 Human、已有 authority 或不可替代 reality，不能按实现便利偷偷排序。Human correction 替换被纠正 premise，只重新打开依赖它的判断；无关且已关闭的选择保持关闭。

当前请求所需意图已经清楚就交付；要进入执行时，剩余问题只改变 Executor How、不再改变 accepted outcome、Human commitment、binding boundary 或 safe start，就停止 Intent Research。执行期 Unknown 正常存在，不要求先产出独立 Goal 再继续。
