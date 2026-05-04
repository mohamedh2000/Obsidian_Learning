---
title: "Codex Plugin CC Adversarial Review - @nicos_ai"
url: "https://x.com/nicos_ai/status/2050891933728354717"
platform: twitter
date_saved: 2026-05-03
source: "Nico (@nicos_ai)"
content_type: guide
topics: [codex, claude-code, plugin, code-review]
tags: [twitter, ai, dev-tools]
status: unread
---

# Codex Plugin CC Adversarial Review - @nicos_ai

> Si usas Claude Code, deja de buscar "el mejor modelo". La clave ahora es hacer que se contradigan — Claude builds, Codex breaks.

| | |
|---|---|
| **Source** | Nico (@nicos_ai) |
| **Saved** | 2026-05-03 |
| **Type** | guide |
| **Engagement** | 211 likes, 26 retweets |
| **URL** | [Link](https://x.com/nicos_ai/status/2050891933728354717) |

## Topics

[[Code Review]] | [[Developer Tools]]

## Key Points

**Plugin Commands:**
- `/codex:review` — Reviews diffs or uncommitted changes
- `/codex:adversarial-review` — Doesn't correct, just questions ("Why this caching?", "Any race conditions?"). Can be guided with instructions.
- `/codex:rescue` — When Claude fails, Codex continues (--resume included)

**Review Gate:**
- Automatic review gate: Claude writes → Codex validates → blocks if it sees problems
- Critical for auth, infra, and migrations

**Philosophy:**
- Claude construye (builds), Codex rompe (breaks)
- Making models contradict each other is more robust than finding the "best model"

## Notes

(Personal annotations)

---

*Filed in: [[Twitter Posts MOC]] | [[Saved Links MOC]]*
