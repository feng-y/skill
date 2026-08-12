# Architecture Judgment Details

只在主 Skill 的高层 architecture judgment 仍不足以区分当前 case 时读取。本文件只提供难判 discriminator / counterexample，不拥有第二套 Flow、architecture model 或输出 contract。

## Architecture or local

局部坏味道只有在它迫使长期 responsibility、dependency、abstraction boundary 或旧 authority/path 改变时才升级为 architecture pressure。文件大小、目录形状、switch/duplication 数量和一次 change locality 都不能单独证明。

## Stable variation

provider/specific boundary 必须由长期且重要的 semantic、contract、lifecycle、performance architecture 或 deployment difference 支撑。当前 class/provider/mode/consumer partition、代码相似度和“未来可能扩展”都只是 Evidence。差异只来自 historical representation 时优先消除；差异会长期改变责任或约束时才保留 specific。

## Real fork

不要把 naming、class shape、registry/facade 选择等 representation 差异当成 architecture alternatives。只有长期 layering、module boundary、abstraction/specific 或 primary-responsibility placement 不同，才是 materially different fork。repo/runtime 能关闭的 decisive fact 先 probe；真正 Human-owned 的 business/compat/risk/long-term commitment 才需要 Human decision。

## Altitude / unknowns

只有会改变 architecture-vs-local、Target Architecture 或 real evolution 的 unknown 才阻塞。AE 可以固定 architecture-level outcome 与 structural done condition；除非 representation 本身被 authority 绑定，不固定 class/API/file/schema/call shape/task/test provider。其他 unknown 留给 Implementation Design / execution。
