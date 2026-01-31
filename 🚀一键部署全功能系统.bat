@echo off
chcp 65001 >nul
echo ╔═══════════════════════════════════════════════════════════════════╗
echo ║          🚀 一键部署全功能系统                                    ║
echo ║          基金估值 + 全球资产监控                                  ║
echo ╚═══════════════════════════════════════════════════════════════════╝
echo.

echo [步骤 1/5] 检查 Python 依赖...
echo.

pip show akshare >nul 2>&1
if errorlevel 1 (
    echo ⚠️  未安装 akshare，正在安装...
    pip install akshare
) else (
    echo ✓ akshare 已安装
)

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
echo [步骤 2/5] 创建数据目录...
if not exist "data" mkdir data
if not exist "public\data" mkdir public\data
echo ✓ 数据目录已创建

echo.
echo [步骤 3/5] 抓取基金数据（200+ 基金）...
python scripts/fetch_data.py
if errorlevel 1 (
    echo ⚠️  基金数据抓取失败，请检查网络连接
) else (
    echo ✓ 基金数据抓取成功
)

echo.
echo [步骤 4/5] 抓取全球资产数据...
python scripts/fetch_global_assets.py
if errorlevel 1 (
    echo ⚠️  全球资产数据抓取失败，请检查网络连接
) else (
    echo ✓ 全球资产数据抓取成功
)

echo.
echo [步骤 5/5] 复制数据到 public 目录...
copy data\funds.json public\data\funds.json >nul 2>&1
copy data\global_assets.json public\data\global_assets.json >nul 2>&1
echo ✓ 数据已复制

echo.
echo ╔═══════════════════════════════════════════════════════════════════╗
echo ║                    ✅ 部署完成！                                  ║
echo ║                                                                   ║
echo ║  现在可以：                                                       ║
echo ║  1. 打开 index.html 查看基金估值（200+ 基金）                    ║
echo ║  2. 打开 global-simple.html 查看全球资产                         ║
echo ║  3. 或者运行 npm start 启动 React 版本                           ║
echo ║                                                                   ║
echo ║  数据文件位置：                                                   ║
echo ║  - data/funds.json                                               ║
echo ║  - data/global_assets.json                                       ║
echo ║  - public/data/funds.json                                        ║
echo ║  - public/data/global_assets.json                                ║
echo ╚═══════════════════════════════════════════════════════════════════╝
echo.

echo 是否立即打开网页？(Y/N)
set /p choice=
if /i "%choice%"=="Y" (
    start index.html
    start global-simple.html
)

pause
