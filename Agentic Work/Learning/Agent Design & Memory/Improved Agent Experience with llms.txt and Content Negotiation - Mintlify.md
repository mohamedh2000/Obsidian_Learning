---
title: "Improved Agent Experience with llms.txt and Content Negotiation"
url: "https://www.mintlify.com/blog/context-for-agents"
platform: web
date_saved: 2026-04-03
source: "Peri Langlois (@mintlify)"
content_type: guide
topics: [Agent Design, Context Engineering]
tags: [llms-txt, content-negotiation, ai-agents, documentation, http-headers, token-efficiency, markdown]
status: unread
---

> Content negotiation via HTTP `Accept` headers enables documentation platforms to serve clean Markdown to AI agents while preserving styled HTML for humans—reducing token consumption by approximately 30x.

| Metric | Value |
|--------|-------|
| Author | Peri Langlois |
| Published | January 29, 2026 |
| Reading Time | 3 min |

**Topics:** [[Agent Design]], [[Context Engineering]]

## Key Points

- **Content negotiation mechanism**: When agents request documentation with `Accept: text/markdown`, they receive stripped-down Markdown rather than HTML with presentational overhead—single URLs serve both audiences
- **llms.txt placement strategy**: Instructional blockquotes moved from page footers to headers ensures AI systems see guidance before truncating long content to preserve context windows
- **HTTP header discovery**: `Link` headers advertise `llms.txt` and `llms-full.txt` indices; `X-Llms-Txt` headers provide simpler single-value alternatives; `X-Robots-Tag: noindex, nofollow` prevents search engines from indexing Markdown variants
- **Infrastructure-level implementation**: All pages return these headers automatically at middleware level, eliminating manual implementation overhead for documentation teams

### How It Works

```
┌─────────────────── REQUEST ───────────────────┐
│  Accept: text/html     → Styled HTML page     │
│  Accept: text/markdown → Clean Markdown       │
└───────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────── HTTP HEADERS ──────────────────┐
│  Link: <llms.txt>; rel="llms-txt"             │
│  Link: <llms-full.txt>; rel="llms-full-txt"   │
│  X-Llms-Txt: /llms.txt                        │
│  X-Robots-Tag: noindex, nofollow (for .md)    │
└───────────────────────────────────────────────┘
```

The approach achieves approximately **30x token reduction** by stripping HTML tags, attributes, and styles while maintaining semantic content. This enables AI agents to consume more documentation within their context windows without sacrificing the visual experience for human readers.

*Filed in: [[Saved Links MOC]]*
