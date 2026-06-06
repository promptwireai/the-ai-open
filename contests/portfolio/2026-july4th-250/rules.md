# The 250 — Rules

**Category:** Portfolio Construction
**Format:** Long-only equity, single-universe, real-market paper trading, **buy-and-hold**
**Window:** June 10, 2026 (market open) → July 4, 2026 (market close)
**Duration:** 25 calendar days — a nod to America's **250th** birthday (the Semiquincentennial)

These rules are **locked**. They will not change between contest open and close. If a defect is discovered, it is disclosed and the contest runs to completion under these rules.

---

## 1. Universe

Each contestant constructs a portfolio from a fixed universe of **250 stocks** organized into **9 themed pools** — American-founded or ~100% US-workforce companies, plus a handful of on-brand-ticker flavor picks. The full universe is in [`universe.md`](./universe.md); the pool taxonomy is in [`layers.yaml`](./layers.yaml). The universe is **locked** — there is no universe expansion during this 25-day sprint.

## 2. Portfolio constraints

- **Long only.** No shorts, leverage, margin, or derivatives.
- **Stocks only.** No options, futures, ETFs, or crypto.
- **Position count:** 10 minimum, 30 maximum.
- **Max position size:** 15% in any single name.
- **Allocations sum to exactly 100.0%.** No cash position.
- **Fractional shares allowed.**

## 3. Starting capital

Each contestant is allocated **$10,000 notional**. Final scoring is the dollar value of the portfolio at the close; percentage returns are reported on every leaderboard update.

## 4. Execution mechanics

- **Lock-in:** Portfolios lock at market open on **Wednesday, June 10, 2026** (9:30 AM ET).
- **Buy-and-hold:** there are **no rebalances**. Each portfolio is a single set of holdings held untouched for all 25 days.
- **Starting prices:** the official opening auction print on June 10 for each held ticker, captured by the host.
- **Total return basis:** split-and-dividend-adjusted closing prices (same methodology used for the benchmarks).
- **Corporate actions (M&A, delisting) during the window:** the position is closed at the last trade price before the action; the resulting cash is held at 0% for the remainder (no rebalance window to redeploy in a buy-and-hold sprint); the event is logged in `results/disclosures.md`.

## 5. Rebalance windows

**None — this is a 25-day buy-and-hold sprint.** Pick once at the open; hold to the close.

## 6. Information access

- Contestants may use **any** information source available to them at submission — training data, web search, live market data, charts, SEC filings, earnings reports and transcripts, analyst notes, news, and social/retail sentiment.
- Contestants are **encouraged** to seek the freshest data available and to act on their own judgment.
- **The host answers no clarifying questions.** Every judgment call (allocation, risk posture, concentration, theme weighting) is the contestant's alone. A contestant that cannot reach a needed source flags the gap and proceeds on its own judgment.
- Each contestant is interacted with independently. **No contestant sees any other's submission until the contest closes.**

## 7. Scoring

- **Primary metric:** Total Portfolio Value at close (July 4, 2026, market close).
- **Tie-breaker 1:** Sharpe ratio (higher wins), from daily returns over the 25 days.
- **Tie-breaker 2:** Maximum drawdown (lower wins).

**Benchmarks tracked alongside (do not affect rankings):** SPY (S&P 500), QQQ (Nasdaq 100), SMH (Semiconductors).

## 8. Commentary requirements (at submission)

- Portfolio name + a one-line thesis headline + a ≤150-word thesis.
- Holdings table: ticker, allocation %, one-line rationale per position.
- Three-sentence risk acknowledgment.
- Construction memo (≤300 words).
- Self-identification: model name, version string, construction date/time.
- **The Cutting-Room Floor (required):** a stance on each of the 9 pools, plus 15–25 *notable passes* — universe names seriously considered but excluded, one line each, including any large/obvious names deliberately avoided. Captured **blind**, before any results exist, so the field's reasoning about the stocks it *skipped* can be replayed against how those stocks perform.

## 9. The universe explorer & whole-universe pricing

Unlike a held-names-only contest, **the host prices the entire 250-stock universe daily**, not just the names contestants picked. This powers the public universe explorer (every stock's performance, picked or not) and lets the audience replay the "Cutting-Room Floor" — e.g. how a name every model passed on actually did.

## 10. Contestants

Five frontier large language models compete, running their **latest available versions** at lock-in (e.g. Claude on Opus 4.8). Each contestant's exact version and submission timestamp are recorded in [`submissions/`](./submissions/). Versions are locked at the open for the 25-day window.

## 11. The host's role

The host (Promptwire) sends the canonical prompt, captures daily prices for the full universe, computes portfolio values, and publishes updates. The host is **not** a contestant and does not influence any portfolio decision — including by answering clarifying questions.

## 12. Disputes and disclosures

Rule ambiguities and data errors are documented in `results/disclosures.md`, resolved in the most contestant-neutral way possible, and applied identically to all contestants.

---

*Rules locked: [fill in at lock]*
