import React, { useState, useEffect } from 'react';
import './index.css';

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [view, setView] = useState('global'); // 'global' or 'funds'

  useEffect(() => {
    loadData();
  }, [view]);

  const loadData = () => {
    setLoading(true);
    const dataFile = view === 'global' ? '/data/global_assets.json' : '/data/funds.json';
    
    fetch(`${dataFile}?t=${Date.now()}`)
      .then(res => res.json())
      .then(jsonData => {
        setData(jsonData);
        setLoading(false);
      })
      .catch(err => {
        console.error("加载失败:", err);
        setLoading(false);
      });
  };

  const renderTag = (type) => {
    if (type === 'crypto') return <span className="tag crypto">💰 Crypto</span>;
    if (type.includes('stock') || type === 'index') return <span className="tag stock">📈 Stock</span>;
    if (type === 'commodity') return <span className="tag gold">🛢️ Commodity</span>;
    return <span className="tag fund">📊 Fund</span>;
  };

  const renderPrice = (item) => {
    if (item.market && item.market.includes('fund')) {
      return <div className="label">实时估值波动</div>;
    }
    
    let price = Number(item.price);
    if (price === 0) return null;
    
    let priceStr = price > 1000 ? parseInt(price).toLocaleString() : price.toFixed(2);
    return <div className="price">${priceStr}</div>;
  };

  const renderGlobalAssets = () => {
    if (!data || !data.assets) return null;

    const grouped = data.grouped || {};
    const sections = [
      { key: 'crypto', title: '💰 加密货币', icon: '₿' },
      { key: 'index', title: '📈 全球指数', icon: '📊' },
      { key: 'stock_us', title: '🇺🇸 美股科技', icon: '💻' },
      { key: 'commodity', title: '🛢️ 大宗商品', icon: '⚡' },
      { key: 'fund_qdii', title: '🌏 QDII基金', icon: '🌍' },
      { key: 'fund_cn', title: '🇨🇳 A股基金', icon: '📈' }
    ];

    return (
      <>
        {sections.map(section => {
          const items = grouped[section.key] || [];
          const successItems = items.filter(item => item.success);
          
          if (successItems.length === 0) return null;

          return (
            <div key={section.key} className="section">
              <h2 className="section-title">{section.title}</h2>
              <div className="grid">
                {successItems.map((item, i) => (
                  <div key={i} className="card">
                    <div className="card-top">
                      <div>
                        <h3>{item.name}</h3>
                        <small className="code">{item.code}</small>
                      </div>
                      {renderTag(item.market)}
                    </div>
                    <div className="card-main">
                      {renderPrice(item)}
                      <div className={`change ${item.change_pct >= 0 ? 'up' : 'down'}`}>
                        {item.change_pct > 0 ? '+' : ''}
                        {Number(item.change_pct).toFixed(2)}%
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          );
        })}
      </>
    );
  };

  const renderFunds = () => {
    if (!data || !data.funds) return null;

    return (
      <div className="grid">
        {data.funds.filter(f => f.success).map((fund) => (
          <div key={fund.code} className="card">
            <div className="card-header">
              <h3>{fund.name}</h3>
              <span className="code">{fund.code}</span>
            </div>

            <div className={`estimation ${fund.estimation >= 0 ? 'up' : 'down'}`}>
              {fund.estimation > 0 ? '+' : ''}{fund.estimation.toFixed(2)}%
              <small>实时估值</small>
            </div>

            {fund.holdings && fund.holdings.length > 0 && (
              <div className="holdings">
                <h4>前十大重仓 ({fund.holdings.length})</h4>
                <ul>
                  {fund.holdings.slice(0, 5).map((stock, index) => (
                    <li key={index}>
                      <span>{stock.股票名称}</span>
                      <span className="weight">{stock.持仓比例}%</span>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
    );
  };

  if (loading) {
    return (
      <div className="loading">
        <div className="spinner"></div>
        <p>正在连接全球市场...</p>
      </div>
    );
  }

  if (!data) {
    return (
      <div className="error">
        <h3>⚠️ 暂无数据</h3>
        <p>请运行数据抓取脚本生成数据</p>
      </div>
    );
  }

  return (
    <div className="container">
      <header className="header">
        <div>
          <h1>{view === 'global' ? '🌍 全球资产雷达' : '📊 基金估值雷达'}</h1>
          <p className="subtitle">
            {view === 'global' ? '加密货币 · 美股 · 指数 · 商品' : '全网最丰富 · 双重估值系统'}
          </p>
        </div>
        
        <div className="header-info">
          <div className="nav-buttons">
            <button 
              className={`nav-btn ${view === 'funds' ? 'active' : ''}`}
              onClick={() => setView('funds')}
            >
              📊 基金估值
            </button>
            <button 
              className={`nav-btn ${view === 'global' ? 'active' : ''}`}
              onClick={() => setView('global')}
            >
              🌍 全球资产
            </button>
          </div>
          
          <div className="header-meta">
            <span className="status-dot"></span>
            <span>🕐 {data.last_updated}</span>
          </div>
          
          <button className="refresh-btn" onClick={loadData}>
            🔄 刷新
          </button>
        </div>
      </header>

      <div className="stats">
        <div className="stat-card">
          <div className="stat-label">总数量</div>
          <div className="stat-value">{data.total_count || data.funds?.length || 0}</div>
        </div>
        <div className="stat-card">
          <div className="stat-label">成功获取</div>
          <div className="stat-value up">{data.success_count || 0}</div>
        </div>
      </div>

      {view === 'global' ? renderGlobalAssets() : renderFunds()}

      <footer className="footer">
        <p>数据源: {view === 'global' ? 'Binance / Yahoo Finance / AkShare' : '天天基金实时接口 / AkShare'}</p>
        <p>工作日自动更新 | 完全免费 | 开源项目</p>
      </footer>
    </div>
  );
}

export default App;
