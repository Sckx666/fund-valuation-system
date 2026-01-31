@echo off
chcp 65001 >nul
echo ========================================
echo    一键提交所有文件到 GitHub
echo ========================================
echo.

echo [1/4] 添加所有文件...
git add .

echo [2/4] 提交...
git commit -m "Initial commit: HTML version fund valuation system"

echo [3/4] 设置分支...
git branch -M main

echo [4/4] 推送到 GitHub...
echo 请输入你的 GitHub 仓库地址（例如：https://github.com/better6666/fund-valuation-system.git）
set /p repo_url="仓库地址: "

git remote add origin %repo_url%
git push -u origin main

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo Vercel 会自动检测并部署
echo 等待 1-2 分钟后访问你的网站
echo.
pause
