# Legacy Architecture Lenses

只在当前 Architecture Intent 涉及历史 mode、compat token、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时读取。不要把 legacy 检查变成默认流程。

## Compat is not runtime behavior

接受的语法、token 或 identity 不等于仍然存在的 runtime 语义。一个 compat token 即使不再驱动运行时，也可能因为 parse、serialization、deployment 或 identity 继续存在。

判断 retirement 时分别确认：

- 它是否仍影响 runtime behavior；
- 它是否仍属于 parse / serialization contract；
- 它是否仍暴露给 deployment、registration 或 repo 外消费者。

## Search absence is not death proof

本地搜索没有 reader，不足以证明 config key、provider identity、registration、serialized type 或 loader name 可以删除。身份可能通过 generated config、indirect registration、deployment metadata 或 repo 外系统传播。

只有当前 intent 的 rename、delete 或 replacement/exit 依赖该 identity 时，才把 repo 外可见性升级为 material unknown 并要求最小证据关闭；否则将 identity 放入 `Must preserve` 或 out of scope，不让未知范围无界扩张。

## Retirement propagation trace

只有当旧意义可能跨阶段传播时，按需追踪：

```text
parse → storage → publication → dispatch → observation → identity
```

不要求每个 intent 都完整走一遍；只检查会改变 intent、boundary 或 replacement/exit 判断的链路。

## Guard

Legacy lens 只用于防止错误删除和错误语义判断。它不拥有迁移计划、兼容策略或执行流程；这些属于后续 design / implementation。
