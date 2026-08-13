# Evaluate Architecture Evolution

只用于显式 smoke/eval；正常 runtime 不读。本文件冻结 behavior property，不定义 runtime。

## Static smoke

1. 主 Skill 自己完成调研 → architecture judgment → Program → delivery；无 ready/completed/status lifecycle。
2. 正常成功路径不依赖第二份 output/compile contract；`rules.md` 只处理难判 discriminator，legacy/Brooks 仅按需读取。
3. Research 从指定 module/capability 与 direct neighborhood 渐进展开；只有会改变 architecture judgment 的 authority/SOT/identity/external constraint 才扩大。
4. 当前 taxonomy/proposed shape 只是 Evidence；没有 stable variation 不制造 provider。
5. Layering/cohesion、abstraction/specific、primary/auxiliary、real evolution 都能改变 Target Architecture；长期 dependency boundary 优先由 repo/module/package/build/tooling 表达，独立 authority/lifecycle 的相邻 subsystem 不因 cohesion 被吞并；反复解释 ownership/dependency 的 guidance 可作为结构歧义 Evidence，但必须与不可消除的 domain semantics 区分。
6. local pressure 不制造 Program；真实 fork 缺 decisive Evidence/Human decision 时保持 unresolved。
7. Program 最多 3 个 Improvements，不补数；每项必须同时解除真实 change pressure、产生可说明的长期演进收益、structural gain + real exit，并按长期 leverage 排序；只有整洁/规范收益的 change 不得冒充 Improvement。
8. Program 引用 authoritative repo SOT；handoff artifact 不成为 repo architecture SOT。
9. AE 停在 architecture outcome / structural done condition；除非 authority 绑定 representation，不固定 implementation。
10. 上游 shaping capability 调用时 AE 返回 Evidence/options/decision surface，不抢 Human Ask ownership。
11. 成功 Program 同文 materialize 到 repo/workspace 外 handoff file，交付只包含当前 judgment/Program；material correction 后完整重交付；写入失败不得假装成功。
12. `agents/openai.yaml` 是 thin invocation pointer；validation 不进入 runtime。

## Regression cases

