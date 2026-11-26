# to-pages 配置与使用

把 HTML 报告或静态目录推送到 GitHub，由 Cloudflare Pages 或 Workers Builds 自动部署。脚本使用 Python 3.10+ 标准库和 Git，支持 Mac 与 Linux。

## 安装

从 skill 管理仓库安装：

```bash
npx skills@latest add feng-y/skill --skill to-pages
```

下文的 `<skill-dir>` 指安装后的 `to-pages` 目录。常见路径为 `$HOME/.codex/skills/to-pages` 或 `$HOME/.agents/skills/to-pages`，也可以在本仓库使用 `skills/to-pages`。

## 创建配置

默认配置路径为：

```text
$HOME/.config/to-pages/config.json
```

`~/.config/to-pages/config.json` 表示同一路径。Mac 和远程机器分别读取各自用户的配置。Shell 中用双引号展开 `$HOME`，不要写成 `'$HOME'`。

复制[配置模板](references/config.example.json)，然后填写实际站点地址：

```bash
mkdir -p "$HOME/.config/to-pages"
chmod 700 "$HOME/.config/to-pages"
cp -n <skill-dir>/references/config.example.json "$HOME/.config/to-pages/config.json"
chmod 600 "$HOME/.config/to-pages/config.json"
```

模板的 `cloudflare.base_url` 留空。下面是 lemon-pages 站点的完整配置示例。发布到其他站点时替换仓库和地址。

```json
{
  "github": {
    "repo": "feng-y/lemon-pages",
    "branch": "main",
    "token_env": "GITHUB_TOKEN"
  },
  "cloudflare": {
    "base_url": "https://pages.lemonyhn.top",
    "output_dir": "public"
  }
}
```

| 字段 | 用途 |
| --- | --- |
| `github.repo` | `owner/name`，不是 GitHub URL。 |
| `github.branch` | 推送分支，默认 `main`，应与 Cloudflare 生产分支一致。 |
| `github.token_env` | 凭证环境变量名，默认 `GITHUB_TOKEN`。 |
| `github.token_file` | 可替代 `token_env`。纯文本凭证文件，可用绝对路径；相对路径基于配置文件目录。 |
| `github.token` | 可替代环境变量或文件，直接放在配置中。配置文件必须归当前用户所有且权限为 `600`。 |
| `cloudflare.base_url` | 实际生产 HTTPS 地址。站点挂载在子路径时包含该路径。支持 `pages.dev`、`workers.dev` 或自定义域名。 |
| `cloudflare.output_dir` | 仓库内的静态目录，默认 `public`。根目录用 `.`，此时报告目录元数据也可能被托管。 |

`token_env`、`token_file` 和 `token` 只能配置一个。环境变量方式不会把 Token 复制到配置文件或仓库。凭证文件也必须归当前用户所有且权限为 `600`。

如果 Token 存在于文件 `$HOME/.config/to-pages/github-token`，可以将 `github` 替换为以下对象：

```json
{
  "repo": "feng-y/lemon-pages",
  "branch": "main",
  "token_file": "github-token"
}
```

运行脚本的进程必须能读取配置的凭证来源。在交互 shell 中存在的变量，不一定存在于 SSH 或定时任务的非交互 shell 中。不要打印 Token，也不要提交本机 `config.json` 或凭证文件。

可用 `TO_PAGES_CONFIG` 覆盖配置路径，或将 `--config /path/config.json` 放在子命令前：

```bash
python3 <skill-dir>/scripts/to_pages.py --config /path/config.json doctor
```

## GitHub 权限

创建或选择目标仓库，并让 fine-grained Token 可以访问该仓库，授予 `Contents: Read and write`。创建仓库的权限与内容写权限分别控制；脚本不会创建 GitHub 仓库。

仓库可以为空。首次推送会创建配置的分支。非空仓库缺少该分支时，脚本会停止，要求核对配置。

`doctor` 会实际读取 GitHub 用户和仓库。它输出的 `repository_role_push` 是账号的仓库角色，不证明 Token 有写入范围。实际 push 才验证当前凭证的写入能力。

## 连接 Cloudflare

选择一种托管方式，并让 Cloudflare 连接同一 GitHub 仓库。首次 GitHub App 授权需要在 Cloudflare 控制台完成，只有 `GITHUB_TOKEN` 不足以授权 Cloudflare 账户。完成连接后，日常发布不需要本机 Cloudflare API Token。

### Cloudflare Pages

在 **Workers & Pages > Create application > Pages > Connect to Git** 选择仓库。

| 设置 | 值 |
| --- | --- |
| Production branch | `github.branch` 的值，例如 `main`。 |
| Framework preset | None。 |
| Build command | `exit 0`。 |
| Build output directory | `cloudflare.output_dir` 的值，例如 `public`。 |
| Root directory | 留空，使用仓库根目录。 |

