#!/usr/bin/env python3
"""
capture-prices.py — Capture opening auction prints for The AI Open universe.

Usage:
    python scripts/capture-prices.py [--date YYYY-MM-DD] [--out PATH]

Environment variables required:
    ALPACA_API_KEY      — Paper-trading API key from Alpaca
    ALPACA_SECRET_KEY   — Paper-trading secret key from Alpaca

Defaults:
    --date  Today (UTC); for Season 0 lock-in, pass --date 2026-05-18
    --out   tournaments/portfolio/2026-season-0/starting-prices.csv

Strategy:
    Primary source:   Alpaca Market Data API (daily bars endpoint)
    Fallback source:  yfinance (Yahoo Finance unofficial API)

    For each ticker, attempt Alpaca first. If Alpaca returns nothing
    (which can happen for newer IPOs or thinly-traded names), fall
    back to yfinance. Always record which source produced the price.

Output:
    CSV with columns: ticker, opening_price, source, captured_at_utc, notes
"""

import argparse
import csv
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ------------------------------------------------------------------
# Universe — keep in sync with tournaments/portfolio/2026-season-0/universe.md
# ------------------------------------------------------------------
UNIVERSE = [
    # Compute Silicon (16)
    "NVDA", "AVGO", "AMD", "MRVL", "ALAB", "ARM", "CRDO", "ADI", "LSCC",
    "QCOM", "TXN", "INTC", "MCHP", "NXPI", "ON", "TSM",
    # Memory & Storage (6)
    "MU", "PSTG", "STX", "SNDK", "WDC", "NTAP",
    # Semicap & EDA (16)
    "ASML", "AMAT", "CDNS", "KLAC", "LRCX", "SNPS", "CAMT", "ENTG", "ONTO",
    "AEIS", "FORM", "ICHR", "KLIC", "MKSI", "UCTT", "ACLS",
    # Networking & Optics (8)
    "ANET", "VRT", "COHR", "FN", "LITE", "CIEN", "CSCO", "AAOI",
    # Servers & Systems (4)
    "DELL", "SMCI", "HPE", "IBM",
    # Data Center REITs (6)
    "EQIX", "DLR", "IRM", "AMT", "CCI", "SBAC",
    # Construction & Engineering (15)
    "EME", "FIX", "PWR", "AGX", "IESC", "MTZ", "MYRG", "STRL", "DY",
    "FLR", "J", "PRIM", "ACM", "KBR", "GVA",
    # Power Generation (26)
    "CEG", "GEV", "VST", "D", "TLN", "AEP", "NEE", "SO", "AES", "DUK",
    "ETR", "EXC", "NRG", "SRE", "XEL", "AEE", "CMS", "CNP", "DTE", "EIX",
    "EVRG", "FE", "PCG", "PNW", "PPL", "ES",
    # Nuclear & SMR (9)
    "CCJ", "BWXT", "LEU", "NXE", "UEC", "DNN", "OKLO", "SMR", "UUUU",
    # Electrical & Cooling (22)
    "ETN", "MOD", "NVT", "TT", "CAT", "DOV", "HUBB", "ATKR", "AZZ", "CARR",
    "CMI", "EMR", "GNRC", "JCI", "PH", "WIRE", "XYL", "AYI", "FLS", "LII",
    "ROP", "WTS",
    # Materials & Mining (22)
    "FCX", "SCCO", "TECK", "AA", "BHP", "CRH", "LIN", "MLM", "NUE", "RIO",
    "STLD", "VMC", "APD", "CENX", "CLF", "CMC", "EXP", "MP", "ALB", "SBSW",
    "SQM", "WPM",
    # Hyperscalers & Cloud (6)
    "AMZN", "GOOG", "GOOGL", "META", "MSFT", "ORCL",
    # AI Software (17)
    "NOW", "CRWD", "DDOG", "NET", "PANW", "PLTR", "SNOW", "ADBE", "CFLT",
    "CRM", "DT", "ESTC", "FTNT", "MDB", "ZS", "SAP", "SHOP",
    # Recent IPO / Emerging (32)
    "CRWV", "NBIS", "BE", "CORZ", "KVYO", "RDDT", "APLD", "FLNC", "GLXY",
    "INOD", "IREN", "ORA", "SYM", "TEM", "WULF", "BKSY", "BTDR", "CIFR",
    "HIVE", "HUT", "PL", "RKLB", "AI", "ASTS", "BBAI", "FCEL", "IRDM",
    "LUNR", "PLUG", "RDW", "SOUN", "STEM",
]

assert len(set(UNIVERSE)) == 205, f"Universe size mismatch: {len(set(UNIVERSE))}"


# ------------------------------------------------------------------
# Ticker remapping
# ------------------------------------------------------------------
# Some tickers in the locked universe have undergone corporate actions
# since the universe was defined. To preserve the contest's universe
# integrity (the universe.md file is tagged-locked), we remap defunct
# symbols at fetch time to their currently-tradeable equivalent. The
# remapping is documented in results/disclosures.md.
TICKER_REMAPPING = {
    "PSTG": "P",  # Pure Storage rebranded to Everpure; ticker changed 2026-04-17
}

# Tickers known to be delisted with no successor — will fail by design.
# Capturing these failures in the CSV is more honest than silently
# skipping them. Both delisted prior to Season 0 open.
KNOWN_DELISTED = {
    "WIRE": "delisted 2024-07-02 — acquired by Prysmian at $290/share",
    "CFLT": "delisted 2026-03-17 — acquired by IBM at $31/share",
}


