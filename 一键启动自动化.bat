@echo off
chcp 65001 >nul
echo ========================================
echo    一键启动完全自动化系统
echo ========================================
echo.

echo [1/4] 提交最新代码...
git add .
git commit -m "Enable full automation - update every 30 minutes"
git push

echo.
echo [2/4] 等待 GitHub 同步...
timeout /t 3 /nobreak >nul

echo.
echo [3/4] 打开 GitHub Actions 页面...
echo 请在浏览器中：
echo 1. 点击 "Actions" 标签
echo 2. 点击 "I understand my workflows, go ahead and enable them"（如果显示）
echo 3. 选择 "Auto Fund Valuation & Deploy"
echo 4. 点击 "Run workflow" 按钮
echo 5. 再次点击绿色的 "Run workflow" 确认
echo.

set /p repo_url="请输入你的 GitHub 仓库地址（例如：https://github.com/better6666/fund-valuation-system）: "
start %repo_url%/actions

echo.
echo [4/4] 等待首次运行完成...
echo.
echo ========================================
echo ✅ 设置完成！
echo ========================================
echo.
echo 自动化已启动：
echo ✓ 工作日每 30 分钟自动更新
echo ✓ 北京时间 9:00 - 15:00
echo ✓ 无需任何手动操作
echo ✓ 数据自动同步到网站
echo.
echo 下次更新时间：
echo - 如果现在是交易时间，30 分钟后
echo - 如果现在是非交易时间，下个交易日 9:00
echo.
echo 访问你的网站查看最新数据：
echo https://fund-valuation-system-3hok.vercel.app
echo.
pause
