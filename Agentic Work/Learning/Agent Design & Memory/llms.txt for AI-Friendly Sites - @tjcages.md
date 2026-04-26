---
title: "llms.txt for AI-Friendly Sites"
url: "https://x.com/tjcages/status/2018859145366303158?s=42"
platform: twitter
date_saved: 2026-04-05
source: "ty (@tjcages)"
content_type: tweet
topics: [Agent Design, Context Engineering]
tags: [llms-txt, ai-friendly, markdown, sitemap, web-standards, agent-navigation, documentation]
status: unread
---

> Important for AI-friendly sites to have auto-generating markdown for every page route. llms.txt acts as a sitemap, pointing agents to each .md path for seamless navigation. AI-friendly by default.

| Metric | Count |
|--------|-------|
| Likes | 136 |
| Retweets | 5 |

**Topics:** [[Agent Design]], [[Context Engineering]]

## Key Points

- **Auto-generating markdown per route**: Every page on an AI-friendly site should automatically produce a markdown representation—no manual content duplication
- **llms.txt as agent sitemap**: Functions like robots.txt but for AI agents, providing an index of all available .md paths the agent can navigate
- **Seamless agent navigation**: Agents can discover content programmatically rather than parsing HTML or guessing URL structures
- **AI-friendly by default**: Sites should build this into their infrastructure from the start rather than retrofitting later

### Implementation Pattern

```
site.com/
├── llms.txt              ← Agent sitemap index
├── docs/
│   ├── intro.md          ← Linked from llms.txt
│   ├── api-reference.md
│   └── guides/
│       └── quickstart.md
└── blog/
    └── 2026-04-05-post.md
```

The llms.txt file acts as the discovery layer:
```
# Site: example.com
# Description: Product documentation

/docs/intro.md
/docs/api-reference.md
/docs/guides/quickstart.md
/blog/2026-04-05-post.md
```

This pattern complements content negotiation (serving markdown via `Accept: text/markdown`) by providing upfront discoverability for agents crawling the site.

*Filed in: [[Saved Links MOC]]*
