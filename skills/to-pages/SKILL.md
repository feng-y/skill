---
name: to-pages
description: 将本地 HTML 或静态目录推送到配置的 GitHub 仓库，由 Cloudflare Pages 或 Workers 静态资源托管，并核对公网内容。用于 to-pages、发布静态报告到 Cloudflare、更新已发布报告。
---

# to-pages

将用户选定的静态报告发布到配置的 GitHub 仓库，由已连接的 Cloudflare 项目自动部署，返回核对过的公网链接。用户要求发布即授权该次发布。仅安装或修改 skill 时执行只读检查，不推送测试页面。

首次使用、凭证缺失或 Cloudflare 尚未连接时，读取 [README.md](README.md) 中的配置说明。默认配置为当前用户的 `$HOME/.config/to-pages/config.json`。沿用实际配置的仓库、生产分支和站点地址，不从机器用户名或仓库名推断目标。

## 准备报告

- 确认源文件和目标路径。新报告使用 `reports/<slug>`。已有报告用 `catalog` 查主题 ID、路径和版本。为同一主题保留新版本时指定原 `--topic` 和新路径，脚本自动分配版本号。
- 已有可用的 HTML 或 SVG 直接使用。需要生成图表时，读取 [图表制作与交付](references/diagrams.md)，用其中的渲染工具保留 Mermaid 源文和 SVG。架构、时序和数据流可直接写 Mermaid。涉及需检查正确性的状态行为、协议或故障路径时，按实际安装的 pstack statechart 工作流生成并检查模型、报告和图，再渲染。
- 单个 HTML 的外部本地资源不会自动收集。包含资源时准备只含发布内容的目录，保留相对路径，并包含 `index.html`。
- HTML 源文件使用 UTF-8。脚本为发布副本补齐编码声明和「返回导航」链接，保留源文件、资源基准地址和 CSP。回链通常指向当前域名的站点首页。若报告含有效的 `<base href>` 且脚本被禁用或被 CSP 阻止，回链使用配置的生产首页。
- 先在原始材料之外做可公开的副本：正文、注释、JSON、截图等均替换真实人员、内部系统、工单和会话内容；优先用合成数据重拍。必须使用截图时，裁剪或实色遮盖后导出为无图层、无元数据的新图片，别把原图放进发布目录。只对最终副本执行发布前复核。
- 运行 `preflight`。脚本拦截能识别的凭据、内网主机名、非示例邮箱；图片、SVG、其他不透明附件及常见内嵌媒体须复核。只有人工看过最终文件、确认可公开后，才把同一份清单传给 `plan` 和 `push/publish`。Hash 只绑定文件，不能证明内容无敏感信息。操作见 [README.md](README.md#发布前脱密)。
- 源文件仍在修改时，固定本次发布快照，以该快照核对，说明发布版本，不循环追赶其他进程的修改。

## 推送与核对

将 `<skill-dir>` 替换为当前 `SKILL.md` 所在目录。

```bash
python3 <skill-dir>/scripts/to_pages.py doctor
python3 <skill-dir>/scripts/to_pages.py plan /path/report.html --path reports/topic
python3 <skill-dir>/scripts/to_pages.py publish /path/report.html --path reports/topic
```

首次发布新主题时，根据用户指定或内容用途选择分类，优先使用「设计原型」「技术方案」「分析报告」「使用文档」；依据不足时使用「未分类」。通过 `--title`、`--category`、`--project` 保存显示信息，已有主题沿用已记录的分类，不因再次发布重新猜测。按需要用 `--summary` 记录版本变更。用户授权更新原路径时加 `--replace`，其他版本仍可打开。

脚本在同一提交中更新报告、目录元数据和受管理的月度首页。首页支持分类、搜索、分页和版本选择。自定义首页保留原样。权限、保护分支或并发 push 错误需检查后处理，不 force push，不改用其他站点或其他身份。目录格式与历史迁移见 [README.md](README.md)。

用户只要求 GitHub 推送时使用 `push`。报告含有效的 `<base href>` 时，`push` 也需要配置 `cloudflare.base_url`。若已连接 Cloudflare，推送仍会触发自动部署。

```bash
python3 <skill-dir>/scripts/to_pages.py push /path/report.html --path reports/topic
```

脚本默认使用 token 通过 HTTPS 推送。HTTPS 传输失败时，可使用目标机器上已配置且核实为同一 GitHub 账号的 SSH 凭证完成推送，并核对远端文件。SSH 成功不能证明 token 有写权限，`doctor` 返回的仓库角色也不能证明 token 的写入范围。

`publish` 会核对准备后的报告、资源和受脚本管理的导航首页，内容相同而未产生新提交时也会核对。等待超时后可用 `verify` 只读核对所选报告及其资源。

```bash
python3 <skill-dir>/scripts/to_pages.py verify /path/report.html --path reports/topic --timeout 300
```

`verified` 才表示公网内容已逐个核对，`pushed` 只表示 GitHub 接收成功。Cloudflare 转换 HTML 导致字节不同时，明确说明未通过字节核对；不能称为验证成功。成功后，最终回复必须以可点击的完整公网链接收尾：发布报告返回已验证的报告链接，仅重建导航返回已验证的首页链接，不只返回状态、路径或提交号。若未完成，说明阻塞并附已推送的提交链接。
