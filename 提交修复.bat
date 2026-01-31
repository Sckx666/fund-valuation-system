@echo off
chcp 65001 >nul
echo ========================================
echo    提交 Vercel 修复到 GitHub
echo ========================================
echo.

echo [1/3] 添加所有修改的文件...
git add .

echo [2/3] 提交修改...
git commit -m "Fix Vercel deployment - remove homepage config and update paths"

echo [3/3] 推送到 GitHub...
git push

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo Vercel 会自动检测到代码变化并重新部署
echo 请等待 1-2 分钟后访问你的网站：
echo https://fund-valuation-system-3hok.vercel.app
echo.
pause
