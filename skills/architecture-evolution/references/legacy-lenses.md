# Legacy Architecture Lenses

只在 architecture judgment 涉及旧 mode/token/config/registration/provider/serialized identity 时读取。

兼容 identity 不等于 runtime behavior；即使不再驱动运行时，也可能仍属于 parse/serialization/deployment/repo 外 contract。本地 search absence 不能证明它已死亡。

只有 identity/authority retirement 会改变 Target Architecture 或 real exit 时，才做最小 probe；否则 must-preserve 或 out of scope。必要时按 `parse → storage → publication → dispatch → observation → identity` 追踪，只查会改变当前 judgment 的链路。

本 lens 只判断 identity/authority 能否退休及是否需保留 compat boundary，不规定兼容实现、迁移 task、发布或验证流程。
