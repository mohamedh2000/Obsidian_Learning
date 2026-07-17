---
title: "Prompting Claude Sonnet 5 — Behavioral Differences & Patterns"
url: "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5"
platform: web
date_saved: 2026-06-30
source: "Anthropic (platform.claude.com docs)"
content_type: guide
topics: [prompt-engineering, claude-sonnet-5]
tags: [anthropic, prompt-engineering, claude-sonnet-5, effort, adaptive-thinking, migration]
status: unread
---

# Prompting Claude Sonnet 5 — Behavioral Differences & Patterns

> Prompting patterns specific to Claude Sonnet 5 — effort, adaptive-thinking defaults, tool use, literal instruction-following, and migration from Sonnet 4.6.

| | |
|---|---|
| **Source** | Anthropic (platform.claude.com docs) |
| **Saved** | 2026-06-30 |
| **Type** | guide |
| **URL** | [Link](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) |

## Topics

[[Prompt Engineering]] | [[Claude Sonnet 5]]

## Key Points

- **Response length is task-calibrated:** shorter on simple lookups, longer on open-ended analysis; add explicit concision instructions if your product needs a fixed verbosity (positive examples beat negative ones)
- **Effort defaults to `high`;** raise to `xhigh` for the hardest coding/agentic tasks. Sonnet 5 respects effort strictly at the low end — fix shallow reasoning by raising effort, not prompting around it
- **Adaptive thinking is on by default** (a change from Sonnet 4.6); manual extended thinking (`budget_tokens`) is removed and returns 400. Leave `max_tokens` headroom — the new tokenizer produces ~30% more tokens
- **More agentic + more literal:** reaches for tools and self-verification more readily; interprets instructions literally and won't generalize scope — state scope explicitly ("apply to every section, not just the first")
- **Migration constraints:** `temperature`/`top_p`/`top_k` non-default values return 400 — use system-prompt instructions for tone/variety instead. Code-review harnesses may show lower recall (a harness effect); prompt for coverage over filtering. Supports `computer_20251124` computer-use tool

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
