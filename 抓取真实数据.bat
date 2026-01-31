@echo off
chcp 65001 >nul
echo ========================================
echo    抓取真实基金估值数据
echo ========================================
echo.

echo [步骤 1/3] 修复 Python 环境...
echo 正在更新 numpy 和 pandas...
pip install --upgrade numpy pandas akshare pytz

echo.
echo [步骤 2/3] 开始抓取数据...
echo 这可能需要 3-5 分钟，请耐心等待...
echo.
python scripts/fetch_data.py

echo.
echo [步骤 3/3] 提交数据到 GitHub...
git add data/funds.json
git commit -m "Update real-time fund valuation data"
git push

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo 真实数据已生成并上传
echo Vercel 会自动重新部署
echo 等待 1-2 分钟后访问你的网站
echo.
pause
