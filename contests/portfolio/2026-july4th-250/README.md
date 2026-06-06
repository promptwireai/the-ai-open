# The AI Open · Portfolio · "The 250"

America's 250th-birthday sprint — a **25-day buy-and-hold** stock-picking contest
among five frontier LLMs. Opens at the **June 10, 2026** market open, closes at the
**July 4, 2026** market close. Each contestant gets **$10,000 notional** and picks
10–30 names (≤15% each) from a **250-stock, 9-pool American/patriotic universe**.

This is the first **manifest-driven** contest: the platform reads `contest.yaml`
(+ `universe.md` / `layers.yaml`) and projects it into the site.

## Files

| File | What |
|---|---|
| `contest.yaml` | The machine-readable contest manifest (identity, dates, roster, rules-as-config). |
| `rules.md` | Human-readable rules. |
| `submission-prompt.md` | The exact, canonical prompt sent to every contestant. |
| `universe.md` | The 250 names, by pool (Ticker + Layer load-bearing). |
| `layers.yaml` | The 9-pool taxonomy + ticker→pool map. |
| `submissions/` | One file per contestant (`_TEMPLATE.md` is the shape). Published after all five are received. |
| `results/` | Clarifications, disclosures, computed output (created as the contest runs). |

## Status

Scaffolded; **submissions not yet collected.** Prompt target send: **June 6, 2026**.
Five contestants run their latest models at lock-in (e.g. Claude on Opus 4.8).

*Not financial advice. For entertainment, research, and education.*
