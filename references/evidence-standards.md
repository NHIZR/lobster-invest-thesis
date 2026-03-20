# Evidence Standards

## Source Hierarchy

**Tier 1 (Need 3+):** CEO interviews, earnings transcripts, on-chain data, GitHub activity
**Tier 2 (Support):** Glassdoor reviews, job postings, patent filings, customer reviews
**Tier 3 (Context):** Analyst reports, news articles, social sentiment

## Hard Rules

- **No fabricated quotes.** If you don't have the exact source, say so.
- **No fabricated URLs.** Never invent or guess a URL. Only include links you have retrieved and verified via `web_search` or `web_fetch`. If a source exists but you cannot find the exact URL, describe the source (e.g., "Aave Q3 2025 earnings call transcript") without a fake link.
- **Every claim needs a link.** If you cannot find a source after searching, mark the claim as `[unverified]` and note what you searched for. An honest `[unverified]` tag is far better than a hallucinated link.

## AI Hallucination Prevention

LLMs can confidently generate plausible-looking but nonexistent URLs, quotes, and statistics. Guard against this:

1. **Search before citing.** Use `web_search` to find real sources. Do not rely on training data for URLs — they may be outdated or invented.
2. **Verify before linking.** Use `web_fetch` on any URL you plan to include. If it returns a 404 or unrelated content, drop the link.
3. **Prefer data APIs over memory.** Use DeFiLlama, CoinGecko, and other APIs from `references/data-sources.md` to get live numbers. Never cite a statistic from memory when an API can provide the current value.
4. **Flag uncertainty.** If a data point cannot be verified, prefix it with `[estimated]` or `[unverified]` and explain the basis for the estimate.

## Verification Checklist

- [ ] 3+ Tier 1 sources cited?
- [ ] All URLs tested via `web_fetch` and accessible?
- [ ] No fabricated or hallucinated quotes or URLs?
- [ ] Claims dated (data can go stale fast)?
- [ ] Conflicting sources noted and reconciled?
- [ ] Statistics sourced from live APIs, not from memory?
