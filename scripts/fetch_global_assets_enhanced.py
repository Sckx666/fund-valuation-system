import akshare as ak
import yfinance as yf
import ccxt
import json
import os
from datetime import datetime
import pytz
import time
import requests

# === 全球资产监控清单（增强版 - 更多国外数据）===
ASSETS = [
    # === 加密货币（10个主流币种）===
    {"code": "BTC", "name": "比特币", "type": "crypto", "symbol": "BTC/USDT"},
    {"code": "ETH", "name": "以太坊", "type": "crypto", "symbol": "ETH/USDT"},
    {"code": "BNB", "name": "币安币", "type": "crypto", "symbol": "BNB/USDT"},
    {"code": "SOL", "name": "索拉纳", "type": "crypto", "symbol": "SOL/USDT"},
    {"code": "XRP", "name": "瑞波币", "type": "crypto", "symbol": "XRP/USDT"},
    {"code": "ADA", "name": "艾达币", "type": "crypto", "symbol": "ADA/USDT"},
    {"code": "DOGE", "name": "狗狗币", "type": "crypto", "symbol": "DOGE/USDT"},
    {"code": "AVAX", "name": "雪崩", "type": "crypto", "symbol": "AVAX/USDT"},
    {"code": "DOT", "name": "波卡", "type": "crypto", "symbol": "DOT/USDT"},
    {"code": "MATIC", "name": "Polygon", "type": "crypto", "symbol": "MATIC/USDT"},
    
    # === 美股科技巨头（FAANG + 芯片）===
    {"code": "AAPL", "name": "苹果", "type": "stock_us", "symbol": "AAPL"},
    {"code": "MSFT", "name": "微软", "type": "stock_us", "symbol": "MSFT"},
    {"code": "GOOGL", "name": "谷歌", "type": "stock_us", "symbol": "GOOGL"},
    {"code": "AMZN", "name": "亚马逊", "type": "stock_us", "symbol": "AMZN"},
    {"code": "META", "name": "Meta", "type": "stock_us", "symbol": "META"},
    {"code": "NVDA", "name": "英伟达", "type": "stock_us", "symbol": "NVDA"},
    {"code": "TSLA", "name": "特斯拉", "type": "stock_us", "symbol": "TSLA"},
    {"code": "AMD", "name": "AMD", "type": "stock_us", "symbol": "AMD"},
    {"code": "INTC", "name": "英特尔", "type": "stock_us", "symbol": "INTC"},
    {"code": "NFLX", "name": "奈飞", "type": "stock_us", "symbol": "NFLX"},
    
    # === 美股其他热门股票 ===
    {"code": "BABA", "name": "阿里巴巴", "type": "stock_us", "symbol": "BABA"},
    {"code": "JD", "name": "京东", "type": "stock_us", "symbol": "JD"},
    {"code": "PDD", "name": "拼多多", "type": "stock_us", "symbol": "PDD"},
    {"code": "NIO", "name": "蔚来", "type": "stock_us", "symbol": "NIO"},
    {"code": "BIDU", "name": "百度", "type": "stock_us", "symbol": "BIDU"},
    {"code": "V", "name": "Visa", "type": "stock_us", "symbol": "V"},
    {"code": "MA", "name": "万事达", "type": "stock_us", "symbol": "MA"},
    {"code": "DIS", "name": "迪士尼", "type": "stock_us", "symbol": "DIS"},
    {"code": "COIN", "name": "Coinbase", "type": "stock_us", "symbol": "COIN"},
    {"code": "SQ", "name": "Block", "type": "stock_us", "symbol": "SQ"},
    
    # === 全球主要指数 ===
    {"code": "^GSPC", "name": "标普500", "type": "index", "symbol": "^GSPC"},
    {"code": "^DJI", "name": "道琼斯", "type": "index", "symbol": "^DJI"},
    {"code": "^IXIC", "name": "纳斯达克", "type": "index", "symbol": "^IXIC"},
    {"code": "^NDX", "name": "纳斯达克100", "type": "index", "symbol": "^NDX"},
    {"code": "^RUT", "name": "罗素2000", "type": "index", "symbol": "^RUT"},
    {"code": "^FTSE", "name": "富时100", "type": "index", "symbol": "^FTSE"},
    {"code": "^GDAXI", "name": "德国DAX", "type": "index", "symbol": "^GDAXI"},
    {"code": "^N225", "name": "日经225", "type": "index", "symbol": "^N225"},
    {"code": "^HSI", "name": "恒生指数", "type": "index", "symbol": "^HSI"},
    {"code": "000001.SS", "name": "上证指数", "type": "index", "symbol": "000001.SS"},
    
    # === 大宗商品 ===
    {"code": "GC=F", "name": "黄金期货", "type": "commodity", "symbol": "GC=F"},
    {"code": "SI=F", "name": "白银期货", "type": "commodity", "symbol": "SI=F"},
    {"code": "CL=F", "name": "原油期货", "type": "commodity", "symbol": "CL=F"},
    {"code": "NG=F", "name": "天然气期货", "type": "commodity", "symbol": "NG=F"},
    {"code": "HG=F", "name": "铜期货", "type": "commodity", "symbol": "HG=F"},
    
    # === 外汇（通过 Yahoo Finance）===
    {"code": "EURUSD=X", "name": "欧元/美元", "type": "forex", "symbol": "EURUSD=X"},
    {"code": "GBPUSD=X", "name": "英镑/美元", "type": "forex", "symbol": "GBPUSD=X"},
    {"code": "JPYUSD=X", "name": "日元/美元", "type": "forex", "symbol": "JPYUSD=X"},
    {"code": "CNYUSD=X", "name": "人民币/美元", "type": "forex", "symbol": "CNYUSD=X"},
    
    # === ETF ===
    {"code": "SPY", "name": "标普500 ETF", "type": "etf", "symbol": "SPY"},
    {"code": "QQQ", "name": "纳斯达克100 ETF", "type": "etf", "symbol": "QQQ"},
    {"code": "IWM", "name": "罗素2000 ETF", "type": "etf", "symbol": "IWM"},
    {"code": "VTI", "name": "全市场ETF", "type": "etf", "symbol": "VTI"},
    {"code": "GLD", "name": "黄金ETF", "type": "etf", "symbol": "GLD"},
    
    # === QDII基金（中国投资海外）===
    {"code": "004046", "name": "华安纳斯达克100", "type": "fund_qdii", "benchmark": "^NDX"},
    {"code": "161125", "name": "易方达标普500", "type": "fund_qdii", "benchmark": "^GSPC"},
    {"code": "270042", "name": "广发纳斯达克100", "type": "fund_qdii", "benchmark": "^NDX"},
]