保存并部署，将生成的生产 URL 写入 `cloudflare.base_url`。Direct Upload 项目不能直接切换为 Git integration；需要 Git 集成时另建项目。

### Cloudflare Workers 静态资源

已有 Worker 时可继续使用 Workers Builds。连接仓库，生产分支与配置一致，构建命令留空，根目录为 `/`。

lemon-pages 的部署命令为：

```bash
npx wrangler deploy --assets ./public --name lemon-pages --compatibility-date 2026-11-23
```

其他项目需替换 Worker 名称和静态目录。兼容日期应使用 Cloudflare 支持的日期。`--assets` 指定站点目录；未提供兼容日期时 Wrangler 会拒绝上传。也可在仓库自己的 Wrangler 配置中声明这些设置。

保存后重新构建，检查构建结果，将实际生产地址写入 `cloudflare.base_url`。

## 生成图表

已有 HTML 或 SVG 可直接用于发布。图表助手使用 Node.js 20+，首次 `setup` 需要 npm。

```bash
node "<skill-dir>/scripts/diagram.mjs" setup
node "<skill-dir>/scripts/diagram.mjs" doctor
node "<skill-dir>/scripts/diagram.mjs" render ./chart.mmd --out ./prepared-chart
```

输出目录包含查看页、原始 Mermaid、跟随系统明暗偏好的 SVG 和来源校验记录。确认其中的所有内容都允许公开后，可把该目录作为静态报告发布。生成图表的详细流程、pstack statechart 安装与 TLC 说明见 [图表制作与交付](references/diagrams.md)。日常静态发布使用 Python 和 Git。

## 发布报告

单个 HTML 会保存为目标目录的 `index.html`。带图片、CSS 或脚本时使用静态目录，并在其中提供 `index.html`。脚本会递归上传该目录，不会自动收集 HTML 引用的外部本地资源。

HTML 源文件使用 UTF-8。脚本在发布副本中补齐编码声明和「返回导航」链接。从同域名的首页打开报告时，回链会保留首页筛选和页码。若报告含有效的 `<base href>` 且脚本被禁用或被 CSP 阻止，回链使用 `cloudflare.base_url` 指定的生产首页。源文件、非 HTML 资源以及报告原有的资源基准地址和 CSP 均保留原样。

```bash
python3 <skill-dir>/scripts/to_pages.py doctor
python3 <skill-dir>/scripts/to_pages.py plan /path/report.html --path reports/topic
python3 <skill-dir>/scripts/to_pages.py publish /path/report.html --path reports/topic
```

例如 `--path reports/topic` 的页面位于站点地址下的 `reports/topic/`，对应仓库中的 `public/reports/topic/index.html`。`--path` 相对于站点目录，不要重复包含 `public`。

授权更新已有报告时使用 `--replace`：

```bash
python3 <skill-dir>/scripts/to_pages.py publish /path/static-dir --path reports/topic --replace
```

脚本保留其他报告和目标目录里的旧资源。相同内容不会创建新提交。并发 push 被拒时，重新检查远端变更，再预览和推送，不 force push。

仅推送到 GitHub 时使用 `push`。报告含有效的 `<base href>` 时，`push` 也需要配置 `cloudflare.base_url`。

```bash
python3 <skill-dir>/scripts/to_pages.py push /path/report.html --path reports/topic
```

等待 Cloudflare 部署超时后，只读核对所选报告及其资源。

```bash
python3 <skill-dir>/scripts/to_pages.py verify /path/report.html --path reports/topic --timeout 300
```

`publish` 和 `verify` 需要配置站点地址。两条命令逐字节核对准备后的报告及资源，`publish` 还会核对受脚本管理的导航首页。核对失败时返回非零退出码。

## 主题与版本

`catalog` 只读查询目标分支的已登记主题、分类、报告路径和版本。发布前可用它确认已有主题的 ID。

```bash
python3 <skill-dir>/scripts/to_pages.py catalog
python3 <skill-dir>/scripts/to_pages.py publish /path/rook.html --path reports/rook \
  --topic rook --title "Rook 部署方案" --category "技术方案" --project Rook --summary "首次发布"
python3 <skill-dir>/scripts/to_pages.py publish /path/rook-updated.html --path reports/rook-v2 \
  --topic rook --summary "补充回滚步骤"
```

`plan`、`push` 和 `publish` 接受相同的可选元数据。

