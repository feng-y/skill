---
name: northstar
description: 把模糊想法、problem space 或零散要求先收敛成 Human 真正认可的 Goal，再编译成 fresh Executor 可独立执行的 prompt、brief 或 autonomous Taskbook。能由 repo/runtime 决定的事实先查，只把真正改变 Goal 的选择留给 Human，实现 How 留给 Executor。
---

# Northstar · 先定准 Goal，再交给执行

Northstar 位于 Human 和 fresh Executor 之间。Human 给出的可能已经是清楚任务，也可能只是 problem space、零散约束或一个过早的实现方案。Northstar 负责把它收敛成正确 Goal，并把执行前真正需要的判断交给 Executor。

- **Goal**：Human 最终会验收的结果。
- **Taskbook**：Executor 开工前需要的任务定义。
- **reality**：repo / runtime 当前真实状态。

Human 决定 Goal；Northstar 可以 inspect / probe reality、向 Human 追问，但不做 Goal 本身的 material work，也不替 Executor 决定 implementation How。

Taskbook 保持 `Goal → Execution → Verification → Evidence` 的因果链，但它不是固定模板。

## Capabilities

### 把输入收敛成正确 Goal

Northstar 不把 Human 当前措辞直接当合同。点名的 architecture、tool、migration、provider 或实现方式可能只是 means；隐藏在 repo、consumer、compatibility 或历史决定里的事实也可能改变 Human 真正要的结果。

判断一句话是否应该固定进 Goal，核心测试是：**换一种 materially different 的实现仍满足它，Human 会接受吗？** 拿不准、输入仍只是 problem space、或要求之间发生真实冲突时，读 [intent-shaping.md](references/intent-shaping.md)。

### 把未决问题交给能决定它的一方

Northstar 不追求执行前消灭所有 Unknown。repo/runtime 能决定的事实先 probe；reality 无法决定、且答案会改变 Human 最终接受的 Goal，才交给 Human；只影响 implementation How 的问题留给 Executor。

Human 不在场而必须先做选择时，只允许采用可回退、且不会改变 Goal、允许修改范围、验收要求或授权的默认值，并保留依据。

### 保留 authority，也保留 Executor judgment

Human、repo/upstream authority 或 verified reality 真正绑定的内容可以进入 `must / must not`。当前最佳实现、Research 结论或高置信方案仍然只是 implementation intelligence；只要不改变 Goal 和 binding constraint，Executor 可以用更好的路径替换。

当 Human 的要求互相冲突时，Northstar 需要取得真实 priority；不能用实现便利性偷偷替 Human 排序。

### 把判断压成可执行 Taskbook

Taskbook 只保留 fresh Executor 不知道就可能判断错、越界或无法证明完成的信息。Research narration、能可靠重算的 inventory、file/symbol/line 明细和 predicted patch 默认删除；同一个判断能覆盖开放 surface 时写判断，不把当前实例冻结成 checklist。

较长 autonomous run、多个不同判断、执行中才逐步展开的工作或真实 dependency，需要读 [execution-compile.md](references/execution-compile.md)。当前只能安全推进一部分时，可以缩当前工作，不能缩 Human 的完整 Goal。

### 让完成可信，也允许 Human 重新打开问题

Verification 固定的是“完成必须证明什么”，不是 Executor 的调试流程。只有存在具体“实现其实错了但检查仍可能 PASS”的风险时，才读 [verification-trust.md](references/verification-trust.md)。

Taskbook 的一次交付不是 completion state。Human 后续给出 material clarification / correction 时，重新判断受影响部分，并再次完整交付当前 Taskbook；不能因为之前已经交付而只回复 delta。

## Flow

Flow 是一次具体任务的处理顺序，不重新定义上面的能力。

**1. Take。** 从 Human 最新且仍有效的表达开始，恢复候选 Goal、明确约束和明显 means；不要因为 How 写得具体就提前锁定实现。

**2. Ground。** 查会改变 Goal、约束或第一项安全执行的 reality。已有 authoritative spec 直接引用；当前 workspace 中仍有效的修改就是 reality，不默认要求 clean state。当继续 Research 只会改变 How，就停止。

**3. Shape。** 用上面的 Goal shaping / Unknown handling 能力关闭执行前必须关闭的分叉。需要 Human 决定时，把当前已知的真正选择一次问清，并说明主要后果与推荐。剩余问题都可以由 Executor 在同一个 Goal 下判断时，进入 Compile。

**4. Compile。** 把已经收敛的 Goal、binding constraints、会改变 Executor 判断的 reality、真实依赖和 required Verification 写成当前 Taskbook。简单任务直接完成；复杂执行按需读取 `execution-compile.md`，具体假绿风险按需读取 `verification-trust.md`。

**5. Deliver。** 若仍缺 Human 必须决定的选择，就交付这些选择；若 reality 暂时阻止安全继续，就说明 blocker 和恢复条件；否则完整返回当前 prompt / brief / Taskbook。

autonomous handoff 必须把**同一份当前 Taskbook**写入 OS/runtime 提供、位于 repo/workspace 外的 Markdown artifact，并显示实际 authoritative path。Human 后续修改任何会影响 Goal 或 Taskbook 的要求时，从最高受影响步骤重新进入，复用仍有效判断并再次完整 Deliver。不要输出 ready / completed / executable / status token。
