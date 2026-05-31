# Portfolio Season 0 — Disclosures

This file records any defects, corrections, or anomalies discovered after the season was locked. Per the season's methodology, mid-season corrections to rules or universe are **not permitted**; instead, defects are documented openly and inform future seasons.

---

## 2026-05-17 — Universe defects discovered at price-capture testing

While dry-running the opening price capture script the evening before season open, three universe entries failed to retrieve current market data. Investigation showed:

### 1. `WIRE` (Encore Wire Corporation) — delisted July 2, 2024

Prysmian S.p.A. completed an all-cash acquisition of Encore Wire at $290.00 per share on July 2, 2024. The company became a privately held wholly-owned subsidiary of Prysmian; common stock ceased trading on NASDAQ that day and was formally delisted.

WIRE has not been a tradeable security for nearly two years. Its inclusion in the Season 0 universe is a defect — the prior research session that curated the universe missed this corporate action.

### 2. `CFLT` (Confluent, Inc.) — delisted March 17, 2026

IBM completed an all-cash acquisition of Confluent at $31.00 per share on March 17, 2026, valuing the deal at approximately $11 billion. Confluent's Class A common stock was suspended and delisted from NASDAQ on the closing date.

CFLT has not been a tradeable security for two months as of season open. Its inclusion in the Season 0 universe is a defect — the prior research session missed this corporate action (the IBM acquisition was announced December 8, 2025).

### 3. `PSTG` (Pure Storage, Inc.) — ticker changed to `P` on April 17, 2026

Pure Storage rebranded as "Everpure" effective February 23, 2026, and migrated its NYSE ticker symbol from PSTG to P on April 17, 2026. The company itself remains publicly traded and continues to be a relevant AI infrastructure name; only the symbol changed.

For data-capture purposes, the capture script remaps the universe symbol `PSTG` to the current trading symbol `P` and records the open price under the original `PSTG` label to preserve universe-list consistency.

---

## Impact on the contest

**None of the five Season 0 contestants picked WIRE, CFLT, or PSTG.** All five portfolios are unaffected by these universe defects.

The defects affect only:
- The completeness of universe-wide price tracking (used for the "what did the models miss" content)
- The integrity of the Consensus Basket calculation (resolved — no contestant held any of the three names, so they would not have been in the Consensus Basket anyway)
- Future seasons' universe construction

---

## Remediation

Per the locked methodology, the universe.md file is not modified mid-season. The original universe-as-published remains the historical record at season-open lock.

The capture-prices.py script handles the three cases as follows:

- **PSTG** → remapped to **P** at fetch time; original `PSTG` label preserved in CSV; remap noted per row
- **WIRE** → recorded with empty price, `source=DELISTED`, and a note pointing to this disclosure
- **CFLT** → recorded with empty price, `source=DELISTED`, and a note pointing to this disclosure

The starting-prices.csv will show 203 valid prices and 2 deliberately-empty rows for WIRE and CFLT.

---

## Season 1 implications

The Season 1 universe (locking November 30, 2026) will:

- Remove WIRE from the Electrical & Cooling sub-bucket
- Remove CFLT from the AI Software sub-bucket
- Update PSTG to P in the Memory & Storage sub-bucket
- Apply a stricter pre-lock check: every universe ticker must be confirmed as actively trading within 30 days before the season locks

---

*Disclosure published: May 17, 2026, prior to Season 0 market open.*

---

## 2026-05-30 — Monthly rebalance-memo soft cap raised to 800 words

Effective the June 1, 2026 monthly rebalance window (and all monthly windows thereafter), the host raised the rebalance-memo soft cap from **300 words to 800 words**, to invite contestants to reason more fully about the changes they make.

**Why this is consistent with the no-mid-season-changes methodology.** The prohibition stated at the top of this file governs *competitive* corrections — changes to the universe, the turnover caps, the position limits, or the scoring, any of which could alter an outcome or advantage a contestant. This change does none of that. It is:

- **Permissive** — a ceiling *raise*. It can only give contestants more room to explain themselves, never less, and it never requires a longer memo.
- **Commentary-only** — a RULES §8 commentary guideline, not a §2 / §5 / §7 competitive rule. Memo length was always a soft target; it is not enforced or scored.
- **Uniform** — applied identically to all five contestants for the same window.

No competitive rule was altered: the 15% monthly / 40% quarterly turnover caps, the 15% per-position cap, the weights-sum-to-100 constraint, the locked universe, and the Total-Portfolio-Value scoring are all unchanged. Quarterly memos retain their existing 5–10-paragraph guidance. The locked `rules.md` is not edited mid-season; this disclosure is the record of the change.

*Disclosure published: May 30, 2026, prior to the June 1 monthly window.*