| 参数 | 用途 |
| --- | --- |
| `--topic` | 稳定的主题 ID。同一主题用相同 ID 与不同报告路径。省略时，已有路径沿用登记的 ID，新路径创建独立主题。 |
| `--title` | 主题标题。新主题默认取报告的 `<title>`、首个 `<h1>` 或路径。主题描述取首次登记时的 HTML 描述或与标题不同的首个 `<h1>`。 |
| `--category`、`--project` | 主题分类和项目。新主题缺少分类时使用「未分类」，已有主题沿用已登记字段。 |
| `--version` | 主题内唯一的版本标签。新路径默认分配下一个 `vN`；既有路径沿用标签。 |
| `--summary` | 当前版本的变更说明。 |

同一主题的两个版本各有自己的 URL。加 `--replace` 会更新所选路径的报告和资源。需要继续打开旧正文时，用新路径发布新版本。旧路径和已使用的版本标签不能改派。仅改元数据时保留报告日期。重复提交相同发布内容和元数据时沿用已有提交。

## 导航首页

受管理的首页按主题最新更新时间归档，月份和时间使用 UTC，每页 20 个主题。点单版本标题直接打开报告。多版本标题和版本数按钮都会打开版本选择，按发布时间排列，同一时间优先显示后登记的版本。在地址中保留月份、分类、搜索和页码。禁用 JavaScript 时仍可通过静态链接打开报告。

首页缺失时，脚本创建带 `<!-- to-pages:managed-index -->` 标记的首页。后续发布更新带标记的首页，自定义首页保留。可以在不发布报告的情况下初始化或重建目录和受管理的首页。

```bash
python3 <skill-dir>/scripts/to_pages.py index plan
python3 <skill-dir>/scripts/to_pages.py index publish
```

`index push` 仅推送 Git 提交。目标分支尚无目录时，读取得到空目录；未登记的报告仍在首页各自展示，归为「未分类」和「时间未记录」，标题或路径后缀相同也会独立展示。

## 目录格式与历史迁移

`.to-pages/catalog.json` 位于仓库根目录。静态目录用 `public` 等子目录时，目录文件留在静态资源外。静态目录用 `.` 时，文件和资源同处仓库根目录，可能被公开托管。目录的标题、描述、分类、项目、摘要等都是公开内容；凭证保存在各机器的配置或环境变量中。

格式为 `schema: 1`，包含 `output_dir` 和 `topics`。主题字段为 `id`、`title`、`description`、`category`、`project` 和 `versions`。每个版本有 `label`、`path`、`published_at`、`updated_at`、`digest` 和 `summary`。路径相对静态目录，填写报告目录，省略末尾斜线和 `index.html`。日期用 ISO 8601 UTC 时间或 `null`。以该版本首次与最后一次已证实的发布为准；只有可靠历史证据时才为旧版本补日期。目录记录的主题描述、分类和版本归属也需有证据，未核实的旧报告可继续由首页发现。

在站点检出目录里迁移时，将 `scripts/` 加入 Python 导入路径，调用 `catalog.load_catalog(repo, output_dir)` 读取已有记录，按可靠历史补日期和关联。用 `catalog.content_digest(files)` 计算已发布文件集合的内容摘要，`files` 为 report-relative 文件名到实际发布字节的映射（摘要为这些文件名及逐文件 SHA-256 的 SHA-256）。`catalog.write_catalog(repo, catalog)` 校验实际报告路径并写入目录。调用 `navigation.render_homepage(repo / output_dir, catalog=catalog)` 生成首页字节；返回 `None` 表示当前是自定义首页。检查各版本的实际链接和 Git diff，再将目录和首页一同提交。

## 验证与排错

运行脚本测试，不访问真实 GitHub 或 Cloudflare，也不会发布测试页面：

```bash
python3 <skill-dir>/scripts/test_to_pages.py -v
```

运行过图表助手的 `setup` 后，可运行 `node --test "<skill-dir>/scripts/diagram.test.mjs"` 验证渲染。

| 现象 | 检查项 |
| --- | --- |
| `GitHub token missing` | 当前进程是否加载了环境变量，或能读取配置的凭证文件。 |
| GitHub 返回 403 | Token 是否包含目标仓库，并有 `Contents: Read and write`；账号角色不能代替 Token 权限。 |
| 无法检测静态目录 | Workers 部署命令或 Wrangler 配置是否指定了 `public`。 |
| 缺少兼容日期 | Workers 部署命令或 Wrangler 配置是否设置兼容日期。 |
| 根地址 404、报告地址正常 | 检查 Cloudflare 静态目录是否包含本次发布提交里的首页 `index.html`。 |
| 中文乱码 | HTML 是否声明 UTF-8，浏览器实际编码是否正确。 |
| 已推送但未 `verified` | 查看 Cloudflare 构建结果，并检查公网是否仍为旧版本，或是否转换了 HTML。 |

参考 [Cloudflare Pages Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)、[Workers Builds 配置](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/)。
