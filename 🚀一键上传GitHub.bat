@echo off
chcp 65001 >nul
echo ========================================
echo 🚀 一键上传到GitHub
echo ========================================
echo.

echo 📋 第一步：检查Git配置
echo ----------------------------------------
git config user.name >nul 2>&1
if errorlevel 1 (
    echo ⚠️ 未配置Git用户名
    echo.
    set /p username="请输入你的GitHub用户名: "
    git config --global user.name "!username!"
    echo ✅ 用户名已设置
) else (
    for /f "delims=" %%i in ('git config user.name') do set current_user=%%i
    echo ✅ 当前用户名: !current_user!
)
echo.

git config user.email >nul 2>&1
if errorlevel 1 (
    echo ⚠️ 未配置Git邮箱
    echo.
    set /p email="请输入你的GitHub邮箱: "
    git config --global user.email "!email!"
    echo ✅ 邮箱已设置
) else (
    for /f "delims=" %%i in ('git config user.email') do set current_email=%%i
    echo ✅ 当前邮箱: !current_email!
)
echo.

echo 📋 第二步：添加所有文件
echo ----------------------------------------
git add .
if errorlevel 1 (
    echo ❌ 添加文件失败
    pause
    exit /b 1
)
echo ✅ 所有文件已添加
echo.

echo 📋 第三步：提交到本地仓库
echo ----------------------------------------
git commit -m "🎉 初始提交：实时估值系统 - 200+基金双重估值"
if errorlevel 1 (
    echo ⚠️ 提交失败或无新更改
)
echo ✅ 已提交到本地仓库
echo.

echo 📋 第四步：连接GitHub仓库
echo ----------------------------------------
echo.
echo 💡 请先在GitHub上创建一个新仓库：
echo    1. 打开 https://github.com/new
echo    2. 仓库名称建议：fund-valuation-system
echo    3. 选择 Public（公开）
echo    4. 不要勾选任何初始化选项
echo    5. 点击 Create repository
echo.
echo 创建完成后，复制仓库地址（类似：https://github.com/你的用户名/fund-valuation-system.git）
echo.
set /p repo_url="请粘贴你的GitHub仓库地址: "

if "%repo_url%"=="" (
    echo ❌ 未输入仓库地址
    pause
    exit /b 1
)

git remote add origin %repo_url%
if errorlevel 1 (
    echo ⚠️ 可能已经添加过远程仓库，尝试更新...
    git remote set-url origin %repo_url%
)
echo ✅ 已连接到GitHub仓库
echo.

echo 📋 第五步：推送到GitHub
echo ----------------------------------------
git branch -M main
git push -u origin main
if errorlevel 1 (
    echo.
    echo ❌ 推送失败！
    echo.
    echo 💡 可能的原因：
    echo    1. 需要GitHub身份验证
    echo    2. 仓库地址错误
    echo    3. 网络问题
    echo.
    echo 💡 解决方案：
    echo    1. 使用GitHub Desktop（推荐）
    echo    2. 配置Personal Access Token
    echo    3. 使用SSH密钥
    echo.
    echo 详细教程请查看：GitHub-Pages详细教程.txt
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ 上传成功！
echo ========================================
echo.
echo 📋 接下来的步骤：
echo.
echo 1. 【启用GitHub Pages】
echo    • 打开你的GitHub仓库页面
echo    • 点击 Settings（设置）
echo    • 左侧菜单找到 Pages
echo    • Source 选择：main 分支
echo    • Folder 选择：/ (root)
echo    • 点击 Save
echo.
echo 2. 【等待部署】
echo    • 等待5-10分钟
echo    • GitHub会自动部署网站
echo.
echo 3. 【访问网站】
echo    • 网址：https://你的用户名.github.io/仓库名
echo    • 例如：https://zhangsan.github.io/fund-valuation-system
echo.
echo 4. 【等待数据更新】
echo    • 打开仓库 → Actions标签
echo    • 等待自动运行完成（2-3分钟）
echo    • 数据文件会自动生成
echo.
echo ========================================
echo.
echo 🎉 恭喜！你的基金估值系统已经上传到GitHub！
echo.
echo 📚 详细教程：
echo    • GitHub-Pages详细教程.txt
echo    • ⚡立即体验实时估值.txt
echo.
echo ========================================
pause
