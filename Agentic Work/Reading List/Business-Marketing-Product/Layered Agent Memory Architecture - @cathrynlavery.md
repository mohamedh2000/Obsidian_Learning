---
title: "Layered Agent Memory Architecture - @cathrynlavery"
url: "https://x.com/cathrynlavery/status/2023208962762445063"
platform: twitter
date_saved: 2026-02-15
source: "Cathryn (@cathrynlavery)"
content_type: tutorial
topics: [agent-memory, markdown-files, context-management]
tags: [twitter, business]
status: unread
---

# Layered Agent Memory Architecture - @cathrynlavery

> Layered memory files in the agent workspace. MEMORY.md for long-term curated knowledge, daily files in memory/ for raw context, and AGENTS.md for standing instructions. The agent reads these on every session start. No vector DB needed, just flat markdown files the agent reads and writes to. The memory_search hook handles semantic recall across all of them.

| | |
|---|---|
| **Source** | Cathryn (@cathrynlavery) |
| **Saved** | 2026-02-15 |
| **Type** | tutorial |
| **Engagement** | 124 likes, 5 retweets |
| **URL** | [Link](https://x.com/cathrynlavery/status/2023208962762445063) |

## Topics

[[AI Agents]] | [[Developer Tools]]

## Key Points

- Three-layer memory: MEMORY.md (long-term), daily files in memory/ (raw context), AGENTS.md (instructions)
- No vector DB needed - flat markdown files with semantic recall via memory_search hook
- Enable compaction.memoryFlush.enabled to auto-save before context trimming

## Notes

(Personal annotations)

---

*Filed in: [[Saved Links MOC]]*
