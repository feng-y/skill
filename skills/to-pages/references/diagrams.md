# 图表制作与交付

用户已经给出可用的 HTML 或 SVG 时，直接使用现有产物。需要生成图表时，先选定要回答的读者问题。架构、时序、数据流可以直接写 Mermaid。用读者能识别的组件、状态和动作作为标签，用分组和颜色区分阶段，并给关键连线加上触发条件或结果。单张图尽量控制在约 20 条箭头。复杂流程分图，保留失败、回滚和恢复路径。

## 渲染 Mermaid

Pele 主题支持 `blue`、`orange`、`purple`、`yellow`、`teal`、`tan`、`pink` 七种阶段色。给节点加对应的 class，例如：

```mermaid
flowchart LR
  A["收集请求"] -->|"提交"| B["核对输入"]
  B -->|"通过"| C["完成"]
  class A,B teal
  class C blue
```

在执行机器安装 Node.js 20+ 与 npm，例如 Node.js 22。把 `<skill-dir>` 替换为当前 to-pages 的安装目录。

```bash
node "<skill-dir>/scripts/diagram.mjs" setup
node "<skill-dir>/scripts/diagram.mjs" doctor
node "<skill-dir>/scripts/diagram.mjs" render ./chart.mmd --out ./prepared-chart --title "支付流程"
```

`setup` 用锁文件安装 Pele 1.9.0 到 `${XDG_CACHE_HOME:-$HOME/.cache}/to-pages/pele-1.9.0`，使用绝对的 `XDG_CACHE_HOME` 可选择隔离缓存。首次安装可能访问 npm。之后 `doctor` 实际加载 Pele、试渲染并报告 Node 和 Pele 版本，`render` 离线运行。缓存不存在时执行 `setup`。现有缓存损坏时，按照错误提示移走该缓存目录，再执行 `setup`。

输入是 UTF-8 `.mmd`。输出用新目录，保留同名 `.mmd`、生成同名 `.svg`、查看页 `index.html` 和来源校验记录 `render.json`。同一输入和标题会生成相同的文件字节。渲染失败时查看命令输出中的错误和 Mermaid 源文，修正后用同一路径重试。图中的图像文件引用会破坏 SVG 的独立性，出现此错误时检查源文中的图像节点。

渲染使用 pstack statechart 的 Pele 参数 `{ limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 }` 以及完整的浅色和深色主题。主题 CSS 与上游代码块逐字节一致。版本、来源、SHA-256 和 MIT 声明随 `render.json` 交付。[上游 render.md](https://github.com/michael-denyer/pstack-claude/blob/103a68d9a9aa23759d00ad95b01cb78cb8f57772/plugins/pstack/skills/statechart/references/render.md) · [Pele API](https://pele.run/api)。

打开输出目录的 `index.html` 可查看图和 Mermaid 源文。Fit 把全图缩进画布，Reset 恢复 100%，Full-size SVG 在新标签页以 100% 打开图。聚焦画布后可按 `+`、`-`、`0`、`F` 操作，也可用方向键滚动放大的图。页面只读本目录资源，SVG 本身跟随浏览器明暗偏好。随报告发布时保留相对路径，也可在已有 HTML 中以 `<img src="…">` 引用生成的 SVG。

## 建模与检查状态行为

对有正确性要求的状态行为、协议或故障路径，使用上游 pstack statechart 工作流。先定位并读取实际安装里的 `SKILL.md` 与它指向的参考资料。

1. 如果设置了 `TO_PAGES_STATECHART_DIR`，先检查该目录。未设置时先检查 `$HOME/.local/share/to-pages/statechart`。
2. 查找已安装 pstack 插件的 `skills/statechart/SKILL.md`。常见位置在 `$HOME/.codex/plugins/cache/*/pstack/*/` 或 `$HOME/.claude/plugins/cache/*/pstack/*/`。确认实际路径和内容后再调用其中的脚本。
3. 缺少上游 skill 时，可从固定提交安装原版到个人数据目录。目标目录需要是新目录。已有安装时可另选目录，并用 `TO_PAGES_STATECHART_DIR` 指向该目录。

```bash
statechart_rev=103a68d9a9aa23759d00ad95b01cb78cb8f57772
statechart_tmp="$(mktemp -d)"
statechart_dest="${TO_PAGES_STATECHART_DIR:-$HOME/.local/share/to-pages/statechart}"
statechart_source="pstack-claude-$statechart_rev/plugins/pstack"
curl -fL "https://codeload.github.com/michael-denyer/pstack-claude/tar.gz/$statechart_rev" \
  -o "$statechart_tmp/pstack.tar.gz" &&
tar -xzf "$statechart_tmp/pstack.tar.gz" -C "$statechart_tmp" \
  "$statechart_source/skills/statechart" "$statechart_source/LICENSE" &&
mkdir -p "$(dirname "$statechart_dest")" &&
mkdir "$statechart_dest" &&
cp -R "$statechart_tmp/$statechart_source/skills/statechart/." "$statechart_dest/" &&
cp "$statechart_tmp/$statechart_source/LICENSE" "$statechart_dest/UPSTREAM-LICENSE"
```

按上游说明写 `.tla`、`.cfg` 和 view 模块，明确不变量、抽象范围和读者看到的状态与动作。用上游脚本运行 TLC，检查 `report.md` 和 TLC 原始输出，阅读实际生成的 `chart.mmd`。分组、合并状态或拆图时保留故障路径、规则关联和 `breaks`、`mayBreak`、`bugPath`、`repeats` 标记。对真实代码的故障路径，按报告逐步复现。注明抽象和未检查的规则。

上游启动器选择受支持的 Node.js、Bun 或 Deno。使用 Node.js 22 时需 22.18+。它可通过 mise 首次安装 Java 和 TLC。已有 Java 11+ 与 TLC 1.7.4 时可指定路径直接运行。若当前机器已有 `$HOME/.local/share/to-pages/statechart-env.sh`，可用 `source "$HOME/.local/share/to-pages/statechart-env.sh"` 加载配置好的 PATH、JAVA 和 TLA2TOOLS，再执行相同的 statechart 命令。

```bash
statechart_dir="${TO_PAGES_STATECHART_DIR:-$HOME/.local/share/to-pages/statechart}"
JAVA=/path/to/java TLA2TOOLS=/path/to/tla2tools.jar \
  "$statechart_dir/scripts/statechart" ./Spec.tla --config ./Spec.cfg --view ./view.mjs --out ./model-run
node "<skill-dir>/scripts/diagram.mjs" render ./model-run/chart.mmd --out ./prepared-chart
```

如果上游运行失败或没有生成 `chart.mmd`，交付实际报告和可核对的错误或覆盖范围。TLC 检查结论以实际运行报告和原始输出为据。保留 `.tla`、`.cfg`、view、报告和 TLC 输出以供复跑。仅在逐项确认公开范围后，把适合公开的文件纳入发布目录，检查可下载的 Mermaid 源文及 SVG 标签。参考 [pstack statechart](https://github.com/michael-denyer/pstack-claude/tree/103a68d9a9aa23759d00ad95b01cb78cb8f57772/plugins/pstack/skills/statechart) 和 [TLC 1.7.4](https://github.com/tlaplus/tlaplus/releases/tag/v1.7.4)。
