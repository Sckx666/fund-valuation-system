@echo off
chcp 65001 >nul
echo ========================================
echo    部署全网最丰富的基金估值系统
echo ========================================
echo.

echo [1/3] 添加所有文件...
git add index.html scripts/fetch_data.py data/funds.json

echo [2/3] 提交修改...
git commit -m "Upgrade to most comprehensive fund valuation system - 100+ funds"

echo [3/3] 推送到 GitHub...
git push

echo.
echo ========================================
echo ✅ 完成！
echo ========================================
echo.
echo 新功能：
echo ✓ 100+ 只基金覆盖
echo ✓ 实时搜索功能
echo ✓ 涨跌筛选
echo ✓ 多种排序方式
echo ✓ 统计数据展示
echo.
echo Vercel 会自动重新部署
echo 等待 1-2 分钟后访问你的网站
echo.
pause
