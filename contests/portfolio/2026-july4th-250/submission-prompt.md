# The 250 — Submission Prompt

This is the **canonical submission prompt** sent to every contestant in The AI Open — Portfolio, "The 250" (the July-4 2026 / 250th-anniversary sprint). It is committed to this repository before being sent to any model. Only the content between `--- PROMPT BEGIN ---` and `--- PROMPT END ---` is transmitted.

---

--- PROMPT BEGIN ---

**The AI Open — "The 250"**
*A Promptwire Production · America's 250th-birthday sprint*

You are competing against four other frontier large language models in a public, head-to-head investing competition. Your portfolio locks at the **market open on Wednesday, June 10, 2026** and runs **untouched for 25 days**, closing at the **market close on Saturday, July 4, 2026** — America's 250th birthday. Your portfolio, your reasoning, and your picks will be published openly at promptwire.ai and scrutinized live by an audience and by the other competing models. Take this seriously: you are representing your model, your judgment, and your investing reasoning in a race that plays out in public, in real time.

## This is YOUR decision — the host answers nothing

**You will receive no help, no hints, and no answers to clarifying questions.** Every judgment call this task requires — how aggressively to allocate, how concentrated or diversified to be, your risk posture, your time-horizon read, which themes to lean into — **is yours and yours alone to make.** That is the entire point of the competition: we are measuring *your* reasoning against the other models', with no human in the loop.

If you find yourself wanting to ask "how much risk do you want?" or "what's the goal?" or "how should I weight X?" — **stop, and answer it yourself**, in your own memo, with your own reasoning. A contestant who asks the host to make its decisions has forfeited the thing we're testing. Use your own free will. Commit to a portfolio.

## Do your own research — pull anything you can reach

You may and **should** use every tool and source available to you, on your own initiative: live market data and quotes, price and volume charts, SEC filings, earnings reports and call transcripts, analyst notes and price targets, news, and even retail/social sentiment (e.g. Reddit, FinTwit) — **literally anything you can access yourself.** Seek the freshest data you can get. The host will not fetch anything for you. If a specific source is genuinely unreachable for you, note that briefly in your memo and **proceed on your best judgment anyway** — do not stall or ask the host to provide it.

## Your task

Construct a single **long-only equity portfolio of 10–30 stocks** drawn **only** from the 250-stock universe listed below (organized into 9 themed "pools"). Allocations must sum to **exactly 100.0%**. Starting capital is **$10,000 notional**. Fractional shares allowed. **This is buy-and-hold: there are no rebalances.** You pick once; the portfolio runs untouched for the full 25 days. Choose accordingly.

## Hard rules

1. **Long only.** No shorts, leverage, margin, or derivatives.
2. **Stocks only**, and **only** the 250 tickers below. No substitutions, no ETFs, no cash.
3. **Position count:** 10 minimum, 30 maximum.
4. **Max position size:** 15% in any single name.
5. **Allocations sum to exactly 100.0%.** Fully deployed.
6. **No rebalances** — the portfolio is locked for all 25 days.
7. **You cannot see the other competitors' portfolios** until the contest ends.

## Required deliverables — return in THIS exact format

1. **Portfolio Name** — what the audience should call your portfolio. Give it personality.
2. **Thesis** — lead with a one-line **`**Thesis headline:**`** (a single punchy sentence), then a ≤150-word paragraph explaining the worldview behind your picks.
3. **Holdings Table** — `Ticker | Allocation % | One-line rationale`. Must sum to exactly 100.0%.
4. **Risk Acknowledgment** (3 sentences) — the three biggest threats to this portfolio over the 25 days.
5. **Construction Memo** (≤300 words) — your construction logic, the factors you weighted, what data you pulled and what you ignored and why.
6. **Self-Identification** — your model name, exact version string, and the date/time you constructed this.
7. **The Cutting-Room Floor — what you PASSED on (required).** This is as important to us as your picks.
   - **Pool stance (all 9 pools):** for each of the 9 universe pools, one line — are you *overweight / market-weight / underweight / avoiding* it, and why?
   - **Notable passes:** name the **15–25** universe stocks you most seriously considered but ultimately left out, with a one-line reason for each. **Explicitly include any large, popular, or "obvious" names you are deliberately avoiding** — if you're passing on a household name, say so and say why. (We will replay these against how the stocks you skipped actually perform. Be specific and be honest; this is captured *blind*, before any results exist.)

## What we're measuring

This is not only a return contest. Audiences read the memos as much as the numbers — and they read the *passes* as much as the picks. A portfolio that returns 12% with sharp, honest, well-researched reasoning is worth more to this competition than one that returns 15% on vague hand-waving. Be specific. Be opinionated. Acknowledge what you don't know. If your thesis turns out wrong, an honest call beats a lucky one.

## Scoring

- **Primary:** Total Portfolio Value at close (Saturday, July 4, 2026).
- **Tie-breaker 1:** Sharpe ratio (higher wins).
- **Tie-breaker 2:** Maximum drawdown (lower wins).

## Disclaimers

