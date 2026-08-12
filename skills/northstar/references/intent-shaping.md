# Intent Shaping under uncertain territory

只在主 Skill 的 `Shape` 仍无法从当前输入形成稳定 Goal，或明显存在会改变 Goal / boundary / authority 的 blind spot 时读取。这里不重复 Unknown routing；routing 仍由 `SKILL.md` 拥有。

## Map is not territory

Human 的 prompt、已有 plan 和本 Skill 都只是 map；repo、运行环境、历史约束和真实使用者才是 territory。不要因为 map 写得详细就假设 Unknown 已关闭，也不要为了理论上的完整性穷尽所有 Unknown。

只寻找**会改变 Stable Goal 的 Unknown**。优先检查这些容易被 prompt 漏掉、但会改变完成后世界的地方：

- tacit business / compatibility / risk constraint；
- 已有 authoritative spec、precedent、reference implementation 或历史决定；
- “什么算好”的 quality bar / acceptance authority；
- repo 外 consumer、serialized/config identity、部署或授权边界；
- 同名概念在 repo 中指向不同 live responsibility 的 collision；
- 当前 working tree / 已完成但未验证 work 与 Human Goal 的真实关系。

这些只是 blind-spot lens，不是每次固定 checklist。发现一个候选后先问：**它若取不同值，会不会改变主 Skill 已定义的 Goal contract？** 不会就留给 Executor 或忽略。

## Smallest decisive probe

能由 repo/runtime authority 关闭的 Unknown，用最小 decisive probe 关闭，而不是问 Human。优先取得能够区分 materially different Goal 的 Evidence；不要为了“了解更多”扩大 Research。

Reality 可以推翻模型推荐的 means，但不能替 Human 改 outcome。Human 明确的 priority、boundary、authorization 或 verification requirement 仍保持 authority。

## Stable Goal closure

使用 `SKILL.md` 的 Goal contract 作为唯一 closure 标准。若两个 materially different completed worlds 仍都符合当前 Human 表达，而且 repo/upstream authority 不能决定，就把差异、后果与推荐一次交给 Human；不要拿一个 implementation How 偷填。

若剩余 Unknown 已可在稳定 Goal / priority / boundary 下由 Executor 根据 live Evidence 裁决，**停止 Intent Research 并 Compile**。Planning 不需要、也不应该提前消灭 implementation 中才会出现的 Unknown。
