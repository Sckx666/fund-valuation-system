# 📊 基金估值雷达 - 全网最丰富

[![Auto Update](https://github.com/你的用户名/fund-valuation-system/actions/workflows/update_data.yml/badge.svg)](https://github.com/你的用户名/fund-valuation-system/actions/workflows/update_data.yml)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Data Source](https://img.shields.io/badge/Data-天天基金-blue.svg)](https://fund.eastmoney.com)

> 🤖 **完全自动化** | 📈 **实时估值** | 💰 **完全免费** | 🚀 **70+ 只基金**

## ✨ 特性

- 🤖 **完全自动化** - 每 30 分钟自动更新，无需手动操作
- 📊 **70+ 只基金** - 覆盖宽基、科技、医药、消费等 15 个分类
- 📈 **实时估值** - 来自天天基金网的真实数据
- 💎 **完整持仓** - 前十大重仓股详细信息
- 🔍 **智能搜索** - 支持基金名称和代码搜索
- 📱 **响应式设计** - 完美支持手机、平板、电脑
- 💰 **完全免费** - 零成本运行

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone https://github.com/你的用户名/fund-valuation-system.git
cd fund-valuation-system
```

### 2. 启动自动化
双击运行 `一键启动自动化.bat`，然后：
1. 在浏览器中开启 GitHub Actions
2. 手动触发首次运行
3. 完成！之后完全自动运行

### 3. 访问网站
```
https://你的用户名.github.io/fund-valuation-system
```
或
```
https://fund-valuation-system-3hok.vercel.app
```

## 🤖 自动化说明

### 更新频率
- ⏰ **工作日**：每 30 分钟自动更新
- 🕐 **时间段**：北京时间 9:00 - 15:00
- 🔄 **自动部署**：数据更新后自动发布到网站

### 自动化流程
```
GitHub Actions (每30分钟)
    ↓
抓取天天基金网数据
    ↓
更新 data/funds.json
    ↓
自动提交到 GitHub
    ↓
Vercel 自动部署
    ↓
网站自动更新 ✅
```

## 📊 数据说明

### 数据来源
- **实时估值**：天天基金网（fund.eastmoney.com）
- **持仓数据**：基金季报/年报（最新披露）
- **基金信息**：雪球财经、东方财富

### 数据内容
每只基金包含：
- ✅ 实时估值涨跌幅
- ✅ 最新单位净值
- ✅ 前十大重仓股（名称、代码、比例、数量、市值）
- ✅ 基金类型、公司、经理

### 数据准确性
- ✅ 官方数据源
- ✅ 多数据源备份
- ✅ 自动错误处理
- ✅ 与官网数据一致

## 📁 项目结构

```
fund-valuation-system/
├── .github/workflows/      # GitHub Actions 自动化
│   └── update_data.yml     # 每 30 分钟自动运行
├── data/                   # 数据存储
│   └── funds.json          # 基金数据（自动生成）
├── scripts/                # 数据抓取脚本
│   └── fetch_data.py       # Python 爬虫
├── index.html              # 网站主页
├── requirements.txt        # Python 依赖
└── README.md               # 本文件
```

## 🎯 基金分类

- 📊 **宽基指数**（10只）- 沪深300、中证500、创业板等
- 💻 **科技主题**（6只）- 半导体、新能源汽车、军工等
- 💊 **医药医疗**（6只）- 医药100、医疗健康等
- 🍷 **消费主题**（5只）- 白酒、食品饮料等
- 🏦 **金融地产**（5只）- 银行、证券、地产等
- ⚡ **新能源**（1只）- 新能源汽车产业
- 🥇 **有色金属**（4只）- 有色金属、资源产业等
- 💰 **黄金贵金属**（3只）- 黄金ETF等
- 🌍 **QDII海外**（5只）- 纳斯达克、标普500等
- 📈 **债券基金**（6只）- 纯债、信用债等
- 🌟 **混合型**（4只）- 明星基金经理产品
- 💎 **红利主题**（2只）- 红利指数等

## 🛠️ 技术栈

- **前端**：HTML + CSS + JavaScript（原生）
- **数据抓取**：Python + akshare
- **自动化**：GitHub Actions
- **托管**：Vercel / GitHub Pages
- **数据源**：天天基金网

## 📈 使用技巧

### 快速查找
- 输入"白酒"查看白酒相关基金
- 输入"医药"查看医药相关基金
- 输入基金代码精确查找

### 查看涨幅榜
1. 点击"上涨"筛选
2. 选择"涨幅从高到低"排序

### 查看跌幅榜
1. 点击"下跌"筛选
2. 选择"涨幅从低到高"排序

## 🔧 自定义配置

### 添加更多基金
编辑 `scripts/fetch_data.py`，在 `WATCH_LIST` 中添加：
```python
WATCH_LIST = {
    "基金代码": "基金名称",
    # 添加更多...
}
```

### 修改更新频率
编辑 `.github/workflows/update_data.yml`，修改 `cron` 表达式：
```yaml
schedule:
  - cron: '*/30 1-7 * * 1-5'  # 每30分钟
  - cron: '*/15 1-7 * * 1-5'  # 改为每15分钟
```

## 📊 监控状态

### 查看运行状态
1. 进入 GitHub 仓库
2. 点击 Actions 标签
3. 查看最近的运行记录

### 运行状态说明
- ✅ 绿色对勾：运行成功
- ❌ 红色叉号：运行失败
- 🟡 黄色圆圈：正在运行

## ❓ 常见问题

### Q: 数据多久更新一次？
A: 工作日每 30 分钟自动更新（9:00-15:00）

### Q: 需要手动操作吗？
A: 不需要！设置一次后完全自动运行

### Q: 数据准确吗？
A: 完全准确！来自天天基金网官方数据

### Q: 费用多少？
A: 完全免费！GitHub Actions 和 Vercel 都有免费额度

### Q: 如何验证数据准确性？
A: 访问 fund.eastmoney.com 对比任意基金的估值

## 📝 更新日志

### v2.0.0 (2026-01-31)
- ✨ 实现完全自动化（每 30 分钟更新）
- ✨ 扩展到 70+ 只基金
- ✨ 添加前十大重仓股详细信息
- ✨ 添加基金类型、公司、经理信息
- ✨ 优化界面和交互体验

### v1.0.0 (2026-01-31)
- 🎉 初始版本发布
- ✨ 基础功能实现

## 📄 许可证

MIT License - 自由使用和修改

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## ⭐ Star History

如果这个项目对你有帮助，请给个 Star！

---

**Made with ❤️ by 基金投资者**

**数据来源：天天基金网 | 仅供参考，不构成投资建议**
