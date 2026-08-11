# Architecture Reasoning Kernel

只在需要 architecture judgement 时读取。本文件拥有 architecture forces、current model、design-space、trade-off 与 evolution judgment；这些是可按 evidence 选用的 lenses，不是固定推理流程。本文件不定义最终输出模板，也不规定实现 representation。

## Architecture or local

有效 architecture work 必须能追溯到真实 pressure，而不是模式偏好。常见 pressure 包括：变化持续跨多个 owner 传播、caller 反复重建内部知识、多个事实源或 policy 并存、runtime control / lifecycle 被错误边界持有、provider/family/mode 分支持续增长、兼容路径长期不退、结构原因反复造成事故或回归。

文件大、函数长、目录不整齐、switch/if 很多或单次局部修改都只是 evidence；如果一个局部修复就能消除 pressure 且不重新定义长期 responsibility / authority / knowledge / control / lifecycle / dependency / variation boundary，就不要升级为 architecture evolution。

## Architecture forces

只展开会改变 architecture decision 的 forces。

### Change locality

问未来最可能反复发生的变化是什么，以及当前结构会迫使哪些本不应一起变化的责任同时修改。好的 boundary 让稳定共变的 responsibility 靠近，让独立变化保持局部；不要用“高内聚低耦合”替代具体 change-pressure 判断。

### Knowledge ownership

问一个组件为了完成自己的责任，正在知道哪些本不该知道的事实：implementation identity、configuration interpretation、ordering、lifecycle、state、fallback、protocol 或 capability-private variation。caller 能调用 capability 不等于 caller 应理解 capability 如何成立。

纯 composition-root wiring 不自动是 knowledge leakage；如果它只选择 implementation，没有承载业务 policy、runtime sequencing、lifecycle ownership 或 usage knowledge，就是合法组装边界。

### Authority, control & lifecycle

不要把 ownership 压成单一 owner。按当前问题区分 semantic authority、configuration authority、construction、runtime selection、execution control、state ownership、publication/reload、lifecycle 与 observation。只有 evidence 证明必须 cohesive 的责任才应收敛；相邻 subsystem 已有正确 owner 时，优先稳定 relation/contract，不因“统一”吞并它。

### Authority / SOT / dependency

同一事实、policy 或 decision 应有清楚 authoritative source。source dependency 和 runtime control 都要看：clean source graph 不代表 runtime control 正确，clean interface 也不代表 authority 已闭合。稳定 policy 不应被 provider、场景或 implementation 反向定义。

### Essential variation

Observed partition 只是 evidence。只有差异稳定改变 business semantics、precondition、output contract、consistency/lifecycle、performance architecture、deployment boundary 或其他长期 invariant 时，才值得成为 architecture-level variation；历史 API、当前 class hierarchy、provider 名称、mode 或调用形状本身不能证明 variation 应长期存在。

## Minimal current architecture model

不要机械生成 C4/目录图。只建足以改变 decision 的最小模型：capability / responsibility、authority / SOT、knowledge、control / lifecycle、source/runtime dependency、stable or suspected variation、change-pressure relation。模型的价值是解释为什么 change 会传播、knowledge 为什么泄漏、authority 为什么分裂，以及哪个 boundary 真正承担长期变化；不能影响 decision 的 inventory 不进入当前模型。

## Design space

不要在第一个 plausible shape 上停止。若存在 materially different 的 architecture，它们至少应改变一个长期 architecture axis：responsibility owner、knowledge boundary、authority/SOT、control direction、lifecycle ownership、dependency direction 或 essential variation model。

`FooManager` vs `FooProvider`、同一 owner 的不同类层次、不同文件布局或 API 命名不算不同 architecture。

也不要固定“必须三个方案”。当 repo authority / forces 已经唯一决定方向时，不制造 alternatives ceremony；当两个 materially different architecture 都成立而关键 forces 尚不足以裁决时，返回 unresolved。

## Architecture decision

选择 architecture 不是选“最整洁”的图，而是选择哪组长期 trade-off 更适合真实 forces。只比较会改变结论的维度：future change locality、caller/coordinator knowledge、authority/SOT、control/lifecycle、essential variation、conceptual integrity，以及新 abstraction 把 complexity 搬到哪里。

特别警惕删除 central branch 后形成 flag matrix、mini-framework、implicit DSL、global registry 或长期 adapter；如果 decision knowledge 仍由另一个 generic layer 重新解释，complexity 只是搬家。

### Counterfactual test

如果一个 materially different Target Architecture 也能满足同一 outcome / boundary，必须能用 forces 解释为什么当前选择更合适。解释只能依赖稳定 semantics、change pressure、authority、lifecycle、dependency 或 evolution cost；不能因为当前代码更像某个方案就选择它。

### Complexity relocation

真实 evolution 必须让旧 complexity 退出，而不是 `old A → new abstraction → old B`。比较方案时明确：哪些 knowledge / branch / source / compatibility / dependency 被删除，哪些新 complexity 是必要的，以及新 complexity 是否有更稳定 owner。

需要经典架构约束辅助判断时按需读 `brooks-constraints.md`，但不要把其中的名称、评分或 checklist 变成输出协议。

## Target Architecture altitude

Target Architecture 可以固定长期 responsibility / capability boundary、authority / SOT、knowledge / control direction、state / lifecycle ownership、dependency invariant、essential variation boundary，以及 architecture-level acceptance 与必须退出的旧责任/知识/路径。

它不能仅凭 model preference 固定 class、API、文件、具体 helper、某个 flag/metadata schema、虚函数形态、调用顺序实现、migration task、lint/test/provider 套餐。representation 只有 Human/repo authority 或不可替代的技术约束使其成为 invariant 时才进入 architecture law。

## Architecture evolution

Architecture Decision 不能只有目标图，还要说明系统如何从 current architecture 进入 target architecture，但只到 architecture-level transition。

重点判断新 authority / boundary 何时建立、旧 authority 何时停止 authoritative；哪类 caller knowledge / control / dependency 在什么 architecture condition 成立后退出；adapter、dual path、compat 或 bridge 若必须出现，其 architecture purpose 和 exit condition 是什么；哪些 ordering 来自 architecture dependency；哪些 transition 可回退、哪些会形成长期 lock-in。

最终 evolution 应让 target architecture 比 current architecture 更容易解释和继续变化；如果中间结构只是把复杂度叠加且没有可信退出条件，decision 尚未成立。

## Material Unknown

只有会改变 architecture vs local、Target Architecture、关键 trade-off、boundary 或 evolution path 的 unknown 才是 Material Unknown。

```text
Claim at risk → Minimal probe / Human decision → Evidence → Decision changed / retained
```

事实缺口能从 repo/runtime reality 关闭就先 probe；真正属于 Human-owned 的业务、兼容、风险或长期承诺才 Ask。不会改变 architecture decision 的 unknown 留给后续 design / execution。

## Evidence lifetime

同一事实或 judgment 只保留一份当前 authoritative state。前提未变就复用；新 authoritative evidence 改变前提时，只 reopen 依赖它的 current model、alternative comparison、decision 或 evolution conclusion，不把新旧 snapshot 并列为 active truth。

任何反证若证明问题其实 local、不同 bounded context 被误统一、alternative 只是 representation、complexity 只是搬家、transition 依赖永久 dual authority/adapter，或存在 Human-owned 长期决定，都应直接缩小、替换或保持 unresolved；不要新增一套 guard 来保住原结论。
