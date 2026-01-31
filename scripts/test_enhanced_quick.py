"""快速测试增强版脚本（仅测试代码结构）"""
import json
import os
from datetime import datetime
import pytz

# 模拟测试数据
test_assets = [
    {"code": "BTC", "name": "比特币", "type": "crypto", "price": 95234.50, "change": 2.34},
    {"code": "NVDA", "name": "英伟达", "type": "stock_us", "price": 875.23, "change": 3.45},
    {"code": "^GSPC", "name": "标普500", "type": "index", "price": 5234.12, "change": 0.87},
]

os.makedirs("data", exist_ok=True)
os.makedirs("public/data", exist_ok=True)

results = []
for asset in test_assets:
    results.append({
        "code": asset["code"],
        "name": asset["name"],
        "market": asset["type"],
        "price": asset["price"],
        "change_pct": asset["change"],
        "data_source": "测试数据",
        "success": True
    })

# 按类型分组
grouped = {
    "crypto": [r for r in results if r["market"] == "crypto"],
    "stock_us": [r for r in results if r["market"] == "stock_us"],
    "index": [r for r in results if r["market"] == "index"],
}

beijing_tz = pytz.timezone('Asia/Shanghai')
output = {
    "last_updated": datetime.now(beijing_tz).strftime('%Y-%m-%d %H:%M:%S'),
    "total_count": len(results),
    "success_count": len(results),
    "assets": results,
    "grouped": grouped
}

with open("data/global_assets.json", "w", encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

with open("public/data/global_assets.json", "w", encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("✅ 测试数据生成成功！")
print(f"总数: {len(results)}")
print("文件已保存到:")
print("  - data/global_assets.json")
print("  - public/data/global_assets.json")
