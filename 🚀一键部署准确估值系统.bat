@echo off
chcp 65001 >nul
echo ========================================
echo 🚀 一键部署准确估值系统
echo ========================================
echo.

echo [1/3] 添加所有文件到Git...
git add .
if errorlevel 1 (
    echo ❌ Git添加失败，请检查Git是否安装
    pause
    exit /b 1
)
echo ✅ 文件添加成功
echo.

echo [2/3] 提交更改...
git commit -m "🎉 升级到准确估值系统 - 200+基金，天天基金实时数据"
if errorlevel 1 (
    echo ⚠️ 没有新的更改需要提交，或提交失败
)
echo.

echo [3/3] 推送到GitHub...
git push -u origin main
if errorlevel 1 (
    echo ❌ 推送失败，可能需要先设置远程仓库
    echo.
    echo 💡 如果是首次推送，请先运行：
    echo    git remote add origin https://github.com/你的用户名/仓库名.git
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ 部署成功！
echo ========================================
echo.
echo 📋 接下来的步骤：
echo.
echo 1. 打开GitHub仓库页面
echo 2. 点击 Actions 标签
echo 3. 等待自动运行完成（约2-3分钟）
echo 4. 访问你的网站查看效果
echo.
echo 🌐 GitHub Pages地址：
echo    https://你的用户名.github.io/仓库名
echo.
echo 📊 数据特点：
echo    ✓ 200+只基金覆盖全市场
echo    ✓ 天天基金实时API，数据最准确
echo    ✓ 每30分钟自动更新
echo    ✓ 完整的前10大重仓股信息
echo.
echo ========================================
pause
