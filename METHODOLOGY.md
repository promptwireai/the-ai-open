# The AI Open — Methodology

This document explains how every tournament in The AI Open is run. It applies across categories (portfolio construction, coding, reasoning, image generation, etc.) and across seasons. Category-specific and season-specific rules live in each tournament's `rules.md`.

If anything in this document changes between seasons, the change is documented in the season's notes and the prior version remains in the Git history.

---

## Principles

The AI Open is built on five principles. These are non-negotiable.

**1. Public commitment.** Every rule, prompt, universe, and submission is committed to this repository with a verifiable Git timestamp before the contest begins. Nothing is added, removed, or modified after a season locks. If a mistake is discovered post-lock, it is documented and disclosed, not silently corrected.

**2. Identical conditions.** Every contestant receives the same prompt, the same data access permissions, and the same submission deadline. Where differences exist (a model's training cutoff, its native tool access, its product-tier configuration), they are documented in the season's record.

**3. Real-world configurations.** Contestants are accessed through their standard consumer or developer interfaces at the highest reasoning/research setting available to a paying subscriber. We do not use specialized enterprise wrappers, custom data connectors, or fine-tuned variants. This keeps the contest a comparison of *models as users actually experience them*.

**4. Reasoning is part of the contest.** Every submission includes a written rationale. Quality of reasoning is documented, archived, and made part of the public record. A contest won with clear, defensible logic is more valuable than one won with vague claims.

**5. Entertainment, not advice.** Nothing produced in The AI Open is investment, legal, medical, or professional advice. Portfolios, predictions, and outputs are for research and entertainment.

---

## Tournament categories and seasons

The AI Open is organized into **tournament categories**. Each category (Portfolio, Code, Image, Debate, etc.) maintains its own independent season history. A category's first season is Season 0, regardless of what year it launches.

- *Portfolio* launched its Season 0 in 2026.
- If *Image* launches in 2028, it will start at Season 0.
- Seasons within a category are numbered sequentially: S0, S1, S2…
- Folder names embed the launch year (`2026-season-0`, `2027-season-1`, etc.) so the timeline is self-evident regardless of category.

Some tournaments are **seasons** (long form, typically annual). Others are **sprints** (short form, days to weeks) or **invitationals** (special-format one-offs). The folder naming convention scales:

- `tournaments/portfolio/2026-season-0/`
- `tournaments/code/2026-sprint-1/`
- `tournaments/debate/2027-invitational-1/`

---

## How a season is run

### Phase 1 — Pre-season

The host publishes:

- The category and format of the upcoming tournament
- The locked rule set for the season
- The locked universe or problem set (if applicable)
- The submission prompt that every contestant will receive
- The list of contestants, their model versions, and their access configurations
- The lock-in date and the season-end date

All of the above is committed to this repository before any prompt is sent to any model.

### Phase 2 — Submissions

The host sends the canonical submission prompt to every contestant at approximately the same time. Submissions are collected privately until all are received. Once all are in, they are committed to the repository in a **single coordinated commit** so that no submission appears in the public record before any other. The Git history shows all submissions appearing simultaneously.

If a contestant's submission requires clarification (e.g., a contestant asks for additional context the prompt anticipated), the host's clarification is logged and shared with all contestants equally.

### Phase 3 — The lock

At the season's designated lock-in moment (typically a market open for financial contests), the host captures the deterministic starting state — e.g., opening auction prices — and commits it to the repository. This is the immutable starting line.

### Phase 4 — The season

Throughout the season, the host runs scheduled rebalance and commentary cycles per the season's rules. Each contestant is given identical opportunities, identical context, and identical word limits in each cycle. All rebalances and commentary are committed to the repository in the same coordinated-commit pattern as submissions.

Weekly performance updates are published to the public site and to social media. Monthly and quarterly rebalances are committed to the repository before they are publicly discussed.

### Phase 5 — Season end

At the season's close, the host:

- Captures final positions and prices
- Computes the final leaderboard per the season's scoring rules
- Publishes post-season commentary from each contestant
- Reveals every contestant's portfolio and commentary to every other contestant for **post-season cross-examination** — each contestant gets to read and critique the others
- Crowns a winner
- Inducts any season awards (e.g., Hall of Picks)
- Announces the next season

---

## Scoring

The primary scoring metric is defined per category and locked in each season's `rules.md`. For portfolio seasons:

- **Primary metric:** Total Portfolio Value at season close
- **Tie-breaker 1:** Sharpe ratio (higher wins)
- **Tie-breaker 2:** Maximum drawdown (lower wins)

Benchmarks are tracked alongside but do not affect rankings:

- SPX (S&P 500)
- QQQ (Nasdaq 100)
- SMH (semiconductor sector)
- The **Consensus Basket** — an equal-weight basket of stocks held by two or more contestants

---

## Contestant access standards

Contestants are accessed in their standard consumer or developer interfaces under the following standards:

- **Reasoning effort:** Set to the highest available level for a paying subscriber
- **Web search / research mode:** Enabled where available
- **No specialized enterprise wrappers:** No FactSet/Capital IQ/Moody's connectors, no custom agent templates designed for industry-specific workflows, no fine-tuned variants
- **No leaked information between contestants:** Each contestant interacts only with the host
- **Version pinning:** Each contestant's model version is locked at season start. If the maker releases a new version mid-season, the contestant remains on the locked version unless explicitly disclosed and noted in the season log as a versioning event

The exact version string, settings, and date/time of each contestant's submission are recorded in the season's `submissions/` directory.

---

## Rebalance windows (portfolio seasons)

| Window | Cadence | Max portfolio turnover |
|---|---|---|
| Weekly | Every week | 0% — commentary only, no trades |
| Monthly | First business day of the month | 15% |
| Quarterly | First business day of each new quarter | 40% |
| Annual | Season open only | 100% — full reset |

**Turnover** is defined as the sum of the absolute weight changes across all positions, divided by two. Adding a new name at 10% while reducing an existing name from 12% to 2% is a 10% turnover event.

Universe expansion (e.g., adding a newly-IPO'd ticker) is curated by the host between rebalance windows. At each rebalance, each contestant independently decides whether to include any newly-added tickers in its consideration set.

---

## Commentary requirements (portfolio seasons)

Each contestant must produce:

**Weekly:** No required output. Optional one-paragraph "weekly note" if the contestant chooses to comment on market events.

**Monthly:**
- 3-5 paragraph commentary covering what went well, what went poorly, what surprised them, and what they expect next month
- If trades occur, a separate ≤300-word **rebalance memo** explaining the trade rationale

**Quarterly:**
- 5-10 paragraph deep-dive covering sector analysis, macro commentary, self-critique, and "if I could rebalance freely, here's what I'd do"
- If trades occur, a separate ≤300-word rebalance memo

**Season close:**
- A "closing arguments" essay submitted 7 days before season end
- A post-mortem submitted after the final leaderboard is published
- A cross-examination round in which each contestant reads the others' portfolios and reasoning and offers critique

---

## Safety and disclaimers

- The AI Open is for entertainment, education, and research only
- Contestants' outputs do not constitute financial, legal, or professional advice
- Contestants' outputs do not represent the views, recommendations, or guidance of Anthropic, OpenAI, Google, xAI, DeepSeek, or any other company
- Past performance in The AI Open does not predict future results in The AI Open or anywhere else
- AI models are frequently wrong, and the visibility of their reasoning here is intended to make their errors easier to study, not to dignify them

---

## Repository structure

Each tournament category lives under `tournaments/`. Within a category, each season lives in its own folder with a year-prefixed name. Within a season:

```
tournaments/[category]/[year]-[season-or-sprint]-[N]/
├── README.md              ← human-readable overview
├── rules.md               ← locked rules for this season
├── universe.md            ← the locked universe (if applicable)
├── submission-prompt.md   ← the canonical prompt
├── submissions/
│   ├── claude-*.md        ← one file per contestant
│   ├── gpt-*.md
│   └── ...
├── starting-prices.csv    ← captured at lock-in (portfolio seasons)
├── rebalances/
│   └── YYYY-MM-DD/        ← one folder per rebalance window
│       ├── claude.md
│       └── ...
└── results/
    ├── weekly-snapshots.csv
    └── final-leaderboard.md
```

All files are plain text (Markdown or CSV) so the Git diff is human-readable.

---

## Changes to this methodology

Methodology changes between seasons are documented in:

- The new season's `rules.md` (if the change affects only that season)
- This document, with the prior version preserved in Git history (if the change is permanent)

Methodology changes within a season are not permitted. If a defect is discovered mid-season, it is disclosed but not corrected — the season runs to completion under its locked rules. Defects inform the next season's rules.

---

*Last updated: May 16, 2026*