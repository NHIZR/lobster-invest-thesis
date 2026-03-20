#!/usr/bin/env python3
"""
Lobster Investment Research — Data Fetcher

Wraps common free API calls for DeFiLlama, CoinGecko, and Yahoo Finance.
No API keys required for basic usage.

Usage:
    python fetch_data.py defi <protocol-slug>       # DeFiLlama protocol data
    python fetch_data.py crypto <coin-id>            # CoinGecko coin data
    python fetch_data.py stock <TICKER>              # Yahoo Finance quote
    python fetch_data.py fees <protocol-slug>        # DeFiLlama fees/revenue
    python fetch_data.py yields <protocol>           # DeFiLlama yield pools

Examples:
    python fetch_data.py defi aave
    python fetch_data.py crypto bitcoin
    python fetch_data.py stock AAPL
    python fetch_data.py fees aave
"""

import json
import sys
import urllib.request
import urllib.error
from typing import Any


def fetch_json(url: str) -> Any:
    """Fetch JSON from a URL with a reasonable timeout."""
    req = urllib.request.Request(url, headers={"User-Agent": "LobsterResearch/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}", file=sys.stderr)
        sys.exit(1)


def defi_protocol(slug: str) -> None:
    """Fetch DeFiLlama protocol overview (TVL, chains)."""
    data = fetch_json(f"https://api.llama.fi/protocol/{slug}")
    result = {
        "name": data.get("name"),
        "tvl": data.get("tvl"),
        "chains": list(data.get("currentChainTvls", {}).keys()),
        "chain_tvls": data.get("currentChainTvls"),
        "category": data.get("category"),
        "url": data.get("url"),
    }
    print(json.dumps(result, indent=2))


def defi_fees(slug: str) -> None:
    """Fetch DeFiLlama fees and revenue data."""
    data = fetch_json(f"https://api.llama.fi/summary/fees/{slug}")
    result = {
        "name": slug,
        "total_24h": data.get("total24h"),
        "total_7d": data.get("total7d"),
        "total_30d": data.get("total30d"),
    }
    print(json.dumps(result, indent=2))


def defi_yields(protocol: str) -> None:
    """Fetch DeFiLlama yield pools for a protocol."""
    data = fetch_json("https://yields.llama.fi/pools")
    pools = [
        {"pool": p.get("pool"), "tvl_usd": p.get("tvlUsd"), "apy": p.get("apy")}
        for p in data.get("data", [])
        if p.get("project", "").lower() == protocol.lower()
    ]
    pools.sort(key=lambda x: x.get("tvl_usd") or 0, reverse=True)
    print(json.dumps(pools[:10], indent=2))


def crypto_coin(coin_id: str) -> None:
    """Fetch CoinGecko coin data (price, market cap, volume, supply)."""
    data = fetch_json(
        f"https://api.coingecko.com/api/v3/coins/{coin_id}"
        "?localization=false&tickers=false&community_data=false&developer_data=false"
    )
    md = data.get("market_data", {})
    result = {
        "name": data.get("name"),
        "symbol": data.get("symbol"),
        "price_usd": md.get("current_price", {}).get("usd"),
        "market_cap_usd": md.get("market_cap", {}).get("usd"),
        "fully_diluted_valuation": md.get("fully_diluted_valuation", {}).get("usd"),
        "total_volume_usd": md.get("total_volume", {}).get("usd"),
        "circulating_supply": md.get("circulating_supply"),
        "total_supply": md.get("total_supply"),
        "max_supply": md.get("max_supply"),
        "price_change_24h_pct": md.get("price_change_percentage_24h"),
        "price_change_7d_pct": md.get("price_change_percentage_7d"),
        "price_change_30d_pct": md.get("price_change_percentage_30d"),
        "ath": md.get("ath", {}).get("usd"),
        "ath_change_pct": md.get("ath_change_percentage", {}).get("usd"),
    }
    print(json.dumps(result, indent=2))


def stock_quote(ticker: str) -> None:
    """Fetch Yahoo Finance quote data."""
    data = fetch_json(
        f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
        "?interval=1d&range=5d"
    )
    meta = data.get("chart", {}).get("result", [{}])[0].get("meta", {})
    result = {
        "symbol": meta.get("symbol"),
        "price": meta.get("regularMarketPrice"),
        "previous_close": meta.get("previousClose"),
        "currency": meta.get("currency"),
        "exchange": meta.get("exchangeName"),
        "market_time": meta.get("regularMarketTime"),
    }
    print(json.dumps(result, indent=2))


COMMANDS = {
    "defi": ("protocol-slug", defi_protocol),
    "crypto": ("coin-id", defi_protocol),
    "stock": ("TICKER", stock_quote),
    "fees": ("protocol-slug", defi_fees),
    "yields": ("protocol", defi_yields),
}


def main() -> None:
    if len(sys.argv) < 3:
        print(__doc__.strip())
        sys.exit(1)

    cmd = sys.argv[1].lower()
    arg = sys.argv[2]

    if cmd == "defi":
        defi_protocol(arg)
    elif cmd == "crypto":
        crypto_coin(arg)
    elif cmd == "stock":
        stock_quote(arg)
    elif cmd == "fees":
        defi_fees(arg)
    elif cmd == "yields":
        defi_yields(arg)
    else:
        print(f"Unknown command: {cmd}")
        print(f"Available: {', '.join(COMMANDS.keys())}")
        sys.exit(1)


if __name__ == "__main__":
    main()