# ------------------------------------------------------------------
# Alpaca client (primary source)
# ------------------------------------------------------------------
def fetch_from_alpaca(ticker: str, date_str: str) -> tuple[float | None, str]:
    """
    Returns (price, note). price is None on failure; note explains why.
    Uses Alpaca's daily bars endpoint and returns the day's open price.
    """
    try:
        import requests
    except ImportError:
        return None, "requests library not installed"

    api_key = os.environ.get("ALPACA_API_KEY")
    secret_key = os.environ.get("ALPACA_SECRET_KEY")
    if not api_key or not secret_key:
        return None, "ALPACA_API_KEY/SECRET_KEY not in environment"

    url = f"https://data.alpaca.markets/v2/stocks/{ticker}/bars"
    params = {
        "start": date_str,
        "end": date_str,
        "timeframe": "1Day",
        "feed": "iex",  # IEX feed is available on free tier
        "adjustment": "raw",
    }
    headers = {
        "APCA-API-KEY-ID": api_key,
        "APCA-API-SECRET-KEY": secret_key,
    }

    try:
        resp = requests.get(url, params=params, headers=headers, timeout=10)
        if resp.status_code != 200:
            return None, f"alpaca http {resp.status_code}"
        bars = resp.json().get("bars") or []
        if not bars:
            return None, "alpaca returned no bars"
        return float(bars[0]["o"]), ""
    except Exception as e:
        return None, f"alpaca exception: {type(e).__name__}"


# ------------------------------------------------------------------
# yfinance client (fallback source)
# ------------------------------------------------------------------
def fetch_from_yfinance(ticker: str, date_str: str) -> tuple[float | None, str]:
    """
    Returns (price, note). price is None on failure.
    Uses yfinance to pull the day's bar and returns the Open value.
    """
    try:
        import yfinance as yf
    except ImportError:
        return None, "yfinance library not installed"

    try:
        # yfinance wants a date range; end is exclusive so add 1 day
        from datetime import datetime as dt, timedelta
        start = dt.strptime(date_str, "%Y-%m-%d")
        end = start + timedelta(days=1)
        data = yf.download(
            ticker,
            start=start.strftime("%Y-%m-%d"),
            end=end.strftime("%Y-%m-%d"),
            progress=False,
            auto_adjust=False,
        )
        if data.empty:
            return None, "yfinance returned no data"
        open_price = float(data["Open"].iloc[0])
        return open_price, ""
    except Exception as e:
        return None, f"yfinance exception: {type(e).__name__}"


# ------------------------------------------------------------------
# Main loop
# ------------------------------------------------------------------
def capture_prices(date_str: str, out_path: Path) -> None:
    print(f"\nCapturing opening prints for {len(UNIVERSE)} tickers, date={date_str}")
    print(f"Output: {out_path}\n")

    captured_at_utc = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rows = []
    successes = 0
    failures = []

    for i, ticker in enumerate(UNIVERSE, 1):
        # Short-circuit known-delisted tickers: record clearly and move on
        if ticker in KNOWN_DELISTED:
            rows.append({
                "ticker": ticker,
                "opening_price": "",
                "source": "DELISTED",
                "captured_at_utc": captured_at_utc,
                "notes": KNOWN_DELISTED[ticker],
            })
            failures.append(ticker)
            if i % 25 == 0:
                print(f"  [{i:3d}/{len(UNIVERSE)}] last: {ticker} (delisted)")
            time.sleep(0.05)
            continue

        # Apply ticker remapping for renamed symbols
        fetch_symbol = TICKER_REMAPPING.get(ticker, ticker)
        remap_note = ""
        if fetch_symbol != ticker:
            remap_note = f"remapped {ticker}->{fetch_symbol} per ticker change"

        # Try Alpaca first
        price, note = fetch_from_alpaca(fetch_symbol, date_str)
        source = "alpaca"

        # Fall back to yfinance if Alpaca failed
        if price is None:
            fallback_price, fallback_note = fetch_from_yfinance(fetch_symbol, date_str)
            if fallback_price is not None:
                price = fallback_price
                source = "yfinance"
                note = f"alpaca: {note} | fallback used"
            else:
                source = "FAILED"
                note = f"alpaca: {note} | yfinance: {fallback_note}"

        # Combine any remap note with source notes
        if remap_note:
            note = f"{remap_note} | {note}" if note else remap_note

        rows.append({
            "ticker": ticker,  # Always record the original ticker from universe.md
            "opening_price": f"{price:.4f}" if price is not None else "",
            "source": source,
            "captured_at_utc": captured_at_utc,
            "notes": note,
        })

        if price is not None:
            successes += 1
            status = "✓"
        else:
            failures.append(ticker)
            status = "✗"

        # Progress every 25
        if i % 25 == 0:
            print(f"  [{i:3d}/{len(UNIVERSE)}] last: {ticker} {status}")

        # Light rate limiting to be polite to free-tier APIs
        time.sleep(0.05)

    # Write CSV with utf-8-sig encoding: writes a BOM so Excel opens cleanly,
    # and safely encodes any Unicode characters in the notes column.
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(
            f, fieldnames=["ticker", "opening_price", "source", "captured_at_utc", "notes"]
        )
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"Captured: {successes}/{len(UNIVERSE)}")
    print(f"Failed:   {len(failures)}/{len(UNIVERSE)}")
    if failures:
        print(f"\nFailures (manual review needed):")
        for t in failures:
            print(f"  - {t}")
    print(f"\nOutput written to: {out_path}")
    print(f"{'=' * 60}\n")


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--date",
        default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        help="Trading date (YYYY-MM-DD). Defaults to today (UTC).",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=Path("tournaments/portfolio/2026-season-0/starting-prices.csv"),
        help="Output CSV path. Defaults to repo location.",
    )
    args = parser.parse_args()

    capture_prices(args.date, args.out)