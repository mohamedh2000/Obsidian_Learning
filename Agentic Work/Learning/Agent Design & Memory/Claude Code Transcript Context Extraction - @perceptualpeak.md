---
title: "Claude Code Transcript Context Extraction"
url: "https://x.com/perceptualpeak/status/2016687203796341173?s=42"
platform: twitter
date_saved: 2026-01-29
source: "Zac (@perceptualpeak)"
content_type: tweet
topics: [Claude Code, Context Engineering]
tags: [claude-code, transcripts, context-window, jsonl, markdown-conversion, session-history, token-optimization]
status: unread
---

> CLAUDE CODE TIP: If you've ever tried to get Claude to reference/consume transcripts from previous chat sessions... you'll exhaust your context window well before it's even halfway done evaluating the transcript.

| Metric | Count |
|--------|-------|
| Likes | 47 |
| Retweets | 5 |

**Topics:** [[Claude Code]], [[Context Engineering]]

## Key Points
- **98% size reduction**: Raw 1.9 MB transcript → 43.6 KB converted markdown — maintains all actionable data
- **Problem**: Raw `.jsonl` transcripts are too large to fit in context window — Claude exhausts context before processing
- **Solution prompt**: "Before you review the transcript, please convert the raw .jsonl transcript file to markdown format, extracting only the user messages, system messages, and thinking blocks"
- **What gets dropped**: Tool outputs, intermediate responses, metadata — only decision-relevant content retained
- **Enables cross-session continuity**: Previous sessions become practical sources of context instead of theoretical ones

### Conversion Workflow
```
RAW TRANSCRIPT (.jsonl)          CONVERTED (markdown)
──────────────────────          ─────────────────────
1.9 MB                    →      43.6 KB
Tool outputs              →      [dropped]
Intermediate responses    →      [dropped]
User messages            →      [kept]
System messages          →      [kept]
Thinking blocks          →      [kept]
```

### When to Use This
- Extracting context from long past sessions
- Building session summaries for handoff
- Creating training data from real conversations
- Debugging what went wrong in a failed session

*Filed in: [[Saved Links MOC]]*
