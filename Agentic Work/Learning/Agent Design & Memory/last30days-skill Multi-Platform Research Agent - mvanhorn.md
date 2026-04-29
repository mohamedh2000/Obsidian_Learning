---
title: "last30days-skill Multi-Platform Research Agent"
url: "https://github.com/mvanhorn/last30days-skill"
platform: github
date_saved: 2026-01-26
source: "mvanhorn"
content_type: repo
topics: [Agent Design, Research Tools]
tags: [ai-skill, research-automation, multi-platform, reddit, twitter, youtube, hacker-news, polymarket, engagement-ranking]
status: unread
---

> An AI agent skill that conducts multi-platform research on any topic, synthesizing findings from Reddit, X/Twitter, YouTube, TikTok, Hacker News, Polymarket, and GitHub — ranking by actual engagement rather than algorithmic relevance.

| | |
|---|---|
| **Source** | mvanhorn |
| **Saved** | 2026-01-26 |
| **Type** | Repository |
| **Language** | Python 3.12+ (98.8%) |
| **Tests** | 1,012 passing |
| **URL** | [Link](https://github.com/mvanhorn/last30days-skill) |

**Topics:** [[Agent Design & Memory]], [[Developer Tools]]

## Key Points

- **Intelligent pre-search resolution**: Automatically identifies relevant handles, subreddits, hashtags, and communities before querying
- **Cross-source clustering**: Merges duplicate stories appearing across multiple platforms into single entries
- **Engagement-based ranking**: Scores content by upvotes, likes, view counts, and Polymarket odds rather than algorithmic curation
- **Multi-source synthesis**: Provides full YouTube transcripts, Reddit comment threads with vote counts, and prediction market odds

### Architecture Patterns

- **Bring-your-own-keys**: Leverages user-provided credentials to access otherwise siloed platforms
- **Parallel API orchestration**: Searches multiple sources concurrently rather than serially
- **Entity disambiguation**: Resolves ambiguous terms bidirectionally (person↔company, product↔founder)
- **Resilient degradation**: Timeout budgets prevent slow sources from blocking entire runs

### Features

- **Person-mode for GitHub**: Pulls PR velocity, merge rates, and recent shipping activity when researching individuals
- **ELI5 mode**: Rewrites technical findings in plain language while preserving citations
- Uses yt-dlp for YouTube transcripts, vendored Bird client for X search, ScrapeCreators API for social platforms

*Filed in: [[Saved Links MOC]]*
