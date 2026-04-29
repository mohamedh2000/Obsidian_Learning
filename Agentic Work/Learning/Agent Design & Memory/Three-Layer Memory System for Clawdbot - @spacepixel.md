---
title: "Three-Layer Memory System for Clawdbot"
url: "https://x.com/spacepixel/status/2015967798636556777?s=42"
platform: twitter
date_saved: 2026-01-28
source: "pixel (@spacepixel)"
content_type: tweet
topics: [Agent Memory, Knowledge Graphs, Self-Improving Systems]
tags: [ai-agents, memory-systems, knowledge-graph, claude-code, clawdbot, self-evolution, zettelkasten, cron-jobs]
status: unread
---

> Give your Clawdbot a knowledge graph that compounds forever. Most AI assistants forget by default. Clawdbot doesn't—but out of the box, its memory is still static. This guide upgrades Clawdbot's memory into a self-maintaining, compounding knowledge graph that evolves automatically as your life changes.

| Metric | Count |
|--------|-------|
| Likes | 1,700+ |
| Retweets | 137 |

**Topics:** [[Agent Memory]], [[Knowledge Graphs]], [[Self-Improving Systems]]

## Key Points
- **Static Memory Problem**: Out-of-the-box Clawdbot memory (AGENTS.md, MEMORY.md) is static and requires manual maintenance — leads to stale context like "your boss Sarah is difficult" persisting months after changing jobs
- **Automatic Fact Extraction**: Every ~30 minutes, a cheap sub-agent scans conversations and saves durable facts — costs pennies per day and removes manual context management burden
- **Entity-Based Storage**: Facts stored by person/company/project in `/life/areas/` rather than dumped into a monolithic blob — enables targeted retrieval and relationship mapping
- **Weekly Synthesis Cron**: Sunday cron job rewrites summaries from raw facts and prunes stale context automatically — prevents context rot without manual intervention
- **Superseding Not Deleting**: When facts change, old ones are marked historical rather than deleted — preserves full history for temporal queries ("what did I think about X in March?")

### The Three-Layer Architecture

```
Layer 1: Knowledge Graph   (/life/areas/)
  └── Entities with atomic facts + living summaries

Layer 2: Daily Notes       (memory/YYYY-MM-DD.md)
  └── Raw event logs — what happened, when

Layer 3: Tacit Knowledge   (MEMORY.md)
  └── Patterns, preferences, lessons learned
```

### Atomic Facts Structure
Every fact is stored as a discrete `items.json` entry within entity folders like `/life/areas/people/sarah/items.json`. This enables surgical retrieval — "what do I know about Sarah?" returns only relevant facts, not the entire memory blob.

### Why This Matters
This shifts agent memory from "I told it once" to "it compounds what it learns." The system turns every conversation into potential persistent knowledge while automatically handling the housekeeping humans forget to do.

*Filed in: [[Twitter Posts MOC]] | [[Learning MOC]] | [[Saved Links MOC]]*
