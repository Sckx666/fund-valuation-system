import akshare as ak
import json
import os
from datetime import datetime
import pytz
import time

# 简化版：只使用 AkShare（国内可访问）
ASSETS = [
    # A股指数
    {"code": "000001", "name": "上证指数", "type": "index_cn"},
    {"code": "399001", "name": "深证成指", "type": "index_cn"},
    {"code": "399006", "name": "创业板指", "type": "index_cn"},
    
    # A股热门股票
    {"code": "600519", "name": "贵州茅台", "type": "stock_cn"},
    {"code": "000858", "name": "五粮液", "type": "stock_cn"},
    {"code": "601318", "name": "中国平安", "type": "stock_cn"},
    {"code": "600036", "name": "招商银行", "type": "stock_cn"},
    {"code": "000333", "name": "美的集团", "type": "stock_cn"},
    
    # 基金（使用已有的基金数据）
    {"code": "110020", "name": "易方达沪深300ETF联接A", "type": "fund"},
    {"code": "161725", "name": "招商中证白酒", "type": "fund"},
    {"code": "512480", "name": "半导体ETF", "type": "fund"},
]

def get_index_data(code):
    """获取指数数据"""
    try:
        df = ak.stock_zh_index_spot_em()
        index = df[df['代码'] == code]
        if not index.empty:
            return {
                'price': float(index['最新价'].values[0]),
                'change': float(index['涨跌幅'].values[0])
            }
    except Exception as e:
        print(f"获取指数 {code} 失败: {str(e)[:30]}")
    return None

def get_stock_data(code):
    """获取股票数据"""
    try:
        df = ak.stock_zh_a_spot_em()
        stock = df[df['代码'] == code]
        if not stock.empty:
            return {
                'price': float(stock['最新价'].values[0]),
                'change': float(stock['涨跌幅'].values[0])
            }
    except Exception as e:
        print(f"获取股票 {code} 失败: {str(e)[:30]}")
    return None

def get_fund_data(code):
    """获取基金估值"""
    try:
        import requests
        url = f"http://fundgz.1234567.com.cn/js/{code}.js"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data_str = response.text.replace('jsonpgz(', '').replace(');', '')
            data = json.loads(data_str)
            return {
                'price': float(data['dwjz']),
                'change': float(data['gszzl'])
            }
    except Exception as e:
        print(f"获取基金 {code} 失败: {str(e)[:30]}")
    return None

def process_asset(item):
    """处理单个资产"""
    print(f"[{item['code']}] {item['name']}...", end=" ")
    
    result = {
        "code": item["code"],
        "name": item["name"],
        "market": item["type"],
        "price": 0,
        "change_pct": 0,
        "success": False
    }
    
    try:
        data = None
        
        if item["type"] == "index_cn":
            data = get_index_data(item["code"])
        elif item["type"] == "stock_cn":
            data = get_stock_data(item["code"])
        elif item["type"] == "fund":
            data = get_fund_data(item["code"])
        
        if data:
            result["price"] = data["price"]
            result["change_pct"] = data["change"]
            result["success"] = True
            print(f"{data['change']:+.2f}% ✓")
        else:
            print("✗")
    
    except Exception as e:
        print(f"✗ {str(e)[:30]}")
    
    return result

def main():
    print("=" * 60)
    print(f"开始抓取 {len(ASSETS)} 个国内资产数据（AkShare）")
    print("=" * 60)
    
    os.makedirs("data", exist_ok=True)
    os.makedirs("public/data", exist_ok=True)
    
    results = []
    success_count = 0
    
    for i, asset in enumerate(ASSETS, 1):
        print(f"[{i}/{len(ASSETS)}] ", end="")
        result = process_asset(asset)
        results.append(result)
        
        if result["success"]:
            success_count += 1
        
        time.sleep(0.2)  # 避免请求过快
    
    # 按类型分组
    grouped = {
        "index_cn": [r for r in results if r["market"] == "index_cn"],
        "stock_cn": [r for r in results if r["market"] == "stock_cn"],
        "fund": [r for r in results if r["market"] == "fund"],
    }
    
    beijing_tz = pytz.timezone('Asia/Shanghai')
    output = {
        "last_updated": datetime.now(beijing_tz).strftime('%Y-%m-%d %H:%M:%S'),
        "total_count": len(results),
        "success_count": success_count,
        "assets": results,
        "grouped": grouped
    }
    
    # 保存到两个位置
    with open("data/global_assets.json", "w", encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    with open("public/data/global_assets.json", "w", encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print("=" * 60)
    print(f"完成！成功: {success_count}/{len(results)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
