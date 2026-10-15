# 旧身份和兼容边界

只在 Evolution Program 要用承接者替换旧 path / authority，或其 real exit / migration boundary 取决于旧模式、标记、配置项、注册名、provider 名称或序列化身份是否仍承担外部契约时读取。

不再驱动当前 runtime，不等于可以删除。旧身份仍可能属于解析、存储、发布、部署或仓库外契约；本地搜索不到使用方，也不能证明它已经失效。

只追踪会改变“当前能否退出、必须保留多久、Program 是否需要 compatibility boundary”的 Evidence。必要时沿“解析 → 存储 → 发布 → 分发 → 观测 → 外部身份”做最小调查，不为完整 inventory 扩大范围。

若 Evidence 表明旧身份对应新的长期 binding compatibility commitment，并会 materially 改变 Target Architecture，回 Architecture Evolution 的 Target judgment；不要为了当前迁移方便直接改写 Target。

用承接者替换旧 path / authority / writer 时，real exit 分两段，顺序不能颠倒：

1. **承接者推全。** 按使用点（入口 × 部署单元 × 生效条件）逐个切到承接者，每个切换单元都有可回退的切换点和等价证明。共存期间旧路径保持可用并作为回退，不修改也不删除。所有使用点都切完，并有 runtime 观测确认，才进入下一段。
2. **旧路径按深度退出。** 由浅到深：回退开关与旧分支 → 旧配置与装载 → 旧代码依赖 → 旧对外身份。每退一层前，先取得该层已无使用的观测 Evidence。退到哪一层属于 Human commitment，未选的层写成非目标。

完成是“承接者推全 + 退到选定深度”；开关打开或承接者可用都不是完成。使用点观测不到（没有能区分新旧路径的 runtime 信号）本身是 Program gap，不能留给验证细节。

这里只判断当前 Program 的 legacy exit / compatibility boundary，不规定兼容实现、迁移任务、发布方式或 backend 命令。behavior/compatibility claim 需要验证时交 `$verify`；它可以选择 DaVinci Replay、test、runtime probe 或其他项目 backend 作为 Evidence source。
