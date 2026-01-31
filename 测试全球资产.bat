@echo off
chcp 65001 >nul
echo ╔═══════════════════════════════════════════════════════════════════╗
echo ║              🌍 测试全球资产监控系统                             ║
echo ╚═══════════════════════════════════════════════════════════════════╝
echo.

echo [步骤 1/3] 检查Python依赖...
pip show yfinance >nul 2>&1
if errorlevel 1 (
    echo ⚠️  未安装 yfinance，正在安装...
    pip install yfinance
) else (
    echo ✓ yfinance 已安装
)

pip show ccxt >nul 2>&1
if errorlevel 1 (
    echo ⚠️  未安装 ccxt，正在安装...
    pip install ccxt
) else (
    echo ✓ ccxt 已安装
)

echo.
echo [步骤 2/3] 运行数据抓取脚本...
python scripts/fetch_global_assets.py

echo.
echo [步骤 3/3] 打开浏览器查看效果...
start global.html

echo.
echo ╔═══════════════════════════════════════════════════════════════════╗
echo ║                    ✅ 完成！                                      ║
echo ║                                                                   ║
echo ║  浏览器已打开 global.html                                        ║
echo ║  你应该能看到全球资产监控页面                                    ║
echo ║                                                                   ║
echo ║  如果页面显示"暂无数据"，请检查：                                ║
echo ║  1. data/global_assets.json 是否生成                             ║
echo ║  2. 网络连接是否正常                                             ║
echo ║  3. 控制台是否有错误信息                                         ║
echo ╚═══════════════════════════════════════════════════════════════════╝
echo.
pause
