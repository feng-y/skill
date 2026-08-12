# Evaluate Architecture Evolution

只用于显式 smoke/eval；正常 runtime 不读。本文件冻结 behavior property，不定义 runtime。

## Static smoke

1. 主 Skill 自己完成调研 → architecture judgment → Program → delivery；无 ready/completed/status lifecycle。
2. 正常成功路径不依赖第二份 output/compile contract；`rules.md` 只处理难判 discriminator，legacy/Brooks 仅按需读取。
3. Research 从指定 module/capability 与 direct neighborhood 渐进展开；只有会改变 architecture judgment 的 authority/SOT/identity/external constraint 才扩大。
4. 当前 taxonomy/proposed shape 只是 Evidence；没有 stable variation 不制造 provider。
5. Layering/cohesion、abstraction/specific、primary/auxiliary、real evolution 都能改变 Target Architecture。
6. local pressure 不制造 Program；真实 fork 缺 decisive Evidence/Human decision 时保持 unresolved。
7. Program 最多 3 个 Improvements，不补数；每项完成即 structural gain + real exit；research/setup/future/implementation step 不得冒充 Improvement。
8. Program 引用 authoritative repo SOT；handoff artifact 不成为 repo architecture SOT。
9. AE 停在 architecture outcome / structural done condition；除非 authority 绑定 representation，不固定 implementation。
10. 上游 shaping capability 调用时 AE 返回 Evidence/options/decision surface，不抢 Human Ask ownership。
11. 成功 Program 同文 materialize 到 repo/workspace 外 handoff file；material correction 后完整重交付；写入失败不得假装成功。
12. `agents/openai.yaml` 是 thin invocation pointer；validation 不进入 runtime。

## Regression cases

- **P1 Bounded research**：历史模块 + current provider taxonomy → 从责任/直接上下游重识别 boundary，仅 decisive unknown 扩搜。
- **P2 Consumer knowledge**：consumer 仍解释 capability 私有事实 → Target 必须让旧 consumer knowledge/path 退出。
- **P3 Provider taxonomy**：family switch 存在 → 只有 stable semantic/lifecycle/performance/deployment variation 才形成 provider。
- **P4 Dependency**：common/core 依赖 specific implementation → Target 建立稳定单向 dependency boundary。
- **P5 Abstraction**：代码相似但 semantics 不同 / 实现不同但 invariant 相同 → 前者 specific，后者抽象 stable invariant。
- **P6 Performance**：无 profiling/SLA/resource Evidence 的 fast path → 不得打穿 primary boundary。
- **P7 Real evolution**：新增 facade/registry 但旧 authority/path 仍在 → 不得算 evolution。
- **P8 Second system**：简单 pressure 引入 plugin/framework/hooks → 无当前长期 Evidence 就缩小。
- **C1 Improvement quality**：research/data collection 不进 Top Improvements；只有独立 structural gain + real exit 的 change 可进。
- **C2 Ceiling**：只有 2 个真实 Improvements → 只输出 2 个。
- **C3 Setup-only**：先建 abstraction、以后再迁 → 若当前不产生 gain/exit，不得入 Program。
- **C4 Leverage**：多个真实 Improvements → 优先解除跨边界 knowledge/dependency，而非最易实现项。
- **C5 SOT**：已有 authoritative contract → 引用原 SOT；需演进时指向原 source delta。
- **N1 Local**：bug/dead getter/mechanical cleanup → local judgment，不制造 Target/Program。
- **R1 Real fork**：两个长期结构都可行且缺 decisive constraint → unresolved，不按模式偏好强选。
- **H1 Human ownership**：Northstar 路由来的 Human-owned choice → AE 返回 decision surface，不自行串行 Ask。
- **L1 Legacy**：旧 token 本地无 reader但可能外部可见 → search absence 不等于可删，只做 decision-relevant probe。
- **O1 Altitude**：Target 已稳定 → 固定 architecture outcome，不规定 class/API/file/schema/MR/test provider。
- **D1 Re-entry**：Program 交付后 Human material correction → 重开受影响判断并完整重交付，不只回复 delta。
- **D2 Artifact failure**：Program 已收敛但外部 file 不可写 → blocker，不把 conversation 当成功 handoff。

## Captured properties

1. taxonomy / proposed shape 是 Evidence，不是 law；
2. abstraction 由 stable semantics/invariants 决定；
3. auxiliary concern 不塑造 primary architecture；
4. caller 不重组 capability 私有 knowledge；
5. real evolution 要求旧 authority/knowledge/dependency/path 退出；
6. Research bounded，Program 只保留 independently improving changes；
7. authoritative repo truth 不复制成平行 SOT；
8. specialist 不抢 Human decision ownership；
9. delivery 不是 lifecycle state，material update 后必须完整重交付；
10. handoff artifact 只承担 transport authority，不替代 repo SOT。

## Paired behavioral eval

同一 model / repo snapshot / tool permission / budget：
`A. 不加载 architecture-evolution` vs `B. 加载 architecture-evolution`。

评分：Research scope、architecture taste、Program convergence、architecture altitude、Human routing、re-entry、handoff integrity、context cost。

只有 clean-session paired Evidence 才能声明 behavioral uplift；否则标记 `NOT RUN`。
