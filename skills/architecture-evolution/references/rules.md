# Architecture Judgment Details

只在主 Skill 的高层判断仍不足以区分当前 case 时读取；这里只提供 discriminator，不拥有第二套 Flow/model/output contract。

- **Architecture or local**：局部坏味道只有迫使长期 responsibility/dependency/abstraction boundary/旧 authority-path 改变时才升级；文件大小、目录形状、switch/duplication、一次 change locality 都不能单独证明。
- **Stable variation**：specific/provider boundary 必须由长期 semantic/contract/lifecycle/performance architecture/deployment difference 支撑；当前 taxonomy、代码相似度和未来扩展愿望都只是 Evidence。
- **Real fork**：只有长期 layering、module boundary、abstraction/specific 或 primary-responsibility placement 不同才是 architecture alternative；representation 差异不是。
- **Altitude / unknowns**：只有会改变 architecture-vs-local、Target Architecture 或 real evolution 的 unknown 才阻塞；其他 unknown 与 concrete representation 留给 Implementation Design / execution。
