---
name: lobster-invest-thesis
version: 2.0.0
description: "Structured investment research framework producing actionable memos with kill conditions, valuation, and Devil's Advocate debate. Use when analyzing stocks, crypto tokens, DeFi protocols, or any investment target. Triggers on: 'analyze $TICKER', 'should I buy', 'investment thesis', 'due diligence', 'deep dive on', 'research this stock/token', 'investment memo', or any casual request like 'is $X worth buying'."
metadata:
  trigger: "investment research, analyze $TICKER, deep dive, thesis, should I buy, investment memo, due diligence"
  author: KK (@lobster_kk)
  category: data-fetching-analysis
  requires:
    web_search: "Search engine access for live data"
    web_fetch: "URL fetching for source verification"
---

# Lobster Invest Thesis 📊

**Direct. Sharp. Source-backed.**

Produce actionable investment memos with kill conditions. Cover stocks, crypto, DeFi protocols, and pre-token projects.

**Core Principle**: Good analysis is falsifiable. Great analysis tells you exactly when you're wrong.

---

## Quick Start

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

## The Six Lenses (Pick 2-3 That Fit)

Don't use all six — picking all signals lack of focus. See `references/six-lenses.md` for full descriptions and kill signals.

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

### Step 0: Edge Check (Before Everything)

Before writing any research, ask: **Does this target align with my defined Edge?**

Your Edge is the systematic advantage you bring. Define it using `references/edge-framework.md`. Common edge types:
- **Sentiment Mispricing** — Markets overreact to fear/greed; you see mean-reversion
- **Second-Order Thinking** — You trace causal chains others stop short of
- **Catalyst Timing** — You combine improving fundamentals with near-term catalysts for optimal entry

If no edge → still write the report, but conclude with "Watch" instead of "Go"
If edge exists → explicitly state it in TL;DR

### Step 0.5: Non-Price Signal Check

