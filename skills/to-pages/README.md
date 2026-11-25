# to-pages 配置与使用

把 HTML 报告或静态目录推送到 GitHub，由 Cloudflare Pages 或 Workers Builds 自动部署。脚本使用 Python 标准库和 Git，支持 Mac 与 Linux。

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
    "base_url": "https://lemon-pages.lemonsun224.workers.dev",
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
| `cloudflare.base_url` | 实际生产 HTTPS 地址。支持 `pages.dev`、`workers.dev` 或自定义域名。 |
| `cloudflare.output_dir` | 仓库内的静态目录，默认 `public`；仓库根目录用 `.`。 |

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

## 发布报告

单个 HTML 会保存为目标目录的 `index.html`。带图片、CSS 或脚本时使用静态目录，并在其中提供 `index.html`。脚本会递归上传该目录，不会自动收集 HTML 引用的外部本地资源。

确认 HTML 使用 UTF-8，并在前 1024 字节声明 `<meta charset="utf-8">`。脚本逐字节复制文件，不会自动修改编码或生成导航页。

```bash
python3 <skill-dir>/scripts/to_pages.py doctor
python3 <skill-dir>/scripts/to_pages.py plan /path/report.html --path reports/topic
python3 <skill-dir>/scripts/to_pages.py publish /path/report.html --path reports/topic
```

发布后的相对 URL 为 `/reports/topic/`，对应仓库中的 `public/reports/topic/index.html`。`--path` 相对于站点目录，不要重复包含 `public`。

授权更新已有报告时使用 `--replace`：

```bash
python3 <skill-dir>/scripts/to_pages.py publish /path/static-dir --path reports/topic --replace
```

脚本保留其他报告，不删除目标目录的旧资源。相同内容不会创建新提交。并发 push 被拒时，重新检查远端变更，再预览和推送，不 force push。

仅推送到 GitHub：

```bash
python3 <skill-dir>/scripts/to_pages.py push /path/report.html --path reports/topic
```

推送成功不等于 Cloudflare 已部署。等待超时后只读核对：

```bash
python3 <skill-dir>/scripts/to_pages.py verify /path/report.html --path reports/topic --timeout 300
```

`publish` 和 `verify` 需要配置站点地址。`verify` 会逐个比较公网文件，失败时返回非零退出码。`push` 不要求站点地址，也不做公网核对。

脚本拒绝把 `.` 用作报告路径。站点根目录的导航页应通过普通 Git 提交为 `public/index.html`，保留已有内容。新增报告时同步添加导航入口，并验证根地址和跳转。

## 验证与排错

运行脚本测试，不访问真实 GitHub 或 Cloudflare，也不会发布测试页面：

```bash
python3 <skill-dir>/scripts/test_to_pages.py -v
```

| 现象 | 检查项 |
| --- | --- |
| `GitHub token missing` | 当前进程是否加载了环境变量，或能读取配置的凭证文件。 |
| GitHub 返回 403 | Token 是否包含目标仓库，并有 `Contents: Read and write`；账号角色不能代替 Token 权限。 |
| 无法检测静态目录 | Workers 部署命令或 Wrangler 配置是否指定了 `public`。 |
| 缺少兼容日期 | Workers 部署命令或 Wrangler 配置是否设置兼容日期。 |
| 根地址 404、报告地址正常 | 站点目录缺少 `index.html`，需要首页或导航页。 |
| 中文乱码 | HTML 是否声明 UTF-8，浏览器实际编码是否正确。 |
| 已推送但未 `verified` | 查看 Cloudflare 构建结果，并检查公网是否仍为旧版本，或是否转换了 HTML。 |

参考 [Cloudflare Pages Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)、[Workers Builds 配置](https://developers.cloudflare.com/workers/ci-cd/builds/configuration/)。