- **P1 Bounded research**：历史模块 + current provider taxonomy → 从责任/直接上下游重识别 boundary，仅 decisive unknown 扩搜。
- **P2 Consumer/cohesion boundary**：consumer 仍解释 capability 私有事实，且相邻 subsystem 已有独立 authority/lifecycle → Target 让旧 consumer knowledge/path 退出，但不为 cohesion 吞并相邻 owner。
- **P3 Provider taxonomy**：family switch 存在 → 只有 stable semantic/lifecycle/performance/deployment variation 才形成 provider。
- **P4 Dependency**：common/core 依赖 specific implementation → Target 建立稳定单向 dependency boundary，并优先由 module/package/build/tooling 机械表达，而非仅靠文档约定。
- **P5 Abstraction**：代码相似但 semantics 不同 / 实现不同但 invariant 相同 → 前者 specific，后者抽象 stable invariant。
- **P6 Performance**：无 profiling/SLA/resource Evidence 的 fast path → 不得打穿 primary boundary。
- **P7 Real evolution**：新增 facade/registry 但旧 authority/path 仍在 → 不得算 evolution；Program completion 必须指出整体完成后哪些旧 authority/dependency/path 不再 authoritative。
- **P8 Second system**：简单 pressure 引入 plugin/framework/hooks → 无当前长期 Evidence 就缩小。
- **P9 Prose-compensated boundary**：同一 ownership/dependency 规则在 AGENTS/comment/runbook 中反复解释，而 repo territory/build dependency 仍无法直接表达 → 把这种重复 guidance 作为 architecture Evidence 继续判断；若它只是不可从结构推出的 domain semantics，则保留 guidance，不得为了“agent 更好读”强行改 architecture。
- **P10 Guidance exit**：Architecture Improvement 已把原本只能靠 prose 约束的 owner/dependency 物化进 module/package/build/tooling → 对应补偿性 guidance 应退出或停止 authoritative；若仍有独立 domain semantic/contract，则只删除已被结构替代的部分。
- **V1 Low-value cleanup**：一个候选 change 能删掉旧 helper/namespace、让 dependency 更干净，也满足 structural gain + real exit，但当前或反复出现的 change pressure 并未因此更容易、更独立或更可验证 → 不得仅因结构更漂亮进入 Top Improvements；最多作为 local cleanup/附带退出处理。
- **V2 Positive leverage**：一类真实需求每次都要跨多个 owner 重组私有 knowledge；候选 Target 让该 capability 的 responsibility/dependency/authority 闭合，后续同类变化可在单一边界内完成并由稳定 Evidence 验证，同时旧跨边界 path 退出 → 这是优先 Architecture Improvement，即使实际 patch 不大。
- **V3 AI-native as consequence**：候选结构让后续 change 的 owner、allowed dependency、authoritative state 和完成 Evidence 可从局部 repo territory/tooling 发现并验证，减少跨边界 reconstruction → 可作为正确 boundary 的正向收益；若为了 agent/navigation 便利而破坏 primary responsibility 或制造额外层，则失败。
- **C1 Improvement quality**：research/data collection 不进 Top Improvements；只有同时产生长期演进收益、structural gain + real exit 的 change 可进。
- **C2 Ceiling**：只有 2 个真实 Improvements → 只输出 2 个。
- **C3 Setup-only**：先建 abstraction、以后再迁 → 若当前不产生 gain/exit，不得入 Program。
- **C4 Leverage**：多个真实 Improvements → 优先解除当前/反复 change pressure 对 capability 独立演进的结构约束，而不是最易实现、最整洁或只减少表面 cross-boundary dependency 的项。
- **C5 SOT**：已有 authoritative contract → 引用原 SOT；需演进时指向原 source delta。
- **N1 Local**：bug/dead getter/mechanical cleanup → local judgment，不制造 Target/Program。
- **R1 Real fork**：两个长期结构都可行且缺 decisive constraint → unresolved，不按模式偏好强选。
- **H1 Human ownership**：Northstar 路由来的 Human-owned choice → AE 返回 decision surface，不自行串行 Ask。
- **L1 Legacy**：旧 token 本地无 reader但可能外部可见 → search absence 不等于可删，只做 decision-relevant probe。
- **O1 Altitude**：Target 已稳定 → 固定 architecture outcome，不规定 class/API/file/schema/MR/test provider。
- **D1 Re-entry**：Program 交付后 Human material correction → 重开受影响判断并完整重交付当前 Program，不附 Research inventory、rejected alternatives 或旧 Program。
- **D2 Artifact failure**：Program 已收敛但外部 file 不可写 → blocker，不把 conversation 当成功 handoff。

## Captured properties

1. taxonomy / proposed shape 是 Evidence，不是 law；
2. Target / Improvements 必须从真实 change pressure 的长期演进收益出发，结构正确但不改变后续演进能力的 cleanup 不够；
3. abstraction 由 stable semantics/invariants 决定；
4. 长期 dependency boundary 优先机械可见，cohesion 不吞并独立 authority/lifecycle；正确 boundary 还应让后续 change 所需的 owner/authority/Evidence 更局部可发现和验证，但 AI convenience 不得塑造 primary architecture；
5. auxiliary concern 不塑造 primary architecture，caller 不重组 capability 私有 knowledge；
6. real evolution 要求旧 authority/knowledge/dependency/path 退出，已被结构替代的补偿性 guidance 同样退出；
7. Research bounded，Program 只保留 independently improving changes；
8. authoritative repo truth 不复制成平行 SOT；
9. repeated ownership/dependency prose 只是 architecture Evidence，必须先区分 structural ambiguity 与 irreducible domain semantics；
10. specialist 不抢 Human decision ownership；
11. delivery 只交当前 judgment/Program，且不是 lifecycle state；material update 后必须完整重交付；
12. handoff artifact 只承担 transport authority，不替代 repo SOT。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget：
`A. 不加载 architecture-evolution` vs `B. 加载 architecture-evolution`。

评分：Research scope、change-pressure alignment、architecture taste、Program leverage/convergence、architecture altitude、Human routing、re-entry、handoff integrity、context cost。

只有 clean-session paired Evidence 才能声明 behavioral uplift；否则标记 `NOT RUN`。
