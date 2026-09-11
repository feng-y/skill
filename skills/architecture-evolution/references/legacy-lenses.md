# 旧身份和兼容边界

只在 Evolution Program 的 real exit / migration boundary 取决于旧模式、标记、配置项、注册名、provider 名称或序列化身份是否仍承担外部契约时读取。

不再驱动当前 runtime，不等于可以删除。旧身份仍可能属于解析、存储、发布、部署或仓库外契约；本地搜索不到使用方，也不能证明它已经失效。

只追踪会改变“当前能否退出、必须保留多久、Program 是否需要 compatibility boundary”的 Evidence。必要时沿“解析 → 存储 → 发布 → 分发 → 观测 → 外部身份”做最小调查，不为完整 inventory 扩大范围。

若 Evidence 表明旧身份对应新的长期 binding compatibility commitment，并会 materially 改变 Target Architecture，回 Architecture Evolution 的 Target judgment；不要为了当前迁移方便直接改写 Target。

这里只判断当前 Program 的 legacy exit / compatibility boundary，不规定兼容实现、迁移任务、发布方式或 backend 命令。behavior/compatibility claim 需要验证时交 `$verify`；它可以选择 DaVinci Replay、test、runtime probe 或其他项目 backend 作为 Evidence source。
