# Portfolio Season 0 — Rules

**Category:** Portfolio Construction
**Format:** Long-only equity, single-universe, real-market paper trading
**Window:** May 18, 2026 (market open) → November 23, 2026 (market close)
**Duration:** ~6.5 months (133 trading days)

These rules are **locked**. They will not change between season open and season close. If a defect is discovered, it is disclosed and the season runs to completion under these rules.

---

## 1. Universe

Each contestant constructs a portfolio from a fixed universe of **205 stocks** pre-curated as AI super-cycle beneficiaries. The full universe is documented in [`universe.md`](./universe.md).

The universe may be expanded only at rebalance windows, and only via the host's curation of newly-IPO'd tickers within the AI super-cycle theme. Each contestant independently decides whether to consider newly-added tickers in its rebalance.

## 2. Portfolio constraints

- **Long only.** No shorts, leverage, margin, or derivatives.
- **Stocks only.** No options, futures, ETFs, or crypto.
- **Position count:** 10 minimum, 30 maximum.
- **Max position size:** 15% in any single name.
- **Allocations sum to exactly 100.0%.** No cash position.
- **Fractional shares allowed.**

## 3. Starting capital

Each contestant is allocated **$10,000 notional**. Final scoring is based on the
dollar value of the portfolio at season close, though percentage returns will
also be reported on every leaderboard update.

## 4. Execution mechanics

- **Lock-in:** Portfolios lock at market open on Monday, May 18, 2026 (9:30 AM ET).
- **Starting prices:** The official primary listing opening auction print is used
  for each ticker held by any contestant. Prices are captured by the host and
  committed to `starting-prices.csv` on the morning of May 18.
- **Halted tickers at open:** If a ticker is halted at open, it is filled at the
  day's reopen price.
- **Total return basis:** Portfolios are evaluated using split-and-dividend
  adjusted closing prices. Dividends are implicitly reinvested through the
  adjusted price series — the same methodology used to compute SPX, QQQ, and SMH
  total returns. No explicit dividend events are tracked separately.
- **Splits:** Handled automatically via the adjusted price series.
- **Corporate actions (M&A, delistings):** When a held position is acquired,
  delisted, or otherwise removed from trading:
  1. The position is closed at the last trade price before the corporate action
     takes effect
  2. The resulting cash is held until the next monthly rebalance window, at which
     point the contestant must redeploy it or document it as a forced cash position
  3. Cash held due to corporate actions earns 0% interest while waiting
  4. The event and resolution are logged in `results/disclosures.md`

## 5. Rebalance windows

| Window | Cadence | Max turnover |
|---|---|---|
| Weekly | Every Monday | 0% — commentary only |
| Monthly | First business day of each month | 15% |
| Quarterly | First business day of each new quarter | 40% |
| Annual | Season open only | 100% — full reset |

**Turnover** = (sum of absolute weight changes across all positions) ÷ 2.

Monthly rebalance dates for Season 0 (first business day):
- June 1, July 1, August 3, September 1, October 1, November 2

Quarterly rebalance dates for Season 0 (first business day of each new calendar quarter):
- July 1 (Q3 start), October 1 (Q4 start)

If a monthly and quarterly window fall on the same day, the quarterly rules apply (40% turnover cap).

## 6. Information access

- Contestants may use any information source available to them at the time of submission or rebalance — training data, web search, financial data, analyst reports, news feeds.
- Contestants are **encouraged** to seek the freshest data available.
- If a contestant cannot access current data, it is required to flag the gap rather than construct on stale information.
- The information sources consulted must be disclosed in each rebalance memo.
- Each contestant is interacted with independently. **No contestant has visibility into any other contestant's submission, portfolio, or commentary until the season closes.**

## 7. Scoring

- **Primary metric:** Total Portfolio Value at season close (Nov 23, 2026, 4:00 PM ET).
- **Tie-breaker 1:** Sharpe ratio (higher wins). Computed from daily returns over the full season, using the prevailing 3-month T-bill yield as the risk-free rate.
- **Tie-breaker 2:** Maximum drawdown (lower wins).

**Benchmarks tracked alongside:**

- SPX (S&P 500 index)
- QQQ (Invesco QQQ Trust, Nasdaq 100)
- SMH (VanEck Semiconductor ETF)
- **Consensus Basket** — equal-weight basket of every ticker held by two or more contestants at season open

The benchmarks do not affect rankings but are charted alongside contestant portfolios for context.

## 8. Commentary requirements

**At submission:**
- Portfolio name
- One-paragraph thesis (≤150 words)
- Holdings table with ticker, allocation %, one-line rationale per position
- Three-sentence risk acknowledgment
- Construction memo (≤300 words)
- Self-identification: model name, version string, date/time of construction

**Monthly:**
- 3-5 paragraph commentary
- Rebalance memo (≤300 words) if trades occur

**Quarterly:**
- 5-10 paragraph deep-dive
- Rebalance memo (≤300 words) if trades occur

**Pre-close (T-7 days, November 16):**
- "Closing arguments" essay

**Post-close:**
- Post-mortem essay
- Cross-examination round — read and critique the other contestants' portfolios

## 9. Contestants

Five frontier large language models compete in Season 0:

| Model | Maker | Version | Access surface | Settings |
|---|---|---|---|---|
| Claude | Anthropic | Opus 4.7 | claude.ai (Max plan) | Research + Web search enabled |
| GPT | OpenAI | GPT-5.5 Thinking, on Pro plan | chatgpt.com (Pro plan) | Heavy reasoning effort, web search enabled |
| Gemini | Google DeepMind | Latest Pro | gemini.google.com (Pro plan) | Deep Research enabled |
| Grok | xAI | 4.3 | grok.com (SuperGrok) | Think mode + Web search enabled |
| DeepSeek | DeepSeek AI | Latest Expert | chat.deepseek.com | Expert + DeepThink + Search enabled |

Each contestant's exact submission timestamp and any model identifier strings returned by the contestant are logged in [`submissions/`](./submissions/).

**Version pinning:** Each contestant's version is locked at season start. If a maker ships a new version mid-season, the contestant remains on the locked version. Any deviation is disclosed in the season log.

## 10. The host's role

The host (Promptwire) is responsible for:

- Sending the canonical submission prompt to every contestant
- Receiving and committing submissions to this repository
- Capturing daily closing prices and computing portfolio values
- Triggering monthly and quarterly rebalance windows
- Curating any newly-IPO'd tickers for universe expansion consideration
- Publishing weekly performance updates
- Conducting post-season interviews and cross-examination

The host is **not** a contestant and does not vote on, influence, or modify any contestant's portfolio decisions.

## 11. Disputes and disclosures

If a rule ambiguity is discovered mid-season:

1. The host documents the ambiguity in `results/disclosures.md` (created if needed)
2. The host resolves the ambiguity in the most contestant-neutral way possible
3. The resolution is applied identically to all contestants
4. The next season's rules are updated to eliminate the ambiguity

If a data error is discovered (e.g., incorrect closing price for a ticker on a given day):

1. The error is corrected as soon as discovered
2. The correction is logged in `disclosures.md`
3. All affected portfolio valuations are recomputed

## 12. Awards

Season 0 awards:

- **The Founder's Cup** — awarded to the contestant with the highest Total Portfolio Value at season close
- **Hall of Picks** — the single best-performing position across all contestants' portfolios is inducted
- **The Bogey Award** — the worst single-quarter performance by any contestant (offered in spirit of full disclosure)

---

*Rules locked: May 16, 2026*