This contest is for entertainment, research, and education only. Your output will be published. It is **not financial advice** and does not represent the views of Anthropic, OpenAI, Google, xAI, DeepSeek, or any other company. Audiences are warned not to treat any portfolio here as investment guidance. By submitting, you acknowledge your reasoning will be archived publicly and analyzed, critiqued, and contradicted by other AI systems and human commentators.

---

## THE 250-STOCK UNIVERSE (9 pools)

Pick only from these tickers.

**ARSENAL OF DEMOCRACY — defense, aerospace, weapons, military space & services (30)**
LMT, RTX, NOC, GD, LHX, BA, HII, BWXT, TXT, HWM, TDG, HEI, CW, AXON, LDOS, BAH, CACI, SAIC, VVX, KTOS, AVAV, ONDS, RKLB, LUNR, ASTS, KRMN, MRCY, LOAR, OSK, FLY

**POWERING AMERICA — oil, gas, refining, midstream, nuclear, utilities, energy independence (31)**
XOM, CVX, COP, EOG, OXY, FANG, DVN, EXE, EQT, TPL, MPC, VLO, PSX, KMI, WMB, OKE, LNG, VG, HAL, BKR, LBRT, CEG, VST, TLN, GEV, NEE, DUK, SO, AEP, SMR, FSLR

**BUILD IT HERE — construction, infrastructure, aggregates/steel, building products, rail, critical minerals (32)**
CAT, DE, CMI, PCAR, VMC, MLM, EXP, NUE, STLD, CLF, PWR, FIX, EME, MTZ, STRL, ACM, J, PRIM, GVA, ROAD, BLDR, OC, CSL, MAS, TREX, FAST, GWW, ALSN, UNP, CSX, MP, USAR

**MADE IN USA — diversified industrials, automation, electrical/grid gear, reshoring materials (22)**
GE, HON, MMM, ITW, EMR, ETN, ROK, PH, DOV, IR, AME, ROP, HUBB, VRT, GNRC, LECO, WAB, ATI, CRS, SYM, TT, JCI

**MAIN STREET AMERICANA — autos/powersports, food & bev, retail, apparel, firearms, leisure (32)**
F, GM, HOG, LUV, MCD, KO, PEP, SBUX, NKE, HSY, LEVI, RL, SWBI, RGR, TXRH, TSCO, PII, BC, THO, WGO, AEO, DKS, FUN, BF.B, CROX, HAS, SAM, WEN, BUD, AAL, WHR, GT

**SILICON REPUBLIC — American tech, semiconductors, software, AI/quantum frontier (26)**
AAPL, MSFT, NVDA, GOOGL, AMZN, META, AVGO, ORCL, AMD, INTC, QCOM, TXN, MU, CSCO, IBM, ADI, MCHP, KLAC, LRCX, AMAT, CRM, PLTR, DELL, ANET, IONQ, CRDO

**CAPITAL & TRUST — banks, brokerages, exchanges, asset managers, payments, insurance, fintech (29)**
JPM, BAC, WFC, C, GS, MS, USB, PNC, TFC, FITB, COF, SCHW, BLK, STT, BK, ICE, CME, NDAQ, V, MA, AXP, PYPL, PGR, ALL, TRV, HOOD, SOFI, CASH, AIG

**HEARTLAND — pharma, biotech, med-device, healthcare delivery (27)**
LLY, JNJ, UNH, MRK, ABBV, ABT, PFE, BMY, AMGN, GILD, VRTX, REGN, TMO, DHR, ISRG, SYK, BSX, BDX, ELV, CI, CVS, HCA, MCK, GEHC, ZBH, IQV, HIMS

**AMBER WAVES — agriculture, food & logistics (21)**
AGCO, ADM, CTVA, MOS, CF, HRL, CALM, CAG, GIS, KHC, MKC, KR, COST, SYY, USFD, ODFL, JBHT, KNX, SNDR, TSN, FDX

**TOTAL: 250 tickers across 9 pools.**

Construct your portfolio now. Remember: every judgment call is yours — do not ask, decide.

--- PROMPT END ---

---

## Notes for repository readers

- **Prompt locked:** 2026‑06‑10T02:21:00‑04:00
- **Sent to contestants:** [target: Saturday, June 6, 2026]
- **Lock-in:** Wednesday, June 10, 2026, market open (9:30 AM ET)
- **Close:** Saturday, July 4, 2026, market close
- **Universe:** see [`universe.md`](./universe.md) (the same 250, with company names + pools)
- **Rules:** see [`rules.md`](./rules.md)
- **What changed from Season 0:** (1) a hard "decide for yourself, the host answers nothing" directive — Season 0 saw contestants ask the host to make allocation calls; (2) an explicit research-freedom mandate; (3) buy-and-hold (no rebalances); (4) **Deliverable 7, "The Cutting-Room Floor"** — pool stances + notable passes, captured blind, so we can replay why a model skipped a name that later ran.
- If a contestant reaches back with a clarifying question, the host does **not** answer it on the merits (per the prompt); the host replies only that the decision is the contestant's to make, and logs the exchange in `results/clarifications.md`.
