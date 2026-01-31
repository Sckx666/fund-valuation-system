import json
import os
from datetime import datetime
import pytz

# 生成测试数据（快速版本）
def generate_test_data():
    print("生成全球资产测试数据...")
    
    os.makedirs("data", exist_ok=True)
    os.makedirs("public/data", exist_ok=True)
    
    # 测试数据
    test_assets = [
        # 加密货币
        {"code": "BTC", "name": "比特币", "market": "crypto", "price": 95234.50, "change_pct": 2.34, "success": True},
        {"code": "ETH", "name": "以太坊", "market": "crypto", "price": 3456.78, "change_pct": 1.23, "success": True},
        
        # 全球指数
        {"code": "NDX", "name": "纳斯达克100", "market": "index", "price": 18234.56, "change_pct": 0.89, "success": True},
        {"code": "SPX", "name": "标普500", "market": "index", "price": 5234.12, "change_pct": 0.45, "success": True},
        
        # 美股
        {"code": "NVDA", "name": "英伟达", "market": "stock_us", "price": 876.54, "change_pct": 3.21, "success": True},
        {"code": "TSLA", "name": "特斯拉", "market": "stock_us", "price": 234.56, "change_pct": -1.23, "success": True},
        
        # 大宗商品
        {"code": "GOLD", "name": "黄金", "market": "commodity", "price": 2034.50, "change_pct": 0.67, "success": True},
    ]
    
    # 按类型分组
    grouped = {
        "crypto": [a for a in test_assets if a["market"] == "crypto"],
        "index": [a for a in test_assets if a["market"] == "index"],
        "stock_us": [a for a in test_assets if a["market"] == "stock_us"],
        "commodity": [a for a in test_assets if a["market"] == "commodity"],
        "fund_qdii": [],
        "fund_cn": []
    }
    
    beijing_tz = pytz.timezone('Asia/Shanghai')
    output = {
        "last_updated": datetime.now(beijing_tz).strftime('%Y-%m-%d %H:%M:%S'),
        "total_count": len(test_assets),
        "success_count": len(test_assets),
        "assets": test_assets,
        "grouped": grouped
    }
    
    # 保存到两个位置
    with open("data/global_assets.json", "w", encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    with open("public/data/global_assets.json", "w", encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 测试数据已生成")
    print(f"✓ data/global_assets.json")
    print(f"✓ public/data/global_assets.json")
    print(f"✓ 共 {len(test_assets)} 个资产")

if __name__ == "__main__":
    generate_test_data()
