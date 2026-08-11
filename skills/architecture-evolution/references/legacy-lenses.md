# Legacy Architecture Lenses

只在当前 Architecture Decision 涉及历史 mode、compat token、旧 config/registration、loader/provider identity、serialized identity 或 residual state 时读取。不要把 legacy 检查变成默认流程。

## Compat is not runtime behavior

接受的语法、token 或 identity 不等于仍然存在的 runtime 语义。一个 compat token 即使不再驱动运行时，也可能因为 parse、serialization、deployment 或 identity 继续存在。

判断 retirement 时分别确认：

- 它是否仍影响 runtime behavior；
- 它是否仍属于 parse / serialization contract；
- 它是否仍暴露给 deployment、registration 或 repo 外消费者。

## Search absence is not death proof

本地搜索没有 reader，不足以证明 config key、provider identity、registration、serialized type 或 loader name 可以删除。身份可能通过 generated config、indirect registration、deployment metadata 或 repo 外系统传播。

只有当前 decision 的 authority/identity retirement 或 replacement/exit 依赖该 identity 时，才把 repo 外可见性升级为 Material Unknown 并要求最小证据关闭；否则将 identity 放入 must-preserve 或 out of scope，不让未知范围无界扩张。

## Retirement propagation trace

只有当旧意义可能跨阶段传播并影响 architecture decision / evolution 时，按需追踪：

```text
parse → storage → publication → dispatch → observation → identity
```

不要求每个 case 都完整走一遍；只检查会改变 Target Architecture、boundary、authority transition 或 replacement/exit 判断的链路。

## Guard

Legacy lens 只帮助判断哪些 identity / authority 能否退休，以及 architecture-level transition 是否需要保留 compat boundary。它不规定具体兼容实现、迁移 task、发布步骤或验证流程；这些属于后续 Implementation Design / execution。
