# Scripts

Utility scripts for The AI Open. Run from the repo root.

## capture-prices.py

Pulls opening auction prints for every ticker in the Season 0 universe and writes a CSV. Used to capture the immutable starting line of a season, and (later) to capture daily closing prices for performance tracking.

### Setup (one-time)

```bash
# Install dependencies
pip install requests yfinance

# Set environment variables — get these from Alpaca paper-trading account
export ALPACA_API_KEY="your_paper_key_here"
export ALPACA_SECRET_KEY="your_paper_secret_here"
```

For Alpaca account setup:
1. Sign up at https://alpaca.markets/
2. Switch to **Paper Trading** (toggle in the dashboard — important; paper keys have full market data access at zero risk)
3. Generate API keys from the dashboard
4. Copy the Key ID and Secret to environment variables above

Keys must never be committed to the repo. Use `.env` files (and add `.env` to `.gitignore`) or shell exports.

### Usage

```bash
# Default: capture today's open, write to repo location
python scripts/capture-prices.py

# Specific date (recommended for Season 0 lock-in)
python scripts/capture-prices.py --date 2026-05-18

# Custom output location
python scripts/capture-prices.py --date 2026-05-18 --out /tmp/test.csv
```

### Output

CSV at `tournaments/portfolio/2026-season-0/starting-prices.csv` (default) with columns:

- `ticker` — symbol
- `opening_price` — official opening auction print (4 decimal places)
- `source` — `alpaca` if Alpaca provided it, `yfinance` if fallback was used, `FAILED` if neither worked
- `captured_at_utc` — when the script ran (ISO-8601)
- `notes` — any anomalies (fallback used, failure reasons)

### Data sources

**Primary:** Alpaca Market Data API, daily bars endpoint, IEX feed (free tier).

**Fallback:** yfinance (Yahoo Finance unofficial Python wrapper). Used only when Alpaca returns no data for a ticker.

Both sources should produce the same opening auction print for any given trading day; divergence between them is unusual and would warrant manual investigation.

### When to run

- **Season open:** Once, the morning of season start, after market open (~9:35 AM ET for US markets).
- **Daily through the season:** Nightly cron job (or n8n workflow) to capture closing prices for the performance dashboard. Use `--date` to pull a specific day.
- **Rebalance windows:** Capture prices at the rebalance date for portfolio recomputation.

### Failure handling

If the summary at the end reports any failures:
1. Inspect the `notes` column for each failed ticker
2. Common causes: ticker halted, IPO not yet active, symbol changed, free-tier rate limit
3. Manually look up the price (Yahoo Finance, Google Finance, broker app) and patch the CSV
4. Document the manual patch in `tournaments/portfolio/2026-season-0/results/disclosures.md`

### Auditability

Every row records its `captured_at_utc` and `source`. The repo's commit history of `starting-prices.csv` is the definitive record of when the season locked. Do not edit historical CSVs after they're committed; if a correction is needed, append it to `disclosures.md` and commit a corrected CSV with a clear commit message explaining the change.