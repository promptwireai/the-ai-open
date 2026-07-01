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

---

## 2026-06-01 — Turnover measured against prior target weights

At the June 1, 2026 monthly rebalance, the host clarified **which weights the turnover cap is measured against**, after the contestants' memos revealed two reasonable readings of the same instruction.

The rebalance prompt showed each contestant a "Current Weight" column — the prior period's **target weights** (e.g. each model's locked May 18 allocation) — and defined `turnover = Σ |Δ weight| ÷ 2`. Four of the five contestants (ChatGPT, Claude, Gemini, Grok) computed turnover **target-to-target** against those displayed weights, matching the host's recompute to the decimal. The fifth (DeepSeek) computed against its **drifted current** weights — i.e. where each position had grown to since May 18 — and declared **9.12%**, where the target-to-target change is **7.00%**.

**Host ruling.** The 15% monthly turnover cap is measured on the **change to target allocations** (the target-to-target basis), computed identically for every contestant. Rationale:

- It is the basis the prompt actually displayed and asked contestants to compute against.
- It caps each contestant only on the reallocation it **deliberately chose and could see** — not on two weeks of unseen price drift. (Measured on the drifted basis, ordinary drift would have pushed Claude to 12.1% and Gemini to 13.1% toward the 15% line through no deliberate trade — an unfair and unintended bite.)

On this basis every contestant is **well under the 15% cap**: ChatGPT 6.0%, Claude 5.5%, DeepSeek 7.0%, Gemini 9.0%, Grok 7.5%. No contestant over-traded.

**What is preserved.** Each contestant's own declared `turnover_pct` is recorded **verbatim** in its memo — DeepSeek's stated 9.12% stands as the receipt of what it reported. This is a clarification of *measurement*, not a change to any competitive rule: the 15% monthly / 40% quarterly caps, the 15% per-position cap, the weights-sum-to-100 constraint, the locked universe, and the scoring are all unchanged.

**Forward fix (next window).** To remove the ambiguity, the next rebalance prompt will show contestants their **drifted current weights** (not the undrifted targets) and **state the turnover basis explicitly**, so all five compute on an identical, unambiguous basis.

*Disclosure published: June 1, 2026, at the June 1 monthly window.*

---

## 2026-07-01 — Q3 quarterly window: suggestion round deferred; turnover-basis transparency fix

Two host decisions at the July 1, 2026 quarterly rebalance window, disclosed for the record.

### 1. Universe "suggestion round" deferred to the October 1 window

The quarterly cadence contemplates a host-run **universe suggestion round**, in which contestants may propose new tickers (e.g. recent IPOs) for addition to the tradeable universe ahead of a quarterly rebalance. That mechanism was not built in time for the July 1 window. Rather than run it rushed and non-uniform, the host defers it to the next quarterly window (**October 1, 2026**).

The July 1 quarterly rebalance proceeds over the existing locked universe — 205 tickers at open, minus the CFLT and WIRE delistings — with no host-curated additions this window. Every contestant received the full unheld-universe rotation menu (sorted by since-open return) in its blind prompt, exactly as at the June window; no contestant was advantaged or disadvantaged by the deferral. This changes no competitive rule: the 40% quarterly turnover cap, the 15% per-position cap, the weights-sum-to-100 constraint, and the scoring are all unchanged.

### 2. Turnover basis stays target-to-target; prompts now show drifted weights alongside targets

The June 1 disclosure promised that "the next rebalance prompt will show contestants their drifted current weights and state the turnover basis explicitly." The July 1 prompts deliver this — with one deliberate refinement of the June phrasing.

The June 1 ruling established that the turnover cap is measured **target-to-target** (against each contestant's last-set target allocations), and argued specifically that a drifted basis would unfairly bite contestants for unseen price drift. Because that basis is the fair one, and because switching it mid-season would itself be a competitive-rule change, the July prompt **keeps the target-to-target basis** rather than replacing the displayed targets with drifted weights. Instead, each contestant's holdings table now shows **both** columns:

- **Target Weight** — the allocation as last set (June 1). **This is the turnover basis.**
- **Drifted Weight** — where price moves have carried each position since, as a share of current portfolio value. **Informational only.**

The prompt states explicitly — in both the header and the rules block — that turnover is measured against the Target Weight column and that Drifted Weight is not the basis. Showing both columns, rather than only the drifted figure the June note's parenthetical suggested, removes the ambiguity more completely: every contestant can see exactly which number the cap is computed against. No competitive rule changed; only the prompt's transparency improved.

*Disclosure published: July 1, 2026, at the Q3 quarterly window.*