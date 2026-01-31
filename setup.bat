@echo off
chcp 65001 >nul
echo ========================================
echo    基金估值系统 - 快速配置脚本
echo ========================================
echo.

:input_username
set /p github_username="请输入你的 GitHub 用户名: "
if "%github_username%"=="" (
    echo [错误] 用户名不能为空！
    goto input_username
)

echo.
echo [信息] 正在配置 package.json...

powershell -Command "(Get-Content package.json) -replace '你的GitHub用户名', '%github_username%' | Set-Content package.json"

echo [成功] 配置完成！
echo.
echo ========================================
echo 下一步操作：
echo ========================================
echo 1. 在 GitHub 创建名为 fund-valuation-system 的仓库
echo 2. 运行以下命令上传代码：
echo.
echo    git init
echo    git add .
echo    git commit -m "Initial commit"
echo    git branch -M main
echo    git remote add origin https://github.com/%github_username%/fund-valuation-system.git
echo    git push -u origin main
echo.
echo 3. 进入 GitHub 仓库的 Actions 标签，点击 Run workflow
echo 4. 等待 2-3 分钟后，访问：
echo    https://%github_username%.github.io/fund-valuation-system
echo ========================================
echo.
pause
