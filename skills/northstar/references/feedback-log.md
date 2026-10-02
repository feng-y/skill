# Feedback Log

本 reference 适用于 Northstar 已承接完整 Intent 的工作；受委托的局部 Intent 问题按 SKILL.md 返回实际 caller，不因此启动 Taskbook execution / learning flow。

Feedback Log 是 material work 的**可选、append-only、跨 session execution-learning artifact**。它把执行 session 的真实 return / observation 与后续 Northstar session 的 judgment / Taskbook delta 串在同一 work identity 下，供未来 Skill / prompt / tool / harness 改进时检索。它不是 Northstar session 内部日志。

它不改变 artifact authority：

- Taskbook 仍是 current Draft、material task state、last Northstar judgment 与 next owner 的唯一 canonical durable surface；
- worker return / PR / real artifact / verifier output 仍是对应 result / Evidence 的 authority；
- Feedback Log 不参与 dispatch、resume、retry、acceptance 或 proof sufficiency；
- `$eval` 仍拥有 agent behavioral measurement；Feedback Log 只是 trace-like input，不是 eval result。

## 什么时候记录

当正常 return / judgment 中的信号**值得跨 session 复用**，或 Human 明确要求独立记录时，再使用此日志；不要求 worker return 与 Northstar judgment 发生在同一 session。值得记录的信号包括：

- Northstar 之前的 judgment、assumption、routing 或 task boundary 被真实 return 明确纠正；
- worker return 暴露了意外且可能重复出现的 friction / missing context / ownership confusion；
- 某个 bounded prompt、handoff、artifact shape 或 context choice 明显减少了歧义、返工或错误判断；
- Taskbook 因 return 发生 material delta，而这个 delta 的原因对未来类似 work 有学习价值。

没有明确记录要求时，不为普通 green return、每次 handoff、命令流水、逐文件修改、test output 或 implementation-local How 写条目。没有 reusable signal 且无明确记录要求就不创建或不追加。

## 放在哪里

优先复用项目已有的 work-artifact / notes 位置；没有现成约定时，与 Taskbook 放在同一目录，使用可推导的 sibling 名称，例如：

```text
<taskbook-stem>.feedback.md
```

仅当本轮确实需要 worker 独立记录时，Northstar 在 scoped instruction / handoff 中携带可定位路径与记录范围，不只给 reference 链接或依赖 worker 继承上下文。普通 dispatch 不预分配路径；意外信号先随正常 return 带回，由接收方按需持久化。不要求 Taskbook 增加 lifecycle field 或每次维护 pointer。

## 最小条目

每次追加只保留本次 writer 已知且相关的字段。worker 不预填 Northstar judgment；Northstar follow-up **另起条目**并关联同一 return identity / pointer，不回填旧条目。

```markdown
## <date/time> — <material task / return identity>

- Worker return: <result / blocker + decisive Evidence / PR / artifact pointer>
- Execution feedback: <worker-side surprise, friction, missing context, or effective pattern>
- Northstar follow-up: <later accepted / revise / blocked judgment + material Taskbook delta, if available>
- Reuse candidate: <what may be worth testing or changing later; "none" is valid>
```

保持 entry 自包含但短。不要复制完整 Taskbook、完整 worker transcript 或 verification output。

## 写入顺序

1. Worker 正常提交 return / Evidence / residual，并附本次可复用信号；已明确要求独立记录时，再按给定路径与范围 append Feedback Log。worker 不写 Taskbook，也不需要等待 Northstar 才能返回。
2. Northstar session 通过宿主 caller-return / handoff / artifact 恢复该 material return，按 current canonical Taskbook 完成 acceptance judgment。
3. Northstar 先更新需要改变的 canonical Taskbook 状态；return 或 judgment 中值得保留的 learning 再进入 Feedback Log。保留 worker observation 的来源；若 worker 已写日志，不重复其条目，有新增 judgment learning 才另起 follow-up。
4. 两侧都没有 reusable signal 且无明确记录要求时不写 Feedback Log。Feedback Log 不能反向驱动 task 状态，也不能因为“值得学习”而阻塞已满足的 work。

## 用于 Skill 改进

Feedback Log 是 observation，不是 remembered answer。

后续维护 Skill 时，可以跨真实 work 检索相关条目和原始 trace / PR / artifact：

- 单条 anecdote 默认只提供 hypothesis；
- recurring 或高影响模式可由 `$eval` 转成有判别力的 Task + Environment + Verifier，或用于解释已有 measurement；
- 只有 measurement / cross-case Evidence 支持稳定 contract gap 时，才改 runtime Skill / prompt / tool / harness；
- 修复后用同一 measurement 重跑；不要把 Feedback Log 自身当作 behavioral uplift 证明。

这样 Feedback Log 保留“执行过程里学到了什么”，但不会演化成新的 evaluator、Graph、状态机或执行控制器。
