---
name: lobster-investment-research
version: 1.0.0
description: "Sharp, no-BS investment research framework with multi-perspective debate, technicals, and sentiment. Fast conviction, bullet-point clarity, source-backed claims. Use when asked to analyze a stock, crypto token, DeFi protocol, or any investment target."
metadata:
  trigger: "investment research, analyze $TICKER, deep dive, thesis, should I buy, investment memo, due diligence"
  author: KK (@lobster_kk)
  homepage: https://github.com/NHIZR/lobster-investment-research
  category: data-fetching-analysis
  requires:
    web_search: "Search engine access for live data"
    web_fetch: "URL fetching for source verification"
---

# Lobster Investment Research 📊

**Direct. Sharp. Source-backed.**

A structured investment research framework that produces actionable memos with kill conditions. Covers stocks, crypto, DeFi protocols, and pre-token projects.

**Core principle**: Good analysis is falsifiable. Great analysis tells you exactly when you're wrong.

---

## Quick Start

**First run:** The agent reads `config.json` from this skill folder. If missing, it walks you through setup and saves one.

```
Input: $TICKER / Project name + Your initial gut feeling
    ↓
3-Step Process:
1. Find the 1-3 forces that actually matter
2. Stress-test with Devil's Advocate debate
3. Output: Actionable memo with kill conditions
    ↓
Decision: Go / No-Go / Watch
```

---

## Configuration

On first use, copy `config.example.json` → `config.json` and fill in your preferences. Or run:

```bash
chmod +x scripts/setup.sh && ./scripts/setup.sh
```

Key settings:
- **`preferred_lenses`** — Which of the 6 investment lenses you use most
- **`edge_definitions`** — Your personal Edge (what gives you an advantage)
- **`report_path`** — Where to save completed reports
- **`watchlist`** — Tickers/tokens you track regularly
- **`data_sources`** — API keys for CoinGecko, Etherscan, etc.

If `config.json` exists, don't ask again. Just use it.

---

## The Six Lenses

Pick 2-3 that fit the target. Using all six is a sign you don't know what matters. Full descriptions in `references/six-lenses.md`.

| # | Lens | Archetype | Best For |
|---|------|-----------|----------|
| 1 | Quality Compounder | Buffett | Established winners with durable moats |
| 2 | Imaginative Growth | a16z | Disruptors, new markets, TAM expansion |
| 3 | Fundamental L/S | Tiger Cubs | Mispriced assets, variant perception |
| 4 | Deep Value | Klarman | Beaten-down assets, margin of safety |
| 5 | Event-Driven | Ackman | Special situations, catalyst timelines |
| 6 | Macro-Tactical | Druckenmiller | Cycle timing, liquidity, risk-on/off |

---

## The Framework

### Step 0: Edge Check

Before writing anything, answer: **Does this target relate to my Edge?**

Your Edge is defined in `config.json` → `edge_definitions`. If you haven't defined one yet, see `references/edge-framework.md`.

```
Edge match: [Yes — which edge / No]
If no edge → Write the report, but conclusion defaults to "Watch" not "Go"
If edge matches → Flag it in TL;DR
```

### Step 1: Find The Forces (10 min)

- What 1-3 things will make or break this investment?
- What does the current price assume?
- Why might I be wrong?

### Step 2: Stress-Test (15 min)

For each force, map three scenarios (bull/bear/base). Probability-weight them.

### Step 3: Write The Memo (30 min)

See `references/report-template.md` for the full template and output requirements.

---

## Devil's Advocate

**Required in every report.** Full guide in `references/devils-advocate.md`.

1. **Burry (Contrarian)** — Where is the crowd wrong? What downside is nobody pricing?
2. **Graham (Safety Margin)** — Conservative liquidation value? Management selling at highs?
3. **Druckenmiller (Macro Cycle)** — Where in the cycle? Liquidity helping or hurting?

---

## Evidence Standards

Every claim needs a link. See `references/evidence-standards.md` for the full source hierarchy and verification checklist.

---

## Technical Snapshot & Sentiment Pulse

Include in every report when data is available. See `references/data-sources.md` for indicator definitions and data sources.

---

## Free Data Sources

No API keys needed for most. Full list with code snippets in `references/data-sources.md`.

| Source | Covers | Rate Limit |
|--------|--------|------------|
| DeFiLlama | TVL, revenue, fees, yields | No key needed |
| CoinGecko | Crypto prices, market caps | 10-30 calls/min free |
| Yahoo Finance | Stock quotes, charts | Unofficial, reliable |
| StockAnalysis.com | Financials, fundamentals | Web scraping |
| Etherscan | On-chain token data | 5 calls/sec free |
| Dune Analytics | Custom on-chain queries | 2,500 credits/month free |
| Token Terminal | Protocol financials | Free tier available |
| TradingView | Technical charts | Browser-based |

---

## Asset Adaptations

**Stocks**: Earnings, margins, moats. DCF + comps valuation. Sources: StockAnalysis, earnings calls, 10-K filings.

**Crypto/DeFi**: Revenue, tokenomics, ecosystem position. FDV/Revenue + P/S valuation. Sources: DeFiLlama, CoinGecko, governance forums.

**Pre-Token/Private**: Team, traction, timing. Market sizing + precedent transactions. Higher uncertainty discount.

---

## IRR Hurdles

| Type | Minimum IRR |
|------|-------------|
| Stock long | ≥15% |
| Stock short | ≥20-25% |
| Crypto long | ≥50% |

Below hurdle = Pass, regardless of narrative quality.

---

## Self-Scoring

Rate each report 1-10:

| Dimension | 10 means |
|-----------|----------|
| Thesis clarity | Falsifiable + variant view explicit |
| Evidence quality | 3+ primary sources with links |
| Valuation rigor | 2+ methods + sensitivity analysis |
| Risk framework | Specific kill conditions defined |
| Decision readiness | Entry/exit/sizing all specified |

Target average: ≥7.5

---

## Common Mistakes

- **"It depends"** — Take a side. You can be wrong. You cannot be vague.
- **Recency bias** — One quarter doesn't make a trend.
- **Consensus as insight** — If everyone agrees, it's priced in.
- **Missing kill conditions** — No exit trigger = no thesis.
- **Fantasy valuation** — Heroic assumptions = pass.

---

## Red Team Checklist

Before finalizing any report. See `references/red-team-checklist.md`.

- [ ] Strongest bear case articulated?
- [ ] Kill conditions specific and measurable?
- [ ] What evidence would prove me wrong?
- [ ] Who's on the other side of this trade?
- [ ] Devil's Advocate section complete?
- [ ] All claims have source links?

---

## Time Budget

**Total: 60-90 minutes**
- Force identification: 10 min
- Research & sources: 20 min
- Writing: 30 min
- Red team & review: 10-20 min

If you can't form conviction in 90 minutes, pass.

---

## File Structure

See `README.md` for the full directory layout and installation instructions.

---

## Version

- **Current**: 1.0.0
- **Lineage**: Built from the private research framework behind [@lobster_kk](https://x.com/lobster_kk)

**The bottom line**: Good research tells you what to buy. This framework tells you exactly when you're wrong.
