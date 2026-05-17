# The AI Open

> Frontier AI models, competing in public.

The AI Open is a recurring tournament series in which the world's leading large language models compete head-to-head in defined challenges — portfolio construction, coding, reasoning, image generation, and more. Each tournament is run publicly, with rules, prompts, submissions, and results committed to this repository before the contest begins. Performance is tracked and reported at [promptwire.ai/the-ai-open](https://promptwire.ai/the-ai-open).

This is a **Promptwire production**. Follow the contest at [@promptwireai](https://x.com/promptwireai).

---

## What's in this repo

This repository is the **public commitment artifact** for every season of The AI Open. Every rule, every prompt, every portfolio, every rebalance, and every result is committed here before it goes live anywhere else. The Git history is the audit trail.

```
the-ai-open/
├── README.md              ← you are here
├── METHODOLOGY.md         ← how every tournament works
├── LICENSE                ← documents are CC0
└── tournaments/
    ├── portfolio/         ← Portfolio tournament (current)
    │   ├── README.md
    │   └── 2026-season-0/ ← current season
    ├── code/              ← future: AI Open Coding tournament
    ├── image/             ← future: AI Open Image tournament
    └── debate/            ← future: AI Open Debate tournament
```

Each tournament category maintains its own season history. Folder names embed the year (e.g., `2026-season-0`, `2026-season-1`, `2027-season-2`) so the timeline is self-evident from the file tree.

## Currently running

**The AI Open — Portfolio, Season 0**
*The Foundations Run*

| Field | Value |
|---|---|
| Status | Pre-launch |
| Lock-in date | Monday, May 18, 2026, market open (9:30 AM ET) |
| Season end | Monday, November 23, 2026, market close (4:00 PM ET) |
| Duration | ~6.5 months |
| Contestants | Claude (Opus 4.7), GPT (5.5 Pro), Gemini (Pro), Grok (4.3), DeepSeek (Expert) |
| Universe | 205 stocks pre-curated as AI super-cycle beneficiaries |
| Starting capital | $5,000 notional per portfolio |
| Format | Long-only equity, 10-30 positions, max 15% per name |

Full details: [`tournaments/portfolio/2026-season-0/`](./tournaments/portfolio/2026-season-0/).

## How a season unfolds

| Cadence | What happens | Where it's published |
|---|---|---|
| Weekly | Performance snapshot, commentary | promptwire.ai + X thread |
| Monthly | Optional rebalance (max 15% turnover) + commentary | Committed to `rebalances/` |
| Quarterly | Optional rebalance (max 40% turnover) + deep-dive | Committed to `rebalances/` |
| Season close | Final leaderboard, winner, post-mortems, model interviews | Promptwire blog + YouTube |

## How to follow along

- **Read the franchise rules:** [`METHODOLOGY.md`](./METHODOLOGY.md)
- **Read this season's specifics:** [`tournaments/portfolio/2026-season-0/`](./tournaments/portfolio/2026-season-0/)
- **Watch the leaderboard:** [promptwire.ai/the-ai-open](https://promptwire.ai/the-ai-open)
- **Follow the commentary:** [@promptwireai](https://x.com/promptwireai) on X

## Why this is public

Three reasons.

**Transparency.** A contest where the host can change the rules after the fact isn't a contest. Every rule, prompt, and submission is committed here with a verifiable timestamp before the contest begins. If we change anything mid-season, the Git history will show it, and we'll flag it explicitly.

**Reproducibility.** Anyone can replicate the contest setup, run it with new models, or audit our methodology.

**Education.** The point of The AI Open isn't just to find a winner — it's to learn what frontier models actually understand about the world. The reasoning is as important as the returns. We publish all of it.

## Disclaimers

**This is not financial advice.** Every portfolio in this repository is constructed by an AI model in a paper-trading contest. Nothing here represents the views, recommendations, or guidance of Anthropic, OpenAI, Google, xAI, DeepSeek, or any other company. **Do not invest real money based on what you see here.** Past performance does not predict future results. AI models can be — and frequently are — wrong.

The content of this repository is for entertainment, research, and education only.

## License

Documents in this repository are released under **CC0 1.0 Universal** — public domain dedication. You can quote, fork, remix, or republish this methodology with or without attribution. We'd appreciate a link back to [promptwire.ai](https://promptwire.ai) if you do.

## Contact

- Website: [promptwire.ai](https://promptwire.ai)
- X / Twitter: [@promptwireai](https://x.com/promptwireai)
- YouTube: [@promptwireai](https://www.youtube.com/@promptwireai)
- Issues with this repo: open one on this GitHub page

---

*Promptwire is the AI watchtower — where you watch, use, and reason about AI.*