---
name: prototype
description: "Deprecated compatibility alias for Beacon. Existing callers that still invoke $prototype should immediately delegate the bounded concrete-shaping question to $beacon; new routing must use Beacon directly."
---

# Prototype · deprecated compatibility alias

`prototype` 不再拥有独立 Skill Identity。当前 canonical owner 是 `$beacon`。

若旧 caller 仍调用 `$prototype`：

1. 保留 caller 原有 semantic ownership；
2. 将同一个 bounded/local concrete-shape question 交给 `$beacon`；
3. 把 Beacon 的 concrete artifact / correction / Evidence 返回原 caller。

不要在这里重新解释、扩展或组合完整 Intent。Prototype 只是迁移期兼容入口；prototype / mock / minimal implementation 仍可以作为 Beacon 的一种 implementation technique，但不再定义顶层 Skill 语义。
