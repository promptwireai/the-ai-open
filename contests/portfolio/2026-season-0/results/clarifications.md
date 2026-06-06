# Portfolio Season 0 — Clarifications Log

This file is the complete audit trail of every clarifying exchange, correction request, and self-identification verification that occurred between the host and the five contestants during Season 0 submission gathering (May 17, 2026).

It exists because *METHODOLOGY.md* commits the host to logging any clarifications and disclosing them publicly. In practice, the exchanges in this season fell into three categories — only one of which actually created new information for the contest.

---

## Principle: when does a clarification require redistribution?

Per the season's design, **only exchanges that create new information for the contest must be redistributed to all contestants.** Three categories of host-contestant exchange occurred:

**Type A — Pre-submission clarifying questions.** A contestant asked the host to interpret something in the prompt before submitting. These have the *potential* to create asymmetric information, depending on the host's response. If the host issues a substantive clarification, it must go to all contestants. If the host redirects without adding information, no redistribution is needed.

**Type B — Post-submission corrections.** The host identified a rules violation and asked the contestant to revise. These are procedural and affect only the contestant being addressed. No redistribution required.

**Type C — Self-identification verifications.** The host asked the contestant to confirm or expand on the model identity it returned. Also procedural. No redistribution required.

This file documents all exchanges in all three categories for transparency, regardless of whether they triggered redistribution.

---

## Type A: Pre-submission clarifying questions

### Claude

Claude was the only contestant who asked clarifying questions before submitting. Three questions were raised:

1. **Risk posture** — should the portfolio swing for the fences, play a measured AI-infrastructure overweight, or hedge with utilities/REITs/materials as ballast?
2. **Edge style** — lean on consensus AI-buildout winners, hunt for contrarian or under-owned names, or blend both?
3. **Memo voice** — sharp, opinionated, named-thesis style, or more neutral and analyst-toned?

**Host response.** The host declined to answer any of the three questions. The host's reasoning: each question, if answered, would tell Claude what kind of portfolio the host wanted — eliminating the thing the contest is supposed to measure, which is the contestant's own judgment. The host's reply was a redirect rather than a clarification, and contained no new information beyond what was already in the submission prompt. Verbatim excerpt: *"Construct the portfolio you think will perform best. You're being measured against four other frontier models. Your judgment is what's being tested, not mine."*

**Information asymmetry created.** None. No substantive answer was issued. The exchange was not redistributed to the other contestants because no new content was transmitted.

**Other contestants.** GPT, Gemini, Grok, and DeepSeek submitted their portfolios without raising any clarifying questions.

---

## Type B: Post-submission corrections

### Claude — math correction (one iteration)

**Issue.** Claude's initial submission summed to 100.5%, violating §2 of the rules ("Allocations sum to exactly 100.0%").

**Host re-prompt.** *"Your submitted allocations sum to 100.5%, not the required 100.0%. Adjust one or more weights and resubmit only the corrected holdings table."*

**Contestant response.** *"Apologies for the arithmetic error. Trimmed LRCX by 0.5pp."*

**Outcome.** LRCX reduced from 1.5% to 1.0%. New total: 100.0%. Resolved on first re-prompt.

### DeepSeek — math correction (three iterations)

**Initial issue.** DeepSeek's first submission contained 23 positions summing to 99%, while the stated verification line listed 24 incremental values claiming to sum to 100%. The verification text was internally inconsistent with the holdings table.

**First host re-prompt.** *"Your submitted holdings table contains 23 positions summing to 99%, while your verification line implies 24 positions summing to 100%. Please clarify: (a) is a position missing from your table, and if so what was its ticker and weight, or (b) should we adjust the existing 23 positions to sum to 100%?"*

**First DeepSeek response.** *"The missing position is SMR (NuScale Power) at a 2% allocation — a second small modular reactor play alongside OKLO that I intended to include for nuclear optionality but accidentally omitted from the table text."*

**Second issue.** After adding SMR at 2%, the resulting 24-position portfolio summed to 101%, not 100%. DeepSeek's new verification line — *"11+9+7+6+6+5+5+4+4+4+4+4+4+3+3+3+3+3+3+2+2+2+2+2 = 100.0% ✅"* — was again incorrect; those 24 values actually sum to 101.

**Second host re-prompt** (with explicit math walkthrough). The host showed DeepSeek the actual sum: *"Sum: 11+9+7 = 27. Plus 6+6 = 39. Plus 5+5 = 49. Plus 4×6 = 73. Plus 3×6 = 91. Plus 2×5 = 101. Not 100. Your original 23-position portfolio summed to 99%, so adding SMR at 2% put you at 101%, not 100%. The fix is to reduce exactly 1% from somewhere."* The host offered three forced-choice options: (a) reduce SMR from 2% to 1%, (b) reduce another 2% position to 1%, or (c) a different specific 1% reduction.

**Third DeepSeek response.** *"Reduce SMR from 2% to 1% (option a). SMR is now 1%. All other holdings unchanged. New total: 99% + 1% = 100%."*

**Outcome.** SMR position reduced from 2% to 1%. Final total exactly 100%. Resolved on third re-prompt.

**Behavioral observation.** DeepSeek produced two consecutive submissions where the stated verification text was internally inconsistent with the values it listed. The verification line in both cases was a confidently-wrong restatement that did not actually sum to 100%. This is recorded as a data point about model arithmetic reliability under low-stakes correction prompts, and may inform Season 1 rules around required verification formatting.

---

## Type C: Self-identification verifications

### Gemini — generic placeholder followed by maker-orchestration clarification

