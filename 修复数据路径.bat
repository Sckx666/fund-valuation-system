@echo off
chcp 65001 >nul
echo ========================================
echo    修复数据路径并重新部署
echo ========================================
echo.

echo [1/5] 配置 Git 用户信息...
set /p git_name="请输入你的名字（例如：Zhang San）: "
set /p git_email="请输入你的邮箱（例如：zhangsan@example.com）: "

git config --global user.name "%git_name%"
git config --global user.email "%git_email%"

echo [2/5] 添加修改的文件...
git add index.html

echo [3/5] 提交修改...
git commit -m "Fix data path for Vercel"

echo [4/5] 设置远程仓库...
set /p repo_url="请输入你的 GitHub 仓库地址: "
git remote add origin %repo_url% 2>nul

echo [5/5] 推送到 GitHub...
git push -u origin main

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo Vercel 会自动重新部署
echo 等待 1-2 分钟后刷新你的网站
echo.
pause