def get_crypto_data(symbol):
    """抓取加密货币数据（多数据源）"""
    # 数据源1: Binance
    try:
        exchange = ccxt.binance()
        ticker = exchange.fetch_ticker(symbol)
        return {
            "price": round(ticker['last'], 2),
            "change": round(ticker['percentage'], 2),
            "source": "Binance"
        }
    except:
        pass
    
    # 数据源2: OKX（备用）
    try:
        exchange = ccxt.okx()
        ticker = exchange.fetch_ticker(symbol)
        return {
            "price": round(ticker['last'], 2),
            "change": round(ticker['percentage'], 2),
            "source": "OKX"
        }
    except:
        pass
    
    # 数据源3: CoinGecko API（免费，无需认证）
    try:
        coin_id = symbol.split('/')[0].lower()
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if coin_id in data:
                return {
                    "price": round(data[coin_id]['usd'], 2),
                    "change": round(data[coin_id].get('usd_24h_change', 0), 2),
                    "source": "CoinGecko"
                }
    except:
        pass
    
    return None

def get_yahoo_data(symbol):
    """抓取美股/指数/商品数据（Yahoo Finance）"""
    try:
        ticker = yf.Ticker(symbol)
        
        # 尝试获取实时数据
        try:
            info = ticker.fast_info
            price = info.last_price
            prev_close = info.previous_close
            change = ((price - prev_close) / prev_close) * 100
        except:
            # 备用：历史数据
            hist = ticker.history(period="2d")
            if len(hist) >= 2:
                price = hist['Close'].iloc[-1]
                prev_close = hist['Close'].iloc[-2]
                change = ((price - prev_close) / prev_close) * 100
            else:
                return None
        
        return {
            "price": round(price, 2),
            "change": round(change, 2),
            "source": "Yahoo Finance"
        }
    except:
        return None

def get_fund_qdii_data(code, benchmark):
    """QDII基金估值（通过锚定指数）"""
    try:
        # 获取锚定指数的涨跌幅
        benchmark_data = get_yahoo_data(benchmark)
        if benchmark_data:
            # 获取基金净值
            url = f"http://fundgz.1234567.com.cn/js/{code}.js"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data_str = response.text.replace('jsonpgz(', '').replace(');', '')
                data = json.loads(data_str)
                return {
                    "price": float(data['dwjz']),
                    "change": benchmark_data['change'],  # 使用指数涨跌幅估算
                    "source": "天天基金+指数估算"
                }
    except:
        pass
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
        "data_source": "无",
        "success": False
    }
    
    try:
        data = None
        
        if item["type"] == "crypto":
            data = get_crypto_data(item["symbol"])
        elif item["type"] in ["stock_us", "index", "commodity", "forex", "etf"]:
            data = get_yahoo_data(item["symbol"])
        elif item["type"] == "fund_qdii":
            data = get_fund_qdii_data(item["code"], item["benchmark"])
        
        if data:
            result["price"] = data["price"]
            result["change_pct"] = data["change"]
            result["data_source"] = data["source"]
            result["success"] = True
            print(f"{data['change']:+.2f}% ({data['source']}) ✓")
        else:
            print("✗")
    
    except Exception as e:
        print(f"✗ {str(e)[:30]}")
    
    return result

def main():
    print("=" * 70)
    print(f"开始抓取 {len(ASSETS)} 个全球资产数据（增强版 - 多数据源）")
    print("=" * 70)
    
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
        
        # 添加延迟避免限流
        time.sleep(0.5)
    
    # 按类型分组
    grouped = {
        "crypto": [r for r in results if r["market"] == "crypto"],
        "stock_us": [r for r in results if r["market"] == "stock_us"],
        "index": [r for r in results if r["market"] == "index"],
        "commodity": [r for r in results if r["market"] == "commodity"],
        "forex": [r for r in results if r["market"] == "forex"],
        "etf": [r for r in results if r["market"] == "etf"],
        "fund_qdii": [r for r in results if r["market"] == "fund_qdii"],
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
    
    print("=" * 70)
    print(f"完成！成功: {success_count}/{len(results)}")
    print(f"成功率: {success_count/len(results)*100:.1f}%")
    print("=" * 70)
    
    # 显示数据源统计
    sources = {}
    for r in results:
        if r["success"]:
            source = r["data_source"]
            sources[source] = sources.get(source, 0) + 1
    
    print("\n数据源统计：")
    for source, count in sources.items():
        print(f"  {source}: {count} 个")

if __name__ == "__main__":
    main()
