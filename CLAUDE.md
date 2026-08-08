# Claude repo guidance

修改本 repo 前先读取根目录 [AGENTS.md](AGENTS.md)。`AGENTS.md` 是 repo-level evolution / context-engineering 规则的唯一 SOT。

不要把这些 repo mutation rules 复制进单个 Skill；Skill runtime 只保留自己的领域 invariant，具体 case 留在 validation / regression。
