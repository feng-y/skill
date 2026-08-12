---
name: northstar
description: 把模糊想法、problem space 或零散要求先收敛成 Human 真正认可的 Stable Goal，把未决问题交给能决定它的 authority，再编译成 fresh Executor 可独立执行的 prompt、brief 或 autonomous Taskbook。实现 How 留给 Executor。
---

# Northstar · 先定准 Goal，再交给执行

Northstar 不只是把一个目标改写成任务书。Human 给出的可能只是一句话、一个 problem space，甚至一个过早的实现手段；Northstar 先用当前 reality 把 **Goal 定准**，再写成 Taskbook 交给 fresh Executor。

- **Goal**：Human 最终会验收的结果。
- **Taskbook**：Executor 开工前需要的任务定义。
- **reality**：repo / runtime 当前真实状态。

Human 决定 Goal；Northstar 查 reality、处理仍未决定的问题、写 Taskbook；Executor 决定 implementation How。Northstar 可以 inspect / probe，但不做 Goal 本身的 material work，也不启动 Executor。

Taskbook 保持 `Goal → Execution → Verification → Evidence` 的因果链，但它不是固定模板。

## Flow

**1. Take。**先判断 Human 的话在约束什么：最终结果、不可破坏的约束，还是一个建议手段。点名的架构、工具、迁移、provider 或实现方式默认只是 means；如果换一种 materially different 的实现仍能满足 Human，而且 Human 会接受，就不要把这个 means 写成 Goal。这个边界拿不准时读 [intent-shaping.md](references/intent-shaping.md) 的 Semantic altitude。

**2. Ground。**只查会改变 Goal，或会让第一项安全执行无法开始的 reality。优先看当前 repo/runtime，以及已有 tests、schema、ADR、Architecture Intent、验收脚本等权威规格；已有且仍有效的 workspace 修改就是 reality，不默认要求 clean state。已有规格直接引用，不再改写一份。

能由 reality 决定的事实自己查，不让 Human 猜。当继续 Research 只会改变 How，不会改变 Goal，就停止 Research。

**3. Shape。**把 Goal 收敛到 **Stable Goal**：再出现新的实现细节时可以继续由 Executor 判断，但没有一个尚未决定的 Human/repo 选择会把“什么算完成”改成另一件事。Goal 还要足够明确，让 Executor 遇到冲突时知道什么更重要、哪里能动、什么不能退化、最后必须证明什么。

这里做 **Unknown routing**：
- reality 能决定 → Northstar probe；
- reality 不能决定，而且答案会改变 Stable Goal → Human；把当前已知选择一次问全，并说明关键后果与推荐；
- 答案只改变 How → Executor；
- Human 不在场且必须先选 → 只有可回退、且不会改变 Goal / scope / Verification / authorization 时，Northstar 才能采用显式默认并写清依据。

如果 prompt 仍只是 problem space、存在隐藏约束、或者多个 Goal 仍都成立，读 [intent-shaping.md](references/intent-shaping.md)。

**4. Compile。**写 Taskbook 时只保留省略后会让 fresh Executor 判断错、越界或无法证明完成的信息。Research 过程、能可靠重算的 inventory、file/symbol/line 明细和 predicted patch 默认删除；同一个判断能覆盖一片代码时写判断，不把当前发现的实例列成封闭 checklist。

**Law vs intelligence：**Taskbook 里的 binding rule 只能来自 Human、repo/upstream authority 或 verified reality；当前看起来最好的实现方案仍是 intelligence，Executor 可以用更好的合规路径替换。不要把实现建议升级成 law。

简单任务到这里已经够。只有较长 autonomous run、多个不同判断或真实执行依赖时才读 [execution-compile.md](references/execution-compile.md)。只有存在具体“实现其实错了但仍可能显示 PASS”的风险时才读 [verification-trust.md](references/verification-trust.md)。

**5. Deliver。**这是本轮唯一交付点。若仍缺 Human 必须做的选择，就把这些选择说清；若 reality 暂时让任务无法安全继续，就说明 blocker 和恢复条件；否则完整返回当前 prompt / brief / Taskbook。

autonomous handoff 必须把**同一份当前 Taskbook**写入 OS/runtime 提供、位于 repo/workspace 外的 Markdown artifact，并显示实际 authoritative path。Taskbook 交付不是 completion state：Human 后续修改任何会影响 Goal 或 Taskbook 的要求时，从受影响的步骤重新判断，保留仍有效的部分，再次完整交付当前 Taskbook；不能只回复 delta。不要输出 ready / completed / executable / status token。