写研报时同时检查非价格信号（参考[[交易方法论#非价格信号源]]）：
- 宏观日历有没有相关事件？
- COT/资金流有没有极端仓位？
- CoinKarma 流动性正常吗？（Crypto）
- 有没有多层信号共振？

### Step 1: Find The Forces (10 min)

- What 1-3 things will make or break this investment?
- What's priced in? (What does current valuation assume?)
- Why might I be wrong?

Output: 3-bullet hypothesis

### Step 2: Stress-Test (15 min)

For each force, map three scenarios:
- Bull case (90th percentile)
- Bear case (10th percentile)
- Base case (your view)

Output: Probability-weighted scenarios

### Step 3: Write The Memo (30 min)

Follow `references/report-template.md` for the full template. Structure:

```
# $TICKER: [Thesis in 5-7 words]

## TL;DR (4 bullets)
- Thesis: [One-liner]
- Variant: [Market is wrong because...]
- Action: [Long/Short/Pass at $X]
- Kill: [Exit if Y happens]

## The Setup
## The Variant View
## Valuation (2+ methods + sensitivity)
## Catalysts (timeline)
## ⚔️ Devil's Advocate
## 📊 Technical Snapshot
## 🎭 Sentiment Pulse
## Risks & Kill Conditions
## Position Sizing
## Bottom Line
```

---

## Devil's Advocate（强制反方辩论）

**每份报告必须包含。** See `references/devils-advocate.md` for the full execution guide.

Attack the thesis from three perspectives:
1. **Burry（逆向）** — 市场在哪里犯了群体性错误？被忽视的下行风险？
2. **Graham（安全边际）** — 按最保守估值值多少？管理层在高位套现？
3. **Druckenmiller（宏观周期）** — 处于周期什么位置？流动性支持还是打压？

```markdown
## ⚔️ Devil's Advocate
**Burry 会说：** [...]
**Graham 会说：** [...]
**Druckenmiller 会说：** [...]
**反方最强论点：** [综合]
**我的回应：** [为什么仍持有 / 什么条件下认输]
```

---

## Evidence Standards

Back every claim with a link. See `references/evidence-standards.md` for source hierarchy and verification checklist.

**Tier 1 (Must Have 3+):** CEO interviews, earnings transcripts, on-chain data, GitHub activity
**Tier 2 (Support):** Glassdoor, job postings, patent filings
**Tier 3 (Context):** Analyst reports, news articles, social sentiment

**⚠️ Hard Rule**: No fabricated CEO quotes. If you don't have the source, don't quote it.

---

## Technical Snapshot & Sentiment Pulse

Include both in every report when data is available. See `references/data-sources.md` for indicator definitions and data endpoints.

### Technical Snapshot
```markdown
## 📊 Technical Snapshot
- RSI (14): XX — [超买/超卖/中性]
- 价格 vs 50MA: [上方 +X% / 下方 -X%]
- 价格 vs 200MA: [上方 +X% / 下方 -X%]
- 关键支撑: $XX / $XX
- 关键阻力: $XX / $XX
- 成交量: [放量/缩量/平稳]
- 技术倾向: [看多/看空/中性]
```

### Sentiment Pulse
```markdown
## 🎭 Sentiment Pulse
- 社交媒体情绪: [极度恐惧 / 恐惧 / 中性 / 贪婪 / 极度贪婪]
- 讨论热度: [冷门 / 一般 / 热门 / 过热]
- 机构动向: [增持 / 持平 / 减持]
- 情绪与基本面是否一致: [是/否 — 解释]
```

---

## Data Sources

See `references/data-sources.md` for the full list with endpoints, rate limits, and example commands.

Quick reference:
- **DeFi/Crypto:** DeFiLlama API, CoinGecko API (Free tier), Etherscan
- **Stocks:** StockAnalysis.com, Yahoo Finance Chart API
- **On-Chain:** Direct RPC via LlamaRPC

---

## Asset Adaptations

| Asset | Focus | Valuation | Sources |
|-------|-------|-----------|---------|
| **Stocks** | Earnings, margins, moats | DCF + comps | StockAnalysis, earnings calls, 10-K |
| **Crypto/DeFi** | Revenue, tokenomics, ecosystem | FDV/Revenue + P/S | DeFiLlama, CoinGecko, governance forums |
| **AI Agent** | Adoption, decentralization, sustainability | Network effects | Moltbook/Clawstr, GitHub, agent metrics |
| **Pre-Token** | Team, traction, timing | Market sizing + precedents | Pitch decks, user metrics |

---

## IRR Hurdles

| Type | Minimum IRR |
|------|-------------|
| Stock long | ≥15% |
| Stock short | ≥20-25% |
| Crypto long | ≥50% |

Below hurdle = Pass, regardless of narrative quality.

---

## Output Format Rules (KK Style)

- **Bullet points 为主** — 表格仅用于数字对比
- **[Sources as links](URL)** — Every claim needs a link
- **Skip throat-clearing** — No "In this memo we examine..."
- **Active voice** — "Management cut costs" not "Costs were reduced"
- **Concrete numbers** — Ranges OK, vagueness not OK

### Length Targets
- Executive Summary: 300-500 chars
- Full Memo: 8,000-15,000 chars
- Max: 20,000 chars

---

## Red Team Checklist

Run before finalizing any report. See `references/red-team-checklist.md` for the full checklist.

- [ ] Strongest bear case articulated?
- [ ] Kill conditions specific and measurable?
- [ ] What evidence would prove me wrong?
- [ ] Who's on the other side of this trade?
- [ ] Devil's Advocate section complete?
- [ ] All claims have source links?
- [ ] Technical Snapshot 查了吗？

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

## 存储路径

所有投研报告统一存到配置的输出目录。

默认路径（可在 agent 配置中覆盖）：
`./output/` 或用户指定的投研存储目录

文件命名：`YYYYMMDD--TICKER投研分析.md`（日期为首次创建日）

---

## Time Allocation

**Total: 60-90 minutes**
- Force identification: 10 min
- Research/sources: 20 min
- Writing: 30 min
- Red team/review: 10-20 min

**If you can't form conviction in 90 minutes, pass.**

---

## UX: Progress Updates

For long-running research tasks, inform the user:
- Before starting: estimated time (typically 2-3 minutes)
- After completion: summary + file location

---

## File Structure

```
~/clawd/skills/lobster-invest-thesis/
├── SKILL.md                      ← 本文件
└── references/
    ├── six-lenses.md             ← 6种投资视角详解
    ├── edge-framework.md         ← Edge 定义框架
    ├── report-template.md        ← 完整报告模板
    ├── devils-advocate.md        ← 反方辩论执行指南
    ├── evidence-standards.md     ← 证据标准与验证清单
    ├── red-team-checklist.md     ← Red Team 完整检查清单
    ├── data-sources.md           ← 数据源 + API endpoints
    └── example-report.md         ← 示例报告
```

---

**The Bottom Line**: Good research tells you what to buy. Great research tells you exactly when you're wrong.
