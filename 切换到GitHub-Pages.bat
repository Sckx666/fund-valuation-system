@echo off
chcp 65001 >nul
echo ========================================
echo    切换到 GitHub Pages（国内可访问）
echo ========================================
echo.

echo [1/2] 提交代码到 GitHub...
git add .
git commit -m "Switch to GitHub Pages for China access"
git push

echo.
echo [2/2] 配置 GitHub Pages...
echo.
echo 请在浏览器中完成以下步骤：
echo.
echo 1. 进入你的 GitHub 仓库
echo 2. 点击顶部的 "Settings"
echo 3. 在左侧菜单找到 "Pages"
echo 4. 在 "Source" 下：
echo    - Branch: 选择 "main"
echo    - Folder: 选择 "/ (root)"
echo 5. 点击 "Save"
echo 6. 等待 5-10 分钟
echo.

set /p repo_url="请输入你的 GitHub 仓库地址: "
start %repo_url%/settings/pages

echo.
echo ========================================
echo ✅ 配置完成！
echo ========================================
echo.
echo 等待 5-10 分钟后访问：
echo https://你的用户名.github.io/fund-valuation-system
echo.
echo 优势：
echo ✓ 国内可直接访问
echo ✓ 完全免费
echo ✓ 自动部署
echo ✓ 速度快
echo.
pause
