# Architecture Program Contract

只在 `Status: Architecture decision ready` 时读取。Compile 的目标是把完整 reasoning 压成薄 Architecture Program，让下游无需重新发现 architecture why；不规定固定 Markdown 章节。

已有 authoritative repo SOT 定义稳定事实时直接引用；Program 只携带新的 architecture judgement / structural delta。若 SOT 本身要变，明确修改该 authoritative source，不建立平行规范。

Program 只需要回答：

- **Target delta** — current → target 的关键 layer/dependency、capability/responsibility、abstraction/specific 变化；
- **Long-lived invariants** — 后续演进仍应保持的少量 architecture boundary；
- **Top Improvements** — 最多 3 个，不补数；按 structural leverage 排序。每个必须说明 structural change、architecture gain、real exit、structural done condition，并在完成时独立让当前结构变好；
- **Route / completion** — 只保留 improvements 之间真实的 architecture dependency，以及整体完成后哪些旧结构不再 authoritative。

research/knowledge task、future wish、纯铺路 abstraction/bridge 或 implementation step 不能冒充 improvement；若缺失 evidence 会决定某个 change 是否真改善结构或改变推进依赖，返回 `Status: Architecture unresolved`。

删除 Research trace、完整 alternatives/Brooks 过程、普通 unknown、文件 inventory 与 implementation detail。除非 representation 本身是 authoritative invariant，不固定 class/API/file/schema/call implementation/MR/task/test provider。
