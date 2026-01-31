# 🚀 Vercel 部署指南

你已经成功部署到 Vercel 了！现在让我们修复空白页面问题。

## 📋 问题原因

Vercel 和 GitHub Pages 的路径配置不同：
- GitHub Pages 需要 `homepage` 配置
- Vercel 不需要，反而会导致路径错误

## ✅ 已修复的内容

我已经帮你修复了：
1. ✅ 移除了 `package.json` 中的 `homepage` 配置
2. ✅ 修改了 `src/App.js` 中的数据路径（`./data/funds.json` → `/data/funds.json`）
3. ✅ 创建了 `vercel.json` 配置文件

## 🔄 重新部署步骤

### 方法 1：通过 Git 推送（推荐）

```bash
git add .
git commit -m "Fix Vercel deployment"
git push
```

Vercel 会自动检测到代码变化并重新部署（约 1-2 分钟）。

### 方法 2：在 Vercel 网站手动触发

1. 登录 [vercel.com](https://vercel.com)
2. 进入你的项目
3. 点击 **Deployments** 标签
4. 点击最新部署右侧的 **...** → **Redeploy**

## ⏰ 等待部署完成

1. 在 Vercel 项目页面，等待部署状态变为 **Ready**（绿色对勾）
2. 大约需要 1-2 分钟
3. 部署完成后，访问你的网站：
   ```
   https://fund-valuation-system-3hok.vercel.app
   ```

## 🎯 关于自动化数据更新

### 重要提示

Vercel 部署后，GitHub Actions 仍然会运行，但数据不会自动同步到 Vercel！

### 解决方案 A：使用 Vercel 的 Cron Jobs（推荐）

1. 在项目根目录创建 `api/update-data.js`：

```javascript
// api/update-data.js
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export default async function handler(req, res) {
  try {
    // 运行 Python 脚本
    await execAsync('python scripts/fetch_data.py');
    
    res.status(200).json({ 
      success: true, 
      message: 'Data updated successfully' 
    });
  } catch (error) {
    res.status(500).json({ 
      success: false, 
      error: error.message 
    });
  }
}
```

2. 在 `vercel.json` 中添加 Cron 配置：

```json
{
  "crons": [{
    "path": "/api/update-data",
    "schedule": "0 1-7 * * 1-5"
  }]
}
```

### 解决方案 B：继续使用 GitHub Pages（推荐新手）

如果你想要完全自动化，建议改用 GitHub Pages：

1. 恢复 `package.json` 中的 `homepage` 配置
2. 按照 `部署指南.md` 部署到 GitHub Pages
3. GitHub Actions 会自动更新数据并部署

## 🔍 验证部署

部署完成后，打开浏览器：

1. 访问你的 Vercel 网站
2. 按 F12 打开开发者工具
3. 查看 Console 标签，应该没有错误
4. 如果显示"暂无数据"，说明需要生成数据文件

## 📊 生成数据文件

### 方法 1：本地生成后推送

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 运行数据抓取脚本
python scripts/fetch_data.py

# 提交并推送
git add public/data/funds.json
git commit -m "Add initial data"
git push
```

### 方法 2：使用 GitHub Actions

1. 进入 GitHub 仓库的 **Actions** 标签
2. 选择 **Auto Fund Valuation & Deploy**
3. 点击 **Run workflow**
4. 等待运行完成
5. 数据文件会生成在 `public/data/funds.json`
6. 手动下载这个文件，放到本地项目的 `public/data/` 目录
7. 提交并推送到 GitHub

## 🎨 Vercel vs GitHub Pages 对比

| 特性 | Vercel | GitHub Pages |
|------|--------|--------------|
| 部署速度 | ⚡ 超快（1-2分钟） | 🐢 较慢（5-10分钟） |
| 自动化数据 | ❌ 需要额外配置 | ✅ 完全自动 |
| 自定义域名 | ✅ 免费 | ✅ 免费 |
| 构建时间 | 无限制 | 有限制 |
| 适合场景 | 需要快速迭代 | 需要自动化 |

## 💡 建议

**如果你想要完全自动化（推荐）：**
→ 使用 GitHub Pages（按照 `部署指南.md` 操作）

**如果你想要快速部署和迭代：**
→ 继续使用 Vercel，但需要手动更新数据

## ❓ 常见问题

### Q: 为什么 Vercel 上还是空白？
A: 等待 1-2 分钟让部署完成，然后强制刷新（Ctrl + F5）

### Q: 如何切换到 GitHub Pages？
A: 
1. 恢复 `package.json` 中的 `homepage` 配置
2. 修改 `src/App.js` 中的路径回 `./data/funds.json`
3. 按照 `部署指南.md` 操作

### Q: 可以同时使用 Vercel 和 GitHub Pages 吗？
A: 可以，但需要维护两套配置，不推荐

---

现在提交代码，等待 Vercel 重新部署即可！
