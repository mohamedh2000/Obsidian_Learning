---
title: "Firecrawl CLI Skill for AI Agent Web Context"
url: "https://x.com/sumanth_077/status/2017223042024501457?s=42"
platform: twitter
date_saved: 2026-01-30
source: "Sumanth (@sumanth_077)"
content_type: tweet
topics: [Developer Tools, Agent Design]
tags: [firecrawl, web-scraping, cli, claude-code, codex, web-context, token-efficiency, javascript-rendering, agent-tools]
status: unread
---

> Firecrawl CLI and skill for AI agents — pulls clean, structured web content locally for maximum token efficiency. Install with `npx skills add firecrawl/cli`.

| Metric | Count |
|--------|-------|
| Likes | 346 |
| Retweets | 50 |

**Topics:** [[Developer Tools]], [[Agent Design & Memory]]

## Key Points
- Most AI agents struggle with web context: unreliable scrapers, API rate limits, wasted tokens on unstructured HTML
- Firecrawl CLI extracts clean markdown/HTML directly to local files via bash commands — token efficient
- Four core operations: **Scrape** (extract clean content with `--only-main-content`), **Search** (query web + scrape results), **Map** (discover all URLs on a site), **Crawl** (process entire websites with depth limits)
- Advanced features: JavaScript rendering with configurable wait times, screenshot capture, tag-level HTML control, multiple output formats (markdown, HTML, JSON, links)

### Key Capabilities
- `--only-main-content` flag removes navigation and ads automatically
- Rate limiting and path filters for respectful crawling
- Sitemap handling for comprehensive site mapping
- Bash-powered design means seamless integration with any agent that can run shell commands

### Why It Matters
Web context is a common agent bottleneck. Clean, structured content + local file storage = more context budget for reasoning instead of parsing HTML soup.

*Filed in: [[Saved Links MOC]]*
