---
title: "Agentation Visual Feedback Tool for Agents"
url: "https://x.com/benjitaylor/status/2014109590972145908?s=42"
platform: twitter
date_saved: 2026-01-22
source: "Benji Taylor (@benjitaylor)"
content_type: tweet
topics: [Agent Tools, Browser Agents]
tags: [agentation, npm, visual-feedback, element-selectors, browser-automation, ai-agents, debugging]
status: unread
---

> Benji Taylor launches Agentation — a visual feedback tool that lets users click elements and add notes, then copies structured markdown with element paths, selectors, and positions for agents to find and fix things.

| Metric | Count |
|--------|-------|
| Likes | 4515 |
| Retweets | 411 |

**Topics:** [[Agent Tools]], [[Browser Agents]]

## Key Points
- **Click-to-Annotate Interface**: Users click elements directly in the browser, add notes, and the tool captures all technical metadata agents need to locate those elements
- **Structured Agent Output**: Copies as markdown with element paths, CSS selectors, and positions — format designed for LLM consumption, not human reading
- **npm Package Distribution**: `npm i agentation` — drop-in installation for any JavaScript project
- **Bridges Human-Agent Communication**: Solves the "pointing at pixels" problem — humans see visually, agents need selectors and paths

### How It Works
```
User Interaction → Agent Input Pipeline:
┌────────────────────────────────────┐
│  1. User clicks element on page    │
│          ↓                         │
│  2. User adds annotation/note      │
│          ↓                         │
│  3. Agentation captures:           │
│     - Element path (DOM tree)      │
│     - CSS selectors                │
│     - Bounding box positions       │
│     - User's annotation            │
│          ↓                         │
│  4. Copy as structured markdown    │
│          ↓                         │
│  5. Paste to agent (Claude, etc.)  │
└────────────────────────────────────┘
```

### Why This Matters
One of the hardest parts of agent-assisted frontend work is communicating *which* element has the issue. Screenshots alone don't give agents actionable selectors. Agentation provides the missing translation layer — humans point, agents receive structured locators.

*Filed in: [[Saved Links MOC]]*
