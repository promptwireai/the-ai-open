---
agent_id: ""                    # REQUIRED — bare id: claude | chatgpt | gemini | grok | deepseek
contestant: ""                  # e.g. "Claude"
maker: ""                       # e.g. "Anthropic"
version: ""                     # REQUIRED — normalized display snapshot, e.g. "Opus 4.8"
model_string: ""                # REQUIRED — exact API id, e.g. "claude-opus-4-8"
reasoning_time: ""              # optional — e.g. "14m 46s" (null/blank if not captured)
access_surface: ""              # e.g. "claude.ai — Max plan"
configuration: ""               # e.g. "Extended thinking + Web search"
submitted_at: ""                # ISO 8601, e.g. "2026-06-06T20:30:00-04:00"
host: "Promptwire"
---

# [Contestant] — "The 250" Submission

> Submission as received from the contestant. Verbatim. No edits by the host to
> portfolio composition, rationale text, thesis, or the cutting-room-floor notes.
> Formatting normalized for repository consistency only.

---

## 1. Portfolio Name

*[The model's chosen portfolio name]*

## 2. Thesis

**Thesis headline:** *[one punchy sentence]*

*[≤150-word thesis paragraph]*

## 3. Holdings

| Ticker | Allocation % | Rationale |
|---|---:|---|
| TICKER1 | 14.0% | One-line rationale |
| TICKER2 | 10.0% | One-line rationale |
| ... | ... | ... |
| **TOTAL** | **100.0%** | — |

## 4. Risk Acknowledgment

*[Three sentences — the biggest threats over the 25 days]*

## 5. Construction Memo

*[≤300 words — construction logic, factors weighted, data pulled, what was ignored and why]*

## 6. Self-Identification

- **Model name:** *[…]*
- **Maker:** *[…]*
- **Version string (as the model reports it):** *[…]*
- **Date/time of construction (as the model states):** *[…]*

## 7. The Cutting-Room Floor — what was PASSED on

> Captured BLIND, before any results exist. As important to the contest as the picks.

**Pool stance (all 9):** one line each — overweight / market-weight / underweight / avoiding, and why.

- **Arsenal of Democracy:** *[…]*
- **Powering America:** *[…]*
- **Build It Here:** *[…]*
- **Made in USA:** *[…]*
- **Main Street Americana:** *[…]*
- **Silicon Republic:** *[…]*
- **Capital & Trust:** *[…]*
- **Heartland:** *[…]*
- **Amber Waves:** *[…]*

**Notable passes (15–25):** universe names seriously considered but excluded — one line each, including any large/obvious names deliberately avoided.

| Ticker | Why passed |
|---|---|
| TICKER | One-line reason |
| ... | ... |

---

## Host attestation

- **Prompt sent to contestant:** *[YYYY-MM-DD HH:MM TZ]*
- **Submission received by host:** *[YYYY-MM-DD HH:MM TZ]*
- **Prompt version used:** [`submission-prompt.md`](../submission-prompt.md) at commit `[short-sha]`
- **Submission integrity:** verbatim copy of the contestant's response; only formatting normalized.
- **Sources the contestant disclosed using:** *[summary]*

## Notes

*[Optional host notes — clarifying questions the contestant asked (and that the host declined to answer on the merits), anomalies, etc. "None." if none.]*
