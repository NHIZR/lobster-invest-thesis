# Lobster Invest Thesis 📊

A structured investment research framework for AI coding agents. Produces actionable memos with kill conditions, multi-perspective stress testing, and source-backed claims.

Built for [OpenClaw](https://github.com/nicepkg/openclaw) and [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Works with any AI agent that reads skill files.

## What Makes This Different

| Feature | Generic AI research | Lobster Invest Thesis |
|---------|--------------------|-----------------------------|
| Output | "Here are some considerations..." | Actionable memo with entry/exit/sizing |
| Conviction | Hedged, vague, "it depends" | Takes a side, names kill conditions |
| Debate | None | Devil's Advocate: 3 legendary investors attack your thesis |
| Sources | Claims without links | Source-backed — every claim linked |
| Valuation | Skipped or hand-wavy | 2+ methods with sensitivity ranges |
| Self-check | None | Red Team Checklist before every report |
| Edge | Generic | Your personal Edge defined in config |

## Install

### OpenClaw

```bash
cp -r lobster-invest-thesis/ ~/.openclaw/skills/lobster-invest-thesis/
```

### Claude Code

```bash
cp -r lobster-invest-thesis/ ~/.claude/skills/lobster-invest-thesis/
```

## Setup

**Option A: Quick setup**

```bash
chmod +x scripts/setup.sh && ./scripts/setup.sh
```

**Option B: Manual**

Copy `config.example.json` → `config.json` and edit:
- `preferred_lenses` — Your 2-3 most-used investment lenses
- `edge_definitions` — What gives you an investing advantage (see `references/edge-framework.md`)
- `report_path` — Where to save completed reports
- `watchlist` — Tickers/tokens you track
- `data_sources` — API keys (most sources are free)

## Usage

```
Analyze NVDA — data center dominance vs China risk
```

```
Deep dive on Aave — DeFi lending moat, revenue sustainability
```

```
Quick take on $BTC — halving cycle positioning
```

The agent picks the relevant lenses, checks your Edge, fetches live data, runs Devil's Advocate, and outputs a structured memo.

## Framework Overview

1. **Edge Check** — Does this target match your defined advantage?
2. **Six Lenses** — Pick 2-3 that fit (Buffett, a16z, Tiger Cubs, Klarman, Ackman, Druckenmiller)
3. **Force Identification** — 1-3 things that make or break the investment
4. **Stress Test** — Bull/bear/base scenarios, probability-weighted
5. **Devil's Advocate** — Burry (contrarian), Graham (safety margin), Druckenmiller (macro) attack your thesis
6. **Technical Snapshot** — RSI, moving averages, support/resistance, volume
7. **Sentiment Pulse** — Social mood, institutional positioning, sentiment-fundamental alignment
8. **Report** — Structured memo with valuation, catalysts, kill conditions, position sizing

## File Structure

```
lobster-invest-thesis/
├── SKILL.md                 ← Main skill file (agent reads this)
├── config.example.json      ← Configuration template
├── README.md                ← This file
├── references/
│   ├── six-lenses.md        ← Detailed guide for each lens
│   ├── devils-advocate.md   ← How to run the debate
│   ├── data-sources.md      ← Free APIs with code snippets
│   ├── edge-framework.md    ← Define your personal Edge
│   ├── example-report.md    ← Full sample report (public data)
│   └── red-team-checklist.md
└── scripts/
    ├── setup.sh             ← Quick setup — copies config template
    ├── fetch_data.py        ← Data fetcher (DeFiLlama, CoinGecko, Yahoo)
    └── README.md            ← Script documentation
```

## Requirements

- An AI agent that reads skill files (OpenClaw, Claude Code, or similar)
- Web search and URL fetching capabilities
- Optional: API keys for CoinGecko, Etherscan (free tiers work fine)

## Philosophy

Take a side. Name the price. Define the exit. If you can't say when you're wrong, you don't have a thesis.

## License

MIT