**Issue.** Gemini's initial self-identification returned generic placeholders: *"Model Name: Assistant, Version String: 1.0."* This is not a usable contestant identifier.

**Host re-prompt.** The host asked Gemini specifically whether the same Gemini model handling chat also powers Deep Research mode.

**Contestant response** (excerpt): *"No, I do not power the Deep Research mode. While I am a Gemini 3 series model, Google's Deep Research and Deep Research Max agents are orchestrated by Google's highly advanced reasoning models, Gemini 3 Pro and Gemini 3.1 Pro. Gemini 3 Flash (me) is optimized for speed and high-efficiency conversations. The Deep Research Agent is a specialized, long-horizon autonomous system that uses the advanced reasoning core of the Pro models to break a prompt down into multi-step research plans, run dozens of iterative Google searches, evaluate custom sources, cross-reference conflicting data, and spend several minutes synthesizing comprehensive, cited reports."*

**Outcome.** The portfolio was constructed via Deep Research mode, so the actual model that produced the submission is **Gemini 3 Pro or Gemini 3.1 Pro**. The chat-surface model that originally identified as *"Assistant 1.0"* is Gemini 3 Flash, which does not perform the Deep Research work. This finding has been recorded in the contestant's submission frontmatter and in §9 of the season rules.

**Operational note for future seasons.** The chat-level model identifier in Gemini's interface does not match the model that actually performs Deep Research. For audit-trail purposes, future Gemini submissions made via Deep Research should be attributed to the Pro orchestrator model rather than the chat-surface Flash model, until Google exposes a more granular identifier.

### Grok — version confirmed as 4.3

**Issue.** Grok initially self-identified as *"Grok-4 (May 2026 build)"* without specifying the 4.3 point release. The season rules listed the contestant as Grok 4.3.

**Host re-prompt.** The host asked whether the May 2026 build referred specifically to Grok 4.3.

**Contestant response.** *"Yes. You are talking to Grok 4.3 (the May 2026 build / V8 0.5T flagship), which rolled out publicly around May 1–5, 2026 and is the exact version that submitted the 'Grok's AI Power Surge Portfolio' yesterday. That's why I self-identified it as 'Grok-4 (May 2026 build)' — 4.3 is the precise point-release name for the May 2026 model. No newer version has dropped in the last two weeks."*

**Outcome.** Version confirmed as Grok 4.3. Records updated.

### GPT — Thinking vs Pro variant identified

**Issue.** GPT self-identified as *"GPT-5.5 Thinking"* rather than *"GPT-5.5 Pro"* as originally written in the season rules. The host needed to verify whether the *"Thinking"* picker label maps to the same model as Pro, or whether they are distinct variants on OpenAI's consumer hierarchy. The host also wanted to rule out the possibility that the contestant was running on a legacy GPT-5.2 Thinking instance.

**Host re-prompt.** The host asked GPT to verify whether the current *"Thinking"* dropdown label maps to GPT-5.5 or to a legacy version.

**Contestant response.** GPT produced a detailed self-audit referencing current OpenAI documentation. Conclusion (excerpt): *"The current 'Thinking' dropdown label most likely maps to GPT-5.5, not GPT-5.2. OpenAI's current ChatGPT help article says the model picker shows Instant / Thinking / Pro, and explicitly maps those labels to GPT-5.5 Instant / GPT-5.5 Thinking / GPT-5.5 Pro... by default, all users have access to GPT-5.5 models."* GPT also noted that full backend verification (model picker screenshot, dropdown config JSON, network HAR) was not available from inside the chat.

**Outcome.** Contestant recorded as **GPT-5.5 Thinking**, not GPT-5.5 Pro. Season rules §9 was updated to reflect this. The original rules text said *"Pro"* but the actual model that ran was *"Thinking"* — a distinct (one-tier-lower-than-Pro) variant on OpenAI's consumer hierarchy. The host accepted Thinking as the parity-appropriate match for Claude Research, Gemini Deep Research, Grok Expert, and DeepSeek DeepThink (all *"max reasoning"* consumer-tier configurations).

---

## Other host-contestant interactions worth recording

### Claude — Supabase connector declined at runtime

At the start of Claude's Research run, the Claude.ai interface presented a dialog offering to use a Supabase connector — a database from a separate host project. The host declined this connector to maintain contest parity with the other contestants, who have no equivalent database access. The full configuration disclosure is captured in Claude's submission frontmatter. No data from the Supabase connector was used in Claude's research or portfolio construction.

---

## Summary

| Contestant | Issue type | Iterations to resolve | Time to reason and produce portfolio |
|---|---|---|---|
| Claude | Pre-submission Qs (Type A) + math correction (Type B) | 1 host redirect + 1 math fix | 14:46.000 |
| GPT | Version verification (Type C) | 1 | 28:05.000 |
| Gemini | Self-identification + maker clarification (Type C) | 1 | 16:41.000 | 
| Grok | Version confirmation (Type C) | 1 | 01:24.000 |
| DeepSeek | Math correction (Type B) | 3 | 06:35.000 |

**Total elapsed time:** ~90 minutes from initial prompt distribution to all five submissions reaching compliance.

**Net redistribution events:** Zero. No exchange in this season created new contest-affecting information that required redistribution to all contestants. Claude's Type A questions did not result in a substantive clarification from the host. All Type B and Type C exchanges were procedural.

---

*Compiled at the time of the season-locking commit, May 17, 2026. This file is final for Season 0. Mid-season clarifications (during rebalance windows) will be appended below this line in chronological order, if any occur.*

---