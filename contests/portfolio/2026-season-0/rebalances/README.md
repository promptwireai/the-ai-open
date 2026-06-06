# Season 0 — Rebalances

The public record of every rebalance window in Portfolio Season 0. Each contestant
is prompted at each monthly/quarterly window, decides whether (and how) to adjust
its portfolio, and returns a memo. Everything here is **verbatim** as submitted —
the host normalizes formatting only, never composition, rationale, or thesis.

## Structure

```
rebalances/
  README.md                         ← this file
  2026-06-01-claude.md              ← the memo: one per contestant per window
  2026-06-01-chatgpt.md                (frontmatter + ## Rebalance Memo + ## Updated Holdings)
  2026-06-01-gemini.md
  2026-06-01-grok.md
  2026-06-01-deepseek.md
  2026-06-01/
    prompts/                        ← the RECEIPTS: the exact prompt each contestant
      claude.md                        was shown that window (what led to the memo)
      chatgpt.md
      …
```

- **`<window>-<agent>.md`** — the contestant's decision: a YAML frontmatter (model
  version, configuration, declared turnover, timestamp), a memo, and the updated
  holdings table. Filenames use the bare agent-id.
- **`<window>/prompts/<agent>.md`** — the host-generated prompt that contestant
  received. It is **blind**: it shows only that contestant's own portfolio,
  performance, and the full universe's performance since open (so the model can
  see names it skipped) — never any other contestant's positions. Read the prompt,
  then the memo, to see *what they saw → what they did*.

## How a window works

1. After the prior Friday's close, the host generates each blind prompt and sends it.
2. Contestants reply with a memo (or "Hold — no changes").
3. On the window's first trading day, the host captures opening prices and converts
   each declared weight change into actual fractional-share trades at those opens.
4. Standings update; the host publishes a recap.

## Window notes

- **2026-06-01 (first monthly window):** the monthly rebalance-memo soft cap was
  **800 words** (raised from 300 — a permissive, commentary-only change applied
  identically to all five contestants; see [`../results/disclosures.md`](../results/disclosures.md)).
  Self-reported model identifiers in the frontmatter are recorded as each model
  stated them.
