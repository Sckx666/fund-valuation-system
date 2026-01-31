@echo off
chcp 65001 >nul
echo ========================================
echo    部署 HTML 版本到 Vercel/GitHub
echo ========================================
echo.

echo [1/3] 添加所有文件...
git add index.html data/funds.json scripts/fetch_data.py .github/workflows/update_data.yml

echo [2/3] 提交修改...
git commit -m "Switch to HTML version - simpler and faster"

echo [3/3] 推送到 GitHub...
git push

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo 如果使用 Vercel：
echo   - Vercel 会自动检测并部署
echo   - 等待 1-2 分钟
echo   - 访问：https://fund-valuation-system-3hok.vercel.app
echo.
echo 如果使用 GitHub Pages：
echo   1. 进入 Settings -^> Pages
echo   2. Source 选择 "main" 分支
echo   3. Root 选择 "/ (root)"
echo   4. 保存后访问：https://你的用户名.github.io/fund-valuation-system
echo.
pause
