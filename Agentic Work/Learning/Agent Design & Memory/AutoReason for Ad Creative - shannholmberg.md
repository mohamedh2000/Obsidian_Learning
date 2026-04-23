---
title: "AutoReason for Ad Creative"
url: "https://x.com/shannholmberg/status/2045537032387363257?s=42"
platform: twitter
date_saved: 2026-04-23
source: "Shann³ (@shannholmberg)"
content_type: guide
topics: [Agent Design, Adversarial Agents, Marketing Automation]
tags: [autoreason, ad-creative, multi-agent, meta-ads]
status: unread
---

> AutoReason uses adversarial isolation with fresh agents to improve ad creative. Each role is a blind agent that can't see what others wrote.

| Metric | Count |
|--------|-------|
| Likes | 608 |
| Retweets | 46 |

**Topics:** [[Agent Design]], [[Adversarial Agents]], [[Marketing Automation]]

## Key Points
- **Adversarial isolation**: Every role is a fresh agent that can't see what others wrote
- **Incumbent A**: Current best ad that's live and spending
- **The Critic**: Fresh agent tears apart incumbent using knowledge layer (50 ads, audience language, competitor ads, swipe file)
- **Author B**: Blind agent only sees teardown, writes rival from scratch
- **The Synthesizer**: Produces three candidates: A unchanged, AB merged, B as-is
- **Judge Panel**: 3 blind agents score using Borda count
- **K=2 stopping**: If A wins twice in a row, system stops
- Knowledge layer includes CTR/CPA data, winning patterns, customer language, competitor ads, swipe file

## Architecture
```
[Incumbent A] → [Critic Agent] → [Teardown]
                                     ↓
                              [Author B (blind)]
                                     ↓
                              [Rival Version]
                                     ↓
                              [Synthesizer]
                               ├─ A unchanged
                               ├─ AB merged
                               └─ B as-is
                                     ↓
                              [3 Judge Agents]
                                     ↓
                              [Borda Count Score]
                                     ↓
                              [Winner → New Incumbent]
```

*Filed in: [[Saved Links MOC]]*
