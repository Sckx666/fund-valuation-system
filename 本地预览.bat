@echo off
chcp 65001 >nul
echo ========================================
echo    启动本地预览服务器
echo ========================================
echo.

echo 正在启动服务器...
echo 浏览器会自动打开 http://localhost:8000
echo.
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.

start http://localhost:8000

python -m http.server 8000
