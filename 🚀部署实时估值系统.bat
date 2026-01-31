@echo off
chcp 65001 >nul
echo ========================================
echo 🚀 部署实时估值系统
echo ========================================
echo.
echo 🔥 新功能：双重估值系统
echo    1. 官方估值（天天基金API）
echo    2. 实时计算估值（成分股实时价格）
echo.
echo ========================================
echo.

echo [1/3] 添加所有文件到Git...
git add .
if errorlevel 1 (
    echo ❌ Git添加失败
    pause
    exit /b 1
)
echo ✅ 文件添加成功
echo.

echo [2/3] 提交更改...
git commit -m "🔥 添加实时估值功能 - 成分股实时计算"
if errorlevel 1 (
    echo ⚠️ 没有新的更改需要提交
)
echo.

echo [3/3] 推送到GitHub...
git push
if errorlevel 1 (
    echo ❌ 推送失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ 部署成功！
echo ========================================
echo.
echo 🔥 新功能特点：
echo.
echo 1. 双重估值显示
echo    • 官方估值（天天基金）
echo    • 实时计算估值（成分股）
echo.
echo 2. 几乎实时更新
echo    • 基于股票实时价格
echo    • 秒级延迟
echo.
echo 3. 更高准确度
echo    • 双重验证机制
echo    • 互相对比
echo.
echo 4. 完整持仓分析
echo    • 看到具体哪些股票在涨跌
echo    • 了解收益来源
echo.
echo ========================================
echo.
echo 📋 接下来：
echo 1. 等待GitHub Actions运行（2-3分钟）
echo 2. 访问网站查看新功能
echo 3. 对比官方估值和实时计算估值
echo.
echo 🌐 访问地址：
echo    https://你的用户名.github.io/仓库名
echo.
echo ========================================
pause
