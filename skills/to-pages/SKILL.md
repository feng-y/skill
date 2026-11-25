---
name: to-pages
description: 将本地 HTML 或静态目录推送到配置的 GitHub 仓库，由 Cloudflare Pages 或 Workers 静态资源托管，并核对公网内容。用于 to-pages、发布静态报告到 Cloudflare、更新已发布报告。
---

# to-pages

将用户选定的静态报告发布到配置的 GitHub 仓库，由已连接的 Cloudflare 项目自动部署，返回核对过的公网链接。用户要求发布即授权该次发布。仅安装或修改 skill 时执行只读检查，不推送测试页面。

首次使用、凭证缺失或 Cloudflare 尚未连接时，读取 [README.md](README.md) 中的配置说明。默认配置为当前用户的 `$HOME/.config/to-pages/config.json`。沿用实际配置的仓库、生产分支和站点地址，不从机器用户名或仓库名推断目标。

## 准备报告

- 确认源文件和目标路径。新报告使用 `reports/<slug>`。已有报告用 `catalog` 查主题 ID、路径和版本。为同一主题保留新版本时指定原 `--topic` 和新路径，脚本自动分配版本号。
- 单个 HTML 的外部本地资源不会自动收集。包含资源时准备只含发布内容的目录，保留相对路径，并包含 `index.html`。
- HTML 源文件使用 UTF-8。脚本为发布副本补齐编码声明和「返回导航」链接，保留源文件、资源基准地址和 CSP。回链通常指向当前域名的站点首页。若报告含有效的 `<base href>` 且脚本被禁用或被 CSP 阻止，回链使用配置的生产首页。
- 检查 HTML、注释、JSON 和资源是否允许公开，排除凭据及未授权的内部数据。脚本的文件名检查不能替代内容检查。
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

`verified` 才表示公网内容已逐个核对，`pushed` 只表示 GitHub 接收成功。Cloudflare 转换 HTML 导致字节不同时，明确说明未通过字节核对；不能称为验证成功。最终返回已验证的页面链接；若未完成，说明阻塞并附已推送的提交链接。
