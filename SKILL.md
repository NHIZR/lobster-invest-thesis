---
name: lobster-invest-thesis
description: "Structured investment research framework producing actionable memos with kill conditions, valuation, and Devil's Advocate debate. Use when analyzing stocks, crypto tokens, DeFi protocols, or any investment target. Triggers on: 'analyze $TICKER', 'should I buy', 'investment thesis', 'due diligence', 'deep dive on', 'research this stock/token', 'what do you think about $X as an investment', 'investment memo', or any request for investment analysis — even casual ones like 'is $X worth buying' or 'look into $TICKER for me'."
metadata:
  trigger: "investment research, analyze $TICKER, deep dive, thesis, should I buy, investment memo, due diligence"
  category: data-fetching-analysis
  requires:
    web_search: "Search engine access for live data"
    web_fetch: "URL fetching for source verification"
---

# Lobster Invest Thesis

Produce actionable investment memos with kill conditions. Cover stocks, crypto, DeFi protocols, and pre-token projects.

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

On first use, read `config.json` from this skill folder. If missing, copy `config.example.json` → `config.json` and walk the user through setup. If `config.json` exists, use it silently.

---

## The Six Lenses

Select 2-3 lenses that fit the target. Using all six signals lack of focus. Read `references/six-lenses.md` for full descriptions and kill signals.

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

Check `config.json` → `edge_definitions` for the user's defined edges. If none defined, see `references/edge-framework.md`.

```
Edge match: [Yes — which edge / No]
If no edge → Write the report, but default conclusion to "Watch" not "Go"
If edge matches → Flag it in TL;DR
```

### Step 1: Find The Forces

Identify 1-3 forces that will make or break this investment. Answer:
- What assumptions does the current price embed?
- Why might those assumptions be wrong?

### Step 2: Stress-Test

For each force, map three scenarios (bull/bear/base). Assign probability weights.

### Step 3: Write The Memo

Follow `references/report-template.md` for the full template and output requirements.

---

## Devil's Advocate

Include in every report. Follow `references/devils-advocate.md` for the full execution guide.

Attack the thesis from three perspectives:
1. **Burry (Contrarian)** — Where is the crowd wrong? What downside is nobody pricing?
2. **Graham (Safety Margin)** — Conservative liquidation value? Management selling at highs?
3. **Druckenmiller (Macro Cycle)** — Where in the cycle? Liquidity helping or hurting?

---

## Evidence Standards

Back every claim with a link. Follow `references/evidence-standards.md` for the source hierarchy and verification checklist.

---

## Technical Snapshot & Sentiment Pulse

Include both sections in every report when data is available. Use `references/data-sources.md` for indicator definitions and data endpoints.

---

## Data Sources

Use `scripts/fetch_data.py` for quick data pulls (DeFiLlama, CoinGecko, Yahoo Finance — no API key needed). See `references/data-sources.md` for the full list with additional endpoints and rate limits.

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

Run before finalizing any report. See `references/red-team-checklist.md` for the full checklist.

- [ ] Strongest bear case articulated?
- [ ] Kill conditions specific and measurable?
- [ ] What evidence would prove me wrong?
- [ ] Who's on the other side of this trade?
- [ ] Devil's Advocate section complete?
- [ ] All claims have source links?

---

## File Structure

See `README.md` for the full directory layout and installation instructions.

---

**The bottom line**: Good research tells you what to buy. This framework tells you exactly when you're wrong.
