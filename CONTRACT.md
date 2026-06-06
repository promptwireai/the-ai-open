<!--
  CONTRACT.md — The Contest Contract, v1.0
  Lives at the root of github.com/promptwireai/the-ai-open.
  This file is the canonical authoring reference. Where this file and any other
  document disagree, THIS FILE WINS.
-->

# The Contest Contract

**Version:** 1.0 · **Status:** stable · **Audience:** humans authoring a new contest, and machines (loaders, validators, IDE language servers, the future `create_contest` tool)

This is the public contract for *The AI Open* — a defined, machine-validated shape every contest in this repository conforms to. It exists so the rules are knowable in advance, the receipts are auditable after the fact, and the website that renders all of this can do so without bespoke code per contest.

It is also, deliberately, a public contract. Anyone can fork this repo, validate manifests against the published schemas, propose a new category via PR, or build their own client on top of the same data. *Receipts before opinions* applies to the rules of the contest themselves, not just to the contestants.

## How to read this document

The fastest path for first-time authoring: §1 (the mental model — read this first or nothing else will make sense) → §3 (identity) → §4 (cross-cutting fields) → §6 (portfolio extensions, if you're authoring a portfolio contest) → §10 (worked example you can copy) → §12 (the new-contest checklist). The validator (§11) will catch anything you miss.

For a quick reference of which features actually run today vs. which validate but are reserved for future work, see **Appendix A**.

## §0. Spec versioning

This is `Contest Contract v1.0`. The contract follows semantic versioning:

| Change | Bump |
|---|---|
| Editorial clarification, no field changes | none (republish in place) |
| New optional field, new enum value, new category | minor (`1.1`, `1.2`, …) |
| Removed field, renamed field, changed default, type change | major (`2.0`, …) |

A new major version means the schema lives at a new versioned path (`schemas/v2/`). Every manifest declares which version it was authored against:

```yaml
spec_version: "1.0"
```

Manifests authored against v1.0 stay valid against v1.0 *forever*. The loader picks the validator that matches the manifest's `spec_version`. This is how the contract evolves without breaking past commitments.

> **The day this spec went public is the day we committed to honoring it.** If you reach for "we'll just change the field's meaning," the answer is `2.0`, not a quiet edit.

---

## §1. The mental model: shell vs. receipts

A contest lives in **one folder** in this repo, at `contests/{category}/{year}-{slug}/`. Internalize this division before you touch anything:

> **`contest.yaml` is the SHELL. The receipts live in other files.**
>
> The shell holds *identity, dates, rules-as-numbers, and pointers* (who competes by id, the position caps, where the universe file is). It NEVER holds the competitive content itself: no holdings, no weights, no per-ticker rationales, no thesis prose, no model output. Those are **verbatim receipts** — they live in `submissions/*.md` and are parsed, never re-typed into the manifest.

This is enforced, not stylistic. The manifest is parsed in **strict mode** (§11). If you paste a `holdings:` block, a `weights:` map, a `rationale:`, or a `thesis:` into `contest.yaml`, the loader **throws** (`unrecognized key: holdings`) — it does not silently accept or ignore them. The receipt lives only in `submissions/*.md`.

### The author-vs-derived principle

The second rule that prevents most mistakes:

> **Author the SOURCE; never author a value the loader can COMPUTE.**

Anything derivable from what you already wrote is derived; writing it yourself is at best redundant and at worst a stale lie the strict parser rejects. The derived values you must NOT author:

| Derived value | Computed from | Do not author |
|---|---|---|
| `season` (number, end-year, label) | `open_date` vs the Nov-30 epoch (§3) | `season:` — *except* the rare reset-straddle override (§4) |
| `duration` ("25-day contest") | `close_date − open_date`, inclusive | any `duration:` / `season_days:` key |
| `universe_size` | count of Ticker rows in `universe.md` (§7) | `universe_size:` — *except* as an optional checksum (§6) |
| layer counts (per-layer tallies) | the `layers.yaml` tickers map (§7) | hand-typed counts anywhere |
| "Day N of M", progress-bar fill | today's date vs `[open_date, close_date]` | any day counter |
| `repo_path` | `contests/` + `id` + `/` | any path key |
| `roster_source` (manifest vs submissions) | `roster_mode` (§4, §9.3) | `roster_source:` — not an authored field |
| standings / rank / return / sparkline | live data × contest state | any of these — runtime data |

**Inclusive day-count convention (load-bearing).** Both `duration` and "Day N" are **inclusive of both endpoints**. May 18 → Nov 23 derives **190** days (not 189); June 10 → July 4 derives **25** days. (Season 0's literal `SEASON_DAYS = 189` is a known off-by-one; the manifest derivation gives the correct 190.) See Appendix B for the gotcha record.

### The contest folder — text only

| File | Required? | Authored or parsed? | What it is |
|---|---|---|---|
| `contest.yaml` | **yes** | authored | The shell. This spec. |
| `universe.md` | yes (portfolio) | authored table, **parsed** | The tradable list. Cols *Ticker* + *Layer* load-bearing; rest advisory. §7. |
| `layers.yaml` | yes (portfolio) | authored | The per-contest editorial layer taxonomy. §7. |
| `rules.md` | yes | authored prose | Human-readable rules. Numbers here MUST match the manifest. |
| `submission-prompt.md` | yes | authored prose | The exact prompt the contestants received. A receipt. |
| `submissions/*.md` | yes (closed roster) | **verbatim receipts, parsed** | One file per entrant: holdings, weights, rationales, thesis. Frontmatter contract in §7. |
| `results/` | created empty | runtime | Clarifications, disclosures, computed output land here later. |

**Branding media (card images, hero images, video) is NOT part of this contract.** The public repo is the factual/textual record; branding lives in the website that renders it. A contest's media is attached during admin onboarding in `promptwire-web` and served from the site's own storage. The repo stays small, the commit history stays meaningful, and the contest folder stays human-readable.

**Submission frontmatter contract (your obligation when you write the `_TEMPLATE.md`).** Each `submissions/*.md` carries YAML frontmatter that MUST include:
- `contestant_id:` — **required.** The bare contestant-id (`claude`, not the filename). This is the file→contestant join; the loader never infers the contestant from the filename.
- `version:` + `model_string:` — the normalized snapshot (e.g. `version: "Opus 4.8"`, `model_string: claude-opus-4-8`). For an LLM, the version + API model id; for a SaaS product, the product version string; for any kind, whatever uniquely pins the snapshot that competed.
- `reasoning_time:` — optional (null when not captured or not applicable).
- A `**Thesis headline:**` marker in the thesis section — an explicit marker, not a first-sentence heuristic, so the headline stays verbatim.

The holdings table, per-ticker rationales, and thesis body are the verbatim receipt — parsed, never authored into the manifest.

**Every required companion file** is specified field-by-field in §7 — "required" never means "figure out the format yourself."

---

## §2. Recommended file header (for IDE autocomplete)

At the top of every `contest.yaml`, add this line so VS Code and any other yaml-language-server client gives you field-level autocomplete and inline validation as you type:

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json
```

This is a comment to YAML — it does not affect parsing — but it is the difference between authoring blind and authoring with a live validator at your elbow. See Appendix C for setup notes.

---

## §3. The identity model — Season · Category · Series · Edition

Every contest's identity is four parts: two you author, one is derived, one is a display string you author.

### Season — DERIVED, almost never authored

A **Season** is the platform *epoch*: one operating year, **Nov 30 → Nov 30**. It is a shared platform clock, **not** a per-format counter. Every contest opening in a window belongs to that Season — a 2028 cooking contest is simply a **Season 2** contest; it does not start its own "Season 0 of cooking."

- **Displayed:** `"Season N · {end-year}"`, where end-year is the calendar year the season's Nov 30 close falls in. `Season 0 · 2026` is the foundations year; `Season 1 · 2027` follows.
- **Anchor:** `SEASON_EPOCH = 2026 → Season 0`. The number is `endYear − 2026`.
- **Derivation:** `deriveSeason(open_date)`. The season is governed by **`open_date`, not `close_date`** — *a contest belongs to the season it STARTS in.* The epoch boundary flips at **Nov 30**: a contest opening on or before Nov 30 of year Y has end-year Y; one opening after Nov 30 rolls to Y+1.

Worked: July-4 opens `2026-06-10` (≤ Nov 30 2026) → end-year 2026 → `Season 0 · 2026`. A 2028 contest → `2028 − 2026 = Season 2 · 2028`. A song contest opening `2027-03-01` → `Season 1 · 2027`.

**You do not author `season:`.** The one exception is in §4.

### Category — authored, the pivot

`category` is the *kind* of contest (`portfolio`, and later `song`, `code`, `forecast`, …). It is the single field the platform switches on: it selects the scorer and the `extensions:` schema. Today the only built category is `portfolio`.

### Series — authored, the record book

`series` is the **repeatable FORMAT that carries year-over-year records** — the thing that makes "the 2027 July-4 edition beat the 2026 one" a sentence the platform can answer. It is a slug (`july-4`, `portfolio-foundations`). Set it to `null` only for a true sealed one-off.

**Recurrence = `series != null`.** This is the *only* place recurrence is expressed. It is NOT a `lifecycle_kind` value, and it must stay consistent with `cadence` (§4).

### Edition — authored, the display name

`edition` is the run's display name: `"The Foundations Run"`, `"The 250"`. Free text.

### Composed display (the loader builds these; never author them)

- `seasonLabel = "Season {N} · {endYear}"` → `"Season 0 · 2026"`
- `contest name = "{seasonLabel} · {edition}"` → `"Season 0 · 2026 · The 250"`
- user badge = `"{edition} · {Cadence} · {derived duration}"` → `"The 250 · Annual · 25-day contest"`

---

## §4. Top-level fields (cross-cutting — identical across every category)

These fields are the same shape for *every* contest type. Only the `extensions:` block (§6) changes by category. The **Default** column matters: a field with a default is **omittable** — type it only to override.

| Field | Type | Required? | Default | Allowed values | Meaning · when to pick |
|---|---|---|---|---|---|
| `spec_version` | string | **yes** | — | `"1.0"` | Which version of this contract the manifest is authored against (§0). |
| `id` | string | **yes** | — | `{category}/{year}-{slug}`, regex `^[a-z0-9-]+/\d{4}-[a-z0-9-]+$` | The PK, repo path, URL fragment, and dispatch slug, all in one. **Must equal the manifest's own directory** — the loader asserts it. e.g. `portfolio/2026-july4-250`. |
| `category` | enum | **yes** | — | `portfolio` (only built value today) | The discriminant. Selects scorer + `extensions:` schema. |
| `series` | string\|null | no | `null` | slug `^[a-z0-9-]+$`, or `null` | The record-book key. **Default to a slug, not null** — author `null` only when you are certain this is a sealed one-off. **Minting:** pick a stable, year-agnostic kebab-case noun for the FORMAT (`july-4`, never `july-4-2026`); reuse the exact existing spelling if the format already ran. All manifests sharing a slug must share a `category` (build-checked). |
| `edition` | string | **yes** | — | non-empty free text | The run's display name. `"The 250"`. |
| `season` | int | no (override only) | derived | a season number | **You normally OMIT this** — season derives from `open_date` (§3). Author it ONLY when the date-derived season disagrees with the one you want the contest filed under. If `deriveSeason(open_date)` already gives the season you want (the normal case), never write it. |
| `scoring_kind` | enum | **yes** | — | see §9.1 | How winners are determined. Today only `objective-automated` is wired. |
| `lifecycle_kind` | enum | **yes** | — | `continuous` \| `episodic` \| `realtime` (§9.2) | The shape of competition over time. **NOT a recurrence value** — `recurring` does not exist. |
| `roster_mode` | enum | no | `closed` | `closed` \| `open` \| `products` (§9.3) | Where competitors come from. |
| `interaction` | enum | no | `parallel` | `parallel` \| `adversarial` (§9.4) | Do competitors affect each other? |
| `cadence` | enum | **yes** | — | `one-off` \| `annual` \| `monthly` \| `weekly` \| `daily` | Does the format repeat, and how often? Distinct from `duration` (how long one run lasts — derived) and from rebalance `kind` vocabulary. **Keep `cadence` and `series` consistent:** `one-off` pairs with `series: null`; any repeating cadence pairs with a non-null `series`. |
| `open_date` | date `YYYY-MM-DD` | **yes** | — | a date | The buy/start date. **Governs season derivation.** The day-0 baseline. |
| `close_date` | date `YYYY-MM-DD` | **yes** | — | a date ≥ `open_date` | The end date. Drives `duration`, "Day N of M", and the progress bar — all computed. |
| `submission_window_close` | date | no | omit | a date | Author this ONLY for `lifecycle_kind: episodic` (where §11 requires it). For every other contest — including closed blind-lock contests — **omit it entirely.** |
| `voting_window_open` | date\|null | no | `null` | a date or `null` | Reserved. Author only for a subjective/hybrid `scoring_kind` (§11 gates this both ways). `null` for objective contests. The voting *method* lives in the extension, not here. |
| `voting_window_close` | date\|null | no | `null` | a date or `null` | As above. |
| `rank` | object | no | `{ direction: desc, tie_breakers: [] }` | see below | **Cross-cutting** ranking contract — the shared leaderboard reads it generically for every category. Omittable if the defaults fit. |
| `rank.direction` | enum | no | `desc` | `asc` \| `desc` | Sort order of the score. `desc` = higher wins. `asc` = lower wins (e.g. a forecasting Brier score). |
| `rank.tie_breakers` | string[] | no | `[]` | category-specific tokens, applied in order | Ordered fallback keys on a tie. **For `category: portfolio` the legal tokens are exactly `sharpe` and `max_drawdown`** — the validator rejects any other token for portfolio. Order matters. `[]` (no tie-breaker) is legal. A future category defines its own token set. |
| `roster` | string[] | conditionally | `[]` | contestant-ids from `contestants.yaml` (§5) | The competitors, by stable contestant-id. **Required non-empty** when `roster_mode` is `closed` or `products`. **Must be empty** when `roster_mode: open` (entrants arrive via submissions). |
| `snapshots` | map | no | omit | `{ <contestant-id>: { version, model_string } }` | Per-contestant version metadata. See the decision rule below. |
| `prize` | string\|null | no | `null` | free text or `null` | Display-only prize name (`"Hall of Picks"`). Reserved. |
| `visibility` | enum | no | `private` | `private` \| `public` | Publication gate (§8). |

**`roster_source` is NOT an authored field — it is DERIVED from `roster_mode`.** The loader infers participant-population behavior: `open` → participants come from submissions; `closed`/`products` → from this manifest's `roster`. You never write `roster_source`.

### When to author `snapshots:`

Mechanical: **open the submission `_TEMPLATE.md` and check its frontmatter.**

- If each submission's frontmatter already carries normalized `version:` and `model_string:` keys (the greenfield case), **omit** `snapshots:` — the loader reads them per-submission.
- If the frontmatter lacks those keys, or carries a drifted legacy `model:` value, **write** `snapshots:` — one entry per roster contestant-id, each `{ version, model_string }`.
- If both exist, the **manifest `snapshots:` block wins.** When in doubt, write the block: it is never wrong, only sometimes redundant.

---

## §5. The contestants registry (`contestants.yaml`)

The `roster` field holds foreign keys into a single **platform-level `contestants.yaml` registry** at the repo root. You never define a contestant inside `contest.yaml`.

### The lineage rule

One row per **lineage**, not per version. `claude` is a row; `claude-opus-4-7` is not. `suno` is a row; `suno-v4.5` is not. The specific version that competed in a given contest is pinned at contest-time via the per-contest `snapshots:` block (§4) or the submission frontmatter (§7), where it belongs.

This keeps the registry small and stable. Frontier-model versions churn every few months — if the registry tracked them, every new release would touch this file. Lineages don't churn; new ones get added rarely.

### Why "contestant" and not "agent"

A contestant can be an LLM, a SaaS product, a robot, a human team, or — eventually — something we haven't imagined yet. The registry must handle all of them. The `kind` field is the discriminant:

| `kind` | Status | What it is | Example |
|---|---|---|---|
| `llm` | **built** | A large-language-model lineage. Used by every contest shipped so far. | `claude`, `chatgpt`, `gemini`, `grok`, `deepseek` |
| `saas-product` | reserved | An AI-powered SaaS product competing as a product, not a model. | `suno`, `udio`, `runway` |
| `robot` | reserved | A physical-AI system or robotics platform. | `optimus`, `figure-02` |
| `team` | reserved | A human team or human-AI collaboration competing as a unit. | `team-anthropic-creative` |

Like the manifest, the registry uses a **common header** every contestant shares (`id`, `kind`, `contestant`, `monogram`, `team_color`, plus a maker/vendor field appropriate to the kind) and a **kind-specific `extensions:` block** for the rest.

### The registry shape

`contestants.yaml` is a map keyed by contestant-id (so the loader does direct FK lookup, and duplicate ids fail at parse):

```yaml
spec_version: "1.0"
contestants:

  claude:
    kind: llm
    contestant: "Claude"
    maker: "Anthropic"
    monogram: "Cl"
    team_color: "#ff8c42"
    extensions:
      default_access_surface: "claude.ai — Max plan"
      default_configuration: "Extended thinking + Web search"

  chatgpt:
    kind: llm
    contestant: "ChatGPT"
    maker: "OpenAI"
    monogram: "Ch"
    team_color: "#10a37f"
    extensions:
      default_access_surface: "chatgpt.com — Pro plan"
      default_configuration: "Thinking mode"

  # … gemini, grok, deepseek …

  # A reserved-kind example — present so the schema can be exercised; not used in any built contest yet:
  suno:
    kind: saas-product
    contestant: "Suno"
    maker: "Suno, Inc."
    monogram: "Su"
    team_color: "#7c3aed"
    extensions:
      product_url: "https://suno.com"
      default_plan_tier: "Pro"
```

### Common contestant fields

| Field | Required? | Meaning |
|---|---|---|
| `kind` | **yes** | The discriminant (`llm` \| `saas-product` \| `robot` \| `team`). |
| `contestant` | **yes** | Display name (`"Claude"`, `"Suno"`). |
| `maker` | **yes** | Organization that owns the lineage (`"Anthropic"`, `"Suno, Inc."`). |
| `monogram` | **yes** | Two-character glyph for the team tile (`"Cl"`). |
| `team_color` | **yes** | Hex color (`"#ff8c42"`). Used for cards, sparklines, badges. |

### `kind: llm` extensions

| Field | Meaning |
|---|---|
| `default_access_surface` | Where the model is being used (`"claude.ai — Max plan"`). Per-contest overrides allowed in submission frontmatter. |
| `default_configuration` | The default mode/tools (`"Extended thinking + Web search"`). Per-contest overrides allowed. |

### `kind: saas-product` extensions (reserved)

| Field | Meaning |
|---|---|
| `product_url` | The product's public URL. |
| `default_plan_tier` | Plan/tier the product is competing on (`"Pro"`, `"Enterprise"`). |

### `kind: robot` and `kind: team` extensions

Reserved. Schema admits them; field set will firm up the first time a robot or team contest enters the planning stage. Adding them is a minor version bump (§0).

### Registry hygiene

- **Add a row BEFORE referencing it in a `roster`.** The loader throws if a roster id has no registry row.
- **Never re-purpose an id.** If a lineage truly retires and a different lineage takes its slot, mint a new id; do not edit the old row.
- **Per-contest snapshots pin the specific version** — see `snapshots:` in §4.

---

## §6. Portfolio extensions (`extensions:`)

Everything portfolio-specific sits under `extensions:`. A non-portfolio contest omits this block and supplies its own. The generic `rank` contract lives at the top level (§4); the extension below carries only the portfolio-specific elaboration.

| Field | Type | Required? | Default | Allowed values | Meaning · when to pick |
|---|---|---|---|---|---|
| `capital` | number | **yes** | — | positive number | Paper dollars per portfolio. The share divisor and the return-% denominator. It is `10000` for every contest so far — author it explicitly: `capital: 10000`. It MUST equal the figure stated in `rules.md`. A non-10000 value is accepted but logged as a loud warning. |
| `universe_path` | string | no | `universe.md` | a relative filename | Points at the tradable list (§7). |
| `layers_path` | string | no | `layers.yaml` | a relative filename | Points at the per-contest layer taxonomy (§7). |
| `sector_taxonomy` | enum | no | `soft` | `soft` \| `none` | Controls the universe's *optional* Sector column. `soft` if `universe.md` has a Sector column you want feeding the explorer's advisory buckets; `none` if it has no Sector column. |
| `universe_size` | int | no (checksum) | derived | a count | DERIVED — the count of *Ticker rows* parsed from `universe.md`. If you include it, the loader asserts your number equals the parsed row count. A guardrail, not a source. |
| `position_min` | int | **yes** | — | a count | Minimum number of names a portfolio may hold. |
| `position_max` | int | **yes** | — | a count ≥ `position_min` | Maximum number of names. |
| `max_position_pct` | number | **yes** | — | a positive % | Single-position weight cap, in percent. |
| `weight_sum_tolerance` | number | no | `0.05` | a small positive number | Σweights must equal 100.0 ± this. |
| `price_source` | enum | no | `alpaca` | `alpaca` (closed enum — only legal value today) | The market-data provider. |
| `price_feed` | enum | no | `iex` | `iex` \| `sip` | `iex` = the free IEX feed; `sip` = the consolidated/paid feed. |
| `price_adjustment` | enum | no | `raw` | `raw` \| `split_div` | `raw` = unadjusted closes; `split_div` = split/dividend-adjusted. |
| `benchmarks` | array | no | `[]` | see below | "Vs the market" context lines. **Do NOT affect rank.** |
| `metric` | object | **yes** | — | `{ primary: total_portfolio_value }` | Declares WHAT is scored. `primary` is a **closed literal** — `total_portfolio_value` is the only accepted value today. `rank.direction` (top level) declares HOW to order it. |
| `clarifications_path` | string | no | omit | a relative path | Points at a `results/clarifications.md` carrying reasoning-time data, if present. |
| `rebalance` | object | no | omit (⇒ buy-and-hold) | see below | Turnover windows. **Absent ⇒ buy-and-hold ⇒ exactly one period (index 0) per contestant, ever.** |

**`benchmarks` entries.** Two shapes:
- `{ ticker: SPY, label: "S&P 500" }` — a real, priced ticker. Benchmark tickers are independent of the contest universe — they need not be held or even in `universe.md`, and may be proxies (e.g. `SPY` for the S&P 500; see Appendix B).
- `{ synthetic: consensus, label: "Consensus Basket", priced: false }` — a display-only synthetic. `synthetic` accepts **only** the literal `consensus`; it is always `priced: false`.

**`rebalance` shape** (only when present):
- `rebalance.schedule` — a list of `{ date, kind }`, where `kind` is `monthly` \| `quarterly` \| `annual` (the closed `RebalanceKind` enum — never `open`/`close`, which are derived triggers). On a date collision the higher tier wins (`quarterly` > `monthly`). **Every schedule date must satisfy `open_date < date ≤ close_date` and the list must be strictly ascending** (§11).
- `rebalance.caps` — a map keyed by the *same* `RebalanceKind` enum, each `{ turnover_cap: <percent> }`. Season-0 values: `monthly: 15`, `quarterly: 40`, `annual: 100`.

---

## §7. The companion files

`contest.yaml` is the shell; the rest of the contest folder carries the data and the receipts.

Two taxonomies coexist and are modeled distinctly:

- **Editorial LAYER taxonomy** (`layers.yaml`) — the narrative grouping. Every **held** ticker must map to exactly one layer; an unmapped held ticker **throws** (launch-blocker). Universe names never held need no layer.
- **Sector taxonomy** (the optional Sector column) — advisory, undefined-tolerant, feeds only the universe explorer. Declared via `sector_taxonomy` (§6).

### `universe.md`

Human-readable Markdown with section headings and one Markdown table per section. The parser reads two columns as **load-bearing**: **col 1 = Ticker**, **col 4 = Layer**. Company (col 2) is advisory (reconciled against the price provider at ingest); Sector/Qual/⚑ are advisory.

```markdown
### Arsenal of Democracy — defense, aerospace … (30)   ← the "(30)" is an ASSERTION, verified, never trusted

| Ticker | Company | Sector | Layer | Qual | ⚑ |
|---|---|---|---|---|---|
| LMT | Lockheed Martin | Defense & Aerospace | arsenal | F | |
| RTX | RTX Corporation | Defense & Aerospace | arsenal | F | |
…
```

Section-heading counts and any summary table are **verified against the parsed rows, never trusted as the source**. The loader reads the universe as-published and applies `results/disclosures.md` corrections separately — it never edits the immutable receipt.

**The compact ticker-list block — OPTIONAL, advisory.** You *may* add one fenced block listing every symbol, for prompt-embedding and cheap grepping. It is **advisory, NOT load-bearing**.

### `layers.yaml`

The per-contest editorial taxonomy. Two blocks: an **ordered** `layers:` list and a `tickers:` map.

```yaml
# Per-contest editorial layer taxonomy.
layers:                                  # ordered → render order + legend; ids are slugs
  - { id: arsenal,          label: "Arsenal of Democracy",  order: 1 }
  - { id: powering-america, label: "Powering America",      order: 2 }
  # … the layers, in order …

tickers:                                 # ticker → layer-id (held names; universe-only names may be omitted)
  LMT: arsenal
  RTX: arsenal
  # … one line per held name …
```

**Colors do NOT live here.** `label`/`order` are authored taxonomy; the CSS color token (`--L-<id>`) is website presentation. The loader's reconcile gate **fails loud** if any layer-id has no matching `--L-<id>` token in the website's stylesheet.

**The reconcile gate** (held-tickers-only, runs at load): parse `universe.md` cols 1+4; parse `layers.yaml`; for every ticker that appears in a held portfolio, assert `universe Layer == layers.yaml tickers[ticker]`, 1:1, zero orphans; derive per-layer counts; assert every layer-id has a `--L-<id>` CSS token.

### `rules.md` — the human-readable rulebook

The plain-English rules the audience and contestants read. The loader does **not** parse it. Its one hard obligation: **every number in it MUST match the manifest.** If they disagree, the manifest is what *runs*, but `rules.md` is what contestants were *promised* — fix `rules.md` so they agree.

Format — GitHub-flavored Markdown, the proven shape:
- A header block — **Category · Format · Window · Duration** — then a one-line "**These rules are locked**" statement.
- Numbered sections: **1** Universe · **2** Portfolio constraints · **3** Starting capital · **4** Execution mechanics · **5** Rebalance windows · **6** Information access · **7** Scoring · **8** Commentary requirements · **9** Contestants · **10** Host's role · **11** Disputes & disclosures · **12** Awards.
- A closing "*Rules locked: <date>*".

**The numbers that MUST match the manifest:**

| `rules.md` states | must equal |
|---|---|
| Starting capital | `extensions.capital` |
| Position count + max size | `position_min` / `position_max` / `max_position_pct` |
| Turnover caps | `extensions.rebalance.caps` |
| Rebalance dates | `extensions.rebalance.schedule` |
| Window (open / close) | `open_date` / `close_date` |
| Scoring metric + tie-breakers | `metric.primary` + `rank.tie_breakers` |
| Contestants + versions | `roster` (+ `snapshots` / submission frontmatter) |

### `submission-prompt.md` — the canonical prompt (a receipt)

The *exact* prompt sent to every contestant, committed **before** it was sent — the receipt proving every contestant got the identical task.

Format — framing for repo-readers, then the transmitted prompt fenced by literal markers (only what's between them was sent), then a notes tail (lock date, sent date, due date, lock-in time, pointers):

```
--- PROMPT BEGIN ---
<everything here, and ONLY this, was sent to the contestants>
--- PROMPT END ---
```

**The prompt body must contain** (and stay consistent with the rest of the folder):
- The task — construct a portfolio of N names from the universe, allocations sum to 100.0%, starting capital $X.
- Hard rules — **the same numbers as `rules.md`**.
- Scoring (primary metric + tie-breakers).
- A **"Required Deliverables — Return in This Exact Format"** list that matches the `submissions/*.md` body one-for-one (Portfolio Name · Thesis · Holdings Table `Ticker \| Allocation % \| Rationale` · Risk Acknowledgment · Construction Memo · Self-Identification).
- Disclaimers ("not financial advice"; output is published).
- The universe embedded as the compact ticker list.

### `submissions/*.md` — the entrant receipts (parsed)

One file per entrant — the **verbatim** record of what each contestant returned. For a `closed` roster the host collects these before lock; the loader **parses** them into the participant + period-0 + holdings rows.

**Filename:** the **bare contestant-id** — `claude.md`, `chatgpt.md`, `gemini.md`, etc. (The file→contestant join uses the frontmatter `contestant_id`, not the filename.)

**Required frontmatter:**

```yaml
---
contestant_id: claude            # REQUIRED — bare id; the file→contestant join
version: "Opus 4.8"              # REQUIRED — normalized display snapshot
model_string: claude-opus-4-8    # REQUIRED — exact API id (forensic)
reasoning_time: "14m 46s"        # optional — null if not captured
contestant: "Claude"             # descriptive ↓
maker: "Anthropic"
access_surface: "claude.ai — Max plan"
configuration: "Extended thinking + Web search"
submitted_at: "2026-06-09T20:30:00-04:00"
host: "Promptwire"
---
```

**Required body sections** (parsed; they mirror the prompt's exact format):

| § | Section | Loader behavior |
|---|---|---|
| 1 | **Portfolio Name** | → `participant.portfolioName` (verbatim) |
| 2 | **Thesis** with a `**Thesis headline:**` line | headline parsed from that marker (verbatim); body → `thesisBody` |
| 3 | **Holdings** — `\| Ticker \| Allocation % \| Rationale \|`, ending in a `\| **TOTAL** \| **100.0%** \| — \|` row | TOTAL stripped; asserts Σ = 100 ± `weight_sum_tolerance` and every ticker ∈ `universe.md`; ticker/weight/rationale carried **verbatim** → period-0 holdings |
| 4 | **Risk Acknowledgment** | receipt (not structurally parsed) |
| 5 | **Construction Memo** | → period-0 `memoMarkdown` (verbatim) |
| 6 | **Self-Identification** | receipt; the authoritative snapshot is the frontmatter |

…followed by a **Host attestation** block (prompt-sent / received timestamps, prompt commit SHA, the verbatim-integrity attestation, disclosed data sources) and an optional **Notes** block.

**Verbatim is law:** holdings, weights, rationales, and thesis are copied **exactly** as returned. The host normalizes only *formatting* (table/heading levels), never content. Inline `[Citation](url)` links some models embed in rationale cells are mechanically stripped by the loader (a documented transform).

---

## §8. Visibility & lifecycle state

There is exactly **one** state knob you author. The rest is derived from dates.

`visibility` (default `private`):
- `private` = scaffolded but only the admin sees it (preview).
- `public` = listed publicly.

The **live/coming-soon/closed** states are NOT authored — they are **derived from `open_date`/`close_date`** for any `public` contest:

- `public` + today < `open_date` → appears in the homepage **"Coming Soon"** carousel.
- `public` + `open_date` ≤ today ≤ `close_date` → **live leaderboard**.
- `public` + today > `close_date` → **results** view.

A `private` contest shows none of these publicly, regardless of date.

> The full multi-state lifecycle machine (announced / judging / archived / …) is **deferred**. `visibility` is the only state knob today.

---

## §9. The four reserved taxonomy axes

Four enum fields classify a contest along orthogonal axes. **All values are legal to author NOW** (the schema accepts them), but most machinery behind the non-default values ships later. Each value below is marked **built** (works end-to-end today) or **reserved** (validates, but the projector/scorer is a defined no-op or future work). The illegal *combinations* are in §9.5 / §11.

### 9.1 `scoring_kind` — how winners are determined

| Value | Status | When to pick |
|---|---|---|
| `objective-automated` | **built** | Score computed from data, no human judgment — e.g. portfolio value from live prices. |
| `objective-manual` | reserved | Objective but measured by a human (e.g. a physical-build measurement protocol). |
| `subjective-vote` | reserved | Public vote decides. Requires a voting window. |
| `subjective-panel` | reserved | A named judging panel decides. Requires a voting window. |
| `hybrid` | reserved | Mix of automated metrics and human/vote judgment. Requires a voting window. |

### 9.2 `lifecycle_kind` — the shape of competition over time

| Value | Status | When to pick |
|---|---|---|
| `continuous` | **built** | One unbroken window from open to close, scored continuously. |
| `episodic` | reserved | Distinct rounds/episodes with a submission window before each. Requires `submission_window_close`. |
| `realtime` | reserved | Scored live as events happen (e.g. a game arena). |

> **`recurring` is not a value here.** A repeating contest sets `series: <slug>` + `cadence: annual|monthly|…`. `lifecycle_kind` is only `continuous` \| `episodic` \| `realtime`.

### 9.3 `roster_mode` — where competitors come from

| Value | Status | When to pick | `roster` field |
|---|---|---|---|
| `closed` | **built** | Competitors named up front. | required, non-empty |
| `open` | reserved | Entrants unknown before start; site users submit. Enrollment closes at start. | **must be empty `[]`** |
| `products` | reserved | Curated SaaS products/companies compete; each contestant-id represents a product, not a model. | required, non-empty |

### 9.4 `interaction` — do competitors affect each other?

| Value | Status | When to pick |
|---|---|---|
| `parallel` | **built** | Each competitor runs independently against the same conditions; no head-to-head moves. |
| `adversarial` | reserved | Competitors play against each other. |

### 9.5 Illegal combinations (rejected at parse — §11)

- `voting_window_*` set **without** a subjective/hybrid `scoring_kind` → reject.
- A subjective/hybrid `scoring_kind` **without** a voting window → reject.
- `interaction: adversarial` **with** `scoring_kind: objective-automated` → reject.
- `lifecycle_kind: episodic` **without** `submission_window_close` → reject.
- `roster_mode: open` **with** a non-empty `roster` → reject.
- `series: null` **with** a repeating `cadence` (or vice versa) → reject.

---

## §10. Worked examples

### 10a. July-4 "The 250" — the real, fully-annotated `contest.yaml`

The file you'd copy to start a new portfolio contest. Every line is commented; OMITTED lines show what you deliberately leave out (the loader derives them).

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json
# contests/portfolio/2026-july4-250/contest.yaml
# The AI Open · The 250 — America's 250th-birthday buy-and-hold sprint.

# ─── CONTRACT BINDING ────────────────────────────────────────────────────────
spec_version: "1.0"

# ─── IDENTITY ────────────────────────────────────────────────────────────────
id: portfolio/2026-july4-250    # MUST equal this file's directory. PK + URL + dispatch slug.
category: portfolio             # discriminant → portfolio scorer + extensions schema
series: july-4                  # the annual record book (recurrence = series != null)
edition: "The 250"              # display name
# season:                       OMITTED — derived: open 2026-06-10 ≤ Nov-30-2026 → "Season 0 · 2026"

# ─── TAXONOMY AXES (§9) ──────────────────────────────────────────────────────
scoring_kind: objective-automated   # price-scored, no human judgment
lifecycle_kind: continuous          # one unbroken open→close window
roster_mode: closed                 # contestants named up front (default; could omit)
interaction: parallel               # each portfolio independent (default; could omit)
# roster_source:                NEVER WRITTEN — derived from roster_mode (closed → manifest)

# ─── CADENCE (§4) ────────────────────────────────────────────────────────────
cadence: annual                 # repeats once a year; consistent with the non-null series
# duration:                     OMITTED — derived: 2026-06-10 → 2026-07-04 inclusive = "25-day contest"

# ─── WINDOW ──────────────────────────────────────────────────────────────────
open_date: 2026-06-10           # buy date; governs season derivation
close_date: 2026-07-04          # end date; drives duration, "Day N of M", progress bar
# submission_window_close:      OMITTED — not episodic; entries blind-lock before open operationally

# ─── RANK (§4) ───────────────────────────────────────────────────────────────
rank:
  direction: desc               # higher portfolio value wins
  tie_breakers: [sharpe, max_drawdown]   # portfolio's only two legal tokens, applied in order

# ─── ROSTER (§4 — FKs into platform contestants.yaml; the 5 already exist there) ──
roster: [claude, chatgpt, gemini, grok, deepseek]
prize: "Hall of Picks"
# snapshots:                    OMITTED — submission frontmatter carries version/model_string
# visibility:                   OMITTED — defaults to private; set `public` when ready to list

# ─── PORTFOLIO EXTENSIONS (§6) ───────────────────────────────────────────────
extensions:
  capital: 10000                # paper $; must match rules.md
  universe_path: universe.md    # the 250 names
  layers_path: layers.yaml      # the 9-layer taxonomy
  sector_taxonomy: soft         # universe.md has an advisory Sector column
  position_min: 10
  position_max: 30
  max_position_pct: 15
  weight_sum_tolerance: 0.05
  price_source: alpaca
  price_feed: iex
  price_adjustment: raw
  benchmarks:
    - { ticker: SPY, label: "S&P 500" }
    - { ticker: QQQ, label: "Nasdaq 100" }
    - { ticker: SMH, label: "Semiconductors" }
  metric:
    primary: total_portfolio_value
  # rebalance:                  OMITTED — absent ⇒ buy-and-hold ⇒ exactly one period (index 0) per contestant
```

### 10b. A song contest — the cross-cutting fields are identical

This sketch proves the top-level shape never changes; only `category`, the taxonomy values, and `extensions:` differ. (Reserved — not buildable today; shown to demonstrate the seam.)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json
spec_version: "1.0"
id: song/2027-anthem
category: song                  # different category → different scorer + extensions schema
series: anthem
edition: "The Anthem Round"
# season derived → open 2027-03-01 → "Season 1 · 2027"

scoring_kind: subjective-vote   # public vote decides (reserved)
lifecycle_kind: continuous
roster_mode: open               # entrants unknown until submission; roster MUST be empty
interaction: parallel

cadence: annual
open_date: 2027-03-01
close_date: 2027-03-02          # 1-day generation window…
voting_window_open: 2027-03-02  # …then a vote window (REQUIRED because scoring is subjective)
voting_window_close: 2027-03-16

rank:
  direction: desc               # most votes wins

roster: []                      # empty — open enrollment
visibility: private

extensions:                     # entirely different shape — defined by the song category
  brief_path: brief.md
  voting_path: voting.md
  eligibility: "one entry per registered user"
```

Every field from `spec_version` through `rank`/`roster` is the *same field* as in 10a — the platform reads them generically and switches on `category` only to pick the extension schema and scorer.

---

## §11. Validation — what fails loud

The manifest is parsed in **strict mode**. No silent acceptance of stray keys, no silent stripping. Two tiers:

### Hard gates (the loader THROWS)

| Gate | Rule | Why |
|---|---|---|
| unknown / forbidden keys | **Strict parse.** Any key not in this spec throws `unrecognized key` — including derived keys (`duration`, `season_days`, …), receipt keys (`holdings`, `weights`, `rationale`, `thesis`), or typos. | A silently-stripped key hides both typos and category errors. |
| spec_version present | `spec_version` required; must equal a published spec version. | The validator-selection key. |
| id matches folder | `id` must equal the manifest's own directory path. | The id is the PK and repo path. |
| id format | `id` matches `^[a-z0-9-]+/\d{4}-[a-z0-9-]+$`. | Stable, parseable, URL-safe. |
| series same category | all manifests sharing a `series` slug share one `category`. | Records must be joinable. |
| dates ordered | `close_date ≥ open_date`. | A negative window is nonsense. |
| series ↔ cadence consistent | `series: null` ⇔ `cadence: one-off`; non-null series ⇔ repeating cadence. | Recurrence stated two ways must agree. |
| capital present & positive | `capital` is required and > 0 (portfolio). | No share divisor otherwise. |
| Σ weights | per portfolio, Σ holding weights == 100.0 ± `weight_sum_tolerance`. | Receipts must balance. |
| held ⊆ universe | every held ticker appears in `universe.md`. | No off-universe holdings. |
| held ⊆ layers | every held ticker maps to exactly one layer (1:1, 0 orphans). | The launch-blocker layer contract. |
| CSS token coverage | every `layers.yaml` layer-id has a `--L-<id>` token in the website stylesheet. | No unstyled tags. |
| universe_size checksum | if authored, equals the parsed Ticker-row count. | Guardrail against a stale universe. |
| `position_max ≥ position_min` | extension constraint. | A degenerate bound. |
| voting requires subjective | `voting_window_*` set ⇒ `scoring_kind ∈ {subjective-vote, subjective-panel, hybrid}`. | A voting window on an objective contest is meaningless. |
| subjective requires voting | `scoring_kind ∈ {subjective-vote, subjective-panel, hybrid}` ⇒ both voting-window dates set. | A vote/panel contest with no window cannot be judged. |
| adversarial ≠ price-scored | `interaction: adversarial` ⇒ `scoring_kind != objective-automated`. | An adversarial contest cannot be price-scored. |
| episodic requires window | `lifecycle_kind: episodic` ⇒ `submission_window_close` set. | Episodes need a per-episode lock. |
| open roster empty | `roster_mode: open` ⇒ `roster == []`. | A pre-listed entrant contradicts open enrollment. |
| closed/products need roster | `roster_mode ∈ {closed, products}` ⇒ `roster` non-empty. | No competitors otherwise. |
| roster ids exist | every `roster` id has a row in `contestants.yaml`. | No phantom contestants. |
| rebalance dates in-window & ordered | every `rebalance.schedule[].date` satisfies `open_date < date ≤ close_date` and the list is strictly ascending. | An out-of-window rebalance creates a dead/duplicate period. |

### Soft / advisory (logged, not blocked)

- `capital != 10000` — loud warning (every contest so far is $10,000; a future one may differ). Confirm it matches `rules.md`.
- `sector_taxonomy: soft` with no Sector column → empty buckets (advisory, no throw).
- Section-heading counts in `universe.md` that disagree with the parsed row count → warning.
- Company names in `universe.md` that disagree with the price provider's → reconciled to the provider; warning.

---

## §12. New-contest authoring checklist

1. **Pick `category`** (today: `portfolio`) and **mint or reuse a `series` slug** (default to a slug; `null` only for a sealed one-off). Confirm the slug's `category` matches any prior editions.
2. **Compute `id`** = `{category}/{year}-{slug}` and create the folder `contests/{id}/` — the `id` must equal this path exactly.
3. **Add the schema header line** at the top of `contest.yaml` for IDE autocomplete (§2).
4. **Set `spec_version: "1.0"`.**
5. **Set the window:** `open_date`, `close_date`. Confirm the derived season is the one you want; author the `season:` override ONLY if it isn't (§4).
6. **Set the taxonomy axes** (§9): `scoring_kind`, `lifecycle_kind`, `roster_mode`, `interaction`. For standard portfolio contests these are `objective-automated` / `continuous` / `closed` / `parallel`.
7. **Set `cadence`** consistently with `series` (repeating ⇒ non-null series; `one-off` ⇒ `series: null`). Never author `duration`.
8. **Author `edition`** (display name) and optional `prize`.
9. **List the `roster`** as contestant-ids that already exist in `contestants.yaml` (add new rows there FIRST). For an `open` contest, leave `roster: []`.
10. **Set `rank`** (`direction`, and `tie_breakers` from the category's legal token set — portfolio: `sharpe`, `max_drawdown`).
11. **Decide `snapshots:`** — open `_TEMPLATE.md`: if it carries `version:`/`model_string:`, omit; otherwise write the block (§4).
12. **Fill `extensions:`** (portfolio): `capital: 10000` (must equal the figure in `rules.md`), `universe_path`, `layers_path`, `sector_taxonomy`, position caps, `weight_sum_tolerance`, price settings, `benchmarks`, `metric`. Add `rebalance` only for a rebalancing contest.
13. **Write the companion files:** `universe.md`, `layers.yaml`, `rules.md`, `submission-prompt.md`, and the submission `_TEMPLATE.md` carrying the required frontmatter contract.
14. **Collect the blind, locked `submissions/*.md`** (closed roster), filenames = bare contestant-ids.
15. **Set `visibility`** — leave `private` until ready, then flip to `public`.
16. **Validate** before committing — every hard gate in §11 must pass. Run `scripts/validate.ts` locally; CI runs it on every PR.

**What you do NOT do in this repo:**
- Add branding media (card images, hero, video). Those are attached during admin onboarding in `promptwire-web`. The public repo stays text-only.
- Author any derived field (§1).
- Pre-position the page in the website. Visibility + dates are the only state knobs.

---

## §13. Repo layout

The full public repo at a glance:

```
the-ai-open/
├── README.md
├── CONTRACT.md                       ← this document
├── METHODOLOGY.md                    ← the franchise rules (how every contest works)
├── CONTRIBUTING.md
├── LICENSE                           ← CC0
├── contestants.yaml                  ← the platform-level contestant registry (§5)
├── schemas/
│   └── v1/
│       ├── contest-manifest.schema.json
│       ├── contestants.schema.json
│       └── submission-frontmatter.schema.json
├── contests/
│   └── {category}/{year}-{slug}/
│       ├── contest.yaml              ← the shell
│       ├── universe.md               ← portfolio-specific; other categories vary
│       ├── layers.yaml               ← portfolio-specific
│       ├── rules.md                  ← human-readable rulebook
│       ├── submission-prompt.md      ← the exact prompt sent
│       ├── submissions/              ← verbatim entrant receipts
│       │   ├── _TEMPLATE.md
│       │   └── {contestant-id}.md
│       └── results/                  ← clarifications, disclosures, post-contest outputs
└── scripts/
    └── validate.ts                   ← runs §11 hard gates from CI
```

**The mental model.** `the-ai-open` is the contract and the receipts. Branding, rendering, and audience experience live in `promptwire-web` (the website that consumes this repo). A contest is *defined* here; it is *rendered* there. Both can be re-rendered by anyone — the contract is public, the data is public, the client UX is whatever someone wants to build.

---

## §14. How these files get authored — today and tomorrow

This spec describes hand-authoring because that is v1.0's starting point — but it is deliberately the **contract** the future *construction surfaces* target. All of them produce this same validated folder and pass the same §11 gates:

- **Today — hand-authored.** You create the folder and files in `the-ai-open` with this spec as your guide; the loader validates and projects.
- **Next — a Contest Builder in `promptwire-web/admin`.** A guided UI (manifest-field forms, a universe/layer editor, a rules/prompt composer) that emits the identical file set and runs the same validation. Branding (the 3:4 card, the 16:9 hero, the video) is attached at this stage, in the SaaS — not in the repo.
- **Later — an MCP `create_contest` tool.** The same validate → write → project pipeline exposed to an agent, with this spec as the tool description.

Nailing the file specs now is the prerequisite for both surfaces.

---

## Appendix A — Built today vs. reserved

At-a-glance reference of which features actually run in v1.0 vs. which validate but are reserved for future work.

| Feature | Status |
|---|---|
| `category: portfolio` | **built** |
| Any other category (`song`, `code`, `forecast`, …) | reserved |
| `scoring_kind: objective-automated` | **built** |
| `scoring_kind` ∈ {`objective-manual`, `subjective-vote`, `subjective-panel`, `hybrid`} | reserved |
| `lifecycle_kind: continuous` | **built** |
| `lifecycle_kind` ∈ {`episodic`, `realtime`} | reserved |
| `roster_mode: closed` | **built** |
| `roster_mode` ∈ {`open`, `products`} | reserved |
| `interaction: parallel` | **built** |
| `interaction: adversarial` | reserved |
| `cadence` ∈ {`one-off`, `annual`} | **built** |
| `cadence` ∈ {`monthly`, `weekly`, `daily`} | accepted; rhythms not yet wired |
| `contestant.kind: llm` | **built** |
| `contestant.kind` ∈ {`saas-product`, `robot`, `team`} | reserved |
| `rebalance` block (Season-0-style) | **built** |
| Buy-and-hold (no `rebalance` block) | **built** |
| `benchmarks` (real tickers + synthetic) | **built** |

A reserved field that's validated but unbuilt means: the manifest will parse, the gates will pass, but the website projector is a defined no-op for that path until the implementation lands. Don't author a reserved-only contest expecting it to run.

---

## Appendix B — Errata & gotchas

Load-bearing details that read as asides in the main text — collected here so they don't get lost.

**The inclusive day-count rule.** `duration` and "Day N of M" are **inclusive of both endpoints**. May 18 → Nov 23 = 190 days, not 189. June 10 → July 4 = 25 days. Season 0's literal `SEASON_DAYS = 189` is a known off-by-one in legacy code; the manifest derivation gives the correct 190. Do not author day counts.

**Benchmark proxies.** Benchmark tickers in `extensions.benchmarks` are *priced* tickers — they need not be the same as what `rules.md` names in prose. The S&P 500 is referenced as `SPX` in rules but priced as `SPY` (the ETF). The code prices what's tradable; the rules name the index. Not a bug.

**Cadence vocabulary overlap.** `monthly`, `quarterly`, and `annual` appear in BOTH `cadence` and `rebalance.caps`, but they mean different things — `cadence` = how often the whole contest repeats, `rebalance.caps` keyed by `RebalanceKind` = the turnover tier of a within-contest rebalance event. They are distinct enums that happen to share token names.

**Strict mode is unforgiving by design.** A typo'd field name will throw, not warn. This is correct behavior — a silently-accepted typo is a future bug. If a key you expect to use isn't in this spec, either you're authoring it wrong or you need a new field (which means a minor spec version bump).

**`series: null` and `cadence: one-off`** are the only legal pairing for a true one-off contest. If you set one without the other, the validator rejects.

**Snapshots write rule.** Open the `_TEMPLATE.md` first. If it carries normalized `version:`/`model_string:`, omit the manifest `snapshots:` block. Otherwise write it. When in doubt, write it — it's never wrong, only sometimes redundant.

---

## Appendix C — Schema location & IDE setup

The JSON Schemas live at versioned paths:

- `https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json`
- `https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contestants.schema.json`
- `https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/submission-frontmatter.schema.json`

**VS Code setup.** Install the `redhat.vscode-yaml` extension (the yaml-language-server client). Then either:

1. **Per-file (recommended)** — add the schema-binding comment at the top of any `contest.yaml`:
   ```yaml
   # yaml-language-server: $schema=https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json
   ```
   This gives you field-level autocomplete, hover docs, and inline validation as you type — no configuration needed.

2. **Workspace-wide** — add to `.vscode/settings.json`:
   ```json
   {
     "yaml.schemas": {
       "https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contest-manifest.schema.json": "contests/**/contest.yaml",
       "https://raw.githubusercontent.com/promptwireai/the-ai-open/main/schemas/v1/contestants.schema.json": "contestants.yaml"
     }
   }
   ```

Either approach works. Both at once is fine (per-file binding wins on conflict). Other editors with yaml-language-server support (Neovim, JetBrains IDEs, Helix) work the same way — point them at the same URLs.

**Pre-commit validation.** `scripts/validate.ts` runs every hard gate in §11 against any manifest you've touched. CI runs it on every PR; you can run it locally with `npm run validate` (or the documented invocation) before committing.

---

*The Contest Contract, v1.0. Released under CC0 1.0 Universal — public domain dedication. Fork it, build on it, propose changes via PR.*
