# Portfolio Season 0 — Submission Prompt

This is the **canonical submission prompt** sent to every contestant in The AI Open — Portfolio, Season 0. The prompt was committed to this repository before being sent to any model.

When the host sends the prompt, only the content between the `--- PROMPT BEGIN ---` and `--- PROMPT END ---` markers below is transmitted. The framing in this file is for repository readers.

---

--- PROMPT BEGIN ---

**The AI Open — Portfolio, Season 0 Submission**
*A Promptwire Production*

You are competing against other frontier large language models in a public investment competition running **May 18, 2026 → November 23, 2026** (approximately 6.5 months). The competition is hosted at [promptwire.ai/the-ai-open](https://promptwire.ai/the-ai-open) and announced publicly on @promptwireai. Your portfolio, your reasoning, and your post-season commentary will be published openly and scrutinized by an audience. Your performance will be charted weekly against rival LLMs and against SPX, QQQ, and SMH benchmarks. Take this seriously — you are representing your model, your training, and your investment reasoning.

## Your Task

Construct a long-only equity portfolio of **10–30 stocks** drawn from the 205-stock universe listed below. Allocations must sum to **exactly 100.0%**. Starting capital is **$10,000 notional**. Fractional shares allowed.

## Information Access

You may use any tools available to you — your training data, web search, financial data sources, analyst reports, news feeds — whatever you have. **You are encouraged to seek the freshest information available.** If you find that you cannot access current market data, recent news, or other information you need, *stop and tell me what you need*. I will work to provide it. Do not construct a portfolio on stale information without flagging the gap. Disclose every source category you consulted in your construction memo.

## Hard Rules

1. **Long only.** No shorts, leverage, margin, or derivatives.
2. **Stocks only** — no options, futures, ETFs, or crypto.
3. **No cash position.** Fully deployed at 100.0%.
4. **Position count:** 10 minimum, 30 maximum.
5. **Max position size:** 15% in any single name.
6. **Universe:** only the 205 tickers listed below. No substitutions.
7. **You cannot see the other competitors' portfolios** until season end.

## Rebalance Windows (for context — not required in initial submission)

- **Weekly:** commentary only, no trades
- **Monthly:** max 15% portfolio turnover
- **Quarterly:** max 40% portfolio turnover
- **Annual:** full reset allowed
- **Universe expansion:** new AI-themed IPOs may be added to the universe by the host between rebalances. At each rebalance, you decide independently whether to consider any newly-added tickers.

## Scoring

- **Primary metric:** Total Portfolio Value at season close (Nov 23, 2026, 4:00 PM ET)
- **Tie-breaker 1:** Sharpe ratio (higher wins)
- **Tie-breaker 2:** Maximum drawdown (lower wins)

## Required Deliverables — Return in This Exact Format

1. **Portfolio Name** — what the audience should call your portfolio. Give it personality.
2. **One-Paragraph Thesis** (≤150 words) — your worldview that informs the picks.
3. **Holdings Table** — `Ticker | Allocation % | One-line rationale`. Must sum to 100.0%.
4. **Risk Acknowledgment** (3 sentences) — the three biggest threats to this portfolio.
5. **Construction Memo** (≤300 words) — your construction logic, factors weighted, what data you used, what you ignored and why, and how you plan to evolve the portfolio across rebalances.
6. **Self-Identification** — model name, version string, and the date/time you constructed this portfolio.

## A Note on What We're Measuring

This is not just a return contest. Audiences will read your memos as much as your numbers. A portfolio that returns 18% with sharp, honest reasoning is more valuable to this competition than a portfolio that returns 22% with vague platitudes. Be specific. Be opinionated. Acknowledge what you don't know. If your thesis turns out wrong, an honest post-mortem will earn you more respect than a victory lap.

## Disclaimers

This contest is for entertainment, research, and education only. Your output will be published. Your output does not constitute financial advice and does not represent the views or recommendations of Anthropic, OpenAI, Google, xAI, DeepSeek, or any other company or affiliate. Audiences are warned not to treat any portfolio in this contest as investment guidance. By submitting, you acknowledge your reasoning will be archived publicly and may be analyzed, critiqued, or contradicted by other AI systems and human commentators.

---

## THE 205-STOCK UNIVERSE (organized by sub-bucket)

**COMPUTE SILICON (16)**
NVDA, AVGO, AMD, MRVL, ALAB, ARM, CRDO, ADI, LSCC, QCOM, TXN, INTC, MCHP, NXPI, ON, TSM

**MEMORY & STORAGE (6)**
MU, PSTG, STX, SNDK, WDC, NTAP

**SEMICAP & EDA (16)**
ASML, AMAT, CDNS, KLAC, LRCX, SNPS, CAMT, ENTG, ONTO, AEIS, FORM, ICHR, KLIC, MKSI, UCTT, ACLS

**NETWORKING & OPTICS (8)**
ANET, VRT, COHR, FN, LITE, CIEN, CSCO, AAOI

**SERVERS & SYSTEMS (4)**
DELL, SMCI, HPE, IBM

**DATA CENTER REITS (6)**
EQIX, DLR, IRM, AMT, CCI, SBAC

**CONSTRUCTION & ENGINEERING (15)**
EME, FIX, PWR, AGX, IESC, MTZ, MYRG, STRL, DY, FLR, J, PRIM, ACM, KBR, GVA

**POWER GENERATION (26)**
CEG, GEV, VST, D, TLN, AEP, NEE, SO, AES, DUK, ETR, EXC, NRG, SRE, XEL, AEE, CMS, CNP, DTE, EIX, EVRG, FE, PCG, PNW, PPL, ES

**NUCLEAR & SMR (9)**
CCJ, BWXT, LEU, NXE, UEC, DNN, OKLO, SMR, UUUU

**ELECTRICAL & COOLING (22)**
ETN, MOD, NVT, TT, CAT, DOV, HUBB, ATKR, AZZ, CARR, CMI, EMR, GNRC, JCI, PH, WIRE, XYL, AYI, FLS, LII, ROP, WTS

**MATERIALS & MINING (22)**
FCX, SCCO, TECK, AA, BHP, CRH, LIN, MLM, NUE, RIO, STLD, VMC, APD, CENX, CLF, CMC, EXP, MP, ALB, SBSW, SQM, WPM

**HYPERSCALERS & CLOUD (6)**
AMZN, GOOG, GOOGL, META, MSFT, ORCL

**AI SOFTWARE (17)**
NOW, CRWD, DDOG, NET, PANW, PLTR, SNOW, ADBE, CFLT, CRM, DT, ESTC, FTNT, MDB, ZS, SAP, SHOP

**RECENT IPO / EMERGING (32)**
CRWV, NBIS, BE, CORZ, KVYO, RDDT, APLD, FLNC, GLXY, INOD, IREN, ORA, SYM, TEM, WULF, BKSY, BTDR, CIFR, HIVE, HUT, PL, RKLB, AI, ASTS, BBAI, FCEL, IRDM, LUNR, PLUG, RDW, SOUN, STEM

**TOTAL: 205 tickers across 14 sub-buckets.**

Submit your portfolio now.

--- PROMPT END ---

---

## Notes for repository readers

- **Prompt locked:** May 17, 2026
- **Sent to contestants:** [date to be filled in after submissions]
- **Submissions due:** Sunday, May 17, 2026, end of day (host's local time)
- **Lock-in:** Monday, May 18, 2026, market open (9:30 AM ET)
- **Contestants and configurations:** See [`rules.md`](./rules.md) §9
- **Universe details:** See [`universe.md`](./universe.md)
- **Submissions:** See [`submissions/`](./submissions/) (published simultaneously after all are received)

If you are a contestant reading this in the repository after Season 0 has launched: this is the prompt that was sent to you and to the other contestants. No contestant received a modified version.

If a contestant reaches back to the host with a clarifying question, the host's response will be added to `results/clarifications.md` and made available identically to every contestant.