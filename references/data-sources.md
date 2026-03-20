# Free Data Sources

No API key required for most of these. Where a key is needed, the free tier is sufficient for research.

---

## DeFi / Crypto

### DeFiLlama (No Key)

```bash
# Protocol TVL & chain breakdown
curl -s "https://api.llama.fi/protocol/{protocol-slug}" | jq '.tvl, .currentChainTvls'

# Protocol revenue and fees
curl -s "https://api.llama.fi/summary/fees/{protocol-slug}" | jq '.total24h, .total7d'

# All protocols ranked by TVL
curl -s "https://api.llama.fi/protocols" | jq '.[0:10] | .[] | {name, tvl}'

# Stablecoin supply data
curl -s "https://stablecoins.llama.fi/stablecoins" | jq '.peggedAssets[] | select(.symbol=="USDC") | .circulating'

# Yield farming pools
curl -s "https://yields.llama.fi/pools" | jq '.data[] | select(.project=="aave") | {pool, tvlUsd, apy}'
```

**Docs:** https://defillama.com/docs/api

### CoinGecko (Free: 10-30 calls/min)

```bash
# Current price + market data
curl -s "https://api.coingecko.com/api/v3/coins/{coin-id}?localization=false&tickers=false" \
  | jq '.market_data | {price: .current_price.usd, mcap: .market_cap.usd, volume: .total_volume.usd}'

# 30-day price history
curl -s "https://api.coingecko.com/api/v3/coins/{coin-id}/market_chart?vs_currency=usd&days=30" \
  | jq '.prices | length'

# Simple price lookup (multiple coins)
curl -s "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,aave&vs_currencies=usd&include_24hr_change=true"

# Trending coins
curl -s "https://api.coingecko.com/api/v3/search/trending" | jq '.coins[] | .item.name'
```

**Pro tip:** Use coin IDs, not tickers. Find IDs at https://api.coingecko.com/api/v3/search?query={name}

### Etherscan (Free: 5 calls/sec)

```bash
# Token total supply
curl -s "https://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress={address}&apikey={key}"

# Account balance
curl -s "https://api.etherscan.io/api?module=account&action=balance&address={address}&apikey={key}"

# Token transfers for an address
curl -s "https://api.etherscan.io/api?module=account&action=tokentx&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={key}"
```

**Get free key:** https://etherscan.io/apis

### Direct RPC (No Key)

```bash
# ETH balance via public RPC
curl -s -X POST https://eth.llamarpc.com \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"eth_getBalance","params":["{address}","latest"],"id":1}'
```

---

## Stocks / Traditional Finance

### Yahoo Finance (Unofficial, no key)

```bash
# Current quote
curl -s "https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?interval=1d&range=1d" \
  | jq '.chart.result[0].meta | {price: .regularMarketPrice, prevClose: .previousClose}'

# 1-year daily data
curl -s "https://query1.finance.yahoo.com/v8/finance/chart/{TICKER}?interval=1d&range=1y" \
  | jq '.chart.result[0].indicators.quote[0].close | length'
```

**Note:** Yahoo's unofficial API may rate-limit aggressively. Use web_fetch as fallback.

### StockAnalysis.com (Web scraping)

Best fetched via `web_fetch` tool:

```
https://stockanalysis.com/stocks/{TICKER}/financials/
https://stockanalysis.com/stocks/{TICKER}/financials/?p=quarterly
https://stockanalysis.com/stocks/{TICKER}/financials/cash-flow-statement/
https://stockanalysis.com/stocks/{TICKER}/financials/balance-sheet/
```

Reliable for: revenue, net income, EPS, free cash flow, margins.

### SEC EDGAR (No key)

```bash
# Company filings
curl -s "https://efts.sec.gov/LATEST/search-index?q={company}&dateRange=custom&startdt=2024-01-01" \
  -H "User-Agent: YourName your@email.com"
```

---

## General Research

### Web Search
Use the agent's built-in `web_search` tool for:
- Recent news and developments
- Analyst commentary
- Competitor analysis
- Regulatory updates

### Web Fetch
Use the agent's `web_fetch` tool to pull full content from:
- Investor presentations
- Blog posts and analysis
- Governance forum discussions
- Protocol documentation

---

## Rate Limit Guidelines

- **DeFiLlama:** No hard limit, but be reasonable (1 req/sec)
- **CoinGecko free:** 10-30 calls/min. Cache results within a session.
- **Yahoo Finance:** Unpredictable throttling. Space requests 2+ seconds apart.
- **Etherscan free:** 5 calls/sec, 100k calls/day.

When rate-limited, fall back to web_fetch on the provider's website.

---

## Additional Sources

### Dune Analytics

Community-built SQL dashboards for on-chain data across EVM chains, Solana, and more.

- **URL:** https://dune.com
- **API:** https://dune.com/docs/api/ (free tier: 2,500 credits/month)
- **Best for:** Custom on-chain queries, protocol-specific metrics, whale tracking, DEX volume

```bash
# Execute a saved query
curl -s "https://api.dune.com/api/v1/query/{query_id}/results" \
  -H "X-DUNE-API-KEY: {key}"
```

### Token Terminal

Fundamental financial metrics for crypto protocols — revenue, earnings, P/S, P/E ratios.

- **URL:** https://tokenterminal.com
- **API:** https://docs.tokenterminal.com (free tier available)
- **Best for:** Protocol revenue comparisons, financial multiples, growth metrics

```bash
# Protocol financials
curl -s "https://api.tokenterminal.com/v2/projects/{project_id}" \
  -H "Authorization: Bearer {key}"
```

### TradingView

Charting platform with technical analysis tools. No REST API, but useful for manual chart review and embedding.

- **URL:** https://www.tradingview.com
- **Best for:** Technical analysis, chart patterns, indicator overlays, community ideas
- **Usage:** Open `https://www.tradingview.com/chart/?symbol={EXCHANGE}:{TICKER}` via browser for interactive charts

---

## Technical Snapshot Reference

When including a Technical Snapshot in reports, cover these indicators:

- **RSI (14):** overbought (>70) / oversold (<30) / neutral
- **Price vs 50MA and 200MA:** trend direction and distance
- **Key support and resistance levels:** 2 each, from recent price action
- **Volume trend:** expanding, contracting, flat

**Crypto additions:** Active addresses, exchange net flows, whale wallet changes.

Sources: TradingView for charts, CoinGecko for crypto price data, DeFiLlama for on-chain metrics.

---

## Sentiment Pulse Reference

Quick scan of market mood for reports:

- **Social media sentiment:** fear ↔ greed spectrum
- **Discussion volume:** cold / normal / hot / overheated
- **Institutional positioning:** accumulating / flat / distributing
- **Sentiment-fundamental alignment:** yes/no + why

Sources: Twitter/X search, Reddit (r/wallstreetbets, r/cryptocurrency), governance forums, on-chain flow data from Etherscan/DeFiLlama.
